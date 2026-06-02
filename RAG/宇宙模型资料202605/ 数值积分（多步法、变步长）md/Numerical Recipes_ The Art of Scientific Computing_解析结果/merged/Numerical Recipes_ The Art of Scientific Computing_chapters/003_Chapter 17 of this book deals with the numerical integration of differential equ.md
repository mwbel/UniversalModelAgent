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


<!-- chunk 0004: pages 211-280 -->
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

Convergence acceleration of a sequence by the 
 algorithm. Initialize by calling the constructor with arguments nmax, an upper bound on the number of terms to be summed, and epss, the desired accuracy. Then make successive calls to the function next, with argument the next partial sum of the sequence. The current estimate of the limit of the sequence is returned by next. The flag cnvgd is set when convergence is detected.

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


<!-- chunk 0005: pages 281-350 -->
$\epsilon$ . For $N = 1 4$ , and a certain set of $c$ ’s and $\gamma$ (calculated by P. Godfrey), the error is smaller than $| \epsilon | < 1 0 ^ { - 1 5 }$ . Even more impressive is the fact that, with these same constants, the formula (6.1.5) applies for the complex gamma function, everywhere in the half complex plane Re $z > 0$ , achieving almost the same accuracy as on the real line.

It is better to implement $\ln \Gamma ( x )$ than $\Gamma ( x )$ , since the latter will overflow at quite modest values of $x$ . Often the gamma function is used in calculations where the large values of $\Gamma ( x )$ are divided by other large numbers, with the result being a perfectly ordinary value. Such operations would normally be coded as subtraction of logarithms. With (6.1.5) in hand, we can compute the logarithm of the gamma function with two calls to a logarithm and a few dozen arithmetic operations. This makes it not much more difficult than other built-in functions that we take for granted, such as sin $x$ or $e ^ { x }$ :

Doub gammln(const Doub xx) {   
Returns the value $\ln [ \Gamma ( \mathbf { x x } ) ]$ for $\mathbf { x x } > \mathbf { 0 }$ . Int j; Doub x,tmp,y,ser; static const Doub cof[14] $=$ {57.1562356658629235,-59.5979603554754912, 14.1360979747417471,-0.491913816097620199,.339946499848118887e-4, .465236289270485756e-4,-.983744753048795646e-4,.158088703224912494e-3, -.210264441724104883e-3,.217439618115212643e-3,-.164318106536763890e-3, .844182239838527433e-4,-.261908384015814087e-4,.368991826595316234e-5}; if (xx $\mathit { \Theta } < = \mathit { \Theta } 0 .$ ) throw("bad arg in gammln"); $\mathbf { y } = \mathbf { x } = \mathbf { x } \mathbf { x }$ ; tmp $= \ x + 5$ .24218750000000000; Rational 671/128. tmp $=$ ( $\mathbf { \boldsymbol { x } } { + } 0$ .5)\*log(tmp)-tmp; ser $=$ 0.999999999999997092; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<14;j $^ { + + }$ ) ser $+ =$ cof[j]/++y; return tmp+log(2.5066282746310005\*ser/x);   
}

How shall we write a routine for the factorial function $n ! 2$ Generally the factorial function will be called for small integer values, and in most applications the same integer value will be called for many times. It is obviously inefficient to call $\exp ( \mathrm { g a m m l n } ( \mathbf { n } + 1 . ) )$ for each required factorial. Better is to initialize a static table on the first call, and do a fast lookup on subsequent calls. The fixed size 171 for the table is because 170Š is representable as an IEEE double precision value, but 171Š overflows. It is also sometimes useful to know that factorials up to 22Š have exact double precision representations (52 bits of mantissa, not counting powers of two that are absorbed into the exponent), while 23Š and above are represented only approximately.

# gamma.h

Doub factrl(const Int n) {   
Returns the value nŠ as a floating-point number. static VecDoub a(171); static Bool init=true; if (init) { init $=$ false; $\mathrm { a } \left[ 0 \right] ~ = ~ 1 . ~ ;$ ; for (Int i=1;i<171;i++) a[i] $=$ i\*a[i-1]; } if (n < 0 || n > 170) throw("factrl out of range"); return a[n];

More useful in practice is a function returning the log of a factorial, which doesn’t have overflow issues. The size of the table of logarithms is whatever you can afford in space and initialization time. The value $\mathtt { N T O P } = 2 0 0 0$ should be increased if your integer arguments are often larger.

# gamma.h

Doub factln(const Int n) {Returns ln.nŠ/.

static const Int NTOP $^ { \prime } =$ 2000;   
static VecDoub a(NTOP);   
static Bool init=true;   
if (init) { init $=$ false; for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<NTOP; $\Dot { \ b { 1 } } + +$ ) a[i] $=$ gammln(i+1.);   
}   
if $\mathbf { \Omega } _ { \mathbf { \lambda } } \mathbf { \hat { n } \Sigma } < \mathbf { \Omega } 0 \mathbf { \dot { \Omega } } .$ ) throw("negative arg in factln");   
if $\mathrm { ~ \textit ~ { ~ a ~ } ~ } <$ NTOP) return a[n];   
return gammln $( \mathtt { n } + 1 . )$ ; Out of range of table.

}

The binomial coefficient is defined by

$$
{ \binom { n } { k } } = { \frac { n ! } { k ! ( n - k ) ! } } \qquad 0 \leq k \leq n
$$

A routine that takes advantage of the tables stored in factrl and factln is

Doub bico(const Int n, const Int k) {

Returns the binomial coefficient $\textstyle { \binom { n } { k } }$ as a floating-point number.

if (n<0 || $\mathtt { k } < 0$ || k>n) throw("bad args in bico");   
if ( $\scriptstyle \mathtt { n } < 1 7 1 $ ) return floor(0.5+factrl(n)/(factrl(k)\*factrl(n-k)));   
return floor(0. $^ { 5 + }$ exp(factln(n)-factln(k)-factln(n-k)));

The floor function cleans up roundoff error for smaller values of $\mathbf { n }$ and k.

If your problem requires a series of related binomial coefficients, a good idea is to use recurrence relations, for example,

$$
{ \begin{array} { l } { \displaystyle { \binom { n + 1 } { k } } = { \frac { n + 1 } { n - k + 1 } } { \binom { n } { k } } = { \binom { n } { k } } + { \binom { n } { k - 1 } } } \\ { \displaystyle { \binom { n } { k + 1 } } = { \frac { n - k } { k + 1 } } { \binom { n } { k } } } \end{array} }
$$

Finally, turning away from the combinatorial functions with integer-valued arguments, we come to the beta function,

$$
B ( z , w ) = B ( w , z ) = \int _ { 0 } ^ { 1 } t ^ { z - 1 } ( 1 - t ) ^ { w - 1 } d t
$$

which is related to the gamma function by

$$
B ( z , w ) = { \frac { \Gamma ( z ) \Gamma ( w ) } { \Gamma ( z + w ) } }
$$

hence

Doub beta(const Doub z, const Doub w) { Returns the value of the beta function $B ( z , w )$ . return exp(gammln(z)+gammln(w)-gammln $( z + \pi )$ ); }

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 6.   
Lanczos, C. 1964, “A Precision Approximation of the Gamma Function,” SIAM Journal on Numerical Analysis,ser. B,vol.1,pp.86-96.[1]

# 6.2 Incomplete Gamma Function and Error Function

The incomplete gamma function is defined by

$$
P ( a , x ) \equiv \frac { \gamma ( a , x ) } { \Gamma ( a ) } \equiv \frac { 1 } { \Gamma ( a ) } \int _ { 0 } ^ { x } e ^ { - t } t ^ { a - 1 } d t \qquad ( a > 0 )
$$

It has the limiting values

$$
P ( a , 0 ) = 0 \qquad \mathrm { a n d } \qquad P ( a , \infty ) = 1
$$

The incomplete gamma function $P ( \boldsymbol { a } , \boldsymbol { x } )$ is monotonic and (for $a$ greater than one or so) rises from “near-zero” to “near-unity” in a range of $x$ centered on about $a - 1$ , and of width about $\sqrt { a }$ (see Figure 6.2.1).

The complement of $P ( \boldsymbol { a } , \boldsymbol { x } )$ is also confusingly called an incomplete gamma function,

$$
Q ( a , x ) \equiv 1 - P ( a , x ) \equiv \frac { \Gamma ( a , x ) } { \Gamma ( a ) } \equiv \frac { 1 } { \Gamma ( a ) } \int _ { x } ^ { \infty } e ^ { - t } t ^ { a - 1 } d t \qquad ( a > 0 )
$$

It has the limiting values

$$
\ Q ( a , 0 ) = 1 \qquad \mathrm { a n d } \qquad Q ( a , \infty ) = 0
$$

The notations $P ( a , x ) , \gamma ( a , x )$ , and $\Gamma ( a , x )$ are standard; the notation $Q ( a , x )$ is specific to this book.

There is a series development for $\gamma ( a , x )$ as follows:

$$
\gamma ( a , x ) = e ^ { - x } x ^ { a } \sum _ { n = 0 } ^ { \infty } \frac { \Gamma ( a ) } { \Gamma ( a + 1 + n ) } x ^ { n }
$$

One does not actually need to compute a new $\Gamma ( a + 1 + n )$ for each $n$ ; one rather uses equation (6.1.3) and the previous coefficient.

![](images/c20552309628f7ab821814fcd55d01476a945adaab277bd68eed882860956a95.jpg)  
Figure 6.2.1. The incomplete gamma function $P ( \boldsymbol a , x )$ for four values of $^ { a }$ .

A continued fraction development for $\Gamma ( a , x )$ is

$$
\Gamma ( a , x ) = e ^ { - x } x ^ { a } \left( { \frac { 1 } { x + } } { \frac { 1 - a } { 1 + } } { \frac { 1 } { x + } } { \frac { 2 - a } { 1 + } } { \frac { 2 } { x + } } \cdots \right) \qquad ( x > 0 )
$$

It is computationally better to use the even part of (6.2.6), which converges twice as fast (see $\ S 5 . 2 )$ :

$$
\Gamma ( a , x ) = e ^ { - x } x ^ { a } \left( { \frac { 1 } { x + 1 - a - } } { \frac { 1 \cdot ( 1 - a ) } { x + 3 - a - } } { \frac { 2 \cdot ( 2 - a ) } { x + 5 - a - } } \cdots \right) \qquad ( x > 0 )
$$

It turns out that (6.2.5) converges rapidly for $x$ less than about $a + 1$ , while (6.2.6) or (6.2.7) converges rapidly for $x$ greater than about $a + 1$ . In these respective regimes each requires at most a few times $\sqrt { a }$ terms to converge, and this many only near $x = a$ , where the incomplete gamma functions are varying most rapidly. For moderate values of $a$ , less than 100, say, (6.2.5) and (6.2.7) together allow evaluation of the function for all $x$ . An extra dividend is that we never need to compute a function value near zero by subtracting two nearly equal numbers.

Some applications require $P ( \boldsymbol { a } , \boldsymbol { x } )$ and $Q ( a , x )$ for much larger values of $a$ , where both the series and the continued fraction are inefficient. In this regime, however, the integrand in equation (6.2.1) falls off sharply in both directions from its peak, within a few times $\sqrt { a }$ . An efficient procedure is to evaluate the integral directly, with a single step of high-order Gauss-Legendre quadrature (-4.6) extending from $x$ just far enough into the nearest tail to achieve negligible values of the integrand. Actually it is “half a step,” because we need the dense abscissas only near $x$ , not far out on the tail where the integrand is effectively zero.

We package the various incomplete gamma parts into an object Gamma. The only persistent state is the value $\mathtt { g l n }$ , which is set to $\Gamma ( a )$ for the most recent call to $P ( \boldsymbol { a } , \boldsymbol { x } )$ or $Q ( a , x )$ . This is useful when you need a different normalization convention, for example $\gamma ( a , x )$ or $\Gamma ( a , x )$ in equations (6.2.1) or (6.2.3).

# struct Gamma : Gauleg18 {

Object for incomplete gamma function. Gauleg18 provides coefficients for Gauss-Legendre quadrature.

static const Int ASWITCH $\mathop {    }$ 100;   
static const Doub EPS;   
static const Doub FPMIN;   
Doub gln; When to switch to quadrature method.   
See end of struct for initializations.

Doub gammp(const Doub a, const Doub x) { Returns the incomplete gamma function $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ .

if $( \texttt { x < 0 . 0 ~ } | \texttt { | a < = 0 . 0 } )$ throw("bad args in gammp"); if ( $\mathbf { \bar { x } } \ = = \ 0 . 0$ ) return 0.0; else if ((Int)a $> =$ ASWITCH) return gammpapprox $( \mathsf { a } , \mathsf { x } , 1 )$ ; Quadrature. else if $\mathit { \Pi } _ { \overline { { \mathbf { X } } } } ^ { ' } \ < \ \mathtt { a } + 1 . 0$ ) return gser(a,x); Use the series representation. else return 1.0-gcf(a,x); Use the continued fraction representation. L

Doub gammq(const Doub a, const Doub x) { Returns the incomplete gamma function $Q ( a , x ) \equiv 1 - P ( a , x )$ .

if $\mathit { \Omega } \left( \mathbf { x } \ < \ 0 . 0 \right.$ | $| \mathrm { ~  ~ a ~ } < = 0 . 0 \dot { } .$ ) throw("bad args in gammq");   
if $\mathit { \textbf { \xi } } _ { \mathbf { X } } = = \ 0 . 0 $ ) return 1.0;   
else if ((Int)a $> =$ ASWITCH) return gammpapprox $( \mathtt { a } , \mathtt { x } , 0 )$ ; Quadrature.   
else if $( \mathbf { x } ~ < ~ \mathsf { a } + 1 . 0 ) ^ { \dagger }$ ) return 1.0-gser(a,x); Use the series representation.   
else return gcf(a,x); Use the continued fraction representation.

# }

# Doub gser(const Doub a, const Doub x) {

Returns the incomplete gamma function $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ evaluated by its series representation.   
Also sets ln $\Gamma ( a )$ as $\mathtt { g l n }$ . User should not call directly.

Doub sum,del,ap; gln=gammln(a); $\mathtt { a p - a }$ ; del $\cdot ^ { = }$ sum=1.0/a; for (;;) { ++ap; del $\ast =$ x/ap; sum $+ =$ del; if (fabs(del) $<$ fabs(sum) $^ *$ EPS) { return sum\*exp(-x+a\*log(x)-gln); } } }

# Doub gcf(const Doub a, const Doub x) {

Returns the incomplete gamma function $Q ( a , x )$ evaluated by its continued fraction representation. Also sets ln $\Gamma ( a )$ as $\mathtt { g l n }$ . User should not call directly.

Int i;   
Doub an,b,c,d,del,h;   
gln=gammln(a);   
$\mathtt { b { = } x { + } 1 } . 0 { - } \mathtt { a }$ ;   
$\mathtt { C } = 1$ .0/FPMIN;   
${ \tt d } = 1$ .0/b;   
$\mathtt { h } { = } \mathtt { d }$ ;   
for ( $\scriptstyle \dot { \mathtt { 1 } } = 1$ ;;i++) { $\mathrm { { a n \ = \ - i * ( i - a ) \ ; } }$ ; b $+ = ~ 2 . 0$ ; d=an\*d+b;

Set up for evaluating continued fraction by modified Lentz’s method (-5.2) with $b _ { 0 } = \mathbf { 0 }$ .

Iterate to convergence.

if (fabs(d) $<$ FPMIN) $\mathtt { d } =$ FPMIN; c=b+an/c; if (fabs(c) $<$ FPMIN) $c =$ FPMIN; $\mathrm { d } { = } 1$ .0/d; del=d\*c; h $\ast =$ del; if (fabs(del-1.0) $< =$ EPS) break;   
}   
return $\exp \left( - \mathrm { { x } + \mathrm { { a } * 1 0 g } \left( \mathrm { { x } } \right) - \mathrm { { g } 1 n } } \right) * \mathrm { { h } }$ ; Put factors in front. Doub gammpapprox(Doub a, Doub x, Int psig) $\left\{ \begin{array} { r l } \end{array} \right.$   
Incomplete gamma by quadrature. Returns $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ or $Q ( a , x )$ , when psig is 1 or 0, respectively. User should not call directly.

Int j; Doub xu,t,sum,ans; Doub a1 $= \ a - 1 . 0$ , lna1 $=$ log(a1), sqrta1 $=$ sqrt(a1); ${ \bf g l n = \bf g a m m l n ( a ) }$ ; Set how far to integrate into the tail: if ( $\texttt { x } >$ a1) $\mathrm { ~ \tt ~ { ~ x ~ u ~ } ~ } =$ MAX(a1 $^ +$ 11. $^ { 5 \ast }$ sqrta1, x + 6. $^ { 0 * }$ sqrta1); else xu $=$ MAX(0.,MIN(a1 - 7.5\*sqrta1, x - 5.0\*sqrta1)); sum $\mathit { \Theta } = \mathit { \Theta } 0$ ; for (j=0;j<ngau;j++) { Gauss-Legendre. $\texttt { t } = \texttt { x } + \texttt { ( x u - x ) } * \texttt { y } [ \texttt j ]$ ; sum += w[j]\*exp(-(t-a1)+a1\*(log(t)-lna1)); ans $=$ sum\*(xu-x)\*exp(a1\*(lna1-1.)-gln); return (psig?(ans>0.0? 1.0-ans:-ans):(ans> ${ } = 0$ .0? ans:1.0+ans)); }

Doub invgammp(Doub p, Doub a);   
Inverse function on $x$ of $P ( { \boldsymbol { a } } , { \boldsymbol { x } } )$ . See $\ S 6 . 2 . 1$ . };   
const Doub Gamma::EPS $=$ numeric_limits<Doub>::epsilon();   
const Doub Gamma::FPMIN $=$ numeric_limits<Doub>::min()/EPS;

Remember that since Gamma is an object, you have to declare an instance of it before you can use its member functions. We habitually write

# Gamma gam;

as a global declaration, and then call gam.gammp or gam.gammq as needed. The structure Gauleg18 just contains the abscissas and weights for the Gauss-Legendre quadrature.

# struct Gauleg18 {

Abscissas and weights for Gauss-Legendre quadrature.

static const Int ngau $\ c = \ 1 8$ ; static const Doub y[18]; static const Doub w[18];   
};   
const Doub Gauleg18::y[18] $=$ {0.0021695375159141994,   
0.011413521097787704,0.027972308950302116,0.051727015600492421,   
0.082502225484340941, 0.12007019910960293,0.16415283300752470,   
0.21442376986779355, 0.27051082840644336, 0.33199876341447887,   
0.39843234186401943, 0.46931971407375483, 0.54413605556657973,   
0.62232745288031077, 0.70331500465597174, 0.78649910768313447,   
0.87126389619061517, 0.95698180152629142};   
const Doub Gauleg18::w[18] $=$ {0.0055657196642445571,   
0.012915947284065419,0.020181515297735382,0.027298621498568734,   
0.034213810770299537,0.040875750923643261,0.047235083490265582,   
0.053244713977759692,0.058860144245324798,0.064039797355015485,

0.068745323835736408,0.072941885005653087,0.076598410645870640,   
0.079687828912071670,0.082187266704339706,0.084078218979661945,   
0.085346685739338721,0.085983275670394821};

# 6.2.1 Inverse Incomplete Gamma Function

In many statistical applications one needs the inverse of the incomplete gamma function, that is, the value $x$ such that $P ( a , x ) = p$ , for a given value $0 \leq p \leq 1$ . Newton’s method works well if we can devise a good-enough initial guess. In fact, this is a good place to use Halley’s method (see $\ S 9 . 4$ ), since the second derivative (that is, the first derivative of the integrand) is easy to compute.

For $a > 1$ , we use an initial guess that derives from $\ S 2 6 . 2 . 2 2$ and $\ S 2 6 . 4 . 1 7$ in reference [1]. For $a \leq 1$ , we first roughly approximate $P _ { a } \equiv P ( a , 1 )$ :

$$
P _ { a } \equiv P ( a , 1 ) \approx 0 . 2 5 3 a + 0 . 1 2 a ^ { 2 } , \qquad 0 \leq a \leq 1
$$

and then solve for $x$ in one or the other of the (rough) approximations:

$$
\begin{array} { r } { P ( a , x ) \approx \left\{ \begin{array} { l l } { P _ { a } x ^ { a } , } & { x < 1 } \\ { P _ { a } + ( 1 - P _ { a } ) ( 1 - e ^ { 1 - x } ) , } & { x \geq 1 } \end{array} \right. } \end{array}
$$

An implementation is

Doub Gamma::invgammp(Doub p, Doub a) {   
Returns $x$ such that $P ( a , x ) = p$ for an argument $p$ between 0 and 1. Int j; Doub x,err,t,u,pp,lna1,afac,a $\mathsf { L } = \mathsf { a } - 1$ ; const Doub EPS $\mathop { : = } 1$ .e-8; Accuracy is the square of EPS. gln=gammln(a); if ( $\texttt { a } < = \texttt { 0 } .$ ) throw("a must be pos in invgammap"); if $\mathrm { ( p \ > = \ 1 . }$ ) return MAX(100.,a $^ +$ 100.\*sqrt(a)); if ${ \mathrm { ( p ) < = 0 } } .$ ) return 0.0; if ( $\texttt { a } > \texttt { 1 }$ .) { Initial guess based on reference [1]. lna1 $=$ log(a1); afac $=$ exp(a1\*(lna1-1.)-gln); $\mathrm { p p ~ = ~ ( p ~ < ~ 0 ~ . 5 ) ? ~ p ~ : ~ 1 }$ . - p; $\mathrm {  ~ t ~ } = \mathrm {  ~ \ s q r t { } ~ } ( - 2 . * 1 \mathrm { o g } ( \mathrm { p p } ) )$ ); $\mathrm { ~ x ~ } =$ (2.30753+t\*0.27061)/(1.+t\*(0.99229+t\*0.04481)) - t; if $( \mathtt { p } \ < \ 0 . 5 )$ ) $\mathrm { ~ \tt ~ { ~ x ~ } ~ } = \mathrm { ~ \tt ~ { ~ - ~ x ~ } ~ }$ ; $\mathrm { ~ x ~ } =$ MAX(1.e-3,a\*pow(1.-1./(9.\*a)-x/(3.\*sqrt(a)),3)); } else { Initial guess based on equations (6.2.8) t = 1.0 - a\*(0.253+a\*0.12); and (6.2.9). if (p < t) $_ { \textrm { x } } =$ pow(p/t,1./a); else x = 1.-log(1.-(p-t)/(1.-t)); } for (j=0;j<12;j++) { if ( $\mathrm { ~  ~ \bar { ~ } x ~ } < = \mathrm { ~  ~ 0 ~ } . 0 $ ) return 0.0; $x$ too small to compute accurately. err $=$ gammp(a,x) - p; if (a $> ~ 1 .$ ) t = afac\*exp(-(x-a1)+a1\*(log(x)-lna1)); else t $=$ exp(-x+a1\*log(x)-gln); $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ err/t; $\texttt { x } \texttt { - } \left( \texttt { t } = \texttt { u } / \left( 1 \ldots 0 . 5 * \mathtt { M I N } ( 1 . \texttt { , u * } ( ( \mathtt { a - 1 . } ) / \texttt { x } - \texttt { 1 } ) ) \right) \right) \texttt { m } \texttt { - l - w } \texttt { N } _ { \texttt { i n - w } } ( \texttt { c l - w } _ { \texttt { i n - i - j } } ) \texttt { N } _ { \texttt { i n - i - j } }$ ; Halley’s method. if ( $\begin{array} { r } { \mathrm { ~  ~ x ~ } < = \mathrm { ~  ~ 0 ~ } . } \end{array}$ ) $\textbf { x } = ~ 0 . 5 * ( \textbf { x } + \textbf { t } )$ ; Halve old value if $x$ tries to go negative. if (fabs(t) $<$ EPS\*x ) break; } return x;

# 6.2.2 Error Function

The error function and complementary error function are special cases of the incomplete gamma function and are obtained moderately efficiently by the above procedures. Their definitions are

$$
\operatorname { e r f } ( x ) = { \frac { 2 } { \sqrt { \pi } } } \int _ { 0 } ^ { x } e ^ { - t ^ { 2 } } d t
$$

and

$$
\mathrm { e r f c } ( x ) \equiv 1 - \mathrm { e r f } ( x ) = \frac { 2 } { \sqrt { \pi } } \int _ { x } ^ { \infty } e ^ { - t ^ { 2 } } d t
$$

The functions have the following limiting values and symmetries:

$$
{ \begin{array} { r l r l } & { \operatorname { e r f } ( 0 ) = 0 } & & { \operatorname { e r f } ( \infty ) = 1 \qquad \operatorname { e r f } ( - x ) = - \operatorname { e r f } ( x ) } \\ & { \operatorname { e r f c } ( 0 ) = 1 } & & { \operatorname { e r f c } ( \infty ) = 0 } & & { \operatorname { e r f c } ( - x ) = 2 - \operatorname { e r f c } ( x ) } \end{array} }
$$

They are related to the incomplete gamma functions by

$$
\operatorname { e r f } ( x ) = P \left( { \frac { 1 } { 2 } } , x ^ { 2 } \right) \qquad ( x \geq 0 )
$$

and

$$
\operatorname { e r f c } ( x ) = Q \left( { \frac { 1 } { 2 } } , x ^ { 2 } \right) \qquad ( x \geq 0 )
$$

A faster calculation takes advantage of an approximation of the form

$$
\mathrm { e r f c } ( z ) \approx t \ \mathrm { e x p } [ - z ^ { 2 } + \mathcal { P } ( t ) ] , \qquad z > 0
$$

where

$$
t \equiv { \frac { 2 } { 2 + z } }
$$

and $\mathcal { P } ( t )$ is a polynomial for $0 \leq t \leq 1$ that can be found by Chebyshev methods (-5.8). As with Gamma, implementation is by an object that also includes the inverse function, here an inverse for both erf and erfc. Halley’s method is again used for the inverses (as suggested by P.J. Acklam).

# erf.h

# struct Erf {

Object for error function and related functions.

static const Int ncof $= 2 8$ ;   
static const Doub cof[28];

Initialization at end of struct.

inline Doub erf(Doub x) {   
Return erf $( x )$ for any $x$ . if $\mathrm { (  ~ x ~ } ) = 0 \ .$ ) return 1.0 - erfccheb(x); else return erfccheb(-x) - 1.0;   
}   
inline Doub erfc(Doub x) {   
Return erfc. $( x )$ for any $x$ . if $\begin{array} { r } { \mathrm { ~  ~ \psi ~ } ( { \bf x } ) = { \bf \psi } 0 . } \end{array}$ ) return erfccheb $\mathbf { \Psi } ( \mathbf { x } )$ ; else return 2.0 - erfccheb $\left( - \mathbf { \vec { x } } \right)$ ;   
}

# Doub erfccheb(Doub z){

Evaluate equation (6.2.16) using stored Chebyshev coefficients. User should not call directly.

Int j;  
Doub t,ty,tmp, $\mathtt { d } \mathtt { = } 0$ .,dd=0.;  
if ( $\ z \ < \ 0 .$ ) throw("erfccheb requires nonnegative argument")  
$\tt { t } = \displaystyle 2 . / ( 2 . + z )$ ;  
ty $=$ 4.\*t - 2.;  
for (j=ncof-1;j>0;j--) {tmp $=$ d;d $=$ ty\*d - dd $^ +$ cof[j];dd $=$ tmp;  
}  
return t\*exp(-z\*z + 0.5\*(cof[0] $^ +$ ty\*d) - dd);

# }

# Doub inverfc(Doub p) {

Inverse of complementary error function. Returns $x$ such that erfc $( x ) = p$ for argument $p$ between 0 and 2.

Doub x,err,t,pp;   
if (p $> = \ 2 . 0 )$ return -100.; Return arbitrary large pos or neg value.   
if $( \mathbf { p } ) \ < = \ 0 . 0 )$ ) return 100.;   
$\mathrm { p p } = ( \mathrm { p } < 1 . 0 ) ? \mathrm { p } : 2 . -$ p;   
$\mathrm { ~ t ~ } = \mathrm { ~ s q r t } \left( - 2 . * \mathrm { { 1 o g } } \left( \mathrm { p p } / 2 . \right) \right) ;$ Initial guess:   
x = -0.70711\*((2.30753+t\*0.27061)/(1.+t\*(0.99229+t\*0.04481)) - t);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<2;j $^ { + + }$ ) { err $=$ erfc(x) - pp; x $+ =$ err/(1.12837916709551257\*exp(-SQR $\mathbf { \Psi } ( \mathbf { x } )$ )-x\*err); Halley.   
return $\ : \left( \mathrm { p } < 1 . 0 ? \ : \mathrm {  ~ x ~ } : - \mathrm { x } \right) :$ ; inline Doub inverf(Doub p) {return inverfc(1.-p);}   
Inverse of the error function. Returns $x$ such that $\operatorname { s r f } ( x ) = p$ for argument $p$ between 1 and 1.

#

onst Doub Erf::cof[28] $= ~ \left\{ - 1 \atop \right.$ .3026537197817094, 6.4196979235649026e-1, 1.9476473204185836e-2,-9.561514786808631e-3,-9.46595344482036e-4, 3.66839497852761e-4,4.2523324806907e-5,-2.0278578112534e-5, -1.624290004647e-6,1.303655835580e-6,1.5626441722e-8,-8.5238095915e-8, 6.529054439e-9,5.059343495e-9,-9.91364156e-10,-2.27365122e-10, 9.6467911e-11, 2.394038e-12,-6.886027e-12,8.94487e-13, 3.13092e-13, -1.12708e-13,3.81e-16,7.106e-15,-1.523e-15,-9.4e-17,1.21e-16,-2.8e-17};

A lower-order Chebyshev approximation produces a very concise routine, though with only about single precision accuracy:

# Doub erfcc(const Doub x)

Returns the complementary error function erfc $\mathbf { \rho } ( \mathbf { x } )$ with fractional error everywhere less than $1 . 2 \times 1 0 ^ { - 7 }$ .

Doub t,z=fabs $\left( \mathbf { \boldsymbol { x } } \right)$ ,ans;   
$\mathrm { t } { = } 2 . / ( 2 . +  { \mathrm { z } } )$ ;   
ans=t\*exp(-z\*z-1.26551223+t\*(1.00002368+t\*(0.37409196+t\*(0.09678418+ t\*(-0.18628806+t\*(0.27886807+t\*(-1.13520398+t\*(1.48851587+ t\*(-0.82215223+t\*0.17087277)))))))));   
return $\mathrm { ~ ( ~ x ~ ) = ~ 0 ~ . 0 ~ }$ ? ans : 2.0-ans);

![](images/5b2bdea95927dba5c942d25f629039f68b7daa91357cde1412da389934c091ad.jpg)  
Figure 6.3.1. Exponential integrals $E _ { n } ( x )$ for $n = 0 , 1 , 2 , 3 , 5$ ; and 10, and the exponential integral $\operatorname { E i } ( x )$ .

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapters 6, 7, and 26.[1]

Pearson, K. (ed.) 1951, Tables of the Incomplete Gamma Function (Cambridge, UK: Cambridge University Press).

# 6.3 Exponential Integrals

The standard definition of the exponential integral is

$$
E _ { n } ( x ) = \int _ { 1 } ^ { \infty } { \frac { e ^ { - x t } } { t ^ { n } } } d t , \qquad x > 0 , \quad n = 0 , 1 , \ldots .
$$

The function defined by the principal value of the integral

$$
\operatorname { E i } ( x ) = - \int _ { - x } ^ { \infty } { \frac { e ^ { - t } } { t } } d t = \int _ { - { \infty } } ^ { x } { \frac { e ^ { t } } { t } } d t , \qquad x > 0
$$

is also called an exponential integral. Note that $\operatorname { E i } ( - x )$ is related to $- E _ { 1 } ( x )$ by analytic continuation. Figure 6.3.1 plots these functions for representative values of their parameters.

The function $E _ { n } ( x )$ is a special case of the incomplete gamma function

$$
E _ { n } ( x ) = x ^ { n - 1 } \Gamma ( 1 - n , x )
$$

We can therefore use a similar strategy for evaluating it. The continued fraction — just equation (6.2.6) rewritten — converges for all $x > 0$ :

$$
E _ { n } ( x ) = e ^ { - x } \left( { \frac { 1 } { x + } } { \frac { n } { 1 + } } { \frac { 1 } { x + } } { \frac { n + 1 } { 1 + } } { \frac { 2 } { x + } } \cdots \right)
$$

We use it in its more rapidly converging even form,

$$
E _ { n } ( x ) = e ^ { - x } \left( { \frac { 1 } { x + n - } } { \frac { 1 \cdot n } { x + n + 2 - } } { \frac { 2 ( n + 1 ) } { x + n + 4 - } } \cdots \right)
$$

The continued fraction only really converges fast enough to be useful for $x \gtrsim 1$ . For $0 < x \lesssim 1$ , we can use the series representation

$$
E _ { n } ( x ) = { \frac { ( - x ) ^ { n - 1 } } { ( n - 1 ) ! } } [ - \ln x + \psi ( n ) ] - \sum _ { \stackrel { m = 0 } { m \neq n - 1 } } ^ { \infty } { \frac { ( - x ) ^ { m } } { ( m - n + 1 ) m ! } }
$$

The quantity $\psi ( n )$ here is the digamma function, given for integer arguments by

$$
\psi ( 1 ) = - \gamma , \qquad \psi ( n ) = - \gamma + \sum _ { m = 1 } ^ { n - 1 } \frac { 1 } { m }
$$

where $\gamma = 0 . 5 7 7 2 1 5 6 6 4 9 \ldots$ is Euler’s constant. We evaluate the expression (6.3.6) in order of ascending powers of $x$ :

$$
\begin{array} { c } { { E _ { n } ( x ) = - \displaystyle \left[ \frac { 1 } { ( 1 - n ) } - \frac { x } { ( 2 - n ) \cdot 1 } + \frac { x ^ { 2 } } { ( 3 - n ) ( 1 \cdot 2 ) } - \cdots + \frac { ( - x ) ^ { n - 2 } } { ( - 1 ) ( n - 2 ) ! } \right] } } \\ { { + \displaystyle \frac { ( - x ) ^ { n - 1 } } { ( n - 1 ) ! } [ - \ln x + \psi ( n ) ] - \displaystyle \left[ \frac { ( - x ) ^ { n } } { 1 \cdot n ! } + \frac { ( - x ) ^ { n + 1 } } { 2 \cdot ( n + 1 ) ! } + \cdots \right] } } \end{array}
$$

The first square bracket is omitted when $n = 1$ . This method of evaluation has the advantage that, for large $n$ , the series converges before reaching the term containing $\psi ( n )$ . Accordingly, one needs an algorithm for evaluating $\psi ( n )$ only for small $n , n \stackrel { < } { \sim }$ $2 0 - 4 0$ . We use equation (6.3.7), although a table lookup would improve efficiency slightly.

Amos [1] presents a careful discussion of the truncation error in evaluating equation (6.3.8) and gives a fairly elaborate termination criterion. We have found that simply stopping when the last term added is smaller than the required tolerance works about as well.

Two special cases have to be handled separately:

$$
\begin{array} { l } { \displaystyle E _ { 0 } ( \boldsymbol { x } ) = \frac { e ^ { - x } } { x } } \\ { \displaystyle E _ { n } ( 0 ) = \frac { 1 } { n - 1 } , \qquad n > 1 } \end{array}
$$

The routine expint allows fast evaluation of $E _ { n } ( x )$ to any accuracy EPS within the reach of your machine’s precision for floating-point numbers. The only modification required for increased accuracy is to supply Euler’s constant with enough significant digits. Wrench [2] can provide you with the first 328 digits if necessary!

Doub expint(const Int n, const Doub x) Evaluates the exponential integral $E _ { n } ( x )$ . {

static const Int MAXI $\mathtt { \tau } = 1 0 0$ ;   
static const Doub EULER $_ { = 0 }$ .577215664901533, EPS=numeric_limits<Doub>::epsilon(), BIG $\mathbf { \bar { \mathbf { \tau } } }$ numeric_limits<Doub>::max()\*EPS; Here MAXIT is the maximum allowed number of iterations; EULER is Euler’s con ; EPS is the desired relative error, not smaller than the machine precision; BIG number near the largest representable floating-point number.   
Int i,ii,nm1 $= \mathtt { n } - 1$ ;   
Doub a,b,c,d,del,fact,h,psi,ans;   
if ( $\mathrm { ~ \textit ~ { ~ n ~ } ~ } < \mathrm { ~ \textit ~ { ~ O ~ } ~ }$ || $\texttt { x } < 0 . 0$ || $\scriptstyle \mathbf { \underline { { x } } } = = 0 . 0$ && $\scriptstyle ( \mathtt { n } = = 0 \ \mid \mid \ \mathtt { n } = = 1 ) ) \ .$ ) throw("bad arguments in expint");   
if $\mathbf { \Omega } _ { \mathrm { ~ n ~ } } = = \mathbf { \Omega } 0$ ) ans ${ } = { }$ exp $( - \mathbf { x } ) / \mathbf { x }$ ; Special case.   
else { if $( \textbf { x } = = \ 0 . 0$ ) ans $= 1$ .0/nm1; Another special case. else { if $\mathit { \check { \Psi } } _ { \mathrm { ~ X ~ } } > \ 1 . 0 \ \rangle$ { Lentz’s algorithm (-5.2). ${ \tt b } = { \tt x } + { \tt n }$ ; $c =$ BIG; $\mathtt { d } \mathtt { = } 1$ .0/b; $\mathtt { h } = \mathtt { d }$ ; for ( $\dot { \ b _ { 1 } } = 1$ ;i $\cdot < =$ MAXIT;i++) { a = -i\*(nm1+i); b $+ = ~ 2 . 0$ ; d=1.0/(a\*d+b); Denominators cannot be zero. c=b+a/c; del=c\*d; h $* =$ del; if (abs(del-1.0) $< =$ EPS) { ans=h\*exp(-x); return ans; } } throw("continued fraction failed in expint"); } else { Evaluate series. ans $=$ (nm1 $\iota { = } 0$ ? 1.0/nm1 : -log(x)-EULER); Set first term. fact $= 1$ .0; for ( $\dot { \ b _ { 1 } } = 1$ ;i $< =$ MAXIT;i++) { fact $\ast = \mathbf { \Gamma } - \mathbf { x } / \mathrm { i }$ ; if (i ! $\downarrow =$ nm1) del $=$ -fact/(i-nm1); else { psi $=$ -EULER; Compute $\psi ( n )$ . for ( $\dot { 1 } \dot { 1 } = 1$ ;ii $< =$ nm1;ii $^ { + + }$ ) psi $+ =$ 1.0/ii; del=fact\*(-log(x)+psi); ans $+ =$ del; if (abs(del) $<$ abs(ans)\*EPS) return ans; } throw("series failed in expint"); } }   
return ans;

A good algorithm for evaluating Ei is to use the power series for small $x$ and the asymptotic series for large $x$ . The power series is

$$
\operatorname { E i } ( x ) = \gamma + \ln x + { \frac { x } { 1 \cdot 1 ! } } + { \frac { x ^ { 2 } } { 2 \cdot 2 ! } } + \cdots
$$

where $\gamma$ is Euler’s constant. The asymptotic expansion is

$$
\operatorname { E i } ( x ) \sim { \frac { e ^ { x } } { x } } \left( 1 + { \frac { 1 ! } { x } } + { \frac { 2 ! } { x ^ { 2 } } } + \cdots \right)
$$

The lower limit for the use of the asymptotic expansion is approximately $| \ln { \tt E P S } |$ , where EPS is the required relative error.

Doub ei(const Doub x) { mputes the exponential integral $\operatorname { E i } ( x )$ for $x > 0$ . static const Int MAXIT $^ { \prime = 1 }$ 100; static const Doub EULER $_ { = 0 }$ .577215664901533, EPS=numeric_limits<Doub>::epsilon(), FPMIN=numeric_limits<Doub>::min()/EPS; Here MAXIT is the maximum number of iterations allowed; EULER is Euler’s constant $\gamma$ ; EPS is the relative error, or absolute error near the zero of Ei at $x = 0 . 3 7 2 5$ ; FPMIN is a number close to the smallest representable floating-point number. Int k; Doub fact,prev,sum,term; if ( $\varpi \ : < = \ : 0 . 0 \dot { . }$ ) throw("Bad argument in ei"); if ( $\texttt { x } <$ FPMIN) return log(x)+EULER; Special case: Avoid failure of convergence if (x <= -log(EPS)) { test because of underflow. sum $\mathord { \left[ - 0 \mathrm { ~ , ~ } 0 \mathrm { ~ } \right] }$ ; Use power series. fact ${ = } 1$ .0; for $\scriptstyle ( \mathtt { k } = 1$ ;k $< =$ MAXIT;k++) { fact $\ast = ~ \mathrm { { \ x / k } }$ ; term=fact/k; sum $+ =$ term; if (term $<$ EPS\*sum) break; } if (k $>$ MAXIT) throw("Series failed in ei"); return sum+log(x)+EULER; else { Use asymptotic series. sum $= 0$ .0; Start with second term. term $= 1$ .0; for $\mathtt { k } = 1$ ;k $< =$ MAXIT;k++) { prev=term; term $\ast = ~ \mathrm { k } / \mathrm { x }$ ; if (term $<$ EPS) break; Since final sum is greater than one, term itself approximates the relative error. if (term $<$ prev) sum $+ =$ term; Still converging: Add new term. else { sum $- =$ prev; Diverging: Subtract previous term and break; exit. } } return exp(x)\*(1.0+sum)/x; }

# CITED REFERENCES AND FURTHER READING:

Stegun, I.A., and Zucker, R. 1974, “Automatic Computing Methods for Special Functions. II. The Exponential Integral $E _ { n } ( x )$ ,” Journal of Research of the National Bureau of Standards,

vol. 78B, pp. 199–216; 1976, “Automatic Computing Methods for Special Functions. III. The Sine, Cosine, Exponential Integrals, and Related Functions,” op. cit., vol. 80B, pp. 291–311.

Amos D.E. 1980, “Computation of Exponential Integrals,” ACM Transactions on Mathematical Software,vol.6,pp.365-377[1]; also vol.6, pp.420-428.

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 5.

Wrench J.W. 1952, “A New Calculation of Euler’s Constant,” Mathematical Tables and OtherAids to Computation,vol. 6,p. 255.[2]

# 6.4 Incomplete Beta Function

The incomplete beta function is defined by

$$
I _ { x } ( a , b ) \equiv \frac { B _ { x } ( a , b ) } { B ( a , b ) } \equiv \frac { 1 } { B ( a , b ) } \int _ { 0 } ^ { x } t ^ { a - 1 } ( 1 - t ) ^ { b - 1 } d t \qquad ( a , b > 0 )
$$

It has the limiting values

$$
I _ { 0 } ( a , b ) = 0 \qquad I _ { 1 } ( a , b ) = 1
$$

and the symmetry relation

$$
I _ { x } ( a , b ) = 1 - I _ { 1 - x } ( b , a )
$$

If $a$ and $b$ are both rather greater than one, then $I _ { x } ( a , b )$ rises from “near-zero” to “near-unity” quite sharply at about $x = a / ( a + b )$ . Figure 6.4.1 plots the function for several pairs $( a , b )$ .

The incomplete beta function has a series expansion

$$
I _ { x } ( a , b ) = \frac { x ^ { a } ( 1 - x ) ^ { b } } { a B ( a , b ) } \left[ 1 + \sum _ { n = 0 } ^ { \infty } \frac { B ( a + 1 , n + 1 ) } { B ( a + b , n + 1 ) } x ^ { n + 1 } \right]
$$

but this does not prove to be very useful in its numerical evaluation. (Note, however, that the beta functions in the coefficients can be evaluated for each value of $n$ with just the previous value and a few multiplies, using equations 6.1.9 and 6.1.3.)

The continued fraction representation proves to be much more useful:

$$
I _ { x } ( a , b ) = { \frac { x ^ { a } ( 1 - x ) ^ { b } } { a B ( a , b ) } } \left[ { \frac { 1 } { 1 + } } { \frac { d _ { 1 } } { 1 + } } { \frac { d _ { 2 } } { 1 + } } \cdots \right]
$$

where

$$
\begin{array} { c } { { d _ { 2 m + 1 } = - \displaystyle \frac { ( a + m ) ( a + b + m ) x } { ( a + 2 m ) ( a + 2 m + 1 ) } } } \\ { { d _ { 2 m } = \displaystyle \frac { m ( b - m ) x } { ( a + 2 m - 1 ) ( a + 2 m ) } } } \end{array}
$$

This continued fraction converges rapidly for $x \ < \ ( a + 1 ) / ( a + b + 2 )$ , except when $a$ and $b$ are both large, when it can take $O ( \sqrt { \operatorname* { m i n } ( a , b ) } )$ iterations. For $x \ >$ $( a + 1 ) / ( a + b + 2 )$ we can just use the symmetry relation (6.4.3) to obtain an equivalent computation in which the convergence is again rapid. Our computational strategy is thus very similar to that used in Gamma: We use the continued fraction except when $a$ and $b$ are both large, in which case we do a single step of high-order Gauss-Legendre quadrature.

![](images/b13ef3b387045e0f83d128d9c2e140487de117395e1af8964610bca545ae9b53.jpg)  
Figure 6.4.1. The incomplete beta function $I _ { x } ( a , b )$ for five different pairs of $( a , b )$ . Notice that the pairs .0:5; 5:0/ and .5:0; 0:5/ are symmetrically related as indicated in equation (6.4.3).

Also as in Gamma, we code an inverse function using Halley’s method. When $a$ and $b$ are both $\geq 1$ , the initial guess comes from $\ S 2 6 . 5 . 2 2$ in reference [1]. When either is less than 1, the guess comes from first crudely approximating

$$
\int _ { 0 } ^ { 1 } t ^ { a - 1 } ( 1 - t ) ^ { b - 1 } d t \approx { \frac { 1 } { a } } \left( { \frac { a } { a + b } } \right) ^ { a } + { \frac { 1 } { b } } \left( { \frac { b } { a + b } } \right) ^ { b } \equiv S
$$

which comes from breaking the integral at $t = a / ( a + b )$ and ignoring one factor in the integrand on each side of the break. We then write

$$
I _ { x } ( a , b ) \approx \left\{ \begin{array} { l l } { x ^ { a } / ( S a ) } & { x \leq a / ( a + b ) } \\ { ( 1 - x ) ^ { b } / ( S b ) } & { x > a / ( a + b ) } \end{array} \right.
$$

and solve for $x$ in the respective regimes. While crude, this is good enough to get well within the basin of convergence in all cases.

# struct Beta : Gauleg18 {

Object for incomplete beta function. Gauleg18 provides coefficients for Gauss-Legendre quadrature.

static const Int SWITCH=3000; When to switch to quadrature method.   
static const Doub EPS, FPMIN; See end of struct for initializations.

Doub betai(const Doub a, const Doub b, const Doub x) { Returns incomplete beta function $I _ { x } ( a , b )$ for positive $^ { a }$ and $^ { b }$ , and $x$ between 0 and 1.

Doub bt;   
if ( $\texttt { a } < = \texttt { 0 } . 0$ || b $< = \ 0 . 0$ ) throw("Bad a or b in routine betai");   
if $( \texttt { x } < 0 . 0 \ | \ | \ \texttt { x } > \ 1 . 0 )$ throw("Bad x in routine betai");   
if $( \mathrm {  ~ x ~ } = = \mathrm {  ~ 0 ~ } . 0 | | \mathrm {  ~ x ~ } = = \mathrm {  ~ 1 ~ } . 0 )$ ) return x;   
if ( $\texttt { a } >$ SWITCH && b $>$ SWITCH) return betaiapprox(a,b,x);   
bt=exp(gammln(a+b)-gammln(a)-gammln(b)+a\*log(x)+b\*log(1.0-x));   
if $\left( \mathrm { x } < \left( \mathrm { a } + 1 . 0 \right) / \left( \mathrm { a } + \mathrm { b } + 2 . 0 \right) \right.$ ) return bt\*betacf(a,b,x)/a;   
else return 1.0-bt\*betacf(b,a,1.0-x)/b;

# Doub betacf(const Doub a, const Doub b, const Doub x) {

Evaluates continued fraction for incomplete beta function by modified Lentz’s method (-5.2). User should not call directly.

Int m,m2;   
Doub aa,c,d,del,h,qab,qam,qap;   
qab $= \mathtt { a } + 1$ b; These q’s will be used in factors that   
qap $\mathtt { \Gamma } _ { 1 } = \mathtt { a } + 1$ .0; occur in the coefficients (6.4.6).   
qam=a-1.0;   
c=1.0; First step of Lentz’s method.   
$\mathtt { d } \mathtt { = } 1$ .0-qab\*x/qap;   
if (fabs(d) $<$ FPMIN) d=FPMIN;   
d=1.0/d;   
h=d;   
for (m=1;m<10000;m++) { $\mathtt { m } 2 \mathrm { = } 2 \ast \mathtt { m }$ ; aa=m\*(b-m)\*x/((qam+m2)\*(a+m2)); d=1.0+aa\*d; One step (the even one) of the recurif (fabs(d) $<$ FPMIN) $\mathrm { d } \mathrm { = }$ FPMIN; rence. c=1.0+aa/c; if (fabs(c) $<$ FPMIN) $c =$ FPMIN; $\mathtt { d } \mathtt { = } 1$ .0/d; $\mathrm {  ~ h ~ \ * = ~ \ d * c }$ ; aa = -(a+m)\*(qab+m)\*x/((a+m2)\*(qap+m2)); $\mathrm { d } { = } 1$ .0+aa\*d; Next step of the recurrence (the odd if (fabs(d) $<$ FPMIN) $\mathrm { d } \mathrm { = }$ FPMIN; one). c=1.0+aa/c; if (fabs(c) $<$ FPMIN) $c =$ FPMIN; $\mathtt { d } \mathtt { = } 1$ .0/d; del=d\*c; h $\ast =$ del; if (fabs(del-1.0) $< =$ EPS) break; Are we done?   
}   
return h;

Doub betaiapprox(Doub a, Doub b, Doub $\mathbf { x }$ ) { Incomplete beta by quadrature. Returns $I _ { x } ( a , b )$ . User should not call directly.

Int j;   
Doub xu,t,sum,ans;   
Doub a $1 \ = \ \mathsf { a } { - } 1 . 0$ , $ { \mathbf { b } }  { \mathbf { 1 } } ~ = ~  { \mathbf { b } } - 1 . 0$ , $\mathrm { \ m u ~ = ~ a / ( a + b ) }$ ;   
Doub lnmu $\cdot ^ { = }$ log(mu),lnmuc=log(1.-mu);   
${ \texttt { t } } =$ sqrt(a\*b/(SQR(a+b)\*(a+b+1.0)));   
if $x > a / ( a + b )$ ) { Set how far to integrate into the tail: if $( \textbf { x } > = \textbf { 1 } . 0 )$ ) return 1.0; $\mathrm { ~ x u ~ } =$ MIN(1.,MAX(mu $^ +$ 10.\*t, $\textbf { x } + \textbf { 5 } . 0 { * } \mathrm { t } ) \big )$ ;   
} else {

if $\mathit { \Psi } ( \mathbf { x } \ < = \ 0 . 0 ) $ ) return 0.0; xu $=$ MAX(0.,MIN(mu - 10.\*t, x - 5.0\*t)); } sum = 0; for (j=0;j<18;j++) { Gauss-Legendre. t = x + (xu-x)\*y[j]; sum += w[j]\*exp(a1\*(log(t)-lnmu)+b1\*(log(1-t)-lnmuc)); ans $=$ sum\*(xu-x)\*exp(a1\*lnmu-gammln(a)+b1\*lnmuc-gammln(b)+gammln(a+b)); return ans>0.0? 1.0-ans : -ans;

Doub invbetai(Doub p, Doub a, Doub b) {   
Inverse of incomplete beta function. Returns $x$ such that $I _ { x } ( a , b ) = p$ for argument $p$ between 0 and 1.

const Doub EPS $\ l = \ 1$ .e-8; Doub pp,t,u,err,x,al,h,w,afac,a1=a-1.,b1=b-1.; Int j; if $( \mathtt { p } \ < = \ 0 .$ ) return 0.; else if ( $\mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ } \mathrm {  ~ \cdot ~ }$ ) return 1.; else if ( $a > = 1$ . && b $> = ~ 1 ,$ ) { Set initial guess. See text. $\mathrm { { p p } ~ = ~ ( p ~ < ~ 0 ~ . 5 ) ? ~ p ~ : ~ 1 . }$ - p; $\texttt { t } = \texttt { s q r t } ( - 2 . * 1 \circ \mathtt { g } ( \mathtt { p p } ) )$ ; $\mathrm { ~ x ~ } =$ (2.30753+t\*0.27061)/(1.+t\*(0.99229+t\*0.04481)) - t; if $( \mathtt { p } \ < \ 0 . 5 )$ $\mathrm { ~ \tt ~ { ~ x ~ } ~ } = \mathrm { ~ \tt ~ - { ~ x ~ } ~ }$ ; $\mathrm { { \bf { a } } } \mathrm { { \bf { 1 } } } = ( { \tt S Q R } ( { \bf { x } } ) - 3 . ) / 6 .$ ; h = 2./(1./(2.\*a-1.)+1./(2.\*b-1.)); $\kappa =$ (x\*sqrt(al+h)/h)-(1./(2.\*b-1)-1./(2.\*a-1.))\*(al+5./6.-2./(3.\*h)); x = a/(a+b\*exp(2.\*w)); } else { Doub lna $=$ log(a/(a+b)), lnb $=$ log(b/(a+b)); $\begin{array} { r l } { \mathbf { \epsilon } _ { \mathbf { { t } } } } & { { } = } \end{array}$ exp(a\*lna)/a; $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ exp(b\*lnb)/b; $\mathrm { ~  ~ w ~ } = \mathrm { ~ t ~ } + \mathrm { ~  ~ \Omega ~ }$ u; if $( \mathbb { p } \ < \ \pm / \mathbb { w } )$ x = pow(a\*w\*p,1./a); else $\texttt { x } = \texttt { 1 }$ . - pow(b\*w\*(1.-p),1./b); } afac $=$ -gammln(a)-gammln(b)+gammln(a+b); for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<10;j++) { if ( $\mathrm { ~  ~ x ~ } = = \mathrm { ~  ~ 0 ~ }$ . || $\begin{array} { r } { \mathbf { x } \ = = \ 1 . } \end{array}$ ) return x; a or $^ { b }$ too small for accurate calcuerr $=$ betai(a,b,x) - p; lation. $\begin{array} { r l } { \tplus } & { { } = } \end{array}$ exp(a1\*log(x)+b1\*log(1.-x) $^ +$ afac); $u \ =$ err/t; Halley: $\begin{array} { r l } { \mathbf { x } } & { { } - = } \end{array}$ (t = u/(1.-0.5\*MIN(1.,u\*(a1/x - b1/(1.-x))))); if $\mathbf { \Phi } _ { \mathbf { x } } \mathbf { \Phi } < = \mathbf { \Phi } 0 .$ ) $\textbf { x } = ~ 0 \ : . 5 * ( \textbf { x } + \textbf { t } )$ ; Bisect if $x$ tries to go neg or $> 1$ . if $\mathbf { \Psi } ( \mathbf { x _ { \alpha } } > = \mathbf { \Psi } 1 .$ ) $\textbf { x } = \ 0 . 5 * ( \textbf { x } + \textbf { t } + \textbf { 1 . } )$ ; if (fabs(t) $<$ EPS\*x && ${ \\mathrm { ~ j ~ } } > { \mathrm { ~ 0 ~ } } ,$ ) break; } return x; } onst Doub Beta::EPS $=$ numeric_limits<Doub>::epsilon(); onst Doub Beta::FPMIN $=$ numeric_limits<Doub>::min()/EPS;

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapters 6 and 26.[1]   
Pearson, E., and Johnson, N. 1968, Tables of the Incomplete Beta Function (Cambridge, UK: Cambridge University Press).

# 6.5 Bessel Functions of Integer Order

This section presents practical algorithms for computing various kinds of Bessel functions of integer order. In $\ S 6 . 6$ we deal with fractional order. Actually, the more complicated routines for fractional order work fine for integer order too. For integer order, however, the routines in this section are simpler and faster.

For any real $\nu$ , the Bessel function $J _ { \nu } ( x )$ can be defined by the series representation

$$
J _ { \nu } ( x ) = \left( { \frac { 1 } { 2 } } x \right) ^ { \nu } \sum _ { k = 0 } ^ { \infty } { \frac { ( - { \frac { 1 } { 4 } } x ^ { 2 } ) ^ { k } } { k ! \Gamma ( \nu + k + 1 ) } }
$$

The series converges for all $x$ , but it is not computationally very useful for $x \gg 1$ .

For $\nu$ not an integer, the Bessel function $Y _ { \nu } ( x )$ is given by

$$
Y _ { \nu } ( x ) = \frac { J _ { \nu } ( x ) \cos ( \nu \pi ) - J _ { - \nu } ( x ) } { \sin ( \nu \pi ) }
$$

The right-hand side goes to the correct limiting value $Y _ { n } ( x )$ as $\nu$ goes to some integer $n$ , but this is also not computationally useful.

For arguments $x \_ { \nu }$ , both Bessel functions look qualitatively like simple power laws, with the asymptotic forms for $0 < x \ll \nu$

$$
\begin{array} { l l l } { { J _ { \nu } ( x ) \sim \displaystyle { \frac { 1 } { \Gamma ( \nu + 1 ) } } \left( \frac { 1 } { 2 } x \right) ^ { \nu } } } & { { ~ \nu \geq 0 } } \\ { { \displaystyle Y _ { 0 } ( x ) \sim \frac { 2 } { \pi } \ln ( x ) } } & { { } } \\ { { \displaystyle Y _ { \nu } ( x ) \sim - \frac { \Gamma ( \nu ) } { \pi } \left( \frac { 1 } { 2 } x \right) ^ { - \nu } } } & { { ~ \nu > 0 } } \end{array}
$$

For $x > \nu$ , both Bessel functions look qualitatively like sine or cosine waves whose amplitude decays as $x ^ { - 1 / 2 }$ . The asymptotic forms for $x \gg \nu$ are

$$
\begin{array} { l } { { J _ { \nu } ( x ) \sim \displaystyle { \sqrt { \frac { 2 } { \pi x } } } \cos \left( x - \frac { 1 } { 2 } \nu \pi - \frac { 1 } { 4 } \pi \right) } } \\ { { { \cal Y } _ { \nu } ( x ) \sim \displaystyle { \sqrt { \frac { 2 } { \pi x } } } \sin \left( x - \frac { 1 } { 2 } \nu \pi - \frac { 1 } { 4 } \pi \right) } } \end{array}
$$

In the transition region where $x \sim \nu$ , the typical amplitudes of the Bessel functions are on the order

$$
\begin{array} { l } { { J _ { \nu } ( \nu ) \sim \displaystyle { \frac { 2 ^ { 1 / 3 } } { 3 ^ { 2 / 3 } \Gamma ( \frac 2 3 ) } \frac { 1 } { \nu ^ { 1 / 3 } } \sim \frac { 0 . 4 4 7 3 } { \nu ^ { 1 / 3 } } } } } \\ { { { } } } \\ { { Y _ { \nu } ( \nu ) \sim \displaystyle { - \frac { 2 ^ { 1 / 3 } } { 3 ^ { 1 / 6 } \Gamma ( \frac 2 3 ) } \frac { 1 } { \nu ^ { 1 / 3 } } \sim - \frac { 0 . 7 7 4 8 } { \nu ^ { 1 / 3 } } } } } \end{array}
$$

which holds asymptotically for large $\nu$ . Figure 6.5.1 plots the first few Bessel functions of each kind.

The Bessel functions satisfy the recurrence relations

$$
J _ { n + 1 } ( x ) = { \frac { 2 n } { x } } J _ { n } ( x ) - J _ { n - 1 } ( x )
$$

![](images/13d54d90b9747a75c776bde5199a54e6315e13ea0b36c434ad3a8ba60cdcd814.jpg)  
Figure 6.5.1. Bessel functions $J _ { 0 } ( x )$ through $J _ { 3 } ( x )$ and $Y _ { 0 } ( x )$ through $Y _ { 2 } ( x )$ .

and

$$
Y _ { n + 1 } ( x ) = { \frac { 2 n } { x } } Y _ { n } ( x ) - Y _ { n - 1 } ( x )
$$

As already mentioned in $\ S 5 . 4$ , only the second of these, (6.5.7), is stable in the direction of increasing $n$ for $x < n$ . The reason that (6.5.6) is unstable in the direction of increasing $n$ is simply that it is the same recurrence as (6.5.7): A small amount of “polluting” $Y _ { n }$ introduced by roundoff error will quickly come to swamp the desired $J _ { n }$ , according to equation (6.5.3).

A practical strategy for computing the Bessel functions of integer order divides into two tasks: first, how to compute $J _ { 0 } , J _ { 1 } , Y _ { 0 }$ , and $Y _ { 1 }$ ; and second, how to use the recurrence relations stably to find other $J$ ’s and $Y$ ’s. We treat the first task first.

For $x$ between zero and some arbitrary value (we will use the value 8), approximate $J _ { 0 } ( x )$ and $J _ { 1 } ( x )$ by rational functions in $x$ . Likewise approximate by rational functions the “regular part” of $Y _ { 0 } ( x )$ and $Y _ { 1 } ( x )$ , defined as

$$
Y _ { 0 } ( x ) - { \frac { 2 } { \pi } } J _ { 0 } ( x ) \ln ( x ) \qquad { \mathrm { a n d } } \qquad Y _ { 1 } ( x ) - { \frac { 2 } { \pi } } \left[ J _ { 1 } ( x ) \ln ( x ) - { \frac { 1 } { x } } \right]
$$

For $8 < x < \infty$ , use the approximating forms $( n = 0 , 1$ )

$$
{ \begin{array} { r } { J _ { n } ( x ) = { \sqrt { \frac { 2 } { \pi x } } } { \biggl [ } P _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \cos ( X _ { n } ) - Q _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \sin ( X _ { n } ) { \biggr ] } } \\ { Y _ { n } ( x ) = { \sqrt { \frac { 2 } { \pi x } } } { \biggl [ } P _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \sin ( X _ { n } ) + Q _ { n } { \biggl ( } { \frac { 8 } { x } } { \biggr ) } \cos ( X _ { n } ) { \biggr ] } } \end{array} }
$$

where

$$
X _ { n } \equiv x - \frac { 2 n + 1 } { 4 } \pi
$$

and where $P _ { 0 } , P _ { 1 } , Q _ { 0 }$ , and $Q _ { 1 }$ are each polynomials in their arguments, for $0 ~ <$ $8 / x < 1$ . The $P$ ’s are even polynomials, the $Q$ ’s odd.

In the routines below, the various coefficients were calculated in multiple precision so as to achieve full double precision in the relative error. (In the neighborhood of the zeros of the functions, it is the absolute error that is double precision.) However, because of roundoff, evaluating the approximations can lead to a loss of up to two significant digits.

One additional twist: The rational approximation for $\ 0 \ < \ x \ < \ 8$ is actually computed in the form [1]

$$
J _ { 0 } ( x ) = ( x ^ { 2 } - x _ { 0 } ^ { 2 } ) ( x ^ { 2 } - x _ { 1 } ^ { 2 } ) \frac { r ( x ^ { 2 } ) } { s ( x ^ { 2 } ) }
$$

and similarly for $J _ { 1 } , \ Y _ { 0 }$ and $Y _ { 1 }$ . Here $x _ { 0 }$ and $x _ { 1 }$ are the two zeros of $J _ { 0 }$ in the interval, and $r$ and $s$ are polynomials. The polynomial $r ( x ^ { 2 } )$ has alternating signs. Writing it in terms of $6 4 - x ^ { 2 }$ makes all the signs the same and reduces roundoff error. For the approximations (6.5.9) and (6.5.10), our coefficients are similar but not identical to those given by Hart [2].

The functions $J _ { 0 } , J _ { 1 } , Y _ { 0 }$ , and $Y _ { 1 }$ share a lot of code, so we package them as a single object Bessjy. The routines for higher $J _ { n }$ and $Y _ { n }$ are also member functions, with implementations discussed below. All the numerical coefficients are declared in Bessjy but defined (as a long list of constants) separately; the listing is in a Webnote [3].

# struct Bessjy {

static const Doub xj00,xj10,xj01,xj11,twoopi,pio4;   
static const Doub j0r[7],j0s[7],j0pn[5],j0pd[5],j0qn[5],j0qd[5];   
static const Doub j1r[7],j1s[7],j1pn[5],j1pd[5],j1qn[5],j1qd[5];   
static const Doub y0r[9],y0s[9],y0pn[5],y0pd[5],y0qn[5],y0qd[5];   
static const Doub y1r[8],y1s[8],y1pn[5],y1pd[5],y1qn[5],y1qd[5];   
Doub nump,denp,numq,denq,y,z,ax,xx;

# Doub j0(const Doub x) {

Returns the Bessel function $J _ { 0 } ( \mathbf { x } )$ for any real x.

if ((ax=abs(x)) $<$ 8.0) { Direct rational function fit. rat(x,j0r,j0s,6); return nump\*(y-xj00)\*(y-xj10)/denp; } else { Fitting function (6.5.9). asp(j0pn,j0pd,j0qn,j0qd,1.); return sqrt(twoopi/ax)\*(cos(xx)\*nump/denp-z\*sin(xx)\*numq/denq); } }

# Doub j1(const Doub x) {

Returns the Bessel function $J _ { 1 } ( \mathbf { x } )$ for any real x. if ((ax=abs(x)) $<$ 8.0) { Direct rational approximation. rat(x,j1r,j1s,6); return $\mathrm { { x * n u m p * ( y ^ { - } x j 0 1 ) * ( y ^ { - } x j 1 1 ) / d e n p } ; }$ } else { Fitting function (6.5.9). asp(j1pn,j1pd,j1qn,j1qd,3.); Doub ans $=$ sqrt(twoopi/ax) $^ *$ (cos(xx)\*nump/denp-z\*sin(xx)\*numq/denq); return $\mathrm { ~ x ~ } > \ 0 . 0$ ? ans : -ans; }

Doub y0(const Doub x) {   
Returns the Bessel function $Y _ { 0 } ( \mathbf { x } )$ for positive x. if $\mathrm { ~ ( ~ x ~ < ~ } 8 . 0 \mathrm { ) }$ ) Rational function approximation of (6.5.8). Doub $\mathrm { j } 0 \mathbf { x } \ = \ \mathrm { j } 0 \left( \mathbf { x } \right)$ ; rat(x,y0r,y0s,8); return nump/denp+twoopi\*j0x\*log(x); } else { Fitting function (6.5.10). $\mathtt { a x } \mathrm { = x }$ ; asp(y0pn,y0pd,y0qn,y0qd,1.); return sqrt(twoopi/x)\*(sin(xx)\*nump/denp+z\*cos(xx)\*numq/denq); }   
Doub y1(const Doub x) {   
Returns the Bessel function $Y _ { 1 } ( \mathbf { x } )$ for positive x. if $\mathit { \Theta } _ { \overline { { \mathbf { X } } } } ~ < ~ 8 . 0$ ) { Rational function approximation of (6.5.8). Doub $\mathrm { j } 1 \mathrm { x } \ = \ \mathrm { j } 1 ( \mathrm { x } )$ ; rat(x,y1r,y1s,7); return x\*nump/denp+twoopi\*(j1x\*log(x)-1.0/x); } else { Fitting function (6.5.10). $\mathtt { a x } \mathrm { = x }$ ; asp(y1pn,y1pd,y1qn,y1qd,3.); return sqrt(twoopi/x)\*(sin(xx)\*nump/denp+z\*cos(xx)\*numq/denq); }   
} Doub jn(const Int n, const Doub x);   
Returns the Bessel function $J _ { \mathtt { n } } ( \mathbf { x } )$ for any real x and integer $\mathbf { n } \geq \mathbf { 0 }$ . Doub yn(const Int n, const Doub x);   
Returns the Bessel function $Y _ { \mathrm { { n } } } ( \mathbf { x } )$ for any positive x and integer $\mathbf { n } \geq \mathbf { 0 }$ .

void rat(const Doub x, const Doub \*r, const Doub \*s, const Int n) { Common code: Evaluates rational approximation.

$\begin{array} { r } { \mathrm { ~ y ~ } = \mathrm { ~ x * x } , } \end{array}$ $\scriptstyle 2 = 6 4 . 0 - y$ ; nump ${ } = \mathbf { r }$ [n]; denp=s[n]; for (Int $\dot { \tt 1 } = { \tt n } - 1$ ; $\scriptstyle \dot { 1 } > = 0$ ;i--) nump=nump\*z+r[i]; denp=denp\*y+s[i]; } }

void asp(const Doub \*pn, const Doub \*pd, const Doub \*qn, const Doub \*qd,   
Common code: Evaluates asymptotic approximation. const Doub fac) { $z { = } 8$ .0/ax; y=z\*z; xx=ax-fac\*pio4; nump=pn[4]; denp=pd[4]; numq=qn[4]; denq=qd[4]; for (Int i=3;i>=0;i--) { nump $\mid =$ nump\*y+pn[i]; denp=denp\*y+pd[i]; numq=numq\*y+qn[i]; denq=denq\*y+qd[i]; }   
}

We now turn to the second task, namely, how to use the recurrence formulas (6.5.6) and (6.5.7) to get the Bessel functions $J _ { n } ( x )$ and $Y _ { n } ( x )$ for $n \geq 2$ . The latter of these is straightforward, since its upward recurrence is always stable:

Doub Bessjy::yn(const Int n, const Doub x)   
Returns the Bessel function $Y _ { \mathrm { n } } ( \mathbf { x } )$ for any positive $\mathbf { x }$ and integer $\mathbf { n } \geq \mathbf { 0 }$ . {

Int j; Doub by,bym,byp,tox; if ( $\scriptstyle \mathtt { n } = = 0$ ) return y0(x); if ( $\scriptstyle \mathtt { n } = = 1$ ) return y1(x); tox $^ { = 2 }$ .0/x; by=y1(x); bym=y0(x); for ( $\scriptstyle { \dot { \mathsf { J } } } = 1$ ;j<n;j++) { byp=j\*tox\*by-bym; bym=by; by $=$ byp; } return by; }

The cost of this algorithm is the calls to y1 and y0 (which generate a call to each of ${ \dot { \mathsf { J } } } ^ { 1 }$ and ${ \bf j } 0$ ), plus $O ( n )$ operations in the recurrence.

For $J _ { n } ( x )$ , things are a bit more complicated. We can start the recurrence upward on $n$ from $J _ { 0 }$ and $J _ { 1 }$ , but it will remain stable only while $n$ does not exceed $x$ . This is, however, just fine for calls with large $x$ and small $n$ , a case that occurs frequently in practice.

The harder case to provide for is that with $x \ < \ n$ . The best thing to do here is to use Miller’s algorithm (see discussion preceding equation 5.4.16), applying the recurrence downward from some arbitrary starting value and making use of the upward-unstable nature of the recurrence to put us onto the correct solution. When we finally arrive at $J _ { 0 }$ or $J _ { 1 }$ we are able to normalize the solution with the sum (5.4.16) accumulated along the way.

The only subtlety is in deciding at how large an $n$ we need start the downward recurrence so as to obtain a desired accuracy by the time we reach the $n$ that we really want. If you play with the asymptotic forms (6.5.3) and (6.5.5), you should be able to convince yourself that the answer is to start larger than the desired $n$ by an additive amount of order $[ \mathrm { c o n s t a n t } \times n ] ^ { 1 / 2 }$ , where the square root of the constant is, very roughly, the number of significant figures of accuracy.

The above considerations lead to the following function.

# bessel.h

Doub Bessjy::jn(const Int n, const Doub x) Returns the Bessel function $J _ { \mathrm { { n } } } ( \mathbf { x } )$ for any real $\mathbf { x }$ and integer $\mathbf { n } \geq \mathbf { 0 }$ . {

const Doub $\mathtt { A C C = 1 6 0 . 0 }$ ; ACC determines accuracy.   
const Int IEXP $^ { 1 } =$ numeric_limits<Doub>::max_exponent/2;   
Bool jsum;   
Int j,k,m;   
Doub ax,bj,bjm,bjp,dum,sum,tox,ans;   
if ( $\scriptstyle \mathtt { n } = = 0$ ) return ${ \bf j } 0 ( { \bf x } )$ ;   
if ( $\scriptstyle \mathbf { \cdot n } = = 1$ ) return j1 $\left( \mathbf { \boldsymbol { x } } \right)$ ;   
ax=abs(x);   
if (ax\*ax $< =$ 8.0\*numeric_limits<Doub>::min()) return 0.0;   
else if (ax $>$ Doub(n)) { Upwards recurrence from $J _ { 0 }$ and $J _ { 1 }$ .   
tox $^ { = 2 }$ .0/ax;

bjm=j0(ax); bj=j1(ax); for (j=1;j<n;j++) { bjp=j\*tox\*bj-bjm; bjm=bj; bj=bjp; } ans $=$ bj; } else { Downward recurrence from an even m here tox $^ { - 2 }$ .0/ax; computed. ${ \tt m } = 2 *$ ((n+Int(sqrt(ACC\*n)))/2); jsum=false; jsum will alternate between false and true; bjp=ans $=$ sum=0.0; when it is true, we accumulate in sum bj=1.0; the even terms in (5.4.16). for (j=m;j>0;j--) { The downward recurrence. bjm=j\*tox\*bj-bjp; bjp=bj; bj=bjm; dum=frexp(bj,&k); if (k $>$ IEXP) { Renormalize to prevent overflows. bj ${ } = 1$ dexp(bj,-IEXP); bjp $\mid =$ ldexp(bjp,-IEXP); ans $: =$ ldexp(ans,-IEXP); sum=ldexp(sum,-IEXP); if (jsum) sum $+ =$ bj; Accumulate the sum. jsum=!jsum; Change false to true or vice versa. if (j == n) ans=bjp; Save the unnormalized answer. } sum $^ { 1 = 2 }$ .0\*sum-bj; Compute (5.4.16) ans /= sum; and use it to normalize the answer. } return $\texttt { x } < 0 . 0$ && (n & 1) ? -ans : ans;

The function ldexp, used above, is a standard C and $\mathrm { C } { + } { + }$ library function for scaling the binary exponent of a number.

# 6.5.1 Modified Bessel Functions of Integer Order

The modified Bessel functions $I _ { n } ( x )$ and $K _ { n } ( x )$ are equivalent to the usual Bessel functions $J _ { n }$ and $Y _ { n }$ evaluated for purely imaginary arguments. In detail, the relationship is

$$
\begin{array} { l } { { I _ { n } ( x ) = ( - i ) ^ { n } J _ { n } ( i x ) } } \\ { { K _ { n } ( x ) = \displaystyle \frac { \pi } { 2 } i ^ { n + 1 } [ J _ { n } ( i x ) + i Y _ { n } ( i x ) ] } } \end{array}
$$

The particular choice of prefactor and of the linear combination of $J _ { n }$ and $Y _ { n }$ to form $K _ { n }$ are simply choices that make the functions real-valued for real arguments $x$ .

For small arguments $x ~ \ll ~ n$ , both $I _ { n } ( x )$ and $K _ { n } ( x )$ become, asymptotically, simple powers of their arguments

$$
{ \begin{array} { l } { \displaystyle I _ { n } ( x ) \approx { \frac { 1 } { n ! } } \left( { \frac { x } { 2 } } \right) ^ { n } \qquad n \geq 0 } \\ { \displaystyle K _ { 0 } ( x ) \approx - \ln ( x ) } \\ { \displaystyle K _ { n } ( x ) \approx { \frac { ( n - 1 ) ! } { 2 } } \left( { \frac { x } { 2 } } \right) ^ { - n } \qquad n > 0 } \end{array} }
$$

These expressions are virtually identical to those for $J _ { n } ( x )$ and $Y _ { n } ( x )$ in this region, except for the factor of $- 2 / \pi$ difference between $Y _ { n } ( x )$ and $K _ { n } ( x )$ . In the region $x \gg n$ , however, the modified functions have quite different behavior than the Bessel functions,

$$
\begin{array} { l } { { I _ { n } ( x ) \approx \displaystyle \frac { 1 } { \sqrt { 2 \pi x } } \exp ( x ) } } \\ { { K _ { n } ( x ) \approx \displaystyle \frac { \pi } { \sqrt { 2 \pi x } } \exp ( - x ) } } \end{array}
$$

The modified functions evidently have exponential rather than sinusoidal behavior for large arguments (see Figure 6.5.2). Rational approximations analogous to those for the $J$ and $Y$ Bessel functions are efficient for computing $I _ { 0 }$ , $I _ { 1 }$ , $K _ { 0 }$ , and $K _ { 1 }$ . The corresponding routines are packaged as an object Bessik. The routines are similar to those in [1], although different in detail. (All the constants are again listed in a Webnote [3].)

# struct Bessik {

static const Doub i0p[14],i0q[5],i0pp[5],i0qq[6];   
static const Doub i1p[14],i1q[5],i1pp[5],i1qq[6];   
static const Doub k0pi[5],k0qi[3],k0p[5],k0q[3],k0pp[8],k0qq[8];   
static const Doub k1pi[5],k1qi[3],k1p[5],k1q[3],k1pp[8],k1qq[8];   
Doub y,z,ax,term;   
Doub i0(const Doub x) {   
Returns the modified Bessel function $I _ { 0 } ( \mathbf { x } )$ for any real $\mathbf { x }$ . if ((ax=abs(x)) $<$ 15.0) { Rational approximation. $\begin{array} { r } { \mathbf { y } ~ = ~ \mathbf { x } * \mathbf { x } } \end{array}$ ; return poly(i0p,13,y)/poly(i0q,4,225.-y); } else { Rational approximation with $e ^ { x } / { \sqrt { x } }$ factored out. $z { = } 1$ .0-15.0/ax; return exp(ax)\*poly(i0pp,4,z)/(poly(i0qq,5,z)\*sqrt(ax)); }   
}   
Doub i1(const Doub x) {   
Returns the modified Bessel function $I _ { 1 } ( \mathbf { x } )$ for any real $\mathbf { x }$ . if ((ax=abs(x)) $<$ 15.0) { Rational approximation. $\mathtt { y } \mathtt { = x } \ast \mathtt { x }$ ; return x\*poly(i1p,13,y)/poly(i1q,4,225.-y); } else { Rational approximation with $e ^ { x } / { \sqrt { x } }$ factored out. z=1.0-15.0/ax; Doub ans $=$ exp(ax)\*poly(i1pp,4,z)/(poly(i1qq,5,z)\*sqrt(ax)); return $\mathrm { ~ x ~ } > \ 0 . 0$ ? ans : -ans; }   
}   
Doub k0(const Doub x) {   
Returns the modified Bessel function $K _ { 0 } ( \mathbf { x } )$ for positive real x. if $( \textbf { x } < = \textbf { 1 } . 0 )$ ) { Use two rational approximations. ${ \bf z } = { \bf x } * { \bf x }$ ; term $=$ poly(k0pi,4,z)\*log(x)/poly(k0qi,2,1.-z); return poly(k0p,4,z)/poly(k0q,2,1.-z)-term; } else { Rational approximation with $e ^ { - x } / { \sqrt { x } }$ factored $\scriptstyle { z = 1 . 0 / \mathbf { x } }$ ; out. return exp(-x)\*poly(k0pp,7,z)/(poly(k0qq,7,z)\*sqrt(x)); }   
Doub k1(const Doub x) {   
Returns the modified Bessel function $K _ { 1 } ( \mathbf { x } )$ for positive real x. if ( $\mathit { \check { x } } < = \mathit { 1 . 0 } \rangle$ ) { Use two rational approximations. ${ z } = \mathbf { x } * \mathbf { x }$ ; term $=$ poly(k1pi,4,z)\*log(x)/poly(k1qi,2,1.-z); return x\*(poly(k1p,4,z)/poly(k1q,2,1.-z)+term) $^ { + 1 }$ ./x; } else { Rational approximation with $e ^ { - x } / { \sqrt { x } }$ factored $z { = } 1$ .0/x; out. return exp(-x)\*poly(k1pp,7,z)/(poly(k1qq,7,z)\*sqrt(x)); }   
} Doub in(const Int n, const Doub x);   
Returns the modified Bessel function $I _ { \mathrm { { n } } } ( \mathbf { x } )$ for any real $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ . Doub kn(const Int n, const Doub x);   
Returns the modified Bessel function $K _ { \mathfrak { n } } ( \mathbf { x } )$ for positive $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ .

![](images/4f814f447313a9e5005e7a798908c820e15655723b52b327ba57005a123aa308.jpg)  
Figure 6.5.2. Modified Bessel functions $I _ { 0 } ( x )$ through $I _ { 3 } ( x )$ , and $K _ { 0 } ( x )$ through $K _ { 2 } ( x )$ .

inline Doub poly(const Doub \*cof, const Int n, const Doub x) { Common code: Evaluate a polynomial. Doub ans $=$ cof[n]; for (Int i=n $- 1 ; \mathrm { i } > = 0 ; \mathrm { i } -- )$ ans $=$ ans\*x+cof[i]; return ans; } };

The recurrence relation for $I _ { n } ( x )$ and $K _ { n } ( x )$ is the same as that for $J _ { n } ( x )$ and $Y _ { n } ( x )$ provided that $i x$ is substituted for $x$ . This has the effect of changing a sign in the relation,

$$
\begin{array} { l } { { I _ { n + 1 } ( x ) = - \displaystyle \left( \frac { 2 n } { x } \right) I _ { n } ( x ) + I _ { n - 1 } ( x ) } } \\ { { { } } } \\ { { K _ { n + 1 } ( x ) = + \displaystyle \left( \frac { 2 n } { x } \right) K _ { n } ( x ) + K _ { n - 1 } ( x ) } } \end{array}
$$

These relations are always unstable for upward recurrence. For $K _ { n }$ , itself growing, this presents no problem. The implementation is

# bessel.h

Doub Bessik::kn(const Int n, const Doub x) Returns the modified Bessel function $K _ { \mathfrak { n } } ( \mathbf { x } )$ for positive $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ . {

Int j; Doub bk,bkm,bkp,tox; if ( $\scriptstyle \mathtt { n } = = 0$ ) return k0 $\mathbf { \Psi } ( \mathbf { x } )$ ; if ( $\scriptstyle \mathtt { n } = = 1$ ) return k1 $\mathbf { \Psi } ( \mathbf { x } )$ ; to $= 2$ .0/x; bkm=k0(x); bk=k1(x); for ( $\mathrm { j } = 1$ ;j<n;j++) { bkp=bkm+j\*tox\*bk; bkm $\mathbf { \tau } _ { 1 } =$ bk; bk $\ c =$ bkp; 1 return bk; }

For $I _ { n }$ , the strategy of downward recursion is required once again, and the starting point for the recursion may be chosen in the same manner as for the routine Bessjy::jn. The only fundamental difference is that the normalization formula for $I _ { n } ( x )$ has an alternating minus sign in successive terms, which again arises from the substitution of $i x$ for $x$ in the formula used previously for $J _ { n }$ :

$$
1 = I _ { 0 } ( x ) - 2 I _ { 2 } ( x ) + 2 I _ { 4 } ( x ) - 2 I _ { 6 } ( x ) + \cdots
$$

In fact, we prefer simply to normalize with a call to i0.

Doub Bessik::in(const Int n, const Doub x) Returns the modified Bessel function $I _ { \mathrm { { n } } } ( \mathbf { x } )$ for any real $\mathbf { x }$ and $\mathbf { n } \geq \mathbf { 0 }$ . {

const Doub ACC=200.0; ACC determines accuracy.   
const Int IEXP $^ { \prime } =$ numeric_limits<Doub>::max_exponent/2;   
Int j,k;   
Doub bi,bim,bip,dum,tox,ans;   
if ( $\scriptstyle \cdot = = 0$ ) return i0 $\left( \mathbf { \boldsymbol { x } } \right)$ ;   
if ( $\scriptstyle \mathbf { \cdot n } = = 1$ ) return i1 $\left( \mathbf { \boldsymbol { x } } \right)$ ;   
if (x\*x <= 8. $^ { 0 * }$ numeric_limits<Doub>::min()) return 0.0;   
else { tox $^ { - 2 }$ .0/abs(x); bip $\mid =$ ans=0.0; b $\lrcorner = 1$ .0; for (j $= 2 *$ ( $\mathrm { \Omega } \mathrm { n } +$ Int(sqrt(ACC $\ast \mathrm { n } ,$ )));j>0;j--) { Downward recurrence. bim bip+j\*tox\*bi; bip=bi; bi=bim; dum=frexp(bi,&k); if (k $>$ IEXP) { Renormalize to prevent overflows. ans $=$ ldexp(ans,-IEXP); bi $=$ ldexp(bi,-IEXP); bip=ldexp(bip,-IEXP);

} if (j == n) ans=bip; 1 ans $\ast =$ i0(x)/bi; Normalize with bessi0. return $\mathrm { ~ z ~ < ~ 0 ~ . 0 ~ }$ && (n & 1) ? -ans : ans; } }

The function ldexp, used above, is a standard C and $\mathrm { C } { + } { + }$ library function for scaling the binary exponent of a number.

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 9.   
Carrier, G.F., Krook, M. and Pearson, C.E. 1966, Functions of a Complex Variable (New York: McGraw-Hill), pp. 220ff.   
SPECFUN, $^ { 2 0 0 7 + }$ ,athttp://www.netlib.org/specfun.[1]   
Hart, J.F., et al. 1968, Computer Approximations (New York: Wiley), $\ S 6 . 8$ , p. 141.[2]   
Numerical Recipes Software 2007, “Coefficients Used in the Bessjy and Bessik Objects,” Numerical Recipes Webnote No.7,at http://www.nr.com/webnotes?7 [3]

# 6.6 Bessel Functions of Fractional Order, Airy Functions, Spherical Bessel Functions

Many algorithms have been proposed for computing Bessel functions of fractional order numerically. Most of them are, in fact, not very good in practice. The routines given here are rather complicated, but they can be recommended wholeheartedly.

# 6.6.1 Ordinary Bessel Functions

The basic idea is Steed’s method, which was originally developed [1] for Coulomb wave functions. The method calculates $J _ { \nu }$ , $J _ { \nu } ^ { \prime }$ , $Y _ { \nu }$ , and $\bar { Y } _ { \nu } ^ { \prime }$ simultaneously, and so involves four relations among these functions. Three of the relations come from two continued fractions, one of which is complex. The fourth is provided by the Wronskian relation

$$
W \equiv J _ { \nu } Y _ { \nu } ^ { \prime } - Y _ { \nu } J _ { \nu } ^ { \prime } = { \frac { 2 } { \pi x } }
$$

The first continued fraction, CF1, is defined by

$$
\begin{array}{c} f _ { \nu } \equiv \frac { J _ { \nu } ^ { \prime } } { J _ { \nu } } = \frac { \nu } { x } - \frac { J _ { \nu + 1 } } { J _ { \nu } }  \\ { = \frac { \nu } { x } - \frac { 1 } { 2 ( \nu + 1 ) / x - } \frac { 1 } { 2 ( \nu + 2 ) / x - } \dots } \end{array}
$$

You can easily derive it from the three-term recurrence relation for Bessel functions: Start with equation (6.5.6) and use equation (5.4.18). Forward evaluation of the continued fraction by one of the methods of $\ S 5 . 2$ is essentially equivalent to backward recurrence of the recurrence relation. The rate of convergence of CF1 is determined by the position of the turning point $x _ { \mathrm { t p } } = \sqrt { \nu ( \nu + 1 ) } \approx \nu$ , beyond which the Bessel functions become oscillatory. If $x \lesssim x _ { \mathrm { t p } }$ , convergence is very rapid. If $x \gtrsim x _ { \mathrm { t p } }$ , then each iteration of the continued fraction effectively increases $\nu$ by one until $x \lesssim x _ { \mathrm { t p } }$ ; thereafter rapid convergence sets in. Thus the number of iterations of CF1 is of order $x$ for large $x$ . In the routine besseljy we set the maximum allowed number of iterations to 10,000. For larger $x$ , you can use the usual asymptotic expressions for Bessel functions.

One can show that the sign of $J _ { \nu }$ is the same as the sign of the denominator of CF1 once it has converged.

The complex continued fraction CF2 is defined by

$$
p + i q \equiv \frac { J _ { \nu } ^ { \prime } + i Y _ { \nu } ^ { \prime } } { J _ { \nu } + i Y _ { \nu } } = - \frac { 1 } { 2 x } + i + \frac { i } { x } \ : \frac { ( 1 / 2 ) ^ { 2 } - \nu ^ { 2 } } { 2 ( x + i ) + } \ : \frac { ( 3 / 2 ) ^ { 2 } - \nu ^ { 2 } } { 2 ( x + 2 i ) + } \ : \cdots
$$

(We sketch the derivation of CF2 in the analogous case of modified Bessel functions in the next subsection.) This continued fraction converges rapidly for $x \gtrsim x _ { \mathrm { t p } }$ , while convergence fails as $x \to 0$ . We have to adopt a special method for small $x$ , which we describe below. For $x$ not too small, we can ensure that $x \gtrsim x _ { \mathrm { t p } }$ by a stable recurrence of $J _ { \nu }$ and $J _ { \nu } ^ { \prime }$ downward to a value $\nu = \mu \lesssim x$ , thus yielding the ratio $f _ { \mu }$ at this lower value of $\nu$ . This is the stable direction for the recurrence relation. The initial values for the recurrence are

$$
J _ { \nu } = \mathrm { a r b i t r a r y } , \qquad J _ { \nu } ^ { \prime } = f _ { \nu } J _ { \nu } ,
$$

with the sign of the arbitrary initial value of $J _ { \nu }$ chosen to be the sign of the denominator of CF1. Choosing the initial value of $J _ { \nu }$ very small minimizes the possibility of overflow during the recurrence. The recurrence relations are

$$
\begin{array} { l } { { J _ { \nu - 1 } = \displaystyle \frac { \nu } { x } J _ { \nu } + J _ { \nu } ^ { \prime } } } \\ { { \ J _ { \nu - 1 } ^ { \prime } = \displaystyle \frac { \nu - 1 } { x } J _ { \nu - 1 } - J _ { \nu } } } \end{array}
$$

Once CF2 has been evaluated at $\nu = \mu$ , then with the Wronskian (6.6.1) we have enough relations to solve for all four quantities. The formulas are simplified by introducing the quantity

$$
\gamma \equiv \frac { p - f _ { \mu } } { q }
$$

Then

$$
\begin{array} { l } { { J _ { \mu } = \pm \left( \displaystyle \frac { W } { q + \gamma ( p - f _ { \mu } ) } \right) ^ { 1 / 2 } } } \\ { { J _ { \mu } ^ { \prime } = f _ { \mu } J _ { \mu } } } \\ { { Y _ { \mu } = \gamma J _ { \mu } } } \\ { { Y _ { \mu } ^ { \prime } = Y _ { \mu } \left( p + \displaystyle \frac { q } { \gamma } \right) } } \end{array}
$$

The sign of $J _ { \mu }$ in (6.6.7) is chosen to be the same as the sign of the initial $J _ { \nu }$ in (6.6.4).

Once all four functions have been determined at the value $\nu = \mu$ , we can find them at the original value of $\nu$ . For $J _ { \nu }$ and $J _ { \nu } ^ { \prime }$ , simply scale the values in (6.6.4) by the ratio of (6.6.7) to the value found after applying the recurrence (6.6.5). The quantities $Y _ { \nu }$ and $Y _ { \nu } ^ { \prime }$ can be found by starting with the values in (6.6.9) and (6.6.10) and using the stable upward recurrence

$$
Y _ { \nu + 1 } = { \frac { 2 \nu } { x } } Y _ { \nu } - Y _ { \nu - 1 }
$$

together with the relation

$$
Y _ { \nu } ^ { \prime } = { \frac { \nu } { x } } Y _ { \nu } - Y _ { \nu + 1 }
$$

Now turn to the case of small $x$ , when CF2 is not suitable. Temme [2] has given a good method of evaluating $Y _ { \nu }$ and $Y _ { \nu + 1 }$ , and hence $Y _ { \nu } ^ { \prime }$ from (6.6.12), by series expansions that

accurately handle the singularity as $x \to 0$ . The expansions work only for $| \nu | \leq 1 / 2$ , and so now the recurrence (6.6.5) is used to evaluate $f _ { \nu }$ at a value $\nu = \mu$ in this interval. Then one calculates $J _ { \mu }$ from

$$
J _ { \mu } = \frac { W } { Y _ { \mu } ^ { \prime } - Y _ { \mu } f _ { \mu } }
$$

and $J _ { \mu } ^ { \prime }$ from (6.6.8). The values at the original value of $\nu$ are determined by scaling as before, and the $Y$ ’s are recurred up as before.

Temme’s series are

$$
Y _ { \nu } = - \sum _ { k = 0 } ^ { \infty } c _ { k } g _ { k } \qquad Y _ { \nu + 1 } = - \frac { 2 } { x } \sum _ { k = 0 } ^ { \infty } c _ { k } h _ { k }
$$

Here

$$
c _ { k } = { \frac { ( - x ^ { 2 } / 4 ) ^ { k } } { k ! } }
$$

while the coefficients $g _ { k }$ and $h _ { k }$ are defined in terms of quantities $p _ { k } , q _ { k }$ , and $f _ { k }$ that can be found by recursion:

$$
{ \begin{array} { r l } & { g _ { k } = f _ { k } + { \frac { 2 } { \nu } } \sin ^ { 2 } \left( { \frac { \nu \pi } { 2 } } \right) q _ { k } } \\ & { h _ { k } = - k g _ { k } + p _ { k } } \\ & { p _ { k } = { \frac { p _ { k - 1 } } { k - \nu } } } \\ & { q _ { k } = { \frac { q _ { k - 1 } } { k + \nu } } } \\ & { f _ { k } = { \frac { k f _ { k - 1 } + p _ { k - 1 } + q _ { k - 1 } } { k ^ { 2 } - \nu ^ { 2 } } } } \end{array} }
$$

The initial values for the recurrences are

$$
\begin{array} { l } { { p _ { 0 } = \displaystyle \frac { 1 } { \pi } \left( \frac { x } { 2 } \right) ^ { - \nu } \Gamma ( 1 + \nu ) } } \\ { { q _ { 0 } = \displaystyle \frac { 1 } { \pi } \left( \frac { x } { 2 } \right) ^ { \nu } \Gamma ( 1 - \nu ) } } \\ { { f _ { 0 } = \displaystyle \frac { 2 } { \pi } \frac { \nu \pi } { \sin \nu \pi } \left[ \cosh \sigma \Gamma _ { 1 } ( \nu ) + \frac { \sinh \sigma } { \sigma } \ln \left( \frac { 2 } { x } \right) \Gamma _ { 2 } ( \nu ) \right] } } \end{array}
$$

with

$$
{ \begin{array} { c } { \displaystyle \sigma = \nu \ln \left( { \frac { 2 } { x } } \right) } \\ { \displaystyle \Gamma _ { 1 } ( \nu ) = { \frac { 1 } { 2 \nu } } \left[ { \frac { 1 } { \Gamma ( 1 - \nu ) } } - { \frac { 1 } { \Gamma ( 1 + \nu ) } } \right] } \\ { \displaystyle \Gamma _ { 2 } ( \nu ) = { \frac { 1 } { 2 } } \left[ { \frac { 1 } { \Gamma ( 1 - \nu ) } } + { \frac { 1 } { \Gamma ( 1 + \nu ) } } \right] } \end{array} }
$$

The whole point of writing the formulas in this way is that the potential problems as $\nu  0$ can be controlled by evaluating $\nu \pi / \sin \nu \pi$ , $\sinh \sigma / \sigma$ , and $\Gamma _ { 1 }$ carefully. In particular, Temme gives Chebyshev expansions for $\Gamma _ { 1 } ( \nu )$ and $\Gamma _ { 2 } ( \nu )$ . We have rearranged his expansion for $\Gamma _ { 1 }$ to be explicitly an even series in $\nu$ for more efficient evaluation, as explained in $\ S 5 . 8$ .

Because $J _ { \nu }$ , $Y _ { \nu }$ , $J _ { \nu } ^ { \prime }$ , and $Y _ { \nu } ^ { \prime }$ are all calculated simultaneously, a single void function sets them all. You then grab those that you need directly from the object. Alternatively, the functions $\dot { \mathtt { J } } \mathtt { n u }$ and ynu can be used. (We’ve omitted similar helper functions for the derivatives, but you can easily add them.) The object Bessel contains various other methods that will be discussed below.

The routines assume $\nu \geq 0$ . For negative $\nu$ you can use the reflection formulas

$$
\begin{array} { r } { J _ { - \nu } = \cos \nu \pi J _ { \nu } - \sin \nu \pi Y _ { \nu } } \\ { Y _ { - \nu } = \sin \nu \pi J _ { \nu } + \cos \nu \pi Y _ { \nu } } \end{array}
$$

The routine also assumes $x > 0$ . For $x < 0$ , the functions are in general complex but expressible in terms of functions with $x > 0$ . For $x = 0$ , $Y _ { \nu }$ is singular. The complex arithmetic is carried out explicitly with real variables.

# struct Bessel {

Object for Bessel functions of arbitrary order $\nu$ , and related functions.

static const Int NUSE1 $^ { . = 7 }$ , NUSE2 $\scriptstyle : = 8$ ;   
static const Doub c1[NUSE1],c2[NUSE2];   
Doub xo,nuo;   
Doub jo,yo,jpo,ypo;   
Doub io,ko,ipo,kpo;   
Doub aio,bio,aipo,bipo;   
Doub sphjo,sphyo,sphjpo,sphypo;   
Int sphno;

Bessel() : xo(9.99e99), nuo(9.99e99), sphno(-9999) {} Default constructor. No arguments.

void besseljy(const Doub nu, const Doub x); Calculate Bessel functions $J _ { \nu } ( x )$ and $Y _ { \nu } ( x )$ and their derivatives. void besselik(const Doub $\mathbf { n u }$ , const Doub x) Calculate Bessel functions $I _ { \nu } ( x )$ and $K _ { \nu } ( x )$ and their derivatives.

Doub jnu(const Doub nu, const Doub x) {   
Simple interface returning $J _ { \nu } ( x )$ . if (nu $! =$ nuo $| \textbf { | } \textbf { x } : = \textbf { x } 0 \ $ ) besseljy(nu,x); return jo;   
}   
Doub ynu(const Doub nu, const Doub x) {   
Simple interface returning $Y _ { \nu } ( x )$ . if (nu $! =$ nuo $| \mathbf { \Psi } | \subset \mathrm { ~ \mathbb { X } ~ } : = \mathrm { ~ \mathbb { X } \circ ~ }$ ) besseljy(nu,x); return yo;   
}   
Doub inu(const Doub nu, const Doub x) {   
Simple interface returning $I _ { \nu } ( x )$ . if (nu $! =$ nuo $| \textbf { | } \textbf { x } : = \textbf { x } 0 \ $ ) besselik(nu,x); return io;   
}   
Doub knu(const Doub nu, const Doub x) {   
Simple interface returning $K _ { \nu } ( x )$ . if $\mathrm {  ~ \ l u ~ } \ ! = \ \mathrm { \ n u o ~ } \ | \ | \ \mathrm {  ~ \ x ~ } \ ! = \ \mathrm { \ x o }$ ) besselik(nu,x); return ko;   
} void airy(const Doub x);   
Calculate Airy functions $\operatorname { A i } ( x )$ and $\operatorname { B i } ( x )$ and their derivatives.   
Doub airy_ai(const Doub x);   
Simple interface returning $\operatorname { A i } ( x )$ .   
Doub airy_bi(const Doub x);   
Simple interface returning $\operatorname { B i } ( x )$ . void sphbes(const Int n, const Doub x);   
Calculate spherical Bessel functions $j _ { n } ( x )$ and $y _ { n } ( x )$ and their derivatives.   
Doub sphbesj(const Int n, const Doub x);   
Simple interface returning $j _ { n } ( x )$ .   
Doub sphbesy(const Int $\mathbf { n }$ , const Doub x);   
Simple interface returning $y _ { n } ( x )$ .

inline Doub chebev(const Doub \*c, const Int m, const Doub x) { Utility used by besseljy and besselik, evaluates Chebyshev series.

Doub d=0.0,dd $\mathtt { = 0 }$ .0,sv; Int j; for (j=m-1;j>0;j--) { sv=d; d=2.\*x\*d-dd+c[j]; dd=sv; } return x\*d-dd+0.5\*c[0]; } };

const Doub Bessel::c1[7] $= \ \ell - 1$ .142022680371168e0,6.5165112670737e-3,   
3.087090173086e-4,-3.4706269649e-6,6.9437664e-9,3.67795e-11, -1.356e-13}; const Doub Bessel::c2[8] $=$ {1.843740587300905e0,-7.68528408447867e-2,   
1.2719271366546e-3,-4.9717367042e-6,-3.31261198e-8,2.423096e-10, -1.702e-13,-1.49e-15};

The code listing for Bessel::besseljy is in a Webnote [4].

# 6.6.2 Modified Bessel Functions

Steed’s method does not work for modified Bessel functions because in this case CF2 is purely imaginary and we have only three relations among the four functions. Temme [3] has given a normalization condition that provides the fourth relation.

The Wronskian relation is

$$
W \equiv I _ { \nu } K _ { \nu } ^ { \prime } - K _ { \nu } I _ { \nu } ^ { \prime } = - { \frac { 1 } { x } }
$$

The continued fraction CF1 becomes

$$
f _ { \nu } \equiv \frac { I _ { \nu } ^ { \prime } } { I _ { \nu } } = \frac { \nu } { x } + \frac { 1 } { 2 ( \nu + 1 ) / x + } \frac { 1 } { 2 ( \nu + 2 ) / x + } \cdots
$$

To get CF2 and the normalization condition in a convenient form, consider the sequence of confluent hypergeometric functions

$$
z _ { n } ( x ) = U ( \nu + 1 / 2 + n , 2 \nu + 1 , 2 x )
$$

for fixed $\nu$ . Then

$$
\begin{array} { c } { { K _ { \nu } ( x ) = \pi ^ { 1 / 2 } ( 2 x ) ^ { \nu } e ^ { - x } z _ { 0 } ( x ) } } \\ { { \displaystyle \frac { K _ { \nu + 1 } ( x ) } { K _ { \nu } ( x ) } = \frac { 1 } { x } \left[ \nu + \frac { 1 } { 2 } + x + \left( \nu ^ { 2 } - \frac { 1 } { 4 } \right) \frac { z _ { 1 } } { z _ { 0 } } \right] } } \end{array}
$$

Equation (6.6.23) is the standard expression for $K _ { \nu }$ in terms of a confluent hypergeometric function, while equation (6.6.24) follows from relations between contiguous confluent hypergeometric functions (equations 13.4.16 and 13.4.18 in Ref. [5]). Now the functions $z _ { n }$ satisfy the three-term recurrence relation (equation 13.4.15 in Ref. [5])

$$
z _ { n - 1 } ( x ) = b _ { n } z _ { n } ( x ) + a _ { n + 1 } z _ { n + 1 }
$$

with

$$
\begin{array} { c } { b _ { n } = 2 ( n + x ) } \\ { a _ { n + 1 } = - [ ( n + 1 / 2 ) ^ { 2 } - \nu ^ { 2 } ] } \end{array}
$$

Following the steps leading to equation (5.4.18), we get the continued fraction CF2

$$
{ \frac { z _ { 1 } } { z _ { 0 } } } = { \frac { 1 } { b _ { 1 } + } } { \frac { a _ { 2 } } { b _ { 2 } + } } \cdots
$$

from which (6.6.24) gives $K _ { \nu + 1 } / K _ { \nu }$ and thus $K _ { \nu } ^ { \prime } / K _ { \nu }$

Temme’s normalization condition is that

$$
\sum _ { n = 0 } ^ { \infty } C _ { n } z _ { n } = \left( \frac { 1 } { 2 x } \right) ^ { \nu + 1 / 2 }
$$

where

$$
C _ { n } = { \frac { ( - 1 ) ^ { n } } { n ! } } { \frac { \Gamma ( \nu + 1 / 2 + n ) } { \Gamma ( \nu + 1 / 2 - n ) } }
$$

Note that the $C _ { n }$ ’s can be determined by recursion:

$$
C _ { 0 } = 1 , \qquad C _ { n + 1 } = - \frac { a _ { n + 1 } } { n + 1 } C _ { n }
$$

We use the condition (6.6.28) by finding

$$
S = \sum _ { n = 1 } ^ { \infty } C _ { n } { \frac { z _ { n } } { z _ { 0 } } }
$$

Then

$$
z _ { 0 } = \left( \frac { 1 } { 2 x } \right) ^ { \nu + 1 / 2 } \frac { 1 } { 1 + S }
$$

and (6.6.23) gives $K _ { \nu }$

Thompson and Barnett [6] have given a clever method of doing the sum (6.6.31) simultaneously with the forward evaluation of the continued fraction CF2. Suppose the continued fraction is being evaluated as

$$
{ \frac { z _ { 1 } } { z _ { 0 } } } = \sum _ { n = 0 } ^ { \infty } \Delta h _ { n }
$$

where the increments $\Delta h _ { n }$ are being found by, e.g., Steed’s algorithm or the modified Lentz’s algorithm of $\ S 5 . 2$ . Then the approximation to $S$ keeping the first $N$ terms can be found as

$$
S _ { N } = \sum _ { n = 1 } ^ { N } Q _ { n } \Delta h _ { n }
$$

Here

$$
Q _ { n } = \sum _ { k = 1 } ^ { n } C _ { k } q _ { k }
$$

and $q _ { k }$ is found by recursion from

$$
q _ { k + 1 } = ( q _ { k - 1 } - b _ { k } q _ { k } ) / a _ { k + 1 }
$$

starting with $q _ { 0 } = 0$ , $q _ { 1 } = 1$ . For the case at hand, approximately three times as many terms are needed to get $S$ to converge as are needed simply for CF2 to converge.

To find $K _ { \nu }$ and $K _ { \nu + 1 }$ for small $x$ we use series analogous to (6.6.14):

$$
K _ { \nu } = \sum _ { k = 0 } ^ { \infty } c _ { k } f _ { k } \qquad K _ { \nu + 1 } = { \frac { 2 } { x } } \sum _ { k = 0 } ^ { \infty } c _ { k } h _ { k }
$$

Here

$$
\begin{array} { r l } & { c _ { k } = \frac { ( x ^ { 2 } / 4 ) ^ { k } } { k ! } } \\ & { h _ { k } = - k f _ { k } + p _ { k } } \\ & { p _ { k } = \frac { p _ { k - 1 } } { k - \nu } } \\ & { q _ { k } = \frac { q _ { k - 1 } } { k + \nu } } \\ & { f _ { k } = \frac { k f _ { k - 1 } + p _ { k - 1 } + q _ { k - 1 } } { k ^ { 2 } - \nu ^ { 2 } } } \end{array}
$$

The initial values for the recurrences are

$$
\begin{array} { l } { \displaystyle { p _ { 0 } = \frac { 1 } { 2 } \left( \frac { x } { 2 } \right) ^ { - \nu } \Gamma ( 1 + \nu ) } } \\ { \displaystyle { q _ { 0 } = \frac { 1 } { 2 } \left( \frac { x } { 2 } \right) ^ { \nu } \Gamma ( 1 - \nu ) } } \\ { \displaystyle { f _ { 0 } = \frac { \nu \pi } { \sin \nu \pi } \left[ \cosh \sigma \Gamma _ { 1 } ( \nu ) + \frac { \sinh \sigma } { \sigma } \ln \left( \frac { 2 } { x } \right) \Gamma _ { 2 } ( \nu ) \right] } } \end{array}
$$

Both the series for small $x$ , and CF2 and the normalization relation (6.6.28) require $| \nu | \leq 1 / 2$ . In both cases, therefore, we recurse $I _ { \nu }$ down to a value $\nu = \mu$ in this interval, find $K _ { \mu }$ there, and recurse $K _ { \nu }$ back up to the original value of $\nu$ .

The routine assumes $\nu \geq 0$ . For negative $\nu$ use the reflection formulas

$$
\begin{array} { l } { { I _ { - \nu } = I _ { \nu } + \displaystyle \frac { 2 } { \pi } \sin ( \nu \pi ) K _ { \nu } } } \\ { { K _ { - \nu } = K _ { \nu } } } \end{array}
$$

Note that for large $x$ , $I _ { \nu } \sim e ^ { x }$ and $K _ { \nu } \sim e ^ { - x }$ , and so these functions will overflow or underflow. It is often desirable to be able to compute the scaled quantities $e ^ { - x } I _ { \nu }$ and $e ^ { x } K _ { \nu }$ . Simply omitting the factor $e ^ { - x }$ in equation (6.6.23) will ensure that all four quantities will have the appropriate scaling. If you also want to scale the four quantities for small $x$ when the series in equation (6.6.37) are used, you must multiply each series by $e ^ { x }$ .

As with besseljy, you can either call the void function besselik, and then retrieve the function and/or derivative values from the object, or else just call inu or knu.

The code listing for Bessel::besselik is in a Webnote [4].

# 6.6.3 Airy Functions

For positive $x$ , the Airy functions are defined by

$$
\begin{array} { l } { { \displaystyle \mathrm { A i } ( x ) = \frac { 1 } { \pi } \sqrt { \frac { x } { 3 } } K _ { 1 / 3 } ( z ) } } \\ { { \displaystyle \mathrm { B i } ( x ) = \sqrt { \frac { x } { 3 } } [ I _ { 1 / 3 } ( z ) + I _ { - 1 / 3 } ( z ) ] } } \end{array}
$$

where

$$
z = { \frac { 2 } { 3 } } x ^ { 3 / 2 }
$$

By using the reflection formula (6.6.40), we can convert (6.6.42) into the computationally more useful form

$$
\mathrm { B i } ( x ) = \sqrt { x } \left[ \frac { 2 } { \sqrt { 3 } } I _ { 1 / 3 } ( z ) + \frac { 1 } { \pi } K _ { 1 / 3 } ( z ) \right]
$$

so that Ai and Bi can be evaluated with a single call to besselik.

![](images/eafa14a0d115d32a5ac68c8bf59f0d0ba5a88fdf3bec7649b365cf682a976c93.jpg)  
Figure 6.6.1. Airy functions $\operatorname { A i } ( x )$ and $\operatorname { B i } ( x )$ .

The derivatives should not be evaluated by simply differentiating the above expressions because of possible subtraction errors near $x = 0$ . Instead, use the equivalent expressions

$$
\begin{array} { l l l } { { \displaystyle \mathrm { A i } ^ { \prime } ( x ) = - \frac { x } { \pi \sqrt { 3 } } K _ { 2 / 3 } ( z ) } } \\ { { \displaystyle \mathrm { B i } ^ { \prime } ( x ) = x \left[ \frac { 2 } { \sqrt { 3 } } I _ { 2 / 3 } ( z ) + \frac { 1 } { \pi } K _ { 2 / 3 } ( z ) \right] } } \end{array}
$$

The corresponding formulas for negative arguments are

$$
\begin{array} { l l l } { { \mathrm { A i } ( - x ) = } } & { { \displaystyle \frac { \sqrt { x } } { 2 } \left[ { \cal J } _ { 1 / 3 } ( z ) - \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal Y } _ { 1 / 3 } ( z ) \right] } } \\ { { \mathrm { B i } ( - x ) = - \displaystyle \frac { \sqrt { x } } { 2 } \left[ \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal J } _ { 1 / 3 } ( z ) + { \cal Y } _ { 1 / 3 } ( z ) \right] } } \\ { { \mathrm { A i } ^ { \prime } ( - x ) = } } & { { \displaystyle \frac { x } { 2 } \left[ { \cal J } _ { 2 / 3 } ( z ) + \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal Y } _ { 2 / 3 } ( z ) \right] } } \\ { { \mathrm { B i } ^ { \prime } ( - x ) = } } & { { \displaystyle \frac { x } { 2 } \left[ \displaystyle \frac { 1 } { \sqrt { 3 } } { \cal J } _ { 2 / 3 } ( z ) - { \cal Y } _ { 2 / 3 } ( z ) \right] } } \end{array}
$$

# void Bessel::airy(const Doub x) {

Sets aio, bio, aipo, and bipo, respectively, to the Airy functions $\operatorname { A i } ( x )$ , $\operatorname { B i } ( x )$ and their derivatives $\operatorname { A i } ^ { \prime } ( x )$ , $\operatorname { B i } ^ { \prime } ( x )$ .

static const Doub $\mathtt { P I } = 3$ .141592653589793238, ONOVRT $ \scriptstyle = 0$ .577350269189626,THR $\ P = 1$ ./3.,TWOTHR=2.\*THR;   
Doub absx,rootx,z;   
absx $\equiv$ abs(x);   
rootx=sqrt(absx);   
$z { = }$ TWOTHR\*absx\*rootx;

if $( \textbf { x } > \ 0 . 0 )$ { besselik(THR,z); aio $=$ rootx\*ONOVRT\*ko/PI; bio $=$ rootx\*(ko/PI+2. $^ { 0 * }$ ONOVRT\*io); besselik(TWOTHR,z); aipo $=$ -x\*ONOVRT\*ko/PI; bipo $=$ x\*(ko/PI+2.0\*ONOVRT\*io); else if $( \textbf { x } < \ 0 . 0 )$ { besseljy(THR,z); aio $=$ 0.5\*rootx\*(jo-ONOVRT\*yo); bio $=$ -0.5\*rootx\*(yo+ONOVRT\*jo); besseljy(TWOTHR,z); aipo $=$ 0.5\*absx $^ *$ (ONOVRT\*yo+jo); bipo $=$ 0.5\*absx\*(ONOVRT\*jo-yo); } else { Case $x = 0$ . aio ${ = } 0$ .355028053887817; bio $=$ aio/ONOVRT; aipo $=$ -0.258819403792807; bipo $=$ -aipo/ONOVRT; } }

#

Doub Bessel::airy_ai(const Doub x) {   
Simple interface returning $\operatorname { A i } ( x )$ . if $( \textbf { x } : = \textbf { x } 0$ ) airy(x); return aio;   
}   
Doub Bessel::airy_bi(const Doub x) {   
Simple interface returning $\operatorname { B i } ( x )$ . if $( \mathrm {  ~ x ~ \unboldmath ~ } ! = \mathrm {  ~ x 0 ~ \unboldmath } )$ ) airy(x); return bio;   
}

# 6.6.4 Spherical Bessel Functions

For integer $n$ , spherical Bessel functions are defined by

$$
\begin{array} { l } { \displaystyle j _ { n } ( x ) = \sqrt { \frac { \pi } { 2 x } } J _ { n + \frac { 1 } { 2 } } ( x ) } \\ { \displaystyle y _ { n } ( x ) = \sqrt { \frac { \pi } { 2 x } } Y _ { n + \frac { 1 } { 2 } } ( x ) } \end{array}
$$

They can be evaluated by a call to besseljy, and the derivatives can safely be found from the derivatives of equation (6.6.47).

Note that in the continued fraction CF2 in (6.6.3) just the first term survives for $\nu = 1 / 2$ . Thus one can make a very simple algorithm for spherical Bessel functions along the lines of besseljy by always recursing $j _ { n }$ down to $n = 0$ , setting $p$ and $q$ from the first term in CF2, and then recursing $y _ { n }$ up. No special series is required near $x = 0$ . However, besseljy is already so efficient that we have not bothered to provide an independent routine for spherical Bessels.

void Bessel::sphbes(const Int n, const Doub x) Sets sphjo, sphyo, sphjpo, and sphypo, respectively, to the spherical Bessel functions $j _ { n } ( x )$ , $y _ { n } ( x )$ , and their derivatives ${ j _ { n } ^ { \prime } } ( x )$ , $y _ { n } ^ { \prime } ( x )$ for integer $_ n$ (which is saved as sphno).

const Doub RTPIO2 $^ { * 1 }$ .253314137315500251;   
Doub factor,order;   
if $( \ln \mathbf { \chi } < \mathbf { \chi } _ { 0 } | \mathbf { \chi } | \ : \mathrm { ~ x ~ } < = \mathbf { \chi } _ { 0 } . 0 )$ throw("bad arguments in sphbes");   
order $= \mathtt { n } + 0$ .5;   
besseljy(order,x);   
factor=RTPIO2/sqrt(x);   
sphj $\circ =$ factor\*jo;

sphyo=factor\*yo; sphjpo $=$ factor\*jpo-sphjo/(2.\*x); sphypo factor\*ypo-sphyo/(2.\*x); sphno $= \textbf { n }$ ; }

#

Doub Bessel::sphbesj(const Int n, const Doub x) {   
Simple interface returning $j _ { n } ( x )$ . if (n $\downarrow =$ sphno || x != xo) sphbes(n,x); return sphjo;   
}   
Doub Bessel::sphbesy(const Int n, const Doub x) {   
Simple interface returning $y _ { n } ( x )$ . if (n $\downarrow =$ sphno $| \textbf { | } \textbf { x } : = \textbf { x } 0 \ $ ) sphbes(n,x); return sphyo;   
}

# CITED REFERENCES AND FURTHER READING:

Barnett, A.R., Feng, D.H., Steed, J.W., and Goldfarb, L.J.B. 1974, “Coulomb Wave Functions for All Real $\eta$ and $\rho$ ,” Computer Physics Communications, vol. 8, pp. 377–395.[1]   
Temme, N.M. 1976, “On the Numerical Evaluation of the Ordinary Bessel Function of the Second Kind,” Journal of Computational Physics, vol. 21, pp. 343–350[2]; 1975, op. cit., vol. 19, pp. 324–337.[3]   
Numerical Recipes Software 2007, “Bessel Function Implementations,” Numerical Recipes Webnote No.8,at http://www.nr.com/webnotes?8 [4]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 10.[5]   
Thompson, I.J., and Barnett, A.R. 1987, “Modified Bessel Functions $I _ { \nu } ( z )$ and $K _ { \nu } ( z )$ of Real Order and Complex Argument, to Selected Accuracy,” Computer Physics Communications, vol. 47, pp. 245–257.[6]   
Barnett, A.R. 1981, “An Algorithm for Regular and Irregular Coulomb and Bessel functions of Real Order to Machine Accuracy,” Computer Physics Communications, vol. 21, pp. 297– 314.   
Thompson, I.J., and Barnett, A.R. 1986, “Coulomb and Bessel Functions of Complex Arguments and Order,” Journal of Computational Physics, vol. 64, pp. 490–509.

# 6.7 Spherical Harmonics

Spherical harmonics occur in a large variety of physical problems, for example, whenever a wave equation, or Laplace’s equation, is solved by separation of variables in spherical coordinates. The spherical harmonic $Y _ { l m } ( \theta , \phi ) , - l \le m \le l$ ; is a function of the two coordinates $\theta , \phi$ on the surface of a sphere.

The spherical harmonics are orthogonal for different $l$ and $m$ , and they are normalized so that their integrated square over the sphere is unity:

$$
\int _ { 0 } ^ { 2 \pi } d \phi \int _ { - 1 } ^ { 1 } d ( \cos \theta ) { \cal Y } _ { l ^ { \prime } m ^ { \prime } } ^ { \ast } ( \theta , \phi ) { \cal Y } _ { l m } ( \theta , \phi ) = \delta _ { l ^ { \prime } l } \delta _ { m ^ { \prime } m }
$$

Here the asterisk denotes complex conjugation.

Mathematically, the spherical harmonics are related to associated Legendre polynomials by the equation

$$
Y _ { l m } ( \theta , \phi ) = \sqrt { \frac { 2 l + 1 } { 4 \pi } \frac { ( l - m ) ! } { ( l + m ) ! } } P _ { l } ^ { m } ( \cos \theta ) e ^ { i m \phi }
$$

By using the relation

$$
Y _ { l , - m } ( \theta , \phi ) = ( - 1 ) ^ { m } Y _ { l m } ^ { \ast } ( \theta , \phi )
$$

we can always relate a spherical harmonic to an associated Legendre polynomial with $m \geq 0$ . With $x \equiv \cos \theta$ , these are defined in terms of the ordinary Legendre polynomials (cf. $\ S 4 . 6$ and $\ S 5 . 4 )$ b y

$$
P _ { l } ^ { m } ( x ) = ( - 1 ) ^ { m } ( 1 - x ^ { 2 } ) ^ { m / 2 } \frac { d ^ { m } } { d x ^ { m } } P _ { l } ( x )
$$

Be careful: There are alternative normalizations for the associated Legendre polynomials and alternative sign conventions.

The first few associated Legendre polynomials, and their corresponding normalized spherical harmonics, are

$$
\begin{array} { r l r l } & { \frac { P _ { 0 } ^ { 0 } ( x ) } { P _ { 0 } ^ { 1 } ( x ) } = } & { 1 } & { Y _ { 0 0 } = } & { \sqrt { \frac { 1 } { 4 \pi } } } \\ & { \frac { P _ { 1 } ^ { 1 } ( x ) } { P _ { 1 } ^ { 1 } ( x ) } = } & { - ( 1 - x ^ { 2 } ) ^ { 1 / 2 } } & { Y _ { 1 1 } = - \sqrt { \frac { 3 } { 8 \pi } } \sin \theta e ^ { i \phi } } \\ & { \frac { P _ { 0 } ^ { 0 } ( x ) } { P _ { 1 } ^ { 2 } ( x ) = } } & { x } & { Y _ { 1 0 } = } & { \sqrt { \frac { 3 } { 4 \pi } } \cos \theta } \\ & { \frac { P _ { 2 } ^ { 2 } ( x ) = } { 3 ( 1 - x ^ { 2 } ) } } & { Y _ { 2 2 } = \frac { 1 } { 4 } \sqrt { \frac { 1 5 } { 2 \pi } } \sin ^ { 2 } \theta e ^ { 2 i \phi } } \\ & { P _ { 2 } ^ { 1 } ( x ) = - 3 ( 1 - x ^ { 2 } ) ^ { 1 / 2 } x } & { Y _ { 2 1 } = - \sqrt { \frac { 1 5 } { 4 \pi } } \sin \theta \cos \theta e ^ { i \phi } } \\ & { P _ { 2 } ^ { 0 } ( x ) = \frac { 1 } { 2 } ( 3 x ^ { 2 } - 1 ) } & { Y _ { 2 0 } = } & { \sqrt { \frac { 5 } { 4 \pi } } ( \frac { 3 } { 2 } \cos ^ { 2 } \theta - \frac { 1 } { 2 } ) } \end{array}
$$

There are many bad ways to evaluate associated Legendre polynomials numerically. For example, there are explicit expressions, such as

$$
\begin{array} { c } { { P _ { l } ^ { m } ( x ) = \displaystyle { \frac { ( - 1 ) ^ { m } ( l + m ) ! } { 2 ^ { m } m ! ( l - m ) ! } } ( 1 - x ^ { 2 } ) ^ { m / 2 } \biggl [ 1 - \displaystyle { \frac { ( l - m ) ( m + l + 1 ) } { 1 ! ( m + 1 ) } } \left( \frac { 1 - x } { 2 } \right) } } \\ { { + \displaystyle { \frac { ( l - m ) ( l - m - 1 ) ( m + l + 1 ) ( m + l + 2 ) } { 2 ! ( m + 1 ) ( m + 2 ) } } \left( \frac { 1 - x } { 2 } \right) ^ { 2 } - \cdots \biggl ] } } \end{array}
$$

where the polynomial continues up through the term in $( 1 - x ) ^ { l - m }$ . (See [1] for this and related formulas.) This is not a satisfactory method because evaluation of the polynomial involves delicate cancellations between successive terms, which alternate in sign. For large $l$ , the individual terms in the polynomial become very much larger than their sum, and all accuracy is lost.

In practice, (6.7.6) can be used only in single precision (32-bit) for $l$ up to 6 or 8, and in double precision (64-bit) for $l$ up to 15 or 18, depending on the precision required for the answer. A more robust computational procedure is therefore desirable, as follows.

The associated Legendre functions satisfy numerous recurrence relations, tabulated in [1,2]. These are recurrences on $l$ alone, on $m$ alone, and on both $l$ and $m$ simultaneously. Most of the recurrences involving $m$ are unstable, and so are dangerous for numerical work. The following recurrence on $l$ is, however, stable (compare 5.4.1):

$$
( l - m ) P _ { l } ^ { m } = x ( 2 l - 1 ) P _ { l - 1 } ^ { m } - ( l + m - 1 ) P _ { l - 2 } ^ { m }
$$

Even this recurrence is useful only for moderate $l$ and $m$ , since the $P _ { l } ^ { m }$ ’s themselves grow rapidly with $l$ and quickly overflow. The spherical harmonics by contrast remain bounded — after all, they are normalized to unity (eq. 6.7.1). It is exactly the square-root factor in equation (6.7.2) that balances the divergence. So the right function to use in the recurrence relation is the renormalized associated Legendre function,

$$
\widetilde { P } _ { l } ^ { m } = \sqrt { \frac { 2 l + 1 } { 4 \pi } \frac { ( l - m ) ! } { ( l + m ) ! } } P _ { l } ^ { m }
$$

Then the recurrence relation (6.7.7) becomes

$$
\widetilde { P } _ { l } ^ { m } = \sqrt { \frac { 4 l ^ { 2 } - 1 } { l ^ { 2 } - m ^ { 2 } } } \left[ x \widetilde { P } _ { l - 1 } ^ { m } - \sqrt { \frac { ( l - 1 ) ^ { 2 } - m ^ { 2 } } { 4 ( l - 1 ) ^ { 2 } - 1 } } \widetilde { P } _ { l - 2 } ^ { m } \right]
$$

We start the recurrence with the closed-form expression for the $l = m$ function,

$$
\widetilde { P } _ { m } ^ { m } = ( - 1 ) ^ { m } \sqrt { \frac { 2 m + 1 } { 4 \pi ( 2 m ) ! } } ( 2 m - 1 ) ! ! ( 1 - x ^ { 2 } ) ^ { m / 2 }
$$

Using (6.7.9) with (The notation $n ! !$ denotes the product of all odd integers less than or equal to $l = m + 1$ , and setting ${ \widetilde { P } } _ { m - 1 } ^ { m } = 0$ , we find $n$ .)

$$
\tilde { P } _ { m + 1 } ^ { m } = x \sqrt { 2 m + 3 } \tilde { P } _ { m } ^ { m }
$$

Equations (6.7.10) and (6.7.11) provide the two starting values required for (6.7.9) for general $l$ .

The function that implements this is

Doub plegendre(const Int l, const Int m, const Doub x) {

Computes the renormalized associated Legendre polynomial $\tilde { P } _ { l } ^ { m } ( x )$ , equation (6.7.8). Here m and $l$ are integers satisfying $0 \leq m \leq l$ , while $x$ lies in the range $- 1 \leq x \leq 1$ .

static const Doub $\mathtt { P I } = 3$ .141592653589793;   
Int i,ll;   
Doub fact,oldfact,pll,pmm,pmmp1,omx2;   
if $( \mathrm { m } ~ < ~ 0 ~ | ~ | ~ \mathrm { ~ m ~ } > ~ 1 $ || abs $\mathrm { ~ ( ~ x ~ ) ~ } > \mathrm { ~ 1 ~ . ~ 0 ~ }$ ) throw("Bad arguments in routine plgndr");   
pmm=1.0; Compute $\widetilde { P } _ { m } ^ { m }$ .   
if $\mathrm { ~ \textit ~ { ~  ~ } ~ } \mathrm { ~ > ~ } \mathrm { ~ 0 ~ }$ ) { $\mathtt { o m x 2 } = ( 1 \mathrm { ~ . ~ } 0 \mathrm { - x } ) * ( 1 \mathrm { ~ . ~ } 0 \mathrm { + x } )$ ; fact $^ { = 1 }$ .0; for $\mathrm { { ( i = 1 ; i < = m ; i + + ) } }$ { pmm $\ast =$ omx2\*fact/(fact+1.0); fact $+ = ~ 2 . 0$ ; }   
}   
pmm=sqrt((2\*m+1)\*pmm/(4.0\*PI));

if (m & 1) pmm=-pmm; if $\mathrm { ~  ~ \Omega ~ } . \mathrm { ~  ~ \Omega ~ } . \mathrm { ~  ~ \Omega ~ } .$ ) return pmm; else { Compute $\tilde { P } _ { m + 1 } ^ { m }$ . pmmp1=x\*sqrt(2.0\*m+3.0)\*pmm; if $\scriptstyle { \mathrm { ~ ( ~ 1 ~ } = = \mathrm { ~ ( m + 1 ) ~ } }$ ) return pmmp1; else { Compute $\widetilde { P } _ { l } ^ { m }$ , $l > m + 1$ . oldfact=sqrt(2.0\*m+3.0); for (ll=m+2;ll<=l;ll++) { fact=sqrt((4.0\*ll\*ll-1.0)/(ll\*ll-m\*m)); pll=(x\*pmmp1-pmm/oldfact)\*fact; oldfact=fact; pmm=pmmp1; pmmp1=pll; } return pll; } } }

Sometimes it is convenient to have the functions with the standard normalization, as defined by equation (6.7.4). Here is a routine that does this. Note that it will overflow for $m \gtrsim 8 0$ , or even sooner if $l \gg m$ .

Doub plgndr(const Int l, const Int m, const Doub x)   
Computes the associated Legendre polynomial $P _ { l } ^ { m } ( x )$ , equation (6.7.4). Here $m$ and $l$ are integers satisfying $0 \leq m \leq l$ , while $x$ lies in the range $- 1 \leq x \leq 1$ . These functions will overflow for $m \gtrsim 8 0$ .   
const Doub $\mathtt { P I } = 3$ .141592653589793238;   
if $\mathrm { ~ ( ~ m ~ < ~ 0 ~ ~ | ~ | ~ ~ m ~ > ~ 1 ~ }$ || abs(x) > 1.0) throw("Bad arguments in routine plgndr");   
Doub prod=1.0;   
for (Int $\scriptstyle \mathbf { j } = 1 - \mathbf { m } + 1 ; \mathbf { j } < = 1 + \mathbf { m } ; \mathbf { j } + + )$ prod $\ast = \mathrm { ~ j ~ }$ ;   
return sqrt(4.0\*PI\*prod/( $^ { 2 * 1 + 1 }$ ))\*plegendre(l,m,x);

# 6.7.1 Fast Spherical Harmonic Transforms

Any smooth function on the surface of a sphere can be written as an expansion in spherical harmonics. Suppose the function can be well-approximated by truncating the expansion at $l = { l _ { \mathrm { { m a x } } } }$ :

$$
\begin{array} { c } { { f ( \theta _ { i } , \phi _ { j } ) = \displaystyle \sum _ { l = 0 } ^ { l _ { \mathrm { m a x } } } \sum _ { m = - l } ^ { m = l } a _ { l m } Y _ { l m } ( \theta _ { i } , \phi _ { j } ) } } \\ { { = \displaystyle \sum _ { l = 0 } ^ { l _ { \mathrm { m a x } } } \sum _ { m = - l } ^ { m = l } a _ { l m } \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } ) e ^ { i m \phi _ { j } } } } \end{array}
$$

Here we have written the function evaluated at one of $N _ { \theta }$ sample points $\theta _ { i }$ and one of $N _ { \phi }$ sample points $\phi _ { j }$ . The total number of sample points is $N = N _ { \theta } N _ { \phi }$ . In applications, typically $N _ { \theta } \sim N _ { \phi } \sim \sqrt { N }$ . Since the total number of spherical harmonics in the sum (6.7.12) is $l _ { \mathrm { m a x } } ^ { 2 }$ , we also have $l _ { \mathrm { m a x } } \sim \sqrt { N }$ .

How many operations does it take to evaluate the sum (6.7.12)? Direct evaluation of $l _ { \mathrm { m a x } } ^ { 2 }$ terms at $N$ sample points is an $O ( N ^ { 2 } )$ process. You might try to speed this up by choosing the sample points $\phi _ { j }$ to be equally spaced in angle and doing the sum over $m$ by an FFT. Each FFT is $O ( N _ { \phi } \ln { N _ { \phi } } )$ , and you have to do $O ( N _ { \theta } l _ { \mathrm { m a x } } )$ of them, for a total of $O ( N ^ { 3 / 2 } \ln N )$ operations, which is some improvement. A simple rearrangement [3-5] gives an even better way: Interchange the order of summation

$$
\sum _ { l = 0 } ^ { l _ { \mathrm { m a x } } } \sum _ { m = - l } ^ { l } \longleftrightarrow \sum _ { m = - l _ { \mathrm { m a x } } } ^ { l _ { \mathrm { m a x } } } \sum _ { l = | m | } ^ { l _ { \mathrm { m a x } } }
$$

so that

$$
f ( \theta _ { i } , \phi _ { j } ) = \sum _ { m = - l _ { \mathrm { m a x } } } ^ { l _ { \mathrm { m a x } } } q _ { m } ( \theta _ { i } ) e ^ { i m \phi _ { j } }
$$

where

$$
q _ { m } ( \theta _ { i } ) = \sum _ { l = | m | } ^ { l _ { \mathrm { m a x } } } a _ { l m } \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } )
$$

Evaluating the sum in (6.7.15) is $O ( l _ { \mathrm { m a x } } )$ , and one must do this for $O ( l _ { \operatorname* { m a x } } N _ { \theta } ) q _ { m }$ ’s, so the total work is ${ \cal O } ( N ^ { 3 / 2 } )$ . To evaluate equation (6.7.14) by an FFT at fixed $\theta _ { i }$ is $O ( N _ { \phi } \ln { N _ { \phi } } )$ . There are $N _ { \theta }$ FFTs to be done, for a total operations count of $O ( N \ln N )$ , which is negligible in comparison. So the total algorithm is $O ( N ^ { 3 / 2 } )$ . Note that you can evaluate equation (6.7.14) either by precomputing and storing the $\widetilde { P } _ { l } ^ { m }$ ’s using the recurrence relation (6.7.9), or by Clenshaw’s method (-5.4).

What about inverting the transform (6.7.12)? The formal inverse for the expansion of a continuous function $f ( \theta , \phi )$ follows from the orthonormality of the $Y _ { l m }$ ’s, equation (6.7.1),

$$
a _ { l m } = \int \sin \theta d \theta d \phi f ( \theta , \phi ) e ^ { - i m \phi } \widetilde { P } _ { l } ^ { m } ( \cos \theta )
$$

For the discrete case, where we have a sampled function, the integral becomes a quadrature:

$$
a _ { l m } = \sum _ { i , j } w ( \theta _ { i } ) f ( \theta _ { i } , \phi _ { j } ) e ^ { - i m \phi _ { j } } \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } )
$$

Here $w ( \theta _ { i } )$ are the quadrature weights. In principle we could consider weights that depend on $\phi _ { j }$ as well, but in practice we do the $\phi$ quadrature by an FFT, so the weights are unity. A good choice for the weights for an equi-angular grid in $\theta$ is given in Ref. [3], Theorem 3. Another possibility is to use Gaussian quadrature for the $\theta$ integral. In this case, you choose the sample points so that the cos $\theta _ { i }$ ’s are the abscissas returned by gauleg and the $w ( \theta _ { i } )$ ’s are the corresponding weights. The best way to organize the calculation is to first do the FFTs, computing

$$
g _ { m } ( \theta _ { i } ) = \sum _ { j } f ( \theta _ { i } , \phi _ { j } ) e ^ { - i m \phi _ { j } }
$$

Then

$$
a _ { l m } = \sum _ { i } w ( \theta _ { i } ) g _ { m } ( \theta _ { i } ) \widetilde { P } _ { l } ^ { m } ( \cos \theta _ { i } )
$$

You can verify that the operations count is dominated by equation (6.7.19) and scales as $O ( N ^ { 3 / 2 } )$ once again. In a real calculation, you should exploit all the symmetries that let you reduce the workload, such as $g _ { - m } = g _ { m } ^ { \ast }$ and $\tilde { P } _ { l } ^ { m } [ \cos ( \pi - \theta ) ] =$ $( - 1 ) ^ { l + m } \tilde { P } _ { l } ^ { m } ( \cos \theta )$ .

Very recently, algorithms for fast Legendre transforms have been developed, similar in spirit to the FFT [3,6,7]. Theoretically, they reduce the forward and inverse spherical harmonic transforms to $O ( N \log ^ { 2 } N )$ problems. However, current implementations [8] are not much faster than the $O ( N ^ { 3 / 2 } )$ methods above for $N \sim$ 500, and there are stability and accuracy problems that require careful attention [9]. Stay tuned!

# CITED REFERENCES AND FURTHER READING:

Magnus, W., and Oberhettinger, F. 1949, Formulas and Theorems for the Functions of Mathematical Physics (New York: Chelsea), pp. 54ff.[1]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 8.[2]   
Driscoll, J.R., and Healy, D.M. 1994, “Computing Fourier Transforms and Convolutions on the 2–sphere,” Advances in Applied Mathematics, vol. 15, pp. 202–250.[3]   
Muciaccia, P.F., Natoli, P., and Vittorio, N. 1997, “Fast Spherical Harmonic Analysis: A Quick Algorithm for Generating and/or Inverting Full-Sky, High-Resolution Cosmic Microwave Background Anisotropy Maps,” Astrophysical Journal, vol. 488, pp. L63–66.[4]   
Oh, S.P., Spergel, D.N., and Hinshaw, G. 1999, “An Efficient Technique to Determine the Power Spectrum from Cosmic Microwave Background Sky Maps,” Astrophysical Journal, vol. 510, pp. 551–563, Appendix A.[5]   
Healy, D.M., Rockmore, D., Kostelec, P.J., and Moore, S. 2003, “FFTs for the 2-Sphere: Improvements and Variations,” Journal of Fourier Analysis and Applications, vol. 9, pp. 341–385.[6]   
Potts, D., Steidl, G., and Tasche, M. 1998, “ Fast and Stable Algorithms for Discrete Spherical Fourier Transforms,” Linear Algebra and Its Applications, vol. 275-276, pp. 433–450.[7]   
Moore, S., Healy, D.M., Rockmore, D., and Kostelec, P.J. $^ { 2 0 0 7 + }$ , SpharmonicKit. Software at http://www.cs.dartmouth.edu/\~geelong/sphere.[8]   
Healy, D.M., Kostelec, P.J., and Rockmore, D. 2004, “Towards Safe and Effective High-Order Legendre Transforms with Applications to FFTs for the 2-Sphere,” Advances in Computational Mathematics,vol.21,pp.59-105.[9]

# 6.8 Fresnel Integrals, Cosine and Sine Integrals

# 6.8.1 Fresnel Integrals

The two Fresnel integrals are defined by

$$
C ( x ) = \int _ { 0 } ^ { x } \cos \left( { \frac { \pi } { 2 } } t ^ { 2 } \right) d t , \qquad S ( x ) = \int _ { 0 } ^ { x } \sin \left( { \frac { \pi } { 2 } } t ^ { 2 } \right) d t
$$

and are plotted in Figure 6.8.1.

![](images/61816714351e29f7ffbb7d3293bb66017c95a8bc0d49bdf4094c199e08bd454d.jpg)  
Figure 6.8.1. Fresnel integrals $C ( x )$ and $S ( x )$ $( \ S 6 . 8 )$ , and Dawson’s integral $F ( x )$ (-6.9).

The most convenient way of evaluating these functions to arbitrary precision is to use power series for small $x$ and a continued fraction for large $x$ . The series are

$$
\begin{array} { l } { { C ( x ) = x - \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 2 } \displaystyle \frac { x ^ { 5 } } { 5 \cdot 2 ! } + \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 4 } \displaystyle \frac { x ^ { 9 } } { 9 \cdot 4 ! } - \cdots } } \\ { { S ( x ) = \left( \displaystyle \frac { \pi } { 2 } \right) \displaystyle \frac { x ^ { 3 } } { 3 \cdot 1 ! } - \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 3 } \displaystyle \frac { x ^ { 7 } } { 7 \cdot 3 ! } + \left( \displaystyle \frac { \pi } { 2 } \right) ^ { 5 } \displaystyle \frac { x ^ { 1 1 } } { 1 1 \cdot 5 ! } - \cdots } } \end{array}
$$

There is a complex continued fraction that yields both $S ( x )$ and $C ( x )$ simultaneously:

$$
C ( x ) + i S ( x ) = \frac { 1 + i } { 2 } \mathrm { e r f } z , \qquad z = \frac { \sqrt { \pi } } { 2 } ( 1 - i ) x
$$

where

$$
{ \begin{array} { r l } & { e ^ { z ^ { 2 } } \operatorname { e r f c } z = { \cfrac { 1 } { \sqrt { \pi } } } \left( { \cfrac { 1 } { z + } } { \cfrac { 1 / 2 } { z + } } { \cfrac { 1 } { z + } } { \cfrac { 3 / 2 } { z + } } { \cfrac { 2 } { z + } } \cdots \right) } \\ & { \qquad = { \cfrac { 2 z } { \sqrt { \pi } } } \left( { \cfrac { 1 } { 2 z ^ { 2 } + 1 - } } { \cfrac { 1 \cdot 2 } { 2 z ^ { 2 } + 5 - } } { \cfrac { 3 \cdot 4 } { 2 z ^ { 2 } + 9 - } } \cdots \right) } \end{array} }
$$

In the last line we have converted the “standard” form of the continued fraction to its “even” form (see $\ S 5 . 2 )$ , which converges twice as fast. We must be careful not to evaluate the alternating series (6.8.2) at too large a value of $x$ ; inspection of the terms shows that $x = 1 . 5$ is a good point to switch over to the continued fraction.

Note that for large $x$

$$
C ( x ) \sim \frac { 1 } { 2 } + \frac { 1 } { \pi x } \sin \left( \frac { \pi } { 2 } x ^ { 2 } \right) , \qquad S ( x ) \sim \frac { 1 } { 2 } - \frac { 1 } { \pi x } \cos \left( \frac { \pi } { 2 } x ^ { 2 } \right)
$$

Thus the precision of the routine frenel may be limited by the precision of the library routines for sine and cosine for large $x$ .

Complex frenel(const Doub x) $\begin{array} { r } { \mathopen { } \mathclose \bgroup \left\{ \begin{array} { r l r l } \end{array} \aftergroup \egroup \right. } \end{array}$   
Computes the Fresnel integrals $S ( x )$ and $C ( x )$ for all real $x$ . $C ( x )$ is returned as the real part   
of cs and $S ( x )$ as the imaginary part. static const Int MAXIT $\scriptstyle \mathtt { \Gamma = 1 0 0 }$ ; static const Doub $\mathtt { P I } = 3$ .141592653589793238, PIBY2 $\Bumpeq$ (PI/2.0), XMIN=1.5, EPS=numeric_limits<Doub>::epsilon(), FPMIN=numeric_limits<Doub>::min(), BIG=numeric_limits<Doub>::max()\*EPS; Here MAXIT is the maximum number of iterations allowed; EPS is the relative error; FPMIN is a number near the smallest representable floating-point number; BIG is a number near the machine overflow limit; and XMIN is the dividing line between using the series and continued fraction. Bool odd; Int k,n; Doub a,ax,fact,pix2,sign,sum,sumc,sums,term,test; Complex b,cc,d,h,del,cs; if ((ax abs(x)) $<$ sqrt(FPMIN)) { Special case: Avoid failure of convergence cs=ax; test because of underflow. } else if (ax $< =$ XMIN) { Evaluate both series simultaneously. sum=sums=0.0; sumc $=$ ax; sign $= 1$ .0; fact=PIBY2\*ax\*ax; odd=true; term=ax; $\mathtt { n } = 3$ ; for $\mathrm { k } = 1$ ;k $< =$ MAXIT;k++) { term $\ast =$ fact/k; sum $+ =$ sign\*term/n; test ${ } = { }$ abs(sum)\*EPS; if (odd) { sign $=$ -sign; sums $=$ sum; sum=sumc; } else { sumc $=$ sum; sum=sums; if (term $<$ test) break; odd $= !$ odd; $\mathrm { ~ n ~ } + = \mathrm { ~ 2 ~ }$ ; } if (k $>$ MAXIT) throw("series failed in frenel"); cs=Complex(sumc,sums); } else { Evaluate continued fraction by modified pix2 $=$ PI\*ax\*ax; Lentz’s method (-5.2). b=Complex(1.0,-pix2); cc=BIG; $d = \mathrm { h } = 1$ .0/b; $\texttt { n } = \ - 1$ ; for (k=2;k $< =$ MAXIT;k++) { $\texttt { n } + = \ 2 ;$ ; $\mathrm { \ a \ = \ - n * ( n { + } 1 ) \ ; }$ ; b $\scriptstyle + = \ 4 , 0$ ; d=1.0/(a\*d+b); Denominators cannot be zero. cc=b+a/cc; del=cc\*d; h $\ast =$ del; if (abs(real(del)-1.0)+abs(imag(del)) $< =$ EPS) break; }

![](images/dc8f87c1ac8922226c8a9a8ecba7eaa3cd8c3638b2bc893bb9054a66abdf7530.jpg)  
Figure 6.8.2. Sine and cosine integrals $\mathrm { S i } ( x )$ and $\operatorname { C i } ( x )$ .

if (k > MAXIT) throw("cf failed in frenel"); h $\ast =$ Complex(ax,-ax); cs=Complex(0.5,0.5) \*(1.0-Complex(cos(0.5\*pix2),sin(0.5\*pix2))\*h); } if $\mathit { \Pi } _ { \mathrm { ~ x ~ } } < \mathit { \Pi } 0 . 0 \mathit { \Pi } _ { \mathrm { ~ \tiny ~  ~ } }$ ) cs = -cs; Use antisymmetry. return cs;

# 6.8.2 Cosine and Sine Integrals

The cosine and sine integrals are defined by

$$
\begin{array} { l } { \displaystyle \mathrm { C i } ( \boldsymbol { x } ) = \gamma + \ln \boldsymbol { x } + \int _ { 0 } ^ { \boldsymbol { x } } \frac { \cos t - 1 } { t } d t } \\ { \displaystyle \mathrm { S i } ( \boldsymbol { x } ) = \int _ { 0 } ^ { \boldsymbol { x } } \frac { \sin t } { t } d t } \end{array}
$$

and are plotted in Figure 6.8.2. Here $\gamma \approx 0 . 5 7 7 2 . . .$ is Euler’s constant. We only need a way to calculate the functions for $x > 0$ , because

$$
\mathrm { S i } ( - x ) = - \mathrm { S i } ( x ) , \qquad \mathrm { C i } ( - x ) = \mathrm { C i } ( x ) - i \pi
$$

Once again we can evaluate these functions by a judicious combination of power

series and complex continued fraction. The series are

$$
\begin{array} { l } { \displaystyle \mathrm { S i } ( x ) = x - \frac { x ^ { 3 } } { 3 \cdot 3 ! } + \frac { x ^ { 5 } } { 5 \cdot 5 ! } - \cdots } \\ { \displaystyle \mathrm { C i } ( x ) = \gamma + \ln x + \left( - \frac { x ^ { 2 } } { 2 \cdot 2 ! } + \frac { x ^ { 4 } } { 4 \cdot 4 ! } - \cdots \right) } \end{array}
$$

The continued fraction for the exponential integral $E _ { 1 } ( i x )$ is

$$
\begin{array} { l } { { \displaystyle E _ { 1 } ( i x ) = - \mathrm { C i } ( x ) + i [ \mathrm { S i } ( x ) - \pi / 2 ] } } \\ { ~ = e ^ { - i x } \left( \frac 1 { i x + } \frac 1 { 1 + } \frac 1 { i x + } \frac 2 { 1 + } \frac 2 { i x + } \dots \right) }  \\ { { \displaystyle ~ = e ^ { - i x } \left( \frac 1 { 1 + i x - } \frac 1 { 3 + i x - } \frac 2 { 5 + i x - } \dots \right) } } \end{array}
$$

The “even” form of the continued fraction is given in the last line and converges twice as fast for about the same amount of computation. A good crossover point from the alternating series to the continued fraction is $x = 2$ in this case. As for the Fresnel integrals, for large $x$ the precision may be limited by the precision of the sine and cosine routines.

# Complex cisi(const Doub x) {

Computes the cosine and sine integrals $\operatorname { C i } ( x )$ and $\mathrm { S i } ( x )$ . The function $\operatorname { C i } ( x )$ is returned as the real part of cs, and $\mathrm { S i } ( x )$ as the imaginary part. $\mathrm { C i } ( 0 )$ is returned as a large negative number and no error message is generated. For $x < 0$ the routine returns $\operatorname { C i } ( - x )$ and you must supply the $- i \pi$ yourself.

static const Int MAXIT $\mathtt { \Pi } = 1 0 0$ ; Maximum number of iterations allowed.   
static const Doub EULER ${ } = 0$ .577215664901533, PIBY2=1.570796326794897, TMIN $^ { = 2 }$ .0, EPS $=$ numeric_limits<Doub>::epsilon(), FPMIN=numeric_limits<Doub>::min() $^ { * 4 }$ .0, BIG $\scriptstyle  =$ numeric_limits<Doub>::max()\*EPS; Here EULER is Euler’s constant $\gamma$ ; PIBY2 is $\pi / 2$ ; TMIN is the dividing line between using the series and continued fraction; EPS is the relative error, or absolute error near a zero of $\operatorname { C i } ( x )$ ; FPMIN is a number close to the smallest representable floating-point number; and BIG is a number near the machine overflow limit.   
Int i,k;   
Bool odd;   
Doub a,err,fact,sign,sum,sumc,sums,t,term;   
Complex h,b,c,d,del,cs;   
if $: ( \mathrm { t } { = } { \bf a b s } \left( \mathrm { \bf x } \right) ) = = 0 . 0 \mathrm { \Omega }$ ) return -BIG; Special case.   
if ( $t >$ TMIN) { Evaluate continued fraction by modified b $\mid =$ Complex(1.0,t); Lentz’s method (-5.2). $z =$ Complex(BIG,0.0); $\mathrm { \ d } { = } \mathrm { h } { = } 1$ .0/b; for ( $\dot { \bf 1 } = 1$ ;i<MAXIT;i++) { a= -i\*i; b $+ = ~ 2 , 0$ ; d=1.0/(a\*d+b); Denominators cannot be zero. c=b+a/c; del=c\*d; h $\ast =$ del; if (abs(real(del)-1.0)+abs(imag(del)) $< =$ EPS) break; if (i $> =$ MAXIT) throw("cf failed in cisi"); $\mathrm { h } =$ Complex(cos(t),-sin(t))\*h; cs $=$ -conj(h)+Complex(0.0,PIBY2);   
} else { Evaluate both series simultaneously.

Special case: Avoid failure of convergence test because of underflow.

if (t < sqrt(FPMIN)) { sumc=0.0; sums=t; } else { sum=sums ${ } _ { , } = { }$ sumc ${ = } 0$ .0; sign=fact $= 1$ .0; odd=true; for $\mathrm { k } = 1$ ;k $< =$ MAXIT;k++) { fact $* = \mathrm { ~ t ~ } / \mathrm { k }$ ; term=fact/k; sum $+ =$ sign\*term; err=term/abs(sum); if (odd) { sign $=$ -sign; sums $=$ sum; sum=sumc; } else { sumc=sum; sum=sums; if (err $<$ EPS) break; odd=!odd; } if (k $>$ MAXIT) throw("maxits exceeded in cisi"); } cs=Complex(sumc+log(t)+EULER,sums); } if $\left( \mathbf { x } ~ < ~ 0 . 0 \right)$ cs $=$ conj(cs); return cs;

# CITED REFERENCES AND FURTHER READING:

Stegun, I.A., and Zucker, R. 1976, “Automatic Computing Methods for Special Functions. III. The Sine, Cosine, Exponential integrals, and Related Functions,” Journal of Research of the National Bureau of Standards,vol. 80B,pp.291-311； 1981,“Automatic Computing Methods for Special Functions. IV. Complex Error Function, Fresnel Integrals, and Other Related Functions,” op. cit., vol. 86, pp. 661–686.   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapters 5 and 7.

# 6.9 Dawson's Integral

Dawson’s Integral $F ( x )$ is defined by

$$
F ( x ) = e ^ { - x ^ { 2 } } \int _ { 0 } ^ { x } e ^ { t ^ { 2 } } d t
$$

See Figure 6.8.1 for a graph of the function. The function can also be related to the complex error function by

$$
F ( z ) = \frac { i \sqrt { \pi } } { 2 } e ^ { - z ^ { 2 } } \left[ 1 - \mathrm { e r f c } ( - i z ) \right] .
$$

A remarkable approximation for $F ( z )$ , due to Rybicki [1], is

$$
F ( z ) = \operatorname* { l i m } _ { h \to 0 } { \frac { 1 } { \sqrt { \pi } } } \sum _ { n { \mathrm { ~ o d d } } } { \frac { e ^ { - ( z - n h ) ^ { 2 } } } { n } }
$$

What makes equation (6.9.3) unusual is that its accuracy increases exponentially as $h$ gets small, so that quite moderate values of $h$ (and correspondingly quite rapid convergence of the series) give very accurate approximations.

We will discuss the theory that leads to equation (6.9.3) later, in $\ S 1 3 . 1 1$ , as an interesting application of Fourier methods. Here we simply implement a routine for real values of $x$ based on the formula.

It is first convenient to shift the summation index to center it approximately on the maximum of the exponential term. Define $n _ { 0 }$ to be the even integer nearest to $x / h$ , and $x _ { 0 } \equiv n _ { 0 } h$ , $x ^ { \prime } \equiv x - x _ { 0 }$ , and $n ^ { \prime } \equiv n - n _ { 0 }$ , so that

$$
F ( x ) \approx { \frac { 1 } { \sqrt { \pi } } } \sum _ { n ^ { \prime } = - N _ { \ \prime } ^ { n } \ \mathrm { o d d } } ^ { N } { \frac { e ^ { - ( x ^ { \prime } - n ^ { \prime } h ) ^ { 2 } } } { n ^ { \prime } + n _ { 0 } } }
$$

where the approximate equality is accurate when $h$ is sufficiently small and $N$ is sufficiently large. The computation of this formula can be greatly speeded up if we note that

$$
e ^ { - ( x ^ { \prime } - n ^ { \prime } h ) ^ { 2 } } = e ^ { - { x ^ { \prime } } ^ { 2 } } e ^ { - ( n ^ { \prime } h ) ^ { 2 } } \left( e ^ { 2 x ^ { \prime } h } \right) ^ { n ^ { \prime } }
$$

The first factor is computed once, the second is an array of constants to be stored, and the third can be computed recursively, so that only two exponentials need be evaluated. Advantage is also taken of the symmetry of the coefficients $e ^ { - ( n ^ { \prime } h ) ^ { 2 } }$ by breaking up the summation into positive and negative values of $n ^ { \prime }$ separately.

In the following routine, the choices $h = 0 . 4$ and $N = 1 1$ are made. Because of the symmetry of the summations and the restriction to odd values of $n$ , the limits on the for loops are 0 to 5. The accuracy of the result in this version is about $2 \times 1 0 ^ { - 7 }$ . In order to maintain relative accuracy near $x = 0$ , where $F ( x )$ vanishes, the program branches to the evaluation of the power series [2] for $F ( x )$ , for $| x | < 0 . 2$ .

Returns Dawson’s integral Doub dawson(const Doub $\begin{array} { c } { { \mathrm { \ x { x } } ) \mathrm { ~ \ x { ~ } } \mathrm { ~ \ x { ~ } } } } \\ { { F ( x ) = \exp ( - x ^ { 2 } ) \int _ { 0 } ^ { x } \exp ( t ^ { 2 } ) d t } } \end{array}$ for any real $x$ .

# dawson.h

static const Int NMAX $_ { = 6 }$ ;   
static VecDoub c(NMAX);   
static Bool init $=$ true;   
static const Doub $\mathtt { H } = 0 \mathtt { \Omega } . 4$ , ${ \tt A 1 } = 2$ .0/3.0, $\mathtt { A 2 = 0 }$ .4, $_ { \textrm { A 3 = 2 } }$ .0/7.0;   
Int i,n0; Flag is true if we need to initialize, else false.   
Doub d1,d2,e1,e2,sum,x2,xp,xx,ans;   
if (init) { init=false; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<NMAX;i++) c[i] $=$ exp(-SQR((2.0\*i+1.0)\*H));   
}   
if (abs(x) < 0.2) { Use series expansion. ${ \bf x } 2 \mathrm { = x * } { \bf x }$ ; ans=x\*(1.0-A1\*x2\*(1.0-A2\*x2\*(1.0-A3\*x2)));   
} else { Use sampling theorem representation. xx=abs(x); ${ \tt n } 0 = 2 *$ Int(0.5\*xx/H+0.5); xp=xx-n0\*H; e1=exp(2.0\*xp\*H);

e2=e1\*e1; d1=n0+1; d2=d1-2.0; sum=0.0; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<NMAX; $\dot { \bf 1 } + +$ ,d1 $+ { = } 2$ .0,d2- $- = 2$ .0,e1 $\mathtt { * } \mathtt { e } 2$ ) sum $+ =$ c[i]\*(e1/d1+1.0/(d2\*e1)); ans ${ = } 0$ .5641895835\*SIGN(exp(-xp\*xp),x)\*sum; Constant is $1 / { \sqrt { \pi } }$ return ans;

Other methods for computing Dawson’s integral are also known [2,3].

# CITED REFERENCES AND FURTHER READING:

Rybicki, G.B. 1989, “Dawson’s Integral and The Sampling Theorem,” Computers in Physics, vol. 3, no. 2, pp. 85–87.[1]   
Cody, W.J., Pociorek, K.A., and Thatcher, H.C. 1970, “Chebyshev Approximations for Dawson’s Integral,” Mathematics of Computation, vol. 24, pp. 171–178.[2]   
McCabe, J.H. 1974, “A Continued Fraction Expansion, with a Truncation Error Estimate, for Dawson’s Integral,” Mathematics of Computation, vol. 28, pp. 811–816.[3]

# 6.10 Generalized Fermi-Dirac Integrals

The generalized Fermi-Dirac integral is defined as

$$
F _ { k } ( \eta , \theta ) = \int _ { 0 } ^ { \infty } { \frac { x ^ { k } ( 1 + { \frac { 1 } { 2 } } \theta x ) ^ { 1 / 2 } } { e ^ { x - \eta } + 1 } } d x
$$

It occurs, for example, in astrophysical applications with $\theta$ nonnegative and arbitrary $\eta$ . In condensed matter physics one usually has the simpler case of $\theta = 0$ and omits the “generalized” from the name of the function. The important values of $k$ are $- 1 / 2 , 1 / 2 , 3 / 2$ , and $5 / 2$ , but we’ll consider arbitrary values greater than $^ { - 1 }$ . Watch out for an alternative definition that multiplies the integral by $1 / \Gamma ( k + 1 )$ .

For $\eta \ll - 1$ and $\eta \gg 1$ there are useful series expansions for these functions (see, e.g., [1]). These give, for example,

$$
\begin{array} { l } { { F _ { 1 / 2 } ( \eta , \theta ) \to \displaystyle \frac { 1 } { \sqrt { 2 \theta } } e ^ { \eta } e ^ { 1 / \theta } K _ { 1 } \left( \frac { 1 } { \theta } \right) , \quad \eta \to - \infty } } \\ { { \ } } \\ { { F _ { 1 / 2 } ( \eta , \theta ) \to \displaystyle \frac { 1 } { 2 \sqrt { 2 } } \eta ^ { 3 / 2 } \displaystyle \frac { y \sqrt { 1 + y ^ { 2 } } - \sinh ^ { - 1 } y } { ( \sqrt { 1 + y ^ { 2 } } - 1 ) ^ { 3 / 2 } } , \quad \eta \to \infty } } \end{array}
$$

Here $y$ is defined by

$$
1 + y ^ { 2 } = ( 1 + \eta \theta ) ^ { 2 }
$$

It is the middle range of $\eta$ values that is difficult to handle.

For $\theta = 0$ , Macleod [2] has given Chebyshev expansions accurate to $1 0 ^ { - 1 6 }$ for the four important $k$ values, covering all $\eta$ values. In this case, one need look no further for an algorithm. Goano [3] handles arbitrary $k$ for $\theta = 0$ . For nonzero $\theta$ , it is reasonable to compute the functions by direct integration, using variable transformation to get rapidly converging quadratures [4]. (Of course, this works also for $\theta = 0$ , but is not as efficient.) The usual transformation $x = \exp ( t - e ^ { - t } )$ handles the singularity at $x = 0$ and the exponential fall off at large $x$ (cf. equation 4.5.14). For $\eta \gtrsim 1 5$ , it is better to split the integral into two regions, $[ 0 , \eta ]$ and $[ \eta , \eta + 6 0 ]$ . (The contribution beyond $\eta + 6 0$ is negligible.) Each of these integrals can then be done with the DE rule. Between 60 and 500 function evaluations give full double precision, larger $\eta$ requiring more function evaluations. A more efficient strategy would replace the quadrature by a series expansion for large $\eta$ .

In the implementation below, note how operator() is overloaded to define both a function of one variable (for Trapzd) and a function of two variables (for DErule). Note also the syntax

Trapzd<Fermi> s(\*this,a,b);

for declaring a Trapzd object inside the Fermi object itself.

# struct Fermi {

Doub kk,etaa,thetaa; Doub operator() (const Doub t); Doub operator() (const Doub x, const Doub del); Doub val(const Doub k, const Doub eta, const Doub theta); };

Doub Fermi::operator() (const Doub t) {   
Integrand for trapezoidal quadrature of generalized Fermi-Dirac integral with transformation $x = \mathrm { { e x p } } ( t - e ^ { - t } )$ .   
Doub $_ \textrm { x }$ ;   
$_ { \textrm { x } = }$ exp(t-exp(-t));   
return x\*(1.0+exp(-t))\*pow(x,kk)\*sqrt(1.0+thetaa\*0.5\*x)/ (exp(x-etaa)+1.0);

# }

Doub Fermi::operator() (const Doub x, const Doub del) { Integrand for DE rule quadrature of generalized Fermi-Dirac integral.

if $\mathit { \Psi } _ { \left. \mathbf { X } \right. } ^ { \prime } < \left. \mathbf { 1 } . 0 \right.$ ) return pow(del,kk)\*sqrt(1. $^ { 0 + }$ thetaa\*0.5\*x)/(exp(x-etaa)+1.0);   
else return pow(x,kk)\*sqrt(1. $^ { 0 + }$ thetaa\*0.5\*x)/(exp(x-etaa)+1.0);

# }

# oub Fermi::val(const Doub k, const Doub eta, const Doub theta)

Computes the generalized Fermi-Dirac integral $F _ { k } ( \eta , \theta )$ , where $k > - 1$ and $\theta \ge 0$ . The accuracy is approximately the square of the parameter EPS. NMAX limits the total number of quadrature steps.

Load the arguments into the member variables for use in the function evaluations.

const Doub EPS $^ { \mathtt { = 3 } }$ .0e-9;   
const Int NMAX $= 1 1$ ;   
Doub a,aa,b,bb,hmax,olds,sum;   
$\mathbf { k } \mathbf { k } { = } \mathbf { k }$ ;   
etaa=eta;   
thetaa $\cdot ^ { = }$ theta;   
if (eta $< =$ 15.0) { a=-4.5; $\mathtt { b } = 5$ .0; Trapzd<Fermi> s(\*this,a,b); for (Int $\dot { 1 } = 1$ ; $\mathrm { i } < =$ NMAX; $\Dot { 1 } + +$ ) { sum=s.next(); if (i > 3) if (abs(sum-olds) $< =$

Set limits for $x = \exp ( t - e ^ { - t } )$ mapping.

return sum; olds $=$ sum; Save value for next convergence test. } } else { a=0.0; Set limits for DE rule. $\mathtt { b } =$ eta; aa=eta; bb ${ } ^ { 1 = }$ eta+60.0; hmax ${ = } 4$ .3; Big enough to handle negative $k$ or large $\eta$ . DErule<Fermi> s(\*this,a,b,hmax); DErule<Fermi> ss(\*this,aa,bb,hmax); for (Int $\dot { \mathbf { 1 } } = 1$ ; $\mathrm { i } < =$ NMAX; $\dot { \bar { \lambda } } + +$ ) { sum $= \tt s$ .next()+ss.next(); if ( $\textsuperscript { i } > 3 )$ if (abs(sum-olds) $< =$ EPS\*abs(olds)) return sum; olds=sum; } throw("no convergence in fermi"); return 0.0;

You get values of the Fermi-Dirac functions by declaring a Fermi object:

# Fermi ferm;

and then making repeated calls to the val function:

ans=ferm.val(k,eta,theta);

Other quadrature methods exist for these functions [5-7]. A reasonably efficient method [8] involves trapezoidal quadrature with “pole correction,” but it is restricted to $\theta \lesssim 0 . 2$ . Generalized Bose-Einstein integrals can also be computed by the DE rule or the methods in these references.

# CITED REFERENCES AND FURTHER READING:

Cox, J.P., and Giuli, R.T. 1968, Principles of Stellar Structure (New York: Gordon and Breach), vol. II, $\ S 2 4 . 7$ .[1]   
Macleod, A.J. 1998, “Fermi-Dirac Functions of Order $- 1 / 2 , 1 / 2 , 3 / 2 , 5 / 2 .$ ,” ACM Transactions on Mathematical Software,vol. 24, pp.1-12.(Algorithm 779,available from netlib.)[2]   
Goano, M. 1995, “Computation of the Complete and Incomplete Fermi-Dirac Integral,” ACM Transactions on Mathematical Software,vol.21,pp.221-232.(Algorithm 745,available from netlib.)[3]   
Natarajan, A., and Kumar, N.M. 1993, “On the Numerical Evaluation of the Generalised Fermi-Dirac Integrals,” Computer Physics Communications, vol. 76, pp. 48–50.[4]   
Pichon, B. 1989, “Numerical Calculation of the Generalized Fermi-Dirac Integrals,” Computer Physics Communications, vol.55, pp.127-136.[5]   
Sagar, R.P. 1991, “A Gaussian Quadrature for the Calculation of Generalized Fermi-Dirac Integrals,” Computer Physics Communications, vol. 66, pp. 271–275.[6]   
Gautschi, W. 1992, “On the Computation of Generalized Fermi-Dirac and Bose-Einstein Integrals,” Computer Physics Communications, vol. 74, pp. 233–238.[7]   
Mohankumar, N., and Natarajan, A. 1996, “A Note on the Evaluation of the Generalized Fermi-Dirac Integral,” Astrophysical Journal, vol. 458, pp. 233–235.[8]

![](images/aad0a5c881053367886c3db2fa92d1c4b107d1379353ccd001d3356b1ac0c490.jpg)  
Figure 6.11.1. The function $x \log ( x )$ is shown for $0 < x < 1$ . Although nearly invisible, an essential singularity at $x = 0$ makes this function tricky to invert.

# 6.11 Inverse of the Function x log(x)

The function

$$
y ( x ) = x \log ( x )
$$

and its inverse function $x ( y )$ occur in a number of statistical and information theoretical contexts. Obviously $y ( x )$ is nonsingular for all positive $x$ , and easy to evaluate. For $x$ between 0 and 1, it is negative, with a single minimum at $( x , y ) =$ $( e ^ { - 1 } , - e ^ { - 1 } )$ . The function has the value 0 at $x = 1$ , and it has the value 0 as its limit at $x = 0$ , since the linear factor $x$ easily dominates the singular logarithm.

Computing the inverse function $x ( y )$ is, however, not so easy. (We will need this inverse in $\ 8 6 . 1 4 . 1 2 .$ ) From the appearance of Figure 6.11.1, it might seem easy to invert the function on its left branch, that is, return a value $x$ between 0 and $e ^ { - 1 }$ for every value $y$ between 0 and $- e ^ { - 1 }$ . However, the lurking logarithmic singularity at $x = 0$ causes difficulties for many methods that you might try.

Polynomial fits work well over any range of $y$ that is less than a decade or so (e.g., from 0.01 to 0.1), but fail badly if you demand high fractional precision extending all the way to $y = 0$ .

What about Newton’s method? We write

$$
\begin{array} { c } { { f ( x ) \equiv x \log ( x ) - y } } \\ { { f ^ { \prime } ( x ) = 1 + \log ( x ) } } \end{array}
$$

giving the iteration

$$
x _ { i + 1 } = x _ { i } - { \frac { x _ { i } \log ( x _ { i } ) - y } { 1 + \log ( x _ { i } ) } }
$$

This doesn’t work. The problem is not with its rate of convergence, which is of course quadratic for any finite $y \ i f$ we start close enough to the solution (see $\ S 9 . 4 )$ . The problem is that the region in which it converges at all is very small, especially as $y  0$ . So, if we don’t already have a good approximation as we approach the singularity, we are sunk.

If we change variables, we can get different (not computationally equivalent) versions of Newton’s method. For example, let

$$
u \equiv \log ( x ) , \qquad x = e ^ { u }
$$

Newton’s method in $u$ looks like this:

$$
\begin{array} { l } { f ( u ) = u e ^ { u } - y } \\ { f ^ { \prime } ( u ) = ( 1 + u ) e ^ { u } } \\ { u _ { i + 1 } = u _ { i } - \displaystyle \frac { u _ { i } - e ^ { - u _ { i } } y } { 1 + u _ { i } } } \end{array}
$$

But it turns out that iteration (6.11.5) is no better than (6.11.3).

The observation that leads to a good solution is that, since its log term varies only slowly, $y = x \log ( x )$ is only very modestly curved when it is plotted in log-log coordinates. (Actually it is the negative of $y$ that is plotted, since log-log coordinates require positive quantities.) Algebraically, we rewrite equation (6.11.1) as

$$
( - y ) = ( - u ) e ^ { u }
$$

(with $u$ as defined above) and take logarithms, giving

$$
\log ( - y ) = u + \log ( - u )
$$

This leads to the Newton formulas,

$$
\begin{array} { l } { f ( u ) = u + \log ( - u ) - \log ( - y ) } \\ { f ^ { \prime } ( u ) = \frac { u + 1 } { u } } \\ { u _ { i + 1 } = u _ { i } + \frac { u _ { i } } { u _ { i } + 1 } \left[ \log \left( \frac { y } { u _ { i } } \right) - u _ { i } \right] } \end{array}
$$

It turns out that the iteration (6.11.8) converges quadratically over quite a broad region of initial guesses. For $- 0 . 2 < y < 0$ , you can just choose $^ { - 1 0 }$ (for example) as a fixed initial guess. When $- 0 . 2 \ < \ y \ < \ - e ^ { - 1 }$ , one can use the Taylor series expansion around $x = e ^ { - 1 }$ ,

$$
y ( x - e ^ { - 1 } ) = - e ^ { - 1 } + { \textstyle \frac { 1 } { 2 } } e ( x - e ^ { - 1 } ) ^ { 2 } + \cdots
$$

which yields

$$
x \approx e ^ { - 1 } - \sqrt { 2 e ^ { - 1 } ( y + e ^ { - 1 } ) }
$$

With these initial guesses, (6.11.8) never takes more than six iterations to converge to double precision accuracy, and there is just one log and a few arithmetic operations per iteration. The implementation looks like this:

# Doub invxlogx(Doub y) {

For negative $y$ , $0 > y > - e ^ { - 1 }$ , return $x$ such that $y = x \log ( x )$ . The value returned is always the smaller of the two roots and is in the range $0 < x < e ^ { - 1 }$

const Doub ooe $\qquad = \ 0$ .367879441171442322;   
Doub t,u,to ${ = } 0$ .;   
if $( \mathtt { y } ) = 0$ . || y $< =$ -ooe) throw("no such inverse value");   
if (y $< ~ - 0 . 2 )$ u $=$ log(ooe-sqrt( $^ { 2 * }$ ooe\*(y+ooe))); First approximation by inverse   
else $\mathrm { ~ u ~ } = \mathrm { ~ - 1 0 ~ }$ .; of Taylor series.   
do { See text for derivation. $\mathrm { ~ u ~ } + = \mathrm { ~ ( t = ( \log { ( y / u ) } - u ) * ( u / ( 1 . + u ) ) ~ ) ~ }$ ; if (t < 1.e-8 && abs(t+to) $< 0$ .01\*abs(t)) break; to = t;   
} while (abs(t/u) $>$ 1.e-15);   
return exp(u);

# 6.12 Elliptic Integrals and Jacobian Elliptic Functions

Elliptic integrals occur in many applications, because any integral of the form

$$
\int R ( t , s ) \ d t
$$

where $R$ is a rational function of $t$ and $s$ , and $s$ is the square root of a cubic or quartic polynomial in $t$ , can be evaluated in terms of elliptic integrals. Standard references [1] describe how to carry out the reduction, which was originally done by Legendre. Legendre showed that only three basic elliptic integrals are required. The simplest of these is

$$
I _ { 1 } = \int _ { y } ^ { x } \frac { d t } { \sqrt { ( a _ { 1 } + b _ { 1 } t ) ( a _ { 2 } + b _ { 2 } t ) ( a _ { 3 } + b _ { 3 } t ) ( a _ { 4 } + b _ { 4 } t ) } }
$$

where we have written the quartic $s ^ { 2 }$ in factored form. In standard integral tables [2], one of the limits of integration is always a zero of the quartic, while the other limit lies closer than the next zero, so that there is no singularity within the interval. To evaluate $I _ { 1 }$ , we simply break the interval $[ y , x ]$ into subintervals, each of which either begins or ends on a singularity. The tables, therefore, need only distinguish the eight cases in which each of the four zeros (ordered according to size) appears as the upper or lower limit of integration. In addition, when one of the $b$ ’s in (6.12.2) tends to zero, the quartic reduces to a cubic, with the largest or smallest singularity moving to $\pm \infty$ ; this leads to eight more cases (actually just special cases of the first eight). The 16 cases in total are then usually tabulated in terms of Legendre’s standard elliptic integral of the first kind, which we will define below. By a change of the variable of integration $t$ , the zeros of the quartic are mapped to standard locations on the real axis. Then only two dimensionless parameters are needed to tabulate Legendre’s integral. However, the symmetry of the original integral (6.12.2) under permutation of the roots is concealed in Legendre’s notation. We will get back to Legendre’s notation below. But first, here is a better approach:

Carlson [3] has given a new definition of a standard elliptic integral of the first kind,

$$
R _ { F } ( x , y , z ) = { \frac { 1 } { 2 } } \int _ { 0 } ^ { \infty } { \frac { d t } { \sqrt { ( t + x ) ( t + y ) ( t + z ) } } }
$$

where $x , y$ , and $z$ are nonnegative and at most one is zero. By standardizing the range of integration, he retains permutation symmetry for the zeros. (Weierstrass’ canonical form also has this property.) Carlson first shows that when $x$ or $y$ is a zero of the quartic in (6.12.2), the integral $I _ { 1 }$ can be written in terms of $R _ { F }$ in a form that is symmetric under permutation of the remaining three zeros. In the general case, when neither $x$ nor $y$ is a zero, two such $R _ { F }$ functions can be combined into a single one by an addition theorem, leading to the fundamental formula

$$
I _ { 1 } = 2 R _ { F } ( U _ { 1 2 } ^ { 2 } , U _ { 1 3 } ^ { 2 } , U _ { 1 4 } ^ { 2 } )
$$

where

$$
\begin{array} { l c r } { { U _ { i j } = ( X _ { i } X _ { j } Y _ { k } Y _ { m } + Y _ { i } Y _ { j } X _ { k } X _ { m } ) / ( x - y ) } } \\ { { \nonumber } } \\ { { X _ { i } = ( a _ { i } + b _ { i } x ) ^ { 1 / 2 } , \qquad Y _ { i } = ( a _ { i } + b _ { i } y ) ^ { 1 / 2 } } } \end{array}
$$

and $i , j , k , m$ is any permutation of 1; 2; 3; 4. A short-cut in evaluating these expressions is

$$
\begin{array} { c } { { U _ { 1 3 } ^ { 2 } = U _ { 1 2 } ^ { 2 } - ( a _ { 1 } b _ { 4 } - a _ { 4 } b _ { 1 } ) ( a _ { 2 } b _ { 3 } - a _ { 3 } b _ { 2 } ) } } \\ { { U _ { 1 4 } ^ { 2 } = U _ { 1 2 } ^ { 2 } - ( a _ { 1 } b _ { 3 } - a _ { 3 } b _ { 1 } ) ( a _ { 2 } b _ { 4 } - a _ { 4 } b _ { 2 } ) } } \end{array}
$$

The $U$ ’s correspond to the three ways of pairing the four zeros, and $I _ { 1 }$ is thus manifestly symmetric under permutation of the zeros. Equation (6.12.4) therefore reproduces all 16 cases when one limit is a zero, and also includes the cases when neither limit is a zero.

Thus Carlson’s function allows arbitrary ranges of integration and arbitrary positions of the branch points of the integrand relative to the interval of integration. To handle elliptic integrals of the second and third kinds, Carlson defines the standard integral of the third kind as

$$
R _ { J } ( x , y , z , p ) = { \frac { 3 } { 2 } } \int _ { 0 } ^ { \infty } { \frac { d t } { ( t + p ) { \sqrt { ( t + x ) ( t + y ) ( t + z ) } } } }
$$

which is symmetric in $x , y$ , and $z$ . The degenerate case when two arguments are equal is denoted

$$
R _ { D } ( x , y , z ) = R _ { J } ( x , y , z , z )
$$

and is symmetric in $x$ and $y$ . The function $R _ { D }$ replaces Legendre’s integral of the second kind. The degenerate form of $R _ { F }$ is denoted

$$
R _ { C } ( x , y ) = R _ { F } ( x , y , y )
$$

It embraces logarithmic, inverse circular, and inverse hyperbolic functions.

Carlson [4-7] gives integral tables in terms of the exponents of the linear factors of the quartic in (6.12.1). For example, the integral where the exponents are $( \frac { 1 } { 2 } , \frac { 1 } { 2 } , - \frac { 1 } { 2 } , - \frac { 3 } { 2 } )$ can be expressed as a single integral in terms of $R _ { D }$ ; it accounts for 144 separate cases in Gradshteyn and Ryzhik [2]!

Refer to Carlson’s papers [3-8] for some of the practical details in reducing elliptic integrals to his standard forms, such as handling complex-conjugate zeros.

Turn now to the numerical evaluation of elliptic integrals. The traditional methods [9] are Gauss or Landen transformations. Descending transformations decrease the modulus $k$ of the Legendre integrals toward zero, and increasing transformations increase it toward unity. In these limits the functions have simple analytic expressions. While these methods converge quadratically and are quite satisfactory for integrals of the first and second kinds, they generally lead to loss of significant figures in certain regimes for integrals of the third kind. Carlson’s algorithms [10,11], by contrast, provide a unified method for all three kinds with no significant cancellations.

The key ingredient in these algorithms is the duplication theorem:

$$
\begin{array} { c } { { R _ { F } ( x , y , z ) = 2 R _ { F } ( x + \lambda , y + \lambda , z + \lambda ) } } \\ { { { } } } \\ { { = R _ { F } \left( \displaystyle { \frac { x + \lambda } { 4 } } , \displaystyle { \frac { y + \lambda } { 4 } } , \displaystyle { \frac { z + \lambda } { 4 } } \right) } } \end{array}
$$

where

$$
\lambda = ( x y ) ^ { 1 / 2 } + ( x z ) ^ { 1 / 2 } + ( y z ) ^ { 1 / 2 }
$$

This theorem can be proved by a simple change of variable of integration [12]. Equation (6.12.11) is iterated until the arguments of $R _ { F }$ are nearly equal. For equal arguments we have

$$
R _ { F } ( x , x , x ) = x ^ { - 1 / 2 }
$$

When the arguments are close enough, the function is evaluated from a fixed Taylor expansion about (6.12.13) through fifth-order terms. While the iterative part of the algorithm is only linearly convergent, the error ultimately decreases by a factor of $\dot { 4 } ^ { 6 } = 4 0 9 6$ for each iteration. Typically only two or three iterations are required, perhaps six or seven if the initial values of the arguments have huge ratios. We list the algorithm for $R _ { F }$ here, and refer you to Carlson’s paper [10] for the other cases.

Stage 1: For $n = 0 , 1 , 2 , \ldots$ compute

$$
\begin{array} { r l } & { \mu _ { n } = ( x _ { n } + y _ { n } + z _ { n } ) / 3 } \\ & { X _ { n } = 1 - ( x _ { n } / \mu _ { n } ) , \quad Y _ { n } = 1 - ( y _ { n } / \mu _ { n } ) , \quad Z _ { n } = 1 - ( z _ { n } / \mu _ { n } ) } \\ & { \epsilon _ { n } = \operatorname* { m a x } ( | X _ { n } | , | Y _ { n } | , | Z _ { n } | ) } \end{array}
$$

If $\epsilon _ { n } \ <$ tol, go to Stage 2; else compute

$$
\begin{array} { r l } { \lambda _ { n } = ( x _ { n } y _ { n } ) ^ { 1 / 2 } + ( x _ { n } z _ { n } ) ^ { 1 / 2 } + ( y _ { n } z _ { n } ) ^ { 1 / 2 } ~ } & { { } } \\ { x _ { n + 1 } = ( x _ { n } + \lambda _ { n } ) / 4 , \quad y _ { n + 1 } = ( y _ { n } + \lambda _ { n } ) / 4 , \quad z _ { n + 1 } = ( z _ { n } + \lambda _ { n } ) / 4 } \end{array}
$$

and repeat this stage.

Stage 2: Compute

$$
\begin{array} { r l } & { E _ { 2 } = X _ { n } Y _ { n } - Z _ { n } ^ { 2 } , \quad E _ { 3 } = X _ { n } Y _ { n } Z _ { n } } \\ & { R _ { F } = ( 1 - \frac { 1 } { 1 0 } E _ { 2 } + \frac { 1 } { 1 4 } E _ { 3 } + \frac { 1 } { 2 4 } E _ { 2 } ^ { 2 } - \frac { 3 } { 4 4 } E _ { 2 } E _ { 3 } ) / ( \mu _ { n } ) ^ { 1 / 2 } } \end{array}
$$

In some applications the argument $p$ in $R _ { J }$ or the argument $y$ in $R _ { C }$ is negative, and the Cauchy principal value of the integral is required. This is easily handled by using the formulas

$$
\begin{array} { c } { { R _ { J } ( x , y , z , p ) = } } \\ { { \ } } \\ { { \left[ ( \gamma - y ) R _ { J } ( x , y , z , \gamma ) - 3 R _ { F } ( x , y , z ) + 3 R _ { C } ( x z / y , p \gamma / y ) \right] / ( y - p ) } } \end{array}
$$

where

$$
\gamma \equiv y + { \frac { ( z - y ) ( y - x ) } { y - p } }
$$

is positive if $p$ is negative, and

$$
R _ { C } ( x , y ) = \left( \frac { x } { x - y } \right) ^ { 1 / 2 } R _ { C } ( x - y , - y )
$$

The Cauchy principal value of $R _ { J }$ has a zero at some value of $p < 0$ , so (6.12.14) will give some loss of significant figures near the zero.

Doub rf(const Doub x, const Doub y, const Doub z) {   
Computes Carlson’s elliptic integral of the first kind, $R _ { F } ( x , y , z )$ . x, $y$ , and $z$ must be non  
negative, and at most one can be zero. static const Doub ERRTOL $\mathtt { \Omega } = 0$ .0025, THIRD $^ { 1 = 1 }$ .0/3.0, $\mathtt { C 1 } = 1$ .0/24.0, ${ \tt C } 2 { = } 0 . 1$ , $\mathtt { C 3 } = 3$ .0/44.0, $\mathtt { C 4 } = 1$ .0/14.0; static const Doub TINY $\mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt \mathtt  \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt $ . $^ { 0 * }$ numeric_limits<Doub>::min(), $\mathtt { B I G } { = } 0 . 2 *$ numeric_limits<Doub>::max(); Doub alamb,ave,delx,dely,delz,e2,e3,sqrtx,sqrty,sqrtz,xt,yt,zt; if (MIN(MIN(x,y),z) $< ~ 0 . 0$ || MIN(MIN(x+y,x+z), $y + z$ ) $<$ TINY || MAX(MAX(x,y),z) $>$ BIG) throw("invalid arguments in rf"); xt=x; $y t = y$ ; zt=z; do { sqrtx $\cdot ^ { = }$ sqrt(xt); sqrty $=$ sqrt(yt); sqrtz sqrt(zt); alamb sqrtx\*(sqrty+sqrtz)+sqrty\*sqrtz; xt=0.25\*(xt+alamb); yt=0.25\*(yt+alamb); zt=0.25\*(zt+alamb); ave=THIRD\*(xt+yt+zt); delx (ave-xt)/ave; dely $=$ (ave-yt)/ave; delz=(ave-zt)/ave; } while (MAX(MAX(abs(delx),abs(dely)),abs(delz)) $>$ ERRTOL); e2=delx\*dely-delz\*delz; e3=delx\*dely\*delz; return (1. $^ { 0 + }$ (C1\*e2-C2-C3\*e3)\*e2+C4\*e3)/sqrt(ave);

A value of 0.0025 for the error tolerance parameter gives full double precision (16 significant digits). Since the error scales as $\epsilon _ { n } ^ { 6 }$ , we see that 0.08 would be adequate for single precision (7 significant digits), but would save at most two or three more iterations. Since the coefficients of the sixth-order truncation error are different for the other elliptic functions, these values for the error tolerance should be set to 0.04 (single precision) or 0.0012 (double precision) in the algorithm for $R _ { C }$ , and 0.05 or 0.0015 for $R _ { J }$ and $R _ { D }$ . As well as being an algorithm in its own right for certain combinations of elementary functions, the algorithm for $R _ { C }$ is used repeatedly in the computation of $R _ { J }$ .

The $\mathrm { C } { + } { + }$ implementations test the input arguments against two machine-dependent constants, TINY and BIG, to ensure that there will be no underflow or overflow during the computation. You can always extend the range of admissible argument values by using the homogeneity relations (6.12.22), below.

Doub rd(const Doub x, const Doub y, const Doub z) {   
Computes Carlson’s elliptic integral of the second kind, $R _ { D } ( x , y , z )$ . $x$ and $y$ must be nonneg  
ative, and at most one can be zero. z must be positive. static const Doub ERRTOL $_ { * 0 }$ .0015, $\mathtt { C 1 } = 3$ .0/14.0, $\mathtt { C 2 } = 1$ .0/6.0, $\mathtt { C 3 } = 9$ .0/22.0, C4=3.0/26.0, $\mathtt { C 5 = 0 } \mathtt { \ . 2 5 * C 3 }$ , $\mathrm { C 6 } { = } 1 \ . 5 { * } \mathrm { C } 4$ ; static const Doub TINY $^ { - 2 }$ . $^ { 0 * }$ pow(numeric_limits<Doub>::max(),-2./3.), BIG $\scriptstyle = 0$ .1\*ERRTOL\*pow(numeric_limits<Doub>::min(),-2./3.); Doub alamb,ave,delx,dely,delz,ea,eb,ec,ed,ee,fac,sqrtx,sqrty, sqrtz,sum,xt,yt,zt; if (MIN(x,y) $<$ 0.0 || MIN(x+y,z) $<$ TINY || MAX(MAX(x,y),z) $>$ BIG) throw("invalid arguments in rd"); xt=x; yt=y; $z { \ t } { = } z$ ; sum $= 0$ .0; fac $= 1$ .0; do { sqrtx=sqrt(xt); sqrty sqrt(yt); sqrtz $=$ sqrt(zt); alamb $=$ sqrtx\*(sqrty+sqrtz)+sqrty\*sqrtz; sum $+ =$ fac/(sqrtz\*(zt+alamb)); fac ${ = } 0$ .25\*fac; xt=0.25\*(xt+alamb); yt=0.25\*(yt+alamb); zt ${ = } 0$ .25\*(zt+alamb); ave ${ = } 0$ . $^ { 2 * }$ (xt+yt+3.0\*zt); delx $: =$ (ave-xt)/ave; dely $=$ (ave-yt)/ave; delz $=$ (ave-zt)/ave;   
} while (MAX(MAX(abs(delx),abs(dely)),abs(delz)) $>$ ERRTOL);   
ea=delx\*dely;   
eb=delz\*delz;   
ec=ea-eb;   
ed=ea-6.0\*eb;   
ee=ed+ec+ec;   
return 3.0\*sum+fac\*(1.0+ed\*(-C1+C5\*ed-C6\*delz\*ee) +delz\*(C2\*ee+delz\*(-C3\*ec+delz\*C4\*ea)))/(ave\*sqrt(ave));

# elliptint.h

Doub rj(const Doub x, const Doub y, const Doub z, const Doub p) { Computes Carlson’s elliptic integral of the third kind, $R _ { J } ( x , y , z , p )$ . $x$ , $y$ , and $z$ must be nonnegative, and at most one can be zero. $p$ must be nonzero. If $p < 0$ , the Cauchy principal value is returned.

static const Doub ERRTOL $_ { , = 0 }$ .0015, $\mathrm { C } \mathrm { 1 } = \mathrm { 3 }$ .0/14.0, $\mathtt { C 2 } = 1$ .0/3.0, $\mathtt { C 3 } = 3$ .0/22.0, C4=3.0/26.0, $\mathtt { C 5 } { = } 0 . 7 5 { * } \mathtt { C } 3$ , $\mathtt { C 6 = 1 }$ . $5 * \mathrm { C 4 }$ , ${ \mathsf { C } } 7 { = } 0 \ldots { } 5 { * } { \mathsf { C } } 2$ , $_ { \mathsf { C } } 8 \mathrm { = } \mathsf { C } 3 \mathrm { + } \mathsf { C } 3$ ;   
static const Doub TINY $\mathrm { \Delta } =$ pow(5. $^ { 0 * }$ numeric_limits<Doub>::min(),1./3.), BIG $\scriptstyle = 0$ .3\*pow(0. $^ { 2 * }$ numeric_limits<Doub>::max(),1./3.);   
Doub a,alamb,alpha,ans,ave,b,beta,delp,delx,dely,delz,ea,eb,ec,ed,ee, fac,pt,rcx,rho,sqrtx,sqrty,sqrtz,sum,tau,xt,yt,zt;   
if (MIN(MIN(x,y),z) $< ~ 0 . 0$ || MIN(MIN $( \mathbf { x } + \mathbf { y } , \mathbf { x } + \mathbf { z } )$ ),MIN $( y + z$ ,abs(p))) $<$ TINY || MAX(MAX(x,y),MAX(z,abs(p))) $>$ BIG) throw("invalid arguments in rj");   
sum $= 0$ .0;   
fac $^ { = 1 }$ .0;   
if $( \mathtt { p } > 0 . 0 )$ { $\tt x t = \tt x$ ; $\tt y t = y$ ; $z { \ t } { = } z$ ; pt=p; else { xt=MIN(MIN(x,y),z); zt=MAX(MAX(x,y),z); yt=x+y+z-xt-zt; a=1.0/(yt-p); b=a\*(zt-yt)\*(yt-xt); pt=yt+b; rho=xt\*zt/yt; tau=p\*pt/yt; rcx=rc(rho,tau);   
}   
do { sqrtx sqrt(xt); sqrty=sqrt(yt); sqrtz $=$ sqrt(zt); alamb $\mid =$ sqrtx\*(sqrty+sqrtz)+sqrty\*sqrtz; alpha SQR(pt\*(sqrtx+sqrty+sqrtz)+sqrtx\*sqrty\*sqrtz); beta=pt\*SQR(pt+alamb); sum $+ =$ fac\*rc(alpha,beta); fac ${ = } 0$ .25\*fac; xt=0.25\*(xt+alamb); yt=0.25\*(yt+alamb);

zt=0.25\*(zt+alamb); pt=0.25\*(pt+alamb); ave ${ = } 0$ .2\*(xt+yt+zt+pt+pt); delx=(ave-xt)/ave; dely $=$ (ave-yt)/ave; delz $=$ (ave-zt)/ave; delp (ave-pt)/ave; } while (MAX(MAX(abs(delx),abs(dely)), MAX(abs(delz),abs(delp))) $>$ ERRTOL); ea=delx\*(dely+delz)+dely\*delz; eb=delx\*dely\*delz; ec=delp\*delp; ed=ea-3.0\*ec; ee=eb $^ { + 2 }$ .0\*delp\*(ea-ec); ans $^ { = 3 }$ . $^ { 0 * }$ sum+fac\*(1. $^ { 0 + }$ ed\*(-C1+C5\*ed-C6\*ee)+eb\*(C7+delp\*(-C8+delp\*C4)) +delp\*ea\*(C2-delp\*C3)-C2\*delp\*ec)/(ave\*sqrt(ave)); if $_ { \mathrm { ~ \tiny ~ P ~ } } < = \mathrm { ~ \tiny ~ 0 ~ . ~ 0 ~ }$ ) ans=a\*(b\*ans+3.0\*(rcx-rf(xt,yt,zt))); return ans;

Doub rc(const Doub x, const Doub y) {   
Computes Carlson’s degenerate elliptic integral, $R _ { C } ( x , y )$ . x must be nonnegative and $y$ must be nonzero. If $y < 0$ , the Cauchy principal value is returned.   
static const Doub ERRTOL ${ = } 0$ .0012, THIRD $^ { 1 = 1 }$ .0/3.0, $\mathrm { C 1 } { = } 0 . 3$ , $\mathtt { C 2 } = 1$ .0/7.0, $\mathtt { C 3 } = 0$ .375, $\mathtt { C 4 } = 9$ .0/22.0;   
static const Doub TINY $\mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt  \mathtt \mathtt  \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt  \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt \mathtt $ . $^ { 0 * }$ numeric_limits<Doub>::min(), $\mathtt { B I G } = 0$ . $^ { 2 \ast }$ numeric_limits<Doub>::max(), COMP1=2.236/sqrt(TINY), COMP2 $\mathbf { \equiv }$ SQR(TINY\*BIG)/25.0;   
Doub alamb,ave,s,w,xt,yt;   
if $\mathit { \check { x } } ~ < ~ 0 . 0$ || $\ y \ = = \ 0 . 0$ || $\mathbf { x } +$ abs(y)) $<$ TINY || ( $^ { \mathbb { X } + }$ abs(y)) $>$ BIG || (y<-COMP1 && $\textbf { z } > \ 0 . 0$ && $\mathrm { ~ x ~ } <$ COMP2)) throw("invalid arguments in rc");   
if $( \mathrm { y } > 0 . 0 )$ { $\tt x t = x$ ; yt=y; $\scriptstyle { \mathtt { w } } = 1$ .0;   
} else { xt=x-y; yt= -y; w=sqrt(x)/sqrt(xt);   
}   
do { alamb $^ { - 2 }$ .0\*sqrt(xt)\*sqrt(yt)+yt; xt ${ = } 0$ .25\*(xt+alamb); yt ${ = } 0$ .25\*(yt+alamb); ave $=$ THIRD\*(xt+yt+yt); $\mathbf { s } =$ (yt-ave)/ave;   
} while (abs(s) $>$ ERRTOL);   
return w\*(1.0+s\*s\*(C1+s\*(C2+s\*(C3+s\*C4))))/sqrt(ave);

At times you may want to express your answer in Legendre’s notation. Alternatively, you may be given results in that notation and need to compute their values with the programs given above. It is a simple matter to transform back and forth. The Legendre elliptic integral of the first kind is defined as

$$
F ( \phi , k ) \equiv \int _ { 0 } ^ { \phi } { \frac { d \theta } { \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \theta } } }
$$

The complete elliptic integral of the first kind is given by

$$
K ( k ) \equiv F ( \pi / 2 , k )
$$

In terms of $R _ { F }$

$$
\begin{array} { c } { { F ( \phi , k ) = \sin \phi R _ { F } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } } \\ { { K ( k ) = R _ { F } ( 0 , 1 - k ^ { 2 } , 1 ) } } \end{array}
$$

The Legendre elliptic integral of the second kind and the complete elliptic integral of the second kind are given by

$$
\begin{array} { l } { \displaystyle { E ( \phi , k ) \equiv \int _ { 0 } ^ { \phi } \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \theta } ~ d \theta } } \\ { \displaystyle { \quad = \sin \phi R _ { F } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } } \\ { \displaystyle { \qquad - \frac { 1 } { 3 } k ^ { 2 } \sin ^ { 3 } \phi R _ { D } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } } \\ { \displaystyle { E ( k ) \equiv E ( \pi / 2 , k ) = R _ { F } ( 0 , 1 - k ^ { 2 } , 1 ) - \frac { 1 } { 3 } k ^ { 2 } R _ { D } ( 0 , 1 - k ^ { 2 } , 1 ) } } \end{array}
$$

Finally, the Legendre elliptic integral of the third kind is

$$
\begin{array} { l } { \displaystyle \Pi ( \phi , n , k ) \equiv \int _ { 0 } ^ { \phi } \frac { d \theta } { \displaystyle ( 1 + n \sin ^ { 2 } \theta ) \sqrt { 1 - k ^ { 2 } \sin ^ { 2 } \theta } } } \\ { \displaystyle = \sin \phi R _ { F } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 ) } \\ { \displaystyle \qquad - \frac { 1 } { 3 } n \sin ^ { 3 } \phi R _ { J } ( \cos ^ { 2 } \phi , 1 - k ^ { 2 } \sin ^ { 2 } \phi , 1 , 1 + n \sin ^ { 2 } \phi ) } \end{array}
$$

(Note that this sign convention for $n$ is opposite that of Abramowitz and Stegun [13], and that their $\sin \alpha$ is our $k$ .)

Doub ellf(const Doub phi, const Doub ak) $\begin{array} { r } { \mathopen { } \mathclose \bgroup \left\{ \begin{array} { r l r l } \end{array} \aftergroup \egroup \right. } \end{array}$   
Legendre elliptic integral of the first kind $F ( \phi , k )$ , evaluated using Carlson’s function $R _ { F }$ . The argument ranges are $0 \leq \phi \leq \pi / 2$ , $0 \leq k \sin \phi \leq 1$ .

Doub s=sin(phi); return s\*rf(SQR(cos(phi)), $( 1 . 0 \mathrm { - } \mathrm { s } \ast \mathrm { a k } ) \ast ( 1 . 0 \mathrm { + } \mathrm { s } \ast \mathrm { a k } ) , 1 . 0 ) ;$ }

# elliptint.h

# Doub elle(const Doub phi, const Doub ak) $\left\{ \begin{array} { r l } \end{array} \right.$

Legendre elliptic integral of the second kind $E ( \phi , k )$ , evaluated using Carlson’s functions $R _ { D }$ and $R _ { F }$ . The argument ranges are $0 \leq \phi \leq \pi / 2$ , $0 \leq k \sin \phi \leq 1$ .

Doub cc,q,s;   
$\mathbf { s } =$ sin(phi);   
cc=SQR(cos(phi));   
$\mathsf { q } = \left( 1 \mathsf { \ldots } 0 \mathsf { - s } \mathsf { * a k } \right) \mathsf { \ldots } \left( 1 \mathsf { \ldots } 0 \mathsf { + s } \mathsf { * a k } \right) \mathsf { \ldots }$ ;   
return s\*(rf(cc,q,1.0)-(SQR(s\*ak))\*rd(cc,q,1.0)/3.0);

# elliptint.h

Doub ellpi(const Doub phi, const Doub en, const Doub ak) {

Legendre elliptic integral of the third kind $\scriptstyle \Pi ( \phi , n , k )$ , evaluated using Carlson’s functions $R J$ and $R _ { F }$ . (Note that the sign convention on $_ { n }$ is opposite that of Abramowitz and Stegun.) The ranges of $\phi$ and $k$ are $0 \leq \phi \leq \pi / 2$ , $0 \leq k \sin \phi \leq 1$ .

Doub cc,enss,q,s;   
$\mathbf { s } =$ sin(phi);   
enss=en\*s\*s;   
cc=SQR(cos(phi));   
$\mathsf { q } = \left( 1 \mathsf { \ldots } 0 \mathsf { - s } \mathsf { * a k } \right) \mathsf { \ldots } \left( 1 \mathsf { \ldots } 0 \mathsf { + s } \mathsf { * a k } \right) \vdots$ ;   
return s\*(rf(cc,q,1.0)-enss\*rj(cc,q,1.0,1.0+enss)/3.0);

# elliptint.h

Carlson’s functions are homogeneous of degree $- \frac 1 2$ and $- \frac { 3 } { 2 }$ , so

$$
\begin{array} { c } { { R _ { F } ( \lambda x , \lambda y , \lambda z ) = \lambda ^ { - 1 / 2 } R _ { F } ( x , y , z ) } } \\ { { { } } } \\ { { R _ { J } ( \lambda x , \lambda y , \lambda z , \lambda p ) = \lambda ^ { - 3 / 2 } R _ { J } ( x , y , z , p ) } } \end{array}
$$

Thus, to express a Carlson function in Legendre’s notation, permute the first three arguments into ascending order, use homogeneity to scale the third argument to be 1, and then use equations (6.12.19) – (6.12.21).

# 6.12.1 Jacobian Elliptic Functions

The Jacobian elliptic function sn is defined as follows: Instead of considering the elliptic integral

$$
u ( y , k ) \equiv u = F ( \phi , k )
$$

consider the inverse function

$$
y = \sin \phi = \sin ( u , k )
$$

Equivalently,

$$
u = \int _ { 0 } ^ { \mathrm { s n } } \frac { d y } { \sqrt { ( 1 - y ^ { 2 } ) ( 1 - k ^ { 2 } y ^ { 2 } ) } }
$$

When $k = 0$ , sn is just sin. The functions cn and dn are defined by the relations

$$
\begin{array} { r } { \mathrm { s n } ^ { 2 } + \mathrm { c n } ^ { 2 } = 1 , \qquad k ^ { 2 } \mathrm { s n } ^ { 2 } + \mathrm { d n } ^ { 2 } = 1 } \end{array}
$$

The routine given below actually takes $m _ { c } \equiv k _ { c } ^ { 2 } = 1 - k ^ { 2 }$ as an input parameter. It also computes all three functions sn, cn, and dn since computing all three is no harder than computing any one of them. For a description of the method, see [9].

void sncndn(const Doub uu, const Doub emmc, Doub &sn, Doub &cn, Doub &dn) { Returns the Jacobian elliptic functions $\mathsf { s n } ( u , k _ { c } )$ , ${ \mathsf { c n } } ( u , k _ { c } )$ , and $\mathsf { d n } ( u , k _ { c } )$ . Here $\mathtt { u u } = u$ , while emmc $= k _ { c } ^ { 2 }$ .

The accuracy is the square of CA.

static const Doub $\mathtt { C A = 1 }$ .0e-8;   
Bool bo;   
Int i,ii,l;   
Doub a,b,c,d,emc,u;   
VecDoub em(13),en(13);   
emc=emmc;   
u=uu;   
if (emc != 0.0) { bo $=$ (emc < 0.0); if (bo) { $\mathrm { d } { = } 1$ .0-emc; emc /= -1.0/d; u \*= ( $\mathtt { d } =$ sqrt(d)); } $\mathtt { a } = 1$ .0; d $\mathtt { n } { = } 1$ .0; for (i=0;i<13;i++) { $\beth = \dot { \beth }$ ; em[i] $= a$ ; en[i] $=$ (emc=sqrt(emc)); c=0.5\*(a+emc); if (abs(a-emc) $< =$ CA\*a) break; emc $\ast = \mathtt { a }$ ;

a=c; } u \*= c; sn=sin(u); cn=cos(u); if (sn $\ ! =$ 0.0) a=cn/sn; c \*= a; for (ii=l;ii>=0;ii--) b=em[ii]; a \*= c; c \*= dn; dn=(en[ii]+a)/(b+a); a=c/b; a=1.0/sqrt(c\*c+1.0); sn=(sn >= 0.0 ? a : -a); cn=c\*sn; } if (bo) { a=dn; dn=cn; $\mathtt { c n } { = } \mathtt { a }$ ; sn /= d; } } else { cn=1.0/cosh(u); dn=cn; sn=tanh(u); }

# CITED REFERENCES AND FURTHER READING:

Erdélyi, A., Magnus, W., Oberhettinger, F., and Tricomi, F.G. 1953, Higher Transcendental Functions,Vol. I,(New York: McGraw-Hill).[1]   
Gradshteyn, I.S., and Ryzhik, I.W. 1980, Table of Integrals, Series, and Products (New York: Academic Press).[2]   
Carlson, B.C. 1977, “Elliptic Integrals of the First Kind,” SIAM Journal on Mathematical Analysis, vol. 8, pp. 231–242.[3]   
Carlson, B.C. 1987, “A Table of Elliptic Integrals of the Second Kind,” Mathematics of Computation,vol.49,pp.595-606[4]; 1988,“A Table of Eliptic Integrals of the Third Kind”op.cit., vol. 51, pp. 267–280[5]; 1989, “A Table of Elliptic Integrals: Cubic Cases,” op. cit., vol. 53, pp. 327–333[6]; 1991, “A Table of Elliptic Integrals: One Quadratic Factor,” op. cit., vol. 56, pp. 267–280.[7]   
Carlson, B.C., and FitzSimons, J. 2000, “Reduction Theorems for Elliptic Integrands with the Square Root of Two Quadratic Factors,” Journal of Computational and Applied Mathematics, vol. 118,pp.71-85.[8]   
Bulirsch, R. 1965, “Numerical Calculation of Elliptic Integrals and Elliptic Functions,” Numerische Mathematik,vol.7,pp.78-90;1965,op. cit.,vol.7,pp. 353-354; 1969,op. cit.,vol.13, pp. 305–315.[9]   
Carlson, B.C. 1979, “Computing Elliptic Integrals by Duplication,” Numerische Mathematik, vol. 33, pp. 1–16.[10]   
Carlson, B.C., and Notis, E.M. 1981, “Algorithms for Incomplete Elliptic Integrals,” ACM Transactions on Mathematical Software, vol.7,pp.398-403.[11]   
Carlson, B.C. 1978, “Short Proofs of Three Theorems on Elliptic Integrals,” SIAM Journal on Mathematical Analysis, vol. 9,p. 524-528.[12]   
Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands, Chapter 17.[13]   
Mathews, J., and Walker, R.L. 1970, Mathematical Methods of Physics, 2nd ed. (Reading, MA: W.A. Benjamin/Addison-Wesley), pp. 78–79.

# 6.13 Hypergeometric Functions

As was discussed in $\ S 5 . 1 4$ , a fast, general routine for the the complex hypergeometric function $_ 2 F _ { 1 } ( a , b , c ; z )$ is difficult or impossible. The function is defined as the analytic continuation of the hypergeometric series

$$
{ \begin{array} { r l } & { _ { 2 } F _ { 1 } ( a , b , c ; z ) = 1 + { \frac { a b } { c } } { \frac { z } { 1 ! } } + { \frac { a ( a + 1 ) b ( b + 1 ) } { c ( c + 1 ) } } { \frac { z ^ { 2 } } { 2 ! } } + \cdots } \\ & { \qquad + { \frac { a ( a + 1 ) \ldots ( a + j - 1 ) b ( b + 1 ) \ldots ( b + j - 1 ) } { c ( c + 1 ) \ldots ( c + j - 1 ) } } { \frac { z ^ { j } } { j ! } } + \cdots } \end{array} }
$$

This series converges only within the unit circle $| z | < 1$ (see [1]), but one’s interest in the function is not confined to this region.

Section 5.14 discussed the method of evaluating this function by direct path integration in the complex plane. We here merely list the routines that result.

Implementation of the function hypgeo is straightforward and is described by comments in the program. The machinery associated with Chapter 17’s routine for integrating differential equations, Odeint, is only minimally intrusive and need not even be completely understood: Use of Odeint requires one function call to the constructor, with a prescribed format for the derivative routine Hypderiv, followed by a call to the integrate method.

The function hypgeo will fail, of course, for values of $Z$ too close to the singularity at 1. (If you need to approach this singularity, or the one at $\infty$ , use the “linear transformation formulas” in $\ S 1 5 . 3$ of [1].) Away from $z = 1$ , and for moderate values of $a , b , c$ , it is often remarkable how few steps are required to integrate the equations. A half-dozen is typical.

Complex hypgeo(const Complex &a, const Complex &b,const Complex &c, const Complex &z)

Complex hypergeometric function ${ } _ { 2 } F _ { 1 }$ for complex $a , b , c$ , and $z$ , by direct integration of the hypergeometric equation in the complex plane. The branch cut is taken to lie along the real axis, Re $z > 1$ .

const Doub atol $^ { = 1 }$ .0e-14,rtol $^ { = 1 }$ .0e-14; Accuracy parameters.   
Complex ans,dz,z0,y[2];   
VecDoub yy(4);   
if (norm(z) $< =$ 0.25) { Use series... hypser(a,b,c,z,ans,y[1]); return ans;   
}   
...or pick a starting point for the path integration.   
else if (real(z) $<$ 0.0) z0=Complex(-0.5,0.0);   
else if (real(z) $< = ~ 1 . 0$ ) z0=Complex(0.5,0.0); else z0=Complex(0.0,imag(z) >= 0.0 ? 0.5 : -0.5);   
dz=z-z0;   
hypser(a,b,c,z0,y[0],y[1]); Get starting function and derivative.   
yy[0] $=$ real(y[0]);   
yy[1] $=$ imag(y[0]);   
yy[2] $=$ real(y[1]);   
yy[3] $=$ imag(y[1]);   
Hypderiv d(a,b,c,z0,dz); Set up the functor for the derivatives.   
Output out; Suppress output in Odeint.   
Odeint<StepperBS<Hypderiv> $>$ ode(yy,0.0,1.0,atol,rtol,0.1,0.0,out,d);   
The arguments to Odeint are the vector of independent variables, the starting and ending values of the dependent variable, the accuracy parameters, an initial guess for the stepsize, a minimum stepsize, and the names of the output object and the derivative object. The integration is performed by the Bulirsch-Stoer stepping routine.   
ode.integrate();   
y[0] $=$ Complex(yy[0],yy[1]);   
return y[0];   
void hypser(const Complex &a, const Complex &b, const Complex &c, const Complex &z, Complex &series, Complex &deriv)   
Returns the hypergeometric series ${ } _ { 2 } F _ { 1 }$ and its derivative, iterating to machine accuracy. For   
$| z | \leq 1 / 2$ convergence is quite rapid.   
{   
deri $\mathtt { v } = 0 . 0$ ;   
Complex fac $^ { = 1 }$ .0;   
Complex temp=fac;   
Complex $\mathtt { a a } = \mathtt { a }$ ;   
Complex bb=b;   
Complex $\mathtt { C C } { = } \mathtt { C }$ ;   
for (Int $\tt { n } { = } 1$ ; $\mathtt { n < = 1 0 0 0 ; n + + } )$ ) { fac $\ast =$ ((aa\*bb)/cc); deriv $+ =$ fac; fac $\ast = \mathrm { ~ ( ~ ( ~ 1 ~ . ~ 0 / n ) \ast z ) ~ }$ ; series $=$ temp+fac; if (series $= =$ temp) return; temp=series; aa $+ = \ 1 . 0$ ; bb $+ = \ 1 . 0$ ; cc $+ = \ 1 . 0$ ;   
}   
throw("convergence failure in h

# }

# struct Hypderiv {

Functor to compute derivatives for the hypergeometric equation; see text equation (5.14.4).

Complex a,b,c,z0,dz; Hypderiv(const Complex &aa, const Complex &bb, const Complex &cc, const Complex &z00, const Complex &dzz) : a(aa),b(bb),c(cc),z0(z00),dz(dzz) {} void operator() (const Doub s, VecDoub_I &yy, VecDoub_O &dyyds) { Complex z,y[2],dyds[2]; y[0] $=$ Complex(yy[0],yy[1]); y[1]=Complex(yy[2],yy[3]); z=z0+s\*dz; dyds[0] $\mathbf { \Pi } = \mathbf { y }$ [1]\*dz; dyds[1] $=$ (a\*b\*y[0]-(c-(a+b+1.0)\*z)\*y[1])\*dz/(z\*(1.0-z)); dyyds[0] $=$ real(dyds[0]); dyyds[1] $=$ imag(dyds[0]); dyyds[2] $=$ real(dyds[1]); dyyds[3] $=$ imag(dyds[1]); } };

# CITED REFERENCES AND FURTHER READING:

Abramowitz, M., and Stegun, I.A. 1964, Handbook of Mathematical Functions (Washington: National Bureau of Standards); reprinted 1968 (New York: Dover); online at http://www.nr. com/aands.[1]

# 6.14 Statistical Functions

Certain special functions get frequent use because of their relation to common univariate statistical distributions, that is, probability densities in a single variable. In this section we survey a number of such common distributions in a unified way, giving, in each case, routines for computing the probability density function $p ( x )$ ; the cumulative density function or cdf, written $P ( < x )$ ; and the inverse of the cumulative density function $x ( P )$ . The latter function is needed for finding the values of $x$ associated with specified percentile points or quantiles in significance tests, for example, the $0 . 5 \%$ , $5 \%$ , $9 5 \%$ or $9 9 . 5 \%$ points.

The emphasis of this section is on defining and computing these statistical functions. Section $\ S 7 . 3$ is a related section that discusses how to generate random deviates from the distributions discussed here. We defer discussion of the actual use of these distributions in statistical tests to Chapter 14.

# 6.14.1 Normal (Gaussian) Distribution

If $x$ is drawn from a normal distribution with mean $\mu$ and standard deviation $\sigma$ , then we write

$$
\begin{array} { c } { { x \sim \mathrm { N } ( \mu , \sigma ) , \sigma > 0 } } \\ { { p ( x ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } \sigma } \exp \left( - \frac { 1 } { 2 } \left[ \frac { x - \mu } { \sigma } \right] ^ { 2 } \right) } } \end{array}
$$

with $p ( x )$ the probability density function. Note the special use of the notation “
” in this section, which can be read as “is drawn from a distribution.” The variance of the distribution is, of course, $\sigma ^ { 2 }$ .

The cumulative distribution function is the probability of a value $\leq x$ . For the normal distribution, this is given in terms of the complementary error function by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { - \infty } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = { \frac { 1 } { 2 } } \operatorname { e r f c } \left( - { \frac { 1 } { \sqrt { 2 } } } \left[ { \frac { x - \mu } { \sigma } } \right] \right)
$$

The inverse cdf can thus be calculated in terms of the inverse of erfc,

$$
x ( P ) = \mu - \sqrt { 2 } \sigma \mathrm { e r f c } ^ { - 1 } ( 2 P )
$$

The following structure implements the above relations.

![](images/6067bf5da51e310225eed902504246e2af8263de816533687455c48d1aa2a521.jpg)  
Figure 6.14.1. Examples of centrally peaked distributions that are symmetric on the real line. Any of these can substitute for the normal distribution either as an approximation or in applications such as robust estimation. They differ largely in the decay rate of their tails.

# struct Normaldist : Erf {

Normal distribution, derived from the error function Erf. Doub mu, sig; Normaldist(Doub mmu $\qquad = \ 0 .$ , Doub ssig $\qquad = \ 1 .$ ) : mu(mmu), sig(ssig) { Constructor. Initialize with $\mu$ and $\sigma$ . The default with no arguments is ${ \mathsf { N } } ( 0 , 1 )$ . if (sig $< = ~ 0 .$ ) throw("bad sig in Normaldist"); } Doub p(Doub x) { Return probability density function. return (0.398942280401432678/sig)\*exp(-0.5\*SQR((x-mu)/sig)); } Doub cdf(Doub x) { Return cumulative distribution function. return 0.5\*erfc(-0.707106781186547524\*(x-mu)/sig); Doub invcdf(Doub p) { Return inverse cumulative distribution function. if ( $\mathbf { \partial } \cdot \mathbf { p } < = \mathbf { \partial } 0$ . $| \mathrm { ~ l ~ } \mathrm { ~ p ~ } > = \mathrm { ~ 1 ~ } .$ ) throw("bad p in Normaldist"); return -1.41421356237309505\*sig\*inverfc $( 2 , * _ { \mathrm { P } } ) + \mathrm { m u }$ ; }   
};

We will use the conventions of the above code for all the distributions in this section. A distribution’s parameters (here, $\mu$ and $\sigma$ ) are set by the constructor and then referenced as needed by the member functions. The density function is always $\mathtt { p ( ) }$ , the cdf is cdf(), and the inverse cdf is invcdf(). We will generally check the arguments of probability functions for validity, since many program bugs can show up as, e.g., a probability out of the range Œ0; 1.

# 6.14.2 Cauchy Distribution

Like the normal distribution, the Cauchy distribution is a centrally peaked, symmetric distribution with a parameter $\mu$ that specifies its center and a parameter $\sigma$ that specifies its width. Unlike the normal distribution, the Cauchy distribution has tails that decay very slowly at infinity, as $| x | ^ { - 2 }$ , so slowly that moments higher than the zeroth moment (the area under the curve) don’t even exist. The parameter $\mu$ is therefore, strictly speaking, not the mean, and the parameter $\sigma$ is not, technically, the standard deviation. But these two parameters substitute for those moments as measures of central position and width.

The defining probability density is

$$
\begin{array} { c } { x \sim \mathrm { C a u c h y } ( \mu , \sigma ) , \qquad \sigma > 0 } \\ { p ( x ) = \displaystyle \frac { 1 } { \pi \sigma } \left( 1 + \left[ \frac { x - \mu } { \sigma } \right] ^ { 2 } \right) ^ { - 1 } } \end{array}
$$

If $x \sim { \mathrm { C a u c h y } } ( 0 , 1 )$ , then also $1 / x \sim \mathrm { C a u c h y } ( 0 , 1 )$ and also $( a x + b ) ^ { - 1 } \sim$ Cauchy $( - b / a , 1 / a )$ .

The cdf is given by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { - \infty } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = { \frac { 1 } { 2 } } + { \frac { 1 } { \pi } } \arctan \left( { \frac { x - \mu } { \sigma } } \right)
$$

The inverse cdf is given by

$$
x ( P ) = \mu + \sigma \tan \left( \pi [ P - { \textstyle { \frac { 1 } { 2 } } } ] \right)
$$

Figure 6.14.1 shows Cauchy $( 0 , 1 )$ as compared to the normal distribution $\mathrm { { N } } ( 0 , 1 )$ , as well as several other similarly shaped distributions discussed below.

The Cauchy distribution is sometimes called the Lorentzian distribution.

# struct Cauchydist {

Cauchy distribution.

Doub mu, sig;   
Cauchydist(Doub ${ \tt m m u } = 0 .$ , Doub $\mathbf { s s i g } = \mathbf { 1 . } ) \mathbf { \Sigma } : \mathrm { \ m u ( m m u ) }$ , sig(ssig) {   
Constructor. Initialize with $\mu$ and $\sigma$ . The default with no arguments is Cauchy.0; 1/. if (sig $< = ~ 0 .$ ) throw("bad sig in Cauchydist");   
}   
Doub p(Doub x) {   
Return probability density function. return 0.318309886183790671/(sig\*(1.+SQR((x-mu)/sig)));   
1   
Doub cdf(Doub x) {   
Return cumulative distribution function. return $0 . 5 \substack { + 0 }$ .318309886183790671\*atan2(x-mu,sig);   
}   
Doub invcdf(Doub p) {   
Return inverse cumulative distribution function. if $( \mathtt { p } \ < = \ 0$ . $| \texttt { p } > = 1 .$ ) throw("bad p in Cauchydist"); return mu $^ +$ sig\*tan(3.14159265358979324\*(p-0.5));   
}

# 6.14.3 Student-t Distribution

A generalization of the Cauchy distribution is the Student-t distribution, named for the early 20th century statistician William Gosset, who published under the name “Student” because his employer, Guinness Breweries, required him to use a pseudonym. Like the Cauchy distribution, the Student-t distribution has power-law tails at infinity, but it has an additional parameter $\nu$ that specifies how rapidly they decay, namely as $| t | ^ { - ( \nu + 1 ) }$ . When $\nu$ is an integer, the number of convergent moments, including the zeroth, is thus $\nu$ .

The defining probability density (conventionally written in a variable $t$ instead of $x$ ) is

$$
\begin{array} { l } { t \sim \mathrm { S t u d e n t } ( \nu , \mu , \sigma ) , \qquad \nu > 0 , \sigma > 0 } \\ { p ( t ) = \displaystyle \frac { \Gamma ( \frac { 1 } { 2 } [ \nu + 1 ] ) } { \Gamma ( \frac { 1 } { 2 } \nu ) \sqrt { \nu \pi } \sigma } \left( 1 + \frac { 1 } { \nu } \left[ \frac { t - \mu } { \sigma } \right] ^ { 2 } \right) ^ { - \frac { 1 } { 2 } ( \nu + 1 ) } } \end{array}
$$

The Cauchy distribution is obtained in the case $\nu = 1$ . In the opposite limit, $\nu \to \infty$ , the normal distribution is obtained. In pre-computer days, this was the basis of various approximation schemes for the normal distribution, now all generally irrelevant. Figure 6.14.1 shows examples of the Student-t distribution for $\nu ~ = ~ 1$ (Cauchy), $\nu = 4$ , and $\nu = 6$ . The approach to the normal distribution is evident.

The mean of Student $( \nu , \mu , \sigma )$ is (by symmetry) $\mu$ . The variance is not $\sigma ^ { 2 }$ , but rather

$$
\operatorname { V a r } \{ \operatorname { S t u d e n t } ( \nu , \mu , \sigma ) \} = \frac { \nu } { \nu - 2 } \sigma ^ { 2 }
$$

For additional moments, and other properties, see [1].

The cdf is given by an incomplete beta function. If we let

$$
x \equiv \frac { \nu } { \nu + \left( \frac { t - \mu } { \sigma } \right) ^ { 2 } }
$$

then

$$
\operatorname { c d f } \equiv P ( < t ) \equiv \int _ { - \infty } ^ { t } p ( t ^ { \prime } ) d t ^ { \prime } = { \left\{ \begin{array} { l l } { { \frac { 1 } { 2 } } I _ { x } ( { \frac { 1 } { 2 } } \nu , { \frac { 1 } { 2 } } ) , } & { t \leq \mu } \\ { 1 - { \frac { 1 } { 2 } } I _ { x } ( { \frac { 1 } { 2 } } \nu , { \frac { 1 } { 2 } } ) , } & { t > \mu } \end{array} \right. }
$$

The inverse cdf is given by an inverse incomplete beta function (see code below for the exact formulation).

In practice, the Student-t cdf is the above form is rarely used, since most statistical tests using Student-t are double-sided. Conventionally, the two-tailed function $A ( t | \nu )$ is defined (only) for the case $\mu = 0$ and $\sigma = 1$ by

$$
A ( t | \nu ) \equiv \int _ { - t } ^ { + t } p ( t ^ { \prime } ) d t ^ { \prime } = 1 - I _ { x } ( \frac { 1 } { 2 } \nu , \frac { 1 } { 2 } )
$$

with $x$ as given above. The statistic $A ( t | \nu )$ is notably used in the test of whether two observed distributions have the same mean. The code below implements both equations (6.14.10) and (6.14.11), as well as their inverses.

uct Studenttdist : Beta {   
dent-t distribution, derived from the beta function Beta.   
Doub nu, mu, sig, np, fac;   
Studenttdist(Doub nnu, Doub mmu $\qquad = \ 0 .$ , Doub ssig $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ )   
: nu(nnu), mu(mmu), sig(ssig) {   
Constructor. Initialize with $\nu$ , $\mu$ and $\sigma$ . The default with one argument is Student $( \nu , 0 , 1 )$ . if (sig $\scriptstyle < = \ 0$ . || nu $< = ~ 0 .$ ) throw("bad sig,nu in Studentdist"); ${ \tt n p } = 0 . 5 * ( \tt n u + 1 . )$ ; fac $=$ gammln(np)-gammln(0.5\*nu);   
}   
Doub p(Doub t) {   
Return probability density function. return exp(-np\*log(1.+SQR((t-mu)/sig)/nu)+fac) /(sqrt(3.14159265358979324\*nu)\*sig);   
}   
Doub cdf(Doub t) {   
Return cumulative distribution function. Doub $\mathrm { ~ p ~ } = \mathrm { ~ 0 ~ }$ .5\*betai(0. $5 * \mathrm { n u }$ , 0.5, nu/(nu+SQR((t-mu)/sig))); if $\bf \Pi _ { t } ^ { \prime } > = \ m u _ { \tau } ^ { \prime }$ ) return 1. - p; else return p;   
}   
Doub invcdf(Doub p) {   
Return inverse cumulative distribution function. if $\mathbf { \Phi } \cdot \mathbf { p } \ < = \ 0$ . $| \mathbf { \Psi } | \mathbf { \Psi } \supset = \mathbf { \Psi } 1 .$ ) throw("bad p in Studentdist"); Doub $\mathrm { ~ \tt ~ { ~ x ~ } ~ } =$ invbetai(2.\*MIN(p,1.-p), 0.5\*nu, 0.5); $\mathrm { ~ x ~ } =$ sig\*sqrt(nu\*(1.-x)/x); return $( \mathrm { p } > = 0 . 5 ? \mathrm { \ m u + x : \ m u - x ) }$ ;   
}   
Doub aa(Doub t) {   
Return the two-tailed cdf $A ( t | \nu )$ . if $\ : \mathrm { ~  ~ \cdot ~ } \ t \in \ : 0 . \ :$ ) throw("bad t in Studentdist"); return 1.-betai(0. ${ 5 * } \mathrm { n u }$ , 0.5, nu/(nu+SQR(t)));   
Doub invaa(Doub p) {   
Return the inverse, namely $t$ such that $p = A ( t | \nu )$ . if $\tt ( p < 0$ . $| \mathrm { ~ l ~ } \mathrm { ~ p ~ } > = \mathrm { ~ 1 ~ } .$ ) throw("bad p in Studentdist"); Doub $_ { \textrm { x } } =$ invbetai(1.-p, $0 . 5 { \ast } \mathrm { n u }$ , 0.5); return sqrt $\left( \mathtt { n u * } \left( 1 \ldots \right) / \mathtt { x } \right)$ ;   
}

# 6.14.4 Logistic Distribution

The logistic distribution is another symmetric, centrally peaked distribution that can be used instead of the normal distribution. Its tails decay exponentially, but still much more slowly than the normal distribution’s “exponent of the square.”

The defining probability density is

$$
p ( y ) = { \frac { e ^ { - y } } { ( 1 + e ^ { - y } ) ^ { 2 } } } = { \frac { e ^ { y } } { ( 1 + e ^ { y } ) ^ { 2 } } } = { \textstyle { \frac { 1 } { 4 } } } \mathrm { s e c h } ^ { 2 } \left( { \frac { 1 } { 2 } } y \right)
$$

The three forms are algebraically equivalent, but, to avoid overflows, it is wise to use the negative and positive exponential forms for positive and negative values of $y$ , respectively.

The variance of the distribution (6.14.12) turns out to be $\pi ^ { 2 } / 3$ . Since it is convenient to have parameters $\mu$ and $\sigma$ with the conventional meanings of mean and standard deviation, equation (6.14.12) is often replaced by the standardized logistic

distribution,

$$
\begin{array} { c c l } { { x \sim \mathrm { L o g i s t i c } ( \mu , \sigma ) , } } & { { \sigma > 0 } } \\ { { p ( x ) = \displaystyle \frac { \pi } { 4 \sqrt { 3 } \sigma } \mathrm { s e c h } ^ { 2 } \left( \displaystyle \frac { \pi } { 2 \sqrt { 3 } } \left[ \displaystyle \frac { x - \mu } { \sigma } \right] \right) } } \end{array}
$$

which implies equivalent forms using the positive and negative exponentials (see code below).

The cdf is given by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { - \infty } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = \left[ 1 + \exp \left( - { \frac { \pi } { \sqrt { 3 } } } \left[ { \frac { x - \mu } { \sigma } } \right] \right) \right] ^ { - 1 }
$$

The inverse cdf is given by

$$
x ( P ) = \mu + { \frac { \sqrt { 3 } } { \pi } } \sigma \log \left( { \frac { P } { 1 - P } } \right)
$$

struct Logisticdist {   
Logistic distribution. Doub mu, sig; Logisticdist(Doub mmu $\mathit { \Theta } = \mathit { \Theta } 0 .$ , Doub ssig $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ) : mu(mmu), sig(ssig) { Constructor. Initialize with $\mu$ and $\sigma$ . The default with no arguments is Logistic.0; 1/. if (sig $< = ~ 0 .$ ) throw("bad sig in Logisticdist"); } Doub p(Doub x) { Return probability density function. Doub e $=$ exp(-abs(1.81379936423421785\*(x-mu)/sig)); return 1.81379936423421785\*e/(sig\*SQR(1.+e)); } Doub cdf(Doub x) { Return cumulative distribution function. Doub $\qquad \mathtt { \ e } \quad =$ exp(-abs(1.81379936423421785\*(x-mu)/sig)); if $\mathbf { \Omega } ( \mathbf { x } ) = \mathbf { \Omega } \cdot \mathbf { n } \mathbf { u } .$ ) return 1./(1.+e); Because we used abs to control overelse return ${ \mathsf { e } } / ( 1 . + { \mathsf { e } } )$ ; flow, we now have two cases. } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $( \mathtt { p } \ < = \ 0$ . | $| \mathrm { ~  ~ p ~ } > = 1 .$ ) throw("bad p in Logisticdist"); return mu $+ \ 0$ .551328895421792049\*sig\*log(p/(1.-p)); }   
};

The logistic distribution is cousin to the logit transformation that maps the open unit interval $0 < p < 1$ onto the real line $- \infty < u < \infty$ by the relation

$$
u = \log \left( { \frac { p } { 1 - p } } \right)
$$

Back when a book of tables and a slide rule were a statistician’s working tools, the logit transformation was used to approximate processes on the interval by analytically simpler processes on the real line. A uniform distribution on the interval maps by the logit transformation to a logistic distribution on the real line. With the computer’s ability to calculate distributions on the interval directly (beta distributions, for example), that motivation has vanished.

![](images/5fa30d7264f90c22ec2c86fa58c08ed1c9e7245b6302b56f0ecfac879c033c18.jpg)  
Figure 6.14.2. Examples of common distributions on the half-line $x > 0$ .

Another cousin is the logistic equation,

$$
\frac { d y } { d t } \propto y ( y _ { \mathrm { { m a x } } } - y )
$$

a differential equation describing the growth of some quantity $y$ , starting off as an exponential but reaching, asymptotically, a value $y _ { \mathrm { m a x } }$ . The solution of this equation is identical, up to a scaling, to the cdf of the logistic distribution.

# 6.14.5 Exponential Distribution

With the exponential distribution we now turn to common distribution functions defined on the positive real axis $x \ge 0$ . Figure 6.14.2 shows examples of several of the distributions that we will discuss. The exponential is the simplest of them all. It has a parameter $\beta$ that can control its width (in inverse relationship), but its mode is always at zero:

$$
\begin{array} { c } { x \displaystyle \mathrm { ~ \ w \ w o n e n u a l { } ( \boldsymbol { p } ) , ~ } \quad \mathrm { ~ } \boldsymbol { p } \mathrm { ~ } \mathrm { > ~ } 0 } \\ { p \displaystyle ( \boldsymbol { x } ) = \beta \exp ( - \beta \boldsymbol { x } ) , \qquad \boldsymbol { x } \mathrm { ~ } \mathrm { > ~ } 0 } \\ { \displaystyle \mathrm { ~ } \mathrm { c d f } \equiv P ( < \boldsymbol { x } ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = 1 - \exp ( - \beta x ) } \\ { x ( P ) = - \frac { 1 } { \beta } \log ( 1 - P ) } \end{array}
$$

The mean and standard deviation of the exponential distribution are both $1 / \beta$ . The median is $\log ( 2 ) / \beta$ . Reference [1] has more to say about the exponential distribution than you would ever think possible.


<!-- chunk 0006: pages 351-420 -->
# struct Expondist {

Exponential distribution. Doub bet; Expondist(Doub bbet) : bet(bbet) { Constructor. Initialize with $\beta$ . if (bet $< = ~ 0 .$ ) throw("bad bet in Expondist"); } Doub p(Doub x) { Return probability density function. if ( $\mathbf { \Phi } _ { \mathbf { x } } < \mathbf { \Phi } 0 .$ ) throw("bad x in Expondist"); return bet\*exp(-bet\*x); } Doub cdf(Doub x) { Return cumulative distribution function. if $( \mathbb { x } \ < \ 0 .$ ) throw("bad x in Expondist"); return 1.-exp(-bet\*x); Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $\mathtt { ( p < 0 }$ . || $\mathrm {  ~ p ~ } > = \mathrm {  ~ 1 ~ } .$ ) throw("bad p in Expondist"); return -log(1.-p)/bet; }   
};

# 6.14.6 Weibull Distribution

The Weibull distribution generalizes the exponential distribution in a way that is often useful in hazard, survival, or reliability studies. When the lifetime (time to failure) of an item is exponentially distributed, there is a constant probability per unit time that an item will fail, if it has not already done so. That is,

$$
{ \mathrm { h a z a r d } } \equiv { \frac { p ( x ) } { P ( > x ) } } \propto { \mathrm { c o n s t a n t } }
$$

Exponentially lived items don’t age; they just keep rolling the same dice until, one day, their number comes up. In many other situations, however, it is observed that an item’s hazard (as defined above) does change with time, say as a power law,

$$
{ \frac { p ( x ) } { P ( > x ) } } \propto x ^ { \alpha - 1 } , \qquad \alpha > 0
$$

The distribution that results is the Weibull distribution, named for Swedish physicist Waloddi Weibull, who used it as early as 1939. When $\alpha > 1$ , the hazard increases with time, as for components that wear out. When $0 < \alpha < 1$ , the hazard decreases with time, as for components that experience “infant mortality.”

We say that

$$
x \sim \mathrm { { W e i b u l l } } ( \alpha , \beta ) \qquad \mathrm { { i f f } } \qquad y \equiv \left( { \frac { x } { \beta } } \right) ^ { \alpha } \sim \mathrm { { E x p o n e n t i a l } } ( 1 )
$$

The probability density is

$$
p ( x ) = \left( { \frac { \alpha } { \beta } } \right) \left( { \frac { x } { \beta } } \right) ^ { \alpha - 1 } e ^ { - ( x / \beta ) ^ { \alpha } } , \qquad x > 0
$$

The cdf is

$$
{ \mathrm { c d f } } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = 1 - e ^ { - ( x / \beta ) ^ { \alpha } }
$$

The inverse cdf is

$$
x ( P ) = \beta [ - \log ( 1 - P ) ] ^ { 1 / \alpha }
$$

For $0 < \alpha < 1$ , the distribution has an infinite (but integrable) cusp at $x = 0$ and is monotonically decreasing. The exponential distribution is the case of $\alpha = 1$ . When $\alpha > 1$ , the distribution is zero at $x = 0$ and has a single maximum at the value $x = \beta [ ( \alpha - 1 ) / \alpha ] ^ { 1 / \alpha }$ .

The mean and variance are given by

$$
\begin{array} { c l c r } { \mu = \beta \Gamma ( 1 + \alpha ^ { - 1 } ) } \\ { \sigma ^ { 2 } = \beta ^ { 2 } \left\{ \Gamma ( 1 + 2 \alpha ^ { - 1 } ) - \left[ \Gamma ( 1 + \alpha ^ { - 1 } ) \right] ^ { 2 } \right\} } \end{array}
$$

With correct normalization, equation (6.14.22) becomes

$$
{ \mathrm { h a z a r d } } \equiv { \frac { p ( x ) } { P ( > x ) } } = \left( { \frac { \alpha } { \beta } } \right) \left( { \frac { x } { \beta } } \right) ^ { \alpha - 1 }
$$

# 6.14.7 Lognormal Distribution

Many processes that live on the positive $x$ -axis are naturally approximated by normal distributions on the $ { \mathbf { \hat { \theta } } } _ { \mathrm { { l o g } } } ( x )$ -axis,” that is, for $- \infty < \log ( x ) < \infty$ . A simple, but important, example is the multiplicative random walk, which starts at some positive value $x _ { 0 }$ , and then generates new values by a recurrence like

$$
x _ { i + 1 } = \left\{ \begin{array} { l l } { x _ { i } ( 1 + \epsilon ) } & { \mathrm { w i t h } \mathrm { p r o b a b i l i t y } 0 . 5 } \\ { x _ { i } / ( 1 + \epsilon ) } & { \mathrm { w i t h } \mathrm { p r o b a b i l i t y } 0 . 5 } \end{array} \right.
$$

Here $\epsilon$ is some small, fixed, constant.

These considerations motivate the definition

$$
x \sim \operatorname { L o g n o r m a l } ( \mu , \sigma ) \qquad { \mathrm { i f f } } \qquad u \equiv { \frac { \log ( x ) - \mu } { \sigma } } \sim \operatorname { N } ( 0 , 1 )
$$

or the equivalent definition

$$
\begin{array} { c } { { x \sim \mathrm { L o g n o r m a l } ( \mu , \sigma ) , \qquad \sigma > 0 } } \\ { { p ( x ) = \displaystyle \frac { 1 } { \sqrt { 2 \pi } \sigma x } \exp \left( - \frac { 1 } { 2 } \left[ \frac { \log ( x ) - \mu } { \sigma } \right] ^ { 2 } \right) , \qquad x > 0 } } \end{array}
$$

Note the required extra factor of $x ^ { - 1 }$ in front of the exponential: The density that is “normal” is $p ( \log x ) d \log x$ .

While $\mu$ and $\sigma$ are the mean and standard deviation in $\log x$ space, they are not so in $x$ space. Rather,

$$
\begin{array} { r l } & { \mathrm { M e a n } \{ \mathrm { L o g n o r m a l } ( \mu , \sigma ) \} = e ^ { \mu + \frac { 1 } { 2 } \sigma ^ { 2 } } } \\ & { \quad \mathrm { V a r } \{ \mathrm { L o g n o r m a l } ( \mu , \sigma ) \} = e ^ { 2 \mu } e ^ { \sigma ^ { 2 } } ( e ^ { \sigma ^ { 2 } } - 1 ) } \end{array}
$$

The cdf is given by

$$
\operatorname { c d f } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = { \frac { 1 } { 2 } } \mathrm { e r f c } \left( - { \frac { 1 } { \sqrt { 2 } } } \left[ { \frac { \log ( x ) - \mu } { \sigma } } \right] \right)
$$

The inverse to the cdf involves the inverse complementary error function,

$$
x ( P ) = \exp [ \mu - \sqrt { 2 } \sigma \mathrm { e r f c } ^ { - 1 } ( 2 P ) ]
$$

# struct Lognormaldist : Erf {

# erf.h

Lognormal distribution, derived from the error function Erf.

Doub mu, sig; Lognormaldist(Doub mmu $\qquad = \ 0 .$ , Doub ssig $\begin{array} { r l } { \mathbf { \Psi } } & { { } = \mathbf { \Psi } \perp \mathbf { \Psi } . } \end{array}$ .) : mu(mmu), sig(ssig) { if (sig $< = ~ 0 .$ ) throw("bad sig in Lognormaldist"); } Doub p(Doub x) { Return probability density function. if ( $\begin{array} { r } { \mathrm { ~  ~ x ~ } < 0 . } \end{array}$ ) throw("bad x in Lognormaldist"); if ( $\mathbf { x } \ = = \ 0 .$ ) return 0.; return (0.398942280401432678/(sig\*x))\*exp(-0.5\*SQR((log(x)-mu)/sig)); } Doub cdf(Doub x) { Return cumulative distribution function. if ( $\mathbf { \Phi } _ { \mathbf { x } } < \mathbf { \Phi } 0 .$ ) throw("bad x in Lognormaldist"); if ( $\mathbf { x } \ = = \ 0 .$ ) return 0.; return 0.5\*erfc(-0.707106781186547524\*(log(x)-mu)/sig); } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $_ { \mathrm { ~ \tiny ~ Q ~ } } < = \mathrm { ~ \tiny ~ 0 ~ }$ . $| \mathbf { \Psi } | \mathbf { \Psi } \supset = \mathbf { \Psi } 1 .$ ) throw("bad p in Lognormaldist"); return exp(-1.41421356237309505\*sig\*inverfc(2.\*p)+mu); } };

Multiplicative random walks like (6.14.29) and lognormal distributions are key ingredients in the economic theory of efficient markets, leading to (among many other results) the celebrated Black-Scholes formula for the probability distribution of the price of an investment after some elapsed time $\tau$ . A key piece of the Black-Scholes derivation is implicit in equation (6.14.32): If an investment’s average return is zero (which may be true in the limit of zero risk), then its price cannot simply be a widening lognormal distribution with fixed $\mu$ and increasing $\sigma$ , for its expected value would then diverge to infinity! The actual Black-Scholes formula thus defines both how $\sigma$ increases with time (basically as $\tau ^ { 1 / 2 }$ ) and how $\mu$ correspondingly decreases with time, so as to keep the overall mean under control. A simplified version of the Black-Scholes formula can be written as

$$
\begin{array} { r } { S ( \tau ) \sim S ( 0 ) \times \mathrm { L o g n o r m a l } \left( r \tau - \frac { 1 } { 2 } \sigma ^ { 2 } \tau , \sigma \sqrt { \tau } \right) } \end{array}
$$

where $S ( \tau )$ is the price of a stock at time $\tau , r$ is its expected (annualized) rate of return, and $\sigma$ is now redefined to be the stock’s (annualized) volatility. The definition of volatility is that, for small values of $\tau$ , the fractional variance of the stock’s price is $\sigma ^ { 2 } \tau$ . You can check that (6.14.35) has the desired expectation value $E [ S ( \tau ) ] =$ $S ( 0 )$ , for all $\tau$ , if $r = 0$ . A good reference is [3].

# 6.14.8 Chi-Square Distribution

The chi-square (or $\chi ^ { 2 }$ ) distribution has a single parameter $\nu > 0$ that controls both the location and width of its peak. In most applications $\nu$ is an integer and is referred to as the number of degrees of freedom (see $\ S 1 4 . 3 )$ .

The defining probability density is

$$
\begin{array} { c c } { { \chi ^ { 2 } \sim \mathrm { C h i s q u a r e } ( \nu ) , } } & { { \nu > 0 } } \\ { { p ( \chi ^ { 2 } ) d \chi ^ { 2 } = \frac { 1 } { 2 ^ { \frac { 1 } { 2 } \nu } \Gamma ( { \frac { 1 } { 2 } } \nu ) } ( \chi ^ { 2 } ) ^ { \frac { 1 } { 2 } \nu - 1 } \exp \left( - { \frac { 1 } { 2 } } \chi ^ { 2 } \right) d \chi ^ { 2 } , } } & { { \chi ^ { 2 } > 0 } } \end{array}
$$

where we have written the differentials $d \chi ^ { 2 }$ merely to emphasize that $\chi ^ { 2 }$ , not $\chi$ , is to be viewed as the independent variable.

The mean and variance are given by

$$
\begin{array} { r } { \mathrm { M e a n } \{ \mathrm { C h i s q u a r e } ( \nu ) \} = \nu } \\ { \mathrm { V a r } \{ \mathrm { C h i s q u a r e } ( \nu ) \} = 2 \nu } \end{array}
$$

When $\nu \geq 2$ there is a single mode at $\chi ^ { 2 } = \nu - 2$ .

The chi-square distribution is actually just a special case of the gamma distribution, below, so its cdf is given by an incomplete gamma function $P ( \boldsymbol { a } , \boldsymbol { x } )$ ,

$$
{ \mathrm { c d f } } \equiv P ( < \chi ^ { 2 } ) \equiv P ( \chi ^ { 2 } | \nu ) \equiv \int _ { 0 } ^ { \chi ^ { 2 } } p ( \chi ^ { 2 \prime } ) d \chi ^ { 2 \prime } = P \left( { \frac { \nu } { 2 } } , { \frac { \chi ^ { 2 } } { 2 } } \right)
$$

One frequently also sees the complement of the cdf, which can be calculated either from the incomplete gamma function $P ( \boldsymbol { a } , \boldsymbol { x } )$ , or from its complement $Q ( a , x )$ (often more accurate if $P$ is very close to 1):

$$
\mathcal { Q } ( \chi ^ { 2 } | \nu ) \equiv 1 - P ( \chi ^ { 2 } | n ) = 1 - P \left( \frac { \nu } { 2 } , \frac { \chi ^ { 2 } } { 2 } \right) \equiv Q \left( \frac { \nu } { 2 } , \frac { \chi ^ { 2 } } { 2 } \right)
$$

The inverse cdf is given in terms of the function that is the inverse of $P ( \boldsymbol { a } , \boldsymbol { x } )$ on its second argument, which we here denote $P ^ { - 1 } ( a , p )$ :

$$
x ( P ) = 2 P ^ { - 1 } \left( { \frac { \nu } { 2 } } , P \right)
$$

# struct Chisqdist : Gamma {

$\chi ^ { 2 }$ distribution, derived from the gamma function Gamma.

Doub nu,fac;   
Chisqdist(Doub nnu) : nu(nnu) {   
Constructor. Initialize with $\nu$ . if $\mathrm {  ~ \Omega ~ } ^ { \prime } \mathrm {  ~ \ n u ~ } < = \mathrm {  ~ \Omega ~ } 0 .$ ) throw("bad nu in Chisqdist"); fac $\mathit { \Theta } = \mathit { \Theta } 0$ .693147180559945309\*(0.5\*nu)+gammln(0.5\*nu);   
}   
Doub p(Doub x2) {   
Return probability density function. if $( \mathbf { x } 2 \ < = \ 0 .$ ) throw("bad x2 in Chisqdist"); return exp(-0.5\*(x2-(nu-2.)\*log(x2))-fac);   
}   
Doub cdf(Doub x2) {

Return cumulative distribution function. if $\left( \mathbf { x } 2 \ < \ 0 . \right.$ ) throw("bad x2 in Chisqdist"); return gammp $( 0 . 5 * \mathrm { n u } , 0 . 5 * \mathrm { x } 2 )$ ; Doub invcdf(Doub p) { Return inverse cumulative distribution function. if ${ \mathrm { ( p ~ < ~ } } 0$ . $| \mathrm { ~ \bf ~ \underline { ~ } { ~ \underline { ~ } { ~ p ~ } ~ } ~ } > = \mathrm { ~ \bf ~ 1 ~ } .$ ) throw("bad p in Chisqdist"); return 2.\*invgammp(p,0.5\*nu); } };

# 6.14.9 Gamma Distribution

The gamma distribution is defined by

$$
\begin{array} { r l r l } { x \sim \mathrm { G a m m a } ( \alpha , \beta ) , } & { } & { \alpha > 0 , \beta > 0 } \\ { p ( x ) = \displaystyle \frac { \beta ^ { \alpha } } { \Gamma ( \alpha ) } x ^ { \alpha - 1 } e ^ { - \beta x } , } & { } & { x > 0 } \end{array}
$$

The exponential distribution is the special case with $\alpha = 1$ . The chi-square distribution is the special case with $\alpha = \nu / 2$ and $\beta = 1 / 2$ .

The mean and variance are given by,

$$
\begin{array} { r } { \mathrm { M e a n } \{ \mathrm { G a m m a } ( \alpha , \beta ) \} = \alpha / \beta } \\ { \mathrm { V a r } \{ \mathrm { G a m m a } ( \alpha , \beta ) \} = \alpha / \beta ^ { 2 } } \end{array}
$$

When $\alpha \geq 1$ there is a single mode at $x = ( \alpha - 1 ) / \beta$ .

Evidently, the cdf is the incomplete gamma function

$$
{ \mathrm { c d f } } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = P \left( \alpha , \beta x \right)
$$

while the inverse cdf is given in terms of the inverse of $P ( \boldsymbol { a } , \boldsymbol { x } )$ on its second argument by

$$
x ( P ) = \frac { 1 } { \beta } P ^ { - 1 } \left( \alpha , P \right)
$$

# struct Gammadist : Gamma {

amma distribution, derived from the gamma function Gamma.

Doub alph, bet, fac;   
Gammadist(Doub aalph, Doub bbet $\qquad = \ 1 \ .$ ) : alph(aalph), bet(bbet) {   
Constructor. Initialize with $\pmb { \alpha }$ and $\beta$ . if (alph $\scriptstyle < = \ 0$ . || bet $< = ~ 0 .$ ) throw("bad alph,bet in Gammadist"); fac $=$ alph\*log(bet)-gammln(alph);   
}   
Doub p(Doub x) {   
Return probability density function. if ( $\mathbf { \bar { x } } \ < = \ 0 .$ ) throw("bad x in Gammadist"); return exp(-bet\*x+(alph-1.)\*log(x)+fac);   
}   
Doub cdf(Doub x) {   
Return cumulative distribution function. if $\mathbf { \Phi } _ { \mathbf { x } } < \mathbf { \Phi } 0 .$ ) throw("bad x in Gammadist"); return gammp(alph,bet\*x);   
}

Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $\mathrm { ~ ( ~ p ~ < ~ 0 ~ }$ . | $| \texttt { p } > = \texttt { 1 } .$ ) throw("bad p in Gammadist"); return invgammp(p,alph)/bet; } };

# 6.14.10 F-Distribution

The $F$ -distribution is parameterized by two positive values $\nu _ { 1 }$ and $\nu _ { 2 }$ , usually (but not always) integers.

The defining probability density is

$$
\begin{array} { c } { { F \sim \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) , \qquad \nu _ { 1 } > 0 , \nu _ { 2 } > 0 } } \\ { { \qquad \nu _ { 1 } ^ { \frac 1 2 \nu _ { 1 } } \nu _ { 2 } ^ { \frac 1 2 \nu _ { 2 } } } } \\ { { p ( F ) = \displaystyle \frac { \nu _ { 1 } ^ { \frac 1 2 \nu _ { 1 } } \nu _ { 2 } ^ { \frac 1 2 } } { B ( \frac 1 2 \nu _ { 1 } , \frac 1 2 \nu _ { 2 } ) } \frac { F ^ { \frac 1 2 \nu _ { 1 } - 1 } } { ( \nu _ { 2 } + \nu _ { 1 } F ) ^ { ( \nu _ { 1 } + \nu _ { 2 } ) / 2 } } , \qquad F > 0 } } \end{array}
$$

where $B ( a , b )$ denotes the beta function. The mean and variance are given by

$$
\begin{array} { r l r } & { \mathrm { M e a n } \{ \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) \} = \frac { \nu _ { 2 } } { \nu _ { 2 } - 2 } , } & { \quad \nu _ { 2 } > 2 } \\ & { \mathrm { V a r } \{ \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) \} = \frac { 2 \nu _ { 2 } ^ { 2 } ( \nu _ { 1 } + \nu _ { 2 } - 2 ) } { \nu _ { 1 } ( \nu _ { 2 } - 2 ) ^ { 2 } ( \nu _ { 2 } - 4 ) } , } & { \quad \nu _ { 2 } > 4 } \end{array}
$$

When $\nu _ { 1 } \geq 2$ there is a single mode at

$$
F = \frac { \nu _ { 2 } ( \nu _ { 1 } - 2 ) } { \nu _ { 1 } ( \nu _ { 2 } + 2 ) }
$$

For fixed $\nu _ { 1 }$ , if $\nu _ { 2 } \to \infty$ , the $F$ -distribution becomes a chi-square distribution, namely

$$
\operatorname* { l i m } _ { \nu _ { 2 } \to \infty } \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } ) \cong \frac { 1 } { \nu _ { 1 } } { \mathrm { C h i s q u a r e } } ( \nu _ { 1 } )
$$

where $\ Y q$ means “are identical distributions.”

The $F$ -distribution’s cdf is given in terms of the incomplete beta function $I _ { x } ( a , b )$ by

$$
{ \mathrm { c d f } } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = I _ { \nu _ { 1 } F / ( \nu _ { 2 } + \nu _ { 1 } F ) } \left( { \frac { 1 } { 2 } } \nu _ { 1 } , { \frac { 1 } { 2 } } \nu _ { 2 } \right)
$$

while the inverse cdf is given in terms of the inverse of $I _ { x } ( a , b )$ on its subscript argument by

$$
\begin{array} { c } { { u \equiv I _ { p } ^ { - 1 } \left( \frac { 1 } { 2 } \nu _ { 1 } , \frac { 1 } { 2 } \nu _ { 2 } \right) } } \\ { { x ( P ) = \displaystyle \frac { \nu _ { 2 } u } { \nu _ { 1 } ( 1 - u ) } } } \end{array}
$$

A frequent use of the $F$ -distribution is to test whether two observed samples have the same variance.

struct Fdist : Beta {   
$F$ distribution, derived from the beta function Beta. Doub nu1,nu2; Doub fac; Fdist(Doub nnu1, Doub nnu2) : nu1(nnu1), nu2(nnu2) { Constructor. Initialize with $\nu _ { 1 }$ and $\nu _ { 2 }$ . if (nu1 $\scriptstyle < = \ 0$ . || nu2 $< = ~ 0 .$ ) throw("bad nu1,nu2 in Fdist"); fac = 0.5\*(nu1\*log(nu1)+nu2\*log(nu2))+gammln(0.5\*(nu1+nu2)) -gammln(0.5\*nu1)-gammln(0.5\*nu2); } Doub p(Doub f) { Return probability density function. if ( ${ \mathrm { ~  ~ \cdot ~ } } { \mathrm { ~  ~ \cdot ~ } } < = { \mathrm { ~  ~ 0 ~ } } .$ ) throw("bad f in Fdist"); return exp((0.5\*nu1-1.)\*log(f)-0.5\*(nu1+nu2)\*log(nu2+nu1\*f)+fac); } Doub cdf(Doub f) { Return cumulative distribution function. if ( $. . . < . . .$ ) throw("bad f in Fdist"); return betai(0. $^ { 5 \ast }$ nu1,0.5\*nu2,nu1\*f/(nu2+nu1\*f)); } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $_ { \mathrm { ~ \tiny ~ Q ~ } } < = \mathrm { ~ \tiny ~ 0 ~ }$ . $| \mathbf { \Psi } | \mathbf { \Psi } \supset = \mathbf { \Psi } 1 .$ ) throw("bad p in Fdist"); Doub $\mathrm { ~ x ~ } =$ invbetai(p,0.5\*nu1,0.5\*nu2); return nu2\*x/(nu1\*(1.-x)); }   
};

# 6.14.11 Beta Distribution

The beta distribution is defined on the unit interval $0 < x < 1$ by

$$
\begin{array} { c } { { x \sim \mathrm { B e t a } ( \alpha , \beta ) , \qquad \alpha > 0 , \beta > 0 } } \\ { { p ( x ) = \displaystyle \frac { 1 } { B ( \alpha , \beta ) } x ^ { \alpha - 1 } ( 1 - x ) ^ { \beta - 1 } , \qquad 0 < x < 1 } } \end{array}
$$

The mean and variance are given by

$$
\begin{array} { l } { { \displaystyle \mathrm { M e a n } \{ \mathrm { B e t a } ( \alpha , \beta ) \} = \frac { \alpha } { \alpha + \beta } } } \\ { { \displaystyle \mathrm { V a r } \{ \mathrm { B e t a } ( \alpha , \beta ) \} = \frac { \alpha \beta } { ( \alpha + \beta ) ^ { 2 } ( \alpha + \beta + 1 ) } } } \end{array}
$$

When $\alpha > 1$ and $\beta > 1$ , there is a single mode at $( \alpha - 1 ) / ( \alpha + \beta - 2 )$ . When $\alpha < 1$ and $\beta < 1$ , the distribution function is “U-shaped” with a minimum at this same value. In other cases there is neither a maximum nor a minimum.

In the limit that $\beta$ becomes large as $\alpha$ is held fixed, all the action in the beta distribution shifts toward $x = 0$ , and the density function takes the shape of a gamma distribution. More precisely,

$$
\operatorname* { l i m } _ { \beta \to \infty } \beta \operatorname { B e t a } ( \alpha , \beta ) \cong \operatorname { G a m m a } ( \alpha , 1 )
$$

The cdf is the incomplete beta function

$$
\mathsf { c d f } \equiv P ( < x ) \equiv \int _ { 0 } ^ { x } p ( x ^ { \prime } ) d x ^ { \prime } = I _ { x } \left( \alpha , \beta \right)
$$

while the inverse cdf is given in terms of the inverse of $I _ { x } ( \alpha , \beta )$ on its subscript argument by

$$
x ( P ) = I _ { p } ^ { - 1 } ( \alpha , \beta )
$$

# struct Betadist : Beta {

Beta distribution, derived from the beta function Beta.

Doub alph, bet, fac; Betadist(Doub aalph, Doub bbet) : alph(aalph), bet(bbet) { Constructor. Initialize with $\pmb { \alpha }$ and $\beta$ . if (alph $< = ~ 0$ . || bet $< = ~ 0 .$ ) throw("bad alph,bet in Betadist"); fac $=$ gammln(alph $\cdot ^ { + }$ bet)-gammln(alph)-gammln(bet); } Doub p(Doub x) { Return probability density function. if $\mathrm { ~  ~ \omega ~ } < = \mathrm { ~  ~ 0 ~ }$ . $| \mathbf { \Psi } | \mathbf { \Psi } \ \mathbf { x } \ > = \ 1 .$ ) throw("bad x in Betadist"); return exp((alph-1.)\*log(x)+(bet-1.)\*log(1.-x)+fac); } Doub cdf(Doub x) { Return cumulative distribution function. if $\mathit { \Omega } _ { \mathrm { ~ x ~ } } < \mathit { \Omega } 0$ . || $\begin{array} { r } { \mathrm { ~ z ~ } > ~ 1 . } \end{array}$ ) throw("bad x in Betadist"); return betai(alph,bet,x); } Doub invcdf(Doub p) { Return inverse cumulative distribution function. if $\mathrm { ~ ( ~ p ~ < ~ 0 ~ }$ . $| \mathsf { I } \ \mathsf { p } > \ \mathsf { 1 } .$ ) throw("bad p in Betadist"); return invbetai(p,alph,bet); } };

# 6.14.12 Kolmogorov-Smirnov Distribution

The Kolmogorov-Smirnov or $K S$ distribution, defined for positive $Z$ , is key to an important statistical test that is discussed in $\ S 1 4 . 3$ . Its probability density function does not directly enter into the test and is virtually never even written down. What one typically needs to compute is the cdf, denoted $P _ { K S } ( z )$ , or its complement, $Q _ { K S } ( z ) \equiv 1 - P _ { K S } ( z )$ .

The cdf $P _ { K S } ( z )$ is defined by the series

$$
P _ { K S } ( z ) = 1 - 2 \sum _ { j = 1 } ^ { \infty } ( - 1 ) ^ { j - 1 } \exp ( - 2 j ^ { 2 } z ^ { 2 } )
$$

or by the equivalent series (nonobviously so!)

$$
P _ { K S } ( z ) = \frac { \sqrt { 2 \pi } } { z } \sum _ { j = 1 } ^ { \infty } \exp { \left( - \frac { ( 2 j - 1 ) ^ { 2 } \pi ^ { 2 } } { 8 z ^ { 2 } } \right) }
$$

Limiting values are what you’d expect for cdf’s named “ $P$ ” and “ $Q$ ”:

$$
\begin{array} { r l } { P _ { K S } ( 0 ) = 0 \qquad } & { { } P _ { K S } ( \infty ) = 1 } \\ { Q _ { K S } ( 0 ) = 1 \qquad } & { { } Q _ { K S } ( \infty ) = 0 } \end{array}
$$

Both of the series (6.14.56) and (6.14.57) are convergent for all $z > 0$ . Moreover, for any $Z$ , one or the other series converges extremely rapidly, requiring no more than three terms to get to IEEE double precision fractional accuracy. A good place to switch from one series to the other is at $z \approx 1 . 1 8$ . This renders the KS functions computable by a single exponential and a small number of arithmetic operations (see code below).

Getting the inverse functions $P _ { K S } ^ { - 1 } ( P )$ and $Q _ { K S } ^ { - 1 } ( \boldsymbol { Q } )$ , which return a value of $Z$ from a $P$ or $Q$ value, is a little trickier. For $Q \lesssim 0 . 3$ (that is, $P \gtrsim 0 . 7 $ ), an iteration based on (6.14.56) works nicely:

$$
\begin{array} { c } { { x _ { 0 } \equiv 0 } } \\ { { x _ { i + 1 } = \frac 1 2 Q + x _ { i } ^ { 4 } - x _ { i } ^ { 9 } + x _ { i } ^ { 1 6 } - x _ { i } ^ { 2 5 } + \cdots } } \\ { { z ( Q ) = \sqrt { - \frac 1 2 \log ( x _ { \infty } ) } } } \end{array}
$$

For $x \lesssim 0 . 0 6$ you only need the first two powers of $x _ { i }$

For larger values of $Q$ , that is, $P \ \lesssim \ 0 . 7$ , the number of powers of $x$ required quickly becomes excessive. A useful approach is to write (6.14.57) as

$$
\begin{array} { l } { { y \log ( y ) = - \displaystyle \frac { \pi P ^ { 2 } } { 8 } \left( 1 + y ^ { 4 } + y ^ { 1 2 } + \cdots + y ^ { 2 j ( j - 1 ) } + \cdots \right) ^ { - 1 } } } \\ { { z ( P ) = \displaystyle \frac { \pi / 2 } { \sqrt { - \log ( y ) } } } } \end{array}
$$

If we can get a good enough initial guess for $y$ , we can solve the first equation in (6.14.60) by a variant of Halley’s method: Use values of $y$ from the previous iteration on the right-hand side of (6.14.60), and use Halley only for the $y \log ( y )$ piece, so that the first and second derivatives are analytically simple functions.

A good initial guess is obtained by using the inverse function to $y \log ( y )$ (the function invxlogx in $\ S 6 . 1 1 \ r ,$ ) with the argument $- \pi P ^ { 2 } / 8$ . The number of iterations within the invxlogx function and the Halley loop is never more than half a dozen in each, often less. Code for the KS functions and their inverses follows.

struct KSdist {   
Kolmogorov-Smirnov cumulative distribution functions and their inverses. Doub pks(Doub z) { Return cumulative distribution function. if $( z \ < \ 0 .$ ) throw("bad z in KSdist"); if $\ _ { Z } \ = = \ 0 .$ ) return 0.; if $\mathit { \Theta } _ { \Xi } < 1 . 1 8 $ ) { Doub y $=$ exp(-1.23370055013616983/SQR(z)); return 2.25675833419102515\*sqrt(-log(y)) \*(y + pow(y,9) + pow(y,25) $^ +$ pow(y,49)); } else { Doub x $=$ exp(-2.\*SQR(z)); return 1. - 2.\*(x - pow(x,4) $^ +$ pow(x,9)); } } Doub qks(Doub z) { Return complementary cumulative distribution function. if $\ . \ z \ < \ 0 .$ ) throw("bad z in KSdist"); if $\ , z \ = \ 0 .$ ) return 1.; if ( $z \ < \ 1 . 1 8 ,$ ) return 1.-pks(z); Doub $\mathbf { x } \ = \ \exp ( - 2 . { * } \mathrm { S } \mathsf { q } \mathrm { R } ( \mathbf { z } ) )$ ; return ${ 2 . * ( { \bf x } \mathrm { ~ - ~ } \mathrm { p o w } ( { \bf x } , 4 ) \mathrm { ~ + ~ } \mathrm { p o w } ( { \bf x } , 9 ) ) } ;$ Doub invqks(Doub q) {

Return inverse of the complementary cumulative distribution function.

Doub y,logy,yp,x,xp,f,ff,u,t; if (q $\scriptstyle < = 0$ . $| \textsf { l q } > \textsf { 1 } .$ ) throw("bad q in KSdist"); if $( { \mathsf { q } } \ ) = = \ { \mathsf { 1 } } .$ ) return 0.; if $( \mathsf { q } > 0 . 3 )$ ) { $\texttt { f } = \texttt { - } 0$ .392699081698724155\*SQR(1.-q); $\mathrm { ~ y ~ } =$ invxlogx(f); Initial guess. do { $\mathrm { \ y p ~ = ~ y _ { \mathrm { ~ } } }$ ; logy $=$ log(y); ff $=$ f/SQR(1.+ pow(y,4)+ pow(y,12)); $u \ =$ (y\*logy-ff)/(1.+logy); Newton’s method correction. $\mathrm { ~ y ~ } = \mathrm { ~ y ~ } -$ ( $t = u$ /MAX(0.5,1.-0.5\*u/(y\*(1.+logy)))); Halley. } while (abs(t/y)>1.e-15); return 1.57079632679489662/sqrt(-log(y)); } else { $\mathrm { ~ x ~ } = \mathrm { ~ 0 ~ } . 0 3$ ; do { Iteration (6.14.59). $\mathbf { x p } \ = \ \mathbf { x } _ { \mathrm { ~ \scriptsize ~ . ~ } }$ ; x = 0.5\*q+pow(x,4)-pow(x,9); if $\mathrm { ~ ( ~ x ~ } > \ 0 . 0 6 )$ x $+ =$ pow(x,16)-pow(x,25); } while (abs((xp-x)/x)>1.e-15); return sqrt(-0.5\*log(x)); } } Doub invpks(Doub p) {return invqks(1.-p);} Return inverse of the cumulative distribution function.

# 6.14.13 Poisson Distribution

The eponymous Poisson distribution was derived by Poisson in 1837. It applies to a process where discrete, uncorrelated events occur at some mean rate per unit time. If, for a given period, $\lambda$ is the mean expected number of events, then the probability distribution of seeing exactly $k$ events, $k \geq 0$ , can be written as

$$
\begin{array} { c c } { { k \sim \mathrm { P o i s s o n } ( \lambda ) , } } & { { \lambda > 0 } } \\ { { p ( k ) = \displaystyle \frac { 1 } { k ! } \lambda ^ { k } e ^ { - \lambda } , } } & { { \ k = 0 , 1 , . . . } } \end{array}
$$

Evidently $\begin{array} { r } { \sum _ { k } p ( k ) = 1 } \end{array}$ , since the $k$ -dependent factors in (6.14.61) are just the series expansion of $e ^ { \lambda }$ .

The mean and variance of Poisson $( \lambda )$ are both $\lambda$ . There is a single mode at $k = \lfloor \lambda \rfloor$ , that is, at $\lambda$ rounded down to an integer.

The Poisson distribution’s cdf is an incomplete gamma function $Q ( a , x )$ ,

$$
P _ { \lambda } ( < k ) = Q ( k , \lambda )
$$

Since $k$ is discrete, $P _ { \lambda } ( < k )$ is of course different from $P _ { \lambda } ( \leq k )$ , the latter being given by

$$
P _ { \lambda } ( \leq k ) = Q ( k + 1 , \lambda )
$$

Some particular values are

$$
P _ { \lambda } ( < 0 ) = 0 \qquad P _ { \lambda } ( < 1 ) = e ^ { - \lambda } \qquad P _ { \lambda } ( < \infty ) = 1
$$

Some other relations involving the incomplete gamma functions $Q ( \boldsymbol { a } , \boldsymbol { x } )$ and $P ( \boldsymbol { a } , \boldsymbol { x } )$ are

$$
\begin{array} { r l } & { P _ { \lambda } ( \geq k ) = P ( k , \lambda ) = 1 - Q ( k , \lambda ) } \\ & { P _ { \lambda } ( > k ) = P ( k + 1 , \lambda ) = 1 - Q ( k + 1 , \lambda ) } \end{array}
$$

Because of the discreteness in $k$ , the inverse of the cdf must be defined with some care: Given a value P, we define $k _ { \lambda } ( P )$ as the integer such that

$$
P _ { \lambda } ( < k ) \le P < P _ { \lambda } ( \le k )
$$

In the interest of conciseness, the code below cheats a little bit and allows the righthand $<$ to be $\leq$ . If you may be supplying $P$ ’s that are exact $P _ { \lambda } ( < k )$ ’s, then you will need to check both $k _ { \lambda } ( P )$ as returned, and $k _ { \lambda } ( P ) + 1$ . (This will essentially never happen for “round” $P$ ’s like 0.95, 0.99, etc.)

# struct Poissondist : Gamma {

oisson distribution, derived from the gamma function Gamma. Doub lam; Poissondist(Doub llam) : lam(llam) { Constructor. Initialize with . if (lam $< = ~ 0 .$ ) throw("bad lam in Poissondist"); } Doub $\mathfrak { p } ( \mathtt { I n t } \ \mathtt { n } )$ { Return probability density function. if $\smash { \left( \mathrm { ~ n ~ } < \mathrm { ~ } 0 \right) }$ ) throw("bad n in Poissondist"); return exp(-lam + n\*log(lam) - gammln(n+1.)); } Doub cdf(Int n) { Return cumulative distribution function. if $\mathrm { ~ ( ~ n ~ < ~ } 0 \mathrm { ) ~ }$ ) throw("bad n in Poissondist"); if ( $\mathbf { \bar { n } _ { \theta } } = \mathbf { \bar { \Phi } } 0$ ) return 0.; return gammq((Doub)n,lam); }

# Int invcdf(Doub p) {

# Given argument $P$ , return integer $_ n$ such that $P ( < n ) \leq P \leq P ( < n + 1 )$

Int n,nl,nu, $\mathtt { i n c } = 1$ ; if (p $< = ~ 0$ . | $| \mathrm { ~  ~ p ~ } > = 1 .$ ) throw("bad p in Poissondist"); if (p $<$ exp(-lam)) return 0; $\mathrm { ~ n ~ } =$ (Int)MAX(sqrt(lam),5.); Starting guess near peak of density. if $( \mathtt { p } <$ cdf(n)) { Expand interval until we bracket. do { $\mathrm { ~ n ~ } =$ MAX(n-inc,0); inc $\ast = ~ 2$ ; } while (p < cdf(n)); nl $= \mathrm { ~ n ~ }$ ; nu $\mathbf { \Sigma } = \texttt { n } +$ inc/2; } else { do { n $+ =$ inc; inc $\ast = ~ 2$ ; } while (p > cdf(n)); nu $= \mathrm { ~ n ~ }$ ; $\mathtt { n 1 } = \mathtt { n }$ - inc/2; } while (nu-nl>1) { Now contract the interval by bisection. $\mathrm { ~ n ~ } = \mathrm { ~ \left( n 1 + n u \right) / 2 ~ }$ ; if $. { \mathrm { ~ p ~ } } <$ cdf $\mathbf { \Psi } ( \mathbf { n } )$ ) $\mathrm { \Omega } \mathfrak { n } \mathfrak { u } \ = \mathrm { \Omega } \mathfrak { n }$ ; else nl $\mathbf { \Phi } = \mathbf { \Phi } _ { \mathbf { n } }$ ; } return nl; }

# 6.14.14 Binomial Distribution

Like the Poisson distribution, the binomial distribution is a discrete distribution over $k \geq 0$ . It has two parameters, $n \geq 1$ , the “sample size” or maximum value for which $k$ can be nonzero; and $p$ , the “event probability” (not to be confused with $p ( k )$ , the probability of a particular $\mathrm { k }$ ). We write

$$
\begin{array} { r l } { k \sim \mathrm { B i n o m i a l } ( n , p ) , \ } & { { } n \geq 1 , \ 0 < p < 1 } \\ { p ( k ) = { \binom { n } { k } } p ^ { k } ( 1 - p ) ^ { n - k } , \ } & { { } k = 0 , 1 , \ldots , n } \end{array}
$$

where $\binom { n } { k }$ is, of course, the binomial coefficient.

The mean and variance are given by

$$
\begin{array} { l } { { \mathrm { M e a n } \{ { \mathrm { B i n o m i a l } } ( n , p ) \} = n p } \atop { \mathrm { V a r } \{ { \mathrm { B i n o m i a l } } ( n , p ) \} = n p ( 1 - p ) } } \end{array}
$$

There is a single mode at the value $k$ that satisfies

$$
( n + 1 ) p - 1 < k \leq ( n + 1 ) p
$$

The distribution is symmetrical iff $\begin{array} { r } { p = \frac { 1 } { 2 } } \end{array}$ . Otherwise it has positive skewness for $\begin{array} { r } { p < { \frac { 1 } { 2 } } } \end{array}$ and negative for $\begin{array} { r } { p > \frac { 1 } { 2 } } \end{array}$ . Many additional properties are described in [2].

The Poisson distribution is obtained from the binomial distribution in the limit $n  \infty , p  0$ with the $n p$ remaining finite. More precisely,

$$
\operatorname* { l i m } _ { n \to \infty } \operatorname { B i n o m i a l } ( n , \lambda / n ) \cong \operatorname { P o i s s o n } ( \lambda )
$$

The binomial distribution’s cdf can be computed from the incomplete beta function $I _ { x } ( a , b )$ ,

$$
P ( < k ) = 1 - I _ { p } ( k , n - k + 1 )
$$

so we also have (analogously to the Poisson distribution)

$$
\begin{array} { l } { P ( \leq k ) = 1 - I _ { p } ( k + 1 , n - k ) } \\ { P ( > k ) = I _ { p } ( k + 1 , n - k ) } \\ { P ( \geq k ) = I _ { p } ( k , n - k + 1 ) } \end{array}
$$

Some particular values are

$$
P ( < 0 ) = 0 \qquad P ( < [ n + 1 ] ) = 1
$$

The inverse cdf is defined exactly as for the Poisson distribution, above, and with the same small warning about the code.

# struct Binomialdist : Beta {

Binomial distribution, derived from the beta function Beta.

Int n;   
Doub pe, fac;   
Binomialdist(Int nn, Doub ppe) : n(nn), pe(ppe) {   
Constructor. Initialize with $_ { n }$ (sample size) and $p$ (event probability). if $( \mathtt { n ~ < = ~ 0 ~ } \mid \mid \mathtt { p e ~ < = ~ 0 ~ . ~ } \mid \mid \mathtt { p e ~ > = ~ 1 . ~ } )$ throw("bad args in Binomialdist");

fac $=$ gammln(n+1.); 1 Doub p(Int k) { Return probability density function. if (k < 0) throw("bad k in Binomialdist"); if $\mathrm { ~ ( ~ k ~ > ~ n ~ ) ~ }$ ) return 0.; return exp(k\*log(pe)+(n-k)\*log(1.-pe) +fac-gammln(k+1.)-gammln(n-k+1.)); } Doub cdf(Int k) { Return cumulative distribution function. if (k < 0) throw("bad k in Binomialdist"); if $\mathbf { \Phi } _ { \mathbf { k } } \ \mathbf { \Phi } = \mathbf { \Phi } _ { 0 }$ ) return 0.; if $\mathrm { ~ ( ~ k ~ > ~ n ~ ) ~ }$ ) return 1.; return 1. - betai((Doub)k,n-k+1.,pe); } Int invcdf(Doub p) { Given argument $P$ , return integer $_ n$ such that $P ( < n ) \leq P \leq P ( < n + 1 )$ . Int k,kl,ku, $\mathtt { i n c } = 1$ ; if (p $\scriptstyle < = \ 0$ . || $\mathrm { ~ p ~ } > = \mathrm { ~ 1 ~ . ~ }$ ) throw("bad p in Binomialdist"); $\mathrm { ~ \bf ~ k ~ } =$ MAX(0,MIN(n,(Int)(n\*pe))); Starting guess near peak of density. if $\cdot \mathtt { p } <$ cdf(k)) { Expand interval until we bracket. do { $\mathrm { ~ \bf ~ k ~ } =$ MAX(k-inc,0); inc $\ast = ~ 2$ ; } while $( \mathtt { p } \ <$ cdf(k)); $\mathbf { k } 1 \ = \ \mathbf { k } ;$ $\mathtt { k u \textbf { = k } + }$ inc/2; } else { do { ${ \bf k } \ = \ { \tt M I N } \left( { \tt k } { + } \mathrm { i n c } \ , \mathrm { n } { + } 1 \right) ;$ inc $\ast = ~ 2$ ; } while (p > cdf(k)); ku $\mathbf { \lambda } = \mathbf { \lambda } _ { \mathbf { k } } ;$ ; $\mathrm { ~ k ~ 1 ~ } = \mathrm { ~ k ~ }$ - inc/2; } while (ku-kl>1) { Now contract the interval by bisectio $k ~ = ~ \left( \mathrm { k } \mathrm { 1 } \mathrm { + } \mathrm { k } \mathrm { u } \right) / 2$ ; if $\mathrm { ~ ( ~ p ~ < ~ }$ cdf $\mathbf { \Psi } ( \mathbf { k } )$ ) $\mathtt { k u } \ = \ \mathtt { k }$ ; else $\mathrm { ~ \ k ~ } ] \ = \ \mathrm { ~ k ~ }$ ; } return kl; }

# CITED REFERENCES AND FURTHER READING:

Johnson, N.L. and Kotz, S. 1970, Continuous Univariate Distributions, 2 vols. (Boston: Houghton Mifflin).[1]   
Johnson, N.L. and Kotz, S. 1969, Discrete Distributions (Boston: Houghton Mifflin).[2]   
Gelman, A., Carlin, J.B., Stern, H.S., and Rubin, D.B. 2003, Bayesian Data Analysis, 2nd ed. (Boca Raton, FL: Chapman & Hall/CRC), Appendix A.   
Lyuu, Y-D. 2002, Financial Engineering and Computation (Cambridge, UK: Cambridge University Press).[3]

# 7.0 Introduction

It may seem perverse to use a computer, that most precise and deterministic of all machines conceived by the human mind, to produce “random” numbers. More than perverse, it may seem to be a conceptual impossibility. After all, any program produces output that is entirely predictable, hence not truly “random.”

Nevertheless, practical computer “random number generators” are in common use. We will leave it to philosophers of the computer age to resolve the paradox in a deep way (see, e.g., Knuth [1] $\ S 3 . 5$ for discussion and references). One sometimes hears computer-generated sequences termed pseudo-random, while the word random is reserved for the output of an intrinsically random physical process, like the elapsed time between clicks of a Geiger counter placed next to a sample of some radioactive element. We will not try to make such fine distinctions.

A working definition of randomness in the context of computer-generated sequences is to say that the deterministic program that produces a random sequence should be different from, and — in all measurable respects — statistically uncorrelated with, the computer program that uses its output. In other words, any two different random number generators ought to produce statistically the same results when coupled to your particular applications program. If they don’t, then at least one of them is not (from your point of view) a good generator.

The above definition may seem circular, comparing, as it does, one generator to another. However, there exists a large body of random number generators that mutually do satisfy the definition over a very, very broad class of applications programs. And it is also found empirically that statistically identical results are obtained from random numbers produced by physical processes. So, because such generators are known to exist, we can leave to the philosophers the problem of defining them.

The pragmatic point of view is thus that randomness is in the eye of the beholder (or programmer). What is random enough for one application may not be random enough for another. Still, one is not entirely adrift in a sea of incommensurable applications programs: There is an accepted list of statistical tests, some sensible and some merely enshrined by history, that on the whole do a very good job of ferreting out any nonrandomness that is likely to be detected by an applications program (in this case, yours). Good random number generators ought to pass all of these tests, or at least the user had better be aware of any that they fail, so that he or she will be able to judge whether they are relevant to the case at hand.

For references on this subject, the one to turn to first is Knuth [1]. Be cautious about any source earlier than about 1995, since the field progressed enormously in the following decade.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley),Chapter 3,especially $\ S 3 . 5 . [ 1 ]$

Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer).

# 7.1 Uniform Deviates

Uniform deviates are just random numbers that lie within a specified range, typically 0.0 to 1.0 for floating-point numbers, or 0 to $2 ^ { 3 2 } - 1$ or $2 ^ { 6 4 } - 1$ for integers. Within the range, any one number is just as likely as any other. They are, in other words, what you probably think “random numbers” are. However, we want to distinguish uniform deviates from other sorts of random numbers, for example, numbers drawn from a normal (Gaussian) distribution of specified mean and standard deviation. These other sorts of deviates are almost always generated by performing appropriate operations on one or more uniform deviates, as we will see in subsequent sections. So, a reliable source of random uniform deviates, the subject of this section, is an essential building block for any sort of stochastic modeling or Monte Carlo computer work.

The state of the art for generating uniform deviates has advanced considerably in the last decade and now begins to resemble a mature field. It is now reasonable to expect to get “perfect” deviates in no more than a dozen or so arithmetic or logical operations per deviate, and fast, “good enough” deviates in many fewer operations than that. Three factors have all contributed to the field’s advance: first, new mathematical algorithms; second, better understanding of the practical pitfalls; and, third, standardization of programming languages in general, and of integer arithmetic in particular — and especially the universal availability of unsigned 64-bit arithmetic in C and $\mathrm { C } { + } { + }$ . It may seem ironic that something as down-in-the-weeds as this last factor can be so important. But, as we will see, it really is.

The greatest lurking danger for a user today is that many out-of-date and inferior methods remain in general use. Here are some traps to watch for:

- Never use a generator principally based on a linear congruential generator (LCG) or a multiplicative linear congruential generator (MLCG). We say more about this below.   
Never use a generator with a period less than $\sim 2 ^ { 6 4 } \approx 2 \times 1 0 ^ { 1 9 }$ , or any generator whose period is undisclosed. Never use a generator that warns against using its low-order bits as being completely random. That was good advice once, but it now indicates an obsolete algorithm (usually a LCG).

- Never use the built-in generators in the C and $\mathrm { C } { + } { + }$ languages, especially rand and srand. These have no standard implementation and are often badly flawed.

If all scientific papers whose results are in doubt because of one or more of the above traps were to disappear from library shelves, there would be a gap on each shelf about as big as your fist.

You may also want to watch for indications that a generator is overengineered, and therefore wasteful of resources:

- Avoid generators that take more than (say) two dozen arithmetic or logical operations to generate a 64-bit integer or double precision floating result. - Avoid using generators (over-)designed for serious cryptographic use. - Avoid using generators with period $> 1 0 ^ { 1 0 0 }$ . You really will never need it, and, above some minimum bound, the period of a generator has little to do with its quality.

Since we have told you what to avoid from the past, we should immediately follow with the received wisdom of the present:

An acceptable random generator must combine at least two (ideally, unrelated) methods. The methods combined should evolve independently and share no state. The combination should be by simple operations that do not produce results less random than their operands.

If you don’t want to read the rest of this section, then use the following code to generate all the uniform deviates you’ll ever need. This is our suspenders-and-belt, full-body-armor, never-any-doubt generator; and, it also meets the above guidelines for avoiding wasteful, overengineered methods. (The fastest generators that we recommend, below, are only ${ \sim } 2 . 5 \times$ faster, even when their code is copied inline into an application.)

# ran.h struct Ran {

Implementation of the highest quality recommended generator. The constructor is called with an integer seed and creates an instance of the generator. The member functions int64, doub, and int32 return the next values in the random sequence, as a variable type indicated by their names. The period of the generator is 	 3:138  1057.

Ullong u,v,w;   
Ran(Ullong j) : v(4101842887655102017LL), w(1) {   
Constructor. Call with any integer seed (except value of $\mathtt { v }$ above). $\mathrm { ~ u ~ } = \mathrm { ~ j ~ }$ ^ v; int64(); $\mathrm { ~ v ~ } = \mathrm { ~ u ~ }$ ; int64(); $\texttt { w } = \texttt { v }$ ; int64();   
}   
inline Ullong int64() {   
Return 64-bit random integer. See text for explanation of method. $\texttt { u } = \texttt { u } *$ 2862933555777941757LL $^ +$ 7046029254386353087LL; $\texttt { V } \hat { } = \texttt { V } > > \texttt { 1 7 }$ ; $\texttt { V } \hat { } = \texttt { V } < < \texttt { 3 1 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 8 }$ ; $\kappa =$ 4294957665U\*(w & 0xffffffff) $^ +$ $\left( \mathrm { ~ w ~ } > > \ 3 2 \right)$ ; Ullong $\texttt { x } = \texttt { u } \hat { }$ ( $\mathbf { \chi } _ { \mathrm { ~ u ~ } } < < \mathbf { \chi } _ { 2 1 } )$ ; $\texttt { x } \hat { } = \texttt { x } > > 3 5$ ; $\mathrm { ~  ~ x ~ } \hat { \mathrm { ~  ~ \mu ~ } } = \mathrm { ~  ~ x ~ } < < \mathrm { ~  ~ 4 ~ } _ { \mathrm { i } }$ ; return $( { \texttt { x } } + { \texttt { v } } ) \ { \hat { } } \sim { \ } _ { \texttt { w } }$ ;   
inline Doub doub() { return 5.42101086242752217E-20 $^ *$ int64(); }   
Return random double-precision floating value in the range 0. to 1.   
inline Uint int32() { return (Uint)int64(); }   
Return 32-bit random integer.

# };

The basic premise here is that a random generator, because it maintains internal state between calls, should be an object, a struct. You can declare more than one instance of it (although it is hard to think of a reason for doing so), and different instances will in no way interact.

The constructor Ran() takes a single integer argument, which becomes the seed for the sequence generated. Different seeds generate (for all practical purposes) completely different sequences. Once constructed, an instance of Ran offers several different formats for random output. To be specific, suppose you have created an instance by the declaration

# Ran myran(17);

where myran is now the name of this instance, and 17 is its seed. Then, the function myran.int64() returns a random 64-bit unsigned integer; the function myran.int32() returns an unsigned 32-bit integer; and the function myran.doub() returns a double-precision floating value in the range 0:0 to 1:0. You can intermix calls to these functions as you wish. You can use any returned random bits for any purpose. If you need a random integer between 1 and n (inclusive), say, then the expression $1 ~ +$ myran.int64() $\%$ $\left( \mathtt { n } \mathrm { - } 1 \right)$ is perfectly OK (though there are faster idioms than the use of $\%$ ).

In the rest of this section, we briefly review some history (the rise and fall of the LCG), then give details on some of the algorithmic methods that go into a good generator, and on how to combine those methods. Finally, we will give some further recommended generators, additional to Ran above.

# 7.1.1 Some History

With hindsight, it seems clear that the whole field of random number generation was mesmerized, for far too long, by the simple recurrence equation

$$
I _ { j + 1 } = a I _ { j } + c { \pmod { m } }
$$

Here $m$ is called the modulus, $a$ is a positive integer called the multiplier, and $c$ (which may be zero) is nonnegative integer called the increment. For $c \neq 0$ , equation (7.1.1) is called a linear congruential generator (LCG). When $c = 0$ , it is sometimes called a multiplicative LCG or MLCG.

The recurrence (7.1.1) must eventually repeat itself, with a period that is obviously no greater than $m$ . If $m , a$ ; and $c$ are properly chosen, then the period will be of maximal length, i.e., of length $m$ . In that case, all possible integers between 0 and $m - 1$ occur at some point, so any initial “seed” choice of $I _ { 0 }$ is as good as any other:

The sequence just takes off from that point, and successive values $I _ { j }$ are the returned “random” values.

The idea of LCGs goes back to the dawn of computing, and they were widely used in the 1950s and thereafter. The trouble in paradise first began to be noticed in the mid-1960s (e.g., [1]): If $k$ random numbers at a time are used to plot points in $k$ -dimensional space (with each coordinate between 0 and 1), then the points will not tend to “fill up” the $k$ -dimensional space, but rather will lie on $( k - 1 )$ -dimensional “planes.” There will be at most about $m ^ { 1 / k }$ such planes. If the constants $m$ and $a$ are not very carefully chosen, there will be many fewer than that. The number $m$ was usually close to the machine’s largest representable integer, often $\sim 2 ^ { 3 2 }$ . So, for example, the number of planes on which triples of points lie in three-dimensional space can be no greater than about the cube root of $2 ^ { 3 2 }$ , about 1600. You might well be focusing attention on a physical process that occurs in a small fraction of the total volume, so that the discreteness of the planes can be very pronounced.

Even worse, many early generators happened to make particularly bad choices for $m$ and $a$ . One infamous such routine, RANDU, with $a \ : = \ : 6 5 5 3 9$ and $m = 2 ^ { 3 1 }$ , was widespread on IBM mainframe computers for many years, and widely copied onto other systems. One of us recalls as a graduate student producing a “random” plot with only 11 planes and being told by his computer center’s programming consultant that he had misused the random number generator: “We guarantee that each number is random individually, but we don’t guarantee that more than one of them is random.” That set back our graduate education by at least a year!

LCGs and MLCGs have additional weaknesses: When m is chosen as a power of 2 (e.g., RANDU), then the low-order bits generated are hardly random at all. In particular, the least significant bit has a period of at most 2, the second at most 4, the third at most 8, and so on. But, if you don’t choose m as a power of 2 (in fact, choosing $m$ prime is generally a good thing), then you generally need access to double-length registers to do the multiplication and modulo functions in equation (7.1.1). These were often unavailable in computers of the time (and usually still are).

A lot of effort subsequently went into “fixing” these weaknesses. An elegant number-theoretical test of $m$ and $a$ , the spectral test, was developed to characterize the density of planes in arbitrary dimensional space. (See [2] for a recent review that includes graphical renderings of some of the appallingly poor generators that were used historically, and also [3].) Schrage’s method [4] was invented to do the multiplication $a I _ { j }$ with only 32-bit arithmetic for $m$ as large as $2 ^ { 3 2 } - 1$ , but, unfortunately, only for certain $a$ ’s, not always the best ones. The review by Park and Miller [5] gives a good contemporary picture of LCGs in their heyday.

Looking back, it seems clear that the field’s long preoccupation with LCGs was somewhat misguided. There is no technological reason that the better, non-LCG, generators of the last decade could not have been discovered decades earlier, nor any reason that the impossible dream of an elegant “single algorithm” generator could not also have been abandoned much earlier (in favor of the more pragmatic patchwork in combined generators). As we will explain below, LCGs and MLCGs can still be useful, but only in carefully controlled situations, and with due attention to their manifest weaknesses.

# 7.1.2 Recommended Methods for Use in Combined Generators

Today, there are at least a dozen plausible algorithms that deserve serious consideration for use in random generators. Our selection of a few is motivated by aesthetics as much as mathematics. We like algorithms with few and fast operations, with foolproof initialization, and with state small enough to keep in registers or firstlevel cache (if the compiler and hardware are able to do so). This means that we tend to avoid otherwise fine algorithms whose state is an array of some length, despite the relative simplicity with which such algorithms can achieve truly humongous periods. For overviews of broader sets of methods, see [6] and [7].

To be recommendable for use in a combined generator, we require a method to be understood theoretically to some degree, and to pass a reasonably broad suite of empirical tests (or, if it fails, have weaknesses that are well characterized). Our minimal theoretical standard is that the period, the set of returned values, and the set of valid initializations should be completely understood. As a minimal empirical standard, we have used the second release (2003) of Marsaglia’s whimsically named Diehard battery of statistical tests [8]. An alternative test suite, NIST-STS [9], might be used instead, or in addition.

Simply requiring a combined generator to pass Diehard or NIST-STS is not an acceptably stringent test. These suites make only ${ \sim } 1 0 ^ { 7 }$ calls to the generator, whereas a user program might make $1 0 ^ { 1 2 }$ or more. Much more meaningful is to require that each method in a combined generator separately pass the chosen suite. Then the combination generator (if correctly constructed) should be vastly better than any one component. In the tables below, we use the symbol “¾” to indicate that a method passes the Diehard tests by itself. (For 64-bit quantities, the statement is that the 32 high and low bits each pass.) Correspondingly, the words “can be used as random,” below, do not imply perfect randomness, but only a minimum level for quick-and-dirty applications where a better, combined, generator is just not needed.

We turn now to specific methods, starting with methods that use 64-bit unsigned arithmetic (what we call Ullong, that is, unsigned long long in the Linux/Unix world, or unsigned __int64 on planet Microsoft).

(A) 64-bit Xorshift Method. This generator was discovered and characterized by Marsaglia [10]. In just three XORs and three shifts (generally fast operations) it produces a full period of $2 ^ { 6 4 } - 1$ on 64 bits. (The missing value is zero, which perpetuates itself and must be avoided.) High and low bits pass Diehard. A generator can use either the three-line update rule, below, that starts with $< <$ , or the rule that starts with $> >$ . (The two update rules produce different sequences, related by bit reversal.)

$$
\begin{array} { r l } { \mathrm { s t a t e : ~ } } & { x ( \mathrm { u n s i g n e d ~ 6 4 - b i t } ) } \\ { \mathrm { i n i t i a l i z e : ~ } } & { x \neq 0 } \\ { \mathrm { u p d a t e : ~ } } & { x \gets x \wedge ( x \ > \ \circ \ \mathfrak { a } _ { 1 } ) , } \\ & { x \gets x \wedge ( x \ \ll \ \mathfrak { a } _ { 2 } ) , } \\ & { x \gets x \wedge ( x \ > \ \circ \ \mathfrak { a } _ { 3 } ) ; } \\ { \mathrm { o r ~ } } & { x \gets x \wedge ( x \ \ll \ \mathfrak { a } _ { 1 } ) , } \\ & { x \gets x \wedge ( x \ > \ \mathfrak { a } _ { 2 } ) , } \end{array}
$$

x x ^ .x << a3/I can use as random: x (all bits) ¾ can use in bit mix: x (all bits) can improve by: output 64-bit MLCG successor period: $2 ^ { 6 4 } - 1$

Here is a very brief outline of the theory behind these generators: Consider the 64 bits of the integer as components in a vector of length 64, in a linear space where addition and multiplication are done modulo 2. Noting that XOR $( \wedge )$ is the same as addition, each of the three lines in the updating can be written as the action of a $6 4 \times$ 64 matrix on a vector, where the matrix is all zeros except for ones on the diagonal, and on exactly one super- or subdiagonal (corresponding to $< <$ or $> >$ ). Denote this matrix as $\mathbf { S } _ { k }$ , where $k$ is the shift argument (positive for left-shift, say, and negative for right-shift). Then, one full step of updating (three lines of the updating rule, above) corresponds to multiplication by the matrix $\mathbf { T } \equiv \mathbf { S } _ { k _ { 3 } } \mathbf { S } _ { k _ { 2 } } \mathbf { S } _ { k _ { 1 } }$ .

One next needs to find triples of integers $( k _ { 1 } , k _ { 2 } , k _ { 3 } )$ , for example $( 2 1 , - 3 5 , 4 )$ , that give the full $M \equiv 2 ^ { 6 4 } - 1$ period. Necessary and sufficient conditions are that ${ \bf { \bar { T } } } ^ { M } = { \bf { 1 } }$ (the identity matrix) and that $\mathbf T ^ { N } \neq \mathbf { \bar { 1 } }$ for these seven values of $N$ : $M / 6 7 0 0 4 1 7$ , M=65537, $M / 6 4 1$ , M=257, M=17, $M / 5$ , and $M / 3$ , that is, $M$ divided by each of its seven distinct prime factors. The required large powers of $\mathbf { T }$ are readily computed by successive squarings, requiring only on the order of $6 4 ^ { 4 }$ operations. With this machinery, one can find full-period triples $( k _ { 1 } , k _ { 2 } , k _ { 3 } )$ by exhaustive search, at a reasonable cost.

Brent [11] has pointed out that the 64-bit xorshift method produces, at each bit position, a sequence of bits that is identical to one produced by a certain linear feedback shift register (LFSR) on 64 bits. (We will learn more about LFSRs in $\ S 7 . 5 . )$ The xorshift method thus potentially has some of the same strengths and weaknesses as an LFSR. Mitigating this, however, is the fact that the primitive polynomial equivalent of a typical xorshift generator has many nonzero terms, giving it better statistical properties than LFSR generators based, for example, on primitive trinomials. In effect, the xorshift generator is a way to step simultaneously 64 nontrivial onebit LFSR registers, using only six fast, 64-bit operations. There are other ways of making fast steps on LFSRs, and combining the output of more than one such generator [12,13], but none as simple as the xorshift method.

While each bit position in an xorshift generator has the same recurrence, and therefore the same sequence with period $2 ^ { 6 4 } - 1$ , the method guarantees offsets to each sequence such that all nonzero 64-bit words are produced across the bit positions during one complete cycle (as we just saw).

A selection of full-period triples is tabulated in [10]. Only a small fraction of full-period triples actually produce generators that pass Diehard. Also, a triple may pass in its $< <$ -first version, and fail in its $> >$ -first version, or vice versa. Since the two versions produce simply bit-reversed sequences, a failure of either sense must obviously be considered a failure of both (and a weakness in Diehard). The following recommended parameter sets pass Diehard for both the $< <$ and $> >$ rules. The sets near the top of the list may be slightly superior to the sets near the bottom. The column labeled ID assigns an identification string to each recommended generator that we will refer to later.

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>a1</td><td rowspan=1 colspan=1>a2</td><td rowspan=1 colspan=1>a3</td></tr><tr><td rowspan=2 colspan=1>A1A2</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>35</td><td rowspan=2 colspan=1>45</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>41</td></tr><tr><td rowspan=1 colspan=1>A3</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>8</td></tr><tr><td rowspan=1 colspan=1>A4</td><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>14</td></tr><tr><td rowspan=1 colspan=1>A5</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>11</td></tr><tr><td rowspan=1 colspan=1>A6</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>A7</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>A8</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>43</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>A9</td><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>41</td><td rowspan=1 colspan=1>18</td></tr></table>

It is easy to design a test that the xorshift generator fails if used by itself. Each bit at step $i + 1$ depends on at most 8 bits of step $i$ , so some simple logical combinations of the two timesteps (and appropriate masks) will show immediate nonrandomness. Also, when the state passes though a value with only small numbers of 1 bits, as it must eventually do (so-called states of low Hamming weight), it will take longer than expected to recover. Nevertheless, used in combination, the xorshift generator is an exceptionally powerful and useful method. Much grief could have been avoided had it, instead of LCGs, been discovered in 1949!

(B) Multiply with Carry (MWC) with Base $\ b { b } = 2 ^ { 3 2 }$ . Also discovered by Marsaglia, the base $b$ of an MWC generator is most conveniently chosen to be a power of 2 that is half the available word length (i.e., $b = 3 2$ for 64-bit words). The MWC is then defined by its multiplier $a$ .

state: $x$ (unsigned 64-bit)   
initialize: $\begin{array} { r l } & { 1 \leq x \leq 2 ^ { 3 2 } - 1 } \\ & { x  a ( x \& [ 2 ^ { 3 2 } - 1 ] ) + ( x \gg 3 2 ) } \\ & { x ( \mathrm { l o w } 3 2 \mathrm { b i t s } ) \quad \ast } \\ & { x ( \mathrm { a l l } 6 4 \mathrm { b i t s } ) } \end{array}$   
update:   
can use as random:   
can use in bit mix:   
can improve by: output 64-bit xorshift successor to 64 bit $x$   
period: $( 2 ^ { 3 2 } a - 2 ) / 2$ (a prime)

An MWC generator with parameters $b$ and $a$ is related theoretically [14] to, though not identical to, an LCG with modulus $m = a b - 1$ and multiplier $a$ . It is easy to find values of $a$ that make $m$ a prime, so we get, in effect, the benefit of a prime modulus using only power-of-two modular arithmetic. It is not possible to choose $a$ to give the maximal period $m$ , but if $a$ is chosen to make both $m$ and $( m - 1 ) / 2$ prime, then the period of the MCG is $( m - 1 ) / 2$ , almost as good. A fraction of candidate $a$ ’s thus chosen passes the standard statistical test suites; a spectral test [14] is a promising development, but we have not made use of it here.

Although only the low $b$ bits of the state $x$ can be taken as algorithmically random, there is considerable randomness in all the bits of $x$ that represent the product $a b$ . This is very convenient in a combined generator, allowing the entire state $x$ to be used as a component. In fact, the first two recommended $a$ ’s below give $a b$ so close to $2 ^ { 6 4 }$ (within about $2 \mathrm { p p m } ,$ that the high bits of $x$ actually pass Diehard. (This is a good example of how any test suite can fail to find small amounts of highly nonrandom behavior, in this case as many as 8000 missing values in the top 32 bits.)

Apart from this kind of consideration, the values below are recommended with no particular ordering.

<table><tr><td>ID</td><td>a</td></tr><tr><td>B1</td><td>4294957665</td></tr><tr><td>B2</td><td>4294963023</td></tr><tr><td>B3</td><td>4162943475</td></tr><tr><td>B4</td><td>3947008974</td></tr><tr><td>B5</td><td>3874257210</td></tr><tr><td>B6</td><td>2936881968</td></tr><tr><td>B7</td><td>2811536238</td></tr><tr><td>B8</td><td>2654432763</td></tr><tr><td>B9</td><td>1640531364</td></tr></table>

(C) LCG Modulo $2 ^ { 6 4 }$ . Why in the world do we include this generator after vilifying it so thoroughly above? For the parameters given (which strongly pass the spectral test), its high 32 bits almost, but don’t quite, pass Diehard, and its low 32 bits are a complete disaster. Yet, as we will see when we discuss the construction of combined generators, there is still a niche for it to fill. The recommended multipliers $a$ below have good spectral characteristics [15].

state: $x$ (unsigned 64-bit)   
initialize: any value   
update: x ax C c .mod $2 ^ { 6 4 }$ /   
can use as random: $x$ (high 32 bits, with caution)   
can use in bit mix: $x$ (high 32 bits)   
can improve by: output 64-bit xorshift successor   
period: $2 ^ { 6 4 }$

<table><tr><td>ID</td><td>a</td><td>c (any odd value ok)</td></tr><tr><td>C1</td><td>3935559000370003845</td><td>2691343689449507681</td></tr><tr><td>C2</td><td>3202034522624059733</td><td>4354685564936845319</td></tr><tr><td>C3</td><td>2862933555777941757</td><td>7046029254386353087</td></tr></table>

(D) MLCG Modulo $2 ^ { 6 4 }$ . As for the preceding one, the useful role for this generator is strictly limited. The low bits are highly nonrandom. The recommended multipliers have good spectral characteristics (some from [15]).

state: $x$ (unsigned 64-bit)   
initialize: $x \neq 0$   
update: $x \gets a x$ .mod $2 ^ { 6 4 }$ /   
can use as random: $x$ (high 32 bits, with caution)   
can use in bit mix: $x$ (high 32 bits)   
can improve by: output 64-bit xorshift successor   
period: $2 ^ { 6 2 }$

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>a</td></tr><tr><td rowspan=2 colspan=1>D1D2</td><td rowspan=1 colspan=1>2685821657736338717</td></tr><tr><td rowspan=1 colspan=1>7664345821815920749</td></tr><tr><td rowspan=1 colspan=1>D3</td><td rowspan=1 colspan=1>4768777513237032717</td></tr><tr><td rowspan=1 colspan=1>D4</td><td rowspan=1 colspan=1>1181783497276652981</td></tr><tr><td rowspan=1 colspan=1>D5</td><td rowspan=1 colspan=1>702098784532940405</td></tr></table>

(E) MLCG with $m \gg 2 ^ { 3 2 }$ , $\mathbf { \nabla } m$ Prime. When 64-bit unsigned arithmetic is available, the MLCGs with prime moduli and large multipliers of good spectral character are decent 32-bit generators. Their main liability is that the 64-bit multiply and 64-bit remainder operations are quite expensive for the mere 32 (or so) bits of the result.

state: initialize: $\begin{array} { r l } & { x \mathrm { ~ ( u n s i g n e d ~ 6 4 - b i t ) } } \\ & { 1 \leq x \leq m - 1 } \\ & { x  a x \mathrm { ~ ( m o d ~ } m \mathrm { ) } } \\ & { x \quad ( 1 \leq x \leq m - 1 ) \mathrm { ~ o r ~ l o w ~ } 3 2 \mathrm { ~ b i t s ~ \quad ~ \ast ~ } } \\ & { \mathrm { ( s a m e ) } } \\ & { m - 1 } \end{array}$   
update:   
can use as random:   
can use in bit mix:   
period:

The parameter values below were kindly computed for us by P. L’Ecuyer. The multipliers are about the best that can be obtained for the prime moduli, close to powers of 2, shown. Although the recommended use is for only the low 32 bits (which all pass Diehard), you can see that (depending on the modulus) as many as 43 reasonably good bits can be obtained for the cost of the 64-bit multiply and remainder operations.

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>m</td><td rowspan=1 colspan=1>a</td></tr><tr><td rowspan=1 colspan=1>E1E2E3</td><td rowspan=1 colspan=1>239-7 = 549755813881</td><td rowspan=1 colspan=1>100141463050882325708129</td></tr><tr><td rowspan=1 colspan=1>E4E5E6</td><td rowspan=1 colspan=1>241-21 = 2199023255531</td><td rowspan=1 colspan=1>518378110707396639568</td></tr><tr><td rowspan=1 colspan=1>E7E8E9</td><td rowspan=1 colspan=1>242-11 = 4398046511093</td><td rowspan=1 colspan=1>178197821143071542852</td></tr><tr><td rowspan=1 colspan=1>E10E11E12</td><td rowspan=1 colspan=1>243-57 = 8796093022151</td><td rowspan=1 colspan=1>209625920521632006881</td></tr></table>

(F) MLCG with $m \gg 2 ^ { 3 2 }$ , $\pmb { m }$ Prime, and $a ( m - 1 ) \approx 2 ^ { 6 4 }$ . A variant, for use in combined generators, is to choose $m$ and $a$ to make $a ( m - 1 )$ as close as possible to $2 ^ { 6 4 }$ , while still requiring that $m$ be prime and that $a$ pass the spectral test. The purpose of this maneuver is to make $a x$ a 64-bit value with good randomness in its high bits, for use in combined generators. The expense of the multiply and remainder operations is still the big liability, however. The low 32 bits of $x$ are not significantly less random than those of the previous MLCG generators E1–E12.

state: $x$ (unsigned 64-bit)   
initialize: $1 \leq x \leq m - 1$   
update: $x \gets a x$ .mod m/   
can use as random: $x$ . $( 1 \leq x \leq m - 1 )$ or low 32 bits ¾   
can use in bit mix: $^ { a x }$ (but don’t use both $a x$ and $x$ ) ¾   
can improve by: output 64-bit xorshift successor of $^ { a x }$   
period: m  1

<table><tr><td>ID</td><td>m</td><td>a</td></tr><tr><td>F1</td><td>1148 × 232 + 11 = 4930622455819</td><td>3741260</td></tr><tr><td>F2</td><td>1264× 23² +9 = 5428838662153</td><td>3397916</td></tr><tr><td>F3</td><td>2039× 232 +3 = 8757438316547</td><td>2106408</td></tr></table>

# 7.1.3 How to Construct Combined Generators

While the construction of combined generators is an art, it should be informed by underlying mathematics. Rigorous theorems about combined generators are usually possible only when the generators being combined are algorithmically related; but that in itself is usually a bad thing to do, on the general principle of “don’t put all your eggs in one basket.” So, one is left with guidelines and rules of thumb.

The methods being combined should be independent of one another. They must share no state (although their initializations are allowed to derive from some convenient common seed). They should have different, incommensurate, periods. And, ideally, they should “look like” each other algorithmically as little as possible. This latter criterion is where some art necessarily enters.

The output of the combination generator should in no way perturb the independent evolution of the individual methods, nor should the operations effecting combination have any side effects.

The methods should be combined by binary operations whose output is no less random than one input if the other input is held fixed. For 32- or 64-bit unsigned arithmetic, this in practice means that only the $^ +$ and $\wedge$ operators can be used. As an example of a forbidden operator, consider multiplication: If one operand is a power of 2, then the product will end in trailing zeros, no matter how random is the other operand.

All bit positions in the combined output should depend on high-quality bits from at least two methods, and may also depend on lower-quality bits from additional methods. In the tables above, the bits labeled “can use as random” are considered high quality; those labeled “can use in bit mix” are considered low quality, unless they also pass a statistical suite such as Diehard.

There is one further trick at our disposal, the idea of using a method as a successor relation instead of as a generator in its own right. Each of the methods described above is a mapping from some 64-bit state $x _ { i }$ to a unique successor state $x _ { i + 1 }$ . For a method to pass a good statistical test suite, it must have no detectable correlations between a state and its successor. If, in addition, the method has period $2 ^ { 6 4 }$ or $2 ^ { 6 4 } - 1$ , then all values (except possibly zero) occur exactly once as successor states.

Suppose we take the output of a generator, say C1 above, with period $2 ^ { 6 4 }$ , and run it through generator A6, whose period is $2 ^ { 6 4 } - 1$ , as a successor relation. This is conveniently denoted by “A6(C1),” which we will call a composed generator. Note that the composed output is emphatically not fed back into the state of C1, which continues unperturbed. The composed generator A6(C1) has the period of C1, not, unfortunately, the product of the two periods. But its random mapping of C1’s output values effectively fixes C1’s problems with short-period low bits. (The better so if the form of A6 with left-shift first is used.) And, A6(C1) will also fix A6’s weakness that a bit depends only on a few bits of the previous state. We will thus consider a carefully constructed composed generator as being a combined generator, on a par with direct combining via $^ +$ or ^.

Composition is inferior to direct combining in that it costs almost as much but does not increase the size of the state or the length of the period. It is superior to direct combining in its ability to mix widely differing bit positions. In the previous example we would not have accepted $\mathbf { A } 6 { + } \mathbf { C } 1$ as a combined generator, because the low bits of C1 are so poor as to add little value to the combination; but A6(C1) has no such liability, and much to recommend it. In the preceding summary tables of each method, we have indicated recommended combinations for composed generators in the table entries, “can improve by.”

We can now completely describe the generator in Ran, above, by the pseudoequation,

$$
\mathrm { R a n } = [ \mathrm { A l } _ { l } ( \mathbf { C } 3 ) + \mathrm { A } 3 _ { r } ] \wedge \mathbf { B } 1
$$

that is, the combination and/or composition of four different generators. For the methods A1 and A3, the subscripts $l$ and $r$ denote whether a left- or right-shift operation is done first. The period of Ran is the least common multiple of the periods of C3, A3, and B1.

The simplest and fastest generator that we can readily recommend is

$$
{ \tt R a n q 1 } \equiv { \tt D 1 } ( { \tt A 1 } _ { r } )
$$

implemented as

struct Ranq1 {   
Recommended generator for everyday use. The period is $\approx 1 . 8 \times 1 0 ^ { 1 9 }$ . Calling conventions same as Ran, above.

Ullong v;Ranq1(Ullong j) : v(4101842887655102017LL) {$ { \texttt { v } } \hat { } = :$ j;$\qquad \mathtt { v } =$ int64();}inline Ullong int64() {$\tau \ \hat { \mathbf { \Omega } } = \textbf { v } > > \ 2 1$ ; $\texttt { v } \hat { } = \texttt { v } < < \texttt { 3 5 }$ ; $\texttt { V } \hat { } = \texttt { V } > > \texttt { 4 }$ ;return $^ { \texttt { v } * }$ 2685821657736338717LL;}inline Doub doub() { return 5.42101086242752217E-20 $^ *$ int64(); }inline Uint int32() { return (Uint)int64(); }};

Ranq1 generates a 64-bit random integer in 3 shifts, 3 xors, and one multiply, or a double floating value in one additional multiply. Its method is concise enough to go easily inline in an application. It has a period of “only” $1 . 8 \times 1 0 ^ { 1 9 }$ , so it should not be used by an application that makes more than $\sim 1 0 ^ { 1 2 }$ calls. With that restriction, we think that Ranq1 will do just fine for $9 9 . 9 9 \%$ of all user applications, and that Ran can be reserved for the remaining $0 . 0 1 \%$ .

If the “short” period of Ranq1 bothers you (which it shouldn’t), you can instead use

$$
\mathrm { R a n q } 2 \equiv \mathrm { A } 3 _ { r } \wedge \mathrm { B } 1
$$

whose period is $8 . 5 \times 1 0 ^ { 3 7 }$ .

# .h struct Ranq2 {

Backup generator if Ranq1 has too short a period and Ran is too slow. The period is $\approx 8 . 5 \times$ $1 0 ^ { 3 7 }$ . Calling conventions same as Ran, above.

Ullong v,w; Ranq2(Ullong j) : v(4101842887655102017LL), w(1) { $\scriptstyle \mathtt { v } \ \hat { } =$ j; $\kappa =$ int64(); $\qquad \mathtt { v } \ =$ int64(); } inline Ullong int64() { $\bar { \tau } \stackrel {  } { = } \texttt { V } > > 1 7$ ; $\texttt { v } \hat { } = \texttt { v } < < \texttt { 3 1 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 8 }$ ; $\kappa =$ 4294957665U\*(w & 0xffffffff) $^ +$ $\mathit { \Pi } _ { \mathbb { W } } ^ { ' } > > \mathit { \Omega } 3 2 )$ ; return $ { \texttt { v } } ^ { \star }  { \texttt { w } }$ ; } inline Doub doub() { return 5.42101086242752217E-20 $^ *$ int64(); } inline Uint int32() { return (Uint)int64(); } };

# 7.1.4 Random Hashes and Random Bytes

Every once in a while, you want a random sequence $H _ { i }$ whose values you can visit or revisit in any order of $i$ ’s. That is to say, you want a random hash of the integers $i$ , one that passes serious tests for randomness, even for very ordered sequences of $i$ ’s. In the language already developed, you want a generator that has no state at all and is built entirely of successor relationships, starting with the value $i$ .

An example that easily passes the Diehard test is

$$
{ \tt R a n h a s h } \equiv { \tt A } 2 _ { l } ( { \tt D } 3 ( { \tt A } 7 _ { r } ( { \tt C } 1 ( i ) ) ) )
$$

Note the alternation between successor relations that utilize 64-bit multiplication and ones using shifts and XORs.

# ran.h struct Ranhash {

High-quality random hash of an integer into several numeric types. inline Ullong int64(Ullong u) { Returns hash of u as a 64-bit integer. Ullong $ { \texttt { v } } =  { \texttt { u } } *$ 3935559000370003845LL $^ +$ 2691343689449507681LL; $\texttt { v } \hat { } = \texttt { v } > > 2 1$ ; $\bar { \tau } = \texttt { V } < < \texttt { 3 7 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 4 }$ ; ${ \textbf { \texttt { v } } } * =$ 4768777513237032717LL; $\texttt { v } \hat { } = \texttt { v } < < \texttt { 2 0 }$ ; v ^= v >> 41; $\texttt { V } \hat { } = \texttt { V } < < \texttt { 5 }$ ; return v; inline Uint int32(Ullong u) Returns hash of u as a 32-bit integer. { return (Uint)(int64(u) & 0xffffffff) ; } inline Doub doub(Ullong u) Returns hash of u as a double-precision floating value between 0. and 1. return 5.42101086242752217E-20 $^ *$ int64(u); }

Since Ranhash has no state, it has no constructor. You just call its $\mathtt { i n t } 6 4 ( i )$ function, or any of its other functions, with your value of $i$ whenever you want.

Random Bytes. In a different set of circumstances, you may want to generate random integers a byte at a time. You can of course pull bytes out of any of the above recommended combination generators, since they are constructed to be equally good on all bits. The following code, added to any of the generators above, augments them with an int8() method. (Be sure to initialize bc to zero in the constructor.)

Ullong breg;   
Int bc;   
inline unsigned char int8() { if (bc--) return (unsigned char)(breg $> > = ~ 8 )$ ; breg $=$ int64(); bc $= ~ 7$ ; return (unsigned char)breg;   
}

If you want a more byte-oriented, though not necessarily faster, algorithm, an interesting one — in part because of its interesting history — is Rivest’s RC4, used in many Internet applications. RC4 was originally a proprietary algorithm of RSA, Inc., but it was protected simply as a trade secret and not by either patent or copyright. The result was that when the secret was breached, by an anonymous posting to the Internet in 1994, RC4 became, in almost all respects, public property. The name RC4 is still protectable, and is a trademark of RSA. So, to be scrupulous, we give the following implementation another name, Ranbyte.

# struct Ranbyte {

nerator for random bytes using the algorithm generally known as RC4.   
Int s[256],i,j,ss;   
Uint v;   
Ranbyte(Int u) {   
Constructor. Call with any integer seed. $\qquad \mathtt { v } \ =$ 2244614371U ^ u; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<256; $\dot { \bf 1 } + +$ ) {s[i] = i;} for $\scriptstyle \dot { \ j } = 0$ , $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<256; $\mathbf { i } + + \mathbf { i }$ ) { ss $=$ s[i]; j = (j + ss + ( $\cdot \mathrm { ~  ~ v ~ } > > 2 4 )$ ) & 0xff; s[i] = s[j]; s[j] $=$ ss; $\begin{array} { c c c c c } { \mathrm { ~  ~ v ~ } = } & { ( \mathrm { ~  ~ v ~ } < < 2 4 ) } & { | } & { ( \mathrm { ~  ~ v ~ } > > 8 ) : } \end{array}$ ; } ${ \\mathrm { ~ \bf ~ i ~ } } = { \mathrm { ~ \bf ~ j ~ } } = { \mathrm { ~ \bf ~ 0 ~ } } _ { \mathrm { { i } } }$ ; for (Int $\mathtt { k } = 0$ ; $\mathtt { k } < 2 5 6$ ; $\mathrm { k } { + + }$ ) int8();   
}   
inline unsigned char int8() {   
Returns next random byte in the sequence. $\begin{array} { r c l } { \dot { \textbf { \ i } } } & { = } & { \left( \dot { \bf 1 } { + } 1 \right) } \end{array}$ & 0xff; ss = s[i]; ${ \dot { \textbf { j } } } =$ (j+ss) & 0xff; s[i] $=$ s[j]; s[j] $=$ ss; return (unsigned char)(s[(s[i] $+ \tt s$ [j]) & 0xff]);   
}   
Uint int32() {   
Returns a random 32-bit integer constructed from 4 random bytes. Slow! $\tt { v } = 0$ ; for (int $\mathtt { k } = 0$ ; k<4; k++) { $\begin{array} { r l r } { \mathrm { ~ i ~ } = } & { { } ( \mathrm { i } + 1 ) } \end{array}$ ) & 0xff; ${ \bf s } { \bf s } = { \bf s } [ \mathrm { i } ]$ ; ${ \mathrm { ~ j ~ } } =$ (j+ss) & 0xff; s[i] $=$ s[j]; s[j] $=$ ss; v = (v << 8) | s[(s[i]+s[j]) & 0xff]; } return v;

# Doub doub() {

Returns a random double-precision floating value between 0. and 1. Slow!! return 2.32830643653869629E-10 $^ *$ ( int32() $^ +$ 2.32830643653869629E-10 $^ *$ int32() );   
}

# };

Notice that there is a lot of overhead in starting up an instance of Ranbyte, so you should not create instances inside loops that are executed many times. The methods that return 32-bit integers, or double floating-point values, are slow in comparison to the other generators above, but are provided in case you want to use Ranbyte as a test substitute for another, perhaps questionable, generator.

If you find any nonrandomness at all in Ranbyte, don’t tell us. But there are several national cryptological agencies that might, or might not, want to talk to you!

# 7.1.5 Faster Floating-Point Values

The steps above that convert a 64-bit integer to a double-precision floating-point value involves both a nontrivial type conversion and a 64-bit floating multiply. They are performance bottlenecks. One can instead directly move the random bits into the right place in the double word with union structure, a mask, and some 64-bit logical operations; but in our experience this is not significantly faster.

To generate faster floating-point values, if that is an absolute requirement, we need to bend some of our design rules. Here is a variant of “Knuth’s subtractive generator,” which is a so-called lagged Fibonacci generator on a circular list of 55 values, with lags 24 and 55. Its interesting feature is that new values are generated directly as floating point, by the floating-point subtraction of two previous values.

# ran.h struct Ranfib {

Implements Knuth’s subtractive generator using only floating operations. See text for cautions.

Doub dtab[55], dd;   
Int inext, inextp;   
Ranfib(Ullong j) : inext(0), inextp(31) {   
Constructor. Call with any integer seed. Uses Ranq1 to initialize. Ranq1 init(j); for (int $\mathtt { k } = 0$ ; k<55; $\mathrm { k } { + + }$ ) dtab[k] $=$ init.doub();   
}   
Doub doub() {   
Returns random double-precision floating value between 0. and 1. if ( $^ { + + }$ inext $\scriptstyle = = { \mathsf { 5 5 } }$ ) inext $\mathit { \Theta } = \mathit { \Theta } 0$ ; if ( $^ { + + }$ inextp $= =$ 55) inextp $\qquad = \ 0$ ; dd $=$ dtab[inext] - dtab[inextp]; if (dd $< 0 \dot { . }$ ) dd $+ = \ 1 . 0$ ; return (dtab[inext] $=$ dd);   
inline unsigned long int32()   
Returns random 32-bit integer. Recommended only for testing purposes. { return (unsigned long)(doub() $^ *$ 4294967295.0);}

# };

The int32 method is included merely for testing, or incidental use. Note also that we use Ranq1 to initialize Ranfib’s table of 55 random values. See earlier editions of Knuth or Numerical Recipes for a (somewhat awkward) way to do the initialization purely internally.

Ranfib fails the Diehard “birthday test,” which is able to discern the simple relation among the three values at lags 0, 24, and 55. Aside from that, it is a good, but not great, generator, with speed as its principal recommendation.

# 7.1.6 Timing Results

Timings depend so intimately on highly specific hardware and compiler details, that it is hard to know whether a single set of tests is of any use at all. This is especially true of combined generators, because a good compiler, or a CPU with sophisticated instruction look-ahead, can interleave and pipeline the operations of the individual methods, up to the final combination operations. Also, as we write, desktop computers are in transition from 32 bits to 64, which will affect the timing of 64-bit operations. So, you ought to familiarize yourself with C’s “clock_t clock(void)” facility and run your own experiments.

That said, the following tables give typical results for routines in this section, normalized to a $3 . 4 ~ \mathrm { G H z }$ Pentium CPU, vintage 2004. The units are $1 0 ^ { 6 }$ returned values per second. Large numbers are better.

<table><tr><td>Generator</td><td>int64()</td><td>doub()</td><td>int8()</td></tr><tr><td>Ran</td><td>19</td><td>10</td><td>51</td></tr><tr><td>Ranq1</td><td>39</td><td>13</td><td>59</td></tr><tr><td>Ranq2</td><td>32</td><td>12</td><td>58</td></tr><tr><td>Ranfib</td><td></td><td>24</td><td></td></tr><tr><td>Ranbyte</td><td></td><td></td><td>43</td></tr></table>

The int8() timings for Ran, Ranq1, and Ranq2 refer to versions augmented as indicated above.

# 7.1.7 When You Have Only 32-Bit Arithmetic

Our best advice is: Get a better compiler! But if you seriously must live in a world with only unsigned 32-bit arithmetic, then here are some options. None of these individually pass Diehard.

# (G) 32-Bit Xorshift RNG

state: $x$ (unsigned 32-bit)   
initialize: update: $\begin{array} { l } { x \neq 0 } \\ { x  x \land ( x \lor \mathrm { > } \vdash b _ { 1 } ) , } \\ { x  x \land ( x \ll b _ { 2 } ) , } \\ { x  x \land ( x \lor \mathrm { > } \vdash b _ { 3 } ) ; } \\ { x  x \land ( x \ll b _ { 1 } ) , } \\ { x  x \land ( x \lor \mathrm { > } \vdash b _ { 2 } ) , } \\ { x  x \land ( x \ll b _ { 3 } ) ; } \end{array}$ or   
can use as random: $x$ (32 bits, with caution)   
can use in bit mix: $x$ (32 bits)   
can improve by: output 32-bit MLCG successor   
period: $2 ^ { 3 2 } - 1$

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>b1</td><td rowspan=1 colspan=1>b2</td><td rowspan=1 colspan=1>b3</td></tr><tr><td rowspan=1 colspan=1>G1</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>17</td><td rowspan=2 colspan=1>53</td></tr><tr><td rowspan=1 colspan=1>G2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13</td></tr><tr><td rowspan=1 colspan=1>G3</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>G4</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>G5</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>G6</td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>G7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1>G8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>G9</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>5</td></tr></table>

# (H) MWC with Base $b = 2 ^ { 1 6 }$

state: initialize: update:

$x , y$ (unsigned 32-bit)   
$1 \leq x , y \leq 2 ^ { 1 6 } - 1$   
$x  a \ ( x \& \ [ 2 ^ { 1 6 } - 1 ] ) + ( x \ > > \ 1 6 )$   
$y  b \ ( y \ \& \ [ 2 ^ { 1 6 } - 1 ] ) + ( y \ > > \ 1 6 )$   
$( x ~ < < ~ 1 6 ) + y$   
same, or (with caution) $x$ or $y$   
output 32-bit xorshift successor   
$( 2 ^ { 1 6 } a - 2 ) ( 2 ^ { 1 6 } b - 2 ) / 4$ (product of two primes)

can use as random: can use in bit mix: can improve by: period:

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=1>a</td><td rowspan=1 colspan=1>b</td></tr><tr><td rowspan=1 colspan=1>H1</td><td rowspan=1 colspan=1>62904</td><td rowspan=2 colspan=1>4187434653</td></tr><tr><td rowspan=1 colspan=1>H2</td><td rowspan=1 colspan=1>64545</td></tr><tr><td rowspan=1 colspan=1>H3</td><td rowspan=1 colspan=1>34653</td><td rowspan=1 colspan=1>64545</td></tr><tr><td rowspan=1 colspan=1>H4</td><td rowspan=1 colspan=1>57780</td><td rowspan=1 colspan=1>55809</td></tr><tr><td rowspan=1 colspan=1>H5</td><td rowspan=1 colspan=1>48393</td><td rowspan=1 colspan=1>57225</td></tr><tr><td rowspan=1 colspan=1>H6</td><td rowspan=1 colspan=1>63273</td><td rowspan=1 colspan=1>33378</td></tr></table>

# (I) LCG Modulo $2 ^ { 3 2 }$

state: $x$ (unsigned 32-bit)   
initialize: any value   
update: $x  a x + c$ .mod $2 ^ { 3 2 }$ /   
can use as random: not recommended   
can use in bit mix: not recommended   
can improve by: output 32-bit xorshift successor   
period: $2 ^ { 3 2 }$

<table><tr><td rowspan=1 colspan=1>ID</td><td rowspan=1 colspan=6>a</td><td rowspan=1 colspan=1>c (any odd ok)</td></tr><tr><td rowspan=2 colspan=1>I1I213</td><td rowspan=2 colspan=6>137238374928913364532024337845</td><td rowspan=2 colspan=1>12897061011640531513797082193</td></tr><tr><td rowspan=1 colspan=2>2024337845</td><td rowspan=1 colspan=3>2024337845</td></tr><tr><td rowspan=4 colspan=1>I4I5</td><td rowspan=3 colspan=2></td><td rowspan=3 colspan=4>32310901</td><td></td></tr><tr><td rowspan=2 colspan=1></td><td></td></tr><tr><td rowspan=1 colspan=1>626627237</td></tr><tr><td rowspan=1 colspan=6>29943829</td><td rowspan=1 colspan=1>1013904223</td></tr></table>

# (J) MLCG Modulo 232

state: $x$ (unsigned 32-bit)   
initialize: $x \neq 0$   
update: $x \gets a x$ .mod $2 ^ { 3 2 }$ /   
can use as random: not recommended   
can use in bit mix: not recommended   
can improve by: output 32-bit xorshift successor   
period: $2 ^ { 3 0 }$

<table><tr><td>ID</td><td>a</td></tr><tr><td>J1</td><td>1597334677</td></tr><tr><td></td><td>741103597</td></tr><tr><td></td><td>1914874293</td></tr><tr><td></td><td>990303917</td></tr><tr><td>我</td><td>747796405</td></tr></table>

A high-quality, if somewhat slow, combined generator is

$$
\mathrm { R a n l i m } 3 2 \equiv [ \mathrm { G } 3 _ { l } ( \mathrm { I } 2 ) + \mathrm { G } 1 _ { r } ] \wedge [ \mathrm { G } 6 _ { l } ( \mathrm { H } 6 _ { b } ) + \mathrm { H } 5 _ { b } ]
$$

implemented as

struct Ranlim32 { High-quality random generator using only 32-bit arithmetic. Same conventions as Ran. Period $\approx 3 . 1 \dot { 1 } \times \dot { 1 0 } ^ { 3 7 }$ . Recommended only when 64-bit arithmetic is not available.

Uint u,v,w1,w2; Ranlim32(Uint j) : v(2244614371U), w1(521288629U), w2(362436069U) { $\mathrm { ~ u ~ } = \mathrm { ~ j ~ }$ ^ v; int32(); $\texttt { v } = \texttt { u }$ ; int32(); } inline Uint int32() { $\texttt { u } = \texttt { u } *$ 2891336453U $^ +$ 1640531513U; $\texttt { V } \hat { } = \texttt { V } > > \ 1 3$ ; $\texttt { V } \hat { } = \texttt { V } < < \texttt { 1 7 }$ ; $\texttt { v } \hat { } = \texttt { v } > > \texttt { 5 }$ ; $\mathrm { w 1 } ~ = ~ 3 3 3 7 8 ~ *$ (w1 & 0xffff) $^ +$ $\left( \mathbf { w } 1 \ > \ 1 6 \right)$ ; $\mathtt { w } 2 ~ = ~ 5 7 2 2 5 ~ *$ (w2 & 0xffff) $^ +$ (w2 >> 16); Uint $\texttt { x } = \texttt { u } \hat { }$ (u << 9); x $\hat { \mathrm { ~ \bf ~ \chi ~ } } = \mathrm { ~ \bf ~ z ~ } > >$ 17; x $ { \hat { \mathbf { \phi } } } <  { \mathbf { \hat { z } } } \leq  { \mathbf { \phi } } \times  { \mathbf { \hat { z } } } <  { \mathbf { \phi } } 6$ ; Uint $\mathrm { ~ y ~ } = \mathrm { ~ w ~ 1 ~ } \ \hat { \ }$ ( $\tau 1 < < 1 7 )$ ; y $\hat { \mathbf { \beta } } = \texttt { y } > > \mathbf { \beta } 1 5$ ; $\mathrm { ~ y ~ } \ \hat { ~ } = \mathrm { ~ y ~ } < < \ 5$ ; return $( { \bf x } { \mathrm { ~ + ~ } } { \mathrm v } ) { \mathrm { ~ \hat { ~ } { ~ ( ~ y ~ + ~ } } } { \mathrm w } 2 )$ ; inline Doub doub() { return 2.32830643653869629E-10 $^ *$ int32(); } inline Doub truedoub() { return 2.32830643653869629E-10 $^ *$ ( int32() + 2.32830643653869629E-10 $^ *$ int32() ); } };

Note that the doub() method returns floating-point numbers with only 32 bits of precision. For full precision, use the slower truedoub() method.

# CITED REFERENCES AND FURTHER READING:

Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer), Chapter 1.   
Marsaglia, G 1968, “Random Numbers Fall Mainly in the Planes”, Proceedings of the National Academy of Sciences, vol. 61, pp. 25-28.[1]   
Entacher, K. 1997, “A Collection of Selected Pseudorandom Number Generators with Linear Structures”, Technical Report No. 97, Austrian Center for Parallel Computation, University of Vienna. [Available on the Web at multiple sites.][2]   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading,MA: Addison-Wesley).[3]   
Schrage, L. 1979, “A More Portable Fortran Random Number Generator,” ACM Transactions on Mathematical Software, vol.5, pp.132-138.[4]   
Park, S.K., and Miller, K.W. 1988, “Random Number Generators: Good Ones Are Hard to Find,” Communications of the ACM,vol.31,pp.1192-1201.[5]   
L’Ecuyer, P. 1997 “Uniform Random Number Generators: A Review,” Proceedings of the 1997 Winter Simulation Conference,Andradótir, S.et al.,eds.(Piscataway, NJ: IEEE).[6]   
Marsaglia, G. 1999, “Random Numbers for C: End, at Last?”, posted 1999 January 20 to sci.stat.math.[7]   
Marsaglia, G. 2003, “Diehard Battery of Tests of Randomness v0.2 beta,” $^ { 2 0 0 7 + }$ at http://www.cs.hku.hk/\~diehard/.[8]   
Rukhin, A. et al. 2001, “A Statistical Test Suite for Random and Pseudorandom Number Generators”, NIST Special Publication 800-22 (revised to May 15, 2001).[9]   
Marsaglia, G. 2003, “Xorshift RNGs”, Journal of Statistical Software, vol. 8, no. 14, pp. 1-6.[10]   
Brent, R.P. 2004, “Note on Marsaglia’s Xorshift Random Number Generators”, Journal of Statistical Software, vol. 11, no.5,pp. 1-5.[11]   
L’Ecuyer, P. 1996, “Maximally Equidistributed Combined Tausworthe Generators,” Mathematics of Computation, vol. 65, pp. 203-213.[12]   
L’Ecuyer, P. 1999, “Tables of Maximally Equidistributed Combined LSFR Generators,” Mathematics of Computation, vol. 68,pp.261-269.[13]   
Couture, R. and L’Ecuyer, P. 1997, “Distribution Properties of Multiply-with-Carry Random Number Generators,” Mathematics of Computation, vol. 66, pp. 591-607.[14]   
L’Ecuyer, P. 1999, “Tables of Linear Congruential Generators of Different Sizes and Good Lattice Structure”, Mathematics of Computation, vol. 68, pp. 249-260.[15]

# 7.2 Completely Hashing a Large Array

We introduced the idea of a random hash or hash function in $\ S 7 . 1 . 4$ . Once in a while we might want a hash function that operates not on a single word, but on an entire array of length $M$ . Being perfectionists, we want every single bit in the hashed output array to depend on every single bit in the given input array. One way to achieve this is to borrow structural concepts from algorithms as unrelated as the Data Encryption Standard (DES) and the Fast Fourier Transform (FFT)!

DES, like its progenitor cryptographic system LUCIFER, is a so-called “block product cipher” [1]. It acts on 64 bits of input by iteratively applying (16 times, in fact) a kind of highly nonlinear bit-mixing function. Figure 7.2.1 shows the flow of information in DES during this mixing. The function $g$ , which takes 32 bits into 32 bits, is called the “cipher function.” Meyer and Matyas [1] discuss the importance of the cipher function being nonlinear, as well as other design criteria.

DES constructs its cipher function $g$ from an intricate set of bit permutations and table lookups acting on short sequences of consecutive bits. For our purposes, a different function $g$ that can be rapidly computed in a high-level computer language is preferable. Such a function probably weakens the algorithm cryptographically. Our purposes are not, however, cryptographic: We want to find the fastest $g$ , and the smallest number of iterations of the mixing procedure in Figure 7.2.1, such that our output random sequence passes the tests that are customarily applied to random number generators. The resulting algorithm is not DES, but rather a kind of “pseudo-DES,” better suited to the purpose at hand.

![](images/f474e184c1327ddc145b14df7a7602f396c3b79d5fe55008eb3edc52183cd8f6.jpg)  
Figure 7.2.1. The Data Encryption Standard (DES) iterates a nonlinear function $_ g$ on two 32-bit words, in the manner shown here (after Meyer and Matyas [1]).

Following the criterion mentioned above, that $g$ should be nonlinear, we must give the integer multiply operation a prominent place in $g$ . Confining ourselves to multiplying 16- bit operands into a 32-bit result, the general idea of $g$ is to calculate the three distinct 32- bit products of the high and low 16-bit input half-words, and then to combine these, and perhaps additional fixed constants, by fast operations (e.g., add or exclusive-or) into a single 32-bit result.

There are only a limited number of ways of effecting this general scheme, allowing systematic exploration of the alternatives. Experimentation and tests of the randomness of the output lead to the sequence of operations shown in Figure 7.2.2. The few new elements in the figure need explanation: The values $C _ { 1 }$ and $C _ { 2 }$ are fixed constants, chosen randomly with the constraint that they have exactly 16 1-bits and $^ { 1 6 0 }$ -bits; combining these constants via exclusive-or ensures that the overall $g$ has no bias toward 0- or 1-bits. The “reverse halfwords” operation in Figure 7.2.2 turns out to be essential; otherwise, the very lowest and very highest bits are not properly mixed by the three multiplications.

It remains to specify the smallest number of iterations $N _ { i t }$ that we can get away with. For purposes of this section, we recommend $N _ { i t } = 2$ . We have not found any statistical deviation from randomness in sequences of up to $1 0 ^ { 9 }$ random deviates derived from this scheme. However, we include $C _ { 1 }$ and $C _ { 2 }$ constants for $N _ { i t } \le 4$ .

# void psdes(Uint &lword, Uint &rword) {

Pseudo-DES hashing of the 64-bit word (lword,rword). Both 32-bit arguments are returned hashed on all bits.

const int NITER $^ { * 2 }$ ;   
static const Uint c1[4] ${ \boldsymbol { = } } \{$ 0xbaa96887L, 0x1e17d32cL, 0x03bcdc3cL, 0x0f33d1b2L};   
static const Uint c2[4] $= \downarrow$ 0x4b0f3b58L, 0xe874f0c3L, 0x6955c5a6L, 0x55a7ca46L};   
Uint i,ia,ib,iswap,itmph $\mathtt { \mathtt { = 0 } }$ ,itmpl $_ { = 0 }$ ;   
for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<NITER; $\mathbf { i } + + \mathbf { i }$ ) {   
Perform niter iterations of DES logic, using a simpler (noncryptographic) nonlinear func  
tion instead of DES’s. ia $=$ (iswap=rword) ^ c1[i]; The bit-rich constants c1 and (below) itmpl $=$ ia & 0xffff; c2 guarantee lots of nonlinear mixitmph $=$ ia >> 16; ing.

![](images/66847a2538c8d1b36330b778d3a3a83e2250cda8a4326340231c9ec2a83d1467.jpg)  
Figure 7.2.2. The nonlinear function $_ g$ used by the routine psdes.

ib=itmpl\*itmpl+ \~(itmph\*itmph); rword $=$ lword ^ (((ia $=$ (ib >> 16) ((ib & 0xffff) << 16)) ^ c2[i])+itmpl\*itmph); lword $=$ iswap; }

Thus far, this doesn’t seem to have much to do with completely hashing a large array. However, psdes gives us a building block, a routine for mutually hashing two arbitrary 32-bit integers. We now turn to the FFT concept of the butterfly to extend the hash to a whole array.

The butterfly is a particular algorithmic construct that applies to an array of length $N$ , a power of 2. It brings every element into mutual communication with every other element in about $N \log _ { 2 } N$ operations. A useful metaphor is to imagine that one array element has a disease that infects any other element with which it has contact. Then the butterfly has two properties of interest here: (i) After its $\log _ { 2 } N$ stages, everyone has the disease. Furthermore, (ii) after $j$ stages, $2 ^ { j }$ elements are infected; there is never an “eye of the needle” or “necking down” of the communication path.

The butterfly is very simple to describe: In the first stage, every element in the first half of the array mutually communicates with its corresponding element in the second half of the array. Now recursively do this same thing to each of the halves, and so on. We can see by induction that every element now has a communication path to every other one: Obviously it works when $N = 2$ . And if it works for $N$ , it must also work for $2 N$ , because the first step gives every element a communication path into both its own and the other half of the array, after which it has, by assumption, a path everywhere.

We need to modify the butterfly slightly, so that our array size $M$ does not have to be a power of 2. Let $N$ be the next larger power of 2. We do the butterfly on the (virtual) size $N$ , ignoring any communication with nonexistent elements larger than $M$ . This, by itself, doesn’t do the job, because the later elements in the first $N / 2$ were not able to “infect” the second $N / 2$ (and similarly at later recursive levels). However, if we do one extra communication between elements of the first $N / 2$ and second $N / 2$ at the very end, then all missing communication paths are restored by traveling through the first $N / 2$ elements.

The third line in the following code is an idiom that sets n to the next larger power of 2 greater or equal to m, a miniature masterpiece due to S.E. Anderson [2]. If you look closely, you’ll see that it is itself a sort of butterfly, but now on bits!

# void hashall(VecUint &arr) {

Replace the array arr by a same-sized hash, all of whose bits depend on all of the bits in arr.   
Uses psdes for the mutual hash of two 32-bit words.   
Int $\mathbb { m } =$ arr.size(), $\tt { n } { = } \tt { m } { - } 1$ ;   
$\mathrm { n } | = \mathrm { n } > > 1$ ; $n \left| = \mathrm { n } > > 2 \right.$ ; $\mathtt { n } | = \mathtt { n } > > 4$ ; $n \left| = \mathtt { n } > > 8 \right.$ ; n $_ 1 | = \mathtt { n } > > 1 6$ ; $\mathrm { \ n } { + } + $ ;   
Incredibly, n is now the next power of $2 \geq \mathtt { m }$ .   
Int nb=n,nb2=n>>1,j,jb;   
if $\scriptstyle \mathbf { n < 2 }$ ) throw("size must be $> ~ 1 "$ );   
while (nb $> ~ 1$ ) { for (jb=0;jb<n-nb+1;jb $+ =$ nb) for (j=0;j<nb2; ${ \dot { \mathrm { 3 } } } \mathrm { + + }$ ) if (jb+j+nb2 < m) psdes(arr[jb+j],arr[jb+j+nb2]); nb $=$ nb2; nb2 $> > = ~ 1$ ;   
n $\scriptstyle > 2 \ = \ n > > 1$ ;   
if (m $! = \mathrm { ~ \tt ~ n ~ } )$ ) for (j=nb2;j<m;j++) psdes(arr[j],arr[j-nb2]);   
Final mix needed only if m is not a power of 2.

# CITED REFERENCES AND FURTHER READING:

Meyer, C.H. and Matyas, S.M. 1982, Cryptography: A New Dimension in Computer Data Security (New York: Wiley).[1]

Zonst, A.E. 2000, Understanding the FFT, 2nd revised ed. (Titusville, FL: Citrus Press).

Anderson, S.E. 2005, “Bit Twiddling Hacks,” $^ { 2 0 0 7 + }$ at http://graphics.stanford.edu/ \~seander/bithacks.html .[2]

Data Encryption Standard,1977 January 15, Federal Information Processing Standards Publication, number 46 (Washington: U.S. Department of Commerce, National Bureau of Standards).

Guidelines forImplementing and Using the NBS Data Encryption Standard,1981 April1,Federal Information Processing Standards Publication, number 74 (Washington: U.S. Department of Commerce, National Bureau of Standards).

# 7.3 Deviates from Other Distributions

In $\ S 7 . 1$ we learned how to generate random deviates with a uniform probability between 0 and 1, denoted $\mathrm { U } ( 0 , 1 )$ . The probability of generating a number between $x$ and $x + d x$ is

$$
p ( x ) d x = { \left\{ \begin{array} { l l } { d x } & { 0 \leq x < 1 } \\ { 0 } & { { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

and we write

$$
x \sim \mathrm { U } ( 0 , 1 )
$$

As in $\ S 6 . 1 4$ , the symbol $\sim$ can be read as “is drawn from the distribution.”

In this section, we learn how to generate random deviates drawn from other probability distributions, including all of those discussed in $\ S 6 . 1 4$ . Discussion of specific distributions is interleaved with the discussion of the general methods used.

# 7.3.1 Exponential Deviates

Suppose that we generate a uniform deviate $x$ and then take some prescribed function of it, $y ( x )$ . The probability distribution of $y$ , denoted $p ( y ) d y$ , is determined by the fundamental transformation law of probabilities, which is simply

$$
| p ( y ) d y | = | p ( x ) d x |
$$

or

$$
p ( y ) = p ( x ) \left| { \frac { d x } { d y } } \right|
$$

As an example, take

$$
y ( x ) = - \ln ( x )
$$

with $x \sim \mathrm { U } ( 0 , 1 )$ . Then

$$
p ( y ) d y = \left| { \frac { d x } { d y } } \right| d y = e ^ { - y } d y
$$

which is the exponential distribution with unit mean, Exponential .1/, discussed in $\ S 6 . 1 4 . 5$ . This distribution occurs frequently in real life, usually as the distribution of waiting times between independent Poisson-random events, for example the radioactive decay of nuclei. You can also easily see (from 7.3.6) that the quantity $y / \beta$ has the probability distribution $\beta e ^ { - \beta y }$ , so

$$
y / \beta \sim \mathrm { E x p o n e n t i a l } \left( \beta \right)
$$

We can thus generate exponential deviates at a cost of about one uniform deviate, plus a logarithm, per call.

struct Expondev : Ran {   
Structure for exponential deviates. Doub beta; Expondev(Doub bbeta, Ullong i) : Ran(i), beta(bbeta) {} Constructor arguments are $\beta$ and a random sequence seed. Doub dev() Return an exponential deviate. Doub u; do u $=$ doub(); while $\mathit { \Omega } _ { \lambda } ^ { ' } = = \mathit { \Omega } 0 . \mathit { \check { \Psi } } .$ ); return -log(u)/beta; }   
};

Our convention here and in the rest of this section is to derive the class for each kind of deviate from the uniform generator class Ran. We use the constructor to set the distribution’s parameters and set the initial seed for the generator. We then provide a method dev() that returns a random deviate from the distribution.

# 7.3.2 Transformation Method in General

Let’s see what is involved in using the above transformation method to generate some arbitrary desired distribution of $y$ ’s, say one with $p ( y ) ~ = ~ f ( y )$ for some positive function $f$ whose integral is 1. According to (7.3.4), we need to solve the differential equation

![](images/4d640d1cbe0a89b22cf2a074907ca7f56a5fad2dd37922fedd7a66f7bfdeae86.jpg)  
Figure 7.3.1. Transformation method for generating a random deviate $y$ from a known probability distribution $p ( y )$ . The indefinite integral of $p ( y )$ must be known and invertible. A uniform deviate $x$ is chosen between 0 and 1. Its corresponding $y$ on the definite-integral curve is the desired deviate.

$$
{ \frac { d x } { d y } } = f ( y )
$$

But the solution of this is just $x = F ( y )$ , where $F ( y )$ is the indefinite integral of $f ( y )$ . The desired transformation that takes a uniform deviate into one distributed as $f ( y )$ is therefore

$$
y ( x ) = F ^ { - 1 } ( x )
$$

where $F ^ { - 1 }$ is the inverse function to $F$ . Whether (7.3.9) is feasible to implement depends on whether the inverse function of the integral of $f ( y )$ is itself feasible to compute, either analytically or numerically. Sometimes it is, and sometimes it isn’t.

Incidentally, (7.3.9) has an immediate geometric interpretation: Since $F ( y )$ is the area under the probability curve to the left of $y$ , (7.3.9) is just the prescription: Choose a uniform random $x$ , then find the value $y$ that has that fraction $x$ of probability area to its left, and return the value $y$ . (See Figure 7.3.1.)

# 7.3.3 Logistic Deviates

Deviates from the logistic distribution, as discussed in $\ S 6 . 1 4 . 4$ , are readily generated by the transformation method, using equation (6.14.15). The cost is again dominated by one uniform deviate, and a logarithm, per logistic deviate.

struct Logisticdev : Ran   
Structure for logistic deviates. Doub mu,sig; Logisticdev(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig) {} Constructor arguments are $\mu , \sigma$ , and a random sequence seed. Doub dev() { Return a logistic deviate. Doub u; do u $=$ doub(); while $( \mathrm { u } * ( 1 \ : . - \mathrm { u } ) = = \ : 0 \ : . )$ ; return mu $^ +$ 0.551328895421792050\*sig\*log(u/(1.-u)); }   
};

# 7.3.4 Normal Deviates by Transformation (Box-Muller)

Transformation methods generalize to more than one dimension. If $x _ { 1 } , x _ { 2 } , \ldots$ are random deviates with a joint probability distribution $p ( x _ { 1 } , x _ { 2 } , . . . ) d x _ { 1 } d x _ { 2 } . . . .$ , and if $y _ { 1 } , y _ { 2 } , \ldots$ are each functions of all the $x$ ’s (same number of $y$ ’s as $x$ ’s), then the joint probability distribution of the $y$ ’s is

$$
p ( y _ { 1 } , y _ { 2 } , \ldots ) d y _ { 1 } d y _ { 2 } \ldots = p ( x _ { 1 } , x _ { 2 } , \ldots ) \left| { \frac { \partial ( x _ { 1 } , x _ { 2 } , \ldots ) } { \partial ( y _ { 1 } , y _ { 2 } , \ldots ) } } \right| d y _ { 1 } d y _ { 2 } \ldots
$$

where $| \partial ( \mathrm { ~  ~ \theta ~ } ) / \partial ( \mathrm { ~  ~ \theta ~ } ) |$ is the Jacobian determinant of the $x$ ’s with respect to the $y$ ’s (or the reciprocal of the Jacobian determinant of the $y$ ’s with respect to the $x$ ’s).

An important historical example of the use of (7.3.10) is the Box-Muller method for generating random deviates with a normal (Gaussian) distribution (-6.14.1):

$$
p ( y ) d y = \frac { 1 } { \sqrt { 2 \pi } } e ^ { - y ^ { 2 } / 2 } d y
$$

Consider the transformation between two uniform deviates on (0,1), $x _ { 1 } , x _ { 2 }$ , and two quantities $y _ { 1 } , y _ { 2 }$ ,

$$
\begin{array} { r } { y _ { 1 } = \sqrt { - 2 \ln x _ { 1 } } \cos 2 \pi x _ { 2 } } \\ { y _ { 2 } = \sqrt { - 2 \ln x _ { 1 } } \sin 2 \pi x _ { 2 } } \end{array}
$$

Equivalently we can write

$$
\begin{array} { l } { { \displaystyle x _ { 1 } = \exp \left[ - \frac { 1 } { 2 } ( y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } ) \right] } } \\ { { \displaystyle x _ { 2 } = \frac { 1 } { 2 \pi } \arctan \frac { y _ { 2 } } { y _ { 1 } } } } \end{array}
$$

Now the Jacobian determinant can readily be calculated (try it!):

$$
\frac { \partial ( x _ { 1 } , x _ { 2 } ) } { \partial ( y _ { 1 } , y _ { 2 } ) } = \left| \frac { \frac { \partial x _ { 1 } } { \partial y _ { 1 } } } { \frac { \partial x _ { 2 } } { \partial y _ { 1 } } } \right. \frac { \left. \frac { \partial x _ { 1 } } { \partial y _ { 2 } } \right| } { \left. \frac { \partial x _ { 2 } } { \partial y _ { 2 } } \right| } = - \left[ \frac { 1 } { \sqrt { 2 \pi } } e ^ { - y _ { 1 } ^ { 2 } / 2 } \right] \left[ \frac { 1 } { \sqrt { 2 \pi } } e ^ { - y _ { 2 } ^ { 2 } / 2 } \right]
$$

Since this is the product of a function of $y _ { 2 }$ alone and a function of $y _ { 1 }$ alone, we see that each $y$ is independently distributed according to the normal distribution (7.3.11).

One further trick is useful in applying (7.3.12). Suppose that, instead of picking uniform deviates $x _ { 1 }$ and $x _ { 2 }$ in the unit square, we instead pick $v _ { 1 }$ and $v _ { 2 }$ as the ordinate and abscissa of a random point inside the unit circle around the origin. Then the sum of their squares, $R ^ { 2 } \equiv v _ { 1 } ^ { 2 } + v _ { 2 } ^ { 2 }$ , is a uniform deviate, which can be used for $x _ { 1 }$ , while the angle that $( v _ { 1 } , v _ { 2 } )$ defines with respect to the $v _ { 1 }$ -axis can serve as the random angle $2 \pi x _ { 2 }$ . What’s the advantage? It’s that the cosine and sine in (7.3.12) can now be written as $v _ { 1 } / \sqrt { R ^ { 2 } }$ and $v _ { 2 } / \sqrt { R ^ { 2 } }$ , obviating the trigonometric function calls! (In the next section we will generalize this trick considerably.)

Code for generating normal deviates by the Box-Muller method follows. Consider it for pedagogical use only, because a significantly faster method for generating normal deviates is coming, below, in $\ S 7 . 3 . 9$ .

struct Normaldev_BM : Ran {   
Structure for normal deviates. Doub mu,sig; Doub storedval; Normaldev_BM(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig), storedval(0.) {} Constructor arguments are $\mu$ , $\sigma$ , and a random sequence seed. Doub dev( Return a normal deviate. Doub v1,v2,rsq,fac; if (storedval $\scriptstyle = = 0$ .) { We don’t have an extra deviate handy, so do { v1=2.0\*doub()-1.0; pick two uniform numbers in the square ex-$\mathtt { v } 2 = 2$ .0\*doub()-1.0; tending from $^ { - 1 }$ to $+ 1$ in each direction, rsq=v1\*v1+v2\*v2; see if they are in the unit circle, } while (rsq $> = ~ 1 . 0$ || $\mathtt { r s q } = = 0 . 0 )$ ; or try again. fac=sqrt(-2.0\*log(rsq)/rsq); Now make the $\mathsf { B o x }$ -Muller transformation to storedval $=$ v1\*fac; get two normal deviates. Return one and return mu $^ +$ sig\*v2\*fac; save the other for next time. } else { We have an extra deviate handy, fac $=$ storedval; storedval $\qquad = \ 0 .$ ; return mu $^ +$ sig\*fac; so return it. } }   
};

# 7.3.5 Rayleigh Deviates

The Rayleigh distribution is defined for positive $z$ by

$$
\begin{array} { r l r } { p ( z ) d z = z \exp \left( - \frac { 1 } { 2 } z ^ { 2 } \right) d z } & { { } } & { ( z > 0 ) } \end{array}
$$

Since the indefinite integral can be done analytically, and the result easily inverted, a simple transformation method from a uniform deviate $x$ results:

$$
z = \sqrt { - 2 \ln x } , \quad x \sim \mathrm { U } ( 0 , 1 )
$$

A Rayleigh deviate $z$ can also be generated from two normal deviates $y _ { 1 }$ and $y _ { 2 }$ by

$$
z = \sqrt { y _ { 1 } ^ { 2 } + y _ { 2 } ^ { 2 } } , \quad y _ { 1 } , y _ { 2 } \sim \mathrm { N } ( 0 , 1 )
$$

Indeed, the relation between equations (7.3.16) and (7.3.17) is immediately evident in the equation for the Box-Muller method, equation (7.3.12), if we square and sum that method’s two normal deviates $y _ { 1 }$ and $y _ { 2 }$ .

# 7.3.6 Rejection Method

The rejection method is a powerful, general technique for generating random deviates whose distribution function $p ( x ) d x$ (probability of a value occurring between $x$ and $x + d x ,$ ) is known and computable. The rejection method does not require that the cumulative distribution function (indefinite integral of $p ( x ) { \ddot { } }$ ) be readily computable, much less the inverse of that function — which was required for the transformation method in the previous section.

The rejection method is based on a simple geometrical argument (Figure 7.3.2):

![](images/7e9df5a5bc3f129e9e3f9da95c15d8d7888937fe57de8fbbc228f15a1ed03925.jpg)  
Figure 7.3.2. Rejection method for generating a random deviate $x$ from a known probability distribution $p ( x )$ that is everywhere less than some other function $f ( x )$ . The transformation method is first used to generate a random deviate $x$ of the distribution $f$ (compare Figure 7.3.1). A second uniform deviate is used to decide whether to accept or reject that $x$ . If it is rejected, a new deviate of $f$ is found, and so on. The ratio of accepted to rejected points is the ratio of the area under $p$ to the area between $p$ and $f$ .

Draw a graph of the probability distribution $p ( x )$ that you wish to generate, so that the area under the curve in any range of $x$ corresponds to the desired probability of generating an $x$ in that range. If we had some way of choosing a random point in two dimensions, with uniform probability in the area under your curve, then the $x$ value of that random point would have the desired distribution.

Now, on the same graph, draw any other curve $f ( x )$ that has finite (not infinite) area and lies everywhere above your original probability distribution. (This is always possible, because your original curve encloses only unit area, by definition of probability.) We will call this $f ( x )$ the comparison function. Imagine now that you have some way of choosing a random point in two dimensions that is uniform in the area under the comparison function. Whenever that point lies outside the area under the original probability distribution, we will reject it and choose another random point. Whenever it lies inside the area under the original probability distribution, we will accept it.

It should be obvious that the accepted points are uniform in the accepted area, so that their $x$ values have the desired distribution. It should also be obvious that the fraction of points rejected just depends on the ratio of the area of the comparison function to the area of the probability distribution function, not on the details of shape of either function. For example, a comparison function whose area is less than 2 will reject fewer than half the points, even if it approximates the probability function very badly at some values of $x$ , e.g., remains finite in some region where $p ( x )$ is zero.

It remains only to suggest how to choose a uniform random point in two dimensions under the comparison function $f ( x )$ . A variant of the transformation method $( \ S 7 . 3 )$ does nicely: Be sure to have chosen a comparison function whose indefinite integral is known analytically, and is also analytically invertible to give $x$ as a function of “area under the comparison function to the left of $x$ .” Now pick a uniform deviate between 0 and $A$ , where $A$ is the total area under $f ( x )$ , and use it to get a corresponding $x$ . Then pick a uniform deviate between 0 and $f ( x )$ as the $y$ value for the two-dimensional point. Finally, accept or reject according to whether it is respectively less than or greater than $p ( x )$ .

So, to summarize, the rejection method for some given $p ( x )$ requires that one find, once and for all, some reasonably good comparison function $f ( x )$ . Thereafter, each deviate generated requires two uniform random deviates, one evaluation of $f$ (to get the coordinate $y$ ) and one evaluation of $p$ (to decide whether to accept or reject the point $x , y )$ . Figure 7.3.1 illustrates the whole process. Then, of course, this process may need to be repeated, on the average, $A$ times before the final deviate is obtained.

# 7.3.7 Cauchy Deviates

The “further trick” described following equation (7.3.14) in the context of the Box-Muller method is now seen to be a rejection method for getting trigonometric functions of a uniformly random angle. If we combine this with the explicit formula, equation (6.14.6), for the inverse cdf of the Cauchy distribution (see $\ S 6 . 1 4 . 2 )$ , we can generate Cauchy deviates quite efficiently.

# struct Cauchydev : Ran {

Structure for Cauchy deviates. Doub mu,sig; Cauchydev(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig) {} Constructor arguments are $\mu$ , $\sigma$ , and a random sequence seed. Doub dev() { Return a Cauchy deviate. Doub v1,v2; do { Find a random point in the unit semicircle. $\scriptstyle \mathtt { v 1 } = 2$ .0\*doub()-1.0; $\mathtt { v } 2 =$ doub(); } while (SQR(v1)+SQR(v2) $> = ~ 1$ . || $\mathrm { v } 2 \ \mathrm { = } \ 0 . )$ ; return mu $^ +$ sig\*v1/v2; Ratio of its coordinates is the tangent of a } random angle.   
};

# 7.3.8 Ratio-of-Uniforms Method

In finding Cauchy deviates, we took the ratio of two uniform deviates chosen to lie within the unit circle. If we generalize to shapes other than the unit circle, and combine it with the principle of the rejection method, a powerful variant emerges. Kinderman and Monahan [1] showed that deviates of virtually any probability distribution $p ( x )$ can be generated by the following rather amazing prescription:

- Construct the region in the $( u , v )$ plane bounded by $0 \leq u \leq [ p ( v / u ) ] ^ { 1 / 2 }$ .   
- Choose two deviates, $u$ and $v$ , that lie uniformly in this region.   
- Return $v / u$ as the deviate.

Proof: We can represent the ordinary rejection method by the equation in the $( x , p )$ plane,

$$
p ( x ) d x = \int _ { p ^ { \prime } = 0 } ^ { p ^ { \prime } = p ( x ) } d p ^ { \prime } d x
$$

Since the integrand is 1, we are justified in sampling uniformly in $( x , p ^ { \prime } )$ as long as $p ^ { \prime }$ is within the limits of the integral (that is, $0 < p ^ { \prime } < p ( x ) )$ . Now make the change of variable

$$
\begin{array} { c } { { \frac { v } { u } = x } } \\ { { u ^ { 2 } = p } } \end{array}
$$

![](images/254c323f805148e7f7de3807ac2ddd1569c822d606e2afd039177c2eb42979e2.jpg)  
Figure 7.3.3. Ratio-of-uniforms method. The interior of this teardrop shape is the acceptance region for the normal distribution: If a random point is chosen inside this region, then the ratio $v / u$ will be a normal deviate.

Then equation (7.3.18) becomes

$$
p ( x ) d x = \int _ { p ^ { \prime } = 0 } ^ { p ^ { \prime } = p ( x ) } d p ^ { \prime } d x = \int _ { u = 0 } ^ { u = \sqrt { p ( x ) } } \frac { \partial ( p , x ) } { \partial ( u , v ) } d u d v = 2 \int _ { u = 0 } ^ { u = \sqrt { p ( v / u ) } } d u d v
$$

because (as you can work out) the Jacobian determinant is the constant 2. Since the new integrand is constant, uniform sampling in $( u , v )$ with the limits indicated for $u$ is equivalent to the rejection method in $( x , p )$ .

The above limits on $u$ very often define a region that is “teardrop” shaped. To see why, note that the locii of constant $x = v / u$ are radial lines. Along each radial, the acceptance region goes from the origin to a point where $u ^ { 2 } = p ( x )$ . Since most probability distributions go to zero for both large and small $x$ , the acceptance region accordingly shrinks toward the origin along radials, producing a teardrop. Of course, it is the exact shape of this teardrop that matters. Figure 7.3.3 shows the shape of the acceptance region for the case of the normal distribution.

Typically this ratio-of-uniforms method is used when the desired region can be closely bounded by a rectangle, parallelogram, or some other shape that is easy to sample uniformly. Then, we go from sampling the easy shape to sampling the desired region by rejection of points outside the desired region.

An important adjunct to the ratio-of-uniforms method is the idea of a squeeze. A squeeze is any easy-to-compute shape that tightly bounds the region of acceptance of a rejection method, either from the inside or from the outside. Best of all is when you have squeezes on both sides. Then you can immediately reject points that are outside the outer squeeze and immediately accept points that are inside the inner squeeze. Only when you have the bad luck of drawing a point between the two squeezes do you actually have to do the more lengthy computation of comparing with the actual rejection boundary. Squeezes are useful both in the ordinary rejection method and in the ratio-of-uniforms method.

# 7.3.9 Normal Deviates by Ratio-of-Uniforms

Leva [2] has given an algorithm for normal deviates that uses the ratio-of-uniforms method with great success. He uses quadratic curves to provide both inner and outer squeezes that hug the desired region in the $( u , v )$ plane (Figure 7.3.3). Only about $1 \%$ of the time is it necessary to calculate an exact boundary (requiring a logarithm).

The resulting code looks so simple and “un-transcendental” that it may be hard to believe that exact normal deviates are generated. But they are!

struct Normaldev : Ran {   
Structure for normal deviates. Doub mu,sig; Normaldev(Doub mmu, Doub ssig, Ullong i) : Ran(i), mu(mmu), sig(ssig){} Constructor arguments are $\mu , \sigma$ , and a random sequence seed. Doub dev() { Return a normal deviate. Doub u,v,x,y,q; do { $u \ =$ doub(); $\qquad \mathtt { v } =$ 1.7156\*(doub()-0.5); x = u - 0.449871; $\mathtt { y } =$ abs(v) $^ +$ 0.386595; q = SQR(x) $^ +$ y\*(0.19600\*y-0.25472\*x); while (q > 0.27597 && (q $>$ 0.27846 || SQR(v) > -4.\*log(u)\*SQR(u))); return mu $^ +$ sig\*v/u; }   
};

Note that the while clause makes use of C’s (and $\mathrm { C } { + + }$ ’s) guarantee that logical expressions are evaluated conditionally: If the first operand is sufficient to determine the outcome, the second is not evaluated at all. With these rules, the logarithm is evaluated only when q is between 0:27597 and 0:27846.

On average, each normal deviate uses 2.74 uniform deviates. By the way, even though the various constants are given only to six digits, the method is exact (to full double precision). Small perturbations of the bounding curves are of no consequence. The accuracy is implicit in the (rare) evaluations of the exact boundary.

# 7.3.10 Gamma Deviates

The distribution $\mathrm { G a m m a } ( \alpha , \beta )$ was described in $\ S 6 . 1 4 . 9$ . The $\beta$ parameter enters only as a scaling,

$$
\mathrm { G a m m a } ( \alpha , \beta ) \cong \frac { 1 } { \beta } \mathrm { G a m m a } ( \alpha , 1 )
$$

(Translation: To generate a $\mathrm { G a m m a } ( \alpha , \beta )$ deviate, generate a $\mathrm { G a m m a } ( \alpha , 1 )$ deviate and divide it by $\beta$ .)

If $\alpha$ is a small positive integer, a fast way to generate $x \sim \mathrm { G a m m a } ( \alpha , 1 )$ is to use the fact that it is distributed as the waiting time to the $\alpha$ th event in a Poisson random process of unit mean. Since the time between two consecutive events is just the exponential distribution Exponential .1/, you can simply add up $\alpha$ exponentially distributed waiting times, i.e., logarithms of uniform deviates. Even better, since the sum of logarithms is the logarithm of the product, you really only have to compute the product of $a$ uniform deviates and then take the log. Because this is such a special case, however, we don’t include it in the code below.

When $\alpha < 1$ , the gamma distribution’s density function is not bounded, which is inconvenient. However, it turns out [4] that if

$$
y \sim \mathrm { G a m m a } ( \alpha + 1 , 1 ) , \qquad u \sim \mathrm { U n i f o r m } ( 0 , 1 )
$$

then

$$
y u ^ { 1 / \alpha } \sim \mathrm { G a m m a } ( \alpha , 1 )
$$

We will use this in the code below.

For $\alpha > 1$ , Marsaglia and Tsang [5] give an elegant rejection method based on a simple transformation of the gamma distribution combined with a squeeze. After transformation, the gamma distribution can be bounded by a Gaussian curve whose area is never more than $5 \%$ greater than that of the gamma curve. The cost of a gamma deviate is thus only a little more than the cost of the normal deviate that is used to sample the comparison function. The following code gives the precise formulation; see the original paper for a full explanation.

# struct Gammadev : Normaldev {

Structure for gamma deviates.

Doub alph, oalph, bet; Doub a1,a2; Gammadev(Doub aalph, Doub bbet, Ullong i) : Normaldev $( 0 . , 1 . , \mathrm { i } )$ , alph(aalph), oalph(aalph), bet(bbet) { Constructor arguments are $\pmb { \alpha }$ , $\beta$ , and a random sequence seed. if (alph $< = ~ 0 .$ ) throw("bad alph in Gammadev"); if (alph $< ~ 1 .$ ) alph $+ = \textit { 1 } .$ ; a1 $=$ alph-1./3.; $\mathsf { a } 2 \ = \ 1$ ./sqrt(9.\*a1); } Doub dev() { Return a gamma deviate by the method of Marsaglia and Tsang. Doub u,v,x; do { do { $_ { \textrm { x } } =$ Normaldev::dev(); $\ l { \textsc { v } } = \ l { \textsc { 1 } }$ . + a2\*x; } while $\mathit { \Pi } _ { \mathbf { v } } \ < = \ 0 . )$ ; $\mathrm { ~ v ~ } = \mathrm { ~ v * v * v } ;$ $u \ =$ doub(); } while $\texttt { u } > 1$ . - 0.331 $^ *$ SQR(SQR(x)) && log(u) $>$ 0.5\*SQR(x) $^ +$ a1\*(1.-v+log(v))); Rarely evaluated. if (alph $= =$ oalph) return a1\*v/bet; else { Case where $\alpha < 1$ , per Ripley. do $\mathbf { u } =$ doub(); while $\mathrm {  ~ u ~ } = = 0 .$ ); return pow(u,1./oalph)\*a1\*v/bet; } } };

There exists a sum rule for gamma deviates. If we have a set of independent deviates $y _ { i }$ with possibly different $\alpha _ { i }$ ’s, but sharing a common value of $\beta$ ,

$$
y _ { i } \sim \mathrm { G a m m a } ( \alpha _ { i } , \beta )
$$

then their sum is also a gamma deviate,

$$
y \equiv \sum _ { i } y _ { i } \sim \mathrm { G a m m a } ( \alpha _ { T } , \beta ) , \qquad \alpha _ { T } = \sum _ { i } \alpha _ { i }
$$

If the $\alpha _ { i }$ ’s are integers, you can see how this relates to the discussion of Poisson waiting times above.

# 7.3.11 Distributions Easily Generated by Other Deviates

From normal, gamma and uniform deviates, we get a bunch of other distributions for free. Important: When you are going to combine their results, be sure that all distinct instances of Normaldist, Gammadist, and Ran have different random seeds! (Ran and its derived classes are sufficiently robust that seeds $i , i + 1 , \ldots$ are fine.)

# Chi-Square Deviates (cf. -6.14.8)

This one is easy:

$$
\mathrm { C h i s q u a r e } ( \nu ) \cong \mathrm { G a m m a } \Big ( \frac { \nu } { 2 } , \frac { 1 } { 2 } \Big ) \cong 2 \mathrm { G a m m a } \Big ( \frac { \nu } { 2 } , 1 \Big )
$$

# Student-t Deviates (cf. -6.14.3)

Deviates from the Student-t distribution can be generated by a method very similar to the Box-Muller method. The analog of equation (7.3.12) is

$$
y = \sqrt { \nu ( u _ { 1 } ^ { - 2 / \nu } - 1 ) } \cos { 2 \pi u _ { 2 } }
$$

If $u _ { 1 }$ and $u _ { 2 }$ are independently uniform, $\mathbf { U } ( 0 , 1 )$ , then

$$
y \sim \mathrm { S t u d e n t } ( \nu , 0 , 1 )
$$

or

$$
\mu + \sigma y \sim \mathrm { S t u d e n t } ( \nu , \mu , \sigma )
$$

Unfortunately, you can’t do the Box-Muller trick of getting two deviates at a time, because the Jacobian determinant analogous to equation (7.3.14) does not factorize. You might want to use the polar method anyway, just to get cos $2 \pi u _ { 2 }$ , but its advantage is now not so large.

An alternative method uses the quotients of normal and gamma deviates. If we have

$$
x \sim \mathrm { N } ( 0 , 1 ) , \qquad y \sim \mathrm { G a m m a } \Big ( \frac { \nu } { 2 } , \frac { 1 } { 2 } \Big )
$$

then

$$
x \sqrt { \nu / y } \sim \mathrm { S t u d e n t } ( \nu , 0 , 1 )
$$

Beta Deviates (cf. -6.14.11)

If

$$
x \sim \operatorname { G a m m a } ( \alpha , 1 ) , \qquad y \sim \operatorname { G a m m a } ( \beta , 1 )
$$

then

$$
\frac { x } { x + y } \sim \operatorname { B e t a } ( \alpha , \beta )
$$

# F-Distribution Deviates (cf. -6.14.10)

If

$$
\begin{array} { r } { x \sim \mathrm { B e t a } ( \frac { 1 } { 2 } \nu _ { 1 } , \frac { 1 } { 2 } \nu _ { 2 } ) } \end{array}
$$

(see equation 7.3.33), then

$$
\frac { \nu _ { 2 } x } { \nu _ { 1 } ( 1 - x ) } \sim \mathrm { F } ( \nu _ { 1 } , \nu _ { 2 } )
$$

![](images/4462aa9a4a983a6ea4e9de77058ac7a346c9b9d615d9f3dd944c0a604de04c48.jpg)  
Figure 7.3.4. Rejection method as applied to an integer-valued distribution. The method is performed on the step function shown as a dashed line, yielding a real-valued deviate. This deviate is rounded down to the next lower integer, which is output.

# 7.3.12 Poisson Deviates

The Poisson distribution, Poisson $( \lambda )$ , previously discussed in $\ S 6 . 1 4 . 1 3$ , is a discrete distribution, so its deviates will be integers, $k$ . To use the methods already discussed, it is convenient to convert the Poisson distribution into a continuous distribution by the following trick: Consider the finite probability $p ( k )$ as being spread out uniformly into the interval from $k$ to $k + 1$ . This defines a continuous distribution $q _ { \lambda } ( k ) d k$ given by

$$
q _ { \lambda } ( k ) d k = \frac { \lambda ^ { \lfloor k \rfloor } e ^ { - \lambda } } { \lfloor k \rfloor ! } d k
$$

where $\lfloor k \rfloor$ represents the largest integer $\leq k$ . If we now use a rejection method, or any other method, to generate a (noninteger) deviate from (7.3.36), and then take the integer part of that deviate, it will be as if drawn from the discrete Poisson distribution. (See Figure 7.3.4.) This trick is general for any integer-valued probability distribution. Instead of the “floor” operator, one can equally well use “ceiling” or “nearest” — anything that spreads the probability over a unit interval.

For $\lambda$ large enough, the distribution (7.3.36) is qualitatively bell-shaped (albeit with a bell made out of small, square steps). In that case, the ratio-of-uniforms method works well. It is not hard to find simple inner and outer squeezes in the $( u , v )$ plane of the form $v ^ { 2 } = Q ( u )$ , where $Q ( u )$ is a simple polynomial in $u$ . The only trick is to allow a big enough gap between the squeezes to enclose the true, jagged, boundaries for all values of $\lambda$ . (Look ahead to Figure 7.3.5 for a similar example.)

For intermediate values of $\lambda$ , the jaggedness is so large as to render squeezes impractical, but the ratio-of-uniforms method, unadorned, still works pretty well.

For small $\lambda$ , we can use an idea similar to that mentioned above for the gamma distribution in the case of integer $a$ . When the sum of independent exponential deviates first exceeds $\lambda$ , their number (less 1) is a Poisson deviate $k$ . Also, as explained for the gamma distribution, we can multiply uniform deviates from $\mathrm { U } ( 0 , 1 )$ instead of adding deviates from Exponential .1/.

These ideas produce the following routine.

ct Poissondev : Ran {   
cture for Poisson deviates.   
Doub lambda, sqlam, loglam, lamexp, lambold;   
VecDoub logfact;   
Int swch;   
Poissondev(Doub llambda, Ullong i) : Ran(i), lambda(llambda), logfact(1024,-1.), lambold(-1.) {}   
Constructor arguments are  and a random sequence seed.   
Int dev()   
Return a Poisson deviate using the most recently set value of . Doub u,u2,v,v2,p,t,lfac; Int k; if (lambda $< ~ 5 .$ ) { Will use product of uniforms method if (lambda $\downarrow =$ lambold) lamexp $\mid =$ exp(-lambda); $\mathrm { ~ k ~ } = \mathrm { ~ - 1 ~ }$ ; t=1.; do { ++k; t $\ast =$ doub(); } while (t > lamexp); } else { Will use ratio-of-uniforms method. if (lambda $\downarrow =$ lambold) { sqlam $=$ sqrt(lambda); loglam $=$ log(lambda); for (;;) { $\mathrm { ~ \textbar ~ { ~ u ~ } ~ } =$ 0.64\*doub(); v = -0.68 $^ +$ 1.28\*doub(); if (lambda $>$ 13.5) { Outer squeeze for fast rejection. $\quad \mathtt { v } 2 =$ SQR(v); if ( $\mathrm {  ~ v ~ } > = \mathrm {  ~ 0 ~ }$ .) {if $( \mathtt { v } 2 \ > \ 6 . 5 * \mathtt { u } * ( 0 . 6 4 \mathrm { - } \mathtt { u } ) * ( \mathtt { u } + 0 . 2 )$ ) continue;} else {if $( \nu 2 \ > \ 9 . 6 { \ast } { \mu } * ( 0 . 6 6 { - \mu } ) * ( \mu + 0 . 0 7 ) )$ continue;} } $\mathrm { ~ \bf ~ k ~ } =$ Int(floor(sqlam\*(v/u)+lambda+0.5)); if (k < 0) continue; u2 $=$ SQR(u); if (lambda $>$ 13.5) { Inner squeeze for fast acceptance. if ( $\mathrm {  ~ v ~ } > = \mathrm {  ~ 0 ~ }$ .) {if $( \mathrm { v } 2 ~ < ~ 1 5 . 2 { * } \mathrm { u } 2 { * } ( 0 . 6 1 \mathrm { - } \mathrm { u } ) { * } ( 0 . 8 \mathrm { - } \mathrm { u } ) )$ ) break;} else {if $( \mathrm { v } 2 ~ < ~ 6 . 7 6 * \mathrm { u } 2 * ( 0 . 6 2 \mathrm { - u } ) * ( 1 . 4 \mathrm { - u } )$ ) break;} } if $( \mathrm { ~ k ~ } < \mathrm { ~ } 1 0 2 4 )$ { if (logfact[k] < 0.) logfact[k] $=$ gammln(k+1.); lfac $=$ logfact[k]; } else lfac $=$ gammln(k+1.); $\mathtt { p } \ =$ sqlam\*exp(-lambda $^ +$ k\*loglam - lfac); Only when we must. if $\mathtt { . u 2 } < \mathtt { p } )$ break; } lambold $=$ lambda; return k;   
Int dev(Doub llambda) {   
Reset  and then return a Poisson deviate. lambda $=$ llambda; return dev();

![](images/8935ba798ee6987b47fdd2776be2e58e9bf81868a8338b3aba7936676d732b34.jpg)  
Figure 7.3.5. Ratio-of-uniforms method as applied to the generation of binomial deviates. Points are chosen randomly in the $( u , v )$ -plane. The smooth curves are inner and outer squeezes. The jagged curves correspond to various binomial distributions with $n > 6 4$ and $n p > 3 0$ . An evaluation of the binomial probability is required only when the random point falls between the smooth curves.

In the regime $\lambda > 1 3 . 5$ , the above code uses about 3:3 uniform deviates per output Poisson deviate and does 0:4 evaluations of the exact probability (costing an exponential and, for large $k$ , a call to gammln).

Poissondev is slightly faster if you draw many deviates with the same value $\lambda$ , using the dev function with no arguments, than if you vary $\lambda$ on each call, using the one-argument overloaded form of dev (which is provided for just that purpose). The difference is just an extra exponential $\lambda < 5$ ) or square root and logarithm $\lambda \geq 5$ ). Note also the object’s table of previously computed log-factorials. If your $\lambda$ ’s are as large as $\sim 1 0 ^ { 3 }$ , you might want to make the table larger.

# 7.3.13 Binomial Deviates

The generation of binomial deviates $k \ \sim \ \mathrm { B i n o m i a l } ( n , p )$ involves many of the same ideas as for Poisson deviates. The distribution is again integer-valued, so we use the same trick to convert it into a stepped continuous distribution. We can always restrict attention to the case $p \leq 0 . 5$ , since the distribution’s symmetries let us trivially recover the case $p > 0 . 5$ .

When $n > 6 4$ and $n p > 3 0$ , we use the ratio-of-uniforms method, with squeezes shown in Figure 7.3.5. The cost is about 3:2 uniform deviates, plus 0:4 evaluations of the exact probability, per binomial deviate.

It would be foolish to waste much thought on the case where $n \ > \ 6 4$ and $n p < 3 0$ , because it is so easy simply to tabulate the cdf, say for $0 \leq k < 6 4$ , and then loop over $k$ ’s until the right one is found. (A bisection search, implemented below, is even better.) With a cdf table of length 64, the neglected probability at the end of the table is never larger than $\sim 1 0 ^ { - 2 0 }$ . (At $1 0 ^ { 9 }$ deviates per second, you could run 3000 years before losing a deviate.)

What is left is the interesting case $n < 6 4$ , which we will explore in some detail, because it demonstrates the important concept of bit-parallel random comparison.

Analogous to the methods for gamma deviates with small integer $a$ and for Poisson deviates with small $\lambda$ , is this direct method for binomial deviates: Generate $n$ uniform deviates in $\mathrm { U } ( 0 , 1 )$ . Count the number of them $< p$ . Return the count as $k \sim \mathrm { B i n o m i a l } ( n , p )$ . Indeed this is essentially the definition of a binomial process!

The problem with the direct method is that it seems to require $n$ uniform deviates, even when the mean value of $k$ is much smaller. Would you be surprised if we told you that for $n \leq 6 4$ you can achieve the same goal with at most seven 64-bit uniform deviates, on average? Here is how.

Expand $p < 1$ into its first 5 bits, plus a residual,

$$
p = b _ { 1 } 2 ^ { - 1 } + b _ { 2 } 2 ^ { - 2 } + \cdots + b _ { 5 } 2 ^ { - 5 } + p _ { r } 2 ^ { - 5 }
$$

where each $b _ { i }$ is 0 or 1, and $0 \leq p _ { r } \leq 1$ .

Now imagine that you have generated and stored 64 uniform $\mathbf { U } ( 0 , 1 )$ deviates, and that the 64-bit word $P$ displays just the first bit of each of the 64. Compare each bit of $P$ to $b _ { 1 }$ . If the bits are the same, then we don’t yet know whether that uniform deviate is less than or greater than $p$ . But if the bits are different, then we know that the generator is less than $p$ (in the case that $b _ { 1 } = 1$ ) or greater than $p$ (in the case that $b _ { 1 } = 0 \}$ ). If we keep a mask of “known” versus “unknown” cases, we can do these comparisons in a bit-parallel manner by bitwise logical operations (see code below to learn how). Now move on to the second bit, $b _ { 2 }$ , in the same way. At each stage we change half the remaining unknowns to knowns. After five stages (for $n = 6 4 .$ ) there will be two remaining unknowns, on average, each of which we finish off by generating a new uniform and comparing it to $p _ { r }$ . (This requires a loop through the 64 bits; but since $\mathrm { C } { + } { + }$ has no bitwise “popcount” operation, we are stuck doing such a loop anyway. If you can do popcounts, you may be better off just doing more stages until the unknowns mask is zero.)

The trick is that the bits used in the five stages are not actually the leading five bits of 64 generators, they are just five independent 64-bit random integers. The number five was chosen because it minimizes $\overline { { 6 4 } } \times 2 ^ { - j } + j$ , the expected number of deviates needed.

So, the code for binomial deviates ends up with three separate methods: bitparallel direct, cdf lookup (by bisection), and squeezed ratio-of-uniforms.

truct Binomialdev : Ran {   
tructure for binomial deviates. Doub pp,p,pb,expnp,np,glnp,plog,pclog,sq; Int n,swch; Ullong uz,uo,unfin,diff,rltp; Int pbits[5]; Doub cdf[64]; Doub logfact[1024]; Binomialdev(Int nn, Doub ppp, Ullong i) : Ran(i), pp(ppp), n(nn) { Constructor arguments are $_ n$ , $p$ , and a random sequence seed. Int j; pb $= \mathrm { ~ p ~ } = \mathrm { ~ ( p p ~ } < = \mathrm { ~ 0 ~ . 5 ~ : ~ } \mathrm { ~ p p ~ } : \mathrm { ~ 1 ~ . 0 \mathrm { - p p } ) ~ } ;$ if $( \mathrm { ~ n ~ } < = \ 6 4 )$ ) { Will use bit-parallel direct method. $\mathtt { u } z = 0$ ; uo $=$ 0xffffffffffffffffLL; $\tt r l t p = 0$ ; for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<5;j++) pbits[j] = 1 & ((Int)(pb \*= 2.)); pb $- =$ floor(pb); Leading bits of $p$ (above) and remaining swch $\mathit { \Theta } = \mathit { \Theta } 0$ ; fraction. } else if $( \mathtt { n } * \mathtt { p } \ < \ 3 0 .$ ) { Will use precomputed cdf table. cdf[0] $=$ exp(n\*log(1-p)); for ( $\mathrm { j } = 1$ ;j<64;j++) cdf[j] $=$ cdf[j-1] $^ +$ exp(gammln $( \mathtt { n } + 1$ .) -gammln(j+1.)-gammln(n-j+1.)+j\*log(p)+(n-j)\*log(1.-p)); swch $\ c = ~ 1$ ;   
} else { Will use ratio-of-uniforms method. np = n\*p; glnp=gammln(n+1.); plog=log(p); pclog=log(1.-p); sq=sqrt(np\*(1.-p)); if (n $<$ 1024) for ( $\scriptstyle \mathrm { j = 0 }$ ;j $< = \mathtt { n }$ ;j++) logfact[j] $=$ gammln(j+1.); swch $= ~ 2$ ;   
}   
dev() {   
turn a binomial deviate.   
Int j,k,kl,km;   
Doub y,u,v,u2,v2,b;   
if (swch $\scriptstyle = = 0$ ) { unfin $=$ uo; Mark all bits as ”unfinished.” for (j ${ = } 0$ ;j<5;j++) { Compare with first five bits of $p$ diff $=$ unfin & (int64()^(pbits[j]? uo : uz)); Mask of diff. if (pbits[j]) rltp $| =$ diff; Set bits to 1, meaning ran $< p$ . else rltp $=$ rltp & \~diff; Set bits to 0, meaning ran $> p$ . unfin $=$ unfin & \~diff; Update unfinished status. } $\mathtt { k } = 0$ ; Now we just count the events. for (j ${ = } 0$ ;j<n;j++) { if (unfin & 1) {if (doub() $<$ pb) $+ + \mathrm { k } ; \}$ Clean up unresolved ca else {if (rltp & 1) ++k;} or use bit answer. unfin $> > = ~ 1$ ; rltp >>= 1;   
} else if (swch $\scriptstyle \mathbf { \mu = } \mathbf { \mu 1 }$ ) { Use stored cdf. $\mathrm { ~ y ~ } =$ doub(); $\mathbf { k } \mathbf { 1 } ~ = ~ - 1$ ; $\mathrm { ~ k ~ } = \ 6 4$ ; while (k-kl>1) { $\begin{array} { r l } { \mathrm { k m } } & { { } = \begin{array} { r l } { \left( \mathrm { k } \mathrm { 1 } { + } \mathrm { k } \right) / 2 \ } \end{array} } \end{array}$ ; if (y $<$ cdf[km]) $\texttt { k } = \texttt { k m }$ ; else $\mathtt { k 1 } \ = \ \mathtt { k m }$ ; }   
} else { Use ratio-of-uniforms method. for (;;) { $\mathrm { ~ \tt ~ u ~ } = \mathrm { ~ 0 ~ }$ .645\*doub(); v = -0.63 $^ +$ 1.25\*doub(); $\mathrm { v } 2 \ = \ \mathrm { S Q R } ( \mathrm { v } )$ ; Try squeeze for fast rejection: if $\begin{array} { r } { \mathrm { ~  ~ \omega ~ } } \\ { \nabla \mathrm { ~  ~ \omega ~ } } \end{array} > = \mathrm { ~  ~ 0 ~ } .$ ) {if $( \mathtt { v } 2 \ > \ 6 . 5 * \mathtt { u } * ( 0 . 6 4 5 \mathtt { - u } ) * ( \mathtt { u } + 0 . 2 )$ ) continue;} else {if $( \mathrm { v } 2 ) 8 . 4 \ast \mathrm { u } \ast ( 0 . 6 4 5 \mathrm { - u } ) \ast ( \mathrm { u } + 0 . 1 ) ^ { \cdot }$ ) continue;} $\mathrm { ~ \bf ~ k ~ } =$ Int(floor $( \mathtt { s q } \ast ( \mathtt { v } / \mathtt { u } ) + \mathtt { n p } + 0 . 5 ) )$ ; if $\mathrm { ~ ( ~ k ~ < ~ } 0 \mathrm { ~ ) ~ }$ ) continue; $\tt { u } 2 \ =$ SQR(u); Try squeeze for fast acceptance: if $\begin{array} { r } { \check { \mathbf { \Xi } } _ { \mathbb { V } } \ > = \ 0 . } \end{array}$ ) {if $( \nu 2 ~ < ~ 1 2 . 2 5 * \mathrm { u } 2 * ( 0 . 6 1 5 \mathrm { - u } ) * ( 0 . 9 2 \mathrm { - u } ) ^ { } )$ ) break;} else {if $( \mathtt { v } 2 ~ < ~ 7 . 8 4 \mathtt { * u } 2 \mathtt { * } ( 0 . 6 1 5 \mathtt { - u } ) \mathtt { * } ( 1 . 2 \mathtt { - u } )$ ) break;} b $=$ sq\*exp(glnp+k\*plog+(n-k)\*pclog Only when we must. - (n < 1024 ? logfact[k]+logfact[n-k] : gammln(k+1.)+gammln(n-k+1.))); if (u2 < b) break; }   
}   
if (p != pp) k = n - k;   
return k;

If you are in a situation where you are drawing only one or a few deviates each for many different values of $n$ and/or $p$ , you’ll need to restructure the code so that $n$ and $p$ can be changed without creating a new instance of the object and without reinitializing the underlying Ran generator.

# 7.3.14 When You Need Greater Speed

In particular situations you can cut some corners to gain greater speed. Here are some suggestions.

- All of the algorithms in this section can be speeded up significantly by using Ranq1 in $\ S 7 . 1$ instead of Ran. We know of no reason not to do this. You can gain some further speed by coding Ranq1’s algorithm inline, thus eliminating the function calls.   
- If you are using Poissondev or Binomialdev with large values of $\lambda$ or $n$ , then the above codes revert to calling gammln, which is slow. You can instead increase the length of the stored tables.   
- For Poisson deviates with $\lambda < 2 0$ , you may want to use a stored table of cdfs combined with bisection to find the value of $k$ . The code in Binomialdev shows how to do this.   
- If your need is for binomial deviates with small $n$ , you can easily modify the code in Binomialdev to get multiple deviates $( \sim 6 4 / n$ , in fact) from each execution of the bit-parallel code.   
Do you need exact deviates, or would an approximation do? If your distribution of interest can be approximated by a normal distribution, consider substituting Normaldev, above, especially if you also code the uniform random generation inline.   
If you sum exactly 12 uniform deviates $U ( 0 , 1 )$ and then subtract 6, you get a pretty good approximation of a normal deviate $N ( 0 , 1 )$ . This is definitely slower then Normaldev (not to mention less accurate) on a general-purpose CPU. However, there are reported to be some special-purpose signal processing chips in which all the operations can be done with integer arithmetic and in parallel.

See Gentle [3], Ripley [4], Devroye [6], Bratley [7], and Knuth [8] for many additional algorithms.

# CITED REFERENCES AND FURTHER READING:

Kinderman, A.J. and Monahan, J.F 1977, “Computer Generation of Random Variables Using the Ratio of Uniform Deviates,” ACM Transactions on Mathematical Software, vol. 3, pp. 257– 260.[1]   
Leva, J.L. 1992. “A Fast Normal Random Number Generator,” ACM Transactions on Mathematical Software,vol.18, no.4, pp. 449-453.[2]   
Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer), Chapters 4–5.[3]   
Ripley, B.D. 1987, Stochastic Simulation (New York: Wiley).[4]   
Marsaglia, G. and Tsang W-W. 2000, “A Simple Method for Generating Gamma Variables,” ACM Transactions on Mathematical Software,vol.26,no.3,pp.363-372.[5]   
Devroye, L. 1986, Non-Uniform Random Variate Generation (New York: Springer).[6]   
Bratley, P., Fox, B.L., and Schrage, E.L. 1983, A Guide to Simulation, 2nd ed. (New York: Springer).[7].   
Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading, MA: Addison-Wesley),pp.125ff.[8]

# 7.4 Multivariate Normal Deviates

A multivariate random deviate of dimension $M$ is a point in $M$ -dimensional space. Its coordinates are a vector, each of whose $M$ components are random — but not, in general, independently so, or identically distributed. The special case of multivariate normal deviates is defined by the multidimensional Gaussian density function

$$
N ( { \bf x } \mid { \pmb \mu } , { \pmb \Sigma } ) = \frac { 1 } { ( 2 \pi ) ^ { M / 2 } \operatorname* { d e t } ( { \pmb \Sigma } ) ^ { 1 / 2 } } \exp [ - \frac { 1 } { 2 } ( { \bf x } - { \pmb \mu } ) \cdot { \pmb \Sigma } ^ { - 1 } \cdot ( { \bf x } - { \pmb \mu } ) ]
$$

where the parameter $\pmb { \mu }$ is a vector that is the mean of the distribution, and the parameter $\pmb { \Sigma }$ is a symmetrical, positive-definite matrix that is the distribution’s covariance.

There is a quite general way to construct a vector deviate $\mathbf { X }$ with a specified covariance $\pmb { \Sigma }$ and mean $\pmb { \mu }$ , starting with a vector $\mathbf { y }$ of independent random deviates of zero mean and unit variance: First, use Cholesky decomposition (-2.9) to factor $\pmb { \Sigma }$ into a left triangular matrix $\mathbf { L }$ times its transpose,

$$
\boldsymbol { \Sigma } = \mathbf { L } \mathbf { L } ^ { T }
$$

This is always possible because $\pmb { \Sigma }$ is positive-definite, and you need do it only once for each distinct $\pmb { \Sigma }$ of interest. Next, whenever you want a new deviate $\mathbf { X }$ , fill $\mathbf { y }$ with independent deviates of unit variance and then construct

$$
\mathbf { x } = \mathbf { L y } + \pmb { \mu }
$$

The proof is straightforward, with angle brackets denoting expectation values: Since the components $y _ { i }$ are independent with unit variance, we have

$$
\langle \mathbf { y } \otimes \mathbf { y } \rangle = \mathbf { 1 }
$$

where 1 is the identity matrix. Then,

$$
{ \begin{array} { r l } & { \left. \left( \mathbf { x } - { \boldsymbol { \mu } } \right) \otimes ( \mathbf { x } - { \boldsymbol { \mu } } ) \right. = \left. \left( \mathbf { L y } \right) \otimes ( \mathbf { L y } ) \right. } \\ & { \qquad = \left. \mathbf { L } ( \mathbf { y } \otimes \mathbf { y } ) \mathbf { L } ^ { T } \right. = \mathbf { L } \left. \mathbf { y } \otimes \mathbf { y } \right. \mathbf { L } ^ { T } } \\ & { \qquad = \mathbf { L } \mathbf { L } ^ { T } = \Sigma } \end{array} }
$$

As general as this procedure is, it is, however, rarely useful for anything except multivariate normal deviates. The reason is that while the components of $\mathbf { X }$ indeed have the right mean and covariance structure, their detailed distribution is not anything “nice.” The $x _ { i }$ ’s are linear combinations of the $y _ { i }$ ’s, and, in general, a linear combination of random variables is distributed as a complicated convolution of their individual distributions.

For Gaussians, however, we do have “nice.” All linear combinations of normal deviates are themselves normally distributed, and completely defined by their mean and covariance structure. Thus, if we always fill the components of y with normal deviates,

$$
y _ { i } \sim \mathrm { N } ( 0 , 1 )
$$

then the deviate (7.4.3) will be distributed according to equation (7.4.1).

Implementation is straightforward, since the Cholesky structure both accomplishes the decomposition and provides a method for doing the matrix multiplication efficiently, taking advantage of $\mathbf { L }$ ’s triangular structure. The generation of normal deviates is inline for efficiency, identical to Normaldev in $\ S 7 . 3$ .

struct Multinormaldev : Ran {   
Structure for multivariate normal deviates. Int mm; VecDoub mean; MatDoub var; Cholesky chol; VecDoub spt, pt; Multinormaldev(Ullong j, VecDoub &mmean, MatDoub &vvar) :   
Ran(j), mm(mmean.size()), mean(mmean), var(vvar), chol(var),   
spt(mm), pt(mm) {   
Constructor. Arguments are the random generator seed, the (vector) mean, and the (matrix) covariance. Cholesky decomposition of the covariance is done here.   
if (var.ncols() $! = \ \mathrm { m m } \ \mathrm { ~ \left| ~ \right| ~ }$ var.nrows() $! = \mathrm { \ m m } .$ ) throw("bad sizes");   
}

# VecDoub &dev() {

Return a multivariate normal deviate. Int i; Doub u,v,x,y,q; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<mm;i++) { Fill a vector of independent normal deviates. do { $u \ =$ doub(); v = 1.7156\*(doub()-0.5); x = u - 0.449871; $y ~ =$ abs(v) $^ +$ 0.386595; ${ \textsc { q } } =$ SQR(x) + y\*(0.19600\*y-0.25472\*x); } while (q $>$ 0.27597 && (q $>$ 0.27846 || SQR(v) > -4.\*log(u)\*SQR(u))); spt[i] $\ l = \ l { \ v } / { \ u }$ ; } chol.elmult(spt,pt); Apply equation (7.4.3). for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<mm; $\dot { 1 } + + \dot { 1 }$ ) {pt[i] $+ =$ mean[i];} return pt;   
}

};

# 7.4.1 Decorrelating Multiple Random Variables

Although not directly related to the generation of random deviates, this is a convenient place to point out how Cholesky decomposition can be used in the reverse manner, namely to find linear combinations of correlated random variables that have no correlation. In this application we are given a vector $\mathbf { X }$ whose components have a known covariance $\pmb { \Sigma }$ and mean $\mu$ . Decomposing $\pmb { \Sigma }$ as in equation (7.4.2), we assert

that

$$
\mathbf { y } = \mathbf { L } ^ { - 1 } ( \mathbf { x } - \pmb { \mu } )
$$

has uncorrelated components, each of unit variance. Proof:

$$
\begin{array} { r l } & { \langle \mathbf { y } \otimes \mathbf { y } \rangle = \left. \left( \mathbf { L } ^ { - 1 } [ \mathbf { x } - \pmb { \mu } ] \right) \otimes \left( \mathbf { L } ^ { - 1 } [ \mathbf { x } - \pmb { \mu } ] \right) \right. } \\ & { \qquad = \mathbf { L } ^ { - 1 } \left. \left( \mathbf { x } - \pmb { \mu } \right) \otimes \left( \mathbf { x } - \pmb { \mu } \right) \right. \mathbf { L } ^ { - 1 T } } \\ & { \qquad = \mathbf { L } ^ { - 1 } \pmb { \Sigma } \mathbf { L } ^ { - 1 T } = \mathbf { L } ^ { - 1 } \mathbf { L } \mathbf { L } ^ { T } \mathbf { L } ^ { - 1 T } = \mathbf { 1 } } \end{array}
$$

Be aware that this linear combination is not unique. In fact, once you have obtained a vector $\mathbf { y }$ of uncorrelated components, you can perform any rotation on it and still have uncorrelated components. In particular, if $\mathbf { K }$ is an orthogonal matrix, so that

$$
\mathbf { K } ^ { T } \mathbf { K } = \mathbf { K } \mathbf { K } ^ { T } = \mathbf { 1 }
$$

then

$$
\left. \left( \mathbf { K } \mathbf { y } \right) \otimes \left( \mathbf { K } \mathbf { y } \right) \right. = \mathbf { K } \left. \mathbf { y } \otimes \mathbf { y } \right. \mathbf { K } ^ { T } = \mathbf { K } \mathbf { K } ^ { T } = \mathbf { 1 }
$$

A common (though slower) alternative to Cholesky decomposition is to use the Jacobi transformation (-11.1) to decompose $\pmb { \Sigma }$ as

$$
\pmb { \Sigma } = \mathbf { V } \mathrm { d i a g } ( \sigma _ { i } ^ { 2 } ) \mathbf { V } ^ { T }
$$

where $\mathbf { V }$ is the orthogonal matrix of eigenvectors, and the $\sigma _ { i }$ ’s are the standard deviations of the (new) uncorrelated variables. Then $\mathbf { V } \mathrm { d i a g } ( \sigma _ { i } )$ plays the role of $\mathbf { L }$ in the proofs above.

Section $\ S 1 6 . 1 . 1$ discusses some further applications of Cholesky decomposition relating to multivariate random variables.

# 7.5 Linear Feedback Shift Registers

A linear feedback shift register (LFSR) consists of a state vector and a certain kind of update rule. The state vector is often the set of bits in a 32- or 64-bit word, but it can sometimes be a set of words in an array. To qualify as an LFSR, the update rule must generate a linear combination of the bits (or words) in the current state, and then shift that result onto one end of the state vector. The oldest value, at the other end of the state vector, falls off and is gone. The output of an LFSR consists of the sequence of new bits (or words) as they are shifted in.

For single bits, “linear” means arithmetic modulo 2, which is the same as using the logical XOR operation for $^ +$ and the logical AND operation for $\times$ . It is convenient, however, to write equations using the arithmetic notation. So, for an LFSR of length $n$ , the words in the paragraph above translate to

$$
\begin{array} { l } { { \displaystyle a _ { 1 } ^ { \prime } = \left( \sum _ { j = 1 } ^ { n - 1 } c _ { j } a _ { j } \right) + a _ { n } } } \\ { { \displaystyle a _ { i } ^ { \prime } = a _ { i - 1 } , \qquad i = 2 , \ldots , n } } \end{array}
$$

![](images/e4eaea2a8eaf2691a3c60857dd45659d8840abd80a973d858ff79514516877f9.jpg)  
Figure 7.5.1. Two related methods for obtaining random bits from a shift register and a primitive polynomial modulo 2. (a) The contents of selected taps are combined by XOR (addition modulo 2), and the result is shifted in from the right. This method is easiest to implement in hardware. (b) Selected bits are modified by XOR with the leftmost bit, which is then shifted in from the right. This method is easiest to implement in software.

Here $\mathbf { a } ^ { \prime }$ is the new state vector, derived from a by the update rule as shown. The reason for singling out $a _ { n }$ in the first line above is that its coefficient $c _ { n }$ must be $\equiv 1$ . Otherwise, the LFSR wouldn’t be of length $n$ , but only of length up to the last nonzero coefficient in the $c _ { j }$ ’s.

There is also a reason for numbering the bits (henceforth we consider only the case of a vector of bits, not of words) starting with 1 rather than the more comfortable 0. The mathematical properties of equation (7.5.1) derive from the properties of the polynomials over the integers modulo 2. The polynomial associated with (7.5.1) is

$$
P ( x ) = x ^ { n } + c _ { n - 1 } x ^ { n - 1 } + \cdots + c _ { 2 } x ^ { 2 } + c _ { 1 } x + 1
$$

where each of the $c _ { i }$ ’s has the value 0 or 1. So, $c _ { 0 }$ , like $c _ { n }$ , exists but is implicitly $\equiv ~ 1$ . There are several notations for describing specific polynomials like (7.5.2). One is to simply list the values $i$ for which $c _ { i }$ is nonzero (by convention including $c _ { n }$ and $c _ { 0 }$ ). So the polynomial

$$
x ^ { 1 8 } + x ^ { 5 } + x ^ { 2 } + x + 1
$$

is abbreviated as

$$
( 1 8 , 5 , 2 , 1 , 0 )
$$

Another, when a value of $n$ (here 18), and $c _ { n } = c _ { 0 } = 1$ , is assumed, is to construct a “serial number” from the binary word $c _ { n - 1 } c _ { n - 1 } \cdot \cdot \cdot c _ { 2 } c _ { 1 }$ (by convention now excluding $c _ { n }$ and $c _ { 0 }$ ). For (7.5.3) this would be 19, that is, $2 ^ { 4 } + 2 ^ { 1 } + 2 ^ { 0 }$ . The nonzero $c _ { i }$ ’s are often referred to as an LFSR’s taps.

Figure 7.5.1(a) illustrates how the polynomial (7.5.3) and (7.5.4) looks as an update process on a register of 18 bits. Bit 0 is the temporary where a bit that is to become the new bit 1 is computed.

The maximum period of an LFSR of $n$ bits, before its output starts repeating, is $2 ^ { n } - 1$ . This is because the maximum number of distinct states is $2 ^ { n }$ , but the special vector with all bits zero simply repeats itself with period 1. If you pick a random polynomial $P ( x )$ , then the generator you construct will usually not be full-period. A fraction of polynomials over the integers modulo 2 are irreducible, meaning that they can’t be factored. A fraction of the irreducible polynomials are primitive, meaning that they generate maximum period LFSRs. For example, the polynomial $x ^ { 2 } + 1 =$ $( x + 1 ) ( x + 1 )$ is not irreducible, so it is not primitive. (Remember to do arithmetic on the coefficients mod 2.) The polynomial $x ^ { 4 } + x ^ { 3 } + x ^ { 2 } + x + 1$ is irreducible, but it turns out not to be primitive. The polynomial $x ^ { 4 } + x + 1$ is both irreducible and primitive.

Maximum period LFSRs are often used as sources of random bits in hardware devices, because logic like that shown in Figure 7.5.1(a) requires only a few gates and can be made to run extremely fast. There is not much of a niche for LFSRs in software applications, because implementing equation (7.5.1) in code requires at least two full-word logical operations for each nonzero $c _ { i }$ , and all this work produces a meager one bit of output. We call this “Method I.” A better software approach, “Method II,” is not obviously an LFSR at all, but it turns out to be mathematically equivalent to one. It is shown in Figure 7.5.1(b). In code, this is implemented from a primitive polynomial as follows:

Let maskp and maskn be two bit masks,

$$
\begin{array} { c c c c c c c c c c } { { \mathrm { m a s k p } \equiv } } & { { ( 0 } } & { { \cdots } } & { { 0 } } & { { c _ { n - 1 } } } & { { c _ { n - 2 } } } & { { \cdots } } & { { c _ { 2 } } } & { { c _ { 1 } } } \\ { { \mathrm { m a s k n } \equiv } } & { { ( 0 } } & { { \cdots } } & { { 1 } } & { { 0 } } & { { 0 } } & { { \cdots } } & { { 0 } } & { { 0 ) } } \end{array}
$$

Then, a word a is updated by

$$
\begin{array} { c c } { { \mathrm { i f } \quad ( \tt a \& m a s k n ) \quad \tt a \equiv \displaystyle ( ( a \mathrm { ~ \hat { ~ } { \theta ~ } { \theta ~ } { \theta ~ } { \theta ~ } ^ { \mathrm { { ~ \tiny ~ m a s k p } } } ) ~ \ll ~ 1 ) ~ } \mid 1 ; } } \\ { { \mathrm { e l s e ~ \tt ~ a ~ < < = ~ 1 ; } } } \end{array}
$$

You should work through the above prescription to see that it is identical to what is shown in the figure. The output of this update (still only one bit) can be taken as (a & maskn), or for that matter any fixed bit in a.

LFSRs (either Method I or Method II) are sometimes used to get random $m$ -bit words by concatenating the output bits from $m$ consecutive updates (or, equivalently for Method I, grabbing the low-order m bits of state after every $m$ updates). This is generally a bad idea, because the resulting words usually fail some standard statistical tests for randomness. It is especially a bad idea if $m$ and $2 ^ { n } - 1$ are not relatively prime, in which case the method does not even give all $m$ -bit words uniformly.

Next, we’ll develop a bit of theory to see the relation between Method I and Method II, and this will lead us to a routine for testing whether any given polynomial (expressed as a bit string of $c _ { i }$ ’s) is primitive. But, for now, if you only need a table of some primitive polynomials go get going, one is provided on the next page.

Since the update rule (7.5.1) is linear, it can be written as a matrix M that multiplies from the left a column vector of bits a to produce an updated state $\mathbf { a } ^ { \prime }$ . (Note that the low-order bits of a start at the top of the column vector.) One can readily read off

$$
\mathbf { M } = { \left[ \begin{array} { l l l l l l l } { c _ { 1 } } & { c _ { 2 } } & { \dots } & { c _ { n - 2 } } & { c _ { n - 1 } } & { 1 } \\ { 1 } & { 0 } & { \dots } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { \dots } & { 0 } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { } & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \dots } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { \dots } & { 0 } & { 1 } & { 0 } \end{array} \right] }
$$

<table><tr><td></td><td></td><td></td><td></td><td>Some Primitive Polynomials Modulo 2 (after Watson [1])</td><td></td><td></td><td></td><td></td><td></td><td>1,</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(51,</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(52,</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(53,</td><td></td><td></td><td></td><td>1,</td><td></td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(54,</td><td></td><td></td><td></td><td></td><td></td><td>2，</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(55,</td><td></td><td></td><td></td><td></td><td></td><td>0)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(56,</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>(57,</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td>2， 0</td><td></td><td>(58,</td><td></td><td></td><td></td><td></td><td></td><td>0 3,</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>(59,</td><td></td><td></td><td></td><td></td><td>1，</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>60,</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(11,</td><td></td><td></td><td></td><td></td><td></td><td>(61,</td><td></td><td></td><td>1,</td><td></td><td>0</td></tr><tr><td>(12,</td><td></td><td></td><td>1,</td><td></td><td></td><td>(62,</td><td></td><td></td><td>3，</td><td></td><td>0 0 2，</td></tr><tr><td>(13, (14,</td><td></td><td></td><td>1, 、</td><td>8</td><td></td><td>(63, 64</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(15, (16,</td><td></td><td></td><td>2，</td><td>0</td><td></td><td>(65, (66,</td><td></td><td></td><td></td><td>１１５１１２１１З２３１２２１２３</td><td>3</td></tr><tr><td>(17, (18,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(19,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>(69,</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(20, (21,</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(22, (23, (24,</td><td></td><td></td><td></td><td></td><td></td><td>geee</td><td></td><td></td><td></td><td></td><td>3 1，0)</td></tr><tr><td>(25, (26, (27,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1，</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0 9</td></tr><tr><td>(28,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>（78,</td><td></td><td></td><td></td><td></td><td>002</td></tr><tr><td>(29,</td><td></td><td></td><td></td><td></td><td></td><td>(79,</td><td></td><td></td><td></td><td></td><td>1,</td></tr><tr><td>(30,</td><td></td><td></td><td>1，</td><td>0</td><td></td><td>(80, (81,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(31,</td><td></td><td></td><td></td><td>1,</td><td>0</td><td>(82,</td><td></td><td></td><td></td><td>8</td><td>1,</td></tr><tr><td>(32, (33,</td><td></td><td></td><td>315</td><td>2</td><td>0</td><td>(83， (84,</td><td></td><td></td><td></td><td></td><td>1,</td></tr><tr><td>(34,</td><td></td><td></td><td></td><td>1,</td><td>0</td><td>(85,</td><td></td><td></td><td></td><td></td><td>8</td></tr><tr><td>(35, (36,</td><td></td><td></td><td>4,</td><td>1,</td><td>0</td><td>(86, (87,</td><td></td><td></td><td></td><td></td><td>3 1，</td></tr><tr><td>(37,</td><td></td><td></td><td>3, 1,</td><td>3 1,</td><td></td><td>(88,</td><td></td><td></td><td>6２5１２１4З２5２</td><td></td><td>0</td></tr><tr><td>(38, (39,</td><td></td><td>3，</td><td></td><td></td><td></td><td>(89, (90,</td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>(40,</td><td></td><td></td><td>0</td><td></td><td></td><td>(91,</td><td></td><td></td><td></td><td></td><td>3 2，</td></tr><tr><td>(41, (42,</td><td></td><td></td><td></td><td>1,</td><td>0</td><td>(92,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(43,</td><td></td><td></td><td></td><td></td><td></td><td>(93,</td><td></td><td></td><td></td><td></td><td>1,</td></tr><tr><td>(44,</td><td></td><td></td><td></td><td></td><td></td><td>(94,</td><td></td><td></td><td>1, 4, 4,</td><td></td><td>0 2 2,</td></tr><tr><td>(45, (46, (47,</td><td></td><td>4の44535の553&#x27;</td><td>33213</td><td>1,</td><td>0</td><td>(95, (96, (97,</td><td></td><td></td></table>

What are the conditions on $\mathbf { M }$ that give a full-period generator, and thereby prove that the polynomial with coefficients $c _ { i }$ is primitive? Evidently we must have

$$
\mathbf { M } ^ { ( 2 ^ { n } - 1 ) } = \mathbf { 1 }
$$

where 1 is the identity matrix. This states that the period, or some multiple of it, is $2 ^ { n } - 1$ . But the only possible such multiples are integers that divide $2 ^ { n } - 1$ . To rule these out, and ensure a full period, we need only check that

$$
{ \bf M } ^ { q _ { k } } \neq { \bf 1 } , \qquad q _ { k } \equiv ( 2 ^ { n } - 1 ) / f _ { k }
$$

for every prime factor $f _ { k }$ of $2 ^ { n } - 1$ . (This is exactly the logic behind the tests of the matrix T that we described, but did not justify, in $\ S 7 . 1 . 2 .$ )

It may at first sight seem daunting to compute the humongous powers of $\mathbf { M }$ in equations (7.5.8) and (7.5.9). But, by the method of repeated squaring of $\mathbf { M }$ , each such power takes only about $n$ (a number like 32 or 64) matrix multiplies. And, since all the arithmetic is done modulo 2, there is no possibility of overflow! The conditions (7.5.8) and (7.5.9) are in fact an efficient way to test a polynomial for primitiveness. The following code implements the test. Note that you must customize the constants in the constructor for your choice of $n$ (called $\mathbb { N }$ in the code), in particular the prime factors of $2 ^ { n } - 1$ . The case $n = 3 2$ is shown. Other than that customization, the code as written is valid for $n \leq 6 4$ . The input to the test is the “serial number,” as defined above following equation (7.5.4), of the polynomial to be tested. After declaring an instance of the Primpolytest structure, you can repeatedly call its test() method to test multiple polynomials. To make Primpolytest entirely self-contained, matrices are implemented as linear arrays, and the structure builds from scratch the few matrix operations that it needs. This is inelegant, but effective.

# struct Primpolytest {

Test polynomials over the integers mod 2 for primitiveness.

Int N, nfactors;   
VecUllong factors;   
VecInt t,a,p;   
Primpolytest() : N(32), nfactors(5), factors(nfactors), t(N\*N), a(N\*N), p(N\*N) { Constructor. The constants are specific to 32-bit LFSRs. Ullong factordata[5] $=$ {3,5,17,257,65537}; for (Int $\scriptstyle { \dot { 1 } } = 0$ ;i<nfactors; $\dot { \bf 1 } + + \dot { }$ ) factors[i] $=$ factordata[i];   
}   
Int ispident() { Utility to test if p is the identity matrix. Int i,j; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<N; $\dot { \bf 1 } + +$ ) for $\scriptstyle \dot { \ j } = 0$ ; j<N; $\mathrm { j } + +$ ) { if ( $\begin{array} { r l } { \dot { \bar { \mathbf { 1 } } } } & { { } = = } \end{array}$ j) { if (p[i\*N+j] $\smash { \downarrow = 1 }$ ) return 0; } else {if (p[i\*N+j] $\smash { \ ! = \ 0 }$ ) return 0; } } return 1;   
}   
void mattimeseq(VecInt &a, VecInt &b) { Utility for a $\ast =$ b on matrices a and b. Int i,j,k,sum; VecInt tmp(N\*N); for ( $\scriptstyle \dot { 1 } = 0$ ; i<N; $\Dot { \ b { 1 } } + +$ ) for ( $\scriptstyle { \dot { \ j } } = 0$ ; j<N; ${ \mathrm { j } } + + { \mathrm { . } }$ ) { sum $\qquad = \ 0$ ; for $\scriptstyle \mathtt { k } = 0$ ; k<N; $\mathtt { k } { + } { + }$ ) sum $+ =$ a[i\*N+k] $^ *$ b[k\*N+j]; tmp[i\*N+j] $=$ sum & 1; } for $\scriptstyle ( \mathtt { k } = 0$ ; k<N\*N; $\mathbf { k } { + } { + }$ ) a[k] $=$ tmp[k];   
}

void matpow(Ullong n) { Utility for matrix $\gamma = \mathsf { a } \mathsf { \hat { n } }$ by successive Int k; squares.

for $( \mathrm { k } = 0$ ; k<N\*N; $\mathtt { k } { + } { + }$ ) p[k] = 0; for $( \mathtt { k } = 0$ ; k<N; $\mathbf { k } { + } { + } \mathbf { \cdot }$ ) p[k\*N+k] = 1; while (1) { if (n & 1) mattimeseq(p,a); n $> > = ~ 1$ ; if $\mathbf { \Omega } _ { \mathrm { ~ n ~ } } = = \mathbf { \Omega } 0$ ) break; mattimeseq(a,a); } }

Int test(Ullong n) {   
Main test routine. Returns 1 if the polynomial with serial number n (see text) is primitive, 0 otherwise.

Int i,k,j; Ullong pow, tnm1, $\mathrm { ~ n n ~ } = \mathrm { ~ n ~ }$ ; tnm1 $=$ ((Ullong)1 << N) - 1; if (n > (tnm1 >> 1)) throw("not a polynomial of degree N"); for $( \mathrm { k } = 0$ ; k<N\*N; $\mathrm { k } { + + }$ ) t[k] $\qquad = \ 0$ ; Construct the update matrix in t. for ( $\scriptstyle { \dot { \hat { 1 } } } = 1$ ; i<N; $\dot { \bar { \mathbf { 1 } } } + + \dot { \bar { \mathbf { \rho } } } .$ ) $\ t [ \mathrm { i } * \mathrm { N } + ( \mathrm { i } - 1 ) ] = 1 ;$ $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; while (nn) { if (nn & 1) t[j] = 1; nn $> > = ~ 1$ ; j++; } t[N-1] $\ l = \ 1$ ; for $\scriptstyle 1 = 0$ ; k<N\*N; $\mathtt { k } { + } { + }$ ) a[k] $=$ t[k]; Test that t^tnm1 is the identity matrix. matpow(tnm1); if (ispident() $! = ~ 1 )$ return 0; for ( $\scriptstyle { \dot { 1 } } = 0$ ; i<nfactors; $\dot { 1 } + +$ ) { Test that the t to the required submultipow $=$ tnm1/factors[i]; ple powers is not the identity matrix. for $\scriptstyle \mathtt { k } = 0$ ; k<N\*N; $\mathbf { k } { + } { + }$ ) a[k] $= ~ \ t$ [k]; matpow(pow); if (ispident $( ) \ = = \ 1$ ) return 0; } return 1; } };

It is straightforward to generalize this method to $n > 6 4$ or to prime moduli $p$ other than 2. If $p ^ { n } > 2 ^ { 6 \mp }$ , you’ll need a multiword binary representation of the integers $p ^ { n } - 1$ and its quotients with its prime factors, so that matpow can still find powers by successive squares. Note that the computation time scales roughly as $O ( n ^ { 4 } )$ , so $n = 6 4$ is fast, while $n = 1 0 2 4$ would be rather a long calculation.

Some random primitive polynomials for $n = 3 2$ bits (giving their serial numbers as decimal values) are 2046052277, 1186898897, 221421833, 55334070, 1225518245, 216563424, 1532859853, 1735381519, 2049267032, 1363072601, and 130420448. Some random ones for $n = 6 4$ bits are 926773948609480634, 3195735403700392248, 4407129700254524327, 256457582706860311, 5017679982664373343, and 1723461400905116882.

Given a matrix M that satisfies equations (7.5.8) and (7.5.9), there are some related matrices that also satisfy those relations. An example is the inverse of M, which you can easily verify as

$$
\mathbf { M } ^ { - 1 } = \left[ \begin{array} { c c c c c c c } { 0 } & { 1 } & { 0 } & { . . . } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { . . . } & { 0 } & { 0 } \\ { . } & { . } & { . } & { } & { . } & { . } \\ { . } & { . } & { . } & { } & { . } & { . } \\ { 0 } & { 0 } & { 0 } & { . . . } & { 0 } & { 1 } \\ { 1 } & { c _ { 1 } } & { c _ { 2 } } & { . . . } & { c _ { n - 2 } } & { c _ { n - 1 } } \end{array} \right]
$$

This is the update rule that backs up a state $\mathbf { a } ^ { \prime }$ to its predecessor state a. You can easily convert (7.5.10) to a prescription analogous to equation (7.5.1) or to Figure 7.5.1(a).

Another matrix satisfying the relations that guarantee a full period is the transpose of the

inverse (or inverse of the transpose) of $\mathbf { M }$ ,

$$
\left( \mathbf { M } ^ { - 1 } \right) ^ { T } = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { \dots } & { 0 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { \dots } & { 0 } & { 0 } & { c _ { 1 } } \\ { 0 } & { 1 } & { \dots } & { 0 } & { 0 } & { c _ { 2 } } \\ { \vdots } & { \vdots } & & { \vdots } & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { \dots } & { 1 } & { 0 } & { c _ { n - 2 } } \\ { 0 } & { 0 } & { \dots } & { 0 } & { 1 } & { c _ { n - 1 } } \end{array} \right]
$$

Surprise! This is exactly Method II, as also shown in Figure 7.5.1(b). (Work it out.)

Even more specifically, the sequence of bits output by a Method II LFSR based on a primitive polynomial $P ( x )$ is identical to the sequence output by a Method I LFSR that uses the reciprocal polynomial $x ^ { n } P ( 1 / x )$ . The proof is a bit beyond our scope, but it is essentially because the matrix $\mathbf { M }$ and its transpose are both roots of the characteristic polynomial, equation (7.5.2), while the inverse matrix $\mathbf { M } ^ { - 1 }$ and its transpose are both roots of the reciprocal polynomial. The reciprocal polynomial, as you can easily check from the definition, just swaps the positions of nonzero coefficients end-to-end. For example, the reciprocal polynomial of equation (7.5.3) is .18; 17; 16; 13; 1/. If a polynomial is primitive, so is its reciprocal.

Try this experiment: Run a Method II generator for a while. Then take $n$ consecutive bits of its output (from its highest bit, say) and put them into a Method I shift register as initialization (low bit the most recent one). Now step the two methods together, using the reciprocal polynomial in the Method I. You’ll get identical output from the two generators.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Seminumerical Algorithms, 3rd ed., vol. 2 of The Art of Computer Programming (Reading,MA:Addison-Wesley),pp.30ff.   
Horowitz, P., and Hill, W. 1989, The Art of Electronics, 2nd ed. (Cambridge, UK: Cambridge University Press), $\ S 9 . 3 2 - \ S 9 . 3 7$ .   
Tausworthe, R.C. 1965, “Random Numbers Generated by Linear Recurrence Modulo Two,” Mathematics of Computation, vol.19,pp.201-209.   
Watson, E.J. 1962, “Primitive Polynomials (Mod 2),” Mathematics of Computation, vol. 16, pp. 368– 369.[1]

# 7.6 Hash Tables and Hash Memories

It’s a strange dream. You’re in a kind of mailroom whose walls are lined with numbered pigeonhole boxes. A man, Mr. Hacher, sits at a table. You are standing. There is an in-basket mounted on the wall. Your job is to take letters from the inbasket and sort them into the pigeonholes.

But how? The letters are addressed by name, while the pigeonholes are only numbered. That is where Mr. Hacher comes in. You show him each letter, and he immediately tells you its pigeonhole number. He always gives the same number for the same name, while different names always get different numbers (and therefore unique pigeonholes).

Over time, as the number of addressees grows, there are fewer and fewer empty boxes until, finally, none at all. This is not a problem as long as letters arrive only for existing boxholders. But one day, you spot a new name on an envelope. With trepidation you put it in front of Mr. Hacher : : : and you wake up!

Mr. Hacher and his table are a hash table. A hash table behaves as if it keeps a running ledger of all the hash keys (the addressee names) that it has ever seen, assigns a unique number to each, and is able to look through all the names for every new query, either returning the same number as before (for a repeat key) or, for a new key, assigning a new one. There is usually also an option to erase a key.

The goal in implementing a hash table is to make all these functions take only a few computer operations each, not even ${ \cal O } ( \log N )$ . That is quite a trick, if you think about it. Even if you somehow maintain an ordered or alphabetized list of keys, it will still take ${ \cal O } ( \log N )$ operations to find a place in the list, by bisection, say. The big idea behind hash tables is the use of random number techniques $( \ S 7 . 1 )$ to map a hash key to a pseudo-random integer between 0 and $N - 1$ , where $N$ is the total number of pigeonholes. Here we definitely want pseudo-random and not random integers, because the same key must produce the same integer each time.

In first approximation, ideally much of the time, that initial pseudo-random integer, called the output of the hash function, or (for short) the key’s hash, is what the hash table puts out, i.e., the number given out by Mr. Hacher. However, it is possible that, by chance, two keys have the same hash; in fact this becomes increasingly probable as the number of distinct keys approaches $N$ , and a certainty when $N$ is exceeded (the pigeonhole principle). The implementation of a hash table therefore requires a collision strategy that ensures that unique integers are returned, even for (different) keys that have the same hash.

Many vendors’ implementations of the $\mathrm { C } { + + }$ ’s Standard Template Library (STL) provide a hash table as the class hash_map. Unfortunately, at this writing, hash_map is not a part of the actual STL standard, and the quality of vendor implementations is also quite variable. We therefore here implement our own; thereby we can both learn more about the principles involved and build in some specific features that will be useful later in this book (for example $\ S 2 1 . 8$ and -21.6).

# 7.6.1 Hash Function Object

By a hash function object we mean a structure that combines a hashing algorithm (as in $\ S 7 . 1$ ) with the “glue” needed to make a hash table. The object should map an arbitrary key type keyT, which itself may be a structure containing multiple data values, into (for our implementation) a pseudo-random 64-bit integer. All the hash function object really needs to know about keyT is its length in bytes, that is, sizeof(keyT), since it doesn’t care how those bytes are used, only that they are part of the key to be hashed. We therefore give the hash function object a constructor that tells it how many bytes to hash; and we let it access a key by a void pointer to the key’s address. Thus the object can access those bytes any way it wants.

As a first example of a hash function object, let’s just put a wrapper around the hash function algorithm of $\ S 7 . 1 . 4$ . This is quite efficient when sizeof $( \mathtt { k e y T } ) = 4$ or 8.

# struct Hashfn1 {

Example of an object encapsulating a hash function for use by the class Hashmap.

Ranhash hasher;   
Int n;   
Hashfn1(Int nn) : n(nn) {}   
Ullong fn(const void \*key) { Uint \*k; Ullong \*kk; The actual hash function.   
Size of key in bytes.   
Constructor just saves key size.   
Function that returns hash from key.

switch (n) { case 4: k = (Uint \*)key; return hasher.int64(\*k); Return 64-bit hash of 32-bit key. case 8: kk $=$ (Ullong \*)key;\ return hasher.int64(\*kk); Return 64-bit hash of 64-bit key. default: throw("Hashfn1 is for 4 or 8 byte keys only."); } } };

(Since n is constant for the life of the object, it’s a bit inefficient to be testing it on every call; you should edit out the unnecessary code when you know n in advance.)

More generally, a hash function object can be designed to work on arbitrary sized keys by incorporating them into a final hash value a byte at a time. There is a trade-off between speed and degree-of-randomness. Historically, hash functions have favored speed, with simple incorporation rules like

$$
\begin{array} { l } { { h _ { 0 } = \mathrm { s o m e ~ f i x e d ~ c o n s t a n t } } } \\ { { \ } } \\ { { h _ { i } = ( m \ h _ { i - 1 } \ \mathrm { o p } \ k _ { i } ) \quad \mathrm { m o d } \ 2 ^ { 3 2 } \qquad ( i = 1 \dots K ) } } \end{array}
$$

Here $k _ { i }$ is the $i$ th byte of the key $1 \leq i \leq K )$ ), $m$ is a multiplier with popular values that include 33, 63689, and $2 ^ { 1 6 } + 2 ^ { 6 } - 1$ (doing the multiplication by shifts and adds in the first and third cases), and “op” is either addition or bitwise XOR. You get the mod function for free when you use 32-bit unsigned integer arithmetic. However, since 64-bit arithmetic is fast on modern machines, we think that the days of small multipliers, or many operations changing only a few bits at a time, are over. We favor hash functions that can pass good tests for randomness. (When you know a lot about your keys, it is possible to design hash functions that are even better than random, but that is beyond our scope here.)

A hash function object may also do some initialization (of tables, etc.) when it is created. Unlike a random number generator, however, it may not store any historydependent state between calls, because it must return the same hash for the same key every time. Here is an example of a self-contained hash function object for keys of any length. This is the hash function object that we will use below.

# hash.h

# struct Hashfn2 {

Another example of an object encapsulating a hash function, allowing arbitrary fixed key sizes or variable-length null terminated strings. The hash function algorithm is self-contained.

static Ullong hashfn_tab[256];   
Ullong h;   
Int n;   
Hashfn2(Int nn) : n(nn) { if $\mathbf { \Phi } _ { \mathbf { { n } } } \ = \mathbf { \Phi } _ { 1 } \mathbf { \Phi } _ { \mathbf { { \Lambda } } }$ ) $\mathrm { ~ \tt ~ n ~ } = \mathrm { ~ 0 ~ }$ ; $\mathbf { \bar { h } _ { \theta } } =$ 0x544B2FBACAAF1684LL; for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<256; ${ \dot { \mathsf { J } } } ^ { + + }$ ) { for (Int $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ; i<31; $\dot { \bf 1 } + +$ ) { $\mathrm { ~ \bf ~ h ~ } =$ (h >> 7) ^ h; h = (h << 11) ^ h; ${ \mathrm { ~  ~ h ~ } } = { \mathrm { ~  ~ \left( ~ h ~ \right) > ~ \thinspace ~ 1 0 ~ } } \widehat { \mathrm { ~  ~ \cdot ~ } } { \mathrm { ~  ~ h ~ } } ;$ } hashfn_tab[j] $= { \textrm { h } }$ ; }   
}   
Size of key in bytes, when fixed size.   
Null terminated string key signaled by $\mathbf { n } = \mathbf { 0 }$ or 1.   
Length 256 lookup table is initialized with values from a 64-bit Marsaglia generator stepped 31 times between each.

Ullong fn(const void \*key) { Function that returns hash from key. Int j; char \*k $=$ (char $^ *$ )key; Cast the key pointer to char pointer. $\mathrm { \textbar { h } = }$ 0xBB40E64DA205B064LL; $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; while (n $? \mathtt { j } + + \mathtt { \le ~ n ~ }$ : \*k) { Fixed length or else until null. $\mathrm { ~ h ~ } = \mathrm { ~ ( ~ h ~ \ * ~ }$ 7664345821815920749LL) hashfn_tab[(unsigned char)(\*k)]; $\mathrm { k } { + + }$ ; } return h; } }; Ullong Hashfn2::hashfn_tab[256]; Defines storage for the lookup table.

The method used is basically equation (7.6.1), but (i) with a large constant that is known to be a good multiplier for a linear congruential random number generator mod $2 ^ { 6 4 }$ , and, more importantly, (ii) a table lookup that substitutes a random (but fixed) 64-bit value for every byte value in 0 : : : 255. Note also the tweak that allows Hashfn2 to be used either for fixed length key types (call constructor with $\mathtt { n } > 1 \mathtt { \Omega }$ ) or with null terminated byte arrays of variable length (call constructor with $\mathtt { n } = 0$ or 1).

# 7.6.2 Hash Table

By hash table we mean an object with the functionality of Mr. Hacher (and his table) in the dream, namely to turn arbitrary keys into unique integers in a specified range. Let’s dive right in. In outline, the Hashtable object is

template<class keyT, class hfnT> struct Hashtable {

Instantiate a hash table, with methods for maintaining a one-to-one correspondence between arbitrary keys and unique integers in a specified range.

Int nhash, nmax, nn, ng;   
VecInt htable, next, garbg;   
VecUllong thehash;   
hfnT hash; An instance of a hash function object.   
Hashtable(Int nh, Int nv);   
Constructor. Arguments are size of hash table and max number of stored elements (keys).

Int iget(const keyT &key); Return integer for a previously set key. Int iset(const keyT &key); Return unique integer for a new key. Int ierase(const keyT &key); Erase a key. Int ireserve(); Reserve an integer (with no key). Int irelinquish(Int k); Un-reserve an integer. };

template<class keyT, class hfnT>   
Hashtable<keyT,hfnT>::Hashtable(Int nh, Int nv):   
Constructor. Set nhash, the size of the hash table, and nmax, the maximum number of elements   
(keys) that can be accommodated. Allocate arrays appropriately. hash(sizeof(keyT)), nhash(nh), nmax(nv), nn(0), ng(0), htable(nh), next(nv), garbg(nv), thehash(nv) for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<nh; $\mathrm { j } + +$ ) { htable[j] $=$ -1; } Signifies empty.   
}

A Hashtable object is templated by two class names: the class of the key (which may be as simple as int or as complicated as a multiply derived class) and the class of the hash function object (e.g., Hashfn1 or Hashfn2, above). Note how the hash function object is automatically created using the size of keyT, so the user is not responsible for knowing this value. If you are going to use variable length, null terminated byte arrays as keys, then the type of keyT is char, not char $^ *$ ; see $\ S 7 . 6 . 5$ for an example.

The hash table object is created from two integer parameters. The most important one is nm, the maximum number of objects that can be stored — in the dream, the number of pigeonholes in the room. For now, suppose that the second parameter, nh, has the same value as nm.

The overall scheme is to convert arbitrary keys into integers in the range $0 \ldots$ $\mathrm { \ n h } { - 1 }$ that index into the array htable, by taking the output of the hash function modulo nh. That array’s indexed element contains either $^ { - 1 }$ , meaning “empty,” or else an index in the range $0 \ldots \mathrm { n m } ^ { - 1 }$ that points into the arrays thehash and next. (For a computer science flavor one could do this with list elements linked by pointers, but in the spirit of numerical computation, we will use arrays; both ways are about equally efficient.)

An element in thehash contains the 64-bit hash of whatever key was previously assigned to that index. We will take the identity of two hashes as being positive proof that their keys were identical. Of course this is not really true. There is a probability of $2 ^ { - 6 4 } \sim 5 \times 1 0 ^ { - 2 0 }$ of two keys giving identical hashes by chance. To guarantee error-free performance, a hash table must in fact store the actual key, not just the hash; but for our purposes we will accept the very small chance that two elements might get confused. (Don’t use these routines if you are typically storing more than a billion elements in a single hash table. But you already knew that!)

This $1 0 ^ { - 2 0 }$ coincidence is not what is meant by hash collision. Rather, hash collisions occur when two hashes yield the same value modulo nh, so that they point to the same element in htable. That is not at all unusual, and we must provide for handling it. Elements in the array next contain values that index back into thehash and next, i.e., form a linked list. So, when two or more keys have landed on the same value $i$ , $0 \leq i < \mathrm { n h }$ , and we want to retrieve a particular one of them, it will either be in the location thehashŒi , or else in the (hopefully short) list that starts there and is linked by nextŒi, nextŒnextŒi, and so forth.

We can now say more about the value that should be initially specified for the parameter nh. For a full table with all nm values assigned, the linked lists attached to each element of htable have lengths that are Poisson distributed with a mean $\lambda \equiv \mathrm { n m / n h }$ . Thus, large $\lambda$ (nh too small) implies a lot of list traversal, while small $\lambda$ (nh too large) implies wasted space in htable. Conventional wisdom is to choose $\lambda \sim 0 . 7 5$ , in which case (assuming a good hash function) $47 \%$ of htable will be empty, $67 \%$ of the nonempty elements will have lists of length one (i.e., you get the correct key on the first try), and the mean number of indirections (steps in traversing the next pointers) is 0.42. For $\lambda = 1$ , that is, $\mathrm { \Delta \ n h } = \mathrm { \ n m }$ , the values are $37 \%$ table empty, $58 \%$ first try hits, and 0.58 mean indirections. So, in this general range, any choice is basically fine. The general formulas are

$$
{ \begin{array} { r l } & { { \mathrm { e m p t y } } { \mathrm { f r a c t i o n } } = P _ { \lambda } ( 0 ) = e ^ { - \lambda } } \\ & { { \mathrm { ~ f r s t } } { \mathrm { t r y h i t s } } = P _ { \lambda } ( 1 ) / [ 1 - P _ { \lambda } ( 0 ) ] = { \frac { \lambda e ^ { - \lambda } } { 1 - e ^ { - \lambda } } } } \\ & { { \mathrm { m e a n i n d i r e c t i o n s } } = \displaystyle \sum _ { j = 2 } ^ { \infty } { \frac { ( j - 1 ) P _ { \lambda } ( j ) } { 1 - P _ { \lambda } ( 0 ) } } = { \frac { e ^ { - \lambda } - 1 + \lambda } { 1 - e ^ { - \lambda } } } } \end{array} }
$$

where $P _ { \lambda } ( j )$ is the Poisson probability function.

Now to the implementations within Hashtable. The simplest to understand is the “get” function, which returns an index value only if the key was previously “set,” and returns $^ { - 1 }$ (by convention) if it was not. Our data structure is designed to make this as fast as possible.

template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::iget(const keyT &key) {   
Returns integer in 0..nmax-1 corresponding to key, or $^ { - 1 }$ if no such key was previously stored. Int j,k; Ullong $\mathrm { \nabla { p p } } =$ hash.fn(&key); Get 64-bit hash ${ \dot { \mathrm { ~  ~ } } } =$ (Int)(pp % nhash); and map it into the hash table. for (k $=$ htable[j]; k $! = ~ - 1$ ; $\mathrm { ~ \bf ~ k ~ } =$ next[k]) { Traverse linked list until an exif (thehash[k] $= = \mathtt { p p }$ ) { act match is found. return k; } return -1; Key was not previously stored.   
}

A language subtlety to be noted is that iget receives key as a const reference, and then passes its address, namely &key, to the hash function object. $\mathrm { C } { + + }$ allows this, because the hash function object’s void pointer argument is itself declared as const.

The routine that “sets” a key is slightly more complicated. If the key has previously been set, we want to return the same value as the first time. If it hasn’t been set, we initialize the necessary links for the future.

# template<class keyT, class hfnT>

Int Hashtable<keyT,hfnT>::iset(const keyT &key)

Returns integer in 0..nmax-1 that will henceforth correspond to key. If key was previously set, return the same integer as before.

Int j,k,kprev;   
Ullong pp $=$ hash.fn(&key); Get 64-bit hash   
${ \dot { \mathrm { ~  ~ } } } =$ (Int)(pp % nhash); and map it into the hash table.   
if (htable[j] $\mathbf { \omega = \omega - 1 }$ ) { Key not in table. Find a free integer, either $\mathrm { ~ k ~ } = \mathrm { ~ n g ~ } ?$ garbg[--ng] : nn++ new or previously erased. htable[j] $= \mathrm { ~ k ~ }$ ;   
} else { Key might be in table. Traverse list. for $\mathrm { ~ ( ~ k ~ } =$ htable[j]; k $! = ~ - 1$ ; $\mathrm { ~ \bf ~ k ~ } =$ next[k]) { if (thehash[k] $= =$ pp) { return k; Yes. Return previous value. kprev = k; $\mathbf { k } \ = \ \mathbf { n } \mathbf { g } \ ?$ garbg[--ng] : $\mathtt { n n } + +$ ; No. Get new integer. next[kprev] $\mathit { \Theta } = \mathit { \Theta } \mathbf { \Theta } \mathbf { k }$ ;   
}   
if ( $\begin{array} { r } { \textbf { k } > = \mathtt { n m a x } , } \end{array}$ ) throw("storing too many values");   
thehash[k] $= \ p _ { \mathrm { p } }$ ; Store the key at the new or previous integer.   
next[k] $\ c = - 1$ ;   
return k;

A word here about garbage collection. When a key is erased (by the routine immediately below), we want to make its integer available to future “sets,” so that nmax keys can always be stored. This is very easy to implement if we allocate a garbage array (garbg) and use it as a last-in first-out stack of available integers. The set routine above always checks this stack when it needs a new integer. (By the way, had we designed Hashtable with list elements linked by pointers, instead of arrays, efficient garbage collection would have been more difficult to implement; see Stroustrop [1].)

# hash.h

template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::ierase(const keyT &key) {   
Erase a key, returning the integer in 0..nmax-1 erased, or $^ { - 1 }$ if the key was not previously set. Int j,k,kprev; Ullong $\begin{array} { r l } { \mathtt { p p } } & { { } = } \end{array}$ hash.fn(&key); ${ \dot { \mathrm { ~  ~ } } } =$ (Int)(pp % nhash); if (htable[j] $\begin{array} { r l } { \mathbf { \Phi } = } & { { } - 1 . } \end{array}$ ) return -1; Key not previously set. kprev $\ c = - 1$ ; for (k $=$ htable[j]; k $! = ~ - 1$ ; $\mathrm { ~ \bf ~ k ~ } =$ next[k]) if (thehash[k] $= = \mathtt { p p }$ ) { Found key. Splice linked list around it. if (kprev $\begin{array} { r l } { \mathbf { \Psi } = } & { { } - 1 \mathbf { \Psi } } \end{array}$ ) htable[j] $=$ next[k]; else next[kprev] $=$ next[k]; garbg[ $\mathbb { n } \underline { { \operatorname { g } } } { + } { + } \mathbb { 1 } = \mathbb { k } ;$ Add k to garbage stack as an available integer. return k; } kprev = k; } return -1; Key not previously set.   
}

Finally, Hashtable has routines that reserve and relinquish integers in the range 0 to nmax. When an integer is reserved, it is guaranteed not to be used by the hash table. Below, we’ll use this feature as a convenience in constructing a hash memory that can store more than one element under a single key.

template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::ireserve() {   
Reserve an integer in 0..nmax-1 so that it will not be used by set(), and return its value. Int $\mathbf { k } \ = \ \mathbf { n } \mathbf { g } \ ?$ garbg $[ - \mathtt { - n g } ]$ : nn++ ; if (k $> =$ nmax) throw("reserving too many values"); next[k] $\ c = - 2$ ; return k;   
}   
template<class keyT, class hfnT>   
Int Hashtable<keyT,hfnT>::irelinquish(Int k) {   
Return to the pool an index previously reserved by reserve(), and return it, or return $^ { - 1 }$ if it   
was not previously reserved. if (next[k] $\ ! = \ - 2 )$ {return -1;} garbg[ng++] $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; return k;   
}

# 7.6.3 Hash Memory

The Hashtable class, above, implements Mr. Hacher’s task. Building on it, we next implement your job in the dream, namely to do the actual storage and retrieval of arbitrary objects by arbitrary keys. This is termed a hash memory.

When you store into an ordinary computer memory, the value of anything previously stored there is overwritten. If you want your hash memory to behave the same way, then a hash memory class, Hash, derived from Hashtable, is almost trivial to write. The class is templated by three structure types: keyT for the key type; elT for the type of the element that is stored in the hash memory; and hfnT, as before, for the object that encapsulates the hash function of your choice.

template<class keyT, class elT, class hfnT>   
struct Hash : Hashtable<keyT, hfnT> {   
Extend the Hashtable class with storage for elements of type elT, and provide methods for storing, retrieving. and erasing elements. key is passed by address in all methods. using Hashtable<keyT,hfnT>::iget;   
using Hashtable<keyT,hfnT>::iset;   
using Hashtable<keyT,hfnT>::ierase;   
vector<elT> els;

Hash(Int nh, Int nm) : Hashtable<keyT, hfnT>(nh, nm), els(nm) {} Same constructor syntax as Hashtable.

void set(const keyT &key, const elT &el) Store an element el. {els[iset(key)] $=$ el;}

Int get(const keyT &key, elT &el) { Retrieve an element into el. Returns 0 if no element is stored under key, or 1 for success.

Int $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iget(key); if (ll < 0) return 0; el $=$ els[ll]; return 1; }

elT& operator[] (const keyT &key) {

Store or retrieve an element using subscript notation for its key. Returns a reference that can be used as an l-value.

Int $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iget(key); if (ll < 0) { $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iset(key); els[ll] $=$ elT(); } return els[ll]; }

Int count(const keyT &key) {   
Return the number of elements stored under key, that is, either 0 or 1. Int $\begin{array} { r l } { { 1 1 } } & { { } = } \end{array}$ iget(key); return $( 1 1 < 0 \ ? \ 0 : \ 1 )$ ;   
}   
Int erase(const keyT &key) {   
Erase an element. Returns 1 for success, or 0 if no element is stored under key. return (ierase(key) $< \ 0 \ ? \ 0 \ : \ 1 )$ ;   
}

The operator[] method, above, is intended for two distinct uses. First, it implements an intuitive syntax for storing and retrieving elements, e.g.,

$$
\mathrm { { m y h a s h } [ \it { s o m e - k e y } ] = \mathrm { { } } \it { r h s } }
$$

for storing, and

$$
l h s ~ = ~ \mathrm { \ m y h a s h [ \ s o m e - } k e y { \mathrm { ~ ] ~ } }
$$

for retrieving. Note, however, that a small inefficiency is introduced, namely a superfluous call to get when an element is set for the first time. Second, the method returns a non-const reference that cannot only be used as an l-value, but also be pointed to, as in

some-pointer $=$ &myhash[ some-key ]

Now the stored element can be referenced through the pointer, possibly multiple times, without any additional overhead of key lookup. This can be an important gain in efficiency in some applications. Of course you can also use the set and get methods directly.

# 7.6.4 Hash Multimap Memory

Next turn to the case where you want to be able to store more than one element under the same key. If ordinary computer memory behaved this way, you could set a variable to a series of values and have it remember all of them! Obviously this is a somewhat more complicated an extension of Hashtable than was Hash. We will call it Mhash, where the M stands for “multivalued” or “multimap.” One requirement is to provide a convenient syntax for retrieving multiple values of a single key, one at a time. We do this by the functions getinit and getnext. Also, in Mhash, below, nmax now means the maximum number of values that can be stored, not the number of keys, which may in general be smaller.

The code, with comments, should be understandable without much additional explanation. We use the reserve and relinquish features of Hashtable so as to have a common numbering system for all stored elements, both the first instance of a key (which Hashtable must know about) and subsequent instances of the same key (which are invisible to Hashtable but managed by Mhash through the linked list nextsis).

# hash.h

template<class keyT, class elT, class hfnT> struct Mhash : Hashtable<keyT,hfnT> {

Extend the Hashtable class with storage for elements of type elT, allowing more than one element to be stored under a single key.

using Hashtable<keyT,hfnT>::iget;   
using Hashtable<keyT,hfnT>::iset;   
using Hashtable<keyT,hfnT>::ierase;   
using Hashtable<keyT,hfnT>::ireserve;   
using Hashtable<keyT,hfnT>::irelinquish;   
vector<elT> els;   
VecInt nextsis; Links to next sister element under a single key.   
Int nextget;   
Mhash(Int nh, Int nm); Same constructor syntax as Hashtable.   
Int store(const keyT &key, const elT &el); Store an element under key.   
Int erase(const keyT &key, const elT &el); Erase a specified element under key.   
Int count(const keyT &key); Count elements stored under key.   
Int getinit(const keyT &key); Prepare to retrieve elements from key.   
Int getnext(elT &el); Retrieve next element specified by getinit.   
template<class keyT, class elT, class hfnT>   
Mhash<keyT,elT,hfnT>::Mhash(Int nh, Int nm) : Hashtable<keyT, hfnT>(nh, nm), nextget(-1), els(nm), nextsis(nm) { for (Int $\scriptstyle { \dot { \ j } } = 0$ ; j<nm; ${ \mathrm { j } } + +$ ) {nextsis[j] $\ c = \ - - 2 ; \}$ Initialize to “empty”.   
}

template<class keyT, class elT, class hfnT> Int Mhash<keyT,elT,hfnT>::store(const keyT &key, const elT &el) {

Store an element el under key. Return index in 0..nmax-1, giving the storage location utilized

Int j,k;   
${ \dot { \mathrm { ~  ~ j ~ } } } =$ iset(key);   
if (nextsis[j] $= = - 2 )$ { Find root index for this key.   
It is the first object with this key.

els[j] = el; nextsis[j] = -1; 1 means it is the terminal element. return j; } else { while (nextsis[j] $! = ~ - 1 )$ {j $=$ nextsis[j];} Traverse the tree. $\mathrm { ~ \bf ~ k ~ } =$ ireserve(); Get a new index and link it into the list. els[k] $\begin{array} { r l } { = } & { { } \ominus 1 } \end{array}$ ; nextsis[j] $\mathit { \Theta } = \mathit { \Theta } \mathbf { k }$ ; nextsis[k] $\ c = - 1$ ; return k; } }

template<class keyT, class elT, class hfnT> Int Mhash<keyT,elT,hfnT>::erase(const keyT &key, const elT &el) {

Erase an element el previously stored under key. Return 1 for success, or 0 if no matching element is found. Note: The $= =$ operation must be defined for the type elT.

Save index of matching el as j.

Int $\mathrm { j ~ = ~ - 1 , k p ~ = ~ - 1 , k p p ~ = ~ - 1 ; }$ ; Int k $=$ iget(key); while (k $> = ~ 0$ ) { if (j < 0 && el $= =$ els[k]) $\dot { \mathrm { ~  ~ j ~ } } = { \bf \ k } ;$ kpp $=$ kp; $\mathrm { k p } ~ = ~ \mathrm { k }$ ; $\mathrm { k } =$ nextsis[k]; } if $( \ j \ < \ 0 )$ ) return 0; if (kpp $<$ 0) { ierase(key); nextsis[j] $= ~ - 2$ ; } else { if (j $! =$ kp) els[j] $=$ els[kp]; nextsis[kpp] $\ c = - 1$ ; irelinquish(kp); nextsis[kp] $= ~ - 2$ ; } return 1; }

No matching el found.   
The element el was unique under key.

Patch the list. Overwrite j with the terminal element and then shorten the list.

Success.

#

template<class keyT, class elT, class hfnT> Int Mhash<keyT,elT,hfnT>::count(const keyT &key) { Return the number of elements stored under key, 0 if none.

Int next, $\texttt { n } = \texttt { 1 }$ ;   
if ((next $=$ iget(key)) $< \ 0 )$ return 0;   
while ((next $=$ nextsis[next]) $> = \ 0 $ ) $\{ \mathtt { n } + +$ ;} return n;

# }

template<class keyT, class elT, class hfnT>   
Int Mhash<keyT,elT,hfnT>::getinit(const keyT &key) {   
Initialize nextget so that it points to the first element stored under key. Return 1 for success, or 0 if no such element.

nextget $=$ iget(key); return ((nextget $<$ 0)? 0 : 1); }

template<class keyT, class elT, class hfnT>   
Int Mhash<keyT,elT,hfnT>::getnext(elT &el)   
If nextget points validly, copy its element into el, update nextget to the next element with the same key, and return 1. Otherwise, do not modify el, and return 0.

if (nextget $\mathit { \Theta } < \mathit { \Theta } 0$ ) {return 0;} el $=$ els[nextget]; nextget $=$ nextsis[nextget]; return 1;

The methods getinit and getnext are designed to be used in code like this, where myhash is a variable of type Mhash:

Retrieve all elements el stored under a single key and do something with them.

if (myhash.getinit(&key)) { while (myhash.getnext(el)) 3 Here use the returned element el. }   
}

# 7.6.5 Usage Examples

Having exposed in such detail the inner workings of the Hash and Mhash classes, we may have left the impression that these are difficult to use. Quite the contrary. Here’s a piece code that declares a hash memory for integers, and then stores the birth years of some personages:

Hash<string,Int,Hashfn2> year(1000,1000);

year[string("Marie Antoinette") $\begin{array} { r l r } { \mathrm {  ~ \Omega ~ } } \end{array} | \mathrm {  ~ \Sigma ~ } \ = \ 1 7 5 5$ ;   
year[string("Ludwig van Beethoven") $\mathrm { ~ \textmu ~ } ] \mathrm { ~ \textmu ~ } = \mathrm { ~ \textmu ~ } _ { 1 } 7 7 0$ ;   
year[string("Charles Babbage" $) ] ~ = ~ 1 7 9 1$ ;

As declared, year can hold up to 1000 entries. We use the $\mathrm { C } { + } { + }$ string class as the key type. If we want to know how old Marie was when Charles was born, we can write,

Int diff $=$ year[string("Charles Babbage")] - year[string("Marie Antoinette")];   
cout $< <$ diff $< < \mathbf { \zeta } ^ { , } \setminus \mathbf { n } ^ { \prime }$ ;

which prints $\mathit { \Omega } ^ { 6 6 } 3 6 ^ { \circ }$ .

Instead of using the $\mathrm { C } { + } { + }$ string class, you can, if you must, use null terminated C strings as keys, like this:

Hash<char,Int,Hashfn2> yearc(1000,1000);   
yearc["Charles Babbage" $\mathbf { \hat { \Sigma } } [ 0 ] ] \ = \ \mathbf { \hat { \Sigma } } _ { 1 7 9 1 }$ ;

This works because Hashfn2 has a special tweak, mentioned above, for key types that are apparently one byte long. Note the required use of [0] to send only the first byte of the C string; but that byte is passed by address, so Hashfn2 knows where to find the rest of the string. (The syntax yearc[\*"Charles Babbage"] is equivalent, also sending the first byte.)

Suppose we want to go the other direction, namely store the names of people into a hash memory indexed by birth year. Since more than one person may be born in a single year, we want to use a hash multimap memory, Mhash:

Mhash<Int,string,Hashfn2> person(1000,1000);

person.store(1775, string("Jane Austen"));   
person.store(1791, string("Charles Babbage"));   
person.store(1767, string("Andrew Jackson"));   
person.store(1791, string("James Buchanan"));   
person.store(1767, string("John Quincy Adams"));   
person.store(1770, string("Ludwig van Beethoven"));   
person.store(1791, string("Samuel Morse"));   
person.store(1755, string("Marie Antoinette"));


<!-- chunk 0007: pages 421-490 -->
It doesn’t matter, of course, the order in which we put the names into the hash. Here is a piece of code to loop over years, printing the people born in that year:

string str;   
for (Int i=1750;i<1800;i++) if (person.getinit(i)) { cout << ’\n’ << "born in $" " < < \mathrm { ~ i ~ } < < \mathrm { ~ " ~ } : \backslash \mathrm { n " ~ } ;$ while (person.getnext(str)) cout << str.data() << ’\n’; }   
}

which gives as output born in 1755: Marie Antoinette born in 1767: Andrew Jackson John Quincy Adams born in 1770: Ludwig van Beethoven born in 1775: Jane Austen born in 1791: Charles Babbage James Buchanan Samuel Morse

Notice that we could not have used null terminated C strings in this example, because $\mathrm { C } { + } { + }$ does not regard them as first-class objects that can be stored as elements of a vector. When you are using Hash or Mhash with strings, you will usually be better off using the $\mathrm { C } { + } { + }$ string class.

In $\ S 2 1 . 2$ and $\ S 2 1 . 8$ we will make extensive use of both the Hash and Mhash classes and almost all their member functions; look there for further usage examples.

By the way, Mr. Hacher’s name is from the French hacher, meaning “to mince or hash.”

# CITED REFERENCES AND FURTHER READING:

Stroustrup, B. 1997, The $C { + + }$ Programming Language, 3rd ed. (Reading, MA: Addison-Wesley), $\ S 1 7 . 6 . 2$ .[1]   
Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 6 . 4 \mathrm { - } \ S 6 . 5$ .   
Vitter, J.S., and Chen, W-C. 1987, Design and Analysis of Coalesced Hashing (New York: Oxford University Press).

# 7.7 Simple Monte Carlo Integration

Inspirations for numerical methods can spring from unlikely sources. “Splines” first were flexible strips of wood used by draftsmen. “Simulated annealing” (we shall

![](images/2aba06665e95d8b255948fd5e0ccc4c797fdc99178bf944552ea173fc4c57119.jpg)  
Figure 7.7.1. Monte Carlo integration of a function $f ( x , y )$ in a region $W$ . Random points are chosen within an area $V$ that includes $W$ and that can easily be sampled uniformly. Of the three possible $V$ ’s shown, $V _ { 1 }$ is a poor choice because $W$ occupies only a small fraction of its area, while $V _ { 2 }$ and $V _ { 3 }$ are better choices.

see in $\ S 1 0 . 1 2 )$ is rooted in a thermodynamic analogy. And who does not feel at least a faint echo of glamor in the name “Monte Carlo method”?

Suppose that we pick $N$ random points, uniformly distributed in a multidimensional volume $V$ . Call them $x _ { 0 } , \ldots , x _ { N - 1 }$ . Then the basic theorem of Monte Carlo integration estimates the integral of a function $f$ over the multidimensional volume,

$$
\int f d V \approx V \langle f \rangle \pm V { \sqrt { \frac { \langle f ^ { 2 } \rangle - \langle f \rangle ^ { 2 } } { N } } }
$$

Here the angle brackets denote taking the arithmetic mean over the $N$ sample points,

$$
\langle f \rangle \equiv { \frac { 1 } { N } } \sum _ { i = 0 } ^ { N - 1 } f ( x _ { i } ) \qquad \left. f ^ { 2 } \right. \equiv { \frac { 1 } { N } } \sum _ { i = 0 } ^ { N - 1 } f ^ { 2 } ( x _ { i } )
$$

The “plus-or-minus” term in (7.7.1) is a one standard deviation error estimate for the integral, not a rigorous bound; further, there is no guarantee that the error is distributed as a Gaussian, so the error term should be taken only as a rough indication of probable error.

Suppose that you want to integrate a function $g$ over a region $W$ that is not easy to sample randomly. For example, $W$ might have a very complicated shape. No problem. Just find a region $V$ that includes $W$ and that can easily be sampled, and then define $f$ to be equal to $g$ for points in $W$ and equal to zero for points outside of $W$ (but still inside the sampled $V$ ). You want to try to make $V$ enclose $W$ as closely as possible, because the zero values of $f$ will increase the error estimate term of (7.7.1). And well they should: Points chosen outside of $W$ have no information content, so the effective value of $N$ , the number of points, is reduced. The error estimate in (7.7.1) takes this into account.

Figure 7.7.1 shows three possible regions $V$ that might be used to sample a complicated region $W$ . The first, $V _ { 1 }$ , is obviously a poor choice. A good choice, $V _ { 2 }$ , can be sampled by picking a pair of uniform deviates $( s , t )$ and then mapping them into $( x , y )$ by a linear transformation. Another good choice, $V _ { 3 }$ , can be sampled by, first, using a uniform deviate to choose between the left and right rectangular subregions (in proportion to their respective areas!) and, then, using two more deviates to pick a point inside the chosen rectangle.

Let’s create an object that embodies the general scheme described. (We will discuss the implementing code later.) The general idea is to create an MCintegrate object by providing (as constructor arguments) the following items:

- a vector xlo of lower limits of the coordinates for the rectangular box to be sampled   
- a vector xhi of upper limits of the coordinates for the rectangular box to be sampled   
- a vector-valued function funcs that returns as its components one or more functions that we want to integrate simultaneously   
a boolean function that returns whether a point is in the (possibly complicated) region $W$ that we want to integrate; the point will already be within the region $V$ defined by xlo and xhi   
- a mapping function to be discussed below, or NULL if there is no mapping function or if your attention span is too short   
- a seed for the random number generator

The object MCintegrate has this structure.

# struct MCintegrate {

Object for Monte Carlo integration of one or more functions in an ndim-dimensional region.

Int ndim,nfun,n; Number of dimensions, functions, and points sampled.   
VecDoub ff,fferr; Answers: The integrals and their standard errors.   
VecDoub xlo,xhi,x,xx,fn,sf,sferr;   
Doub vol; Volume of the box V .

Pointers to the user-supplied functions.

VecDoub (\*funcsp)(const VecDoub &);   
VecDoub (\*xmapp)(const VecDoub &);   
Bool (\*inregionp)(const VecDoub &);   
Ran ran;

Random number generator.

MCintegrate(const VecDoub &xlow, const VecDoub &xhigh, VecDoub funcs(const VecDoub &), Bool inregion(const VecDoub &), VecDoub xmap(const VecDoub &), Int ranseed); Constructor. The arguments are in the order described in the itemized list above.

void step(Int nstep);   
Sample an additional nstep points, accumulating the various sums.

void calcanswers();

Calculate answers ff and fferr using the current sums.

The member function step adds sample points, the number of which is given by its argument. The member function calcanswers updates the vectors ff and fferr, which contain respectively the estimated Monte Carlo integrals of the functions and the errors on these estimates. You can examine these values, and then, if you want, call step and calcanswers again to further reduce the errors.

A worked example will show the underlying simplicity of the method. Suppose that we want to find the weight and the position of the center of mass of an object of complicated shape, namely the intersection of a torus with the faces of a large box. In particular, let the object be defined by the three simultaneous conditions:

![](images/aae3fc3f4f9571759a2c98a37a989c92caee855b9d90b61019dafb43b4cd73cf.jpg)  
Figure 7.7.2. Example of Monte Carlo integration (see text). The region of interest is a piece of a torus, bounded by the intersection of two planes. The limits of integration of the region cannot easily be written in analytically closed form, so Monte Carlo is a useful technique.

$$
z ^ { 2 } + \left( \sqrt { x ^ { 2 } + y ^ { 2 } } - 3 \right) ^ { 2 } \leq 1
$$

(torus centered on the origin with major radius $= 3$ , minor radius $= 1$ )

$$
x \geq 1 \qquad y \geq - 3
$$

(two faces of the box; see Figure 7.7.2). Suppose for the moment that the object has a constant density $\rho = 1$ .

We want to estimate the following integrals over the interior of the complicated object:

$$
\int \rho d x d y d z \qquad \int x \rho d x d y d z \qquad \int y \rho d x d y d z \qquad \int z \rho d x d y d z
$$

The coordinates of the center of mass will be the ratio of the latter three integrals (linear moments) to the first one (the weight).

To use the MCintegrate object, we first write functions that describe the integrands and the region of integration $W$ inside the box $V$ .

VecDoub torusfuncs(const VecDoub &x) {

Return the integrands in equation (7.7.5), with $\rho = 1$

Doub den $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
VecDoub f(4);   
$\mathbf { f } \left[ 0 \right] \mathbf { \tau } =$ den;   
for (Int $\dot { 1 } = 1$ ;i<4; $\Dot { \ b { 1 } } + +$ ) f[i] = x[i-1]\*den;   
return f;

# }

Bool torusregion(const VecDoub &x) {   
Return the inequality (7.7.3). return SQR(x[2])+SQR(sqrt(SQR(x[0])+SQR(x[1]))-3.) <= 1.;   
}

The code to actually do the integration is now quite simple,

VecDoub xlo(3), xhi(3);   
xlo[0] $=$ 1.; xhi[0] $\mathit { \Theta } = \mathit { \Theta } 4 .$ ;   
xlo[1] $= \ - 3 .$ ; xhi[1] $= ~ 4 .$ ;   
xlo[2] $\ c = - 1$ .; xhi[2] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
MCintegrate mymc(xlo,xhi,torusfuncs,torusregion,NULL,10201);   
mymc.step(1000000);   
mymc.calcanswers();

Here we’ve specified the box $V$ by $\tt x l o$ and xhi, created an instance of MCintegrate, sampled a million times, and updated the answers mymc.ff and mymc.fferr, which can be accessed for printing or another use.

# 7.7.1 Change of Variables

A change of variable can often be extremely worthwhile in Monte Carlo integration. Suppose, for example, that we want to evaluate the same integrals, but for a piece of torus whose density is a strong function of $Z$ , in fact varying according to

$$
\rho ( x , y , z ) = e ^ { 5 z }
$$

One way to do this is, in torusfuncs, simply to replace the statement

# Doub ${ \mathsf { d e n } } \ = \ 1 .$ ;

by the statement

Doub ${ \mathsf { d e n } } \ = \ \exp ( { \mathsf { S } } \cdot * { \mathbf { x } } [ 2 ] ) \ ;$

This will work, but it is not the best way to proceed. Since (7.7.6) falls so rapidly to zero as $Z$ decreases (down to its lower limit $^ { - 1 }$ ), most sampled points contribute almost nothing to the sum of the weight or moments. These points are effectively wasted, almost as badly as those that fall outside of the region $W$ . A change of variable, exactly as in the transformation methods of $\ S 7 . 3$ , solves this problem. Let

$$
\begin{array} { r } { d s = e ^ { 5 z } d z \qquad \mathrm { ~ s o ~ t h a t ~ } \qquad s = \frac { 1 } { 5 } e ^ { 5 z } , \quad z = \frac { 1 } { 5 } \ln ( 5 s ) } \end{array}
$$

Then $\rho d z = d s$ , and the limits $- 1 < z < 1$ become : $0 0 1 3 5 < s < 2 9 . 6 8 2$ .

The MCintegrate object knows that you might want to do this. If it sees an argument xmap that is not NULL, it will assume that the sampling region defined by xlo and xhi is not in physical space, but rather needs to be mapped into physical space before either the functions or the region boundary are calculated. Thus, to effect our change of variable, we don’t need to modify torusfuncs or torusregion, but we do need to modify $\tt x l o$ and xhi, as well as supply the following function for the argument xmap:

VecDoub torusmap(const VecDoub &s) {

Return the mapping from $s$ to $z$ defined by the last equation in (7.7.7), mapping the other coordinates by the identity map.

VecDoub xx(s);   
$\arg { \frac { \ d } { \ d t } } = { \bf \nabla } _ { 0 } . 2 \ast \mathrm { { 1 0 g } } \left( 5 . \ast \bf { _ { S } } \left[ 2 \right] \right) ,$ ;   
return xx;

Code for the actual integration now looks like this:

VecDoub slo(3), shi(3);   
slo[0] $\mathbf { \lambda } = \mathbf { \lambda } _ { 1 } . \mathbf { \lambda } ;$ shi[0] $\mathit { \Theta } = \mathit { \Theta } 4 \cdot$ ;   
slo[1] $=$ -3.; shi[1] $= ~ 4 .$ ;   
slo[2] $=$ 0.2\*exp(5.\*(-1.)); shi[2] $=$ 0.2\*exp(5.\*(1.));   
MCintegrate mymc2(slo,shi,torusfuncs,torusregion,torusmap,10201);   
mymc2.step(1000000);   
mymc2.calcanswers();

If you think for a minute, you will realize that equation (7.7.7) was useful only because the part of the integrand that we wanted to eliminate $( e ^ { 5 z } )$ was both integrable analytically and had an integral that could be analytically inverted. (Compare $\ S 7 . 3 . 2 .$ ) In general these properties will not hold. Question: What then? Answer: Pull out of the integrand the “best” factor that can be integrated and inverted. The criterion for “best” is to try to reduce the remaining integrand to a function that is as close as possible to constant.

The limiting case is instructive: If you manage to make the integrand $f$ exactly constant, and if the region $V$ , of known volume, exactly encloses the desired region $W$ , then the average of $f$ that you compute will be exactly its constant value, and the error estimate in equation (7.7.1) will exactly vanish. You will, in fact, have done the integral exactly, and the Monte Carlo numerical evaluations are superfluous. So, backing off from the extreme limiting case, to the extent that you are able to make $f$ approximately constant by change of variable, and to the extent that you can sample a region only slightly larger than $W$ , you will increase the accuracy of the Monte Carlo integral. This technique is generically called reduction of variance in the literature.

The fundamental disadvantage of simple Monte Carlo integration is that its accuracy increases only as the square root of $N$ , the number of sampled points. If your accuracy requirements are modest, or if your computer is large, then the technique is highly recommended as one of great generality. In $\ S 7 . 8$ and $\ S 7 . 9$ we will see that there are techniques available for “breaking the square root of $N$ barrier” and achieving, at least in some cases, higher accuracy with fewer function evaluations.

There should be nothing surprising in the implementation of MCintegrate. The constructor stores pointers to the user functions, makes an otherwise superfluous call to funcs just to find out the size of returned vector, and then sizes the sum and answer vectors accordingly. The step and calcanswer methods implement exactly equations (7.7.1) and (7.7.2).

MCintegrate::MCintegrate(const VecDoub &xlow, const VecDoub &xhigh, VecDoub funcs(const VecDoub &), Bool inregion(const VecDoub &), VecDoub xmap(const VecDoub &), Int ranseed) : ndim(xlow.size()), ${ \mathfrak { n } } ( 0 )$ , xlo(xlow), xhi(xhigh), x(ndim), xx(ndim), funcsp(funcs), xmapp(xmap), inregionp(inregion), vol(1.), ran(ranseed) if (xmapp) nfun $=$ funcs(xmapp(xlo)).size(); else nfun $=$ funcs(xlo).size(); ff.resize(nfun); fferr.resize(nfun);

fn.resize(nfun);   
sf.assign(nfun,0.);   
sferr.assign(nfun,0.);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<ndim;j++) vol $\ast =$ abs(xhi[j]-xlo[j]);

# }

void MCintegrate::step(Int nstep) { Int i,j; for ( $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<nstep; $\dot { 1 } + +$ ) { for (j=0;j<ndim; $\mathrm { j } + +$ ) x[j] $=$ xlo[j]+(xhi[j]-xlo[j])\*ran.doub(); if (xmapp) xx $=$ (\*xmapp)(x); else $\mathbf { \boldsymbol { x } } \mathbf { \boldsymbol { x } } \ = \mathbf { \boldsymbol { x } }$ ; if ((\*inregionp)(xx)) { fn $=$ (\*funcsp)(xx); for (j=0;j<nfun;j++) { sf[j] $+ =$ fn[j]; sferr[j] $+ =$ SQR(fn[j]); } } } n $+ =$ nstep;   
}   
void MCintegrate::calcanswers(){ for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<nfun;j++) { ff[j] $=$ vol\*sf[j]/n; fferr[j] $=$ vol\*sqrt((sferr[j]/n-SQR(sf[j]/n))/n); }   
}

# CITED REFERENCES AND FURTHER READING:

Robert, C.P., and Casella, G. 2006, Monte Carlo Statistical Methods, 2nd ed. (New York: Springer) Sobol’, I.M. 1994, A Primer for the Monte Carlo Method (Boca Raton, FL: CRC Press). Hammersley, J.M., and Handscomb, D.C. 1964, Monte Carlo Methods (London: Methuen). Gentle, J.E. 2003, Random Number Generation and Monte Carlo Methods, 2nd ed. (New York: Springer), Chapter 7. Shreider, Yu. A. (ed.) 1966, The Monte Carlo Method (Oxford: Pergamon). Kalos, M.H., and Whitlock, P.A. 1986, Monte Carlo Methods: Volume 1 : Basics (New York: Wiley).

# 7.8 Quasi- (that is, Sub-) Random Sequences

We have just seen that choosing $N$ points uniformly randomly in an $n$ -dimensional space leads to an error term in Monte Carlo integration that decreases as $1 / \sqrt { N }$ . In essence, each new point sampled adds linearly to an accumulated sum that will become the function average, and also linearly to an accumulated sum of squares that will become the variance (equation 7.7.2). The estimated error comes from the square root of this variance, hence the power $N ^ { - 1 / 2 }$ .

Just because this square-root convergence is familiar does not, however, mean that it is inevitable. A simple counterexample is to choose sample points that lie on a Cartesian grid, and to sample each grid point exactly once (in whatever order).

The Monte Carlo method thus becomes a deterministic quadrature scheme — albeit a simple one — whose fractional error decreases at least as fast as $N ^ { - 1 }$ (even faster if the function goes to zero smoothly at the boundaries of the sampled region or is periodic in the region).

The trouble with a grid is that one has to decide in advance how fine it should be. One is then committed to completing all of its sample points. With a grid, it is not convenient to “sample until” some convergence or termination criterion is met. One might ask if there is not some intermediate scheme, some way to pick sample points “at random,” yet spread out in some self-avoiding way, avoiding the chance clustering that occurs with uniformly random points.

A similar question arises for tasks other than Monte Carlo integration. We might want to search an $n$ -dimensional space for a point where some (locally computable) condition holds. Of course, for the task to be computationally meaningful, there had better be continuity, so that the desired condition will hold in some finite $n$ - dimensional neighborhood. We may not know a priori how large that neighborhood is, however. We want to “sample until” the desired point is found, moving smoothly to finer scales with increasing samples. Is there any way to do this that is better than uncorrelated, random samples?

The answer to the above question is “yes.” Sequences of $n$ -tuples that fill $n$ - space more uniformly than uncorrelated random points are called quasi-random sequences. That term is somewhat of a misnomer, since there is nothing “random” about quasi-random sequences: They are cleverly crafted to be, in fact, subrandom. The sample points in a quasi-random sequence are, in a precise sense, “maximally avoiding” of each other.

A conceptually simple example is Halton’s sequence [1]. In one dimension, the $j$ th number $H _ { j }$ in the sequence is obtained by the following steps: (i) Write $j$ as a number in base $b$ , where $b$ is some prime. (For example, $j = 1 7$ in base $b = 3$ is 122.) (ii) Reverse the digits and put a radix point (i.e., a decimal point base $b$ ) in front of the sequence. (In the example, we get 0:221 base 3.) The result is $H _ { j }$ . To get a sequence of $n$ -tuples in $n$ -space, you make each component a Halton sequence with a different prime base $b$ . Typically, the first $n$ primes are used.

It is not hard to see how Halton’s sequence works: Every time the number of digits in $j$ increases by one place, $j$ ’s digit-reversed fraction becomes a factor of $b$ finer-meshed. Thus the process is one of filling in all the points on a sequence of finer and finer Cartesian grids — and in a kind of maximally spread-out order on each grid (since, e.g., the most rapidly changing digit in $j$ controls the most significant digit of the fraction).

Other ways of generating quasi-random sequences have been proposed by Faure, Sobol’, Niederreiter, and others. Bratley and Fox [2] provide a good review and references, and discuss a particularly efficient variant of the Sobol’ [3] sequence suggested by Antonov and Saleev [4]. It is this Antonov-Saleev variant whose implementation we now discuss.

The Sobol’ sequence generates numbers between zero and one directly as binary fractions of length $w$ bits, from a set of $w$ special binary fractions, $V _ { i }$ ; $i = 1 , 2 , \dots , w$ , called direction numbers. In Sobol’s original method, the $j$ th number $X _ { j }$ is generated by XORing (bitwise exclusive or) together the set of $V _ { i }$ ’s satisfying the criterion on $i$ , “the $i$ th bit of $j$ is nonzero.” As $j$ increments, in other words, different ones of the $V _ { i }$ ’s flash in and out of $X _ { j }$ on different time scales. $V _ { 1 }$ alternates between being present and absent most quickly, while

![](images/409dec64a804d90a731181cd4113d753120deb0643d22d98ab3519377943c179.jpg)  
Figure 7.8.1. First 1024 points of a two-dimensional Sobol’ sequence. The sequence is generated numbertheoretically, rather than randomly, so successive points at any stage “know” how to fill in the gaps in the previously generated distribution.

$V _ { k }$ goes from present to absent (or vice versa) only every $2 ^ { k - 1 }$ steps.

Antonov and Saleev’s contribution was to show that instead of using the bits of the integer $j$ to select direction numbers, one could just as well use the bits of the Gray code of $j , G ( j )$ . (For a quick review of Gray codes, look at $\ S 2 2 . 3 .$ )

Now $G ( j )$ and $G ( j + 1 )$ differ in exactly one bit position, namely in the position of the rightmost zero bit in the binary representation of $j$ (adding a leading zero to $j$ if necessary). A consequence is that the $j + 1 \mathrm { s t }$ Sobol’-Antonov-Saleev number can be obtained from the $j$ th by XORing it with a single $V _ { i }$ , namely with $i$ the position of the rightmost zero bit in $j$ . This makes the calculation of the sequence very efficient, as we shall see.

Figure 7.8.1 plots the first 1024 points generated by a two-dimensional Sobol’ sequence. One sees that successive points do “know” about the gaps left previously, and keep filling them in, hierarchically.

We have deferred to this point a discussion of how the direction numbers $V _ { i }$ are generated. Some nontrivial mathematics is involved in that, so we will content ourselves with a cookbook summary only: Each different Sobol’ sequence (or component of an $n$ -dimensional sequence) is based on a different primitive polynomial over the integers modulo 2, that is, a polynomial whose coefficients are either 0 or 1, and which generates a maximal length shift register sequence. (Primitive polynomials modulo 2 were used in $\ S 7 . 5$ and are further discussed in $\ S 2 2 . 4 .$ ) Suppose $P$ is such a polynomial, of degree $q$ ,

<table><tr><td rowspan=1 colspan=1>Degree</td><td rowspan=1 colspan=1>Primitive Polynomials Modulo 2*</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0 (i.e., x+1)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1 (i.e., x² + x+1)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>1,2 (i.e.,x³ + x +1 and x³+ x²+1)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1,4 (i.e.,x4 +x+1 and x4 +x+1)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>2,4,7, 11,13,14</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>1,13,16,19,22,25</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>1,4,7,8,14,19,21,28,31,32,37,41,42,50,55,56,59,62</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>14,21,22,38,47,49,50,52,56,67,70,84,97,103,115,122</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>8,13,16,22,25,44,47,52,55,59,62,67,74,81,82,87,91,94,103,104,109,122,124,137,138,143,145,152,157,167,173,176,181,182,185,191,194,199,218,220,227,229,230,234,236,241,244,253</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>4,13,19,22,50,55,64,69,98,107,115,121,127,134,140,145,152,158,161,171,181,194,199,203,208,227,242,251,253,265,266,274,283,289,295,301,316,319,324,346,352,361,367,382,395,398,400,412,419,422,426,428,433,446,454,457,472,493,505,508</td></tr><tr><td rowspan=1 colspan=2>*Expressed as a decimal integer whose binary representation gives the coefficients,from thehighest to lowest power of x.Only the internal terms are represented—the highest-order termand the constant term always have coefficient 1.</td></tr></table>

$$
P = x ^ { q } + a _ { 1 } x ^ { q - 1 } + a _ { 2 } x ^ { q - 2 } + \cdots + a _ { q - 1 } x + 1
$$

Define a sequence of integers $M _ { i }$ by the $q$ -term recurrence relation,

$$
M _ { i } = 2 a _ { 1 } M _ { i - 1 } \oplus 2 ^ { 2 } a _ { 2 } M _ { i - 2 } \oplus \cdots \oplus 2 ^ { q - 1 } M _ { i - q + 1 } a _ { q - 1 } \oplus ( 2 ^ { q } M _ { i - q } \oplus M _ { i - q } )
$$

Here bitwise XOR is denoted by $\oplus$ . The starting values for this recurrence are that $M _ { 1 } , \dots , M _ { q }$ can be arbitrary odd integers less than $2 , \ldots , 2 ^ { q }$ , respectively. Then, the direction numbers $V _ { i }$ are given by

$$
V _ { i } = M _ { i } / 2 ^ { i } \qquad i = 1 , \dots , w
$$

The table above lists all primitive polynomials modulo 2 with degree $q \leq 1 0$ . Since the coefficients are either 0 or 1, and since the coefficients of $x ^ { q }$ and of 1 are predictably 1, it is convenient to denote a polynomial by its middle coefficients taken as the bits of a binary number (higher powers of $x$ being more significant bits). The table uses this convention.

Turn now to the implementation of the Sobol’ sequence. Successive calls to the function sobseq (after a preliminary initializing call) return successive points in an $n$ -dimensional Sobol’ sequence based on the first $n$ primitive polynomials in the table. As given, the routine is initialized for maximum $n$ of 6 dimensions, and for a word length $w$ of 30 bits. These parameters can be altered by changing MAXBIT $( \equiv w )$ ) and MAXDIM, and by adding more initializing data to the arrays ip (the primitive polynomials from the table above), mdeg (their degrees), and iv (the starting values for the recurrence, equation 7.8.2). A second table, on the next page, elucidates the initializing data in the routine.

<table><tr><td rowspan=1 colspan=6>Initializing Values Used in sobseq</td></tr><tr><td rowspan=1 colspan=1>Degree</td><td rowspan=1 colspan=1>Polynomial</td><td rowspan=1 colspan=4>Starting Values</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>(3)</td><td rowspan=1 colspan=1>(5)</td><td rowspan=1 colspan=1>(15)...</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>(11)...</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>(5)...</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>(15)...</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>13...</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>9...</td></tr><tr><td rowspan=1 colspan=6>Parenthesized values are not freely specifiable,but are forced by the requiredrecurrence for this degree.</td></tr></table>

# void sobseq(const Int n, VecDoub_O &x)

When n is negative, internally initializes a set of MAXBIT direction numbers for each of MAXDIM different Sobol’ sequences. When n is positive (but MAXDIM), returns as the vector $\mathbf { x } \left[ 0 \ldots \mathbf { n - 1 } \right]$ the next values from n of these sequences. (n must not be changed between initializations.) {

const Int MAXBIT $\scriptstyle = 3 0$ ,MAXDIM=6;   
Int j,k,l;   
Uint i,im,ipp;   
static Int mdeg[MAXDIM] $=$ {1,2,3,3,4,4};   
static Uint in;   
static VecUint ix(MAXDIM);   
static NRvector<Uint\*> iu(MAXBIT);   
static Uint ip[MAXDIM] $= \{ 0$ ,1,1,2,1,4};   
static Uint iv[MAXDIM\*MAXBIT] $=$ {1,1,1,1,1,1,3,1,3,3,1,1,5,7,7,3,3,5,15,11,5,15,13,9};   
static Doub fac;   
if $\mathbf { \chi } _ { \mathbf { n } } \ < \ 0$ ) { Initialize, don’t return a vector. for (k=0;k<MAXDIM; $\mathrm { k } { + } { + }$ ) ix[k] ${ = } 0$ ; $\mathtt { i n } { = } 0$ ; if (iv[0] $! = ~ 1 ^ { \prime }$ ) return; fac $^ { = 1 }$ .0/(1 << MAXBIT); for ( $\scriptstyle { \dot { \mathsf { J } } } = 0$ ,k=0;j<MAXBIT;j++, $\xi + =$ MAXDIM) iu[j] $=$ &iv[k]; To allow both 1D and 2D addressing. for $( \mathrm { k } = 0$ ;k<MAXDIM; $\mathrm { k } { + } { + }$ ) { for ( $\scriptstyle \cdot j = 0$ ;j<mdeg[k]; $\mathrm { j } { + + } )$ ) iu[j][k] <<= (MAXBIT-1-j); Stored values only require normalization. for (j=mdeg[k];j<MAXBIT;j++) { Use the recurrence to get other valipp=ip[k]; ues. $\dot { \bf 1 } =$ iu[j-mdeg[k]][k]; i $\hat { \bf \Phi } =$ (i >> mdeg[k]); for ( $\ b { 1 } =$ mdeg[k]-1; $\scriptstyle 1 > = 1$ ;l--) { if (ipp & 1) i $\hat { \bf \Phi } =$ iu[j-l][k]; ipp $> > = ~ 1$ ; } iu[j][k] ${ \bf \Phi } = \dot { \bf 1 }$ ; } }   
} else { Calculate the next vector in the seim=in++; quence. for (j=0;j<MAXBIT;j++) { Find the rightmost zero bit. if (!(im & 1)) break; im $> > = ~ 1$ ; }

if (j $> =$ MAXBIT) throw("MAXBIT t im=j\*MAXDIM; for $\scriptstyle ( \mathtt { k } = 0$ ;k<MIN(n,MAXDIM); $\mathbf { \nabla } \cdot \mathbf { k } { + + }$ ) { ix[k] $\hat { \mathbf { \alpha } } =$ iv[im+k]; x[k] $\mathbf { \mu } = \ j \mathbf { \mu } _ { \mathbf { X } }$ [k]\*fac; } } }

XOR the appropriate direction number into each component of the vector and convert to a floating number.

How good is a Sobol’ sequence, anyway? For Monte Carlo integration of a smooth function in $n$ dimensions, the answer is that the fractional error will decrease with $N$ , the number of samples, as $( \ln N ) ^ { n } / N$ , i.e., almost as fast as $1 / N$ . As an example, let us integrate a function that is nonzero inside a torus (doughnut) in three-dimensional space. If the major radius of the torus is $R _ { 0 }$ and the minor radius is $r _ { 0 }$ , the minor radial coordinate $r$ is defined by

$$
r = \left( [ ( x ^ { 2 } + y ^ { 2 } ) ^ { 1 / 2 } - R _ { 0 } ] ^ { 2 } + z ^ { 2 } \right) ^ { 1 / 2 }
$$

Let us try the function

$$
f ( x , y , z ) = \left\{ \begin{array} { l l } { 1 + \cos \left( \displaystyle \frac { \pi r ^ { 2 } } { r _ { 0 } ^ { 2 } } \right) } & { \quad r < r _ { 0 } } \\ { 0 } & { \quad r \geq r _ { 0 } } \end{array} \right.
$$

which can be integrated analytically in cylindrical coordinates, giving

$$
\iiint d x d y d z f ( x , y , z ) = 2 \pi ^ { 2 } r _ { 0 } ^ { 2 } R _ { 0 }
$$

With parameters $R _ { 0 } = 0 . 6 , r _ { 0 } = 0 . 3$ , we did 100 successive Monte Carlo integrations of equation (7.8.4), sampling uniformly in the region $- 1 < x , y , z \ < \ 1$ , for the two cases of uncorrelated random points and the Sobol’ sequence generated by the routine sobseq. Figure 7.8.2 shows the results, plotting the r.m.s. average error of the 100 integrations as a function of the number of points sampled. (For any single integration, the error of course wanders from positive to negative, or vice versa, so a logarithmic plot of fractional error is not very informative.) The thin, dashed curve corresponds to uncorrelated random points and shows the familiar $N ^ { - 1 / 2 }$ asymptotics. The thin, solid gray curve shows the result for the Sobol’ sequence. The logarithmic term in the expected $( \mathrm { l n } \bar { N } ) ^ { 3 } / N$ is readily apparent as curvature in the curve, but the asymptotic $N ^ { - 1 }$ is unmistakable.

To understand the importance of Figure 7.8.2, suppose that a Monte Carlo integration of $f$ with $1 \%$ accuracy is desired. The Sobol’ sequence achieves this accuracy in a few thousand samples, while pseudo-random sampling requires nearly 100,000 samples. The ratio would be even greater for higher desired accuracies.

A different, not quite so favorable, case occurs when the function being integrated has hard (discontinuous) boundaries inside the sampling region, for example the function that is one inside the torus and zero outside,

$$
f ( x , y , z ) = \left\{ { \begin{array} { l l } { 1 ~ } & { ~ r < r _ { 0 } } \\ { 0 ~ } & { ~ r \geq r _ { 0 } } \end{array} } \right.
$$

where $r$ is defined in equation (7.8.4). Not by coincidence, this function has the same analytic integral as the function of equation (7.8.5), namely $2 \pi ^ { 2 } r _ { 0 } ^ { 2 } R _ { 0 }$ .

The carefully hierarchical Sobol’ sequence is based on a set of Cartesian grids, but the boundary of the torus has no particular relation to those grids. The result is that it is essentially random whether sampled points in a thin layer at the surface of the torus, containing on the order of $N ^ { 2 / 3 }$ points, come out to be inside or outside the torus. The square root law, applied to this thin layer, gives $N ^ { 1 / 3 }$ fluctuations in the sum, or $N ^ { - 2 / 3 }$ fractional error in the Monte Carlo integral. One sees this behavior verified in Figure 7.8.2 by the thicker gray curve. The thicker dashed curve in Figure 7.8.2 is the result of integrating the function of equation (7.8.7) using independent random points. While the advantage of the Sobol’ sequence is not quite so dramatic as in the case of a smooth function, it can nonetheless be a significant factor $( \sim 5 )$ even at modest accuracies like $1 \%$ , and greater at higher accuracies.

![](images/ab6ac918e3ca3d9f0f7f1d88dbbde807a46cf59e93cfc4ae88245f43edc80ccd.jpg)  
Figure 7.8.2. Fractional accuracy of Monte Carlo integrations as a function of number of points sampled, for two different integrands and two different methods of choosing random points. The quasi-random Sobol’ sequence converges much more rapidly than a conventional pseudo-random sequence. Quasirandom sampling does better when the integrand is smooth (“soft boundary”) than when it has step discontinuities (“hard boundary”). The curves shown are the r.m.s. averages of 100 trials.

Note that we have not provided the routine sobseq with a means of starting the sequence at a point other than the beginning, but this feature would be easy to add. Once the initialization of the direction numbers iv has been done, the $j$ th point can be obtained directly by XORing together those direction numbers corresponding to nonzero bits in the Gray code of $j$ , as described above.

# 7.8.1 The Latin Hypercube

We mention here the unrelated technique of Latin square or Latin hypercube sampling, which is useful when you must sample an $N$ -dimensional space exceedingly sparsely, at $M$ points. For example, you may want to test the crashworthiness of cars as a simultaneous function of four different design parameters, but with a budget of only three expendable cars. (The issue is not whether this is a good plan — it isn’t — but rather how to make the best of the situation!)

The idea is to partition each design parameter (dimension) into $M$ segments, so that the whole space is partitioned into $\mathbf { \Phi } _ { M ^ { N } }$ cells. (You can choose the segments in each dimension to be equal or unequal, according to taste.) With four parameters and three cars, for example, you end up with $3 \times 3 \times 3 \times 3 = 8 1$ cells.

Next, choose $M$ cells to contain the sample points by the following algorithm: Randomly choose one of the $M ^ { N }$ cells for the first point. Now eliminate all cells that agree with this point on any of its parameters (that is, cross out all cells in the same row, column, etc.), leaving $( M - 1 ) ^ { N }$ candidates. Randomly choose one of these, eliminate new rows and columns, and continue the process until there is only one cell left, which then contains the final sample point.

The result of this construction is that each design parameter will have been tested in every one of its subranges. If the response of the system under test is dominated by one of the design parameters (the main effect), that parameter will be found with this sampling technique. On the other hand, if there are important interaction effects among different design parameters, then the Latin hypercube gives no particular advantage. Use with care.

There is a large field in statistics that deals with design of experiments. A brief pedagogical introduction is [5].

# CITED REFERENCES AND FURTHER READING:

Halton, J.H. 1960, “On the Efficiency of Certain Quasi-Random Sequences of Points in Evaluating Multi-dimensional Integrals,” Numerische Mathematik, vol. 2, pp. 84–90.[1]   
Bratley P., and Fox, B.L. 1988, “Implementing Sobol’s Quasirandom Sequence Generator,” ACM Transactions on Mathematical Software, vol.14, pp. 88-100.[2]   
Lambert, J.P. 1988, “Quasi-Random Sequences in Numerical Practice,” in Numerical Mathematics— Singapore 1988, ISNM vol.86,R.P.Agarwal, Y.M. Chow,and S.J.Wilson,eds. (Basel: Birkhäuser), pp. 273–284.   
Niederreiter, H. 1988, “Quasi-Monte Carlo Methods for Multidimensional Numerical Integration.” in Numerical Integration III, ISNM vol. 85, H. Brass and G. Hämmerlin, eds. (Basel: Birkhäuser), pp. 157–171.   
Sobol’, I.M. 1967, “On the Distribution of Points in a Cube and the Approximate Evaluation of Integrals,” USSR Computational Mathematics and Mathematical Physics, vol. 7, no. 4, pp. 86–112.[3]   
Antonov, I.A., and Saleev, V.M 1979, “An Economic Method of Computing $l p _ { t }$ Sequences,” USSR Computational Mathematics and Mathematical Physics,vol.19,no.1，pp.252- 256.[4]   
Dunn, O.J., and Clark, V.A. 1974, Applied Statistics: Analysis of Variance and Regression (New York, Wiley) [discusses Latin Square].   
Czitrom, V. 1999, “One-Factor-at-a-Time Versus Designed Experiments,” The American Statistician,vol.53,pp.126-131,online at http://www.amstat.org/publications/tas/ czitrom.pdf.[5]

# 7.9 Adaptive and Recursive Monte Carlo Methods

This section discusses more advanced techniques of Monte Carlo integration. As examples of the use of these techniques, we include two rather different, fairly sophisticated, multidimensional Monte Carlo codes: vegas [1,2], and miser [4]. The techniques that we discuss all fall under the general rubric of reduction of variance (-7.7), but are otherwise quite distinct.

# 7.9.1 Importance Sampling

The use of importance sampling was already implicit in equations (7.7.6) and (7.7.7). We now return to it in a slightly more formal way. Suppose that an integrand $f$ can be written as the product of a function $h$ that is almost constant times another, positive, function $g$ . Then its integral over a multidimensional volume $V$ is

$$
\int f d V = \int ( f / g ) g d V = \int h g d V
$$

In equation (7.7.7) we interpreted equation (7.9.1) as suggesting a change of variable to $G$ , the indefinite integral of $g$ . That made $g d V$ a perfect differential. We then proceeded to use the basic theorem of Monte Carlo integration, equation (7.7.1). A more general interpretation of equation (7.9.1) is that we can integrate $f$ by instead sampling $h$ — not, however, with uniform probability density $d V$ , but rather with nonuniform density $g d V$ . In this second interpretation, the first interpretation follows as the special case, where the means of generating the nonuniform sampling of $g d V$ is via the transformation method, using the indefinite integral $G$ (see $\ S 7 . 3$ ).

More directly, one can go back and generalize the basic theorem (7.7.1) to the case of nonuniform sampling: Suppose that points $x _ { i }$ are chosen within the volume $V$ with a probability density $p$ satisfying

$$
\int p d V = 1
$$

The generalized fundamental theorem is that the integral of any function $f$ is estimated, using $N$ sample points $x _ { 0 } , \ldots , x _ { N - 1 }$ , by

$$
I \equiv \int f d V = \int \frac { f } { p } p d V \approx \left. \frac { f } { p } \right. \pm \sqrt { \frac { \left. f ^ { 2 } / p ^ { 2 } \right. - \left. f / p \right. ^ { 2 } } { N } }
$$

where angle brackets denote arithmetic means over the $N$ points, exactly as in equation (7.7.2). As in equation (7.7.1), the “plus-or-minus” term is a one standard deviation error estimate. Notice that equation (7.7.1) is in fact the special case of equation (7.9.3), with $p = { \mathrm { c o n s t a n t } } =$ $1 / V$ .

What is the best choice for the sampling density $p \mathrm { ? }$ Intuitively, we have already seen that the idea is to make $h = f / p$ as close to constant as possible. We can be more rigorous by focusing on the numerator inside the square root in equation (7.9.3), which is the variance per sample point. Both angle brackets are themselves Monte Carlo estimators of integrals, so we can write

$$
S \equiv \left. { \frac { f ^ { 2 } } { p ^ { 2 } } } \right. - \left. { \frac { f } { p } } \right. ^ { 2 } \approx \int { \frac { f ^ { 2 } } { p ^ { 2 } } } p d V - \left[ \int { \frac { f } { p } } \ p d V \right] ^ { 2 } = \int { \frac { f ^ { 2 } } { p } } \ d V - \left[ \int f d V \right] ^ { 2 }
$$

We now find the optimal $p$ subject to the constraint equation (7.9.2) by the functional variation

$$
0 = { \frac { \delta } { \delta p } } \left( \int { \frac { f ^ { 2 } } { p } } d V - \left[ \int f d V \right] ^ { 2 } + \lambda \int p d V \right)
$$

with $\lambda$ a Lagrange multiplier. Note that the middle term does not depend on $p$ . The variation (which comes inside the integrals) gives $0 = - f ^ { 2 } / p ^ { 2 } + \lambda$ or

$$
p = { \frac { | f | } { \sqrt { \lambda } } } = { \frac { | f | } { \int | f | d V } }
$$

where $\lambda$ has been chosen to enforce the constraint (7.9.2).

If $f$ has one sign in the region of integration, then we get the obvious result that the optimal choice of $p$ — if one can figure out a practical way of effecting the sampling — is that it be proportional to $\mid f \mid$ . Then the variance is reduced to zero. Not so obvious, but seen

to be true, is the fact that $p \propto | f |$ is optimal even if $f$ takes on both signs. In that case the variance per sample point (from equations 7.9.4 and 7.9.6) is

$$
S = S _ { \mathrm { o p t i m a l } } = \left( \int | f | d V \right) ^ { 2 } - \left( \int f d V \right) ^ { 2 }
$$

One curiosity is that one can add a constant to the integrand to make it all of one sign, since this changes the integral by a known amount, constant $\times V$ . Then, the optimal choice of $\boldsymbol { p }$ always gives zero variance, that is, a perfectly accurate integral! The resolution of this seeming paradox (already mentioned at the end of $\ S 7 . 7 )$ is that perfect knowledge of $p$ in equation (7.9.6) requires perfect knowledge of $\textstyle \int | f | d V$ , which is tantamount to already knowing the integral you are trying to compute!

If your function $f$ takes on a known constant value in most of the volume $V$ , it is certainly a good idea to add a constant so as to make that value zero. Having done that, the accuracy attainable by importance sampling depends in practice not on how small equation (7.9.7) is, but rather on how small is equation (7.9.4) for an implementable $p$ , likely only a crude approximation to the ideal.

# 7.9.2 Stratified Sampling

The idea of stratified sampling is quite different from importance sampling. Let us expand our notation slightly and let $\langle \langle f \rangle \rangle$ denote the true average of the function $f$ over the volume $V$ (namely the integral divided by $V$ ), while $\langle f \rangle$ denotes as before the simplest (uniformly sampled) Monte Carlo estimator of that average:

$$
\langle \langle f \rangle \rangle \equiv { \frac { 1 } { V } } \int f d V \qquad \langle f \rangle \equiv { \frac { 1 } { N } } \sum _ { i } f ( x _ { i } )
$$

The variance of the estimator, $\operatorname { V a r } \left( \langle f \rangle \right)$ , which measures the square of the error of the Monte Carlo integration, is asymptotically related to the variance of the function, $\operatorname { V a r } \left( f \right) \equiv \langle \langle f ^ { 2 } \rangle \rangle -$ $\langle \langle f \rangle \rangle ^ { 2 }$ , by the relation

$$
\operatorname { V a r } \left( \langle f \rangle \right) = { \frac { \operatorname { V a r } \left( f \right) } { N } }
$$

(compare equation 7.7.1).

Suppose we divide the volume $V$ into two equal, disjoint subvolumes, denoted $a$ and $b$ , and sample $N / 2$ points in each subvolume. Then another estimator for $\langle \langle f \rangle \rangle$ , different from equation (7.9.8), which we denote $\langle f \rangle ^ { \prime }$ , is

$$
\begin{array} { r } { \langle f \rangle ^ { \prime } \equiv \frac { 1 } { 2 } ( \langle f \rangle _ { a } + \langle f \rangle _ { b } ) } \end{array}
$$

in other words, the mean of the sample averages in the two half-regions. The variance of estimator (7.9.10) is given by

$$
\begin{array} { r } { \mathrm { { V a r } } \left( \langle f \rangle ^ { \prime } \right) = \displaystyle \frac { 1 } { 4 } \left[ { \mathrm { V a r } } \left( \langle f \rangle _ { a } \right) + { \mathrm { V a r } } \left( \langle f \rangle _ { b } \right) \right] } \\ { = \displaystyle \frac { 1 } { 4 } \left[ \frac { { \mathrm { V a r } } _ { a } \left( f \right) } { N / 2 } + \frac { { \mathrm { V a r } } _ { b } \left( f \right) } { N / 2 } \right] } \\ { = \displaystyle \frac { 1 } { 2 N } \left[ { \mathrm { V a r } } _ { a } \left( f \right) + { \mathrm { V a r } } _ { b } \left( f \right) \right] } \end{array}
$$

Here $\operatorname { V a r } _ { a } \left( f \right)$ denotes the variance of $f$ in subregion $a$ , that is, $\langle \langle f ^ { 2 } \rangle \rangle _ { a } - \langle \langle f \rangle \rangle _ { a } ^ { 2 }$ , and correspondingly for $b$ .

From the definitions already given, it is not difficult to prove the relation

$$
\begin{array} { r } { \mathrm { { V a r } } \left( f \right) = \frac { 1 } { 2 } \left[ \mathrm { { V a r } } _ { a } \left( f \right) + { \mathrm { V a r } } _ { b } \left( f \right) \right] + \frac { 1 } { 4 } \left( \langle \langle f \rangle \rangle _ { a } - \langle \langle f \rangle \rangle _ { b } \right) ^ { 2 } } \end{array}
$$

(In physics, this formula for combining second moments is the “parallel axis theorem.”) Comparing equations (7.9.9), (7.9.11), and (7.9.12), one sees that the stratified (into two subvolumes) sampling gives a variance that is never larger than the simple Monte Carlo case — and smaller whenever the means of the stratified samples, $\langle \langle f \rangle \rangle _ { a }$ and $\langle \langle f \rangle \rangle _ { b }$ , are different.

We have not yet exploited the possibility of sampling the two subvolumes with different numbers of points, say $N _ { a }$ in subregion $a$ and $N _ { b } \equiv N - N _ { a }$ in subregion $b$ . Let us do so now. Then the variance of the estimator is

$$
\mathrm { { V a r } } \left( \left. f \right. ^ { \prime } \right) = \frac { 1 } { 4 } \left[ \frac { \mathrm { { V a r } } _ { a } \left( f \right) } { N _ { a } } + \frac { \mathrm { { V a r } } _ { b } \left( f \right) } { N - N _ { a } } \right]
$$

which is minimized (one can easily verify) when

$$
\frac { N _ { a } } { N } = \frac { \sigma _ { a } } { \sigma _ { a } + \sigma _ { b } }
$$

Here we have adopted the shorthand notation $\sigma _ { a } \equiv [ \mathrm { V a r } _ { a } \left( f \right) ] ^ { 1 / 2 }$ , and correspondingly for $b$ . If $N _ { a }$ satisfies equation (7.9.14), then equation (7.9.13) reduces to

$$
\mathrm { V a r } \left( \langle f \rangle ^ { \prime } \right) = \frac { ( \sigma _ { a } + \sigma _ { b } ) ^ { 2 } } { 4 N }
$$

Equation (7.9.15) reduces to equation (7.9.9) if $\operatorname { V a r } \left( f \right) = \operatorname { V a r } _ { a } \left( f \right) = \operatorname { V a r } _ { b } \left( f \right)$ , in which case stratifying the sample makes no difference.

A standard way to generalize the above result is to consider the volume $V$ divided into more than two equal subregions. One can readily obtain the result that the optimal allocation of sample points among the regions is to have the number of points in each region $j$ proportional to $\sigma _ { j }$ (that is, the square root of the variance of the function $f$ in that subregion). In spaces of high dimensionality (say $d \gtrsim 4 ,$ this is not in practice very useful, however. Dividing a volume into $K$ segments along each dimension implies $K ^ { d }$ subvolumes, typically much too large a number when one contemplates estimating all the corresponding $\sigma _ { j }$ ’s.

# 7.9.3 Mixed Strategies

Importance sampling and stratified sampling seem, at first sight, inconsistent with each other. The former concentrates sample points where the magnitude of the integrand $\mid f \mid$ is largest, the latter where the variance of $f$ is largest. How can both be right?

The answer is that (like so much else in life) it all depends on what you know and how well you know it. Importance sampling depends on already knowing some approximation to your integral, so that you are able to generate random points $x _ { i }$ with the desired probability density $p$ . To the extent that your $p$ is not ideal, you are left with an error that decreases only as $N ^ { - 1 / 2 }$ . Things are particularly bad if your $p$ is far from ideal in a region where the integrand $f$ is changing rapidly, since then the sampled function $h = f / p$ will have a large variance. Importance sampling works by smoothing the values of the sampled function $h$ and is effective only to the extent that you succeed in this.

Stratified sampling, by contrast, does not necessarily require that you know anything about $f$ . Stratified sampling works by smoothing out the fluctuations of the number of points in subregions, not by smoothing the values of the points. The simplest stratified strategy, dividing $V$ into $N$ equal subregions and choosing one point randomly in each subregion, already gives a method whose error decreases asymptotically as $N ^ { - 1 }$ , much faster than $N ^ { - 1 / 2 }$ . (Note that quasi-random numbers, $\ S 7 . 8$ , are another way of smoothing fluctuations in the density of points, giving nearly as good a result as the “blind” stratification strategy.)

However, “asymptotically” is an important caveat: For example, if the integrand is negligible in all but a single subregion, then the resulting one-sample integration is all but useless. Information, even very crude, allowing importance sampling to put many points in the active subregion would be much better than blind stratified sampling.

Stratified sampling really comes into its own if you have some way of estimating the variances, so that you can put unequal numbers of points in different subregions, according to (7.9.14) or its generalizations, and if you can find a way of dividing a region into a practical number of subregions (notably not $K ^ { d }$ with large dimension $d$ ), while yet significantly reducing the variance of the function in each subregion compared to its variance in the full volume. Doing this requires a lot of knowledge about $f$ , though different knowledge from what is required for importance sampling.

In practice, importance sampling and stratified sampling are not incompatible. In many, if not most, cases of interest, the integrand $f$ is small everywhere in $V$ except for a small fractional volume of “active regions.” In these regions the magnitude of $\mid f \mid$ and the standard deviation $\sigma = [ \mathrm { V a r } \left( f \right) ] ^ { 1 / 2 }$ are comparable in size, so both techniques will give about the same concentration of points. In more sophisticated implementations, it is also possible to “nest” the two techniques, so that, e.g., importance sampling on a crude grid is followed by stratification within each grid cell.

# 7.9.4 Adaptive Monte Carlo: VEGAS

The VEGAS algorithm, invented by Peter Lepage [1,2], is widely used for multidimensional integrals that occur in elementary particle physics. VEGAS is primarily based on importance sampling, but it also does some stratified sampling if the dimension $d$ is small enough to avoid $K ^ { d }$ explosion (specifically, if $( K / 2 ) ^ { d } < N / 2$ , with $N$ the number of sample points). The basic technique for importance sampling in VEGAS is to construct, adaptively, a multidimensional weight function $g$ that is separable,

$$
p \propto g ( x , y , z , \ldots ) = g _ { x } ( x ) g _ { y } ( y ) g _ { z } ( z ) \ldots
$$

Such a function avoids the $K ^ { d }$ explosion in two ways: (i) It can be stored in the computer as $d$ separate one-dimensional functions, each defined by $K$ tabulated values, say — so that $K \times d$ replaces $K ^ { d }$ . (ii) It can be sampled as a probability density by consecutively sampling the $d$ one-dimensional functions to obtain coordinate vector components $( x , y , z , \ldots )$ .

The optimal separable weight function can be shown to be [1]

$$
g _ { x } ( x ) \propto \left[ \int d y \int d z \ldots \frac { f ^ { 2 } ( x , y , z , \ldots ) } { g _ { y } ( y ) g _ { z } ( z ) \ldots } \right] ^ { 1 / 2 }
$$

(and correspondingly for $y , z , \ldots )$ . Notice that this reduces to $g \propto | f |$ (7.9.6) in one dimension. Equation (7.9.17) immediately suggests VEGAS’ adaptive strategy: Given a set of $g$ -functions (initially all constant, say), one samples the function $f$ , accumulating not only the overall estimator of the integral, but also the $K d$ estimators ( $K$ subdivisions of the independent variable in each of $d$ dimensions) of the right-hand side of equation (7.9.17). These then determine improved $g$ functions for the next iteration.

When the integrand $f$ is concentrated in one, or at most a few, regions in $d$ -space, then the weight function $g$ ’s quickly become large at coordinate values that are the projections of these regions onto the coordinate axes. The accuracy of the Monte Carlo integration is then enormously enhanced over what simple Monte Carlo would give.

The weakness of VEGAS is the obvious one: To the extent that the projection of the function $f$ onto individual coordinate directions is uniform, VEGAS gives no concentration of sample points in those dimensions. The worst case for VEGAS, e.g., is an integrand that is concentrated close to a body diagonal line, e.g., one from $( 0 , 0 , 0 , \ldots )$ to $( 1 , 1 , 1 , \ldots )$ . Since this geometry is completely nonseparable, VEGAS can give no advantage at all. More generally, VEGAS may not do well when the integrand is concentrated in one-dimensional (or higher) curved trajectories (or hypersurfaces), unless these happen to be oriented close to the coordinate directions.

The routine vegas that follows is essentially Lepage’s standard version, minimally modified to conform to our conventions. (We thank Lepage for permission to reproduce the program here.) For consistency with other versions of the VEGAS algorithm in circulation, we have preserved original variable names. The parameter NDMX is what we have called $K$ , the maximum number of increments along each axis; MXDIM is the maximum value of $d$ ; some other parameters are explained in the comments.

The vegas routine performs $m = \mathtt { i } \mathtt { t m x }$ statistically independent evaluations of the desired integral, each with $N = \mathtt { n c a l 1 }$ function evaluations. While statistically independent, these iterations do assist each other, since each one is used to refine the sampling grid for the next one. The results of all iterations are combined into a single best answer, and its estimated error, by the relations

$$
I _ { \mathrm { b e s t } } = \sum _ { i = 0 } ^ { m - 1 } \frac { I _ { i } } { \sigma _ { i } ^ { 2 } } \bigg / \sum _ { i = 0 } ^ { m - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \qquad \sigma _ { \mathrm { b e s t } } = \left( \sum _ { i = 0 } ^ { m - 1 } \frac { 1 } { \sigma _ { i } ^ { 2 } } \right) ^ { - 1 / 2 }
$$

Also returned is the quantity

$$
\chi ^ { 2 } / m \equiv \frac { 1 } { m - 1 } \sum _ { i = 0 } ^ { m - 1 } \frac { ( I _ { i } - I _ { \mathrm { b e s t } } ) ^ { 2 } } { \sigma _ { i } ^ { 2 } }
$$

If this is significantly larger than 1, then the results of the iterations are statistically inconsistent, and the answers are suspect.

Here is the interface to vegas. (The full code is given in [3].)

void vegas(VecDoub_I &regn, Doub fxn(VecDoub_I &, const Doub), const Int init, const Int ncall, const Int itmx, const Int nprn, Doub &tgral, Doub &sd, Doub &chi2a) {

Performs Monte Carlo integration of a user-supplied ndim-dimensional function fxn over a rectangular volume specified by regn[0..2\*ndim-1], a vector consisting of ndim “lower left” coordinates of the region followed by ndim “upper right” coordinates. The integration consists of itmx iterations, each with approximately ncall calls to the function. After each iteration the grid is refined; more than 5 or 10 iterations are rarely useful. The input flag init signals whether this call is a new start or a subsequent call for additional iterations (see comments in the code). The input flag nprn (normally 0) controls the amount of diagnostic output. Returned answers are tgral (the best estimate of the integral), sd (its standard deviation), and chi2a $\cdot x ^ { 2 }$ per degree of freedom, an indicator of whether consistent results are being obtained). See text for further details.

The input flag init can be used to advantage. One might have a call with init $\scriptstyle = 0$ , ncall $\mathtt { . } 0 0 0$ , itmx $\mathtt { . = 5 }$ immediately followed by a call with init $= 1$ , ncal $\mathtt { L } = 1 0 0 0 0 0$ , itmx $^ { = 1 }$ . The effect would be to develop a sampling grid over five iterations of a small number of samples, then to do a single high accuracy integration on the optimized grid.

To use vegas for the torus example discussed in $\ S 7 . 7$ (the density integrand only, say), the function fxn would be

Doub torusfunc(const VecDoub &x, const Doub wgt) { Doub den $=$ exp(5.\*x[2]); if (SQR(x[2]) $^ +$ SQR(sqrt(SQR(x[0])+SQR(x[1]))-3.) <= 1.) return den; else return 0.;   
}

#

and the main code would be

Doub tgral, sd, chi2a;   
VecDoub regn(6);   
regn[0] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ; regn[3] $\mathit { \Theta } = \mathit { \Theta } 4 , \mathit { \Theta } ;$ regn[1] $=$ -3.; regn[4] $= ~ 4 .$ ;   
regn[2] $\ c = - 1$ .; regn[5] $\smash { = ~ 1 , }$ ;   
vegas(regn,torusfunc,0,10000,10,0,tgral,sd,chi2a);   
vegas(regn,torusfunc,1,900000,1,0,tgral,sd,chi2a);

Note that the user-supplied integrand function, fxn, has an argument wgt in addition to the expected evaluation point $\mathbf { x }$ . In most applications you ignore wgt inside the function. Occasionally, however, you may want to integrate some additional function or functions along with the principal function $f$ . The integral of any such function $g$ can be estimated by

$$
I _ { g } = \sum _ { i } w _ { i } g ( \mathbf { x } )
$$

where the $w _ { i }$ ’s and $\mathbf { X }$ ’s are the arguments wgt and $\mathtt { x }$ , respectively. It is straightforward to accumulate this sum inside your function $\tt f x n$ and to pass the answer back to your main program via global variables. Of course, $g ( \mathbf { x } )$ had better resemble the principal function $f$ to some degree, since the sampling will be optimized for $f$ .

The full listing of vegas is given in a Webnote [3].

# 7.9.5 Recursive Stratified Sampling

The problem with stratified sampling, we have seen, is that it may not avoid the $K ^ { d }$ explosion inherent in the obvious, Cartesian, tessellation of a $d$ -dimensional volume. A technique called recursive stratified sampling [4] attempts to do this by successive bisections of a volume, not along all $d$ dimensions, but rather along only one dimension at a time. The starting points are equations (7.9.10) and (7.9.13), applied to bisections of successively smaller subregions.

Suppose that we have a quota of $N$ evaluations of the function $f$ and want to evaluate $\langle f \rangle ^ { \prime }$ in the rectangular parallelepiped region $R = ( { \bf x } _ { a } , { \bf x } _ { b } )$ . (We denote such a region by the two coordinate vectors of its diagonally opposite corners.) First, we allocate a fraction $\boldsymbol { p }$ of $N$ toward exploring the variance of $f$ in $R$ : We sample $p N$ function values uniformly in $R$ and accumulate the sums that will give the $d$ different pairs of variances corresponding to the $d$ different coordinate directions along which $R$ can be bisected. In other words, in $p N$ samples, we estimate $\operatorname { V a r } \left( f \right)$ in each of the regions resulting from a possible bisection of $R$ ,

$$
\begin{array} { r l } & { R _ { a i } \equiv ( \mathbf { x } _ { a } , \mathbf { x } _ { b } - \frac { 1 } { 2 } \mathbf { e } _ { i } \cdot ( \mathbf { x } _ { b } - \mathbf { x } _ { a } ) \mathbf { e } _ { i } ) } \\ & { R _ { b i } \equiv ( \mathbf { x } _ { a } + \frac { 1 } { 2 } \mathbf { e } _ { i } \cdot ( \mathbf { x } _ { b } - \mathbf { x } _ { a } ) \mathbf { e } _ { i } , \mathbf { x } _ { b } ) } \end{array}
$$

Here $\mathbf { e } _ { i }$ is the unit vector in the $i$ th coordinate direction, $i = 1 , 2 , \ldots , d$ .

Second, we inspect the variances to find the most favorable dimension $i$ to bisect. By equation (7.9.15), we could, for example, choose that $i$ for which the sum of the square roots of the variance estimators in regions $R _ { a i }$ and $R _ { b i }$ is minimized. (Actually, as we will explain, we do something slightly different.)

Third, we allocate the remaining $( 1 - p ) N$ function evaluations between the regions $R _ { a i }$ and $R _ { b i }$ . If we used equation (7.9.15) to choose $i$ , we should do this allocation according to equation (7.9.14).

We now have two parallelepipeds, each with its own allocation of function evaluations for estimating the mean of $f$ . Our “RSS” algorithm now shows itself to be recursive: To evaluate the mean in each region, we go back to the sentence beginning “First,...” in the paragraph above equation (7.9.21). (Of course, when the allocation of points to a region falls below some number, we resort to simple Monte Carlo rather than continue with the recursion.)

Finally, we combine the means and also estimated variances of the two subvolumes using equation (7.9.10) and the first line of equation (7.9.11).

This completes the RSS algorithm in its simplest form. Before we describe some additional tricks under the general rubric of “implementation details,” we need to return briefly to equations $( 7 . 9 . 1 3 ) - ( 7 . 9 . 1 5 )$ and derive the equations that we actually use instead of these. The right-hand side of equation (7.9.13) applies the familiar scaling law of equation (7.9.9) twice, once to $a$ and again to $b$ . This would be correct if the estimates $\langle f \rangle _ { a }$ and $\langle f \rangle _ { b }$ were each made by simple Monte Carlo, with uniformly random sample points. However, the two estimates of the mean are in fact made recursively. Thus, there is no reason to expect equation (7.9.9) to hold. Rather, we might substitute for equation (7.9.13) the relation,

$$
\operatorname { V a r } \left( \langle f \rangle ^ { \prime } \right) = \frac { 1 } { 4 } \left[ \frac { \operatorname { V a r } _ { a } { \left( f \right) } } { N _ { a } ^ { \alpha } } + \frac { \operatorname { V a r } _ { b } { \left( f \right) } } { ( N - N _ { a } ) ^ { \alpha } } \right]
$$

where $\alpha$ is an unknown constant $\geq 1$ (the case of equality corresponding to simple Monte Carlo). In that case, a short calculation shows that $\mathrm { V a r } \overset { \cdot } { ( } \langle f \rangle ^ { \prime } )$ is minimized when

$$
\frac { N _ { a } } { N } = \frac { \mathrm { V a r } _ { a } \left( f \right) ^ { 1 / \left( 1 + \alpha \right) } } { \mathrm { V a r } _ { a } \left( f \right) ^ { 1 / \left( 1 + \alpha \right) } + \mathrm { V a r } _ { b } \left( f \right) ^ { 1 / \left( 1 + \alpha \right) } }
$$

and that its minimum value is

$$
\begin{array} { r } { \mathrm { V a r } \left( \langle f \rangle ^ { \prime } \right) \propto \left[ \mathrm { V a r } _ { a } \left( f \right) ^ { 1 / ( 1 + \alpha ) } + \mathrm { V a r } _ { b } \left( f \right) ^ { 1 / ( 1 + \alpha ) } \right] ^ { 1 + \alpha } } \end{array}
$$

Equations $( 7 . 9 . 2 2 ) - ( 7 . 9 . 2 4 )$ reduce to equations $( 7 . 9 . 1 3 ) - ( 7 . 9 . 1 5 )$ when $\alpha = 1$ . Numerical experiments to find a self-consistent value for $\alpha$ find that $\alpha \approx 2$ . That is, when equation (7.9.23) with $\alpha = 2$ is used recursively to allocate sample opportunities, the observed variance of the RSS algorithm goes approximately as $N ^ { - 2 }$ , while any other value of $\alpha$ in equation (7.9.23) gives a poorer fall-off. (The sensitivity to $\alpha$ is, however, not very great; it is not known whether $\alpha = 2$ is an analytically justifiable result or only a useful heuristic.)

The principal difference between miser’s implementation and the algorithm as described thus far lies in how the variances on the right-hand side of equation (7.9.23) are estimated. We find empirically that it is somewhat more robust to use the square of the difference of maximum and minimum sampled function values, instead of the genuine second moment of the samples. This estimator is of course increasingly biased with increasing sample size; however, equation (7.9.23) uses it only to compare two subvolumes $a$ and $b$ ) having approximately equal numbers of samples. The “max minus min” estimator proves its worth when the preliminary sampling yields only a single point, or a small number of points, in active regions of the integrand. In many realistic cases, these are indicators of nearby regions of even greater importance, and it is useful to let them attract the greater sampling weight that “max minus min” provides.

A second modification embodied in the code is the introduction of a “dithering parameter,” dith, whose nonzero value causes subvolumes to be divided not exactly down the middle, but rather into fractions $0 . 5 \pm$ dith, with the sign of the $\pm$ randomly chosen by a built-in random number routine. Normally dith can be set to zero. However, there is a large advantage in taking dith to be nonzero if some special symmetry of the integrand puts the active region exactly at the midpoint of the region, or at the center of some power-of-two submultiple of the region. One wants to avoid the extreme case of the active region being evenly divided into $2 ^ { d }$ abutting corners of a $d$ -dimensional space. A typical nonzero value of dith, on those occasions when it is useful, might be 0:1. Of course, when the dithering parameter is nonzero, we must take the differing sizes of the subvolumes into account; the code does this through the variable fracl.

One final feature in the code deserves mention. The RSS algorithm uses a single set of sample points to evaluate equation (7.9.23) in all $d$ directions. At the bottom levels of the recursion, the number of sample points can be quite small. Although rare, it can happen that in one direction all the samples are in one half of the volume; in that case, that direction is ignored as a candidate for bifurcation. Even more rare is the possibility that all of the samples are in one half of the volume in all directions. In this case, a random direction is chosen. If this happens too often in your application, then you should increase MNPT (see line if $( \mathrm { j } \mathsf { b } \ = \ - 1 ) \ldots$ in the code).

Note that miser, as given, returns as ave an estimate of the average function value $\langle \langle f \rangle \rangle$ , not the integral of $f$ over the region. The routine vegas, adopting the other convention, returns as tgral the integral. The two conventions are of course trivially related, by equation (7.9.8), since the volume $V$ of the rectangular region is known.

The interface to the miser routine is this:

# void miser(Doub func(VecDoub_I &), VecDoub_I &regn, const Int npts, const Doub dith, Doub &ave, Doub &var) {

Monte Carlo samples a user-supplied ndim-dimensional function func in a rectangular volume specified by regn[0..2\*ndim-1], a vector consisting of ndim “lower-left” coordinates of the region followed by ndim “upper-right” coordinates. The function is sampled a total of npts times, at locations determined by the method of recursive stratified sampling. The mean value of the function in the region is returned as ave; an estimate of the statistical uncertainty of ave (square of standard deviation) is returned as var. The input parameter dith should normally be set to zero, but can be set to (e.g.) 0.1 if func’s active region falls on the boundary of a power-of-two subdivision of region.

Implementing code for the torus problem in $\ S 7 . 7$ is

Doub torusfunc(const VecDoub &x) {Doub den $=$ exp(5.\*x[2]);if (SQR(x[2]) $^ +$ SQR(sqrt(SQR(x[0])+SQR(x[1]))-3.) $< = ~ 1 .$ ) return den;else return 0.;  
}

and the main code is

Doub ave, var, tgral, sd, vol = 3.\*7.\*2.;   
regn[0] $\begin{array} { r l } { \mathbf { \Phi } } & { { } = \mathbf { \Phi } _ { 1 } \qquad } \end{array}$ ; regn[3] $= ~ 4 .$ ;   
regn[1] $=$ -3.; regn[4] $\mathit { \Theta } = \mathit { \Theta } 4 .$ ;   
regn[2] $\ c = - 1$ .; regn[5] $\mathit { \Theta } = \mathit { \Theta } 1 \cdot$ ;   
miser(torusfunc,regn,1000000,0.,ave,var);   
tgral $=$ ave\*vol;   
sd $=$ sqrt(var)\*vol;

(Actually, miser is not particularly well-suited to this problem.)

The complete listing of miser is given in a Webnote [5]. The miser routine calls the short function ranpt to get a random point within a specified $d$ -dimensional region. The version of ranpt in the Webnote makes consecutive calls to a uniform random number generator and does the obvious scaling. One can easily modify ranpt to generate its points via the quasi-random routine sobseq $( \ S 7 . 8 )$ . We find that miser with sobseq can be considerably more accurate than miser with uniform random deviates. Since the use of RSS and the use of quasi-random numbers are completely separable, however, we have not made the code given here dependent on sobseq. A similar remark might be made regarding importance sampling, which could in principle be combined with RSS. (One could in principle combine vegas and miser, although the programming would be intricate.)

# CITED REFERENCES AND FURTHER READING:

Hammersley, J.M. and Handscomb, D.C. 1964, Monte Carlo Methods (London: Methuen).   
Kalos, M.H. and Whitlock, P.A. 1986, Monte Carlo Methods (New York: Wiley).   
Bratley, P., Fox, B.L., and Schrage, E.L. 1983, A Guide to Simulation, 2nd ed. (New York: Springer).   
Lepage, G.P. 1978, “A New Algorithm for Adaptive Multidimensional Integration,” Journal of Computational Physics,vol. 27,pp.192-203.[1]   
Lepage, G.P. 1980, “VEGAS: An Adaptive Multidimensional Integration Program,” Publication CLNS-80/447, Cornell University.[2]   
Numerical Recipes Software 2007, “Complete VEGAS Code Listing,” Numerical Recipes Webnote No.9,at http://www.nr.com/webnotes?9 [3]   
Press, W.H., and Farrar, G.R. 1990, “Recursive Stratified Sampling for Multidimensional Monte Carlo Integration,” Computers in Physics, vol. 4, pp. 190–195.[4]   
Numerical Recipes Software 2007, “Complete Miser Code Listing,” Numerical Recipes Webnote No.10,athttp://www.nr.com/webnotes?10 [5]

# 8.0 Introduction

This chapter almost doesn’t belong in a book on numerical methods: Sorting and selection are bread-and-butter topics in the standard computer science curriculum. However, some review of the techniques for sorting, from the perspective of scientific computing, will prove useful in subsequent chapters. We can develop some standard interfaces for later use, and also illustrate the usefulness of templates in object-oriented programming.

In conjunction with numerical work, sorting is frequently necessary when data (either experimental or numerically generated) are being processed. One has tables or lists of numbers, representing one or more independent (or control) variables, and one or more dependent (or measured) variables. One may wish to arrange these data, in various circumstances, in order by one or another of these variables. Alternatively, one may simply wish to identify the median value or the upper quartile value of one of the lists of values. (These kinds of values are generically called quantiles.) This task, closely related to sorting, is called selection.

Here, more specifically, are the tasks that this chapter will deal with:

- Sort, i.e., rearrange, an array of numbers into numerical order.   
- Rearrange an array into numerical order while performing the corresponding rearrangement of one or more additional arrays, so that the correspondence between elements in all arrays is maintained.   
Given an array, prepare an index table for it, i.e., a table of pointers telling which number array element comes first in numerical order, which second, and so on.   
- Given an array, prepare a rank table for it, i.e., a table telling what is the numerical rank of the first array element, the second array element, and so on.   
- Select the $M$ th largest element from an array.   
- Select the $M$ th largest value, or estimate arbitrary quantile values, from a data stream in one pass (i.e., without storing the stream for later processing).   
- Given a bunch of equivalence relations, organize them into equivalence classes.

For the basic task of sorting $N$ elements, the best algorithms require on the order of several times $N \log _ { 2 } N$ operations. The algorithm inventor tries to reduce the constant in front of this estimate to as small a value as possible. Two of the best algorithms are Quicksort (-8.2), invented by the inimitable C.A.R. Hoare, and Heapsort (-8.3), invented by J.W.J. Williams.

For large $N$ $\mathrm { \Delta \left( s a y \right) > \Delta 1 0 0 0 }$ ), Quicksort is faster, on most machines, by a factor of 1.5 or 2; it requires a bit of extra memory, however, and is a moderately complicated program. Heapsort is a true “sort in place,” and is somewhat more compact to program and therefore a bit easier to modify for special purposes. On balance, we recommend Quicksort because of its speed, but we implement both routines.

For small $N$ one does better to use an algorithm whose operation count goes as a higher, i.e., poorer, power of $N$ , if the constant in front is small enough. For $N < 2 0$ , roughly, the method of straight insertion (-8.1) is concise and fast enough. We include it with some trepidation: It is an $N ^ { 2 }$ algorithm, whose potential for misuse (by using it for too large an $N$ ) is great. The resultant waste of computer resource can be so awesome that we were tempted not to include any $N ^ { 2 }$ routine at all. We will draw the line, however, at the inefficient $N ^ { 2 }$ algorithm, beloved of elementary computer science texts, called bubble sort. If you know what bubble sort is, wipe it from your mind; if you don’t know, make a point of never finding out!

For $N < 5 0$ , roughly, Shell’s method (-8.1), only slightly more complicated to program than straight insertion, is competitive with the more complicated Quicksort on many machines. This method goes as $N ^ { 3 / 2 }$ in the worst case, but is usually faster.

See Refs. [1,2] for further information on the subject of sorting, and for detailed references to the literature.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley).[1]   
Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapters 8– 13.[2]

# 8.1 Straight Insertion and Shell's Method

Straight insertion is an $N ^ { 2 }$ routine and should be used only for small $N$ , say $< 2 0$ .

The technique is exactly the one used by experienced card players to sort their cards: Pick out the second card and put it in order with respect to the first; then pick out the third card and insert it into the sequence among the first two; and so on until the last card has been picked out and inserted.

# sort.h template<class T>

void piksrt(NRvector<T> &arr)

Sort an array arr[0..n-1] into ascending numerical order, by straight insertion. arr is replaced on output by its sorted rearrangement.

Int i,j,n=arr.size();   
T a;   
for (j=1;j<n;j++) { a=arr[j];

Pick out each element in turn.

i=j; while (i > 0 && arr[i-1] > a) { Look for the place to insert it. arr[i] $=$ arr[i-1]; i--; } arr[i] $= \mathtt { a }$ ; Insert it. } }

Notice the use of a template in order to make the routine general for any type of NRvector, including both VecInt and VecDoub. The only thing required of the elements of type T in the vector is that they have an assignment operator and a $>$ relation. (We will generally assume that the relations $< , >$ , and $= =$ all exist.) If you try to sort a vector of elements without these properties, the compiler will complain, so you can’t go wrong.

It is a matter of taste whether to template on the element type, as above, or on the vector itself, as

# template<class T> void piksrt(T &arr)

This would seem more general, since it will work for any type T that has a subscript operator [], not just NRvectors. However, it also requires that T have some method for getting at the type of its elements, necessary for the declaration of the variable a. If T follows the conventions of STL containers, then that declaration can be written

# T::value_type a;

but if it doesn’t, then you can find yourself lost at C.

What if you also want to rearrange an array brr at the same time as you sort arr? Simply move an element of brr whenever you move an element of arr:

template<class T, class U>   
void piksr2(NRvector<T> &arr, NRvector<U> &brr)   
Sort an array arr[0..n-1] into ascending numerical order, by straight insertion, while making the corresponding rearrangement of the array brr[0..n-1].

Int i,j,n=arr.size(); T a; U b; for (j=1;j<n;j++) { Pick out each element in turn. a=arr[j]; b=brr[j]; i=j; while (i > 0 && arr[i-1] > a) { Look for the place to insert it. arr[i] $=$ arr[i-1]; brr[i] $=$ brr[i-1]; i--; } arr[i] $= a$ ; Insert it. brr[i] $= \mathrm { b }$ ; } }

Note that the types of arr and brr are separately templated, so they don’t have to be the same.

Don’t generalize this technique to the rearrangement of a larger number of arrays by sorting on one of them. Instead see $\ S 8 . 4$ .

# 8.1.1 Shell's Method

This is actually a variant on straight insertion, but a very powerful variant indeed. The rough idea, e.g., for the case of sorting 16 numbers $n _ { 0 } \ldots n _ { 1 5 }$ , is this: First sort, by straight insertion, each of the 8 groups of 2 $( n _ { 0 } , n _ { 8 } )$ , $( n _ { 1 } , n _ { 9 } )$ , . . . , $( n _ { 7 } , n _ { 1 5 } )$ . Next, sort each of the 4 groups of 4 $( n _ { 0 } , n _ { 4 } , n _ { 8 } , n _ { 1 2 } )$ , . . . , $( n _ { 3 } , n _ { 7 } , n _ { 1 1 } , n _ { 1 5 } )$ . Next sort the 2 groups of 8 records, beginning with $\left( n _ { 0 } , n _ { 2 } , n _ { 4 } , n _ { 6 } , n _ { 8 } , n _ { 1 0 } , n _ { 1 2 } , n _ { 1 4 } \right)$ . Finally, sort the whole list of 16 numbers.

Of course, only the last sort is necessary for putting the numbers into order. So what is the purpose of the previous partial sorts? The answer is that the previous sorts allow numbers efficiently to filter up or down to positions close to their final resting places. Therefore, the straight insertion passes on the final sort rarely have to go past more than a “few” elements before finding the right place. (Think of sorting a hand of cards that are already almost in order.)

The spacings between the numbers sorted on each pass through the data (8,4,2,1 in the above example) are called the increments, and a Shell sort is sometimes called a diminishing increment sort. There has been a lot of research into how to choose a good set of increments, but the optimum choice is not known. The set $\ldots , 8 , 4 , 2 , 1$ is in fact not a good choice, especially for $N$ a power of 2. A much better choice is the sequence

$$
( 3 ^ { k } - 1 ) / 2 , \ldots , 4 0 , 1 3 , 4 , 1
$$

which can be generated by the recurrence

$$
i _ { 0 } = 1 , \qquad i _ { k + 1 } = 3 i _ { k } + 1 , \quad k = 0 , 1 , \ldots
$$

It can be shown (see [1]) that for this sequence of increments the number of operations required in all is of order $N ^ { 3 / 2 }$ for the worst possible ordering of the original data. For “randomly” ordered data, the operations count goes approximately as $N ^ { 1 . 2 5 }$ , at least for $N < 6 0 0 0 0$ . For $N > 5 0$ , however, Quicksort is generally faster.

# template<class T>

# void shell(NRvector<T> &a, Int $\mathrm { m } { = } { - } 1$ )

Sort an array a[0..n-1] into ascending numerical order by Shell’s method (diminishing increment sort). a is replaced on output by its sorted rearrangement. Normally, the optional argument m should be omitted, but if it is set to a positive value, then only the first m elements of a are sorted.

Use optional argument.   
Determine the starting increment.   
Int i,j,inc, $\scriptstyle , \mathtt { n } = \mathtt { a }$ .size();   
T v;   
if ( $\mathrm { . } \mathrm { m } { > } 0 \mathrm { . }$ ) $\mathrm { ~ n ~ } =$ MIN(m,n);   
inc=1;   
do { inc $\ast = ~ 3$ ; inc++;   
} while (inc $< = \mathrm { ~ n ~ } ,$ );   
do { inc /= 3; for ( $\dot { \bf 1 } =$ inc;i<n;i++) { $\mathtt { v } = \mathtt { a }$ [i]; $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { I } } }$ ; while (a[j-inc] > v) { a[j] $= \mathtt { a }$ [j-inc]; j $- =$ inc; if (j $<$ inc) break; }

Loop over the partial sorts.

Outer loop of straight insertion.

Inner loop of straight insertion.

a[j]=v; } } while (inc > 1);

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 5$ .2.1.[1] Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 8.

# 8.2 Quicksort

Quicksort is, on most machines, on average, for large $N$ , the fastest known sorting algorithm. It is a “partition-exchange” sorting method: A “partitioning element” a is selected from the array. Then, by pairwise exchanges of elements, the original array is partitioned into two subarrays. At the end of a round of partitioning, the element a is in its final place in the array. All elements in the left subarray are $\leq \mathsf { a }$ while all elements in the right subarray are $\geq \mathsf { a }$ . The process is then repeated on the left and right subarrays independently, and so on.

The partitioning process is carried out by selecting some element, say the leftmost, as the partitioning element a. Scan a pointer up the array until you find an element $> \mathtt { a }$ , and then scan another pointer down from the end of the array until you find an element $< \mathtt { a }$ . These two elements are clearly out of place for the final partitioned array, so exchange them. Continue this process until the pointers cross. This is the right place to insert a, and that round of partitioning is done. The question of the best strategy when an element is equal to the partitioning element is subtle; see Sedgewick [1] for a discussion. (Answer: You should stop and do an exchange.)

For speed of execution, we don’t implement Quicksort using recursion. Thus the algorithm requires an auxiliary array of storage, of length $2 \log _ { 2 } N$ , which it uses as a push-down stack for keeping track of the pending subarrays. When a subarray has gotten down to some size $M$ , it becomes faster to sort it by straight insertion (-8.1), so we will do this. The optimal setting of $M$ is machine-dependent, but $M \ = \ 7$ is not too far wrong. Some people advocate leaving the short subarrays unsorted until the end, and then doing one giant insertion sort at the end. Since each element moves at most seven places, this is just as efficient as doing the sorts immediately, and saves on the overhead. However, on modern machines with a cache hierarchy, there is increased overhead when dealing with a large array all at once. We have not found any advantage in saving the insertion sorts till the end.

As already mentioned, Quicksort’s average running time is fast, but its worst case running time can be very slow: For the worst case it is, in fact, an $N ^ { 2 }$ method! And for the most straightforward implementation of Quicksort it turns out that the worst case is achieved for an input array that is already in order! This ordering of the input array might easily occur in practice. One way to avoid this is to use a little random number generator to choose a random element as the partitioning element. Another is to use instead the median of the first, middle, and last elements of the current subarray.

The great speed of Quicksort comes from the simplicity and efficiency of its inner loop. Simply adding one unnecessary test (for example, a test that your pointer has not moved off the end of the array) can almost double the running time! One avoids such unnecessary tests by placing “sentinels” at either end of the subarray being partitioned. The leftmost sentinel is $\leq \mathsf { a }$ , the rightmost $\geq \mathsf { a }$ . With the “medianof-three” selection of a partitioning element, we can use the two elements that were not the median to be the sentinels for that subarray.

Our implementation closely follows [1]:

# sort.h template<class T>

# void sort(NRvector<T> &arr, Int $\mathrm { m } { = } { - } 1$

Sort an array ar $\mathbf { \texttt { c } } [ 0 \ldots \mathbf { \texttt { n } } ^ { - 1 } ]$ into ascending numerical order using the Quicksort algorithm. arr is replaced on output by its sorted rearrangement. Normally, the optional argument m should be omitted, but if it is set to a positive value, then only the first m elements of arr are sorted.

static const Int $\mathtt { M } = 7$ , NSTAC $_ { ; = 6 4 }$ ;   
Here M is the size of subarrays sorted by straight insertion and NSTACK is the required   
auxiliary storage.   
Int i,ir,j,k,jstack $= - 1$ , $\mathtt { 1 } = 0$ , $\mathbf { n } =$ arr.size();   
T a;   
VecInt istack(NSTACK);   
if $\mathrm { m } { > } 0 \mathrm { \Omega }$ ) $\mathrm { ~ n ~ } =$ MIN(m,n); Use optional argument.   
$\mathtt { i r } \mathtt { = n - 1 }$ ;   
for (;;) { Insertion sort when subarray small enough. if (ir-l < M) { for $( \mathrm { j } { = } 1 { + } 1$ ;j<=ir;j++) { a=arr[j]; for (i=j-1;i>=l;i--) { if (arr[i] $\texttt { \textbf { < } } \texttt { \textbf { a } }$ ) break; arr[i+1] $=$ arr[i]; } arr[i+1]=a; } if (jstack < 0) break; ir=istack[jstack--]; Pop stack and begin a new round of partil=istack[jstack--]; tioning. } else { $\mathtt { k } =$ (l+ir) >> 1; Choose median of left, center, and right el-SWAP(arr[k],arr[l+1]); ements as partitioning element a. Also if (arr[l] $>$ arr[ir]) { rearrange so that a $[ 1 ] \le \mathtt { a } [ 1 + 1 ] \le \mathtt { a } [ \mathtt { i r } ]$ . SWAP(arr[l],arr[ir]); } if (arr[l+1] $>$ arr[ir]) { SWAP(arr[l+1],arr[ir]); } if (arr[l] $>$ arr[l+1]) { SWAP(arr[l],arr[l+1]); } $\dot { \bf z } = \bf { 1 } + 1$ ; Initialize pointers for partitioning. $\scriptstyle { \dot { \mathcal { I } } } = { \dot { \mathtt { I } } } \mathtt { r }$ ; a=arr[l+1]; Partitioning element. for (;;) { Beginning of innermost loop. do $\dot { \bf 1 } + +$ ; while (arr[i] < a); Scan up to find element $> \mathtt { a }$ . do j--; while (arr[j] $>$ a); Scan down to find element $< \mathtt { a }$ . if (j < i) break; Pointers crossed. Partitioning complete. SWAP(arr[i],arr[j]); Exchange elements. } End of innermost loop. arr[l+1] $=$ arr[j]; Insert partitioning element. arr[j] $= _ { \mathrm { a } }$ ; jstack $+ = ~ 2$ ; Push pointers to larger subarray on stack; process smaller subarray immediately.

if (jstack $> =$ NSTACK) throw("NSTACK too small in sort."); if $( \mathrm { i } \mathbf { r } \mathbf { - } \mathrm { i } \mathbf { + } 1 > = \mathrm { ~ j \mathbf { - } \mathbf { 1 } ) ~ } .$ { istack[jstack] ${ \stackrel { } { = } } { \dot { \mathtt { 1 } } } \mathtt { r }$ ; istack[jstack-1] ${ \bf \Phi } = \dot { \bf 1 }$ ; ir=j-1; } else { istack[jstack] $= \dot { \jmath } - 1$ ; istack[jstack-1] ${ } = 1$ ; $\beth = \dot { \beth }$ ; } } } }

As usual, you can move any other arrays around at the same time as you sort arr. At the risk of being repetitious:

template<class T, class U>   
void sort2(NRvector<T> &arr, NRvector<U> &brr)   
Sort an array arr[0..n-1] into ascending order using Quicksort, while making the corresponding   
rearrangement of the array brr[0..n-1].   
{ const Int M=7,NSTACK $\mathop {    }$ 64; Int i,ir,j,k,jstack=-1, $\mathtt { 1 } = 0$ , $\mathbf { n } =$ arr.size(); T a; U b; VecInt istack(NSTACK); $\mathrm { i } \mathbf { r } { = } \mathbf { n } { - } 1$ ; for (;;) { Insertion sort when subarray small enough. if (ir-l < M) { for (j=l+1;j<=ir;j++) { $\mathtt { a } =$ arr[j]; $\mathtt { b } =$ brr[j]; for (i=j-1; $\mathrm { i } > = 1$ ;i--) { if (arr[i] $< = { \mathsf { a } } )$ break; arr[i+1] $=$ arr[i]; brr[i+1] $\stackrel { } { = }$ brr[i]; 1 arr[i+1] $= a$ ; brr[i+1]=b; } if (jstack < 0) break; ir=istack[jstack--]; Pop stack and begin a new round of partil=istack[jstack--]; tioning. } else { $\mathrm { k } =$ (l+ir) >> 1; Choose median of left, center, and right el-SWAP(arr[k],arr[l+1]); ements as partitioning element a. Also SWAP(brr[k],brr[l+1]); rearrange so that $\mathsf { a } [ 1 ] \leq \mathsf { a } [ 1 + 1 ] \leq \mathsf { a } [ \mathrm { i r } ]$ if (arr[l] $>$ arr[ir]) { SWAP(arr[l],arr[ir]); SWAP(brr[l],brr[ir]); if (arr[l+1] $>$ arr[ir]) { SWAP(arr[l+1],arr[ir]); SWAP(brr[l+1],brr[ir]); } if (arr[l] $>$ arr[l+1]) { SWAP(arr[l],arr[l+1]); SWAP(brr[l],brr[l+1]); } $\dot { \bar { 1 } } = 1 + 1$ ; Initialize pointers for partitioning. $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } { \boldsymbol { \mathbf { r } } }$ ; a=arr[l+1]; Partitioning element.

b=brr[l+1]; for (;;) { Beginning of innermost loop. do $\dot { \bf 1 } + +$ ; while (arr[i] < a); Scan up to find element $> \mathtt { a }$ . do j--; while (arr[j] $>$ a); Scan down to find element $< \mathtt { a }$ . if (j < i) break; Pointers crossed. Partitioning complete. SWAP(arr[i],arr[j]); Exchange elements of both arrays. SWAP(brr[i],brr[j]); End of innermost loop. arr[l+1] $=$ arr[j]; Insert partitioning element in both arrays. arr[j] $= \mathtt { a }$ ; brr[l+1] $=$ brr[j]; brr[j] $= \mathrm { b }$ ; jstack $+ = ~ 2$ ; Push pointers to larger subarray on stack; process smaller subarray immediately. if (jstack $> =$ NSTACK) throw("NSTACK too small in sort2."); if $( \mathrm { i } \mathbf { r } \mathbf { - } \mathrm { i } \mathbf { + } 1 \ \mathbf { > } \mathbf { = } \ \mathrm { j } \mathbf { - } \mathrm { 1 } )$ { istack[jstack] ${ \tt = } \tt { i r }$ ; istack[jstack-1] ${ \bf \Phi } = \dot { \bf 1 }$ ; $\scriptstyle { \mathrm { i } x = } { \mathrm { j } - 1 }$ ; } else { istack[jstack] $= \dot { ] } - 1$ ; istack[jstack-1] ${ = } 1$ ; $\mathbf { \vec { \tau } } _ { 1 } = \dot { \mathbf { \vec { \tau } } }$ ; } } } }

You could, in principle, rearrange any number of additional arrays along with brr, but this is inefficient if the number of such arrays is larger than one. The preferred technique is to make use of an index table, as described in $\ S 8 . 4$ .

# CITED REFERENCES AND FURTHER READING:

Sedgewick, R. 1978, “Implementing Quicksort Programs,” Communications of the ACM, vol. 21, pp. 847–857.[1]

# 8.3 Heapsort

Heapsort is slower than Quicksort by a constant factor. It is so beautiful that we sometimes use it anyway, just for the sheer joy of it. (However, we don’t recommend that you do this if your employer is paying for efficient code.) Heapsort is a true “in-place” sort, requiring no auxiliary storage. It is an $N \log _ { 2 } N$ algorithm, not only on average, but also for the worst case order of input data. In fact, its worst case is only $20 \%$ or so worse than its average running time.

It is beyond our scope to give a complete exposition on the theory of Heapsort. We mention the general principles, then refer you to the references [1,2]; or you can analyze the program yourself, if you want to understand the details.

A set of $N$ numbers $a _ { j }$ ; $j ~ = ~ 0 , \ldots , N - 1$ , is said to form a “heap” if it satisfies the relation

$$
a _ { ( j - 1 ) / 2 } \geq a _ { j } \quad \mathrm { f o r } \quad 0 \leq ( j - 1 ) / 2 < j < N
$$

![](images/b23bb47fdc7d0e2e655f99fb92916bbb84b3f89fb28b27bffbe3a3deafff18f1.jpg)  
Figure 8.3.1. Ordering implied by a “heap,” here of 12 elements. Elements connected by an upward path are sorted with respect to one another, but there is not necessarily any ordering among elements related only “laterally.”

Here the division in $j / 2$ means “integer divide,” i.e., is an exact integer or else is rounded down to the closest integer. Definition (8.3.1) will make sense if you think of the numbers $a _ { i }$ as being arranged in a binary tree, with the top, “boss,” node being $a _ { 0 }$ ; the two “underling” nodes being $a _ { 1 }$ and $a _ { 2 }$ ; their four underling nodes being $a _ { 3 }$ through $a _ { 6 }$ ; etc. (See Figure 8.3.1.) In this form, a heap has every “supervisor” greater than or equal to its two “supervisees,” down through the levels of the hierarchy.

If you have managed to rearrange your array into an order that forms a heap, then sorting it is very easy: You pull off the “top of the heap,” which will be the largest element yet unsorted. Then you “promote” to the top of the heap its largest underling. Then you promote its largest underling, and so on. The process is like what happens (or is supposed to happen) in a large corporation when the chairman of the board retires. You then repeat the whole process by retiring the new chairman of the board. Evidently the whole thing is an $N \log _ { 2 } N$ process, since each retiring chairman leads to $\log _ { 2 } N$ promotions of underlings.

Well, how do you arrange the array into a heap in the first place? The answer is again a “sift-up” process like corporate promotion. Imagine that the corporation starts out with $N / 2$ employees on the production line, but with no supervisors. Now a supervisor is hired to supervise two workers. If he is less capable than one of his workers, that one is promoted in his place, and he joins the production line. After supervisors are hired, then supervisors of supervisors are hired, and so on up the corporate ladder. Each employee is brought in at the top of the tree, but then immediately sifted down, with more capable workers promoted until their proper corporate level has been reached.

In the Heapsort implementation, the same sift-up code can be used for the initial creation of the heap and for the subsequent retirement-and-promotion phase. One execution of the Heapsort function represents the entire life-cycle of a giant corporation: $N / 2$ workers are hired; $N / 2$ potential supervisors are hired; there is a sifting up in the ranks, a sort of super Peter Principle: In due course, each of the original employees gets promoted to chairman of the board.

namespace hpsort_util { template<class T> void sift_down(NRvector<T> &ra, const Int l, const Int r) Carry out the sift-down on element ra(l) to maintain the heap structure. l and r determine the “left” and “right” range of the sift-down. { Int j,jold; T a; a=ra[l]; jold=l; $\scriptstyle { \mathrm { j } = 2 * 1 + 1 }$ ; while (j $< = \texttt { r }$ ) { if (j $< \textbf { r }$ && ra[j] $<$ ra[j+1]) $\mathrm { j } + +$ ; Compare to the better underling. if (a $> =$ ra[j]) break; Found a’s level. Terminate the siftra[jold] $=$ ra[j]; down. Otherwise, demote a and jold=j; continue. j=2\*j+1; } ra[jold] $= a$ ; Put a into its slot. }   
}

# template<class T>

void hpsort(NRvector<T> &ra)

Sort an array $\mathtt { r a } [ 0 \ldots \mathtt { n - 1 } ]$ into ascending numerical order using the Heapsort algorithm. ra is replaced on output by its sorted rearrangement.

Int i,n=ra.size();   
for (i=n/2-1; $\scriptstyle \dot { 1 } > = 0$ ; i--) The index i, which here determines the “left” range of the sift-down, i.e., the element to be sifted down, is decremented from $\tt { n } / 2 \mathrm { - } 1$ down to 0 during the “hiring” (heap creation) phase. hpsort_util::sift_down(ra,i,n-1);   
for $\scriptstyle \dot { 1 } = \mathtt { n } - 1$ ; i>0; i--) { Here the “right” range of the sift-down is decremented from $\mathtt { n } \mathtt { - } 2$ down to 0 during the “retirement-and-promotion” (heap selection) phase. SWAP(ra[0],ra[i]); Clear a space at the end of the array, and retire hpsort_util::sift_down(ra,0,i-1); the top of the heap into it.   
}

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 5$ .2.3.[1] Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 11.[2]

# 8.4 Indexing and Ranking

The concept of keys plays a prominent role in the management of data files. A data record in such a file may contain several items, or fields. For example, a record in a file of weather observations may have fields recording time, temperature, and wind velocity. When we sort the records, we must decide which of these fields we want to be brought into sorted order. The other fields in a record just come along for the ride and will not, in general, end up in any particular order. The field on which the sort is performed is called the key field.

For a data file with many records and many fields, the actual movement of $N$ records into the sorted order of their keys $K _ { i }$ ; $i = 0 , \ldots , N - 1$ , can be a daunting task. Instead, one can construct an index table $I _ { j }$ ; $j = 0 , \ldots , N - 1$ , such that the smallest $K _ { i }$ has $i = I _ { 0 }$ , the second smallest has $i = I _ { 1 }$ , and so on up to the largest $K _ { i }$ with $i = I _ { N - 1 }$ . In other words, the array

$$
K _ { I _ { j } } \mathrm { ~  ~ \omega ~ } _ { j } = 0 , 1 , \ldots , N - 1
$$

is in sorted order when indexed by $j$ . When an index table is available, one need not move records from their original order. Further, different index tables can be made from the same set of records, indexing them to different keys.

The algorithm for constructing an index table is straightforward: Initialize the index array with the integers from 0 to $N - 1$ ; then perform the Quicksort algorithm, moving the elements around as $i f$ one were sorting the keys. The integer that initially numbered the smallest key thus ends up in the number one position, and so on.

The concept of an index table maps particularly nicely into an object, say Indexx. The constructor takes a vector arr as its argument; it stores an index table to arr, leaving arr unmodified. Subsequently, the method sort can be invoked to rearrange arr, or any other vector, into the sorted order of arr. Indexx is not a templated class, since the stored index table does not depend on the type of vector that is indexed. However, it does need a templated constructor.

struct Indexx {Int n;VecInt indx;

template<class T> Indexx(const NRvector<T> &arr) { Constructor. Calls index and stores an index to the array arr[0..n-1]. index(&arr[0],arr.size()); Indexx() {} Empty constructor. See text.

template<class $\mathrm { T } >$ void sort(NRvector<T> &brr) {   
Sort an array brr[0..n-1] into the order defined by the stored index. brr is replaced on   
output by its sorted rearrangement. if (brr.size() $! = { \textbf { n } } )$ throw("bad size in Index sort"); NRvector<T> tmp(brr); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<n;j $^ { + + }$ ) brr[j] $=$ tmp[indx[j]];   
}

template<class $\mathrm { T } >$ inline const T & el(NRvector<T> &brr, Int j) const { This function, and the next, return the element of brr that would be in sorted position j according to the stored index. The vector brr is not changed.

return brr[indx[j]]; } template<class $\mathrm { T } >$ inline T & el(NRvector<T> &brr, Int j) { Same, but return an l-value. return brr[indx[j]]; }

template<class $\mathrm { \Delta T > }$ void index(const T \*arr, Int nn);   
This does the actual work of indexing. Normally not called directly by the user, but see text for exceptions.

# void rank(VecInt_O &irank) {

Returns a rank table, whose jth element is the rank of arr[j], where arr is the vector originally indexed. The smallest arr[j] has rank 0.

irank.resize(n);

for (Int j=0;j<n;j++) irank[indx[j]] = j; } };

template<class T>   
void Indexx::index(const T \*arr, Int nn)   
Indexes an array arr[0..nn-1], i.e., resizes and sets indx[0..nn-1] such that arr[indx[j]] is in ascending order for ${ \mathfrak { j } } = 0 , 1 , \dotsc , { \mathrm { n n } } - 1$ . Also sets member value n. The input array arr is not changed. nst Int M=7,NSTACK $_ { = 6 4 }$ ; t i,indxt,ir,j,k,jstack $: =$ -1, $_ { 1 = 0 }$ ; a; cInt istack(NSTACK);   
$\texttt { n } = \texttt { n n }$ ; dx.resize(n);   
$\mathtt { i r } \mathtt { = n - 1 }$ ; (j=0;j<n;j++) indx[j]=j; (;;) { if (ir-l < M) { for (j=l+1;j<=ir;j++) { indxt=indx[j]; a=arr[indxt]; for (i=j-1; $\mathrm { i } > = 1$ ;i--) { if (arr[indx[i]] $< = a ,$ ) break; indx[i+1] $=$ indx[i]; } indx[i+1] $=$ indxt; if (jstack < 0) break; ir=istack[jstack--]; $\ b { 1 } =$ istack[jstack--]; } else { $\mathtt { k } =$ (l+ir) >> 1; SWAP(indx[k],indx $\left[ 1 + 1 \right]$ ); if (arr[indx[l]] $>$ arr[indx[ir]]) { SWAP(indx[l],indx[ir]); if (arr[indx[l+1]] $>$ arr[indx[ir]]) { SWAP(indx[l+1],indx[ir]); if (arr[indx[l]] $>$ arr[indx[l+1]]) { SWAP(indx[l],indx[l+1]); $\dot { \bf z } = \bf { 1 } + 1$ ; $\scriptstyle { \dot { \mathsf { J } } } = { \dot { \mathsf { 1 } } } { \boldsymbol { \mathbf { r } } }$ ; indxt $=$ indx[l+1]; a=arr[indxt]; for (;;) { do $\dot { \bf 1 } + +$ ; while (arr[indx[i]] < a); do j--; while (arr[indx[j]] > a); if (j < i) break; SWAP(indx[i],indx[j]); indx[l+1] $=$ indx[j]; indx[j] $=$ indxt; jstack $+ = ~ 2$ ; if (jstack $> =$ NSTACK) throw("NSTACK too if (ir-i+1 $> =$ j-l) { istack[jstack] ${ \tt = i r }$ ; istack[jstack-1] ${ \bf \Phi } = \dot { \bf 1 }$ ; ir=j-1; } else {

istack[jstack] $= \mathrm { j } - 1$ ; istack[jstack-1] ${ = } 1$ ; $\beth = \dot { \beth }$ ; } } } }

A typical use of Indexx might be to rearrange three vectors (not necessarily of the same type) into the sorted order defined by one of them:

Indexx arrindex(arr);   
arrindex.sort(arr);   
arrindex.sort(brr);   
arrindex.sort(crr);

The generalization to any other number of arrays is obvious.

The Indexx object also provides a method el (for “element”) to access any vector in arr-sorted order without actually modifying that vector (or, for that matter, arr). In other words, after we index arr, say by

# Indexx arrindex(arr);

we can address an element in brr that corresponds to the jth element of a virtually sorted arr as simply arrindex.el(brr,j). Neither arr nor brr are altered from their original state. el is provided in two versions, so that it can be both an l-value (on the left-hand side of an assignment) and an r-value (in an expression).

As an aside, the reason that the internal workhorse index uses a pointer, not a vector, for its argument is so that it can be used (purists would say misused) in other situations, such as indexing one row in a matrix. That is also the reason for providing an additional, empty, constructor. If you want to index nn consecutive elements sitting around somewhere, pointed to by ptr, you write

Indexx myhack;   
myhack.index(ptr,nn);

A rank table is different from an index table. A rank table’s $j$ th entry gives the rank of the $j$ th element of the original array of keys, ranging from 0 (if that element was the smallest) to $N - 1$ (if that element was the largest). One can easily construct a rank table from an index table. Indeed, you might already have noticed the method rank in Indexx that returns just such a table, stored as a vector.

Figure 8.4.1 summarizes the concepts discussed in this section.

# 8.5 Selecting the Mth Largest

Selection is sorting’s austere sister. (Say that five times quickly!) Where sorting demands the rearrangement of an entire data array, selection politely asks for a single returned value: What is the $k$ th smallest (or, equivalently, the $m = N - 1 - k$ th largest) element out of $N$ elements? (In this convention, used throughout this section, $k$ takes on values $k = 0 , 1 , \ldots , N - 1$ , so $k = 0$ is the smallest array element and $k = N - 1$ the largest.) The fastest methods for selection do, unfortunately, rearrange the array for their own computational purposes, typically putting all smaller elements to the left of the $k$ th, all larger elements to the right, and scrambling the order within each subset. This side effect is at best innocuous, at worst downright inconvenient. When an array is very long, so that making a scratch copy of it is taxing on memory, one turns to in-place algorithms without side effects, which are slower but leave the original array undisturbed.

![](images/aec119fcc36e6f2c6702e7fc5f65ef67388c759749c8b401ebec4711abea28cf.jpg)  
Figure 8.4.1. (a) An unsorted array of six numbers. (b) Index table whose entries are pointers to the elements of (a) in ascending order. (c) Rank table whose entries are the ranks of the corresponding elements of (a). (d) Sorted array of the elements in (a).

The most common use of selection is in the statistical characterization of a set of data. One often wants to know the median element in an array (quantile $p = 1 / 2 ,$ ) or the top and bottom quartile elements (quantile $p = 1 / 4 , 3 / 4 )$ . When $N$ is odd, the exact definition of the median is that it is the $k$ th element, with $k = ( N - 1 ) / 2$ . When $N$ is even, statistics books define the median as the arithmetic mean of the elements $k = N / 2 - 1$ and $k = N / 2$ (that is, $N / 2$ from the bottom and $N / 2$ from the top). If you embrace such formality, you must perform two separate selections to find these elements. (If you do the first selection by a partition method, see below, you can do the second by a single pass through $N / 2$ elements in the right partition, looking for the smallest element.) For $N > 1 0 0$ we usually use $k = N / 2$ as the median element, formalists be damned.

A variant on selection for large data sets is single-pass selection, where we have a stream of input values, each of which we get to see only once. We want to be able to report at any time, say after $N$ values, the $k$ th smallest (or largest) value seen so far, or, equivalently, the quantile value for some $p$ . We will describe two approaches: If we care only about the smallest (or largest) $M$ values, for fixed $M$ , so that $0 \leq k < M$ , then there are good algorithms that require only $M$ storage. On the other hand, if we can tolerate an approximate answer, then there are efficient algorithms that can report at any time a good estimate of the $p$ -quantile value for any $p$ , $0 < p < 1$ . That is to say, we will get not the exact $k$ th smallest element, $k = p N$ , of the $N$ that have gone by, but something very close to it — and without requiring $N$ storage or having to know $p$ in advance.

The fastest general method for selection, allowing rearrangement, is partitioning, exactly as was done in the Quicksort algorithm (-8.2). Selecting a “random” partition element, one marches through the array, forcing smaller elements to the left, larger elements to the right. As in Quicksort, it is important to optimize the inner loop, using “sentinels” $( \ S 8 . 2 )$ to minimize the number of comparisons. For sorting, one would then proceed to further partition both subsets. For selection, we can ignore one subset and attend only to the one that contains our desired $k$ th element. Selection by partitioning thus does not need a stack of pending operations, and its operations count scales as $N$ rather than as $N \log N$ (see [1]). Comparison with sort in $\ S 8 . 2$ should make the following routine obvious.

# template<class T>

# T select(const Int k, NRvector<T> &arr)

Given k in $\left[ 0 \ldots \mathbf { n } \mathbf { - } 1 \right]$ returns an array value from arr[0..n-1] such that k array values are less than or equal to the one returned. The input array will be rearranged to have this value in location arr[k], with all smaller elements moved to arr[0..k-1] (in arbitrary order) and all larger elements in arr $[ \mathbf { k } { + } 1 \mathbf { \cdot } \mathbf { \cdot } \mathbf { n } { - } 1 ]$ (also in arbitrary order).

Int i,ir,j,l,mid, $\mathbf { n } =$ arr.size();   
T a;   
$\mathtt { 1 } = 0$ ;   
$\mathrm { i } \mathbf { r } { = } \mathbf { n } { - } 1$ ;   
for (;;) { if (ir $< = ~ 1 + 1$ ) { Active partition contains 1 or 2 elements. if ( $\scriptstyle \mathbf { i r } \ = = \ 1 + 1$ && arr[ir] $<$ arr[l]) Case of 2 elements. SWAP(arr[l],arr[ir]); return arr[k]; } else { mid=(l+ir) >> 1; Choose median of left, center, and right el-SWAP(arr[mid],arr[l+1]); ements as partitioning element a. Also if (arr[l] $>$ arr[ir]) rearrange so that a $\mathbf { \hat { \mu } } _ { \mathbf { \mu } } \mathbf { \Sigma } [ 1 ] \mathbf { \beta } \leq \mathbf { a r r } \left[ \mathbf { \hat { \mu } } _ { 1 + 1 } \right]$ , SWAP(arr[l],arr[ir]); $\mathbf { a r r } \left[ \mathbf { i r } \right] \geq \mathbf { a r r } \left[ \mathbf { \bar { 1 } + } \mathbf { 1 } \right]$ . if (arr[l+1] $>$ arr[ir]) SWAP(arr[l+1],arr[ir]); if (arr[l] $>$ arr[l+1]) SWAP(arr[l],arr[l+1]); $\dot { \bf z } = \bf { 1 } + \bf { 1 }$ ; Initialize pointers for partitioning. j=ir; a=arr[l+1]; Partitioning element. for (;;) { Beginning of innermost loop. do i++; while (arr[i] < a); Scan up to find element $> a$ . do j--; while (arr[j] $>$ a); Scan down to find element $< \mathtt { a }$ . if (j < i) break; Pointers crossed. Partitioning complete. SWAP(arr[i],arr[j]); End of innermost loop. arr[l+1] $=$ arr[j]; Insert partitioning element. arr[j] $= a$ ; if (j $> = { \bf \nabla } \mathbf { k } .$ ) ir=j-1; Keep active the partition that contains the if (j <= k) $\mathbf { \vec { \tau } } _ { 1 } = \mathbf { \vec { \tau } } _ { 1 }$ ; kth element. }   
}

If you don’t want your array arr to be rearranged, then you will want to make a scratch copy before calling select, e.g.,

# VecDoub brr(arr);

The reason for not doing this internally in select is because you may wish to call select with a variety of different values k, and it would be wasteful to copy the vector anew each time; instead, just let brr keep getting rearranged.

# 8.5.1 Tracking the M Largest in a Single Pass

Of course select should not be used for the trivial cases of finding the largest, or smallest, element in an array. Those cases, you code by hand as simple for loops.

There are also efficient ways to code the case where $k$ is bounded by some fixed $M$ , modest in comparison to $N$ , so that memory of order $M$ is not burdensome. Indeed, $N$ may not even be known: You may have a stream of incoming data values and be called upon at any time to provide a list of the $M$ largest values seen so far.

A good approach to this case is to use the method of Heapsort (-8.3), maintaining a heap of the $M$ largest values. The advantage of the heap structure, as opposed to a linear array of length $M$ , is that at most $\log M$ , rather than $M$ , operations are required every time a new data value is processed.

The object Heapselect has a constructor, by which you specify $M$ , an “add” method that assimilates a new data value, and a “report” method for getting the $k$ th largest seen so far. Note that the initial cost of a report is $O ( M \log M )$ , because we need to sort the heap; but you can then get all values of $k$ at no extra cost, until you do the next add. A special case is that getting the $M - 1 \mathrm { s } 1$ t largest is always cheap, since it is at the top of the heap; so if you have a single favorite value of $k$ , it is best to choose $M$ with $M - 1 = k$ .

# struct Heapselect {

Object for tracking the m largest values seen thus far in a stream of values.

Int m,n,srtd;   
VecDoub heap;

Heapselect(Int mm) : $\mathbf { m } \left( \mathbf { m } \mathbf { m } \right)$ , ${ \bf n } ( 0 )$ , srtd(0), heap(mm,1.e99) {} Constructor. The argument is the number of largest values to track.

# void add(Doub val) {

Assimilate a new value from the stream. Int j,k; if (n<m) { Heap not yet filled. hea $\ u [ \mathrm { n + + } ] = \mathrm { v a l } ;$ ; if ( $\mathrm { \Omega } _ { \mathrm { { n } } } = = \mathrm { { m } }$ ) sort(heap); Create initial heap by overkill! } else { if (val $>$ heap[0]) { Put it on the heap? heap[0] $=$ val; for $( \mathrm { j } = 0$ ;;) { Sift down. $\mathbf { k } { = } ( \mathrm { ~ j ~ } \ < < \ 1 ) \ + \ 1 \ \mathbf { ; }$ ; if (k $> \ m - 1$ ) break; if (k $\downarrow =$ (m-1) && heap[k] $>$ heap[k+1]) $\mathrm { k } { + + }$ ; if (heap[j] $< =$ heap[k]) break; SWAP(heap[k],heap[j]); $\scriptstyle { \dot { \mathbf { J } } } = \mathbf { k }$ ; } } n++; } srtd $\mathit { \Theta } = \mathit { \Theta } 0$ ; Mark heap as “unsorted”.   
}

# Doub report(Int k) {

Return the kth largest value seen so far. $\mathtt { k } = 0$ returns the largest value seen, $\tt k = 1$ the second largest, : : : , $\mathtt { k } = \mathtt { m } - 1$ the last position tracked. Also, k must be less than the number of previous values assimilated.

Int mm $=$ MIN $( \mathtt { n } , \mathtt { m } )$ ; if $\mathrm { ( k ) ~ } \mathrm { m m } { - } 1 .$ ) throw("Heapselect k too big"); if $( \textbf k = = \textbf { m } { - } 1$ ) return heap[0]; Always free, since top of heap. if (! srtd) { sort(heap); srtd $= ~ 1$ ; } Otherwise, need to sort the heap. return heap[mm-1-k]; }

};

# 8.5.2 Single-Pass Estimation of Arbitrary Quantiles

The data values fly by in a stream. You get to look at each value only once, and do a constant-time process on it (meaning that you can’t take longer and longer to process later and later data values). Also, you have only a fixed amount of storage memory. From time to time you want to know the median value (or 95th percentile value, or arbitrary $p$ -quantile value) of the data that you have seen thus far. How do you do this?

Evidently, with the conditions stated, you’ll have to tolerate an approximate answer, since an exact answer must require unbounded storage and (perhaps) unlimited processing. If you think that “binning” is somehow the answer, you are right. But it is not immediately obvious how to choose the bins, since you have to see a potentially unlimited amount of data before you can tell for sure how its values are distributed.

Chambers et al. [2] have given a robust, and extremely fast, algorithm, which they call $I Q$ agent, that adaptively adjusts a set of bins so that they converge to the data values of specified quantile $p$ -values. The general idea (see Figure 8.5.1) is to accumulate incoming data into batches, then to update a stored, piecewise linear, cumulative distribution function (cdf) by adding a batch’s cdf and then interpolating back to a fixed set of $p$ -values. Arbitrary requested quantile values (“incremental quantiles,” or “IQs,” hence the algorithm’s name) can be obtained at any time by linear interpolation on the stored cdf. Batching allows the program to be very efficient, with an (amortized) cost of only a small number of operations per new data value. The batching is done transparently to the user.

Similar to Heapselect, the IQagent object has add and report methods, the latter now taking a value for $p$ as its argument. In the implementation below, we use a batch size of nbuf $= 1 0 0 0$ but do an early update step with a partial batch whenever a quantile is requested. With these parameters, you should therefore request quantile information no more frequently than after every few nbuf data values, at which point you can request as many different values of $p$ as you want before continuing. The alternative is to remove the call to update from report, in which case you’ll get fast, but constant, answers, changing only after each regular batch update.

IQagent uses internally a general purpose set of 251 $p$ -values that includes integer percentile points from 10 to 90, and a logarithmically spaced set of smaller and larger values spanning $1 0 ^ { - 6 }$ to $1 - 1 0 ^ { - 6 }$ . Other $p$ -values that you request are obtained by interpolation. Of course you cannot get meaningful tail quantiles for small values of $p$ until at least several times $1 / p$ data values have been processed. Before that, the program will simply report the smallest value previously seen (or largest value previously seen, for $p  1 _ { . }$ ).

![](images/7e1329296dc24236966377ad5a339246db31242b3bad3664693dae97ceb77bd5.jpg)  
Figure 8.5.1. Algorithm for updating a piecewise linear cumulative distribution function (cdf). (a) The cdf is represented by quantile values at a fixed set of $p$ -values (here, just 3). (b) A batch of new data values (here, just 4) define a stepwise constant cdf. (c) The two cdfs are summed. New data steps are small in proportion to the new batch size versus number of data values previously processed. (d) The new cdf representation is obtained by interpolating the fixed $p$ -values to (c).

struct IQagent {   
Object for estimating arbitrary quantile values from a continuing stream of data values. static const Int nbuf $\ l = \ 1 0 0 0$ ; Batch size. You may $\times 1 0$ if you expect $>$ Int nq, nt, nd; $1 0 ^ { 6 }$ data values. VecDoub pval,dbuf,qile; Doub q0, qm;   
IQagent() : nq(251), nt(0), nd(0), pval(nq), dbuf(nbuf),   
qile(nq,0.), q0(1.e99), qm(-1.e99) {   
Constructor. No arguments. for (Int $\scriptstyle { \dot { \mathcal { I } } } = 8 5$ ; $\scriptstyle \mathtt { j } < = 1 6 5$ ; $\mathrm { j } + +$ ) pval[j] $=$ (j-75.)/100.; Set general purpose array of $p$ -values ranging from $1 0 ^ { - 6 }$ to $1 - 1 0 ^ { - 6 }$ . You can change this if you want: for (Int $\scriptstyle { \dot { \mathsf { J } } } = 8 4$ ; $\scriptstyle { \dot { \bar { \jmath } } } > = 0$ ;j--) { pval[j] $=$ 0.87191909\*pval[j+1]; pval[250-j] $=$ 1.-pval[j]; }   
}   
void add(Doub datum) {   
Assimilate a new value from the stream. dbuf[nd++] $=$ datum; if (datum $<$ q0) {q0 $=$ datum;} if (datum $>$ qm) {qm $=$ datum;}

if (nd $= =$ nbuf) update();}

Time for a batch update.

# void update() {

Batch update, as shown in Figure 8.5.1. This function is called by add or report and should not be called directly by the user.

Int $\mathrm { j } \mathrm { d } = \mathrm { 0 }$ ,jq=1,iq;   
Doub target, told ${ = } 0$ ., tnew ${ \tt = } 0$ ., qold, qnew;   
VecDoub newqile(nq); Will be new quantiles after update.   
sort(dbuf,nd);   
qold $=$ qnew $=$ qile[0] $= { \textbf { n 6 } }$ wqile[0] $=$ q0; Set lowest and highest to min   
qile[nq-1] $=$ newqile[nq-1] $=$ qm; and max values seen so far,   
pval[0] $=$ min(0.5/(nt+nd),0.5\*pval[1]); and set compatible $p$ -values.   
pval[nq-1] $=$ max(1.-0.5/(nt+nd),0.5\*(1.+pval[nq-2]));   
for (iq=1;iq<nq-1; ${ \mathrm { i } } { \mathrm { q } } + + { \mathrm { \ i } }$ ) { Main loop over target $p$ -values for intertarget $=$ (nt+nd)\*pval[iq]; polation. if (tnew $<$ target) for (;;) Here’s the guts: We locate a succession of abscissa-ordinate pairs (qnew,tnew) that are the discontinuities of value or slope in Figure 8.5.1(c), breaking to perform an interpolation as we cross each target. if (jq $<$ nq && (jd $> =$ nd || qile[jq] $<$ dbuf[jd])) { Found slope discontinuity from old CDF. qnew $=$ qile[jq]; tnew $=$ jd $^ +$ nt\*pval[jq++]; if (tnew $> =$ target) break; } else { Found value discontinuity from batch data qnew $=$ dbuf[jd]; CDF. tnew $=$ told; if (qile[jq]>qile[jq-1]) tnew $+ =$ nt\*(pval[jq]-pval[jq-1]) \*(qnew-qold)/(qile[jq]-qile[jq-1]); jd++; if (tnew $> =$ target) break; told $=$ tnew++; qold $=$ qnew; if (tnew $> =$ target) break; } told $=$ tnew; qold $=$ qnew; } Break to here and perform the new interpolation. if (tnew $= =$ told) newqile[iq] $=$ 0. $^ { 5 \ast }$ (qold+qnew); else newqile[iq] $=$ qold $^ +$ (qnew-qold)\*(target-told)/(tnew-told); told $=$ tnew; qold $=$ qnew;   
}   
qile $=$ newqile;   
nt $+ =$ nd;   
nd $\qquad = \ 0$ ;

# Doub report(Doub p) {

Return estimated p-quantile for the data seen so far. (E.g., $\mathbf { p } = \mathbf { 0 . 5 }$ for median.) Doub q; if (nd > 0) update(); You may want to remove this line. See text. Int $\scriptstyle \mathrm { j } 1 = 0$ ,jh ${ \bf \Phi } _ { \cdot } = { \bf \Phi } _ { \cdot }$ nq-1,j; while (jh-jl>1) { Locate place in table by bisection. j = (jh+jl)>>1; if (p > pval[j]) jl=j; else jh=j; } ${ \mathrm { ~ j ~ } } =$ jl; Interpolate. q $=$ qile[j] $^ +$ (qile[j+1]-qile[j])\*(p-pval[j])/(pval[j+1]-pval[j]); return MAX(qile[0],MIN(qile[nq-1],q));   
}

How accurate is the IQ agent algorithm, as compared, say, to storing all $N$ data values in an array $A$ and then reporting the “exact” quantile $A _ { \lfloor p N \rfloor }$ ? There are several sources of error, all of which you can control by modifying parameters in IQagent. (We think that the default parameters will work just fine for almost all users.) First, there is interpolation error: The desired cdf is represented by a piecewise linear function between $\mathtt { n q } = 2 5 1$ stored values. For typical distributions, this limits the accuracy to three or four significant figures. We find it hard to believe that anyone needs to know a median, e.g., more accurately than this, but if you do, then you can increase the density of $p$ -values in the regions of interest.

Second, there are statistical errors. One way to characterize these is to ask what value $j$ has $A _ { j }$ closest to the quantile reported by IQ agent, and then how small is $\vert j - p N \vert$ as a fraction of $[ N p ( \hat { 1 } - p ) ] ^ { 1 / 2 }$ , the accuracy inherent in your finite sample size $N$ . If this fraction is $\lesssim 1$ , then the estimate is “good enough,” meaning that no method can do substantially better at estimating the population quantiles given your sample.

With the default parameters, and for reasonably behaved distributions, IQagent passes this test for $N \lesssim 1 0 ^ { 6 }$ . For larger $N$ , the statistical error becomes significant (though still generally smaller than the interpolation error, above). You can, however, decrease it by increasing the batch size, nbuf. Larger is always better, if you have the memory and can tolerate the logarithmic increase in the cost per point of the sort.

Although the accuracy of IQagent is not guaranteed by a provable bound, the algorithm is fast, robust, and highly recommended. For other approaches to incremental quantile estimation, including some that do give provable bounds (but have other issues), see [3,4] and references cited therein.

# 8.5.3 Other Uses for Incremental Quantile Estimation

Incremental quantile estimation provides a useful way to histogram data into variable-size bins that each contain the same number of points, without knowing in advance the bin boundaries: First, throw $N$ data values at an IQagent object. Next, choose a number of bins $m$ , and define

$$
p _ { i } \equiv \frac { i } { m } , \qquad i = 0 , \ldots , m
$$

Finally, if $q _ { i }$ is the quantile value at $p _ { i }$ , plot the $i$ th bin from $q _ { i }$ to $q _ { i + 1 }$ with a height

$$
h _ { i } = N \frac { p _ { i + 1 } - p _ { i } } { q _ { i + 1 } - q _ { i } } , \qquad i = 0 , \ldots , m - 1
$$

A different application concerns the monitoring of quantile values for changes. For example, you might be producing widgets with a parameter $T$ whose tolerance is $T \pm \delta T$ , and you want an early warning if the observed values of $T$ at the 5th and 95th percentiles start to drift.

The IQagent object is easily modified for such applications. Simply change the line nt $+ =$ nd to nt $=$ my_constant, where my_constant is the number of past widgets that you want to average over. (More precisely, the number corresponding to one e-fold of weight decrease in an exponentially decreasing average over all past production.) Now, the stored cdf combines with a new batch of data with a constant, not an increasing, weight, and you can look for changes over time in any desired quantiles.

# 8.5.4 In-Place Selection

In-place, nondestructive, selection is conceptually simple, but it requires a lot of bookkeeping, and it is correspondingly slow. The general idea is to pick some number $M$ of elements at random, to sort them, and then to make a pass through the array counting how many elements fall in each of the $M + 1$ intervals defined by these elements. The $k$ th largest will fall in one such interval — call it the “live” interval. One then does a second round, first picking $M$ random elements in the live interval, and then determining which of the new, finer, $M + 1$ intervals all presently live elements fall into. And so on, until the $k$ th element is finally localized within a single array of size $M$ , at which point direct selection is possible.

How shall we pick $M ?$ The number of rounds, $\log _ { M } N = \log _ { 2 } N / \log _ { 2 } M$ , will be smaller if $M$ is larger; but the work to locate each element among $M + 1$ subintervals will be larger, scaling as $\log _ { 2 } M$ for bisection, say. Each round requires looking at all $N$ elements, if only to find those that are still alive, while the bisections are dominated by the $N$ that occur in the first round. Minimizing $O ( N \log _ { M } N ) +$ $O ( N \log _ { 2 } M )$ thus yields the result

$$
M \sim 2 \sqrt { \log _ { 2 } N }
$$

The square root of the logarithm is so slowly varying that secondary considerations of machine timing become important. We use $M = 6 4$ as a convenient constant value.

Further discussion, and code, is in a Webnote [5].

# CITED REFERENCES AND FURTHER READING:

Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), pp. 126ff.[1]   
Knuth, D.E. 1997, Sorting and Searching, 3rd ed., vol. 3 of The Art of Computer Programming (Reading, MA: Addison-Wesley).   
Chambers, J.M., James, D.A., Lambert, D., and Vander Wiel, S. 2006, “Monitoring Networked Applications with Incremental Quantiles,” Statistical Science, vol. 21.[2]   
Tieney, L. 1983, “A Space-efficient Recursive Procedure for Estimating a Quantile of an Unknown Distribution,” SIAM Journal on Scientific and Statistical Computing, vol. 4, pp. 706- 711.[3]   
Liechty, J.C., Lin, D.K.J, and McDermott, J.P. 2003, “Single-Pass Low-Storage Arbitrary Quantile Estimation for Massive Datasets,” Statistics and Computing, vol. 13, pp. 91–100.[4]   
Numerical Recipes Software 2007, “Code Listing for Selip,” Numerical Recipes Webnote No. 1 1, at http://www.nr.com/webnotes?11 [5]

# 8.6 Determination of Equivalence Classes

A number of techniques for sorting and searching relate to data structures whose details are beyond the scope of this book, for example, trees, linked lists, etc. These structures and their manipulations are the bread and butter of computer science, as distinct from numerical analysis, and there is no shortage of books on the subject.

In working with experimental data, we have found that one particular such manipulation, namely the determination of equivalence classes, arises sufficiently often to justify inclusion here.

The problem is this: There are $N$ “elements” (or “data points” or whatever), numbered $0 , \ldots , N - 1$ . You are given pairwise information about whether the elements are in the same equivalence class of “sameness,” by whatever criterion happens to be of interest. For example, you may have a list of facts like: “Element 3 and element 7 are in the same class; element 19 and element 4 are in the same class; element 7 and element 12 are in the same class, : : : ” Alternatively, you may have a procedure, given the numbers of two elements $j$ and $k$ , for deciding whether they are in the same class or different classes. (Recall that an equivalence relation can be anything satisfying the RST properties: reflexive, symmetric, transitive. This is compatible with any intuitive definition of “sameness.”)

The desired output is an assignment to each of the $N$ elements of an equivalence class number, such that two elements are in the same class if and only if they are assigned the same class number.

Efficient algorithms work like this: Let $F ( j )$ be the class or “family” number of element $j$ . Start off with each element in its own family, so that $F ( j ) = j$ . The array $F ( j )$ can be interpreted as a tree structure, where $F ( j )$ denotes the parent of $j$ . If we arrange for each family to be its own tree, disjoint from all the other “family trees,” then we can label each family (equivalence class) by its most senior great-great-: : :grandparent. The detailed topology of the tree doesn’t matter at all, as long as we graft each related element onto it somewhere.

Therefore, we process each elemental datum “ $j$ is equivalent to $k ^ { \prime \prime }$ by (i) tracking $j$ up to its highest ancestor; (ii) tracking $k$ up to its highest ancestor; and (iii) giving $j$ to $k$ as a new parent, or vice versa (it makes no difference). After processing all the relations, we go through all the elements $j$ and reset their $F ( j )$ ’s to their highest possible ancestors, which then label the equivalence classes.

The following routine, based on Knuth [1], assumes that there are m elemental pieces of information, stored in two arrays of length m, lista,listb, the interpretation being that lista[j] and listb[j], $\mathrm { j } { = } 0 \ldots { } . \mathrm { m } { - } 1$ , are the numbers of two elements that (we are thus told) are related.

# void eclass(VecInt_O &nf, VecInt_I &lista, VecInt_I &listb)

Given m equivalences between pairs of n individual elements in the form of the input arrays lista[0..m-1] and listb[0..m-1], this routine returns in $\mathtt { n f } \left[ 0 \dots \dots 1 \right]$ the number of the equivalence class of each of the n elements, integers between 0 and $\mathtt { n - 1 }$ (not all such integers used).

Int l,k,j, $\mathbf { n } =$ nf.size(), $\mathfrak { m } =$ lista.size();   
for $\scriptstyle ( \mathtt { k } = 0$ ;k<n;k++) nf[k] ${ \mathrm { = k } }$ ; Initialize each element its own class.   
for $\scriptstyle 1 = 0$ ;l<m; $^ { 1 + + }$ ) { For each piece of input information... j=lista[l]; while (nf[j] $! =$ j) j=nf[j]; Track first element up to its ancestor. k=listb[l]; while (nf[k] $! =$ k) k=nf[k]; Track second element up to its ancestor. if (j $\mathbf { \updownarrow } = \mathbf { \ k } )$ ) nf[j] $\mathbf { \sigma } = \mathbf { k }$ ; If they are not already related, make them   
} so.   
for $\scriptstyle \dot { \ j } = 0$ ;j<n;j++) Final sweep up to highest ancestors. while (nf[j] $! =$ nf[nf[j]]) nf[j] $=$ nf[nf[j]];

# }

Alternatively, we may be able to construct a boolean function equiv(j,k) that returns a value true if elements $\dot { \mathsf { J } }$ and k are related, or false if they are not. Then we want to loop over all pairs of elements to get the complete picture. D. Eardley has devised a clever way of doing this while simultaneously sweeping the tree up to high ancestors in a manner that keeps it current and obviates most of the final sweep phase:

void eclazz(VecInt_O &nf, Bool equiv(const Int, const Int))

Given a user-supplied boolean function equiv that tells whether a pair of elements, each in the range 0...n-1, are related, return in nf[0..n-1] equivalence class numbers for each element. {

Int kk,jj, $\mathbf { n } =$ nf.size();nf[0] ${ = } 0$ ;for (jj=1;jj<n;jj $^ { + + }$ ) {

Loop over first element of all pairs.

nf[jj]=jj; for (kk=0;kk<jj;kk $^ { + + }$ ) { Loop over second element of all pairs. nf[kk]=nf[nf[kk]]; Sweep it up this much. if (equiv(jj+1,kk+1)) nf[nf[nf[kk]]]=jj; Good exercise for the reader to figure out why this much ancestry is necessary! } for (jj ${ = } 0$ ;jj<n;jj $^ { + + }$ ) nf[jj] $=$ nf[nf[jj]]; Only this much sweeping is needed finally.

# CITED REFERENCES AND FURTHER READING:

Knuth, D.E. 1997, Fundamental Algorithms, 3rd ed., vol. 1 of The Art of Computer Programming (Reading, MA: Addison-Wesley), $\ S 2 . 3 . 3$ .[1] Sedgewick, R. 1998, Algorithms in C, 3rd ed. (Reading, MA: Addison-Wesley), Chapter 30.

# Root Finding and Nonlinear Sets of Equations

# 9.0 Introduction

We now consider that most basic of tasks, solving equations numerically. While most equations are born with both a right-hand side and a left-hand side, one traditionally moves all terms to the left, leaving

$$
f ( x ) = 0
$$

whose solution or solutions are desired. When there is only one independent variable, the problem is one-dimensional, namely to find the root or roots of a function.

With more than one independent variable, more than one equation can be satisfied simultaneously. You likely once learned the implicit function theorem, which (in this context) gives us the hope of satisfying $N$ equations in $N$ unknowns simultaneously. Note that we have only hope, not certainty. A nonlinear set of equations may have no (real) solutions at all. Contrariwise, it may have more than one solution. The implicit function theorem tells us that “generically” the solutions will be distinct, pointlike, and separated from each other. If, however, life is so unkind as to present you with a nongeneric, i.e., degenerate, case, then you can get a continuous family of solutions. In vector notation, we want to find one or more $N$ -dimensional solution vectors $\mathbf { X }$ such that

$$
\mathbf { f } \left( \mathbf { x } \right) = \mathbf { 0 }
$$

where f is the $N$ -dimensional vector-valued function whose components are the individual equations to be satisfied simultaneously.

Don’t be fooled by the apparent notational similarity of equations (9.0.2) and (9.0.1). Simultaneous solution of equations in $N$ dimensions is much more difficult than finding roots in the one-dimensional case. The principal difference between one and many dimensions is that, in one dimension, it is possible to bracket or “trap” a root between bracketing values, and then hunt it down like a rabbit. In multidimensions, you can never be sure that the root is there at all until you have found it.

Except in linear problems, root finding invariably proceeds by iteration, and this is equally true in one or in many dimensions. Starting from some approximate trial solution, a useful algorithm will improve the solution until some predetermined convergence criterion is satisfied. For smoothly varying functions, good algorithms will always converge, provided that the initial guess is good enough. Indeed one can even determine in advance the rate of convergence of most algorithms.

It cannot be overemphasized, however, how crucially success depends on having a good first guess for the solution, especially for multidimensional problems. This crucial beginning usually depends on analysis rather than numerics. Carefully crafted initial estimates reward you not only with reduced computational effort, but also with understanding and increased self-esteem. Hamming’s motto, “the purpose of computing is insight, not numbers,” is particularly apt in the area of finding roots. You should repeat this motto aloud whenever your program converges, with sixteendigit accuracy, to the wrong root of a problem, or whenever it fails to converge because there is actually no root, or because there is a root but your initial estimate was not sufficiently close to it.

“This talk of insight is all very well, but what do I actually do?” For onedimensional root finding, it is possible to give some straightforward answers: You should try to get some idea of what your function looks like before trying to find its roots. If you need to mass-produce roots for many different functions, then you should at least know what some typical members of the ensemble look like. Next, you should always bracket a root, that is, know that the function changes sign in an identified interval, before trying to converge to the root’s value.

Finally (this is advice with which some daring souls might disagree, but we give it nonetheless) never let your iteration method get outside of the best bracketing bounds obtained at any stage. We will see below that some pedagogically important algorithms, such as the secant method or Newton-Raphson, can violate this last constraint and are thus not recommended unless certain fixups are implemented.

Multiple roots, or very close roots, are a real problem, especially if the multiplicity is an even number. In that case, there may be no readily apparent sign change in the function, so the notion of bracketing a root — and maintaining the bracket — becomes difficult. We are hard-liners: We nevertheless insist on bracketing a root, even if it takes the minimum-searching techniques of Chapter 10 to determine whether a tantalizing dip in the function really does cross zero. (You can easily modify the simple golden section routine of $\ S 1 0 . 2$ to return early if it detects a sign change in the function. And, if the minimum of the function is exactly zero, then you have found a double root.)

As usual, we want to discourage you from using routines as black boxes without understanding them. However, as a guide to beginners, here are some reasonable starting points:

- Brent’s algorithm in $\ S 9 . 3$ is the method of choice to find a bracketed root of a general one-dimensional function, when you cannot easily compute the function’s derivative. Ridders’ method $( \ S 9 . 2 )$ is concise, and a close competitor. When you can compute the function’s derivative, the routine rtsafe in $\ S 9 . 4$ , which combines the Newton-Raphson method with some bookkeeping on the bounds, is recommended. Again, you must first bracket your root. If you can easily compute two derivatives, then Halley’s method (-9.4.2) is often worth a try.

- Roots of polynomials are a special case. Laguerre’s method, in $\ S 9 . 5$ , is recommended as a starting point. Beware: Some polynomials are ill-conditioned! Finally, for multidimensional problems, the only elementary method is Newton-Raphson (-9.6), which works very well if you can supply a good first guess of the solution. Try it. Then read the more advanced material in $\ S 9 . 7$ for some more complicated, but globally more convergent, alternatives.

The routines in this chapter require that you input the function whose roots you seek. For maximum flexibility, the routines typically will accept either a function or a functor (see $\ S 1 . 3 . 3 )$ .

# 9.0.1 Graphical Search for Roots

It never hurts to look at your function, especially if you encounter any difficulty in finding its roots blindly. If you are thus hunting roots “by eye,” it is useful to have a routine that repeatedly plots a function to the screen, accepting user-supplied lower and upper limits for $x$ , automatically scaling $y$ , and making zero crossings visible. The following routine, or something like it, can occasionally save you a lot of grief.

# scrsho.h template<class T> void scrsho(T &fx) {

Graph the function or functor fx over the prompted-for interval x1,x2. Query for another plot   
until the user signals satisfaction. const Int RES $\mathtt { \mathtt { = 5 0 0 } }$ ; Number of function evaluations for each plot. const Doub XLL=75., XUR 525., YLL $\cdot ^ { = }$ 250., YUR=700.; Corners of plot, in points. char \*plotfilename $=$ tmpnam(NULL); VecDoub xx(RES), yy(RES); Doub x1,x2; Int i; for (;;) { Doub ymax $=$ -9.99e99, ymin $\ c = \ 9$ .99e99, del; cout $< <$ endl $< <$ "Enter x1 x2 ( $\bf { \chi } _ { x 1 } = \bf { \chi } _ { x 2 }$ to stop):" << endl; cin $> >$ x1 >> x2; Query for another plot, quit if $\tt x 1 { = } \tt x 2$ . if $\scriptstyle \mathbf { x } 1 = = \mathbf { x } 2$ ) break; for ( $\scriptstyle { \dot { \mathbf { 1 } } } = 0$ ;i<RES; $\dot { 1 } + +$ ) { Evaluate the function at equal intervals. Find xx[i] $=$ x1 + i\*(x2-x1)/(RES-1.); the largest and smallest values. yy[i] $=$ fx(xx[i]); if (yy[i] $>$ ymax) ymax=yy[i]; if (yy[i] $<$ ymin) ymin=yy[i]; } del = 0.05\*((ymax-ymin) $^ +$ (ymax ${ \bf \Phi } = =$ ymin ? abs(ymax) : 0.)); Plot commands, following, are in PSplot syntax (-22.1). You can substitute commands for your favorite plotting package. PSpage pg(plotfilename); PSplot plot(pg,XLL,XUR,YLL,YUR); plot.setlimits(x1,x2,ymin-del,ymax+del); plot.frame(); plot.autoscales(); plot.lineplot(xx,yy); if (ymax\*ymin $< 0 .$ ) plot.lineseg(x1,0.,x2,0.); plot.display(); } remove(plotfilename);

# CITED REFERENCES AND FURTHER READING:

Stoer, J., and Bulirsch, R. 2002, Introduction to Numerical Analysis, 3rd ed. (New York: Springer), Chapter 5.

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapters 2, 7, and 14.   
Deuflhard, P. 2004, Newton Methods for Nonlinear Problems (Berlin: Springer).   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), Chapter 8.   
Householder, A.S. 1970, The Numerical Treatment of a Single Nonlinear Equation (New York: McGraw-Hill).

# 9.1 Bracketing and Bisection

We will say that a root is bracketed in the interval $( a , b )$ if $f ( a )$ and $f ( b )$ have opposite signs. If the function is continuous, then at least one root must lie in that interval (the intermediate value theorem). If the function is discontinuous, but bounded, then instead of a root there might be a step discontinuity that crosses zero (see Figure 9.1.1). For numerical purposes, that might as well be a root, since the behavior is indistinguishable from the case of a continuous function whose zero crossing occurs in between two “adjacent” floating-point numbers in a machine’s finite-precision representation. Only for functions with singularities is there the possibility that a bracketed root is not really there, as for example

$$
f ( x ) = { \frac { 1 } { x - c } }
$$

Some root-finding algorithms (e.g., bisection in this section) will readily converge to $c$ in (9.1.1). Luckily there is not much possibility of your mistaking $c$ , or any number $x$ close to it, for a root, since mere evaluation of $\vert f ( x ) \vert$ will give a very large, rather than a very small, result.

If you are given a function in a black box, there is no sure way of bracketing its roots, or even of determining that it has roots. If you like pathological examples, think about the problem of locating the two real roots of equation (3.0.1), which dips below zero only in the ridiculously small interval of about $x = \pi \pm 1 0 ^ { - 6 6 7 }$ .

In the next chapter we will deal with the related problem of bracketing a function’s minimum. There it is possible to give a procedure that always succeeds; in essence, “Go downhill, taking steps of increasing size, until your function starts back uphill.” There is no analogous procedure for roots. The procedure “go downhill until your function changes sign,” can be foiled by a function that has a simple extremum. Nevertheless, if you are prepared to deal with a “failure” outcome, this procedure is often a good first start; success is usual if your function has opposite signs in the limit $x  \pm \infty$ .

# template <class T>

# roots.h

Bool zbrac(T &func, Doub &x1, Doub &x2)

Given a function or functor func and an initial guessed range $\tt x 1$ to $\mathbf { x } 2$ , the routine expands the range geometrically until a root is bracketed by the returned values x1 and $\mathbf { x } 2$ (in which case zbrac returns true) or until the range becomes unacceptably large (in which case zbrac returns false).

const Int NTRY=50;   
const Doub FACTOR $\ L = 1$ .6;   
if $\mathbf { \bar { \Psi } } _ { \mathbf { x } 1 } \ \mathbf { \Psi } = = \ \mathbf { \Psi } _ { \mathbf { x } 2 } ,$ ) throw("Bad initial range in zbrac");   
Doub f1=func(x1);   
Doub f2=func(x2);   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<NTRY;j $^ { + + }$ ) { if (f1\*f2 $<$ 0.0) return true; if (abs(f1) $<$ abs(f2)) f1=func(x1 $+ =$ FACTOR\*(x1-x2)); else f2=func(x2 += FACTOR\*(x2-x1));   
}   
return false;

![](images/77393d599f05c30de0663e80eebaace283dac1ab7b6c94ef11135e701ecff748.jpg)  
Figure 9.1.1. Some situations encountered while root finding: (a) an isolated root $x _ { 1 }$ bracketed by two points $^ { a }$ and $^ { b }$ at which the function has opposite signs; (b) there is not necessarily a sign change in the function near a double root (in fact, there is not necessarily a root!); (c) a pathological function with many roots; in (d) the function has opposite signs at points $^ { a }$ and $^ { b }$ , but the points bracket a singularity, not a root.

Alternatively, you might want to “look inward” on an initial interval, rather than “look outward” from it, asking if there are any roots of the function $f ( x )$ in the interval from $x _ { 1 }$ to $x _ { 2 }$ when a search is carried out by subdivision into n equal intervals. The following function calculates brackets for distinct intervals that each contain one or more roots.

# template <class T>

void zbrak(T &fx, const Doub x1, const Doub x2, const Int n, VecDoub_O &xb1, VecDoub_O &xb2, Int &nroot)

Given a function or functor fx defined on the interval $[ \mathbf { x } \mathbf { 1 } , \mathbf { x } 2 ]$ , subdivide the interval into n equally spaced segments, and search for zero crossings of the function. nroot will be set to the number of bracketing pairs found. If it is positive, the arrays xb1[0..nroot-1] and xb2[0..nroot-1] will be filled sequentially with any bracketing pairs that are found. On input, these vectors may have any size, including zero; they will be resized to $\geq$ nroot. {

Int $n \mathrm { { b } = } 2 0$ ; xb1.resize(nb); xb2.resize(nb); nroot ${ = } 0$ ; Doub ${ \tt d x } = \left( { \tt x } 2 \mathrm { - x } 1 \right) / { \tt n } ;$ Determine the spacing appropriate to the mesh. Doub $\tt x { = } \tt x 1$ ; Doub fp=fx(x1); for (Int $\scriptstyle { \dot { \bar { 1 } } } = 0$ ;i<n;i++) { Loop over all intervals Doub fc=fx $( { \textbf { x } } + = { \mathrm { d } } \mathbf { x } )$ ; if (fc\*fp $< = ~ 0 . 0$ ) { If a sign change occurs, then record values for the xb1[nroot] $= 8$ -dx; bounds. xb2[nroot $\mathbf { \partial } + + \mathbf { \partial } ] = \mathbf { x }$ ; if(nroot $= =$ nb) { VecDoub tempvec1(xb1),tempvec2(xb2); xb1.resize(2\*nb); xb2.resize(2\*nb); for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ; j<nb; j++) { xb1[j] $=$ tempvec1[j]; xb2[j] $=$ tempvec2[j]; } nb \*= 2; } } fp=fc; } }

# 9.1.1 Bisection Method

Once we know that an interval contains a root, several classical procedures are available to refine it. These proceed with varying degrees of speed and sureness toward the answer. Unfortunately, the methods that are guaranteed to converge plod along most slowly, while those that rush to the solution in the best cases can also dash rapidly to infinity without warning if measures are not taken to avoid such behavior.

The bisection method is one that cannot fail. It is thus not to be sneered at as a method for otherwise badly behaved problems. The idea is simple. Over some interval the function is known to pass through zero because it changes sign. Evaluate the function at the interval’s midpoint and examine its sign. Use the midpoint to replace whichever limit has the same sign. After each iteration the bounds containing the root decrease by a factor of two. If after $n$ iterations the root is known to be within an interval of size $\epsilon _ { n }$ , then after the next iteration it will be bracketed within an interval of size

$$
\epsilon _ { n + 1 } = \epsilon _ { n } / 2
$$

neither more nor less. Thus, we know in advance the number of iterations required to achieve a given tolerance in the solution,

$$
n = \log _ { 2 } \frac { \epsilon _ { 0 } } { \epsilon }
$$

where $\epsilon _ { 0 }$ is the size of the initially bracketing interval and $\epsilon$ is the desired ending tolerance.

Bisection must succeed. If the interval happens to contain more than one root, bisection will find one of them. If the interval contains no roots and merely straddles a singularity, it will converge on the singularity.

When a method converges as a factor (less than 1) times the previous uncertainty to the first power (as is the case for bisection), it is said to converge linearly. Methods that converge as a higher power,

$$
\epsilon _ { n + 1 } = { \mathrm { c o n s t a n t } } \times ( \epsilon _ { n } ) ^ { m } \qquad m > 1
$$

are said to converge superlinearly. In other contexts, “linear” convergence would be termed “exponential” or “geometrical.” That is not too bad at all: Linear convergence means that successive significant figures are won linearly with computational effort.

It remains to discuss practical criteria for convergence. It is crucial to keep in mind that only a finite set of floating point values have exact computer representations. While your function might analytically pass through zero, it is probable that its computed value is never zero, for any floating-point argument. One must decide what accuracy on the root is attainable: Convergence to within $1 0 ^ { - 1 0 }$ in absolute value is reasonable when the root lies near 1 but certainly unachievable if the root lies near $1 0 ^ { 2 6 }$ . One might thus think to specify convergence by a relative (fractional) criterion, but this becomes unworkable for roots near zero. To be most general, the routines below will require you to specify an absolute tolerance, such that iterations continue until the interval becomes smaller than this tolerance in absolute units. Often you may wish to take the tolerance to be $\epsilon ( | x _ { 1 } | + | x _ { 2 } | ) / 2$ , where $\epsilon$ is the machine precision and $x _ { 1 }$ and $x _ { 2 }$ are the initial brackets. When the root lies near zero you ought to consider carefully what reasonable tolerance means for your function. The following routine quits after 50 bisections in any event, with $2 ^ { - 5 0 } \approx 1 0 ^ { - 1 5 }$ .

template <class $\mathrm { T } >$   
Doub rtbis(T &func, const Doub x1, const Doub x2, const Doub xacc) {   
Using bisection, return the root of a function or functor func known to lie between x1 and $\tt x 2$ The root will be refined until its accuracy is ˙xacc.   
const Int JMAX $\mathtt { = 5 0 }$ ; Maximum allowed number of bisections.   
Doub dx,xmid,rtb;   
Doub f=func(x1);   
Doub fmid=func(x2);   
if (f\*fmid $> = \ 0 . 0 $ ) throw("Root must be bracketed for bisection in rtbis");   
rtb $\mathbf { \Sigma } = \mathbf { \Sigma } _ { \mathbf { f } } \ < \ \mathbf { \Sigma } 0 . 0$ ? (dx=x2-x1,x1) : (dx=x1-x2,x2); Orient the search so that $\mathtt { f } > 0$   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<JMAX;j++) { lies at $\tt x { + d x }$ . fmid=func(xmid=rtb+(dx $* = \ 0 . 5 )$ ); Bisection loop. if (fmid $< = \ 0 . 0$ ) rtb $=$ xmid; if (abs(dx) $<$ xacc || fmid $\mathrm { ~  ~ \omega ~ } = \mathrm { ~  ~ 0 ~ . ~ 0 ~ }$ ) return rtb;   
}   
throw("Too many bisections in rtbis");

# 9.2 Secant Method, False Position Method, and Ridders' Method

For functions that are smooth near a root, the methods known respectively as false position (or regula falsi) and the secant method generally converge faster than bisection. In both of these methods the function is assumed to be approximately linear in the local region of interest, and the next improvement in the root is taken as the point where the approximating line crosses the axis. After each iteration, one of the previous boundary points is discarded in favor of the latest estimate of the root.

The only difference between the methods is that secant retains the most recent of the prior estimates (Figure 9.2.1; this requires an arbitrary choice on the first iteration), while false position retains that prior estimate for which the function value has the opposite sign from the function value at the current best estimate of the root, so that the two points continue to bracket the root (Figure 9.2.2). Mathematically, the secant method converges more rapidly near a root of a sufficiently continuous function. Its order of convergence can be shown to be the “golden ratio” 1:618 : : : , so that

$$
\operatorname* { l i m } _ { k \to \infty } | \epsilon _ { k + 1 } | \approx \mathrm { c o n s t } \times \left| \epsilon _ { k } \right| ^ { 1 . 6 1 8 }
$$

The secant method has, however, the disadvantage that the root does not necessarily remain bracketed. For functions that are not sufficiently continuous, the algorithm can therefore not be guaranteed to converge: Local behavior might send it off toward infinity.

False position, since it sometimes keeps an older rather than newer function evaluation, has a lower order of convergence. Since the newer function value will sometimes be kept, the method is often superlinear, but estimation of its exact order is not so easy.

Here are sample implementations of these two related methods. While these methods are standard textbook fare, Ridders’ method, described below, or Brent’s method, described in the next section, are almost always better choices. Figure 9.2.3 shows the behavior of the secant and false-position methods in a difficult situation.

![](images/9c4674472d84dcefae577e4283cf37bbe0a308f1e2208567d89c9a48caf87957.jpg)  
Figure 9.2.1. Secant method. Extrapolation or interpolation lines (dashed) are drawn through the two most recently evaluated points, whether or not they bracket the function. The points are numbered in the order that they are used.

![](images/158439ee96f87291f4bdb0106717fd5d60dc1b176bdf891ae34ecdf73d3e9c23.jpg)  
Figure 9.2.2. False-position method. Interpolation lines (dashed) are drawn through the most recent points that bracket the root. In this example, point 1 thus remains “active” for many steps. False position converges less rapidly than the secant method, but it is more certain.

![](images/419b089202f3a300c5b96880a99cc39e4ca142ad93dbc3d213dfcf91f376b0da.jpg)  
Figure 9.2.3. Example where both the secant and false-position methods will take many iterations to arrive at the true root. This function would be difficult for many other root-finding methods.

# template <class T>

Doub rtflsp(T &func, const Doub x1, const Doub x2, const Doub xacc) { Using the false-position method, return the root of a function or functor func known to lie between x1 and $\tt x 2$ . The root is refined until its accuracy is ˙xacc.

const Int MAXIT $\mathtt { . = } 3 0$ ; Set to the maximum allowed number of iterations.   
Doub xl,xh,del;   
Doub fl=func(x1);   
Doub fh func(x2); Be sure the interval brackets a root.   
if (fl\*fh $> 0 . 0 \dot { . }$ ) throw("Root must be bracketed in rtflsp");   
if $( \pm 1 < 0 . 0 )$ ) { Identify the limits so that xl corresponds to the low $\tt x 1 = \tt x 1$ ; side. xh $\scriptstyle = \mathtt { x } 2$ ;   
} else { $\tt x 1 = \tt x 2$ ; xh $\scriptstyle = \mathtt { x 1 }$ ; SWAP(fl,fh);   
Doub dx=xh-xl;   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<MAXIT;j++) { False-position loop. Doub rtf $=$ xl+dx\*fl/(fl-fh); Increment with respect to latest value. Doub f=func(rtf); if $\mathit { \Omega } , \mathit { \Phi } , \mathit { \Phi } , 0 , 0 ,$ ) { Replace appropriate limit. del=xl-rtf; xl=rtf; fl=f; } else { del=xh-rtf; xh=rtf; $\operatorname { f h } = \operatorname { f }$ ; dx=xh-xl; if (abs(del) $<$ xacc || $\mathrm { ~ \\underline ~ { ~ f ~ } ~ } = = \mathrm { ~ \ 0 ~ . 0 ~ } ,$ ) return rtf; Convergence.

throw("Maximum number of iterations exceeded in rtflsp");

template <class T>   
Doub rtsec(T &func, const Doub x1, const Doub x2, const Doub xacc) {   
Using the secant method, return the root of a function or functor func thought to lie between x1 and $\mathbf { x } 2$ . The root is refined until its accuracy is ˙xacc.   
const Int MAXIT $\scriptstyle = 3 0$ ; Maximum allowed number of iterations.   
Doub xl,rts;   
Doub fl=func(x1);   
Doub $\mathtt { f } =$ func(x2);   
if (abs(fl) $<$ abs(f)) Pick the bound with the smaller function value a rts=x1; the most recent guess. $\tt x 1 = \tt x 2$ ; SWAP(fl,f); else { xl=x1; rts=x2;   
}   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<MAXIT;j++) { Secant loop. Doub dx (xl-rts)\*f/(f-fl); Increment with respect to latest value. xl=rts; $\pounds 1 = \pounds$ ; rts $+ =$ dx; $\mathtt { f } =$ func(rts); if (abs(dx) < xacc || $\textbf { f } = = \textbf { 0 } . 0$ ) return rts; Convergence.   
}   
throw("Maximum number of iterations exceeded in rtsec");

# 9.2.1 Ridders' Method

A powerful variant on false position is due to Ridders [1]. When a root is bracketed between $x _ { 1 }$ and $x _ { 2 }$ , Ridders’ method first evaluates the function at the midpoint $x _ { 3 } = ( x _ { 1 } + x _ { 2 } ) / 2$ . It then factors out that unique exponential function that turns the residual function into a straight line. Specifically, it solves for a factor $e ^ { \boldsymbol { Q } }$ that gives

$$
f ( x _ { 1 } ) - 2 f ( x _ { 3 } ) e ^ { Q } + f ( x _ { 2 } ) e ^ { 2 Q } = 0
$$

This is a quadratic equation in $e ^ { \boldsymbol { Q } }$ , which can be solved to give

$$
e ^ { Q } = { \frac { f ( x _ { 3 } ) + \mathrm { s i g n } [ f ( x _ { 2 } ) ] \sqrt { f ( x _ { 3 } ) ^ { 2 } - f ( x _ { 1 } ) f ( x _ { 2 } ) } } { f ( x _ { 2 } ) } }
$$

Now the false-position method is applied, not to the values $f ( x _ { 1 } ) , f ( x _ { 3 } ) , f ( x _ { 2 } )$ , but to the values $\bar { f } ( x _ { 1 } ) , f ( x _ { 3 } ) e ^ { Q } , f ( x _ { 2 } ) e ^ { 2 Q }$ , yielding a new guess for the root, $x _ { 4 }$ . The overall updating formula (incorporating the solution 9.2.3) is

$$
x _ { 4 } = x _ { 3 } + ( x _ { 3 } - x _ { 1 } ) \frac { \mathrm { s i g n } [ f ( x _ { 1 } ) - f ( x _ { 2 } ) ] f ( x _ { 3 } ) } { \sqrt { f ( x _ { 3 } ) ^ { 2 } - f ( x _ { 1 } ) f ( x _ { 2 } ) } }
$$

Equation (9.2.4) has some very nice properties. First, $x _ { 4 }$ is guaranteed to lie in the interval $( x _ { 1 } , x _ { 2 } )$ , so the method never jumps out of its brackets. Second, the convergence of successive applications of equation (9.2.4) is quadratic, that is, $m = 2$ in equation (9.1.4). Since each application of (9.2.4) requires two function evaluations, the actual order of the method is $\sqrt { 2 }$ , not 2; but this is still quite respectably superlinear: The number of significant digits in the answer approximately doubles with each two function evaluations. Third, taking out the function’s “bend” via exponential (that is, ratio) factors, rather than via a polynomial technique (e.g., fitting a parabola), turns out to give an extraordinarily robust algorithm. In both reliability and speed, Ridders’ method is generally competitive with the more highly developed and better established (but more complicated) method of van Wijngaarden, Dekker, and Brent, which we next discuss.

# template <class $\mathrm { T } >$

Doub zriddr(T &func, const Doub x1, const Doub x2, const Doub xacc) { Using Ridders’ method, return the root of a function or functor func known to lie between x1 and $\mathbf { x } 2$ . The root will be refined to an approximate accuracy xacc.

const Int MAXIT $_ { - } = 6 0$ ;   
Doub fl=func(x1);   
Doub fh $\cdot ^ { = }$ func(x2);   
if ( $( \mathbf { f } 1 > 0 . 0$ && fh $< ~ 0 . 0$ ) || (fl < 0.0 && fh > 0.0)) Doub $\tt x l = \tt x l$ ; Doub xh $\scriptstyle 1 = \mathbf { x } 2$ ; Doub ans $=$ -9.99e99; Any highly unlikely value, to simplify logic for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<MAXIT; $\mathrm { i } + +$ ) { below. Doub xm=0.5\*(xl+xh); Doub fm $_ { 1 } =$ func(xm); First of two function evaluations per it-Doub $\mathtt { s } =$ sqrt(fm\*fm-fl\*fh); eration. if ( $\mathrm { ~ s ~ } = = \mathrm { ~ 0 ~ . ~ 0 ~ }$ ) return ans; Doub xnew $\scriptstyle \mathbf { \lambda } = \mathbf { x m } + ( \mathbf { x m } - \mathbf { x } \mathbf { 1 } ) * ( ( \mathbf { f } \mathbf { 1 } \ \mathbf { \lambda } > \mathbf { \lambda } \mathbf { f h } \ \overset { ? } { \mid } \ 1 . 0 \ \ : \ \mathbf { \lambda } - \mathbf { 1 } . 0 ) * \mathbf { f m } / \mathbf { s } ) \ ;$ Updating formula if (abs(xnew-ans) $< =$ xacc) return ans; ans=xnew; Doub fnew=func(ans); Second of two function evaluations per if (fnew $\scriptstyle = = \ 0 . 0 { \mathrm { . } }$ ) return ans; iteration. if (SIGN(fm,fnew) $: = ~ \mathtt { f m } .$ ) { Bookkeeping to keep the root bracketed $\tt x l = \tt x m$ ; on next iteration. fl=fm; xh=ans; fh=fnew; } else if (SIGN(fl,fnew) $! =$ fl) { xh=ans; fh=fnew; } else if (SIGN(fh,fnew) $\downarrow =$ fh) { xl=ans; fl=fnew; } else throw("never get here."); if (abs(xh-xl) $< =$ xacc) return ans; } throw("zriddr exceed maximum iterations");   
}   
else { if ( $\mathrm { ~  ~ \ell ~ } _ { , \pm 1 } = = \mathrm { ~  ~ 0 ~ } _ { , 0 } ,$ ) return x1; if $\mathrm { { ( f h ~ = = ~ 0 . 0 } }$ ) return x2; throw("root must be bracketed in zriddr.");   
}

# CITED REFERENCES AND FURTHER READING:

Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 8 . 3$ .

Ostrowski, A.M. 1966, Solutions of Equations and Systems of Equations, 2nd ed. (New York: Academic Press), Chapter 12.   
Ridders, C.J.F. 1979, “A New Algorithm for Computing a Single Root of a Real Continuous Function,” IEEE Transactions on Circuits and Systems, vol. CAS-26, pp. 979–980.[1]

# 9.3 Van Wijngaarden-Dekker-Brent Method

While secant and false position formally converge faster than bisection, one finds in practice pathological functions for which bisection converges more rapidly. These can be choppy, discontinuous functions, or even smooth functions if the second derivative changes sharply near the root. Bisection always halves the interval, while secant and false position can sometimes spend many cycles slowly pulling distant bounds closer to a root. Ridders’ method does a much better job, but it too can sometimes be fooled. Is there a way to combine superlinear convergence with the sureness of bisection?

Yes. We can keep track of whether a supposedly superlinear method is actually converging the way it is supposed to, and, if it is not, we can intersperse bisection steps so as to guarantee at least linear convergence. This kind of super-strategy requires attention to bookkeeping detail, and also careful consideration of how roundoff errors can affect the guiding strategy. Also, we must be able to determine reliably when convergence has been achieved.

An excellent algorithm that pays close attention to these matters was developed in the 1960s by van Wijngaarden, Dekker, and others at the Mathematical Center in Amsterdam, and later improved by Brent [1]. For brevity, we refer to the final form of the algorithm as Brent’s method. The method is guaranteed (by Brent) to converge, so long as the function can be evaluated within the initial interval known to contain a root.

Brent’s method combines root bracketing, bisection, and inverse quadratic interpolation to converge from the neighborhood of a zero crossing. While the falseposition and secant methods assume approximately linear behavior between two prior root estimates, inverse quadratic interpolation uses three prior points to fit an inverse quadratic function ( $x$ as a quadratic function of $y$ ) whose value at $y = 0$ is taken as the next estimate of the root $x$ . Of course one must have contingency plans for what to do if the root falls outside of the brackets. Brent’s method takes care of all that. If the three point pairs are $[ a , f ( a ) ] , [ b , f ( b ) ] , [ c , f ( c ) ]$ , then the interpolation formula (cf. equation 3.2.1) is

$$
\begin{array} { l } { \displaystyle { x = \frac { [ y - f ( a ) ] [ y - f ( b ) ] c } { [ f ( c ) - f ( a ) ] [ f ( c ) - f ( b ) ] } + \frac { [ y - f ( b ) ] [ y - f ( c ) ] a } { [ f ( a ) - f ( b ) ] [ f ( a ) - f ( c ) ] } } } \\ { \displaystyle { + \frac { [ y - f ( c ) ] [ y - f ( a ) ] b } { [ f ( b ) - f ( c ) ] [ f ( b ) - f ( a ) ] } } } \end{array}
$$

Setting $y$ to zero gives a result for the next root estimate, which can be written as

$$
x = b + P / Q
$$

where, in terms of

$$
R \equiv f ( b ) / f ( c ) , \qquad S \equiv f ( b ) / f ( a ) , \qquad T \equiv f ( a ) / f ( c )
$$

we have

$$
\begin{array} { l } { P = S \left[ T ( R - T ) ( c - b ) - ( 1 - R ) ( b - a ) \right] } \\ { Q = ( T - 1 ) ( R - 1 ) ( S - 1 ) } \end{array}
$$

In practice $b$ is the current best estimate of the root and $P / Q$ ought to be a “small” correction. Quadratic methods work well only when the function behaves smoothly; they run the serious risk of giving very bad estimates of the next root or causing machine failure by an inappropriate division by a very small number ( $Q \approx 0 ,$ . Brent’s method guards against this problem by maintaining brackets on the root and checking where the interpolation would land before carrying out the division. When the correction $P / Q$ would not land within the bounds, or when the bounds are not collapsing rapidly enough, the algorithm takes a bisection step. Thus, Brent’s method combines the sureness of bisection with the speed of a higher-order method when appropriate. We recommend it as the method of choice for general one-dimensional root finding where a function’s values only (and not its derivative or functional form) are available.

# template <class $\mathrm { T } >$

Doub zbrent(T &func, const Doub x1, const Doub x2, const Doub tol)   
Using Brent’s method, return the root of a function or functor func known to lie between x1 and $\mathbf { x } 2$ . The root will be refined until its accuracy is tol.   
{   
const Int ITMAX $\cdot ^ { = }$ 100; Maximum allowed number of iterations.   
const Doub EPS $=$ numeric_limits<Doub>::epsilon();   
Machine floating-point precision.   
Doub a=x1,b=x2, ${ \tt c } = { \tt x } 2$ ,d,e,fa=func(a),fb $=$ func(b),fc,p,q,r,s,tol1,xm;   
if ( $\mathrm { ( f a ~ > ~ 0 . 0 ~ }$ && fb $> ~ 0 . 0$ ) || (fa $<$ 0.0 && fb $< 0 . 0 )$ ) throw("Root must be bracketed in zbrent");   
fc=fb;   
for (Int iter ${ \tt = } 0$ ;iter<ITMAX;iter++) { if ((fb $>$ 0.0 && fc $>$ 0.0) || (fb < 0.0 && fc < 0.0)) { $\mathtt { c } = \mathtt { a }$ ; Rename a, b, c and adjust bounding interva fc=fa; d. e=d=b-a; } if (abs(fc) < abs(fb)) { a=b; $\mathtt { b } = _ { \mathtt { C } }$ ; $\mathtt { c } = \mathtt { a }$ ; fa fb; fb=fc; fc=fa; } tol1 $^ { - 2 }$ .0\*EPS\*abs(b) $+ 0$ .5\*tol; Convergence check. xm=0.5\*(c-b); if (abs(xm) $< =$ tol1 || fb $\mathrm { = = } \ 0 . 0$ ) return b; if (abs(e) $> =$ tol1 && abs(fa) $>$ abs(fb)) { s=fb/fa; Attempt inverse quadratic interpolation. if ( $a ~ = = ~ c$ ) { p=2.0\*xm\*s; q=1.0-s; } else { q=fa/fc; r=fb/fc; p=s\*(2.0\*xm\*q\*(q-r)-(b-a)\*(r-1.0)); q=(q-1.0)\*(r-1.0)\*(s-1.0); } if $\mathrm { ( p ~ > ~ 0 . 0 } ) ,$ ) q = -q; Check whether in bounds. p=abs(p);

Doub min1 $\mathtt { . 3 }$ .0\*xm\*q-abs(tol1\*q); Doub min2 $\cdot =$ abs(e\*q); if (2.0\*p < (min1 $<$ min2 ? min1 : min2)) { e=d; Accept interpolation. d=p/q; } else { d=xm; Interpolation failed, use bisection. e=d; } } else { Bounds decreasing too slowly, use bisection. d=xm; e=d; } a=b; Move last best guess to a. fa=fb; if (abs(d) $>$ tol1) Evaluate new trial root. b $+ =$ d; else b $+ =$ SIGN(tol1,xm); fb=func(b); } throw("Maximum number of iterations exceeded in zbrent");

# CITED REFERENCES AND FURTHER READING:

Brent, R.P. 1973, Algorithms for Minimization without Derivatives (Englewood Cliffs, NJ: Prentice-Hall); reprinted 2002 (New York: Dover), Chapters 3, 4.[1]   
Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods for Mathematical Computations (Englewood Cliffs,NJ: Prentice-Hall), $\ S 7 . 2$ .

# 9.4 Newton-Raphson Method Using Derivative

Perhaps the most celebrated of all one-dimensional root-finding routines is Newton’s method, also called the Newton-Raphson method. Joseph Raphson (1648– 1715) was a contemporary of Newton who independently invented the method in 1690, some 20 years after Newton did, but some 20 years before Newton actually published it. This method is distinguished from the methods of previous sections by the fact that it requires the evaluation of both the function $f ( x )$ and the derivative $f ^ { \prime } ( x )$ , at arbitrary points $x$ . The Newton-Raphson formula consists geometrically of extending the tangent line at a current point $x _ { i }$ until it crosses zero, then setting the next guess $x _ { i + 1 }$ to the abscissa of that zero crossing (see Figure 9.4.1). Algebraically, the method derives from the familiar Taylor series expansion of a function in the neighborhood of a point,

$$
f ( x + \delta ) \approx f ( x ) + f ^ { \prime } ( x ) \delta + { \frac { f ^ { \prime \prime } ( x ) } { 2 } } \delta ^ { 2 } + \cdots
$$

For small enough values of $\delta$ , and for well-behaved functions, the terms beyond linear are unimportant, hence $f ( x + \delta ) = 0$ implies

$$
\delta = - \frac { f ( x ) } { f ^ { \prime } ( x ) }
$$

![](images/f5daa2a77fbfe8d31869e5a6171f3ef7f94926bf64db45b5abdc754c321b7289.jpg)  
Figure 9.4.1. Newton’s method extrapolates the local derivative to find the next estimate of the root. In this example it works well and converges quadratically.

Newton-Raphson is not restricted to one dimension. The method readily generalizes to multiple dimensions, as we shall see in $\ S 9 . 6$ and $\ S 9 . 7$ , below.

Far from a root, where the higher-order terms in the series are important, the Newton-Raphson formula can give grossly inaccurate, meaningless corrections. For instance, the initial guess for the root might be so far from the true root as to let the search interval include a local maximum or minimum of the function. This can be death to the method (see Figure 9.4.2). If an iteration places a trial guess near such a local extremum, so that the first derivative nearly vanishes, then Newton-Raphson sends its solution off to limbo, with vanishingly small hope of recovery. Figure 9.4.3 demonstrates another possible pathology.

Why is Newton-Raphson so powerful? The answer is its rate of convergence: Within a small distance $\epsilon$ of $x$ , the function and its derivative are approximately

$$
\begin{array} { l } { { f ( x + \epsilon ) = f ( x ) + \epsilon f ^ { \prime } ( x ) + \epsilon ^ { 2 } \displaystyle \frac { f ^ { \prime \prime } ( x ) } { 2 } + \cdots , } } \\ { { f ^ { \prime } ( x + \epsilon ) = f ^ { \prime } ( x ) + \epsilon f ^ { \prime \prime } ( x ) + \cdots } } \end{array}
$$

By the Newton-Raphson formula,

$$
x _ { i + 1 } = x _ { i } - { \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) } }
$$

so that

$$
\epsilon _ { i + 1 } = \epsilon _ { i } - \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) }
$$

![](images/847c1bc26105317049f229e2b32415f9721eb4620872f497663abc48dbec82ee.jpg)  
Figure 9.4.2. Unfortunate case where Newton’s method encounters a local extremum and shoots off to outer space. Here bracketing bounds, as in rtsafe, would save the day.

![](images/d5750adcb1abd1453aa91b046ab0c7fa7b2a1497a810745f4a0cf279a3e24f87.jpg)  
Figure 9.4.3. Unfortunate case where Newton’s method enters a nonconvergent cycle. This behavior is often encountered when the function $f$ is obtained, in whole or in part, by table interpolation. With a better initial guess, the method would have succeeded.

When a trial solution $x _ { i }$ differs from the true root by $\epsilon _ { i }$ , we can use (9.4.3) to express $f ( x _ { i } )$ ; $f ^ { \prime } ( x _ { i } )$ in (9.4.4) in terms of $\epsilon _ { i }$ and derivatives at the root itself. The result is a recurrence relation for the deviations of the trial solutions

$$
\epsilon _ { i + 1 } = - \epsilon _ { i } ^ { 2 } \frac { f ^ { \prime \prime } ( x ) } { 2 f ^ { \prime } ( x ) }
$$

Equation (9.4.6) says that Newton-Raphson converges quadratically (cf. equation 9.2.3). Near a root, the number of significant digits approximately doubles with each step. This very strong convergence property makes Newton-Raphson the method of choice for any function whose derivative can be evaluated efficiently, and whose derivative is continuous and nonzero in the neighborhood of a root.

Even where Newton-Raphson is rejected for the early stages of convergence (because of its poor global convergence properties), it is very common to “polish up” a root with one or two steps of Newton-Raphson, which can multiply by two or four its number of significant figures.

For an efficient realization of Newton-Raphson, the user provides a routine that evaluates both $f ( x )$ and its first derivative $f ^ { \prime } ( x )$ at the point $x$ . The Newton-Raphson formula can also be applied using a numerical difference to approximate the true local derivative,

$$
f ^ { \prime } ( x ) \approx { \frac { f ( x + d x ) - f ( x ) } { d x } }
$$

This is not, however, a recommended procedure for the following reasons: (i) You are doing two function evaluations per step, so at best the superlinear order of convergence will be only $\sqrt { 2 }$ . (ii) If you take $d x$ too small, you will be wiped out by roundoff, while if you take it too large, your order of convergence will be only linear, no better than using the initial evaluation $f ^ { \prime } ( x _ { 0 } )$ for all subsequent steps. Therefore, Newton-Raphson with numerical derivatives is (in one dimension) always dominated by Brent’s method (-9.3). (In multidimensions, where there is a paucity of available methods, Newton-Raphson with numerical derivatives must be taken more seriously. See $\ S 9 . 6 - \ S 9 . 7 . )$

The following routine invokes a user-supplied structure that supplies the function value and the derivative. The function value is returned in the usual way as a functor by overloading operator(), while the derivative is returned by the df function in the structure. For example, to find a root of the Bessel function $J _ { 0 } ( x )$ (derivative $- J _ { 1 } ( x ) )$ you would have a structure like

struct Funcd { Bessjy bess; Doub operator() (const Doub x) { return bess.j0(x); } Doub df(const Doub x) { return -bess.j1(x); }   
};

(While you can use any name for Funcd, the name df is fixed.) Your code should then create an instance of this structure and pass it to rtnewt:

Funcd fx;   
Doub root=rtnewt(fx,x1,x2,xacc);

The routine rtnewt includes input bounds on the root $\tt x 1$ and $_ { \tt X 2 }$ simply to be consistent with previous root-finding routines: Newton does not adjust bounds, and works only on local information at the point x. The bounds are used only to pick the midpoint as the first guess, and to reject the solution if it wanders outside of the bounds.

# roots.h template <class T>

Doub rtnewt(T &funcd, const Doub x1, const Doub x2, const Doub xacc) {

Using the Newton-Raphson method, return the root of a function known to lie in the interval $[ \mathbf { x } \mathbf { 1 } , \mathbf { x } 2 ]$ . The root will be refined until its accuracy is known within ˙xacc. funcd is a usersupplied struct that returns the function value as a functor and the first derivative of the function at the point $\mathbf { x }$ as the function df (see text).

const Int JMAX $= 2 0$ ; Set to maximu   
Doub rtn $_ { = 0 }$ .5\*( $\bf { x } 1 + \bf { x } 2 )$ ; Initial guess.   
for (Int $\scriptstyle { \dot { \mathsf { J } } } = 0$ ;j<JMAX; $\mathrm { j } + +$ ) { Doub $\mathtt { f } =$ funcd(rtn); Doub df=funcd.df(rtn); Doub dx=f/df; rtn $- =$ dx; if ((x1-rtn)\*(rtn-x2) < 0.0) throw("Jumped out of brackets in rtnewt"); if (abs(dx) $<$ xacc) return rtn; Convergence.   
}   
throw("Maximum number of iterations exceeded in rtnewt"

While Newton-Raphson’s global convergence properties are poor, it is fairly easy to design a fail-safe routine that utilizes a combination of bisection and Newton-Raphson. The hybrid algorithm takes a bisection step whenever Newton-Raphson would take the solution out of bounds, or whenever Newton-Raphson is not reducing the size of the brackets rapidly enough.

# roots.h template <class T>

Doub rtsafe(T &funcd, const Doub x1, const Doub x2, const Doub xacc) {

Using a combination of Newton-Raphson and bisection, return the root of a function bracketed between $\tt x 1$ and $\mathbf { x } 2$ . The root will be refined until its accuracy is known within ˙xacc. funcd is a user-supplied struct that returns the function value as a functor and the first derivative of the function at the point $\mathbf { x }$ as the function df (see text).

const Int MAXI $\scriptstyle \sum 1 0 0$ ; Maximum allowed number of iterations.   
Doub xh,xl;   
Doub fl=funcd $\mathbf { \Pi } ( \mathbf { x } \mathbf { 1 } )$ ;   
Doub fh=funcd(x2);   
if ( $( \mathbf { f } 1 > 0 . 0 $ && fh $> ~ 0 . 0 \dot { } ,$ ) || $( \pm 1 < 0 . 0$ && fh $< ~ 0 . 0 )$ ) throw("Root must be bracketed in rtsafe");   
if $\mathbf { \dot { f } } 1 \ = = \ 0 . 0 \mathbf { \dot { \Omega } }$ ) return x1;   
if ( $\mathrm { \Delta } \cdot \mathrm { I h } \ = = \ 0 . 0 \mathrm { \cdot }$ ) return x2;   
if ( $\mathbf { \dot { f } } 1 < 0 . 0 \dot { } \dot { }$ ) { Orient the search so that $f ( \mathbf { x } \mathbf { 1 } ) < \mathbf { 0 }$ . $\tt x l = \tt x l$ ; xh ${ \tt = } { \tt x } 2$ ;   
} else { xh=x1; $\tt x 1 = \tt x 2$ ;   
}   
Doub rts ${ = } 0$ .5\*(x1+x2); Initialize the guess for root,   
Doub dxold=abs(x2-x1); the “stepsize before last,”   
Doub dx=dxold; and the last step.   
Doub f=funcd(rts);   
Doub df $=$ funcd.df(rts);   
for (Int $\scriptstyle { \dot { \ j } } = 0$ ;j<MAXIT;j++) { Loop over allowed iterations. if ((((rts-xh)\*df-f)\*((rts-xl)\*df-f) $>$ 0.0) Bisect if Newton out of range, || (abs(2.0\*f) $>$ abs(dxold\*df))) { or not decreasing fast enough

dxold=dx; dx=0.5\*(xh-xl); rts=xl+dx; if (xl $= =$ rts) return rts; Change in root is negligible. } else { Newton step acceptable. Take it. dxold=dx; d $\mathord { \left. \kern - delimiterspace \right.} = \mathbf { f } $ /df; Doub temp=rts; rts $- =$ dx; if (temp $= =$ rts) return rts; if (abs(dx) $<$ xacc) return rts; Convergence criterion. Doub $\mathtt { f } =$ funcd(rts); Doub df=funcd.df(rts); The one new function evaluation per iteration. if $( \pm \ < \ 0 . 0 )$ ) Maintain the bracket on the root. xl=rts; else xh=rts; } throw("Maximum number of iterations exceeded in rtsafe");

For many functions, the derivative $f ^ { \prime } ( x )$ often converges to machine accuracy before the function $f ( x )$ itself does. When that is the case one need not subsequently update $f ^ { \prime } ( x )$ . This shortcut is recommended only when you confidently understand the generic behavior of your function, but it speeds computations when the derivative calculation is laborious. (Formally, this makes the convergence only linear, but if the derivative isn’t changing anyway, you can do no better.)

# 9.4.1 Newton-Raphson and Fractals

An interesting sidelight to our repeated warnings about Newton-Raphson’s unpredictable global convergence properties — its very rapid local convergence notwithstanding — is to investigate, for some particular equation, the set of starting values from which the method does, or doesn’t, converge to a root.

Consider the simple equation

$$
z ^ { 3 } - 1 = 0
$$

whose single real root is $z = 1$ , but which also has complex roots at the other two cube roots of unity, $\exp ( \pm 2 \pi i / 3 )$ . Newton’s method gives the iteration

$$
z _ { j + 1 } = z _ { j } - \frac { z _ { j } ^ { 3 } - 1 } { 3 z _ { j } ^ { 2 } }
$$

Up to now, we have applied an iteration like equation (9.4.9) only for real starting values $z _ { 0 }$ , but in fact all of the equations in this section also apply in the complex plane. We can therefore map out the complex plane into regions from which a starting value $z _ { 0 }$ , iterated in equation (9.4.9), will, or won’t, converge to $z = 1$ . Naively, we might expect to find a “basin of convergence” somehow surrounding the root $z = 1$ . We surely do not expect the basin of convergence to fill the whole plane, because the plane must also contain regions that converge to each of the two complex roots. In fact, by symmetry, the three regions must have identical shapes. Perhaps they will be three symmetric $1 2 0 ^ { \circ }$ wedges, with one root centered in each?

![](images/7e7359e4a158a3506a4a0fe9ffb4c2bc69f473953c7e8c6c27dcee477361e06e.jpg)  
Figure 9.4.4. The complex $z$ -plane with real and imaginary components in the range $( - 2 , 2 )$ . The black region is the set of points from which Newton’s method converges to the root $z = 1$ of the equation $z ^ { \tilde { 3 } } - 1 = 0$ . Its shape is fractal.

Now take a look at Figure 9.4.4, which shows the result of a numerical exploration. The basin of convergence does indeed cover $1 / 3$ the area of the complex plane, but its boundary is highly irregular — in fact, fractal. (A fractal, so called, has self-similar structure that repeats on all scales of magnification.) How does this fractal emerge from something as simple as Newton’s method and an equation as simple as (9.4.8)? The answer is already implicit in Figure 9.4.2, which showed how, on the real line, a local extremum causes Newton’s method to shoot off to infinity. Suppose one is slightly removed from such a point. Then one might be shot off not to infinity, but — by luck — right into the basin of convergence of the desired root. But that means that in the neighborhood of an extremum there must be a tiny, perhaps distorted, copy of the basin of convergence — a kind of “one-bounce away” copy. Similar logic shows that there can be “two-bounce” copies, “three-bounce” copies, and so on. A fractal thus emerges.

Notice that, for equation (9.4.8), almost the whole real axis is in the domain of convergence for the root $z = 1$ . We say “almost” because of the peculiar discrete points on the negative real axis whose convergence is indeterminate (see figure). What happens if you start Newton’s method from one of these points? (Try it.)

# 9.4.2 Halley's Method

Edmund Halley (1656–1742) was a contemporary and close friend of Newton. His contribution to root finding was to extend Newton’s method to use information from the next term in the (as we would now say it) Taylor series, the second derivative $f ^ { \prime \prime } ( x )$ . Omitting a straightforward derivation, the update formula (9.4.4) now becomes

$$
x _ { i + 1 } = x _ { i } - { \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) \left( 1 - { \frac { f ( x _ { i } ) f ^ { \prime \prime } ( x _ { i } ) } { 2 f ^ { \prime } ( x _ { i } ) ^ { 2 } } } \right) } }
$$

You can see that the update scheme is essentially Newton-Raphson, but with an extra, hopefully small, correction term in the denominator.

It only makes sense to use Halley’s method when it is easy to calculate $f ^ { \prime \prime } ( x _ { i } )$ , often from pieces of functions that are already being used in calculating $f ( x _ { i } )$ and $f ^ { \prime } ( x _ { i } )$ . Otherwise, you might just as well do another step of ordinary Newton-Raphson. Halley’s method converges cubically; in the final convergence each iteration triples the number of significant digits. But two steps of Newton-Raphson quadruple that number.

There is no reason to think that the basin of convergence of Halley’s method is generally larger than Newton’s; more often it is probably smaller. So don’t look to Halley’s method for better convergence in the large.

Nevertheless, when you can get a second derivative almost for free, you can often usefully shave an iteration or two off Newton-Raphson by something like this,

$$
x _ { i + 1 } = x _ { i } - { \frac { f ( x _ { i } ) } { f ^ { \prime } ( x _ { i } ) } } { \Bigg / } \operatorname* { m a x } \left[ 0 . 8 , \operatorname* { m i n } \left( 1 . 2 , 1 - { \frac { f ( x _ { i } ) f ^ { \prime \prime } ( x _ { i } ) } { 2 f ^ { \prime } ( x _ { i } ) ^ { 2 } } } \right) \right]
$$

the idea being to limit the influence of the higher-order correction, so that it gets used only in the endgame. We have already used Halley’s method in just this fashion in $\ S 6 . 2 , \ S 6 . 4$ , and $\ S 6 . 1 4$ .

# CITED REFERENCES AND FURTHER READING:

Acton, F.S. 1970, Numerical Methods That Work; 1990, corrected edition (Washington, DC: Mathematical Association of America), Chapter 2.   
Ralston, A., and Rabinowitz, P. 1978, A First Course in Numerical Analysis, 2nd ed.; reprinted 2001 (New York: Dover), $\ S 8 . 4$ .   
Ortega, J., and Rheinboldt, W. 1970, Iterative Solution of Nonlinear Equations in Several Variables (New York: Academic Press); reprinted 20oo (Philadelphia: S.I.A.M.).   
Mandelbrot, B.B. 1983, The Fractal Geometry of Nature (San Francisco: W.H. Freeman).   
Peitgen, H.-O., and Saupe, D. (eds.) 1988, The Science of Fractal Images (New York: Springer).

# 9.5 Roots of Polynomials

Here we give a few methods for finding roots of polynomials. These will serve for most practical problems involving polynomials of low-to-moderate degree or for well-conditioned polynomials of higher degree. Not as well appreciated as it ought to be is the fact that some polynomials are exceedingly ill-conditioned. The tiniest changes in a polynomial’s coefficients can, in the worst case, send its roots sprawling all over the complex plane. (An infamous example due to Wilkinson is detailed by Acton [1].)

Recall that a polynomial of degree $n$ will have $n$ roots. The roots can be real or complex, and they might not be distinct. If the coefficients of the polynomial are real, then complex roots will occur in pairs that are conjugate; i.e., if $x _ { 1 } = a + b i$ is a root, then $x _ { 2 } = a - b i$ will also be a root. When the coefficients are complex, the complex roots need not be related.

Multiple roots, or closely spaced roots, produce the most difficulty for numerical algorithms (see Figure 9.5.1). For example, $P ( x ) = ( x - a ) ^ { 2 }$ has a double real root at $x = a$ . However, we cannot bracket the root by the usual technique of identifying neighborhoods where the function changes sign, nor will slope-following methods such as Newton-Raphson work well, because both the function and its derivative vanish at a multiple root. Newton-Raphson may work, but slowly, since large roundoff errors can occur. When a root is known in advance to be multiple, then special methods of attack are readily devised. Problems arise when (as is generally the case) we do not know in advance what pathology a root will display.

# 9.5.1 Deflation of Polynomials

When seeking several or all roots of a polynomial, the total effort can be significantly reduced by the use of deflation. As each root $r$ is found, the polynomial is factored into a product involving the root and a reduced polynomial of degree one less than the original, i.e., $P ( x ) = ( x - r ) Q ( x )$ . Since the roots of $Q$ are exactly the remaining roots of $P$ , the effort of finding additional roots decreases, because we work with polynomials of lower and lower degree as we find successive roots. Even more important, with deflation we can avoid the blunder of having our iterative method converge twice to the same (nonmultiple) root instead of separately to two different roots.

Deflation, which amounts to synthetic division, is a simple operation that acts on the array of polynomial coefficients. The concise code for synthetic division by a monomial factor was given in $\ S 5 . 1$ . You can deflate complex roots either by converting that code to complex data type, or else — in the case of a polynomial with real coefficients but possibly complex roots — by deflating by a quadratic factor,

$$
\left[ x - ( a + i b ) \right] \left[ x - ( a - i b ) \right] = x ^ { 2 } - 2 a x + ( a ^ { 2 } + b ^ { 2 } )
$$

The routine poldiv in $\ S 5 . 1$ can be used to divide the polynomial by this factor.

Deflation must, however, be utilized with care. Because each new root is known with only finite accuracy, errors creep into the determination of the coefficients of the successively deflated polynomial. Consequently, the roots can become more and more inaccurate. It matters a lot whether the inaccuracy creeps in stably (plus or minus a few multiples of the machine precision at each stage) or unstably (erosion of successive significant figures until the results become meaningless). Which behavior occurs depends on just how the root is divided out. Forward deflation, where the new polynomial coefficients are computed in the order from the highest power of $x$ down to the constant term, was illustrated in $\ S 5 . 1$ . This turns out to be stable if the root of smallest absolute value is divided out at each stage. Alternatively, one can do backward deflation, where new coefficients are computed in order from the constant term up to the coefficient of the highest power of $x$ . This is stable if the remaining root of largest absolute value is divided out at each stage.

![](images/3fe6e40161b1978d2878f9ed5c462b33a41a255857fab87dda81deb7fcb84cd8.jpg)  
Figure 9.5.1. (a) Linear, quadratic, and cubic behavior at the roots of polynomials. Only under high magnification (b) does it become apparent that the cubic has one, not three, roots, and that the quadratic has two roots rather than none.

A polynomial whose coefficients are interchanged “end-to-end,” so that the constant becomes the highest coefficient, etc., has its roots mapped into their reciprocals. (Proof: Divide the whole polynomial by its highest power $x ^ { n }$ and rewrite it as a polynomial in $1 / x$ .) The algorithm for backward deflation is therefore virtually identical to that of forward deflation, except that the original coefficients are taken in reverse order and the reciprocal of the deflating root is used. Since we will use forward deflation below, we leave to you the exercise of writing a concise coding for backward deflation (as in $\ S 5 . 1 )$ . For more on the stability of deflation, consult [2].

To minimize the impact of increasing errors (even stable ones) when using deflation, it is advisable to treat roots of the successively deflated polynomials as only tentative roots of the original polynomial. One then polishes these tentative roots by taking them as initial guesses that are to be re-solved for, using the nondeflated original polynomial $P$ . Again you must beware lest two deflated roots are inaccurate enough that, under polishing, they both converge to the same undeflated root; in that case you gain a spurious root multiplicity and lose a distinct root. This is detectable, since you can compare each polished root for equality to previous ones from distinct tentative roots. When it happens, you are advised to deflate the polynomial just once (and for this root only), then again polish the tentative root, or use Maehly’s procedure (see equation 9.5.29 below).

Below we say more about techniques for polishing real and complex-conjugate tentative roots. First, let’s get back to overall strategy.

There are two schools of thought about how to proceed when faced with a polynomial of real coefficients. One school says to go after the easiest quarry, the real, distinct roots, by the same kinds of methods that we have discussed in previous sections for general functions, i.e., trial-and-error bracketing followed by a safe Newton-

Raphson as in rtsafe. Sometimes you are only interested in real roots, in which case the strategy is complete. Otherwise, you then go after quadratic factors of the form (9.5.1) by any of a variety of methods. One such is Bairstow’s method, which we will discuss below in the context of root polishing. Another is Muller’s method, which we here briefly discuss.

# 9.5.2 Muller's Method

Muller’s method generalizes the secant method but uses quadratic interpolation among three points instead of linear interpolation between two. Solving for the zeros of the quadratic allows the method to find complex pairs of roots. Given three previous guesses for the root $x _ { i - 2 }$ , $x _ { i - 1 }$ , $x _ { i }$ , and the values of the polynomial $P ( x )$ at those points, the next approximation $x _ { i + 1 }$ is produced by the following formulas,

$$
\begin{array} { l } { q \equiv \frac { x _ { i } - x _ { i - 1 } } { x _ { i - 1 } - x _ { i - 2 } } } \\ { A \equiv q P ( x _ { i } ) - q ( 1 + q ) P ( x _ { i - 1 } ) + q ^ { 2 } P ( x _ { i - 2 } ) } \\ { B \equiv ( 2 q + 1 ) P ( x _ { i } ) - ( 1 + q ) ^ { 2 } P ( x _ { i - 1 } ) + q ^ { 2 } P ( x _ { i - 2 } ) } \\ { C \equiv ( 1 + q ) P ( x _ { i } ) } \end{array}
$$

followed by

$$
x _ { i + 1 } = x _ { i } - ( x _ { i } - x _ { i - 1 } ) \frac { 2 C } { B \pm \sqrt { B ^ { 2 } - 4 A C } }
$$

where the sign in the denominator is chosen to make its absolute value or modulus as large as possible. You can start the iterations with any three values of $x$ that you like, e.g., three equally spaced values on the real axis. Note that you must allow for the possibility of a complex denominator, and subsequent complex arithmetic, in implementing the method.

Muller’s method is sometimes also used for finding complex zeros of analytic functions (not just polynomials) in the complex plane, for example in the IMSL routine ZANLY [3].

# 9.5.3 Laguerre's Method

The second school regarding overall strategy happens to be the one to which we belong. That school advises you to use one of a very small number of methods that will converge (though with greater or lesser efficiency) to all types of roots: real, complex, single, or multiple. Use such a method to get tentative values for all $n$ roots of your nth degree polynomial. Then go back and polish them as you desire.

Laguerre’s method is by far the most straightforward of these general, complex methods. It does require complex arithmetic, even while converging to real roots; however, for polynomials with all real roots, it is guaranteed to converge to a root from any starting point. For polynomials with some complex roots, little is theoretically proved about the method’s convergence. Much empirical experience, however, suggests that nonconvergence is extremely unusual and, further, can almost always be fixed by a simple scheme to break a nonconverging limit cycle. (This is implemented in our routine below.) An example of a polynomial that requires this cycle-breaking scheme is one of high degree $( \gtrsim 2 0 )$ , with all its roots just outside of


<!-- chunk 0008: pages 491-560 -->
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
