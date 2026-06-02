# 354 Order stars

We have identified some members of the Pad´e table for the exponential function for which the corresponding numerical methods are A-stable. We now ask: are there other members of the table with this property? It will be seen that everything hinges on the value of $m - l$ , the degree of the denominator minus the degree of the numerator. It is clear that if $m - l < 0$ , A-stability is impossible, because in this case

$$
| R ( z ) | \to \infty ,
$$

as $z  \infty$ , and hence, for some $z$ satisfying $\mathrm { R e } z < 0$ , $| R ( z ) |$ is greater than $^ { 1 }$ . For $m - l \in \{ 0 , 1 , 2 \}$ , A-stability follows from Theorem 353A. Special cases with $m - l > 2$ suggest that these members of the Pad´e table are not A-stable. For the third sub-diagonal, this was proved by Ehle (1969), and for the fourth and fifth sub-diagonals by Nørsett (1974). Based on these observations, Ehle (1973) conjectured that no case with $m - l > 2$ can be A-stable. This result was eventually proved by Wanner, Hairer and Nørsett (1978), and we devote this subsection to introducing the approximations considered in that paper and to proving the Ehle conjecture.

In Subsection 216, we touched on the idea of an order star. Associated with the stability function $R ( z )$ for a Runge–Kutta method, we consider the set of points in the complex plane such that

$$
| \exp ( - z ) R ( z ) | > 1 .
$$

This is known as the ‘order star’ of the method, and the set of points such that

$$
| \exp ( - z ) R ( z ) | < 1
$$

is the ‘dual order star’. The common boundary of these two sets traces out an interesting path, as we see illustrated in Figure 354(i), for the case of the $( 1 , 3 )$ Pad´e approximation given by

$$
R ( z ) = { \frac { 1 + { \frac { 1 } { 4 } } z } { 1 - { \frac { 3 } { 4 } } z + { \frac { 1 } { 4 } } z ^ { 2 } - { \frac { 1 } { 2 4 } } z ^ { 3 } } } .
$$

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/245bb3fc37091066fe93197cfed019393d414bf7d740ed1ff3e9f33fd1156ad7.jpg)  
Order star for the $( 1 , 3 )$ Pad´e approximation to exp

In this diagram, the dual order star, which can also be described as the ‘relative stability region’, is the interior of the unshaded region. The order star is the interior of the shaded region.

In Butcher (1987) an attempt was made to present an informal survey of order stars leading to a proof of the Ehle result. In the present volume, the discussion of order stars will be even more brief, but will serve as an introduction to an alternative approach to achieve similar results. In addition to Wanner, Hairer and Nørsett (1978), the reader is referred to Iserles and Nørsett (1991) for fuller information and applications of order stars.

The ‘order star’, for a particular rational approximation to the exponential function, disconnects into ‘fingers’ emanating from the origin, which may be bounded or not, and similar remarks apply to ‘dual fingers’ which are the connected components of the dual star. The following statements summarize the key properties of order stars for applications of the type we are considering. Because we are including only hints of the proofs, we refer to them as remarks rather than as lemmas or theorems. Note that $S$ denotes the order star for a specific ‘method’ and $I$ denotes the imaginary axis.

Remark 354A A method is $A$ -stable if and only if $S$ has no poles in the negative half-plane and $S \cup I = \emptyset$ , because the inclusion of the exponential factor does not alter the set of poles and does not change the magnitude of the stability function on $I$ .

Remark 354B There exists $\rho _ { 0 } ~ > ~ 0$ such that, for all $\rho ~ \geq ~ \rho _ { 0 }$ , functions $\theta _ { 1 } ( \rho )$ and $\theta _ { 2 } ( \rho )$ exist such that the intersection of $S$ with the circle $| z | = \rho$ is the set $\{ \rho \exp ( i \theta ) : \theta _ { 1 } < \theta < \theta _ { 2 } \}$ and where $\begin{array} { l } { \operatorname* { l i m } _ { \rho \to \infty } \theta _ { 1 } ( \rho ) ~ = ~ \pi / 2 } \end{array}$ and $\operatorname* { l i m } _ { \rho \to \infty } \theta _ { 2 } ( \rho ) = 3 \pi / 2$ , because at a great distance from the origin, the behaviour of the exponential function multiplied by the rational function on which the order star is based is dominated by the exponential factor.

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0004_pages_0211-0280/auto/images/478ddae7b9c90a9cb8002184e20f54a267f735bc8144ad38f973845d858b99b8.jpg)  
Relation between order arrows and order stars

Remark 354C For a method of order $p$ , the arcs $\{ r \exp ( i ( j + \frac { 1 } { 2 } ) \pi / ( p + 1 ) ) :$ $0 \leq r \}$ , where $j = 0 , 1 , \ldots , 2 p + 1$ , are tangential to the boundary of $S$ at 0, because $\exp ( - z ) R ( z ) = 1 + C z ^ { p + 1 } + O \big ( | z | ^ { p + 2 } \big )$ , so that $| \exp ( - z ) R ( z ) | =$ $1 + \mathrm { R e } ( C z ^ { p + 1 } ) + O ( | z | ^ { p + 2 } )$ .

It is possible that $m$ bounded fingers can join together to make up a finger of multiplicity $m$ . Similarly, $m$ dual fingers in $\overline { S }$ can combine to form a dual finger with multiplicity $m$ .

Remark 354D Each bounded finger of $S$ , with multiplicity $_ { m }$ , contains at least m poles, counted with their multiplicities, because, by the Cauchy– Riemann conditions, the argument of $\exp ( - z ) R ( z )$ increases monotonically as the boundary of the order star is traced out in a counter-clockwise direction.

In the following subsection, we introduce a slightly different tool for studying stability questions. The basic idea is to use, rather than the fingers and dual fingers as in order star theory, the lines of steepest ascent and descent from the origin. Since these lines correspond to values for which $R ( z ) \exp ( - z )$ is real and positive, we are, in reality, looking at the set of points in the complex plane where this is the case.

We illustrate this by presenting, in Figure 354(ii), a modified version of Figure 354(i), in which the boundary of the order star is shown as a dashed line and the ‘order arrows’, as we call them, are shown with arrow heads showing the direction of ascent.
