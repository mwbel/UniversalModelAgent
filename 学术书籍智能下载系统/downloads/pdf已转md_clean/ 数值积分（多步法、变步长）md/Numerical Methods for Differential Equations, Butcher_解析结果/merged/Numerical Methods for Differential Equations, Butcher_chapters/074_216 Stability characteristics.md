# 216 Stability characteristics

In addition to knowing that a numerical method converges to the true solution over a bounded interval, it is interesting to know how errors behave over an unbounded interval. Obtaining quantitative results is difficult, because we are no longer able to take limits, as stepsizes tend to zero. Hence, our attention will move towards qualitative questions, such as whether or not a computed result remains bounded. By comparing the answer to questions like this with the known behaviour of the exact solution, we obtain further insight into the appropriateness of the numerical approximation to model the differential equation.

A further reason for carrying out this type of qualitative analysis is that so-called ‘stiff problems’ frequently arise in practice. For such problems, qualitative or ‘stability’ analysis is vital in assessing the fitness of the method to be used in the numerical solution.

Because of the great complexity of this type of analysis, we need to restrict ourselves to purely linear problems with constant coefficients. Thus, we could consider a system of differential equations of the form

$$
y ^ { \prime } ( x ) = M y ( x ) ,
$$

with the matrix $M$ constant. Using fixed stepsize $h$ , the Euler method gives as the approximate solution at $x _ { n } = x _ { 0 } + n h$ ,

$$
y _ { n } = ( I + h M ) y _ { n - 1 } ,
$$

leading to the numerical solution

$$
y _ { n } = ( I + h M ) ^ { n } y _ { 0 } .
$$

For this problem, the exact solution is

$$
y ( x _ { n } ) = \exp ( n h M ) y ( x _ { 0 } ) .
$$

We wish to examine some features of the approximate solution (216b) by comparing these features with corresponding features of the exact solution (216c).

By making a change of basis, so that $y ( x ) = S { \widehat { y } } ( x )$ , and $y _ { n } = S { \widehat { y } } _ { n }$ , where $S$ is a constant non-singular matrix, we can rewrite the differential equation in the form

$$
{ \widehat { y } } ^ { \prime } ( x ) = { \widehat { M } } { \widehat { y } } ( x ) ,
$$

where $\widehat { M } = S ^ { - 1 } M S$ . The solution is

$$
\widehat { y } ( x _ { n } ) = \exp ( n h \widehat { M } ) \widehat { y } ( x _ { 0 } ) .
$$

The solution computed by the Euler method transforms to

$$
\widehat { y } _ { n } = ( I + h \widehat { M } ) ^ { n } \widehat { y } _ { 0 } .
$$

If the transformed matrix $\widehat { M }$ is chosen as the Jordan canonical form of $M$ , then the differential equation system (216d) and the numerical approximation become, to some extent, decoupled. This means that, for each distinct eigenvalue $q$ , one of the equations in the system (216d) has the simple form

$$
y ^ { \prime } ( x ) = q y ( x ) ,
$$

and other components that correspond to the same Jordan block will depend on this solution, but will not contribute to its behaviour.

Hence, to obtain acceptable behaviour, for the type of linear problem given by (216a), it is essential that we obtain acceptable behaviour for (216e). All this will mean is that $( 1 + h q ) ^ { n }$ will be an acceptable approximation to $\exp ( n h q )$ . At very least, we want bounded behaviour for $( 1 + h q ) ^ { n }$ , as $n \longrightarrow \infty$ , whenever $\exp ( n h q )$ is bounded. This, in turn, implies that $| 1 + h q |$ is bounded by $1$ , if $\mathrm { R e } q \le 0$ and $q$ is an eigenvalue of $M$ . Because any analysis of this type will involve the product of $h$ and $q$ , it is convenient to write this product as $z = h q$ . We allow the possibility that $z$ is complex, because there is no reason for $M$ to have only real eigenvalues.

The set of points in the complex plane, in which $z$ may lie for this stable behaviour, is known as the ‘stability region’. Because it is the set for which $| 1 + z | \le 1$ , this stability region is the disc with centre at $^ { - 1 }$ and radius $^ { 1 }$ . This is shown as the unshaded region in Figure 216(i). By contrast, we can find the stability region of the implicit Euler method by replacing $h f ( x _ { n } , y _ { n } )$ by $z y _ { n }$ in the formula defining this method. That is, $y _ { n } = y _ { n - 1 } + h f ( x _ { n } , y _ { n } )$ becomes

$$
y _ { n } = y _ { n - 1 } + z y _ { n } .
$$

