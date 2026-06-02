# 106 The Lotka–Volterra problem and periodic orbits

In the modelling of the two-species ‘predator–prey’ problem, differential equation systems of the following type arise:

$$
\begin{array} { r } { u ^ { \prime } = u ( 2 - v ) , } \\ { v ^ { \prime } = v ( u - 1 ) , } \end{array}
$$

where the factors $2 - v$ and $u - 1$ can be generalized in various ways. This model was proposed independently by Lotka (1925) and Volterra (1926). The two variables represent the time-dependent populations, of which $\boldsymbol { v }$ is the population of predators which feed on prey whose population is denoted by $u$ . It is assumed that $u$ would have been able to grow exponentially without limit, if the predator had not been present, and that the factor $2 - v$ represents the modification to its growth rate because of harvesting by the predator. The predator in turn, in the absence of prey, would die out exponentially, and requires at least a prey population of $u = 1$ to feed upon to be able to grow. Of the two stationary solutions, $( u , v ) = ( 0 , 0 )$ and $( u , v ) = ( 1 , 2 )$ , the second is more interesting because small perturbations from this point will lead to periodic orbits around the stationary point. By dividing (106a) by (106b), we obtain a differential equation for the path traced out by $( u , v )$ . The solution is that $I ( u , v )$ is constant, where

Approximations to the period $T$ , given by (106d) for $( u _ { 0 } , v _ { 0 } ) = ( 2 , 2 )$   

<table><tr><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>Approximate integral</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>4.62974838287860</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>4.61430252126987</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>4.61487057379480</td></tr><tr><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>4.61487051945097</td></tr><tr><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>4.61487051945103</td></tr><tr><td rowspan=1 colspan=1>320</td><td rowspan=1 colspan=1>4.61487051945103</td></tr></table>

$$
I ( u , v ) = \log ( u ) + 2 \log ( v ) - u - v .
$$

It is interesting to try to calculate values of the period $T$ , for a given starting point $( u _ { 0 } , v _ { 0 } )$ . To calculate $T$ , change to polar coordinates centred at the stationary point

$$
u = 1 + r \cos ( \theta ) , \qquad v = 2 + r \sin ( \theta )
$$

and calculate the integral $\int _ { 0 } ^ { 2 \pi } \phi ( \theta ) d \theta$ , where

$$
\phi ( \theta ) = \frac { 1 } { v \cos ^ { 2 } ( \theta ) + u \sin ^ { 2 } ( \theta ) } .
$$

Starting values $( u _ { 0 } , v _ { 0 } ) = ( 2 , 2 )$ lead to the orbit featured in Figure $1 0 6 ( \mathrm { i } )$ . Orbits with various other starting values are also shown. The period, based on the integral of (106c), has been calculated with a varying number $n$ of equally spaced values of $\theta \in [ 0 , 2 \pi ]$ , using the trapezoidal rule. It is known that for certain smooth functions, the error of this type of calculation will behave, not like a power of $n ^ { - 1 }$ , but like $\exp ( - \alpha n )$ , for some problem-specific parameter $\alpha$ . This super-convergence is evidently realized for the present problem, where the observed approximations

$$
T = \int _ { 0 } ^ { 2 \pi } \phi ( \theta ) d \theta \approx { \frac { 2 \pi } { n } } \sum _ { k = 0 } ^ { n - 1 } \phi \left( { \frac { 2 \pi k } { n } } \right)
$$

are shown in Table 106(I) for $n = 1 0 , 2 0 , 4 0 , \ldots , 3 2 0$ . Evidently, to full machine accuracy, the approximations have converged to T = 4.61487051945103. An

α Computation of orbit and period for the Lotka–Volterra problem   

<table><tr><td>theta = linspace(O,2*pi,n+1);</td></tr><tr><td>co = cos(theta);</td></tr><tr><td>si = sin(theta);</td></tr><tr><td>C = u0*v0 2*exp(-u0-v0);</td></tr><tr><td>r = ones(size(theta));</td></tr><tr><td>u = 1+r.*co;</td></tr><tr><td>v = 2+r.*si;</td></tr><tr><td>carryon=1;</td></tr><tr><td>while carryon</td></tr><tr><td>f = u.*v. 2-C*exp(u+v);</td></tr><tr><td>df = -v.*r.*(v.*co. 2+u.*si. 2);</td></tr><tr><td>dr = f./df;</td></tr><tr><td>r = r-dr;</td></tr><tr><td>u = 1+r.*co;</td></tr><tr><td>V = 2+r.*si; carryon = norm(dr,inf）&gt; O.0ooooo001;</td></tr><tr><td>end</td></tr><tr><td>phi = 1./(v.*co.2+u.*si.2);</td></tr><tr><td></td></tr><tr><td>period = (2*pi/n)*sum(phi(1:n));</td></tr></table>

explanation of the phenomenon of rapid convergence of the trapezoidal rule for periodic functions can be found in Davis and Rabinowitz (1984), and in papers referenced in that book.

In Algorithm $1 0 6 \alpha$ , MATLAB statements are presented to carry out the computations that were used to generate Figure 106(i) and Table 106(I). To compute the value of $r$ for each $\theta$ , the equation $f ( r ) = 0$ is solved, where

$$
f ( r ) = ( \exp ( I ( u , v ) ) - C ) \exp ( u + v ) = u v ^ { 2 } - C \exp ( u + v ) ,
$$

with $C = u _ { 0 } v _ { 0 } ^ { 2 } \exp ( - u _ { 0 } - v _ { 0 } )$ . Note that the statement $\boldsymbol { \mathrm { ~ u ~ . ~ v ~ } }$ . $2 \mathrm { - C * e x p \left( u + v \right) }$ evaluates a vector with element number $i$ equal to $u _ { i } v _ { i } ^ { 2 } - C \exp ( u _ { i } + v _ { i } )$ , and that linspace(0,2\*pi,n+1) generates a vector with $n + 1$ components, equally spaced in $[ 0 , 2 \pi ]$ .