Hence, $y _ { n } = ( 1 - z ) ^ { - 1 } y _ { n - 1 }$ , and the sequence formed by this relation is bounded if and only if $| 1 - z | \geq 1$ . This is the complement in the complex plane of the interior of the disc with centre $^ { 1 }$ and radius $^ { 1 }$ , shown as the unshaded region of Figure 216(ii).

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/30ca22b8a24076d1d50d7bddea3249bcb89b9fd057c8bc9588fbd88e8fe64493.jpg)  
Stability region: Euler method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/b3e2a7e70023ec0a4266136d2ddd9db811ab52159672f24cbc5486d6002edd61.jpg)  
Stability region: implicit Euler method

Even if we cannot obtain accurate approximations to the solution to equations like (216e), we frequently wish to guarantee that the numerical approximation is bounded in cases when the exact solution is bounded. This means that we are especially interested in numerical methods, for which the stability region includes all of the left half-plane. This is the case for the implicit Euler method (Figure 216(ii)) but, as we clearly see from Figure 216(i), not for the Euler method itself. Methods with this desirable property are said to be ‘A-stable’. It is widely accepted that this property is close to being essential for stiff problems.

For these two one-step methods, the ratio $y _ { n } / y _ { n - 1 }$ is known as the ‘stability function’. Denote this by $R ( z )$ so that

$$
R ( z ) = \left\{ \begin{array} { l l } { 1 + z , \qquad } & { \mathrm { ( E u l e r ~ m e t h o d ) } } \\ { \displaystyle \frac { 1 } { 1 - z } . \qquad } & { \mathrm { ( i m p l i c i t ~ E u l e r ~ m e t h o d ) } } \end{array} \right.
$$

From a consideration of elementary complex analysis, the property of Astability can be expressed slightly differently. Obviously, for a method to be A-stable, the stability function must have no poles in the left half-plane. Also the magnitude $| R ( z ) |$ must be bounded by $1$ , for $z$ on the imaginary axis.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/dd51a820ae8540723fe9dbc338733700eb600354cb7eea6d4c7ec804fb80a030.jpg)  
Order star: Euler method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/1ccb7d15bc1123a7c3b02ba693c9b1482024f4fcee7eaa627bc14e901a61282c.jpg)  
Order star: implicit Euler method

The interesting thing is that these two conditions are also sufficient for Astability. If a method with these properties were not A-stable, then this would be contrary to the maximum modulus principle.

Multiplying $R ( z )$ by $\exp ( - z )$ should make no difference to these conclusions. That is, if the set in the complex plane for which $| R ( z ) \exp ( - z ) | \leq 1$ is plotted instead, A-stability can still be categorized by this set, including the imaginary axis, together with there being no poles in the left half-plane. The reason for this assertion is that the factor $\exp ( - z )$ does not add to, or take away from, the set of poles. Furthermore, its magnitude is precisely 1 when the real part of $z$ is zero.

The modified plots for the two methods are shown in Figures 216(iii) and 216(iv). These were named ‘order stars’ by their inventors, Wanner, Hairer and Nørsett (1978). The important new feature, introduced by the insertion of the exponential factor, is the pattern that has appeared near zero. Because, for each of these methods, $R ( z ) \exp ( - z ) = 1 + C z ^ { 2 } + O ( z ^ { 3 } )$ , the magnitude of this will be greater than, equal to, or less than $^ { 1 }$ for $| z |$ small, approximately when the real part of $C z ^ { 2 }$ is positive, zero or negative, respectively. The regions adjoining zero for which $\mathrm { R e } ( R ( z ) \exp ( - z ) ) > 0$ are known as ‘fingers’, and those for which $\mathrm { R e } ( R ( z ) \exp ( - z ) ) < 0$ , are ‘dual fingers’. The bounded fingers necessarily contain poles and the bounded dual fingers necessarily contain zeros. For both the Euler method and the implicit Euler method, there is an exact pairing between zeros and bounded dual fingers, and between poles and bounded fingers. Since this pairing also generalizes to other large classes of methods, specifically those methods for which the order is maximal, given the degrees of the numerator and denominator in the stability function, it is possible to relate the angles, at which fingers come out from zero, to the positions of the poles. It will be shown in Subsection 354 how this can be used to determine the possible A-stability of specific methods, and classes of methods.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/62c1d0a3b94f88f68e17291e3390c6dbfd290e51f8fe959a34454802b5a36235.jpg)  
Order arrows: Euler method

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0002_pages_0071-0140/auto/images/8b5aa3e0a73b71ba05e95ebc19ea0e0d7283180d81aef66339f8db7a438e77a4.jpg)  
Order arrows: implicit Euler method

Although less well known, order arrows have a role similar to that of order stars, in the analysis of stability questions. For a given stability function $R ( z )$ , we plot the paths in the complex plane where $w ( z ) = \exp ( - z ) R ( z )$ is real and positive. Arrows are attached to the paths to show the direction of increasing $w$ . For the Euler and implicit Euler methods, order arrow diagrams are shown in Figures 216(v) and 216(vi) respectively.
