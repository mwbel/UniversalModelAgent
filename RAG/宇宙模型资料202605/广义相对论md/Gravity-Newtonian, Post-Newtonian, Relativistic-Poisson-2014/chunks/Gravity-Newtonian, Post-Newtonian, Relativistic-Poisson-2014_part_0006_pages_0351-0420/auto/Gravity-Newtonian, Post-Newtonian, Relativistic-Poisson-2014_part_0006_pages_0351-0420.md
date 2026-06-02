$\tau ^ { \alpha \beta }$ encountered below will always be decomposed in the elementary forms displayed in Eq. (7.19); the complete $h _ { \mathcal { W } } ^ { \alpha \beta }$ can then be obtained by summing over these elementary contributions.

Little more can be said about the general structure of $h _ { \mathcal { W } } ^ { \alpha \beta }$ in the near zone. The sources $f ^ { \alpha \beta }$ vanish in the first iteration of the relaxed field equations, because we are instructed to set $h ^ { \alpha \beta } = 0$ in $\tau ^ { \alpha \beta }$ and the material source is confined to the near zone. In the second and higher iterations, $h ^ { \alpha \beta }$ is no longer zero, and $\tau ^ { \alpha \beta }$ now extends into the wave zone; in these cases we have no choice but to plow through the detailed calculations to see what contribution $h _ { \mathcal { W } } ^ { \alpha \beta }$ might make. We encounter some of these calculations later in this chapter, and then again in Chapter 11.

<table><tr><td>Box 7.1</td><td>Radiation-reaction terms in the potentials To illustrate how the various radiation-reaction terms arise in the potentials, we examine the contribution</td></tr><tr><td></td><td>1 a τ(t,x)(r²-2x.x&#x27;+r&#x27;2)dx&#x27; 6c3 dt t;thisisthethdi.3)tfstotutsi gral, giving -}c-2r²d² S dot0d3x&#x27; = }c-2r²ə² Su δjτoi d3x&#x27;, which becomes a sur- face term,reflecting the fact that energy is conserved apart from a tiny flux of gravitational radiation. In the second term, x can be brought outside the integral, giving }c-2xjd² S doto0x&#x27;i d3x&#x27; = }c-2xiə² S.nt0id3x&#x27;plusasurfaceterm.Thisyields-}c-1xia Suktki dx&#x27;,whichgives</td></tr></table>

The next term in $h _ { \mathcal { N } } ^ { 0 0 }$ involving an odd number of time derivatives is

$$
\begin{array} { c } { { \displaystyle - \frac { 1 } { 1 2 0 c ^ { 5 } } \bigg ( \frac \partial { \partial t } \bigg ) ^ { 5 } \int _ { \mathcal { M } } \tau ^ { 0 0 } ( t , x ^ { \prime } ) \Big [ \mathrm { \small ~ \displaystyle } r ^ { 4 } - 4 r ^ { 2 } x \cdot x ^ { \prime } + 4 ( x \cdot x ^ { \prime } ) ^ { 2 } + 2 r ^ { 2 } r ^ { \prime 2 } } } \\ { { - 4 r ^ { \prime 2 } x \cdot x ^ { \prime } + r ^ { \prime 4 } \Big ] d ^ { 3 } x ^ { \prime } . } } \end{array}
$$

The first two terms can be shown to become surface integrals by appealing to the conservation identities of Eqs. (7.14), and the remaining four terms are displayed in Eq. (7.15a). Similar manipulations, albeit becoming progressively more complicated, yield the corresponding terms displayed in Eqs. (7.15) for $h _ { \mathcal { N } } ^ { 0 j }$ and $h _ { \mathcal { N } } ^ { j k }$ .

# 7.1.3 Near-zone metric

We will need to construct the spacetime metric $g _ { \alpha \beta }$ from the gravitational potentials $h ^ { \alpha \beta }$ . The link is provided by the gothic inverse metric ${ \mathfrak { g } } ^ { \alpha \beta } = \eta ^ { \alpha \beta } - h ^ { \alpha \beta }$ , which is related to the inverse metric $g ^ { \alpha \beta }$ by ${ \mathfrak { g } } ^ { \alpha \beta } = { \sqrt { - g } } g ^ { \alpha \beta }$ g. The inverse relation is $g _ { \alpha \beta } = \sqrt { - \mathfrak { g } } \mathfrak { g } _ { \alpha \beta }$ , in which ${ \mathfrak { g } } _ { \alpha \beta }$ gis the matrix inverse to ${ \mathfrak { g } } ^ { \alpha \beta }$ , and $\mathfrak { g } : = \operatorname* { d e t } [ \mathfrak { g } ^ { \alpha \beta } ]$ . Given that $h ^ { \alpha \beta }$ g gis of order $G$ , we can g g g gsolve these equations and obtain the metric and its inverse as post-Minkowskian expansions in powers of $G$ , and express the results in terms of the potentials $h ^ { \alpha \beta }$ . We find

$$
\begin{array} { l } { { g _ { \alpha \beta } = \eta _ { \alpha \beta } + h _ { \alpha \beta } - \frac { 1 } { 2 } h \eta _ { \alpha \beta } + h _ { \alpha \beta } h _ { \beta } ^ { \mu } - \frac { 1 } { 2 } h h _ { \alpha \beta } } } \\ { { \ \qquad + \left( \frac { 1 } { 8 } h ^ { 2 } - \frac { 1 } { 4 } h ^ { \mu \nu } h _ { \mu \nu } \right) \eta _ { \alpha \beta } + { \cal O } ( G ^ { 3 } ) , } } \\ { { g ^ { \alpha \beta } = \eta ^ { \alpha \beta } - h ^ { \alpha \beta } + \frac { 1 } { 2 } h ^ { \eta \sigma \beta } - \frac { 1 } { 2 } h h ^ { \alpha \beta } } } \\ { { \ \qquad + \left( \frac { 1 } { 8 } h ^ { 2 } + \frac { 1 } { 4 } h ^ { \mu \nu } h _ { \mu \nu } \right) \eta ^ { \alpha \beta } + { \cal O } ( G ^ { 3 } ) , } } \\ { { \ \displaystyle ( - g ) = 1 - h + \frac { 1 } { 2 } h ^ { 2 } - \frac { 1 } { 2 } h ^ { \mu \nu } h _ { \mu \nu } + { \cal O } ( G ^ { 3 } ) , } } \\ { { \ \displaystyle \sqrt { - g } = 1 - \frac { 1 } { 2 } h + \frac { 1 } { 8 } h ^ { 2 } - \frac { 1 } { 4 } h ^ { \mu \nu } h _ { \mu \nu } + { \cal O } ( G ^ { 3 } ) . } } \end{array}
$$

It is understood that here, indices on $h ^ { \alpha \beta }$ are lowered with the Minkowski metric, so that $h _ { \alpha \beta } : = \eta _ { \alpha \mu } \eta _ { \beta \nu } h ^ { \mu \nu }$ and $h : = \eta _ { \mu \nu } h ^ { \mu \nu }$ .

In practice, the construction of the metric from the potentials depends on the context, which dictates the degree of accuracy required of each metric component. Suppose that we are specifically interested in determining the geodesic motion of a slowly-moving particle in the near zone of a weakly-curved spacetime. As we saw back in Sec. 5.2.3, the motion is governed by a Lagrangian $L$ given by

$$
\begin{array} { l } { { { \cal { L } } = - m c \sqrt { - g _ { \alpha \beta } \displaystyle \frac { d r ^ { \alpha } } { d t } \displaystyle \frac { d r ^ { \beta } } { d t } } } } \\ { { { \mathrm { } = - m c ^ { 2 } \sqrt { - g _ { 0 0 } - 2 g _ { 0 j } v ^ { j } / c - g _ { j k } v ^ { j } v ^ { k } / c ^ { 2 } } , } } } \end{array}
$$

where $r ^ { \alpha } = ( c t , r )$ describes the particle’s position in spacetime, and $v ^ { j } = d r ^ { j } / d t$ is its three-dimensional velocity vector. Newtonian gravity is reproduced by inserting the approximations $g _ { 0 0 } = - 1 + 2 U / c ^ { 2 } + O ( c ^ { - 4 } ) , g _ { 0 j } = O ( c ^ { - 3 } )$ , and $g _ { j k } = \delta _ { j k } + O ( c ^ { - 2 } )$ within the Lagrangian, and expanding the square root to order $c ^ { - 2 }$ ; this yields

$$
{ \cal L } = - m c ^ { 2 } + \frac { 1 } { 2 } m v ^ { 2 } + m U + { \cal O } ( c ^ { - 2 } ) ,
$$

in which $U$ is the Newtonian potential. The first term is an irrelevant constant, and we indeed recognize ${ \frac { 1 } { 2 } } m v ^ { 2 } + m U$ as the Lagrangian of Newtonian gravity; the remaining terms of order $c ^ { - 2 }$ are 1pn corrections. This simple exercise teaches us that a contribution of order $c ^ { - 2 }$ to $g _ { 0 0 }$ is a Newtonian term, but that a term of order $c ^ { - 2 }$ in $g _ { j k }$ is actually a post-Newtonian correction.

If we now want the post-Newtonian corrections to the motion, we must evaluate the Lagrangian to order $c ^ { - 2 }$ , and this requires calculation of the metric to the following orders of approximation:

$$
\begin{array} { r c l } { { { \cal O } ( c ^ { - 4 } ) } } & { { \mathrm { f o r } } } & { { g _ { 0 0 } , } } \\ { { { \cal O } ( c ^ { - 3 } ) } } & { { \mathrm { f o r } } } & { { g _ { 0 j } , } } \\ { { { \cal O } ( c ^ { - 2 } ) } } & { { \mathrm { f o r } } } & { { g _ { j k } . } } \end{array}
$$

In this case, a term of order $c ^ { - 4 }$ in $g _ { 0 0 }$ gives rise to a post-Newtonian correction to the Lagrangian. The same is true of a term of order $c ^ { - 3 }$ in $g _ { 0 j }$ , because it multiplies $v ^ { j } / c$ in the Lagrangian, making the combination a term of order $c ^ { - 4 }$ . And the same is also true of a term of order $c ^ { - 2 }$ in $g _ { j k }$ , because it multiplies $v ^ { j } v ^ { k } / c ^ { 2 }$ in the Lagrangian. Generalizing the argument, we find that determination of the motion to npn order requires calculation of the metric to the orders

$$
\begin{array} { r c l } { { { \cal O } ( c ^ { - 2 n - 2 } ) } } & { { \mathrm { f o r } } } & { { g _ { 0 0 } , } } \\ { { } } & { { } } & { { } } \\ { { { \cal O } ( c ^ { - 2 n - 1 } ) } } & { { \mathrm { f o r } } } & { { g _ { 0 j } , } } \\ { { } } & { { } } & { { } } \\ { { { \cal O } ( c ^ { - 2 n } ) } } & { { \mathrm { f o r } } } & { { g _ { j k } ; } } \end{array}
$$

as usual the orders in $c ^ { - 1 }$ descend because of the additional factors of $v ^ { j } / c$ in the Lagrangian.

Suppose next that we wish to determine the motion of a test body to $2 . 5 \mathrm { { p N } }$ order. The previous discussion indicates that we need $g _ { 0 0 }$ to order $c ^ { - 7 } , g _ { 0 j }$ to order $c ^ { - 6 }$ , and $g _ { j k }$ to order $c ^ { - 5 }$ . The metric is obtained from the potentials $h ^ { \alpha \beta }$ , and recalling from Eqs. (7.15) that $h ^ { 0 0 }$ leads off at order $c ^ { - 2 } , h ^ { 0 j }$ at order $c ^ { - 3 }$ , and $h ^ { j k }$ at order $c ^ { - 4 }$ , we find from Eq. (7.20) that the appropriate expression is

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac 1 2 { h ^ { 0 0 } } - \frac 3 8 \bigl ( h ^ { 0 0 } \bigr ) ^ { 2 } + \frac 5 { 1 6 } \bigl ( h ^ { 0 0 } \bigr ) ^ { 3 } + \displaystyle \frac 1 2 { h ^ { k k } } \biggl ( 1 - \frac 1 2 h ^ { 0 0 } \biggr ) + \frac 1 2 h ^ { 0 j } h ^ { 0 j } } } \\ { { \qquad + O ( c ^ { - 8 } ) , } } \\ { { g _ { 0 j } = - h ^ { 0 j } \biggl ( 1 - \frac 1 2 h ^ { 0 0 } \biggr ) + O ( c ^ { - 7 } ) , } } \\ { { g _ { j k } = \delta _ { j k } \left[ 1 + \displaystyle \frac 1 2 h ^ { 0 0 } - \frac 1 8 \bigl ( h ^ { 0 0 } \bigr ) ^ { 2 } \right] + h ^ { j k } - \displaystyle \frac 1 2 \delta _ { j k } h ^ { m m } + O ( c ^ { - 6 } ) , } } \\ { { \qquad \quad ( - g ) = 1 + h ^ { 0 0 } - h ^ { k k } + O ( c ^ { - 6 } ) . } } \end{array}
$$

To arrive at these results we actually had to carry the expansion of Eq. (7.20) to the third order in $G$ , in order to capture the $( h ^ { 0 0 } ) ^ { 3 }$ term in $g _ { 0 0 }$ ; this term is of order $c ^ { - 6 }$ , and it is required for a complete expansion accurate through $2 . 5 \mathrm { { p N } }$ order.

Examining Eqs. (7.23), we begin to see how different orders in the post-Newtonian expansion of $h ^ { \alpha \beta }$ contribute to the metric. Beginning with $g _ { 0 0 }$ , we see from Eq. (7.15) that $h ^ { 0 0 }$ contributes at all orders, from Newtonian order $( c ^ { - 2 } )$ through $2 . 5 \mathrm { { p N } }$ order $( c ^ { - 7 } )$ , that $h ^ { 0 j }$ contributes at 2pn order $( c ^ { - 6 } )$ only, and that $h ^ { j k }$ contributes at all orders beyond the Newtonian order $( c ^ { - 4 } , c ^ { - 5 } , c ^ { - 6 }$ , and $c ^ { - 7 }$ ). With $g _ { 0 j }$ we find that $h ^ { 0 0 }$ contributes at 2pn order $( c ^ { - 5 } )$ only, while $h ^ { 0 j }$ contributes at 1pn, 2pn, and $2 . 5 \mathrm { { p N } }$ orders $( c ^ { - 3 } , c ^ { - 5 }$ , and $c ^ { - 6 }$ ). And finally, with $g _ { j k }$ we see that $h ^ { 0 0 }$ contributes at 1pn, 2pn, and $2 . 5 \mathrm { { p N } }$ orders $( c ^ { - 2 } , c ^ { - 4 }$ , and $c ^ { - 5 }$ ), while $h ^ { j k }$ contributes at $2 \mathrm { P N }$ and $2 . 5 \mathrm { { p N } }$ orders $( c ^ { - 4 }$ and $c ^ { - 5 }$ ).

We observe that each power of $c ^ { - 2 }$ assigned to a contribution to $g _ { \alpha \beta }$ translates to a specific post-Newtonian order. The translation, however, depends on the context. When the metric is examined in isolation, a term of order $c ^ { - 2 }$ in $g _ { j k }$ could be declared to be of the same post-Newtonian order as a term of order $c ^ { - 2 }$ in $g _ { 0 0 }$ . But when the metric is examined in the context of determining the motion of a slowly-moving particle, the $c ^ { - 2 }$ term in $g _ { j k }$ is appropriately declared to be a 1pn term, while the $c ^ { - 2 }$ term in $g _ { 0 0 }$ is labeled as a Newtonian contribution. The translation is again different when the motion is highly relativistic, with velocities $v ^ { j }$ approaching the speed of light. In this case the coupling of the metric with powers of $v ^ { j } / c \simeq 1$ does not alter the post-Newtonian order, and a $c ^ { - 2 }$ term in $g _ { j k }$ would again be declared to be a Newtonian contribution. Context is everything, and it must be specified before a meaningful post-Newtonian order can be assigned to a given expression.

Our considerations in this chapter, and the three chapters that follow, will be limited to post-Newtonian gravity, in which corrections of $2 \mathrm { P N }$ order and higher are neglected. In this 1pn context our expansion for the metric can be truncated to

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 1 } { 2 } h ^ { 0 0 } - \displaystyle \frac { 3 } { 8 } \big ( h ^ { 0 0 } \big ) ^ { 2 } + \displaystyle \frac { 1 } { 2 } h ^ { k k } + { \cal O } ( c ^ { - 6 } ) , } } \\ { { g _ { 0 j } = - h ^ { 0 j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { g _ { j k } = \delta _ { j ^ { k } } \left( 1 + \displaystyle \frac { 1 } { 2 } h ^ { 0 0 } \right) + { \cal O } ( c ^ { - 4 } ) , } } \\ { { ( - g ) = 1 + h ^ { 0 0 } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

We return to the higher-order corrections in Chapter 12, when we study the effects of gravitational reaction in the near zone. There we shall be interested in all $2 . 5 \mathrm { { p N } }$ terms in the metric, those that scale as $c ^ { - 7 }$ in $g _ { 0 0 }$ , as $c ^ { - 6 }$ in $g _ { 0 j }$ , and as $c ^ { - 5 }$ in $g _ { j k }$ . We shall see that with suitable care, we can study these radiative effects independently of the 1pn or $2 \mathrm { P N }$ influences.

# 7.1.4 General structure of the potentials: Wave zone

We proceed with an examination of the general structure of the gravitational potentials when the field point $\boldsymbol { x }$ is in the wave zone, where $r : = | { \mathbf { } } x | > \mathcal { R }$ . Consulting $\operatorname { B o x } 6 . 7$ once more, we see that we can express $h _ { \mathcal { N } } ^ { \alpha \beta }$ as the multipole expansion

$$
h _ { \mathcal { N } } ^ { \alpha \beta } ( t , x ) = \frac { 4 G } { c ^ { 4 } } \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \partial _ { L } \bigg [ \frac { 1 } { r } \int _ { \mathcal { M } } \tau ^ { \alpha \beta } ( \tau , x ^ { \prime } ) x ^ { \prime L } d ^ { 3 } x ^ { \prime } \bigg ] ,
$$

in which $\tau : = t - r / c$ is retarded time.

We first consider $h _ { \mathcal { N } } ^ { 0 0 }$ , and observe that the integral in Eq. (7.25) is just $c ^ { 2 } T ^ { L } ( \tau )$ as defined by Eqs. (7.16); the multipole moments are now evaluated at retarded time $\tau$ instead of time $t$ . The first term ( $\ell = 0$ ) in the series involves the monopole moment

$$
M _ { 0 } : = \mathcal { I } ( \tau ) = \int _ { \mathcal { M } } c ^ { - 2 } \tau ^ { 0 0 } ( \tau , x ) d ^ { 3 } x \ ,
$$

and this represents the total mass contained within the near zone. Because of the conservation equations, we know that its time derivative can be converted to a surface integral on $\partial \mathcal { M }$ , which can be shown to be small; the near-zone mass $M _ { 0 }$ is therefore constant to a large degree of accuracy. The second term in the series involves

$$
M _ { 0 } R _ { 0 } ^ { j } : = \mathcal { T } ^ { j } ( \tau ) = \int _ { \mathcal { M } } c ^ { - 2 } \tau ^ { 0 0 } ( \tau , { \pmb x } ) x ^ { j } d ^ { 3 } x ,
$$

where $R _ { 0 } ^ { j }$ is the center-of-mass position associated with the domain $\mathcal { M }$ . Its rate of change is related to the near-zone momentum

$$
P _ { 0 } ^ { j } : = \int _ { \mathcal { M } } c ^ { - 1 } \tau ^ { 0 j } ( \tau , x ) d ^ { 3 } x
$$

by the conservation statement

$$
{ \frac { d } { d \tau } } \big ( M _ { 0 } R _ { 0 } ^ { j } \big ) = P _ { 0 } ^ { j } + \mathrm { s u r f a c e i n t e g r a l } ,
$$

and the momentum itself can be shown to satisfy

$$
\frac { d P _ { 0 } ^ { j } } { d \tau } = 0 + \mathrm { s u r f a c e ~ i n t e g r a l } .
$$

Because in each case the surface integral can be shown to be small, the total momentum is conserved to a large degree of accuracy, and the center-of-mass moves according to $d ( M _ { 0 } R _ { 0 } ^ { j } ) / d \tau = P _ { 0 } ^ { j } .$ . We may set $P _ { 0 } ^ { j } = 0$ by working in the rest frame of the system, and set $R _ { 0 } ^ { j } = 0$ by placing the center-of-mass at the spatial origin of the harmonic coordinates; the conservation equations ensure that $R _ { 0 } ^ { j }$ remains zero up to very small effects associated with the radiation of linear momentum. Thus, $h _ { \mathcal { N } } ^ { 0 0 }$ consists of a static monopole piece plus timedependent terms involving the quadrupole moment $\mathcal { T } ^ { j k } ( \tau )$ and higher multipole moments.

Turning to $h _ { \mathcal { N } } ^ { 0 j }$ , and making use of the conservation identities of Eqs. (7.14a) and (7.14c), we can show that the $\ell = 0$ contribution to $h _ { \mathcal { N } } ^ { 0 j }$ is of the form $( 4 G / c ^ { 3 } ) r ^ { - 1 } \dot { \mathcal { T } } ^ { j }$ modulo surface terms; but since $\dot { \mathcal { T } } ^ { j } = P _ { 0 } ^ { j } +$ surface integral, we find that this vanishes by virtue of our choice of reference frame. The $\ell = 1$ contribution involves $\int _ { \mathcal { M } } \tau ^ { 0 j } x ^ { k } d ^ { 3 } x$ , which according to Eq. (7.14c) can be converted to $\frac { 1 } { 2 } ( \dot { \mathcal { T } } ^ { j k } - \epsilon ^ { m j k } J _ { 0 } ^ { m } )$ , where

$$
J _ { 0 } ^ { m } : = \epsilon _ { m j k } \int _ { \mathcal { M } } x ^ { j } c ^ { - 1 } \tau ^ { 0 k } ( \tau , { \pmb x } ) d ^ { 3 } x
$$

is the angular momentum contained within the near zone. The conservation identities can again be used to show that $d J _ { 0 } ^ { m } / d \tau$ vanishes up to a surface integral, so that $J _ { 0 }$ is constant except for a small radiative loss of angular momentum. Finally, looking at the $\ell = 0$ term in $h _ { \mathcal { N } } ^ { j k }$ and using the identity of Eq. (7.14b), we find that we may convert it to $( 2 G / c ^ { 4 } ) r ^ { - 1 } \ddot { \mathcal { Z } } ^ { j k }$ modulo surface terms.

With these simplifications we obtain our final expression for $h _ { \mathcal { N } } ^ { \alpha \beta }$ in the wave zone:

$$
\begin{array} { l } { { \displaystyle h _ { \mathcal { N } } ^ { 0 0 } = \frac { 4 G M _ { 0 } } { c ^ { 2 } r } + \frac { 4 G } { c ^ { 2 } } \displaystyle \sum _ { \ell = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \partial _ { L } \bigg [ \frac { Z ^ { L } ( \tau ) } { r } \bigg ] , } } \\ { { \displaystyle h _ { \mathcal { N } } ^ { 0 j } = - \frac { 2 G } { c ^ { 3 } } \frac { ( n \times J _ { 0 } ) ^ { j } } { r ^ { 2 } } - \frac { 2 G } { c ^ { 3 } } \partial _ { k } \bigg [ \frac { \dot { Z } ^ { j k } ( \tau ) } { r } \bigg ] } } \\ { { \displaystyle ~ + \frac { 4 G } { c ^ { 4 } } \displaystyle \sum _ { \ell = 2 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \partial _ { L } \bigg [ \frac { 1 } { r } \int _ { \mathcal { M } } \tau ^ { 0 j } ( \tau , x ^ { \prime } ) x ^ { \prime L } d ^ { 3 } x ^ { \prime } \bigg ] , } } \\ { { \displaystyle h _ { \mathcal { N } } ^ { j k } = \frac { 2 G } { c ^ { 4 } } \frac { \ddot { Z } ^ { j k } ( \tau ) } { r } + \frac { 4 G } { c ^ { 4 } } \displaystyle \sum _ { \ell = 1 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \partial _ { L } \bigg [ \frac { 1 } { r } \int _ { \mathcal { M } } \tau ^ { j k } ( \tau , x ^ { \prime } ) x ^ { \prime L } d ^ { 3 } x ^ { \prime } \bigg ] , } } \end{array}
$$

in which overdots indicate differentiation with respect to $\tau = t - r / c$ .

Still according to $\operatorname { B o x } 6 . 7$ , we see that the wave-zone contribution $h _ { \mathcal { W } } ^ { \alpha \beta }$ to the gravitational potentials is given by

$$
h _ { \mathcal { W } } ^ { \alpha \beta } ( t , x ) = \frac { 4 G } { c ^ { 4 } } \frac { n ^ { \langle L \rangle } } { r } \left\{ \int _ { 0 } ^ { \mathcal { R } } d s f ^ { \alpha \beta } ( \tau - 2 s / c ) A ( s , r ) + \int _ { \mathcal { R } } ^ { \infty } d s f ^ { \alpha \beta } ( \tau - 2 s / c ) B ( s , r ) \right\} ,
$$

when $\tau ^ { \alpha \beta }$ can be put in the specific form displayed in Eq. (7.19); the functions $A ( s , r )$ and $B ( s , r )$ are defined by Eq. (6.104). We shall learn how to evaluate these contributions below in Sec. 7.4, and then again in Chapter 11.

# Box 7.2

# Multipole structure of the wave-zone metric

By using extensions of the conservation identities (7.14), the wave-zone forms of the potentials $h _ { \mathcal { N } } ^ { \alpha \beta }$ can be expressed elegantly in terms of a sequence of multipole moments. The general expressions are

$$
h _ { \mathcal { N } } ^ { \alpha \beta } = \frac { 4 G } { c ^ { 4 } } \sum _ { \ell = 0 } ^ { \infty } \frac { ( - 1 ) ^ { \ell } } { \ell ! } \partial _ { L } \left[ \frac { 1 } { r } \mathcal { M } ^ { \alpha \beta L } ( \tau ) \right] ,
$$

where

$$
\begin{array} { l } { { { \cal M } ^ { \mathrm { o L } } = - 2 \tilde { \cal Z } ^ { L } , } } \\ { { { \cal M } ^ { \mathrm { o L } } = { \frac { c } { 2 ( \ell + 1 ) } } \left( \tilde { \cal Z } ^ { L \ell } - \bar { \epsilon } ^ { \mathrm { e } \epsilon \theta \theta \theta } \mathcal { M } ^ { \mathrm { o L } \nu } \right) \left( \mathrm { s y m } a : L \right) } } \\ { { \ } } \\ { { \ + \ \displaystyle \frac { 1 } { \left( \bar { \ell } + 1 \right) } \oint _ { \mathrm { s } , \epsilon } \mathrm { w } _ { x } \mathcal { M } ^ { \mathrm { o L } } d S _ { x } , } } \\ { { { \cal M } ^ { \mathrm { p L } } = \displaystyle \frac { 1 } { \left( \bar { \ell } + 1 \right) \left( \bar { \ell } + 2 \right) } \tilde { \bar { \ell } } ^ { \mathrm { i n } } + \displaystyle \frac { 2 } { \left( \bar { \ell } + 2 \right) } \int _ { \mathrm { s } } ^ { \mathrm { e } \mathrm { m } \{ \bar { \ell } \} \bar { \omega } ^ { L } - \mathrm { s } \mathrm { e } \left( \mathrm { s y m } a : L \right) } } } \\ { { \ + \ \displaystyle \frac { 8 ( \bar { \ell } - 1 ) } { \left( \bar { \ell } + 1 \right) } p \bar { \ell } ^ { \mathrm { i n } } \mathrm { ~ s y s } , } } \\ { { \ ~ + \ \displaystyle \frac { 1 } { \left( \bar { \ell } + 1 \right) } \sum _ { \bar { \epsilon } \ \mathrm { o } \mathrm { f } } \left[ \mathrm { r } ^ { \mathrm { e } \cdot \mathrm { s } } \omega _ { x } \mathcal { M } ^ { \mathrm { o L } \bar { \nu } } \right] + \partial _ { x } \epsilon ^ { \mathrm { i n } } x _ { x } \mathrm { i n } \Big ] d S _ { x } , } } \\ { { \ ~ - \ \displaystyle \frac { 2 } { \left( \bar { \ell } + 2 \right) } \oint _ { \mathrm { s } , \epsilon } \left[ \mathrm { r } ^ { \mathrm { i n } } \omega _ { x } \mathcal { M } ^ { \mathrm { o L } \bar { \nu } } \cdots \mathrm { ~ } \left( \bar { \ell } + \bar { \kappa } \right) \right] d S _ { x } \mathrm { ( s y m } a : L ) , } } \end{array}
$$

where $\mathcal { T } ^ { L }$ and $\mathcal { I } ^ { j L }$ are defined in Eqs. (7.16), and

$$
\mathcal { P } ^ { j k a b L } : = \int _ { \mathcal { M } } x ^ { [ a } \tau ^ { j ] [ k } x ^ { b ] L } d ^ { 3 } x .
$$

The notation $( \operatorname { s y m } a : L$ ) means symmetrize on all $\ell a$ -indices.

# 7.1.5 Toward two iterations of the field equations

As we pointed out back in Sec. 6.2.3, to achieve the second post-Minkowskian approximation to the gravitational potentials $h ^ { \alpha \beta }$ , we must carry out two iterations of the relaxed field equations and then impose the gauge condition/conservation statement. In other words, we must solve the wave equation $\Theta h ^ { \alpha \beta } = - ( 1 6 \pi G / c ^ { 4 } ) \tau _ { 1 } ^ { \alpha \beta }$ for the potentials $h _ { 2 } ^ { \alpha \beta }$ and then impose the gauge condition $\partial _ { \beta } h _ { 2 } ^ { \alpha \beta } = 0$ or the conservation equation $\partial _ { \beta } \tau _ { 1 } ^ { \alpha \beta } = \bar { 0 }$ . The starting point of these computations is construction of the effective energy-momentum pseudotensor $\tau _ { 1 } ^ { \alpha \beta }$ , which depends on the fluid’s energy-momentum tensor $T ^ { \alpha \beta }$ and the potentials generated during the first iteration of the relaxed field equations. Our very first task, therefore, is to perform the first iteration and obtain $\tau _ { 1 } ^ { \alpha \beta }$ .

# 7.2 First iteration

In this section we complete the first iteration of the relaxed field equations to obtain the gravitational potentials $h _ { 1 } ^ { \alpha \beta }$ . Our goal is to perform the computation to a degree of accuracy that is sufficient for the preparation of the second iteration, to be carried out in Secs. 7.3 and 7.4.

# 7.2.1 Energy-momentum tensor

In the first iteration of the field equations we replace $g _ { \alpha \beta }$ by $\eta _ { \alpha \beta }$ in the energy-momentum tensor of Eq. (7.1), and in the normalization condition for the velocity four-vector. Similarly, we set $\sqrt { - g } = 1$ in Eq. (7.4). We find that $\begin{array} { r } { \gamma = ( 1 - v ^ { 2 } / c ^ { 2 } ) ^ { - 1 / 2 } = 1 + \frac { 1 } { 2 } ( v / c ) ^ { 2 } + O ( c ^ { - 4 } ) } \end{array}$ , and Eq. (7.4) becomes

$$
\rho = \biggl [ 1 - \frac { 1 } { 2 } ( v / c ) ^ { 2 } + { \cal O } ( c ^ { - 4 } ) \biggr ] \rho ^ { * } .
$$

The components of the energy-momentum tensor are then

$$
\begin{array} { l } { { \displaystyle c ^ { - 2 } T _ { 0 } ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + \Pi \biggr ) + O ( c ^ { - 4 } ) \biggr ] , } } \\ { { \displaystyle c ^ { - 1 } T _ { 0 } ^ { 0 j } = \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + \Pi + p / \rho ^ { * } \biggr ) + O ( c ^ { - 4 } ) \biggr ] , } } \\ { { \displaystyle T _ { 0 } ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + O ( c ^ { - 2 } ) . } } \end{array}
$$

They are written as post-Newtonian expansions in flat spacetime, and these include both Newtonian and post-Newtonian contributions; terms occurring at $2 \mathrm { P N }$ order are neglected. Because they do not yet include 1pn terms involving the gravitational potentials, which will appear during the second iteration of the field equations, these post-Newtonian expansions are incomplete.

# 7.2.2 Near zone

We first take the field point $\boldsymbol { x }$ to be in the near zone, so that $r < \mathcal { R }$ . To achieve the first iteration of the relaxed field equations, we set $\tau ^ { \alpha \beta } = T _ { 0 } ^ { \alpha \beta }$ and make the substitution within Eqs. (7.13). Because the energy-momentum tensor is confined to the near zone, there is no need to truncate the integrals to the near-zone domain $\mathcal { M }$ ; they are naturally truncated to the volume occupied by the matter distribution. And because $T _ { 0 } ^ { \alpha \beta }$ does not extend to the wave zone, the potentials $h _ { \mathcal { W } } ^ { \alpha \beta }$ vanish, and $h ^ { \alpha \beta } = h _ { \mathcal { N } } ^ { \alpha \beta }$ .

As we shall see below in Sec. 7.3, for the purposes of preparing the second iteration of the field equations it is sufficient to compute $h _ { 1 } ^ { 0 0 }$ to order $c ^ { - 2 }$ , $h _ { 1 } ^ { 0 j }$ to order $c ^ { - 3 }$ , and to neglect $h _ { 1 } ^ { j k }$ because it is of order $c ^ { - 4 }$ . This requirement implies that we can truncate Eqs. (7.35) to

$$
\begin{array} { c } { { c ^ { - 2 } T _ { 0 } ^ { 0 0 } = \rho ^ { * } + { \cal O } ( c ^ { - 2 } ) , } } \\ { { { } } } \\ { { c ^ { - 1 } T _ { 0 } ^ { 0 j } = \rho ^ { * } v ^ { j } + { \cal O } ( c ^ { - 2 } ) , } } \\ { { { } } } \\ { { T ^ { j k } = { \cal O } ( 1 ) . } } \end{array}
$$

Making the substitution within Eq. (7.13) reveals that the potentials are given by

$$
\begin{array} { l } { { \displaystyle h _ { 1 } ^ { 0 0 } = \frac { 4 } { c ^ { 2 } } U + O ( c ^ { - 4 } ) , } } \\ { { \displaystyle h _ { 1 } ^ { 0 j } = \frac { 4 } { c ^ { 3 } } U ^ { j } + O ( c ^ { - 4 } ) , } } \\ { { \displaystyle h _ { 1 } ^ { j k } = O ( c ^ { - 4 } ) , } } \end{array}
$$

in which $U$ is a Newtonian potential defined by

$$
U ( t , { \pmb x } ) = G \int \frac { \rho ^ { * } ( t , { \pmb x } ^ { \prime } ) } { | { \pmb x } - { \pmb x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , \qquad \nabla ^ { 2 } U = - 4 \pi G \rho ^ { * } ,
$$

in terms of the rescaled mass density $\rho ^ { * }$ , and $U ^ { j }$ is a vector potential defined by

$$
U ^ { j } ( t , x ) = G \int \frac { \rho ^ { * } v ^ { j } ( t , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , \qquad \nabla ^ { 2 } U ^ { j } = - 4 \pi G \rho ^ { * } v ^ { j } ,
$$

in terms of the mass-current density $\rho ^ { * } v ^ { j }$ . It is useful to note that by virtue of the continuity equation (7.3), the potentials satisfy

$$
\partial _ { t } U + \partial _ { j } U ^ { j } = 0
$$

as a matter of identity.

Note that in Eq. (7.37), the corrections to $h _ { 1 } ^ { 0 0 }$ first occur at order $c ^ { - 4 }$ . The expansion of Eq. (7.13), however, contains a term at order $c ^ { - 3 }$ proportional to

$$
\frac { d } { d t } \int \rho ^ { * } d ^ { 3 } x .
$$

This vanishes because $\begin{array} { r } { m : = \int \rho ^ { * } d ^ { 3 } x } \end{array}$ , the total rest-mass within the fluid is conserved by virtue of Eq. (7.3). As was pointed out back in Sec. 7.1.1, the conservation of rest-mass is a basic kinematical requirement, quite divorced from any dynamical requirement based on energy-momentum conservation. This is an important point, because we recall that we are not at liberty to impose the conservation equations $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ during the first iteration of the relaxed field equations; for this we must await the second iteration. With this in mind, you will notice that the corrections to $h _ { 1 } ^ { 0 j }$ first occur at order $c ^ { - 4 }$ ; this represents a term proportional to

$$
\frac { d } { d t } \int \rho ^ { * } v ^ { j } d ^ { 3 } x
$$

in the expansion of Eq. (7.13). The integral is the total momentum at Newtonian order, and it is tempting to declare that this term should vanish by virtue of momentum conservation. This temptation, however, must be resisted during the first iteration.

The gravitational potentials may be inserted within Eqs. (7.24) to obtain the near-zone metric. We obtain

$$
\begin{array} { l } { { g _ { 0 0 } ^ { 1 } = - 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle g _ { 0 j } ^ { 1 } = - \displaystyle \frac { 4 } { c ^ { 3 } } U ^ { j } + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle g _ { j k } ^ { 1 } = \Big ( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U \Big ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

and the metric determinant is $( - g _ { 1 } ) = 1 + 4 U / c ^ { 2 } + O ( c ^ { - 4 } )$ . Recalling our discussion in Sec. 7.1.3, we see that this metric is not sufficiently accurate to obtain the motion of a test particle at post-Newtonian order, because it lacks the $O ( c ^ { - 4 } )$ contributions to $g _ { 0 0 }$ . It is sufficiently accurate, however, to serve as input in the second iteration of the relaxed field equations.

# 7.2.3 Wave zone

We next take the field point $\boldsymbol { x }$ to be in the wave zone, so that $r > \mathcal { R }$ . To achieve the first iteration of the relaxed field equations, we could in principle set $\tau ^ { \alpha \beta } = T _ { 0 } ^ { \alpha \beta }$ , make the substitution within Eqs. (7.25), and evaluate the multipole moments explicitly. There is, however, no immediate need to proceed in this way. We can instead keep things simple by making direct use of Eqs. (7.25) and keeping the multipole moments unevaluated until we have completed the second iteration. An aspect of $\tau ^ { \alpha \beta }$ that we can incorporate is that it does not extend beyond the near zone; this implies that $h _ { \mathcal { W } } ^ { \alpha \beta }$ vanishes, so that $h ^ { \alpha \beta } = h _ { \mathcal { N } } ^ { \alpha \beta }$ .

As we shall see below in Sec. 7.4, only $h _ { 1 } ^ { 0 0 }$ is required in the preparation of the second iteration. It is given by

$$
h _ { 1 } ^ { 0 0 } = \frac { 4 G } { c ^ { 2 } } \left\{ \frac { { \mathcal { T } } ( \tau ) } { r } - \partial _ { j } \bigg [ \frac { { \mathcal { T } } ^ { j } ( \tau ) } { r } \bigg ] + \frac { 1 } { 2 } \partial _ { j k } \bigg [ \frac { { \mathcal { T } } ^ { j k } ( \tau ) } { r } \bigg ] + \cdot \cdot \cdot \right\} ,
$$

in which $\begin{array} { r } { \mathcal { T } ^ { L } ( \tau ) : = \int _ { \mathcal { M } } c ^ { - 2 } \tau ^ { 0 0 } ( \tau , \pmb { x } ) x ^ { L } d ^ { 3 } \pmb { x } } \end{array}$ are the multipole moments of the density $c ^ { - 2 } \tau ^ { 0 0 }$ , expressed as functions of retarded time $\tau = t - r / c$ . Note that we keep the dipole-moment term in the expansion, in spite of the fact that $\mathcal { T } ^ { j }$ will eventually be set equal to zero by a coordinate choice, as we indicated back in Sec. 7.1.4. The reason is that the ability to set $\mathcal { T } ^ { j } = 0$ relies on the conservation equation $\partial _ { \beta } \tau ^ { \alpha \beta } = 0$ , which we are not at liberty to impose during the first iteration.

Counting post-Newtonian orders is more subtle in the wave zone than it is in the near zone. The monopole term on the right-hand side of Eq. (7.42) is evidently of order $G m _ { c } / ( c ^ { 2 } r )$ , and we naturally assign a $0 \mathrm { P N }$ order to this term. To see about the dipole term, we perform the differentiation and express it as

$$
- \frac { 4 G } { c ^ { 2 } } \partial _ { j } \biggl [ \frac { { \mathcal T } ^ { j } ( \tau ) } { r } \biggr ] = \frac { 4 G } { c ^ { 2 } } \biggl ( \frac { \dot { \mathcal { Z } } ^ { j } } { c r } + \frac { { \mathcal T } ^ { j } } { r ^ { 2 } } \biggr ) n _ { j } ,
$$

in which $n ^ { j } : = x ^ { j } / r$ . Noting that $\mathcal { T } ^ { j }$ scales as $m _ { c } r _ { c }$ , this term is of order

$$
{ \frac { G } { c ^ { 2 } } } m _ { c } r _ { c } \biggl ( { \frac { 1 } { c t _ { c } r } } + { \frac { 1 } { r ^ { 2 } } } \biggr ) = { \frac { G m _ { c } } { c ^ { 2 } r } } { \frac { r _ { c } } { c t _ { c } } } \biggl ( 1 + { \frac { c t _ { c } } { r } } \biggr ) .
$$

This is smaller than $G m _ { c } / ( c ^ { 2 } r )$ by a factor of order $( v _ { c } / c ) ( 1 + \lambda _ { c } / r )$ . The second factor is of order unity in the wave zone, and we conclude that the dipole term is smaller than the monopole term by a factor of order $v _ { c } / c$ . To this term we therefore assign a $0 . 5 \mathrm { { P N } }$ order. We do this in spite of the fact that the second term on the right of Eq. (7.43) is formally of Newtonian order. In the near zone, but outside the distribution of matter, this term would give the standard dipole contribution to the Newtonian potential, which normally would be set equal to zero by a suitable choice of coordinates. But because it falls off as $r ^ { - 2 }$ and we are looking in the wave zone at distances $r > \lambda _ { c } = r _ { c } ( c / v _ { c } ) .$ , it has decreased in size to such an extent that it is now comparable to (or even smaller than) the $0 . 5 \mathrm { { P N } }$ term produced by the time derivative of $\mathcal { T } ^ { j }$ .

A simple extension of this argument reveals that the quadrupole term in $h _ { 1 } ^ { 0 0 }$ must be assigned a 1pn order. The octupole term, which would occur next in Eq. (7.42), gives a contribution at $1 . 5 \mathrm { P N }$ order, and the post-Newtonian counting becomes clear: an $\ell$ -pole term contributes at $( \ell / 2 ) \mathbf { p } \mathbf { N }$ order to the gravitational potential.

# 7.3 Second iteration: Near zone

In this section we face the challenging task of completing the second iteration of the relaxed field equations. Here we take the field point $_ x$ to be in the near zone, so that $r < \mathcal { R }$ . The wave zone will be considered next, in Sec. 7.4.

# 7.3.1 Effective energy momentum pseudotensor

Our first order of business is to use the potentials obtained in the first iteration to construct the effective energy-momentum pseudotensor of Eq. (6.52),

$$
\tau ^ { \alpha \beta } = ( - g ) \big ( T ^ { \alpha \beta } + t _ { \mathrm { L L } } ^ { \alpha \beta } + t _ { \mathrm { H } } ^ { \alpha \beta } \big ) ,
$$

with the Landau–Lifshitz contribution defined by Eq. (6.5), and the harmonic contribution defined by Eq. (6.53).

We begin by updating our expression for $T ^ { \alpha \beta }$ , the fluid’s energy-momentum tensor, which was given an incomplete post-Newtonian expansion back in Eq. (7.35). We return to Eq. (7.1) and substitute the near-zone metric displayed in Eq. (7.41). We also involve

this metric in the normalization condition for $u ^ { \alpha }$ , and update our expression for $\gamma$ to $1 +$ $\scriptstyle { \frac { 1 } { 2 } } ( v / c ) ^ { 2 } + U / c ^ { 2 } + O ( c ^ { - 4 } )$ , which now incorporates the Newtonian potential $U$ . Equation (7.34) becomes

$$
\rho = \bigg [ 1 - \frac { 1 } { c ^ { 2 } } \bigg ( \frac { 1 } { 2 } v ^ { 2 } + 3 U \bigg ) + O ( c ^ { - 4 } ) \bigg ] \rho ^ { * } ,
$$

and the components of the energy-momentum tensor are now

$$
\begin{array} { l } { { \displaystyle c ^ { - 2 } ( - g ) T _ { 1 } ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi \biggr ) + { \cal O } ( c ^ { - 4 } ) \biggr ] , } } \\ { { \displaystyle c ^ { - 1 } ( - g ) T _ { 1 } ^ { 0 j } = \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi + p / \rho ^ { * } \biggr ) + { \cal O } ( c ^ { - 4 } ) \biggr ] , } } \\ { { \displaystyle ( - g ) T _ { 1 } ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + { \cal O } ( c ^ { - 2 } ) . } } \end{array}
$$

We have multiplied $T _ { 1 } ^ { \alpha \beta }$ by $( - g )$ because this is the combination that appears in $\tau ^ { \alpha \beta }$ .

The hardest piece of the calculation by far (and this is always true) is the computation of $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ to the appropriate degree of accuracy. To match the accuracy achieved in Eqs. (7.47) we need $c ^ { - 2 } ( - g ) t _ { \mathrm { L L } } ^ { 0 0 }$ to orders $O ( 1 )$ and $O ( c ^ { - 2 } ) , c ^ { - 1 } ( - g ) t _ { \mathrm { L L } } ^ { 0 j }$ to order $O ( 1 )$ and $O ( c ^ { - 2 } )$ , and $( - g ) t _ { \mathrm { L L } } ^ { j k }$ to order $O ( 1 )$ . To pluck out of Eq. (6.5) the terms of relevant orders, we use the facts recorded in Eq. (7.9), that the potentials scale as $h ^ { 0 0 } = O ( c ^ { - 2 } )$ , $h ^ { 0 j } = O ( c ^ { - 3 } )$ , and $h ^ { j k } = O ( c ^ { - 4 } )$ . In addition, we use the property that $\partial _ { 0 } h ^ { 0 0 }$ is of order $c ^ { - 1 }$ relative to $\partial _ { j } h ^ { 0 0 }$ . The dominant piece of $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ will therefore come from $\partial _ { j } h ^ { 0 0 } = 4 \partial _ { j } U / c ^ { 2 }$ .

Armed with these observations, the reduction of $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ to something manageable is well within reach. Let us, for example, examine the term

$$
\frac { 1 } { 4 } \big ( 2 g ^ { \alpha \lambda } g ^ { \beta \mu } - g ^ { \alpha \beta } g ^ { \lambda \mu } \big ) g _ { \nu \rho } g _ { \sigma \tau } \partial _ { \lambda } h ^ { \nu \tau } \partial _ { \mu } h ^ { \rho \sigma }
$$

on the right-hand side of Eq. (6.5), in which we have replaced ${ \mathfrak { g } } ^ { \alpha \beta }$ by $\eta ^ { \alpha \beta } - h ^ { \alpha \beta }$ . A first gsource of simplification arises from the fact that each occurrence of $g _ { \alpha \beta }$ can be replaced by $\eta _ { \alpha \beta }$ ; this comes about because each factor of $h ^ { \alpha \beta }$ contributes a power of $G$ , and we need to compute $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ to order $G ^ { 2 }$ in the second post-Minkowskian approximation. A second source of simplification comes from the fact that at leading order, we can retain terms that involve $\partial _ { j } h ^ { 0 0 }$ only. At this stage the previous expression becomes

$$
\frac { 1 } { 4 } \big ( 2 \eta ^ { \alpha j } \eta ^ { \beta k } - \eta ^ { \alpha \beta } \delta ^ { j k } \big ) \partial _ { j } h ^ { 0 0 } \partial _ { k } h ^ { 0 0 } ,
$$

and it gives rise to a contribution $\textstyle { \frac { 1 } { 4 } } \partial _ { j } h ^ { 0 0 } \partial ^ { j } h ^ { 0 0 }$ to $( - g ) t _ { \mathrm { L L } } ^ { 0 0 }$ , and a contribution $\frac { 1 } { 2 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h ^ { 0 0 } -$ ${ \frac { 1 } { 4 } } \delta ^ { j k } \partial _ { n } h ^ { 0 0 } \partial ^ { n } h ^ { 0 0 }$ to $( - g ) t _ { \mathrm { L L } } ^ { j k }$ ; there is no contribution to $( - g ) t _ { \mathrm { L L } } ^ { 0 j }$ .

Keeping track of all terms that make up $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$ , we eventually arrive at the expressions

$$
\begin{array} { r l } & { \displaystyle \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) t _ { \mathrm { L L } } ^ { 0 0 } = - \frac { 7 } { 8 } \partial _ { j } h ^ { 0 0 } \partial ^ { j } h ^ { 0 0 } + O ( c ^ { - 6 } ) , } \\ & { \displaystyle \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) t _ { \mathrm { L L } } ^ { 0 j } = \frac { 3 } { 4 } \partial ^ { j } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 0 } + \left( \partial ^ { j } h ^ { 0 k } - \partial ^ { k } h ^ { 0 j } \right) \partial _ { k } h ^ { 0 0 } + O ( c ^ { - 7 } ) , } \\ & { \displaystyle \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) t _ { \mathrm { L L } } ^ { j k } = \frac { 1 } { 4 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h ^ { 0 0 } - \frac { 1 } { 8 } \delta ^ { j k } \partial _ { n } h ^ { 0 0 } \partial ^ { n } h ^ { 0 0 } + O ( c ^ { - 6 } ) . } \end{array}
$$

These results are sufficiently accurate for our immediate purposes. At a later stage, however, we shall need additional accuracy in our expression for $( - g ) t _ { \mathrm { L L } } ^ { j k }$ , and we record this improved expression here:

$$
\begin{array} { l } { { \displaystyle \frac { 1 6 \pi G } { c ^ { 4 } } ( - g ) \mathcal { I } _ { \mathrm { L L } } ^ { j k } = \frac { 1 } { 4 } \big ( 1 - 2 h ^ { ( 0 ) } \big ) \partial ^ { j } h ^ { ( 0 ) } \partial ^ { k } h ^ { 0 0 } - \frac { 1 } { 8 } \delta ^ { j k } \big ( 1 - 2 h ^ { ( 0 ) } \big ) \partial _ { n } h ^ { 0 0 } \partial ^ { n } h ^ { 0 0 } } }  \\ { { \displaystyle \qquad - \partial ^ { j } h ^ { 0 n } \partial ^ { k } h _ { n } ^ { 0 } + \partial ^ { j } h ^ { 0 n } \partial _ { n } h ^ { 0 k } + \partial ^ { k } h ^ { 0 n } \partial _ { n } h ^ { 0 j } - \partial _ { n } h ^ { 0 j } \partial ^ { n } h ^ { 0 k } } } \\ { { \displaystyle \qquad + \partial ^ { j } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 k } + \partial ^ { k } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 j } + \frac { 1 } { 4 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h _ { n } ^ { n } + \frac { 1 } { 4 } \partial ^ { k } h ^ { 0 0 } \partial ^ { j } h _ { n } ^ { n } } }  \\ { { \displaystyle \qquad + \delta ^ { j k } \bigg [ - \frac { 3 } { 8 } \big ( \partial _ { 0 } h ^ { 0 0 } \big ) ^ { 2 } - \partial _ { n } h ^ { 0 0 } \partial _ { 0 } h ^ { 0 n } - \frac { 1 } { 4 } \partial _ { n } h ^ { 0 0 } \partial ^ { n } h _ { p } ^ { p } } } \\ { { \displaystyle \qquad + \frac { 1 } { 2 } \partial _ { n } h _ { ~ p } ^ { 0 } \big ( \partial ^ { n } h ^ { 0 p } - \partial ^ { p } h ^ { 0 n } \big ) \bigg ] + { \cal O } ( c ^ { - 8 } ) . } } \end{array}
$$

It should be noted that this incorporates corrections of order $c ^ { - 2 }$ relative to the leading-order expression of Eq. (7.48), and that to be consistent, we have terms such as $h ^ { 0 0 } \partial ^ { j } h ^ { 0 0 } \partial ^ { k } h ^ { 0 0 }$ that contain an additional power of the gravitational constant $G$ .

With the substitutions of Eqs. (7.37), the Landau–Lifshitz pseudotensor becomes

$$
\begin{array} { r l } & { c ^ { - 2 } ( - g ) t _ { \mathrm { L L } } ^ { 0 0 } = - \displaystyle \frac { 1 } { 4 \pi G c ^ { 2 } } \bigg ( \frac { 7 } { 2 } \partial _ { j } U \partial ^ { j } U \bigg ) + { \cal O } ( c ^ { - 4 } ) , } \\ & { c ^ { - 1 } ( - g ) t _ { \mathrm { L L } } ^ { 0 j } = \displaystyle \frac { 1 } { 4 \pi G c ^ { 2 } } \bigg [ 3 \partial _ { t } U \partial ^ { j } U + 4 \big ( \partial ^ { j } U ^ { k } - \partial ^ { k } U ^ { j } \big ) \partial _ { k } U \bigg ] + { \cal O } ( c ^ { - 4 } ) , } \\ & { ( - g ) t _ { \mathrm { L L } } ^ { j k } = \displaystyle \frac { 1 } { 4 \pi G } \bigg ( \partial ^ { j } U \partial ^ { k } U - \frac { 1 } { 2 } \delta ^ { j k } \partial _ { n } U \partial ^ { n } U \bigg ) + { \cal O } ( c ^ { - 2 } ) . } \end{array}
$$

To better understand the importance of these contributions to $\tau ^ { \alpha \beta }$ , we estimate the order of magnitude of $c ^ { - 2 } ( - g ) t _ { \mathrm { L L } } ^ { 0 0 }$ relative to $\rho ^ { * }$ , the dominant contribution to $c ^ { - 2 } \tau ^ { 0 0 }$ . We reintroduce the scaling quantities $m _ { c } , r _ { c }$ , and $v _ { c }$ , and estimate the pseudotensor within the matter distribution. We have that $\rho ^ { * } \sim m _ { c } / r _ { c } ^ { 3 }$ and $U \sim G m _ { c } / r _ { c }$ . After differentiation we get $\partial _ { j } U \sim G m _ { c } / r _ { c } ^ { 2 }$ , and all this produces

$$
\frac { ( - g ) t _ { \mathrm { L L } } ^ { 0 0 } } { \rho ^ { * } c ^ { 2 } } \sim \frac { G m _ { c } } { c ^ { 2 } r _ { c } } .
$$

Since motion within the fluid is governed by gravity, we can rely on the virial theorem and claim that $G m _ { c } / r _ { c } \sim v _ { c } ^ { 2 }$ . The end result is that $c ^ { - 2 } ( - g ) t _ { \mathrm { L L } } ^ { 0 0 }$ is a quantity of order $( v _ { c } / c ) ^ { 2 }$ relative to $\rho ^ { * }$ ; it is comparable to the other 1pn terms that are displayed in Eq. (7.47).

The easiest piece of the calculation by far (and this is always true) is the computation of $( - g ) t _ { \mathrm { H } } ^ { \alpha \beta }$ to the required degree of accuracy. Using the information gathered previously, Eq. (6.53) returns

$$
\begin{array} { r l r } & { } & { { \frac { 1 6 \pi G } { c ^ { 4 } } } ( - g ) t _ { \mathrm { H } } ^ { 0 0 } = { \cal O } ( c ^ { - 6 } ) , } \\ & { } & { { \frac { 1 6 \pi G } { c ^ { 4 } } } ( - g ) t _ { \mathrm { H } } ^ { 0 j } = { \cal O } ( c ^ { - 7 } ) , } \\ & { } & { { \frac { 1 6 \pi G } { c ^ { 4 } } } ( - g ) t _ { \mathrm { H } } ^ { j k } = { \cal O } ( c ^ { - 6 } ) . } \end{array}
$$

These expressions should be compared with Eqs. (7.48); they imply that the harmonic pseudotensor makes no relevant contribution to $\tau ^ { \alpha \beta }$ . For later reference we record the improved expression

$$
{ \frac { 1 6 \pi G } { c ^ { 4 } } } ( - g ) t _ { \mathrm { H } } ^ { j k } = - h ^ { 0 0 } \partial _ { 0 0 } h ^ { j k } + { \cal O } ( c ^ { - 8 } )
$$

for the spatial components of the pseudotensor.

Collecting results, we have obtained

$$
\begin{array} { l } { { \displaystyle c ^ { - 2 } \tau _ { 1 } ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi \biggr ) \biggr ] - \frac { 1 } { 4 \pi G c ^ { 2 } } \biggl ( \frac { 7 } { 2 } \partial _ { j } U \partial ^ { j } U \biggr ) + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle c ^ { - 1 } \tau _ { 1 } ^ { 0 j } = \rho ^ { * } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } + 3 U + \Pi + p / \rho ^ { * } \biggr ) \biggr ] } } \\ { { \displaystyle ~ + \frac { 1 } { 4 \pi G c ^ { 2 } } \biggl [ 3 \partial _ { t } U \partial ^ { j } U + 4 \bigl ( \partial ^ { j } U ^ { k } - \partial ^ { k } U ^ { j } \bigr ) \partial _ { k } U \biggr ] + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle ~ \tau _ { 1 } ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + \frac { 1 } { 4 \pi G } \biggl ( \partial ^ { j } U \partial ^ { k } U - \frac { 1 } { 2 } \delta ^ { j k } \partial _ { n } U \partial ^ { n } U \biggr ) + { \cal O } ( c ^ { - 2 } ) , } } \end{array}
$$

for the effective energy-momentum pseudotensor.

# 7.3.2 Energy-momentum conservation

At this stage of our development of the second post-Minkowskian approximation, we may impose the conservation equations

$$
c ^ { - 2 } \partial _ { t } \tau _ { 1 } ^ { 0 0 } + c ^ { - 1 } \partial _ { j } \tau _ { 1 } ^ { 0 j } = 0 , \qquad c ^ { - 1 } \partial _ { t } \tau _ { 1 } ^ { 0 j } + \partial _ { k } \tau _ { 1 } ^ { j k } = 0 ,
$$

before calculating the second-iterated potentials $h _ { 2 } ^ { \alpha \beta }$ . At leading order the energy equation reproduces Eq. (7.3); not surprisingly, a statement of rest-mass conservation is included in the statement of energy conservation. The equation brings additional information at order $c ^ { - 2 }$ , a statement of energy conservation for all relevant forms of fluid energy: kinetic, internal, and gravitational. We shall return to this theme below.

The momentum equation is equally informative. Using Eqs. (7.54), we have

$$
\begin{array} { l } { { c ^ { - 1 } \partial _ { t } \tau _ { 1 } ^ { 0 j } = ( \partial _ { t } \rho ^ { * } ) v ^ { j } + \rho ^ { * } \partial _ { t } v ^ { j } + O ( c ^ { - 2 } ) } } \\ { { \displaystyle \vphantom { \frac { 1 } { \partial } } } } \\ { { \displaystyle \vphantom { \frac { 1 } { \partial } } = - v ^ { j } \partial _ { k } ( \rho ^ { * } v ^ { k } ) + \rho ^ { * } \frac { d v ^ { j } } { d t } - \rho ^ { * } v ^ { k } \partial _ { k } v ^ { j } + O ( c ^ { - 2 } ) , } } \end{array}
$$

where we have involved Eq. (7.3) and the definition of the total time derivative: $d v ^ { j } / d t =$ $\partial _ { t } v ^ { j } + v ^ { k } \partial _ { k } v ^ { j }$ . We also have

$$
\partial _ { k } \tau _ { 1 } ^ { j k } = v ^ { j } \partial _ { k } ( \rho ^ { * } v ^ { k } ) + \rho ^ { * } v ^ { k } \partial _ { k } v ^ { j } + \partial ^ { j } p + \frac { 1 } { 4 \pi G } ( \partial ^ { j } U ) \nabla ^ { 2 } U + O ( c ^ { - 2 } ) .
$$

Making the substitutions into Eq. (7.55), and replacing $\nabla ^ { 2 } U$ by $- 4 \pi G \rho ^ { * }$ , we arrive at

$$
\rho ^ { * } \frac { d v ^ { j } } { d t } = \rho ^ { * } \partial ^ { j } U - \partial ^ { j } p + { \cal O } ( c ^ { - 2 } ) .
$$

This is Euler’s equation, which governs the dynamics of our perfect fluid at leading order in a post-Newtonian expansion. It was first obtained on the basis of Newtonian theory in

Chapter 1, and indeed, the foregoing computations have already been presented (in reverse order) in Sec. 1.4.4.

Recalling our discussion of the iteration procedure in Sec. 6.2.3, we observe that Euler’s equation (i.e. Newtonian gravity) is the consequence of $\partial _ { \beta } \tau _ { 1 } ^ { \alpha \beta } = 0$ , the conservation equation that goes along with the second iteration of the relaxed field equations. Performing a single iteration is not sufficient to produce this dynamics, because the equations of motion that are compatible with the first iteration, derived from the conservation equation $\partial _ { \beta } \tau _ { 0 } ^ { \alpha \beta } = 0$ , do not contain gravitational interactions. This observation was also made in the context of the linearized approximation to general relativity, back in Sec. 5.5. So formally, a second iteration of the relaxed field equations is required to obtain the Newtonian equations of motion. Similarly, a third iteration is required to find the post-Newtonian equations of motion, and so on. But as we also discussed back in Sec. 6.2.3, the conservation equation compatible with the nth iteration requires ingredients that are collected during the $( n - 1 ) \mathrm { t h }$ iteration, and it can be formulated before completing the nth iteration to obtain the gravitational potentials. In practice, therefore, we may obtain the Newtonian equations of motion on the basis of the first-iterated potentials; the post-Newtonian equations on the basis of the second-iterated potentials, and so on.

As we saw back in Sec. 6.1.4, the local conservation equations (7.55) imply the existence of globally conserved quantities. From Eq. (6.36) we have the total mass

$$
M : = \frac { 1 } { c ^ { 2 } } \int ( - g ) \bigl ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \bigr ) d ^ { 3 } x ,
$$

and from Eq. (6.37) we have the total momentum

$$
P ^ { j } : = \frac { 1 } { c } \int ( - g ) \big ( T ^ { 0 j } + t _ { \mathrm { L L } } ^ { 0 j } \big ) d ^ { 3 } x .
$$

In addition, it is useful to re-introduce the vector

$$
R ^ { j } : = \frac { 1 } { M c ^ { 2 } } \int ( - g ) \big ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \big ) x ^ { j } d ^ { 3 } x ,
$$

which denotes the position of the center-of-mass; this was first defined by Eq. (6.39). We recall that $R ^ { j }$ is related to the total momentum by the equation $M d R ^ { j } / d t = P ^ { j }$ , and that by adopting the center-of-mass frame of the spacetime, we can set both $P ^ { j }$ and $R ^ { j }$ to zero. It is worth pointing out that since $( - g ) t _ { \mathrm { H } } ^ { \alpha \beta }$ makes no relevant contribution to $\tau _ { 1 } ^ { \alpha \beta }$ at this order, as we saw back in Eq. (7.52), the conserved quantities associated with $( - g ) \dot { ( } T ^ { \alpha \beta } + t _ { \mathrm { L L } } ^ { \alpha \beta } )$ are the same as those associated with $\tau ^ { \alpha \beta }$ .

The global quantities $M , P ^ { j }$ , and $R ^ { j }$ are defined in terms of integrals that extend over all space. We may still, however, evaluate them with the near-zone information available to us now, because their expressions turn out to be insensitive to the wave-zone aspects of the integrals. To evaluate $M$ we insert our previous expression for $c ^ { - 2 } \tau _ { 1 } ^ { 0 0 }$ within Eq. (7.59), which we truncate to the near-zone domain $\mathcal { M }$ . The term involving $U$ is handled as follows. We write

$$
\partial _ { j } U \partial ^ { j } U = \partial _ { j } \bigl ( U \partial ^ { j } U \bigr ) - U \nabla ^ { 2 } U = \partial _ { j } \bigl ( U \partial ^ { j } U \bigr ) + 4 \pi G \rho ^ { * } U
$$

and observe that the first term gives rise to a surface integral that must be evaluated at $r = \mathcal { R }$ ; it makes an $\mathcal { R }$ -dependent contribution to $M$ that cancels out when the wave-zone portion of the integral is added to the near-zone portion. Collecting results, we arrive at

$$
M = \int \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \biggr ) \biggr ] d ^ { 3 } x + O ( c ^ { - 4 } )
$$

for the total mass. The integral of $\rho ^ { * }$ is $m$ , the total rest-mass of the fluid, which is separately conserved. The integral of $\scriptstyle { \frac { 1 } { 2 } } \rho ^ { * } v ^ { 2 }$ is $\tau$ , the fluid’s total kinetic energy. The integral of $- \frac { 1 } { 2 } \rho ^ { * } U$ is $\Omega$ , the gravitational potential energy. And finally, the integral of $\rho ^ { * } \Pi = \epsilon + O ( c ^ { - 2 } )$ i s $E _ { \mathrm { i n t } }$ , the total internal energy stored within the fluid. The sum of $\mathcal { T } , \Omega$ , and $E _ { \mathrm { i n t } }$ is the total energy $E$ , and this was shown to be constant (by virtue of Euler’s equation and the first law of thermodynamics) back in Sec. 1.4.3. The total mass can therefore be expressed as $M = m + E / c ^ { 2 } + { \cal O } ( c ^ { - 4 } )$ , and this equation possesses a clear interpretation: The total mass of the spacetime is a measure of all forms of energy, including rest-mass, kinetic, gravitational, and internal energies.

Similar manipulations reveal that $R ^ { j }$ can be expressed as

$$
R ^ { j } = \frac { 1 } { M } \int \rho ^ { * } x ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \biggr ) \biggr ] d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) ,
$$

and Eq. (7.60) becomes

$$
\begin{array} { c } { { P ^ { j } = \displaystyle { \int \rho ^ { * } } v ^ { j } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } { U } + \Pi + p / \rho ^ { * } \biggr ) \biggr ] d ^ { 3 } x } } \\ { { - \displaystyle { \frac { 1 } { 2 c ^ { 2 } } } \int \rho ^ { * } x ^ { j } \bigl ( \partial _ { t } U - v ^ { k } \partial _ { k } U \bigr ) d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

The leading-order piece of the total momentum was shown to be constant (by virtue of Euler’s equation) back in Sec. 1.4.3 of Chapter 1; with this improved expression the momentum is conserved to order $c ^ { - 2 }$ .

It is instructive to examine the relationship between the total mass $M$ , which is known to correspond to the ADM mass of the spacetime, and the near-zone mass $M _ { 0 }$ , defined by Eq. (7.26),

$$
M _ { 0 } = \int _ { \mathcal M } c ^ { - 2 } \tau ^ { 0 0 } d ^ { 3 } x ,
$$

which appears in the expression of Eq. (7.32) for $h ^ { 0 0 }$ in the wave zone. It is easy to see that

$$
M _ { 0 } = M + { \cal O } ( c ^ { - 4 } ) .
$$

This follows because the integrands for $M$ and $M _ { 0 }$ differ by $( - g ) t _ { \mathrm { H } } ^ { 0 0 }$ , which makes no contribution at 1pn order, and because the wave-zone portion of the integral defining $M$ makes no $\mathcal { R }$ -independent contribution to the mass. Examining the relationship at higher post-Newtonian orders, we find that subtle differences between $M _ { 0 }$ and $M$ appear at order $c ^ { - 5 }$ ; these are explored in Exercise 7.8.

Similar manipulations reveal that

$$
R _ { 0 } ^ { j } = R ^ { j } + O ( c ^ { - 4 } )
$$

and

$$
P _ { 0 } ^ { j } = P ^ { j } + { \cal O } ( c ^ { - 4 } ) ,
$$

in which $R _ { 0 } ^ { j }$ is the position of the near-zone center-of-mass introduced in Eq. (7.27), and $P _ { 0 } ^ { j }$ is the near-zone momentum introduced in Eq. (7.28). These equalities imply that at 1pn order, a coordinate choice that enforces $R ^ { j } = 0 = P ^ { j }$ also enforces $R _ { 0 } ^ { j } = 0 = P _ { 0 } ^ { j }$ .

# 7.3.3 Near-zone contribution to potentials

Armed with Eq. (7.54) for $\tau _ { 1 } ^ { \alpha \beta }$ , we are now ready to solve the relaxed field equations for 1 the second-iterated potentials $h ^ { \alpha \beta } = h _ { { \mathcal { N } } } ^ { \alpha \beta } + h _ { { \mathcal { W } } } ^ { \alpha \beta }$ . In this section we focus on the near-zone contribution $h _ { \mathcal { N } } ^ { \alpha \beta }$ , insert $\tau _ { 1 } ^ { \alpha \beta }$ within Eqs. (7.15), and express the results in a convenient form. The spatial components $h ^ { j k }$ require special care, because as we have observed in Sec. 7.1.3, the spatial trace $h ^ { k k }$ contributes to the spacetime metric at 1pn order, while the remaining components contribute only at $2 \mathrm { P N }$ order. With this in mind, it is helpful to decompose the potentials into a “scalar class” comprising $h ^ { 0 0 }$ and $h ^ { k k }$ , a “vector class” comprising $h ^ { 0 j }$ , and a “tensor class” comprising $h ^ { j k }$ .

# Scalar class

We begin with the computation of $h ^ { 0 0 }$ and $h ^ { k k }$ . Examining Eqs. (7.54), we observe that both $\tau _ { 1 } ^ { 0 0 }$ and $\tau _ { 1 } ^ { k k }$ contain a contribution proportional to $\partial _ { j } U \partial ^ { j } U$ , which does not have compact support. It is useful to re-express these terms by exploiting the identity

$$
\nabla ^ { 2 } U ^ { 2 } = 2 \partial _ { j } U \partial ^ { j } U + 2 U \nabla ^ { 2 } U ,
$$

in which we may insert Poisson’s equation $\nabla ^ { 2 } U = - 4 \pi G \rho ^ { * }$ . In this way we obtain

$$
c ^ { - 2 } \tau _ { 1 } ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \biggr ) \biggr ] - \frac { 7 } { 1 6 \pi G c ^ { 2 } } \nabla ^ { 2 } U ^ { 2 } + O ( c ^ { - 4 } )
$$

and

$$
\tau _ { 1 } ^ { k k } = \rho ^ { * } \bigg ( v ^ { 2 } - \frac { 1 } { 2 } U \bigg ) + 3 p - \frac { 1 } { 1 6 \pi G } \nabla ^ { 2 } U ^ { 2 } + O ( c ^ { - 2 } )
$$

for the relevant components of the energy-momentum pseudotensor.

Consulting Eq. (7.15), we see that the leading terms in both $h _ { \mathcal { N } } ^ { 0 0 }$ and $h _ { \mathcal { N } } ^ { k k }$ are Poisson integrals constructed from $c ^ { - 2 } \tau ^ { 0 0 }$ and $\tau ^ { k k }$ . To evaluate these we must distinguish between the pieces of the source functions that have compact support (those that are tied to the fluid variables), and those that depend on the Newtonian potential and extend beyond the matter distribution. To handle the compact-support pieces we introduce the potentials

$$
\begin{array} { l } { \displaystyle \psi ( t , \pmb { x } ) : = G \int \frac { \rho ^ { * \prime } \big ( \frac { 3 } 2 v ^ { \prime 2 } - U ^ { \prime } + \Pi ^ { \prime } \big ) + 3 p ^ { \prime } } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ { \displaystyle V ( t , \pmb { x } ) : = G \int \frac { \rho ^ { * \prime } \big ( v ^ { \prime 2 } - \frac 1 2 U ^ { \prime } \big ) + 3 p ^ { \prime } } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \end{array}
$$

in which primed quantities such as $\rho ^ { * \prime }$ indicate that the fluid variables are expressed as functions of $t$ and $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ . These satisfy the Poisson equations

$$
\begin{array} { l } { { \nabla ^ { 2 } \psi = - 4 \pi G \rho ^ { * } \biggl ( \frac { 3 } { 2 } v ^ { 2 } - U + \Pi + 3 p / \rho ^ { * } \biggr ) , } } \\ { { \nabla ^ { 2 } V = - 4 \pi G \rho ^ { * } \biggl ( v ^ { 2 } - \frac { 1 } { 2 } U + 3 p / \rho ^ { * } \biggr ) . } } \end{array}
$$

With this notation we see that at leading order, the compact-support piece of $h _ { \mathcal { N } } ^ { 0 0 }$ is given by $4 U / c ^ { 2 } + 4 ( \psi - V ) / c ^ { 4 }$ , while the compact-support piece of $h _ { \mathcal { N } } ^ { k k }$ is $4 V / c ^ { 4 }$ ; this choice of notation is motivated by the fact that once the potentials are inserted within the near-zone metric of Eq. (7.24), the leading-order, compact-support piece of $g _ { 0 0 }$ will involve only $U$ and $\psi$ .

Turning next to the Poisson integral involving $\nabla ^ { 2 } U ^ { 2 }$ , we evaluate it by making repeated use of integration by parts:

$$
\begin{array} { l } { { \displaystyle \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { \nabla ^ { 2 } U ^ { \prime 2 } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } = \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } \frac { \partial ^ { \prime \prime } U ^ { \prime 2 } } { | x - x ^ { \prime } | } d S _ { j } ^ { \prime } - \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \partial ^ { \prime \prime } U ^ { \prime 2 } \partial _ { j } ^ { \prime } \frac { 1 } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } } }  \\ { { \displaystyle \qquad = \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } \left( \frac { \partial ^ { \prime } U ^ { \prime 2 } } { | x - x ^ { \prime } | } - U ^ { \prime 2 } \partial _ { j } ^ { \prime } \frac { 1 } { | x - x ^ { \prime } | } \right) d S _ { j } ^ { \prime } } } \\ { { \displaystyle \qquad + \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } U ^ { \prime 2 } \nabla ^ { \prime 2 } \frac { 1 } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } } } \\ { { \displaystyle \qquad = - U ^ { 2 } + \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } \left( \frac { \partial ^ { \prime \prime } U ^ { \prime 2 } } { | x - x ^ { \prime } | } - U ^ { \prime 2 } \partial _ { j } ^ { \prime } \frac { 1 } { | x - x ^ { \prime } | } \right) d S _ { j } ^ { \prime } . \quad \qquad ( } } \end{array}
$$

The surface term is evaluated at $r ^ { \prime } = \mathcal { R }$ , and because $U ^ { \prime }$ falls off as $( r ^ { \prime } ) ^ { - 1 }$ at large distances from the matter distribution, it makes a contribution that scales as $\mathcal { R } ^ { - 2 }$ . As with all $\mathcal { R }$ - dependent terms in the potentials $h _ { \mathcal { N } } ^ { \alpha \beta }$ R R, we may discard it because it will eventually be cancelled by an equal and opposite term in $h _ { \mathcal { W } } ^ { \alpha \beta }$ .

It is interesting to note that if the Poisson integral of $\nabla ^ { 2 } U ^ { 2 }$ were extended to infinity instead of being truncated to the domain $\mathcal { M }$ , it would be exactly equal to $- U ^ { 2 }$ . This may seem like a trivial observation, but we wish to call attention to the fact that the solution to the differential equation $\nabla ^ { 2 } f = \nabla ^ { 2 } g$ is not necessarily the obvious $f = g$ . The actual solution may also include a solution to Laplace’s equation $\nabla ^ { 2 } f = 0$ , and the correct mixture of particular and homogeneous solutions depends on the boundary conditions captured by the surface integral in Eq. (7.75). When the boundary conditions are such that the surface integral vanishes except for $\mathcal { R }$ -dependent terms, the particular solution $f = g$ is justified. When, however, the surface integral returns contributions that are independent of $\mathcal { R }$ , the relevant solution is no longer the simple $f = g$ .

We have now taken care of the leading-order, Poisson-integral terms in Eq. (7.15). Proceeding to the next order in $h _ { \mathcal { N } } ^ { 0 0 }$ , we examine the superpotential term, in which we may insert the leading-order expression $c ^ { - 2 } \tau _ { 1 } ^ { 0 0 } = \rho ^ { * } + { \cal O } ( c ^ { - 2 } )$ , because the correction at order $c ^ { - 2 }$ would contribute to $h _ { \mathcal { N } } ^ { 0 0 }$ at order $c ^ { - 6 }$ . This gives rise to the post-Newtonian

superpotential

$$
X ( t , \pmb { x } ) : = G \int \rho ^ { * } ( t , \pmb { x } ^ { \prime } ) | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } ,
$$

in which the integral over $\mathcal { M }$ is naturally truncated to the volume occupied by the matter distribution. With this notation we observe that the superpotential term in $h _ { \mathcal { N } } ^ { 0 0 }$ is proportional to $\partial _ { t } ^ { 2 } {  \boldsymbol { X } } .$ . Since $\nabla ^ { 2 } | x - x ^ { \prime } | = 2 | x - x ^ { \prime } | ^ { - 1 }$ when $\boldsymbol { x } \neq \boldsymbol { x } ^ { \prime }$ , we see that the superpotential satisfies the Poisson equation

$$
\nabla ^ { 2 } { \boldsymbol { X } } = 2 { \boldsymbol { U } } ,
$$

and $X$ is therefore sourced by the Newtonian potential. The connection between Eqs. (7.76) and (7.77) is further explored in Box 7.3.

Collecting results, we have obtained the following expressions for the scalar potentials $h _ { \mathcal { N } } ^ { 0 0 }$ and $h _ { \mathcal { N } } ^ { k k }$ :

$$
\begin{array} { l } { { { \displaystyle h _ { 2 { \mathcal N } } ^ { 0 0 } = \frac { 4 } { c ^ { 2 } } U + \frac { 1 } { c ^ { 4 } } \bigg ( 7 U ^ { 2 } + 4 \psi - 4 V + 2 \frac { \partial ^ { 2 } X } { \partial t ^ { 2 } } \bigg ) - \frac { 2 G } { 3 c ^ { 5 } } { \dddot { \mathcal Z } } ^ { k k } ( t ) + { \cal O } ( c ^ { - 6 } ) , } } } \\ { { { \displaystyle h _ { 2 { \mathcal N } } ^ { k k } = \frac { 1 } { c ^ { 4 } } \bigg ( U ^ { 2 } + 4 V \bigg ) - 2 \frac { G } { c ^ { 5 } } { \ddot { \mathcal Z } } ^ { k k } ( t ) + { \cal O } ( c ^ { - 6 } ) . } } } \end{array}
$$

These expressions are accurate up to order $c ^ { - 6 }$ , and they incorporate Newtonian, 1pn, and $1 . 5 \mathrm { P N }$ terms. Once we have obtained the spacetime metric from the potentials, the terms of order $c ^ { - 5 }$ will be shown to represent coordinate artifacts that can be removed by a coordinate transformation.

The post-Newtonian superpotential $X$ is defined by Eq. (7.76), and this leads to the Poisson equation displayed in Eq. (7.77). Here we ask whether defining the superpotential through

$$
\nabla ^ { 2 } X = 2 U
$$

necessarily leads back to the integral representation of Eq. (7.76). We shall see that the answer to this question is subtle, and provides further illustration of the fact that boundary conditions and solutions to Laplace’s equation sometimes play an important role in solving Poisson’s equation.

The general solution to Poisson’s equation for the superpotential is

$$
X ( t , \pmb { x } ) = - \frac { 1 } { 2 \pi } \int \frac { U ( t , \pmb { x } ^ { \prime } ) } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } + X _ { 0 } ( t , \pmb { x } ) ,
$$

in which $X _ { 0 }$ is a solution to $\nabla ^ { 2 } X _ { 0 } = 0 .$ . But the integral is ill defined; because $U$ falls off as $( r ^ { \prime } ) ^ { - 1 }$ at large distances, the integrand behaves as $( r ^ { \prime } ) ^ { - 2 }$ , and since it is multiplied by the integration measure ${ r } ^ { \prime 2 } d { r } ^ { \prime }$ , the integral is linearly divergent. To provide a well-defined prescription for the Poisson integral, we truncate the domain of integration to $\mathcal { M }$ . This amounts to modifying the Poisson equation to $\nabla ^ { 2 } X = 2 U \Theta ( \mathcal { R } - r ) ,$ in which $\Theta$ is the Heaviside step function; the modification produces no noticeable changes in the near zone.

Inserting the standard expression of Eq. (7.38) for the Newtonian potential, we find that the superpotential can be expressed as

$$
X ( t , { \pmb x } ) = G \int \rho ^ { * } ( t , { \pmb y } ) K ( { \pmb x } ; { \pmb y } ) d ^ { 3 } y + X _ { 0 } ( t , { \pmb x } ) ,
$$

in which the two-point function $K ( x ; y )$ is defined by

$$
K ( \pmb { x } ; \pmb { y } ) : = - \frac { 1 } { 2 \pi } \int _ { \mathcal { M } } \frac { d ^ { 3 } \pmb { x } ^ { \prime } } { | \pmb { x } - \pmb { x } ^ { \prime } | | \pmb { x } ^ { \prime } - \pmb { y } | } .
$$

To evaluate this we exploit the observation that $K$ can depend on $_ { x }$ and $y$ only through the combination $x - y ,$ and thereby set $\mathbf { \boldsymbol { y } } = \mathbf { \boldsymbol { \mathsf { 0 } } }$ to simplify the integral. Making use of the addition theorem for spherical harmonics, we find that $\begin{array} { r } { K ( \pmb { x } ; \mathbf { 0 } ) = - 2 \int _ { 0 } ^ { \mathcal { R } } ( r _ { > } ) ^ { - 1 } r ^ { \prime } d r ^ { \prime } , } \end{array}$ , in which $r _ { > }$ is the greater of $r$ and $\boldsymbol { r ^ { \prime } }$ . This returns $r - 2 \mathcal { R } ,$ and we conclude that the two-point function is given by

$$
K ( \mathbf { x } ; \mathbf { y } ) = | \mathbf { x } - \mathbf { y } | - 2 \mathcal { R } .
$$

Inserting this within the integral for the superpotential, we obtain

$$
X ( t , x ) = G \int \rho ^ { * } ( t , x ^ { \prime } ) | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } - 2 m { \mathcal { R } } + X _ { 0 } ( t , x ) ,
$$

with $\begin{array} { r } { m : = \int \rho ^ { \ast } ( t , \pmb { x } ^ { \prime } ) d ^ { 3 } x ^ { \prime } } \end{array}$ denoting the total rest-mass of the matter distribution. Choosing $X _ { 0 } =$ $2 m \mathcal { R } ,$ we reproduce the original definition of the superpotential.

It is interesting to note that since it is $\partial _ { t } ^ { 2 } {  \boldsymbol { X } }$ that appears in the gravitational potentials, the addition of $- 2 m \mathcal { R } + X _ { 0 }$ to the integral is immaterial, so long as $X _ { 0 }$ does not depend on time. The superpotential, therefore, is sufficiently robust to withstand the ambiguities associated with the choice of solution to $\nabla ^ { 2 } X = 2 U$ .

# Vector class

For our purposes it is necessary to evaluate the potential $h _ { \mathcal { N } } ^ { 0 j }$ to order $c ^ { - 3 }$ only. Our expression for $c ^ { - 1 } \tau _ { 1 } ^ { 0 j }$ in Eq. (7.54b) is more accurate than we need, and we may truncate it to its leading term $\rho ^ { * } v ^ { j } + O ( c ^ { - 2 } )$ . Consulting Eq. (7.15b), we see that the leading term in the potential is given by a Poisson integral constructed from c−1τ 0 j1 , and we obtain

$$
h _ { 2 \mathcal { N } } ^ { 0 j } = \frac { 4 } { c ^ { 3 } } U ^ { j } + O ( c ^ { - 5 } ) ,
$$

where $U ^ { j }$ is the vector potential defined by Eq. (7.39). In principle we have enough information to calculate the correction terms at order $c ^ { - 5 }$ , but these will not be needed in our future developments.

# Tensor class

The computation of $h _ { \mathcal { N } } ^ { j k }$ is more involved, because its source term contains a field contribution that is not as easy to deal with as it was with the scalar potentials. Returning

to Eq. (7.54) and exploiting once more the identity of Eq. (7.70), we express $\tau _ { 1 } ^ { j k }$ in the form

$$
\tau _ { 1 } ^ { j k } = \rho ^ { * } \bigg ( v ^ { j } v ^ { k } - \frac { 1 } { 2 } U \delta ^ { j k } \bigg ) + p \delta ^ { j k } - \frac { 1 } { 1 6 \pi G } \delta ^ { j k } \nabla ^ { 2 } U ^ { 2 } + \frac { 1 } { 4 \pi G } \partial ^ { j } U \partial ^ { k } U + O ( c ^ { - 2 } ) .
$$

Consulting Eq. (7.15c), we see that the leading term in the potential is a Poisson integral constructed from $\tau _ { 1 } ^ { j k }$ . The first three terms have compact support, and they give rise to the tensorial potential

$$
W ^ { j k } ( t , \mathbf { x } ) : = G \int \frac { \rho ^ { \ast \prime } \big ( v ^ { \prime j } v ^ { \prime k } - \frac { 1 } { 2 } U ^ { \prime } \delta ^ { j k } \big ) + p ^ { \prime } \delta ^ { j k } } { | \mathbf { x } - \mathbf { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

which satisfies the Poisson equation

$$
\nabla ^ { 2 } W ^ { j k } = - 4 \pi G \bigg ( \rho ^ { * } v ^ { j } v ^ { k } - \frac { 1 } { 2 } \rho ^ { * } U \delta ^ { j k } + p \delta ^ { j k } \bigg ) .
$$

The fourth term involves $\nabla ^ { 2 } U ^ { 2 }$ , which we know how to handle, and which produces a contribution proportional to $\delta ^ { j k } U ^ { 2 }$ to $h _ { \mathcal { N } } ^ { j k }$ . The fifth and final term is the hard one. To account for it we introduce another tensorial potential defined by

$$
\chi ^ { j k } ( t , \pmb { x } ) : = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { \partial ^ { j ^ { \prime } } U ^ { \prime } \partial ^ { k ^ { \prime } } U ^ { \prime } } { | \pmb { x } - \pmb { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } ,
$$

which satisfies the Poisson equation

$$
\nabla ^ { 2 } \chi ^ { j k } = - \partial ^ { j } U \partial ^ { k } U .
$$

Because the Poisson integral in Eq. (7.83) is truncated at $r ^ { \prime } = \mathcal { R }$ , the source term on the right-hand side of the Poisson equation should be multiplied by $\Theta ( \mathcal { R } - r )$ , as was discussed in Box 7.3. But since the truncation produces no noticeable changes within the near zone, we have kept it implicit in Eq. (7.84).

Armed with these tensorial potentials, we find that the gravitational potentials can be expressed as

$$
h _ { 2 \mathcal { A } } ^ { j k } = \frac { 1 } { c ^ { 4 } } \Big ( 4 W ^ { j k } + U ^ { 2 } \delta ^ { j k } + 4 \chi ^ { j k } \Big ) - 2 \frac { G } { c ^ { 5 } } \dddot { \mathcal { Z } } ^ { j k } ( t ) + O ( c ^ { - 6 } ) ,
$$

where we have included the $O ( c ^ { - 5 } )$ term for completeness.

$$
\mathsf { C o m p u t a t i o n o f } \chi ^ { j k }
$$

We must now face the computation of $\chi ^ { j k }$ , as defined by Eq. (7.83). Returning to the standard expression of Eq. (7.38) for the Newtonian potential, we differentiate it and obtain

$$
\begin{array} { c } { { \partial _ { j ^ { \prime } } U ^ { \prime } = G \displaystyle \int d ^ { 3 } y _ { 1 } \rho _ { 1 } ^ { * } \frac { \partial } { \partial x ^ { \prime j } } \frac { 1 } { | x ^ { \prime } - y _ { 1 } | } } } \\ { { = - G \displaystyle \int d ^ { 3 } y _ { 1 } \rho _ { 1 } ^ { * } \frac { \partial } { \partial y _ { 1 } ^ { j } } \frac { 1 } { | x ^ { \prime } - y _ { 1 } | } , } } \end{array}
$$

in which $_ { y _ { 1 } }$ is an integration variable, and $\rho _ { 1 } ^ { * } : = \rho ^ { * } ( t , \mathbf { y } _ { 1 } )$ . Expressing $\partial _ { k ^ { \prime } } U ^ { \prime }$ in a similar way, in terms of an independent integration variable $y _ { 2 }$ , and inserting these expressions in the Poisson integral for $\chi ^ { j k }$ , we arrive at

$$
\chi ^ { j k } = G ^ { 2 } \int d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } \frac { \partial ^ { 2 } } { \partial y _ { 1 } ^ { j } \partial y _ { 2 } ^ { k } } K ( { \bf x } ; { \bf y } _ { 1 } , { \bf y } _ { 2 } ) ,
$$

where

$$
K ( \pmb { x } ; \pmb { y } _ { 1 } , \pmb { y } _ { 2 } ) : = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { d ^ { 3 } \pmb { x } ^ { \prime } } { | \pmb { x } - \pmb { x } ^ { \prime } | | \pmb { x } ^ { \prime } - \pmb { y } _ { 1 } | | \pmb { x } ^ { \prime } - \pmb { y } _ { 2 } | }
$$

is a three-point function that must now be evaluated. This computation is presented in $\mathrm { B o x } 7 . 4$ , and the end result is

$$
K ( \mathbf { x } ; \mathbf { y } _ { 1 } , \mathbf { y } _ { 2 } ) = 1 - \ln \frac { S } { 2 \mathcal { R } } ,
$$

where

$$
S : = r _ { 1 } + r _ { 2 } + r _ { 1 2 } ,
$$

with the notations

$$
r _ { 1 } : = \left| \pmb { x } - \pmb { y } _ { 1 } \right| , \qquad r _ { 2 } : = \left| \pmb { x } - \pmb { y } _ { 2 } \right| , \qquad r _ { 1 2 } : = \left| \pmb { y } _ { 1 } - \pmb { y } _ { 2 } \right| .
$$

We also introduce the corresponding separation vectors

$$
r _ { 1 } : = x - y _ { 1 } , \qquad r _ { 2 } : = x - y _ { 2 } , \qquad r _ { 1 2 } : = y _ { 1 } - y _ { 2 } ,
$$

and the unit vectors

$$
{ \pmb n } _ { 1 } : = \frac { { \pmb r } _ { 1 } } { r _ { 1 } } , \qquad { \pmb n } _ { 2 } : = \frac { { \pmb r } _ { 2 } } { r _ { 2 } } , \qquad { \pmb n } _ { 1 2 } : = \frac { { \pmb r } _ { 1 2 } } { r _ { 1 2 } } .
$$

The dependence of $K$ on $\mathcal { R }$ comes from the fact that the domain of integration is truncated at $r ^ { \prime } = \mathcal { R }$ . This dependence plays no role, however, because $K$ is differentiated as soon as it is inserted within Eq. (7.87). These derivatives are straightforward to compute, and we obtain

$$
\frac { \partial ^ { 2 } { \cal K } } { \partial y _ { 1 } ^ { j } \partial y _ { 2 } ^ { k } } = \frac { \left( n _ { 1 } ^ { j } - n _ { 1 2 } ^ { j } \right) \left( n _ { 2 } ^ { k } + n _ { 1 2 } ^ { k } \right) } { S ^ { 2 } } - \frac { n _ { 1 2 } ^ { j } n _ { 1 2 } ^ { k } - \delta ^ { j k } } { S r _ { 1 2 } } .
$$

We then arrive at

$$
\begin{array} { c } { { \chi ^ { j k } = G ^ { 2 } \displaystyle \int \frac { \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } \big ( n _ { 1 } ^ { j } - n _ { 1 2 } ^ { j } \big ) \big ( n _ { 2 } ^ { k } + n _ { 1 2 } ^ { k } \big ) } { S ^ { 2 } } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } } } \\ { { - G ^ { 2 } \displaystyle \int \frac { \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } \big ( n _ { 1 2 } ^ { j } n _ { 1 2 } ^ { k } - \delta ^ { j k } \big ) } { S r _ { 1 2 } } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } . } } \end{array}
$$

It is easy to check that each integral is symmetric in the $j k$ indices; this property is evident in the second integral, and to establish it for the first it is necessary to swap the variables of integration, $y _ { 1 }  y _ { 2 }$ , keeping in mind that ${ \pmb n } _ { 1 2 }  { \pmb n } _ { 2 1 } = - { \pmb n } _ { 1 2 }$ under this operation.

Note that the trace $\chi : = \delta _ { j k } \chi ^ { j k }$ is given by the Poisson potential of ${ \textstyle \frac { 1 } { 2 } } \partial _ { j } U \partial ^ { j } U$ . Using the identity of Eq. (7.70), it is easy to see that $\chi$ can be expressed as

$$
\chi = - \frac { 1 } { 2 } U ^ { 2 } + G \int _ { \mathcal { M } } \frac { \rho ^ { \prime * } U ^ { \prime } } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

By inserting the Poisson integral for $U$ , we can express this in the form

$$
\chi = - \frac { 1 } { 2 } G ^ { 2 } \int \frac { \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } } { | x - y _ { 1 } | | x - y _ { 2 } | } + G ^ { 2 } \int \frac { \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } } { | x - y _ { 1 } | | y _ { 1 } - y _ { 2 } | } .
$$

The second integral can be written in the symmetric form

$$
\frac { 1 } { 2 } \int \frac { \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } } { | \pmb { x } - \pmb { y } _ { 1 } | | \pmb { y } _ { 1 } - \pmb { y } _ { 2 } | } + \frac { 1 } { 2 } \int \frac { \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } } { | \pmb { x } - \pmb { y } _ { 2 } | | \pmb { y } _ { 1 } - \pmb { y } _ { 2 } | } ,
$$

and this gives

$$
\chi = \frac { 1 } { 2 } G ^ { 2 } \int \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } \biggl ( - \frac { 1 } { r _ { 1 } r _ { 2 } } + \frac { 1 } { r _ { 1 } r _ { 1 2 } } + \frac { 1 } { r _ { 2 } r _ { 1 2 } } \biggr ) d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } .
$$

Our final expression is

$$
\chi = \frac { 1 } { 2 } G ^ { 2 } \int \rho _ { 1 } ^ { * } \rho _ { 2 } ^ { * } \frac { r _ { 1 } + r _ { 2 } - r _ { 1 2 } } { r _ { 1 } r _ { 2 } r _ { 1 2 } } d ^ { 3 } y _ { 1 } d ^ { 3 } y _ { 2 } ,
$$

and we may check that the trace of Eq. (7.95) reproduces this. The calculation is aided by the identities

$$
\begin{array} { r l r } & { } & { n _ { 1 } \cdot n _ { 2 } = \frac { r _ { 1 } ^ { 2 } + r _ { 2 } ^ { 2 } - r _ { 1 2 } ^ { 2 } } { 2 r _ { 1 } r _ { 2 } } , } \\ & { } & \\ & { } & { n _ { 1 } \cdot n _ { 1 2 } = \frac { r _ { 2 } ^ { 2 } - r _ { 1 } ^ { 2 } - r _ { 1 2 } ^ { 2 } } { 2 r _ { 1 } r _ { 1 2 } } , } \\ & { } & \\ & { } & { n _ { 2 } \cdot n _ { 1 2 } = \frac { r _ { 2 } ^ { 2 } - r _ { 1 } ^ { 2 } + r _ { 1 2 } ^ { 2 } } { 2 r _ { 2 } r _ { 1 2 } } , } \end{array}
$$

involving the unit vectors defined by Eq. (7.93).

# Box 7.4

# Three-point function K (x; y1, y2)

The computation of the three-point function defined by Eq. (7.88) follows some of the same steps that were used to calculate the two-point function $K ( x ; y )$ in Box 7.3.

We note first that $K ( \boldsymbol { x } ; \boldsymbol { y } _ { 1 } , \boldsymbol { y } _ { 2 } )$ satisfies

$$
\nabla ^ { 2 } K ( { \pmb x } ; { \pmb y } _ { 1 } , { \pmb y } _ { 2 } ) = - \frac { 1 } { | { \pmb x } - { \pmb y } _ { 1 } | | { \pmb x } - { \pmb y } _ { 2 } | } ,
$$

and verify that $K _ { \mathfrak { p } } = - \ln S$ is a particular solution. The relation implies that

$$
\nabla ^ { 2 } K _ { \mathfrak { p } } = - { \frac { 1 } { S ^ { 2 } } } ( S \nabla ^ { 2 } S - \partial _ { j } S \partial ^ { j } S ) ,
$$

and the various derivatives can be computed from the definition of $S$ provided in Eq. (7.90). We have, for example, $\partial ^ { j } S = n _ { 1 } ^ { j } + n _ { 2 } ^ { j }$ , from which it follows that

$$
\partial ^ { j k } S = - \frac { n _ { 1 } ^ { j } n _ { 1 } ^ { k } - \delta ^ { j k } } { r _ { 1 } } - \frac { n _ { 2 } ^ { j } n _ { 2 } ^ { k } - \delta ^ { j k } } { r _ { 2 } } .
$$

From this, and the helpful identities of Eqs. (7.100), we obtain

$$
\nabla ^ { 2 } S = 2 \frac { r _ { 1 } + r _ { 2 } } { r _ { 1 } r _ { 2 } } , \qquad \partial _ { j } S \partial ^ { j } S = \frac { ( r _ { 1 } + r _ { 2 } - r _ { 1 2 } ) S } { r _ { 1 } r _ { 2 } } .
$$

Collecting results, we confirm that $K _ { \mathfrak { p } }$ is a solution to $\nabla ^ { 2 } K = - 1 / ( r _ { 1 } r _ { 2 } )$

To this we must add a suitable solution $K _ { \mathrm { h } }$ to Laplace’s equation. The solution to the homogeneous equation must be non-singular in all three variables $x , y _ { 1 } ,$ and $_ { y _ { 2 } , }$ because the singularity structure required by Eq. (1) is already contained in $K _ { \mathfrak { p } }$ . Furthermore, $K _ { \mathrm { h } }$ must be dimensionless, and the only possibility is to make it equal to a constant. We are therefore looking for a solution of the form

$$
K = K _ { 0 } - \ln ( r _ { 1 } + r _ { 2 } + r _ { 1 2 } ) ,
$$

where $K _ { 0 }$ is a dimensionless constant. To determine this we carry out an independent computation of the special value $K ( x ; { \mathbf 0 } , { \mathbf 0 } )$ , and compare our result to $K _ { 0 } - \ln ( 2 r )$ , which follows from the general expression.

From Eq. (7.88) we have

$$
K ( x ; { \bf 0 } , { \bf 0 } ) = \frac { 1 } { 4 \pi } \int _ { \mathcal { M } } \frac { d ^ { 3 } x ^ { \prime } } { | x - x ^ { \prime } | | x ^ { \prime } | ^ { 2 } } = \frac { 1 } { 4 \pi } \int _ { 0 } ^ { \mathcal { R } } \frac { d r ^ { \prime } d \Omega ^ { \prime } } { | x - x ^ { \prime } | } .
$$

Invoking the addition theorem for spherical harmonics, this is simply $\int _ { 0 } ^ { \mathcal { R } } ( r _ { > } ) ^ { - 1 } d r ^ { \prime }$ , and evaluating the integral gives $K ( \mathbf { \boldsymbol { x } } ; \mathbf { \boldsymbol { 0 } } , \mathbf { \boldsymbol { 0 } } ) = 1 + \ln ( \mathcal { R } / r )$ . This allows us to conclude that $K _ { 0 } = 1 + \ln ( 2 \mathcal { R } )$ . Collecting results, we obtain the expression displayed in Eq. (7.89).

# 7.3.4 Wave-zone contribution to potentials

In this subsection we estimate $h _ { \mathcal { W } } ^ { \alpha \beta }$ , the wave-zone contribution to the second-iterated potentials, still assuming that the field point $\boldsymbol { x }$ is within the near zone. Techniques to carry out such a computation were described back in Sec. 6.3.5, and crude estimates were obtained toward the end of that section. These ignore numerical factors and terms that depend explicitly on $\mathcal { R }$ , but they are sufficient to allow us to conclude that

$$
h _ { \mathcal { W } } ^ { 0 0 } = O ( c ^ { - 8 } ) , \qquad h _ { \mathcal { W } } ^ { 0 j } = O ( c ^ { - 8 } ) , \qquad h _ { \mathcal { W } } ^ { j k } = O ( c ^ { - 8 } ) .
$$

This is far beyond the 1pn accuracy of our calculations in this section, and we shall therefore ignore the wave-zone contribution to $h _ { 2 } ^ { \alpha \beta }$ .

To reach this conclusion we refer to Eq. (6.105), which applies to source terms of the form displayed in Eq. (6.98). In our current application, $\tau _ { 1 } ^ { \alpha \beta }$ is built entirely from $( - g ) t _ { \mathrm { L L } } ^ { \alpha \beta }$

as displayed in Eqs. (7.48), by inserting the wave-zone potentials $h _ { 1 } ^ { 0 0 }$ and $h _ { 1 } ^ { 0 j }$ given by Eqs. (7.32). Focusing our attention on $\tau _ { 1 } ^ { 0 0 }$ for concreteness, and ignoring all numerical and angle-dependent factors, we find that it has a structure given schematically by

$$
\frac { G ^ { 2 } } { c ^ { 4 } } \biggl [ \frac { M _ { 0 } ^ { 2 } } { r ^ { 4 } } + \frac { M _ { 0 } { \cal Z } ^ { j k } } { r ^ { 6 } } + \frac { M _ { 0 } { \dot { \cal Z } } ^ { j k } } { c r ^ { 5 } } + \frac { M _ { 0 } { \ddot { \cal Z } } ^ { j k } } { c ^ { 2 } r ^ { 4 } } + \frac { M _ { 0 } { \ddot { \cal Z } } ^ { j k } } { c ^ { 3 } r ^ { 3 } } + \cdots \biggr ] ,
$$

in which the ellipsis designates terms of higher post-Newtonian order. Each term is of the form $f ( \tau ) / r ^ { n }$ required for the integration techniques of Sec. 6.3.5. Ignoring the overall factor of $G ^ { 2 } / c ^ { 4 }$ , we see, for example, that for $n = 3$ we have $f = M _ { 0 } \ddot { \mathcal { T } } ^ { j k } / c ^ { 3 }$ , and that for $n = 4$ we have $f = M _ { 0 } ^ { 2 } + M _ { 0 } \ddot { \mathcal { L } } ^ { j k } / c ^ { 2 }$ . According to Eq. (6.109), an estimate of $h _ { \mathcal { W } } ^ { 0 0 }$ for each contributing $n$ is $c ^ { - ( n - 2 ) } f ^ { ( n - 2 ) } + c ^ { - ( n - 1 ) } r f ^ { ( n - 1 ) }$ . The dominant term in a post-Newtonian expansion is $c ^ { - ( n - 2 ) } f ^ { ( n - 2 ) }$ , and restoring the factor of $G ^ { 2 } / c ^ { 4 }$ , we find that for each $n$ , $h _ { \mathcal { W } } ^ { 0 0 }$ is estimated as

$$
\frac { G ^ { 2 } M _ { 0 } } { c ^ { 8 } } \frac { d ^ { 4 } \mathcal { T } ^ { j k } } { d \tau ^ { 4 } } .
$$

This is of order $c ^ { - 8 }$ , and contributes to $h _ { 2 } ^ { 0 0 }$ at $3 \mathrm { P N }$ order. A similar result follows for the other components of $h _ { \mathcal { W } } ^ { \alpha \beta }$ 2 , and we arrive at the statement of Eq. (7.101).

In fact, a detailed computation shows that these contributions are actually gauge artifacts that can be removed by a suitable coordinate transformation. The first instance in which $h _ { \mathcal { W } } ^ { \alpha \beta }$ makes a non-trivial contribution to the near-zone potentials turns out to be at $4 \mathrm { P N }$ order. In any event, we see that $h _ { \mathcal { W } } ^ { \alpha \beta }$ is far too small to contribute to our 1pn potentials, and for this reason we do not need to calculate it in detail.

# 7.3.5 Near-zone potentials: Final answer

We are now ready to collect our results and display the final expression for the seconditerated potentials $h _ { 2 } ^ { \alpha \beta }$ in the near zone. Our results are summarized in Box 7.5.

<table><tr><td>Box 7.5</td><td>Near-zone potentials</td></tr><tr><td></td><td>Combining Eqs.(7.78),(7.79),(7.85),and (7.101),wefindthatthenear-zonegravitationalpotentialsare given by</td></tr><tr><td></td><td>²x) 4 (7U²+4ψ -4V +2 2G. (1)+0(c-6)， 1 U + at2 3c5 2 C4 4</td></tr><tr><td></td><td>m Ui+O(c-5)， 3 n2 2()+0(c-)， 4(4Wjk+U28ik+4xik）)- 4</td></tr></table>

The potentials that make up $h ^ { \alpha \beta }$ satisfy the Poisson equations

$$
\begin{array} { r l } & { \nabla ^ { 2 } U = - 4 \pi G \rho ^ { * } , } \\ & { \nabla ^ { 2 } \psi = - 4 \pi G \rho ^ { * } \left( \frac { 3 } { 2 } v ^ { 2 } - U + \Pi + 3 p / \rho ^ { * } \right) , } \\ & { } \\ & { \nabla ^ { 2 } V = - 4 \pi G \rho ^ { * } \left( v ^ { 2 } - \frac { 1 } { 2 } U + 3 p / \rho ^ { * } \right) , } \\ & { \nabla ^ { 2 } X = 2 U , } \\ & { \nabla ^ { 2 } U ^ { j } = - 4 \pi G \rho ^ { * } v ^ { j } , } \\ & { \nabla ^ { 2 } W ^ { j k } = - 4 \pi G \left( \rho ^ { * } v ^ { j } v ^ { k } - \frac { 1 } { 2 } \rho ^ { * } U \delta ^ { j k } + p \delta ^ { j k } \right) , } \\ & { \nabla ^ { 2 } \chi ^ { j k } = - 3 ^ { j } U \partial ^ { k } U . } \end{array}
$$

The solutions are

$$
\begin{array} { r l } & { \quad E - C \int \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } d x ^ { \gamma } , } \\ & { \quad \psi - C \int \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } ( \psi - \psi ^ { \gamma } + \nabla ^ { \beta } ) d x ^ { \gamma } , } \\ & { \quad V - C \int \int ^ { \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } } \| x - x ^ { \gamma } \| ^ { \alpha } d x ^ { \gamma } , } \\ & { \quad \quad X - C \int \int ^ { \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } } \| x - x ^ { \beta } \| ^ { \alpha } d x ^ { \gamma } , } \\ & { \quad X - C \int \int ^ { \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } } \| x - x ^ { \beta } \| ^ { \alpha } d x ^ { \gamma } , } \\ & { \quad \psi - C \int \int _ { \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } } ^ { \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } } \psi ^ { \gamma } , } \\ & { \quad \psi ^ { \beta } - C \int \int ^ { \frac { \partial ^ { \alpha } ( x ^ { \beta } ) ^ { \alpha } } { \| x - x ^ { \beta } } } \frac { \| x - x ^ { \beta } \| ^ { \alpha } } { \| x - x ^ { \beta } \| ^ { \alpha } } d x ^ { \gamma } , } \\ & { \quad \psi ^ { \beta } = C ^ { 2 } \int ^ { \frac { \partial ^ { \alpha } ( x ^ { \beta } ) ^ { \alpha } ( \psi - \psi ^ { \gamma } ) } { \| x - x ^ { \beta } \| ^ { \alpha } } } \frac { \| \psi - x ^ { \beta } \| ^ { \alpha } } { \| x - x ^ { \beta } \| ^ { \alpha } } d x ^ { \gamma } , } \\ & { \quad \quad \psi ^ { \beta } = C ^ { 2 } \int ^ { \frac { \partial ^ { \alpha } } { \| x - x \| ^ { \alpha } } } \frac { \| \psi - x ^ { \beta } \| ^ { \alpha } + \frac { \alpha ^ { 2 } \alpha ^ { 2 } \beta ^ { \alpha } } { \| x - x ^ { \beta } \| ^ { \alpha } } } { \sqrt { \frac { \partial ^ { \alpha } } { \partial x ^ { \beta } } } } d y ^ { \alpha } . } \end{array}
$$

The potentials are evaluated at time $t$ and position $x ;$ ; the sources are evaluated at the same time but at ${ \mathsf { p } } 0 -$ sition $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ . We use the notation $\pmb { r } _ { 1 } : = \pmb { x } - \pmb { y } _ { 1 } , \pmb { r } _ { 1 } : = | \pmb { r } _ { 1 } | , \pmb { n } _ { 1 } : = \pmb { r } _ { 1 } / r _ { 1 }$ (and similarly for $r _ { 2 } , r _ { 2 }$ , and ${ \pmb n } _ { 2 } )$ , as well as $r _ { 1 2 } : = y _ { 1 } - y _ { 2 } , r _ { 1 2 } : = | { \pmb r } _ { 1 2 } |$ and ${ \pmb n } _ { 1 2 } : = { \pmb r } _ { 1 2 } / r _ { 1 2 }$ , in which $_ { y _ { 1 } }$ and $y _ { 2 }$ are integration variables. We also have $S : = r _ { 1 } + r _ { 2 } + r _ { 1 2 } ,$ and the trace of $\chi ^ { j k }$ is given by

$$
\chi = - \frac { 1 } { 2 } U ^ { 2 } + G \int _ { \mathcal { M } } \frac { \rho ^ { * \prime } U ^ { \prime } } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

From Eq. (7.23) we find that the potentials give rise to the spacetime metric

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \biggl ( \psi - U ^ { 2 } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } X } { \partial t ^ { 2 } } \biggr ) - \frac { 4 G } { 3 c ^ { 5 } } \dddot k ( t ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } U _ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \biggl [ 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \biggl ( \psi + U ^ { 2 } - 2 V + \frac { 1 } { 2 } \frac { \partial ^ { 2 } X } { \partial t ^ { 2 } } \biggr ) \biggr ] } } \\ { { \displaystyle ~ + \frac { 4 } { c ^ { 4 } } \biggl ( { \mathcal W } ^ { j k } + { \chi } ^ { j k } \biggr ) - 2 \frac { G } { c ^ { 5 } } \dddot L ^ { ( j k ) } ( t ) + { \cal O } ( c ^ { - 6 } ) . } } \end{array}
$$

This metric is too accurate for most of our purposes. As we indicated back in Sec. 7.1.3, in order to describe the slow motion of a weakly gravitating system accurately through 1pn order, we require $g _ { 0 0 }$ to order $c ^ { - 4 } , g _ { 0 j }$ to order $c ^ { - 3 }$ , and $g _ { j k }$ to order $c ^ { - 2 }$ . For this application our previous expressions can therefore be truncated to

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \biggl ( \psi - U ^ { 2 } + \frac { 1 } { 2 } \frac { \partial ^ { 2 } X } { \partial t ^ { 2 } } \biggr ) + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } U _ { j } + O ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \biggl ( 1 + \frac { 2 } { c ^ { 2 } } U \biggr ) + O ( c ^ { - 4 } ) . } } \end{array}
$$

This metric forms the basis of what is known as post-Newtonian theory. Chapters 8 through 10 will be devoted to the details and many applications of this approximation to general relativity.

We have previously indicated that the $c ^ { - 5 }$ term in $g _ { 0 0 }$ is a coordinate artifact that has no impact on the physics of our gravitating system. Because it depends only on time, this term may in fact be removed by a transformation of the time coordinate given by

$$
t = t ^ { \prime } - \frac { 2 G } { 3 c ^ { 5 } } \ddot { \mathcal { Z } } ^ { k k } ( t ^ { \prime } ) + { \cal O } ( c ^ { - 7 } ) .
$$

It is a simple exercise to show that the time-time component of the transformed metric, expressed in terms of the new time $t ^ { \prime }$ , no longer contains a term at order $c ^ { - 5 }$ ; the other components of the metric are not affected by the transformation. It should be noted that the transformed coordinates are no longer harmonic; the $c ^ { - 5 }$ term must stay if we insist on using harmonic coordinates. A more careful calculation reveals that the transformation generates non-trivial terms in $g _ { 0 0 }$ at order $c ^ { - 7 }$ , or at $2 . 5 \mathrm { { p N } }$ order; these must then be combined with other $2 . 5 \mathrm { { p N } }$ terms in order to give a correct description of radiation-reaction effects. We return to this theme in Chapter 12.

<table><tr><td>Box 7.6</td><td>Post-Minkowskian theory and the slow-motion approximation</td></tr><tr><td></td><td>The advantages of incorporating aslow-motion condition withinpost-Minkowskian theoryshould be prety</td></tr><tr><td></td><td>clear by now, quite apart from the physical relevance of slow motion within a weak-field context. Had we not expanded the various retarded potentials in powers of c-1 right from the start, we would have been faced</td></tr></table>

with the need to evaluate fully retarded potentials such as

$$
\begin{array} { r l } & { \int \frac { \rho ^ { * } ( t - | x - x ^ { \prime } | , x ^ { \prime } ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } \\ & { \int \frac { \rho ^ { * } ( t - | x - x ^ { \prime } | , x ^ { \prime } ) } { | x - x ^ { \prime } | } \frac { \rho ^ { * } ( t - | x - x ^ { \prime } | - | x ^ { \prime } - x ^ { \prime \prime } | , x ^ { \prime \prime } ) } { | x ^ { \prime } - x ^ { \prime \prime } | } d ^ { 3 } x ^ { \prime } d ^ { 3 } x ^ { \prime \prime } , } \\ & { \int _ { \mathcal { M } } \frac { 1 } { | x - x ^ { \prime } | } \partial _ { j } ^ { \prime } \frac { \rho ^ { * } ( t - | x - x ^ { \prime } | - | x ^ { \prime } - x ^ { \prime \prime } | , x ^ { \prime \prime } ) } { | x ^ { \prime } - x ^ { \prime \prime } | } } \\ & { \qquad \times \partial _ { k } ^ { \prime } \frac { \rho ^ { * } ( t - | x - x ^ { \prime } | - | x ^ { \prime } - x ^ { \prime \prime } | , x ^ { \prime \prime \prime } ) } { | x ^ { \prime } - x ^ { \prime \prime } | } d ^ { 3 } x ^ { \prime } d ^ { 3 } x ^ { \prime \prime } d ^ { 3 } x ^ { \prime \prime } ; } \end{array}
$$

these expressions are the fully retarded analogues of $\begin{array} { r } { U , \int \rho ^ { \prime * } U ^ { \prime } | \pmb { x } - \pmb { x } ^ { \prime } | ^ { - 1 } d ^ { 3 } x ^ { \prime } , \mathsf { a n d } \chi ^ { j k } } \end{array}$ , respectively.

Such potentials lead to hopeless complications. Even a relatively simple potential, such as the first one listed above, leads to difficult computations because of the need to account for the retardation condition. Examples of such complexities are known in Maxwell’s theory, in which the evaluation of the retarded potential is difficult even for the simple case of a single point charge (remember the Lienard–Wiechert potentials?). The non- ´ linear potentials are even more challenging, as they involve nested retardation conditions; such potentials do not occur in electromagnetism, because of the linearity of Maxwell’s equations.

In the early 1960s, Peter Havas and Joshua Goldberg, together with their students and collaborators, worked on post-Minkowskian theory in order to study gravitational radiation, but they chose not to incorporate the slow-motion condition. Very quickly they ran into the difficulties noted above, and as a result, they were unable to go beyond the first iteration of the relaxed field equations. And even for the first-iterated potentials, they were able to evaluate quantities like the retarded Newtonian potential only for specific motions, such as circular orbits, where mathematical techniques from electrodynamics were available. In the 1970s, Havas’s student Arnold Rosenblum worked on obtaining the second iteration, but progress was extremely slow, and his untimely death in 1991 essentially brought this program to an end without any definitive conclusion.

# 7.4 Second iteration: Wave zone

Our final task in this chapter is to obtain expressions for the second-iterated potentials when the field point $_ x$ is in the wave zone, where $r : = | { \mathbf { } } x | > \mathcal { R }$ .

# 7.4.1 Near-zone contribution to potentials

Equations (7.32) give us formal expressions for the potentials $h _ { \mathcal { N } } ^ { \alpha \beta }$ evaluated in the wave zone. Recalling our discussion of Sec. 7.2.3, in which we observed that each successive multipole moment brings an additional factor of $v _ { c } / c$ to the post-Newtonian ordering,

we have that

$$
\begin{array} { r l } & { \tilde { t } _ { \mathcal { S } ^ { \prime } } ^ { ( \alpha ) } = \underbrace { \frac { 2 G } { c ^ { 2 } } \delta \mathcal { H } } _ { \mathrm { e + i r N } } + \underbrace { \frac { 2 G } { c ^ { 3 } } \delta _ { \mu } \left[ \frac { \mathcal { F } ^ { \prime } ( \tau ) } { r } \right] } _ { \mathrm { t h } \mathrm { s p t } } - \underbrace { \frac { 2 G } { 3 r ^ { 2 } } \delta _ { \mu } \nu \left[ \frac { \mathcal { F } ^ { \prime } ( \tau ) } { r } \right] } _ { \mathrm { s i g n } } + \cdots , } \\ & { \tilde { t } _ { \mathcal { S } ^ { \prime } } ^ { ( \alpha ) } = - \underbrace { \frac { 2 G } { c ^ { 3 } } \left( \frac { \alpha \kappa \cdot \kappa r } { r ^ { 2 } } \right) } _ { \mathrm { t i r w } } - \underbrace { \frac { 2 G } { c ^ { 3 } } \delta _ { \mu } \left[ \frac { \mathcal { F } ^ { \prime } ( \tau ) } { r } \right] } _ { \mathrm { t i r w } } } \\ & { \quad - \underbrace { \frac { G } { 3 r ^ { 3 } } \delta _ { \mathrm { s i g n } } \left[ \frac { \tilde { T } ^ { \prime } \tilde { t } _ { \mathrm { a } } ( \tau ) } { r } - \frac { 2 G ^ { \prime } \kappa \tilde { t } _ { \mathrm { d } } \zeta _ { \mathrm { f } } ^ { \prime } \kappa ^ { \prime \prime \prime } } { r } \right] } _ { \mathrm { t i r f } } + \cdots , } \\ &  \tilde { t } _ { \mathcal { S } ^ { \prime } } ^ { ( \alpha ) } = \underbrace { \frac { 2 G } { c ^ { 3 } } \tilde { t } _ { \mathcal { S } ^ { \prime } } ^ { ( \alpha ) } ( \frac { \tilde { T } ^ { \prime } \tilde { t } _ { \mathcal { S } ^ { \prime } } ( \tau ) } { r } + \frac { 4 \epsilon ^ { \mathrm { m a x } } ( \tilde { T } ^ { \prime } \tilde { t } ^ { \prime \prime } \tilde { t } _ { \mathcal { S } ^ { \prime } } ( \tau ) ) } { r ^ { \mathrm { s i g n } } } + \cdots , } \end{array}
$$

is a post-Newtonian expansion of the potentials that is accurate through $1 . 5 \mathrm { P N }$ order. Recalling Eq. (7.67), we have replaced the monopole moment ${ \mathcal { T } } = M _ { 0 }$ – the near-zone mass – that originally appeared in Eq. (7.32) with the total mass $M$ , since they agree to order $c ^ { - 4 }$ . We recall that $M$ is given by Eq. (7.63), so that it contains both a 0pn restmass contribution and 1pn corrections provided by the system’s total energy. We have also replaced the near-zone angular momentum $J _ { 0 }$ by the total angular momentum $\pmb { J }$ , since these quantities agree to order $c ^ { - 2 }$ .

The multipole moments that appear in Eqs. (7.107) are all functions of retarded time $\tau = t - r / c$ . Formally they must be evaluated using the first-iterated forms $\tau _ { 1 } ^ { \alpha \beta }$ for the energy-momentum pseudotensor, but since the multipole moments occur at 1pn and $1 . 5 \mathrm { { P N } }$ orders in the potentials, we may truncate $\tau _ { 1 } ^ { \alpha \beta }$ to its leading-order expression $c ^ { - 2 } \tau ^ { 0 0 } =$ $\rho ^ { * } + O ( c ^ { - 2 } )$ and $c ^ { - 1 } \tau ^ { 0 j } = \rho ^ { * } v ^ { j } + { O ( c ^ { - 2 } ) }$ . The multipole moments then take the explicit forms

$$
\begin{array} { l } { { \displaystyle { \mathcal Z } ^ { j k } ( \tau ) = \int \rho ^ { * } x ^ { j } x ^ { k } d ^ { 3 } x + O ( c ^ { - 2 } ) , } } \\ { { \displaystyle } } \\ { { \displaystyle { \mathcal Z } ^ { j k n } ( \tau ) = \int \rho ^ { * } x ^ { j } x ^ { k } x ^ { n } d ^ { 3 } x + O ( c ^ { - 2 } ) , } } \\ { { \displaystyle } } \\ { { \displaystyle { \mathcal I } ^ { j k } ( \tau ) = \epsilon ^ { j a b } \int \rho ^ { * } v ^ { a } x ^ { b } x ^ { k } d ^ { 3 } x + O ( c ^ { - 2 } ) . } } \end{array}
$$

With these, our expressions for $h _ { \mathcal { N } } ^ { \alpha \beta }$ are complete.

# 7.4.2 Wave-zone contribution to potentials

We turn next to the computation of $h _ { \mathcal { W } } ^ { \alpha \beta }$ in the wave zone. To carry this out we in-W sert the first-iterated potentials obtained in Sec. 7.2.3 within $\tau _ { 1 } ^ { \alpha \beta }$ , and solve the relaxed field equations for the second-iterated potentials. By virtue of Eq. (7.52), only the

Landau–Lifshitz pseudotensor of Eq. (7.48) makes a contribution to $\tau _ { 1 } ^ { \alpha \beta }$ . And by virtue of our requirement of $1 . 5 \mathrm { { P N } }$ overall accuracy for the potentials, we find that the only relevant piece of the first-iterated potentials is the Newtonian term in $h _ { \mathcal { W } } ^ { 0 0 }$ , given by

$$
h _ { \mathcal { W } } ^ { 0 0 } = \frac { 4 G M } { c ^ { 2 } r } + { \cal O } ( c ^ { - 4 } ) .
$$

Inserting this within Eq. (7.48), we find that the components of the energy-momentum pseudotensor are

$$
\begin{array} { l } { { \displaystyle \tau _ { 1 } ^ { 0 0 } = - \frac { 7 G M ^ { 2 } } { 8 \pi r ^ { 4 } } + { \cal O } ( c ^ { - 2 } ) , } } \\ { { \displaystyle \tau _ { 1 } ^ { 0 j } = { \cal O } ( c ^ { - 3 } ) , } } \\ { { \displaystyle \tau _ { 1 } ^ { j k } = \frac { G M ^ { 2 } } { 4 \pi r ^ { 4 } } \bigg ( n ^ { j } n ^ { k } - \frac { 1 } { 2 } \delta ^ { j k } \bigg ) , } } \end{array}
$$

in which $n ^ { j } : = x ^ { j } / r$ .

To obtain $h _ { \mathcal { W } } ^ { \alpha \beta }$ we rely on the methods of Sec. 6.3.5, which work for source terms of the form displayed in Eq. (6.98). Our first task is to decompose the effective stress tensor of Eq. (7.110c) in terms of STF angular tensors, refer to Sec. 1.5.3. We invoke the identity $\begin{array} { r } { n ^ { j } n ^ { k } = n ^ { \langle j k \rangle } + \frac { 1 } { 3 } \delta ^ { j k } } \end{array}$ and rewrite Eq. (7.110c) as

$$
\tau _ { 1 } ^ { j k } = \frac { G } { 4 \pi } \frac { M ^ { 2 } } { r ^ { 4 } } \bigg ( n ^ { \langle j k \rangle } - \frac { 1 } { 6 } \delta ^ { j k } \bigg ) .
$$

This and Eq. (7.110a) are now of the form of Eq. (7.19), and we identify $f _ { \ell = 0 } ^ { 0 0 }$ with $- \textstyle { \frac { 7 } { 2 } } G M ^ { 2 }$ , $f _ { \ell = 2 } ^ { j k }$ with $G M ^ { 2 }$ , and $f _ { \ell = 0 } ^ { j k }$ with $- \frac { 1 } { 6 } G M ^ { 2 } \delta ^ { j k }$ . In each case we have that $n = 4$ .

The contribution to $h _ { \mathcal { W } } ^ { \alpha \beta }$ from each value of $\ell$ is given by Eq. (6.105), which we copy here as

$$
h _ { \mathcal { W } } ^ { \alpha \beta } ( t , x ) = \frac { 4 G } { c ^ { 4 } } \frac { n ^ { \langle L \rangle } } { r } \left\{ \int _ { 0 } ^ { \mathcal { R } } d s f ^ { \alpha \beta } ( \tau - 2 s / c ) A ( s , r ) + \int _ { \mathcal { R } } ^ { \infty } d s f ^ { \alpha \beta } ( \tau - 2 s / c ) B ( s , r ) \right\} ,
$$

in which $\begin{array} { r } { A ( s , r ) = \int _ { \mathcal { R } } ^ { r + s } P _ { \ell } ( \xi ) p ^ { - ( n - 1 ) } d p } \end{array}$ , $\begin{array} { r } { B ( s , r ) = \int _ { s } ^ { r + s } P _ { \ell } ( \xi ) p ^ { - ( n - 1 ) } d p } \end{array}$ , and $\xi = ( r +$ $2 s ) / r - 2 s ( r + s ) / ( r p )$ . Because $f ^ { \alpha \beta }$ is a constant, it can be taken outside of each integral, and the remaining computations are simple. For $\ell = 0$ we get

$$
\begin{array} { l } { { \displaystyle h _ { \mathcal { W } } ^ { 0 0 } = 7 \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } \bigg ( 1 - 2 \frac { r } { \mathcal { R } } \bigg ) , } } \\ { { \displaystyle h _ { \mathcal { W } } ^ { j k } = \frac { 1 } { 3 } \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } \delta ^ { j k } \bigg ( 1 - 2 \frac { r } { \mathcal { R } } \bigg ) , } } \end{array}
$$

and for $\ell = 2$

$$
h _ { \mathcal { W } } ^ { j k } = \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } n ^ { \langle j k \rangle } \bigg ( 1 - \frac { 4 \mathcal { R } } { 5 r } \bigg ) .
$$

Discarding all terms involving $\mathcal { R }$ , as we are free to do, and adding the results, we arrive at

$$
\begin{array} { l } { { \displaystyle h _ { \mathcal { W } } ^ { 0 0 } = 7 \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } \ : , } } \\ { { \displaystyle h _ { \mathcal { W } } ^ { j k } = \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } n ^ { j } n ^ { k } \ : . } } \end{array}
$$

The post-Newtonian order of these contributions to $h ^ { 0 0 }$ and $h ^ { j k }$ is $1 . 5 \mathrm { { p N } }$ . To see this, we divide each of these expressions by $h ^ { 0 0 } \sim G M / ( c ^ { 2 } r )$ to obtain something proportional to $G M / ( c ^ { 2 } r )$ . We next incorporate the fact that the Newtonian acceleration $G M / r _ { c } ^ { 2 }$ is of order $r _ { c } / t _ { c } ^ { 2 }$ , which makes $G M$ of order $r _ { c } ^ { 3 } / t _ { c } ^ { 2 }$ . Setting $r \sim \lambda _ { c } = c t _ { c }$ , we finally get $h _ { \mathcal { W } } ^ { \alpha \beta } / h ^ { 0 0 } \sim$ $r _ { c } ^ { 3 } / ( c ^ { 3 } t _ { c } ^ { 3 } ) = ( v _ { c } / c ) ^ { 3 }$ , and conclude that Eqs. (7.115) do indeed make contributions of $1 . 5 \mathrm { { P N } }$ order to the gravitational potentials.

We pull everything together and summarize our results in Box 7.7. It is instructive to note that in the limit of a static, spherically symmetric body, the results correspond precisely to the post-Newtonian expansion of the Schwarzschild metric. This statement is established in Exercise 7.7.

<table><tr><td>Box 7.7</td><td>Wave-zone fields Combinig Eqs. (7.107)and (7.115), we find that the wave-zone gravitational potentials aregiven by</td></tr><tr><td></td><td>4GM (Tjkn) 7 GM² +] Tjk 1 h00 2djk （一） −djkn( c[ r + 4 c²r2</td></tr><tr><td>hoi</td><td>(n-2ym）+ 4G_1(n x J)_ （） 11 -akn [-2r² 12</td></tr><tr><td>hjk</td><td>r 4G[1ijk 1, (Tikn + 2∈mni jmk + 2∈mnk jmi) GM²</td></tr><tr><td></td><td>nin+]. an 6 + [2r 4r2 r</td></tr><tr><td></td><td>The potentials are expressed in terms of nj = xj /r,and in terms of multipole moments that depend on</td></tr><tr><td></td><td></td></tr><tr><td></td><td> retarded time T = t -r/c; overdots indicate differentiation with respect to t.In ho0 the mass term con-</td></tr><tr><td></td><td> tains OPN and 1PN contributions, the quadrupole term is a 1PN contribution,and the octupole and M2</td></tr><tr><td></td><td> terms are 1.5PN contributions.The first two terms in hoj are 1PN contributions, while the rest are 1.5PN.</td></tr><tr><td></td><td></td></tr><tr><td></td><td>And finally, the quadrupole term in hjk is a 1PN contribution, while the remaining terms are all1.5PN contributions.</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>

We have the total gravitational mass

$$
M = \int \rho ^ { * } \biggl [ 1 + \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { 2 } v ^ { 2 } - \frac { 1 } { 2 } U + \Pi \biggr ) \biggr ] d ^ { 3 } x + { \cal O } ( c ^ { - 4 } ) ,
$$

the total angular momentum

$$
\pmb { J } = \int \rho ^ { * } \pmb { x } \times \pmb { v } d ^ { 3 } x + O ( c ^ { - 2 } ) ,
$$

and the mass and current multipole moments

$$
\begin{array} { l } { { \displaystyle { \mathcal { Z } } ^ { j k } ( \tau ) = \int \rho ^ { * } x ^ { j } x ^ { k } d ^ { 3 } x + O ( c ^ { - 2 } ) , } } \\ { { \displaystyle } } \\ { { \displaystyle { \mathcal { Z } } ^ { j k n } ( \tau ) = \int \rho ^ { * } x ^ { j } x ^ { k } x ^ { n } d ^ { 3 } x + O ( c ^ { - 2 } ) , } } \\ { { \displaystyle } } \\ { { \mathcal { I } ^ { j k } ( \tau ) = \epsilon ^ { j a b } \int \rho ^ { * } x ^ { a } v ^ { b } x ^ { k } d ^ { 3 } x + O ( c ^ { - 2 } ) . } } \end{array}
$$

We recall that $M$ and $\pmb { J }$ are conserved quantities. The gravitational potentials are evaluated in the center-ofmass frame, in which the total momentum $P$ and center- $0 \mathsf { f } .$ -mass position $\pmb { R }$ are set equal to zero.

The multipole moments must be differentiated a number of times before they are inserted within the gravitational potentials. These operations are aided by the identity

$$
\dot { F } = \int \rho ^ { * } \frac { d f } { d t } d ^ { 3 } x ,
$$

where $\begin{array} { r } { F ( t ) : = \int \rho ^ { * } ( t , \pmb { x } ) f ( t , \pmb { x } ) d ^ { 3 } \pmb { x } } \end{array}$ and $d f / d t = \partial _ { t } f + v ^ { j } \partial _ { j } f ;$ ; this is established on the basis of the continuity equation $\partial _ { t } \rho ^ { * } + \partial _ { j } ( \rho ^ { * } v ^ { j } ) = 0 _ { i }$ as shown back in Sec. 1.4.3. The terms involving $d { \pmb v } / d t$ are handled by invoking Euler’s equation $\rho ^ { * } ( d v ^ { j } / d t ) = \rho ^ { * } \partial ^ { j } U - \partial ^ { j } p + O ( c ^ { - 2 } ) ,$ , which was shown in Sec. 7.3.2 to be a consequence of energy-momentum conservation.

In the far-away wave zone, where $r \gg \lambda _ { c } ,$ , the gravitational potentials reduce to

$$
\begin{array} { l } { { \displaystyle h ^ { 0 0 } = \frac { 4 G } { c ^ { 2 } r } \bigg [ M + \frac { 1 } { 2 c ^ { 2 } } { \ddot { \mathcal { Z } } } ^ { j k } n _ { j } n _ { k } + \frac { 1 } { 6 c ^ { 3 } } { \overleftrightarrow { \mathcal { Z } } } ^ { j k n } n _ { j } n _ { k } n _ { n } + \cdots \bigg ] } , }  \\ { { \displaystyle h ^ { 0 j } = \frac { 4 G } { c ^ { 3 } r } \bigg [ \frac { 1 } { 2 c } { \ddot { \mathcal { Z } } } ^ { j k } n _ { k } + \frac { 1 } { 1 2 c ^ { 3 } } \bigg ( { \overleftrightarrow { \mathcal { Z } } } ^ { j k n } - 2 \epsilon ^ { m j k } { \overleftrightarrow { \mathcal { J } } } ^ { m n } \bigg ) n _ { k } n _ { n } + \cdots \bigg ] } , }  \\ { { \displaystyle h ^ { j k } = \frac { 4 G } { c ^ { 4 } r } \bigg [ \frac { 1 } { 2 } { \ddot { \mathcal { Z } } } ^ { j k } + \frac { 1 } { 6 c } ( { \overleftrightarrow { \mathcal { Z } } } ^ { j k n } + 2 \epsilon ^ { m n j } { \ddot { \mathcal { Z } } } ^ { m k } + 2 \epsilon ^ { m n k } { \overleftrightarrow { \mathcal { J } } } ^ { m j } ) n _ { n } + \cdots \bigg ] } . }  \end{array}
$$

The time-dependent piece of $h ^ { \alpha \beta }$ is dominated by the quadrupole moment of the mass distribution.

# 7.5 Bibliographical notes

The implementation of post-Minkowskian theory presented in this chapter is based on the DIRE approach (Direct Integration of the Relaxed Einstein equations) of Will and Wiseman (1996) and Pati and Will (2000 and 2001).

The fast-motion implementation of the theory reviewed in Box. 7.6 was attempted by Goldberg, Havas, Rosenblum, and coworkers. Representative papers are Havas and Goldberg (1962), Smith and Havas (1965), and Rosenblum (1978).

# 7.6 Exercises

7.1 Show that in Eq. (7.13), the second term in the retarded expansion of $h _ { \mathcal { N } } ^ { 0 0 }$ is given by the surface integral

$$
\delta h _ { \mathcal { N } } ^ { 0 0 } = \frac { 4 G } { c ^ { 4 } } \oint _ { \partial \mathcal { M } } \tau ^ { 0 j } d S _ { j } .
$$

Using the first term of Eq. (7.48b) to estimate $\tau ^ { 0 j }$ in the wave zone, and taking the monopole and quadrupole contributions to $h ^ { 0 0 }$ from Box 7.7, show that

$$
\delta h _ { \mathcal { N } } ^ { 0 0 } \sim \frac { G ^ { 2 } } { c ^ { 1 0 } } \dddot { \mathcal { T } } ^ { j k } \dddot { \mathcal { T } } ^ { j k }
$$

after discarding terms that depend on the cutoff radius $\mathcal { R }$ . Show that this makes a contribution to $h ^ { 0 0 }$ at 4pn order.

7.2 Verify the identities of Eqs. (7.14). Using these, verify that the odd-order terms in Eq. (7.12) take the forms displayed in Eqs. (7.15), modulo surface terms.

7.3 In this problem we prove that at first post-Newtonian order, the integral of Eq. (7.59) defining the total mass $M$ is insensitive to the wave-zone aspects of the integrand. To show this, decompose the integral into a near-zone portion $r < \mathcal { R }$ and a wave zone portion $r > \mathcal { R }$ . Show that the $\partial _ { j } ( U \partial ^ { j } U )$ term in the energy-momentum pseudotensor makes a contribution

$$
\Delta M _ { \mathrm { n e a r } } = \frac { 7 G } { 2 c ^ { 2 } } \frac { M ^ { 2 } } { \mathcal { R } }
$$

to the near-zone integral. Next, use the expression of Eq. (7.110) to show that the wave-zone contribution to the mass is given by

$$
\Delta M _ { \mathrm { w a v e } } = - \frac { 7 G } { 2 c ^ { 2 } } \frac { M ^ { 2 } } { \mathcal { R } } .
$$

Conclude that these contributions cancel out, and that the wave-zone portion of the integral makes no essential contribution to the mass.

7.4 As we saw in Sec. 7.3.3, the Poisson equation $\nabla ^ { 2 } f = \nabla ^ { 2 } g$ has the solution

$$
f = g - \frac { 1 } { 4 \pi } \oint _ { \partial \mathcal { M } } \left( \frac { \partial ^ { \prime } \boldsymbol { j } ^ { \prime } g ^ { \prime } } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } - g ^ { \prime } \partial _ { \boldsymbol { j } } ^ { \prime } \frac { 1 } { | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | } \right) d S _ { \boldsymbol { j } } ^ { \prime } .
$$

Show that the surface term satisfies Laplace’s equation for any point $\boldsymbol { x }$ within the near zone.

7.5 Consider the superduperpotential of $\rho ^ { * }$ , defined by

$$
Y ( t , \pmb { x } ) : = G \int \rho ^ { * } ( t , \pmb { x } ^ { \prime } ) | \pmb { x } - \pmb { x } ^ { \prime } | ^ { 3 } d ^ { 3 } \pmb { x } ^ { \prime } .
$$

(a) Show that $\nabla ^ { 2 } Y = 1 2 X$ , where $X$ is the superpotential.

(b) Following the method of Box 7.3, show that the solution to $\nabla ^ { 2 } Y = 1 2 X$ can be expressed as

$$
Y ( t , { \pmb x } ) = G \int \rho ^ { * } ( t , { \pmb y } ) K ( { \pmb x } ; { \pmb y } ) d ^ { 3 } y + Y _ { 0 } ( t , { \pmb x } ) ,
$$

in terms of a two-point function $K$ that satisfies $\nabla ^ { 2 } K = 1 2 | \pmb { x } - \pmb { y } | ; ~ Y _ { 0 }$ is a solution to Laplace’s equation.

(c) Calculate the two-point function, and determine $Y _ { 0 }$ so that your answer for $Y$ agrees with its starting definition.

7.6 Show that the quadrupole-moment piece of the wave-zone potential $h ^ { 0 0 }$ in $\mathrm { B o x } 7 . 7$ is given explicitly by

$$
\frac { 2 G } { c ^ { 2 } } \bigg ( \frac { 1 } { c ^ { 2 } r } \ddot { \mathcal { Z } } ^ { j k } + \frac { 3 } { c r ^ { 2 } } \dot { \mathcal { Z } } ^ { \langle j k \rangle } + \frac { 3 } { r ^ { 3 } } \mathcal { Z } ^ { \langle j k \rangle } \bigg ) n _ { j } n _ { k } .
$$

7.7 For a static, spherically-symmetric source, show that the wave-zone potentials given in $\mathrm { B o x } 7 . 7$ reduce to

$$
\begin{array} { l } { { \displaystyle h ^ { 0 0 } = \frac { 4 G M } { c ^ { 2 } r } + 7 \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } + \cdots , } } \\ { { \displaystyle h ^ { 0 j } = 0 , } } \\ { { \displaystyle h ^ { j k } = \bigg ( \frac { G M } { c ^ { 2 } r } \bigg ) ^ { 2 } n ^ { j } n ^ { k } + \cdots } } \end{array}
$$

Verify that this corresponds to the post-Newtonian expansion of the Schwarzschild metric in harmonic coordinates.

7.8 The total mass of a gravitating system is defined by the integral

$$
{ \cal M } = { \frac { 1 } { c ^ { 2 } } } \int ( - g ) \big ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } \big ) d ^ { 3 } x \ .
$$

But the mass parameter that appears in the leading-order contribution to $h ^ { 0 0 }$ in the wave zone is

$$
M _ { 0 } = { \frac { 1 } { c ^ { 2 } } } \int _ { \mathcal { M } } ( - g ) \bigl ( T ^ { 0 0 } + t _ { \mathrm { L L } } ^ { 0 0 } + t _ { \mathrm { H } } ^ { 0 0 } \bigr ) d ^ { 3 } x \ .
$$

Both masses satisfy a conservation law, because $\partial _ { \beta } [ ( - g ) t _ { \mathrm { H } } ^ { \alpha \beta } ] = 0$ identically. This problem explores whether $( - g ) t _ { \mathrm { H } } ^ { 0 0 }$ makes a contribution to the value of the mass.

(a) Defining $\widetilde { t } _ { \mathrm { H } } ^ { \alpha \beta } : = ( 1 6 \pi G / c ^ { 4 } ) \widetilde { ( - g ) } \widetilde { t } _ { \mathrm { H } } ^ { \alpha \beta } = \partial _ { \mu } h ^ { \alpha \nu } \partial _ { \nu } h ^ { \beta \mu } - h ^ { \mu \nu } \partial _ { \mu \nu } h ^ { \alpha \beta }$ , and using the harmonic gauge condition $\partial _ { \beta } h ^ { \alpha \beta } = 0$ , show that

$$
\begin{array} { r l r } & { } & { \tilde { t } _ { \mathrm { H } } ^ { \alpha \beta } = 2 \partial _ { 0 } h ^ { \alpha 0 } \partial _ { 0 } h ^ { \beta 0 } + 2 h ^ { 0 ( \alpha } \partial _ { 0 } ^ { 2 } h ^ { \beta ) 0 } - h ^ { 0 0 } \partial _ { 0 } ^ { 2 } h ^ { \alpha \beta } } \\ & { } & { - 2 \partial _ { 0 } h ^ { 0 0 } \partial _ { 0 } h ^ { \alpha \beta } - h ^ { \alpha \beta } \partial _ { 0 } ^ { 2 } h ^ { 0 0 } + \partial _ { j } f ^ { j \alpha \beta } , } \end{array}
$$

where

$$
\begin{array} { r } { f ^ { j \alpha \beta } : = 2 h ^ { 0 ( \alpha } \partial _ { 0 } h ^ { \beta ) j } + h ^ { k ( \alpha } \partial _ { k } h ^ { \beta ) j } + h ^ { j ( \alpha } \partial _ { 0 } h ^ { \beta ) 0 } } \\ { - 2 h ^ { 0 j } \partial _ { 0 } h ^ { \alpha \beta } - h ^ { j k } \partial _ { k } h ^ { \alpha \beta } - \partial _ { 0 } h ^ { 0 j } h ^ { \alpha \beta } . } \end{array}
$$

(b) Using this expression, show that the contribution of the harmonic energymomentum pseudotensor to a near-zone momentum

$$
P _ { 0 } ^ { \alpha } : = \frac { 1 } { c } \int _ { \mathcal { M } } \tau ^ { \alpha 0 } d ^ { 3 } x
$$

and a near-zone angular momentum

$$
J _ { 0 } ^ { \alpha \beta } : = \frac { 2 } { c } \int _ { \mathcal { M } } x ^ { [ \alpha } \tau ^ { \beta ] 0 } d ^ { 3 } x
$$

comes from integrals over the surface bounding the domain of integration.

(c) Show that $f ^ { j 0 0 } = \partial _ { k } ( h ^ { 0 j } h ^ { 0 k } - h ^ { 0 0 } h ^ { j k } )$

(d) Using the wave-zone form of the potentials from Box 7.7, and keeping only terms that are independent of the cutoff radius $\mathcal { R }$ , show that $M$ and $M _ { 0 }$ are related by

$$
{ \cal M } = { \cal M } _ { 0 } - \frac { 2 } { 3 } \frac { G { \cal M } _ { 0 } } { c ^ { 5 } } \dddot { \cal \underline { { { X } } } } { ^ { k k } } ( \tau ) + { \cal O } ( c ^ { - 7 } ) .
$$

Show that the second term is a correction of order $( v _ { c } / c ) ^ { 5 }$ relative to the first term.

7.9 This problem explores how to solve the Landau–Lifshitz formulation of the Einstein field equations for the Schwarzschild geometry.

(a) Assuming static spherical symmetry, show that the general form of the gothic inverse metric in Cartesian coordinates can be written in the form

$$
\begin{array} { l } { { { \mathfrak { g } } ^ { 0 0 } = N ( r ) , } } \\ { { { \mathfrak { g } } ^ { 0 j } = 0 , } } \\ { { { \mathfrak { g } } ^ { j k } = \alpha ( r ) P ^ { j k } + \beta ( r ) n ^ { j } n ^ { k } , } } \end{array}
$$

where $N , \alpha$ and $\beta$ are arbitrary functions of $r , n ^ { j }$ is a radial unit vector, and $P ^ { j k } : = \delta ^ { j k } - n ^ { j } n ^ { k }$ .

(b) Show that ${ \mathfrak { g } } _ { \alpha \beta }$ is given by ${ \mathfrak { g } } _ { 0 0 } = N ^ { - 1 }$ , ${ \mathfrak { g } } _ { j k } = \alpha ^ { - 1 } P ^ { j k } + \beta ^ { - 1 } n ^ { j } n ^ { k }$ , and that ${ \mathfrak { g } } : =$ $\operatorname* { d e t } [ { \mathfrak { g } } ^ { \alpha \beta } ] = N \alpha ^ { 2 } \beta$ .

g(c) Show that the imposition of the harmonic gauge condition leads to the constraint

$$
\beta ^ { \prime } = { \frac { 2 } { r } } ( \alpha - \beta ) ,
$$

where a prime indicates differentiation with respect to $r$ . Recall that $\partial ^ { j } F ( r ) =$ $F ^ { \prime } ( r ) n ^ { j }$ , and $\partial ^ { j } n ^ { k } = r ^ { - 1 } P ^ { j k }$ .

(d) Show that the three field equations that arise from the vacuum wave equation $\Pi { \mathfrak { g } } ^ { \alpha \beta } = ( 1 6 \pi G / c ^ { 4 } ) \tau ^ { \alpha \beta }$ in harmonic coordinates have the form

$$
\begin{array} { c } { { X ^ { \prime } + X Y + \displaystyle \frac { 1 } { r } ( 2 X - Y ) = \cal Q , } } \\ { { { } } } \\ { { X Y + \displaystyle \frac { 1 } { r } ( 2 X + Y ) = - \cal Q , } } \\ { { { } } } \\ { { Z ^ { \prime } + Y Z + \displaystyle \frac { 2 } { r } Z = \cal Q , } } \end{array}
$$

where

$$
X : = \frac { \alpha ^ { \prime } } { \alpha } , \quad Y : = \frac { \beta ^ { \prime } } { \beta } , \quad Z : = \frac { N ^ { \prime } } { N } ,
$$

and

$$
\displaystyle Q : = \frac { 1 } { 8 } \Bigl ( 3 Y ^ { 2 } - Z ^ { 2 } + 2 Y Z + 4 X Z - 4 X Y \Bigr ) .
$$

Hint: One equation comes from the 00 component of the field equations, the other two come from splitting the $j k$ components into a piece proportional to $n ^ { j } n ^ { k }$ and another piece proportional to $P ^ { j k }$ . Use the gauge condition to simplify your expressions.

(e) By combining the first two field equations, obtain the solutions

$$
X = 0 \quad { \mathrm { o r } } \quad r ^ { 4 } \beta ^ { 2 } X = c ,
$$

where $c \neq 0$ is a constant.

(f) Choosing the solution $X = 0$ , show that the solutions for $\alpha$ and $\beta$ that satisfy appropriate asymptotic conditions at $r = \infty$ are

$$
\alpha = 1 , \beta = 1 - \frac { a } { r ^ { 2 } } ,
$$

where $a$ is an arbitrary constant. Find the solution for $N$ , determine $a$ , and verify that the result is the Schwarzschild metric in harmonic coordinates.

(g) What is your interpretation of the second class of solutions, represented by a nonzero value of $c ?$ Show that by combining the equation $r ^ { 4 } \beta ^ { 2 } X = c$ with the gauge condition, you can eliminate $\alpha$ and obtain the following differential equation for $\beta$ :

$$
W ^ { \prime \prime } - \frac { W ^ { \prime } } { r } = c \frac { W ^ { \prime } } { W ^ { 2 } } ,
$$

where $W : = r ^ { 2 } \beta$ . Spend some time (but not too much!) trying to find a closed form solution to this non-linear equation. (If you find one, please send it to us!)

7.10 Consider the harmonic gauge condition of Eq. (5.175), $\begin{array} { r } { \boxed { \vphantom { \bigg | } } _ { g } X ^ { ( \mu ) } = 0 } \end{array}$ , which is a scalar wave equation for the four scalar fields $T , X , Y$ and $Z$ . Using the metric in Schwarzschild coordinates to calculate the operator $\Pi _ { g }$ , and defining $T : = t , X : =$ $r _ { \mathrm { h } } ( r ) \sin \theta \cos \phi$ , $Y : = r _ { \mathrm { h } } ( r ) \sin \theta \sin \phi$ , and $Z : = r _ { \mathrm { h } } ( r ) \cos \theta$ , show that the harmonic condition reduces to a single differential equation for $r _ { \mathrm { h } } ( r )$ , a Legendre equation of degree $\ell = 1$ . Show that the solution that satisfies the condition that $r _ { \mathrm { h } }  r$ as $r  \infty$ is given by

$$
r _ { \mathrm { h } } = r - \frac { 1 } { 2 } R + b \bigg [ \Big ( r - \frac { 1 } { 2 } R \Big ) \ln \Big ( 1 - \frac { R } { r } \Big ) + R \bigg ] ,
$$

where $R = 2 G M / c ^ { 2 }$ and $^ b$ is an arbitrary constant. What do you conclude about the uniqueness of harmonic coordinates? (We encounter this question again in Sec. 11.1.5, in the context of gravitational waves.) Is there a link between this and the second class of solutions in part (g) of the previous problem?

Post-Newtonian theory is the theory of weak-field gravity within the near zone, and of the slowly moving systems that generate it and respond to it. It was first encountered in Chapter 7, where it was embedded within the post-Minkowskian approximation; the idea relies on the slow-motion condition introduced in Sec. 6.3.2. But while post-Minkowskian theory deals with both the near and wave zone, here we focus exclusively on the near zone. In this chapter we develop the post-Newtonian theory systematically.

We begin in Sec. 8.1 by collecting the main ingredients obtained in Chapter 7, including the near-zone metric to 1pn order and the matter’s energy-momentum tensor $T ^ { \alpha \beta }$ . In Sec. 8.2 we present an alternative derivation of the post-Newtonian metric, based on the Einstein equations in their standard form; this is the “classic approach” to post-Newtonian theory, adopted by Einstein, Infeld, and Hoffmann in the 1930s, and by Fock, Chandrasekhar, and others in the 1960s. Although it produces the same results, we will see that the classic approach presents us with a number of ambiguities that are not present in the post-Minkowskian approach. In Sec. 8.3 we explore the coordinate freedom of post-Newtonian theory, and construct the most general transformation that preserves the post-Newtonian expansion of the metric. And in Sec. 8.4 we derive the laws of fluid dynamics in post-Newtonian theory; these will be applied to the motion of an $N$ -body system in Chapter 9.

# 8.1 Equations of post-Newtonian theory

# 8.1.1 Post-Newtonian metric

We restrict our attention to a matter distribution that is subjected to a slow-motion condition of the sort first considered in Sec. 6.3.2. The distribution is characterized by a length scale $r _ { c }$ and a time scale $t _ { c }$ , and these give us the characteristic velocity $v _ { c } : = r _ { c } / t _ { c }$ . We assume that this is much smaller than the speed of light,

$$
v _ { c } / c \ll 1 ,
$$

and this defines what we mean by the slow-motion condition: all speeds within the matter distribution (such as the speed of sound within a body, or the speed of the body as a whole) shall be small compared with the speed of light. If $\lambda _ { c } : = c t _ { c }$ is a characteristic wavelength of the gravitational radiation produced by the matter distribution, then Eq. (8.1) states that $r _ { c } \ll \lambda _ { c }$ . The region of space occupied by the matter is therefore small compared with the characteristic wavelength; the matter is situated deep within the near-zone region of spacetime, defined by $r : = | \pmb { x } | \ll \lambda _ { c }$ .

Incorporating these assumptions, focusing on field points within the near zone, and carrying out two iterations of the relaxed field equations, we obtained the spacetime metric of a post-Newtonian system back in Sec. 7.3. The metric is displayed in Eq. (7.105), and we reproduce it here:

$$
\begin{array} { l } { { g _ { 0 0 } = - 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U + \displaystyle \frac { 2 } { c ^ { 4 } } \left( \Psi - U ^ { 2 } \right) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle g _ { 0 j } = - \displaystyle \frac { 4 } { c ^ { 3 } } U _ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle g _ { j k } = \delta _ { j k } \left( 1 + \displaystyle \frac { 2 } { c ^ { 2 } } U \right) + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where

$$
\Psi : = \psi + \frac { 1 } { 2 } \partial _ { t t } X .
$$

The potentials that appear in the metric are defined by

$$
\begin{array} { l } { { U ( t , x ) : = G \displaystyle \int \displaystyle \frac { \rho ^ { \ast \prime } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \\ { { \displaystyle \psi ( t , x ) : = G \displaystyle \int \displaystyle \frac { \rho ^ { \ast \prime } \big ( \frac { 3 } { 2 } v ^ { 2 } - U ^ { \prime } + \Pi ^ { \prime } + 3 p ^ { \prime } / \rho ^ { \ast \prime } \big ) } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \\ { { X ( t , x ) : = G \displaystyle \int \rho ^ { \ast \prime } | x - x ^ { \prime } | d ^ { 3 } x ^ { \prime } , } } \\ { { U ^ { j } ( t , x ) : = G \displaystyle \int \displaystyle \frac { \rho ^ { \ast } v ^ { \prime } / } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } , } } \end{array}
$$

in which the primed fluid variables are evaluated at time $t$ and position $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ ; these are determined by the equations of fluid dynamics to be derived in Sec. 8.4. As in the Newtonian theory, the dynamics of the fluid and the dynamics of the gravitational field are intimately coupled to each other. It should be noted that the potentials of Eqs. (8.4) are all instantaneous potentials: their profile at time $t$ depends on the state of the system at the same time. The metric, however, does incorporate retardation effects that arise from solving the wave equation for the gravitational potentials $h ^ { \alpha \beta }$ ; these are captured by the superpotential term $\partial _ { t t } { X }$ in $g _ { 0 0 }$ , which appears when $h ^ { 0 0 }$ is expanded in powers of $c ^ { - 2 }$ within the near zone.

The post-Newtonian metric makes a good approximation to the true spacetime metric in the near zone only; the approximation is not valid beyond $r = \lambda _ { c }$ . The reason for this limitation has already been invoked in Box 6.6. It has to do with the fact that while the behavior of the metric in the near zone is directly tied to the behavior of the matter, so that the metric varies slowly when the matter moves slowly, this is not so in the wave zone, where the radiative behavior of the metric asserts itself. Mathematically, the slow behavior of the metric in the near zone is expressed by the equation

$$
\partial _ { 0 } g _ { \alpha \beta } \sim \frac { v _ { c } } { c } \partial _ { j } g _ { \alpha \beta } ,
$$

which states that derivatives with respect to $x ^ { 0 } : = c t$ are smaller than spatial derivatives by a factor of order $v _ { c } / c \ll 1$ . If we imagine, for example, a matter distribution that consists of $N$ isolated bodies with positions $\pmb { r } _ { A } ( t )$ , then the metric will depend on time through the $N$ position vectors, and temporal derivatives will be generated by spatial differentiation followed by differentiation of $\pmb { r } _ { A } ( t )$ with respect to time; and we see that these operations do indeed bring out the additional factors of $v _ { c } / c$ . The situation is very different in the wave zone, because of the radiative nature of the metric when $r > \lambda _ { c }$ . Here the characteristic velocity of the field becomes the speed of light, and it is no longer related to the matter’s velocity scale. As a result, $\partial _ { 0 } g _ { \alpha \beta }$ is of the same order of magnitude as the spatial derivatives, and the slow-motion condition no longer has the same effect on the behavior of the metric.

# 8.1.2 Energy-momentum tensor

The metric of Eq. (8.2) was constructed from potentials $h _ { 2 } ^ { \alpha \beta }$ obtained after two iterations of the relaxed Einstein equations. These potentials can then be involved in a computation of $\tau _ { 2 } ^ { \alpha \beta }$ , the effective energy-momentum pseudotensor, which can be substituted into the conservation statement $\partial _ { \beta } \tau _ { 2 } ^ { \alpha \beta } = 0$ to obtain the system’s equations of motion. But since this conservation statement is formally equivalent to the covariant expression of energymomentum conservation, $\nabla _ { \beta } T ^ { \alpha \beta } = 0$ , an alternative method to obtain the equations of motion is to compute $T ^ { \alpha \beta }$ to the required degree of accuracy, and to insert it within the covariant equation. This alternative method turns out to be simpler to implement than the original one involving $\tau _ { 2 } ^ { \alpha \beta }$ .

This program will be implemented in Sec. 8.4. In preparation for this discussion, we now compute $T ^ { \alpha \beta }$ to the required post-Newtonian order. We recall that

$$
T ^ { \alpha \beta } = ( \rho + \epsilon / c ^ { 2 } + p / c ^ { 2 } ) u ^ { \alpha } u ^ { \beta } + p g ^ { \alpha \beta } ,
$$

that $\rho = \rho ^ { * } ( 1 - v ^ { 2 } / 2 c ^ { 2 } - 3 U / c ^ { 2 } ) + { \cal O } ( c ^ { - 4 } )$ and that $u ^ { \alpha } = \gamma ( c , \pmb { v } )$ , with $\gamma : = u ^ { 0 } / c = 1 +$ $v ^ { 2 } / 2 c ^ { 2 } + U / c ^ { 2 } + { \cal O } ( c ^ { - 4 } )$ . These relations give us

$$
\begin{array} { c } { { c ^ { - 2 } T ^ { 0 0 } = \rho ^ { * } \biggl [ 1 + \displaystyle \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - U + \Pi \Bigr ) \biggr ] + { \cal O } ( c ^ { - 4 } ) , } } \\ { { { } } } \\ { { c ^ { - 1 } T ^ { 0 j } = \rho ^ { * } v ^ { j } \biggl [ 1 + \displaystyle \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - U + \Pi + p / \rho ^ { * } \Bigr ) \biggr ] + { \cal O } ( c ^ { - 4 } ) , } } \\ { { { } } } \\ { { { \cal T } ^ { j k } = \rho ^ { * } v ^ { j } v ^ { k } \biggl [ 1 + \displaystyle \frac { 1 } { c ^ { 2 } } \Bigl ( \frac { 1 } { 2 } v ^ { 2 } - U + \Pi + p / \rho ^ { * } \Bigr ) \biggr ] + p \biggl ( 1 - \displaystyle \frac { 2 } { c ^ { 2 } } U \biggr ) \delta ^ { j k } } } \\ { { { } } } \\ { { { } ~ + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where $\Pi : = \epsilon / \rho ^ { * }$ . Note that $T ^ { 0 0 }$ is expanded to order $c ^ { 0 }$ , $T ^ { 0 j }$ to order $c ^ { - 1 }$ , and $T ^ { j k }$ to order $c ^ { - 2 }$ . The metric, on the other hand, is expanded to order $c ^ { - 4 }$ for $g _ { 0 0 } , c ^ { - 3 }$ for $g _ { 0 j }$ , and $c ^ { - 2 }$ for $g _ { j k }$ . As expressed here, the components of the energy-momentum tensor follow a reversed hierarchy of post-Newtonian orders compared to the components of the metric. The reason for this is that each component of the energy-momentum tensor must contain a leadingorder piece and a post-Newtonian correction if it is to yield useful information at 1pn order. This is because the components will be inserted within the conservation equations, which take the schematic form $c ^ { - 1 } \partial _ { t } T ^ { \alpha 0 } \approx - \partial _ { k } T ^ { \alpha k }$ ; while the leading-order pieces will deliver the system’s Newtonian dynamics, it is the post-Newtonian corrections that will deliver the post-Newtonian dynamics.

# 8.1.3 Auxiliary potentials

For future reference we list here a number of post-Newtonian potentials that can also be associated with a perfect fluid; some appear in the potential $\psi$ , while others will be used later in this chapter:

$$
\begin{array} { r l } & { \Phi _ { 1 } : = G \int \frac { \rho ^ { s } \nu ^ { 2 } } { | x - x ^ { 2 } | ^ { d } } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 2 } : = G \int \frac { \rho ^ { s } \nu ^ { 2 } \nu ^ { 2 } } { | x - x ^ { 2 } | ^ { d } } d x ^ { \prime } , } \\ & { \Phi _ { 3 } : = G \int \frac { \rho ^ { s } \nu ^ { 2 } } { | x - x ^ { 2 } | ^ { d } } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 4 } : = G \int \frac { \rho ^ { s } } { | x - x ^ { 2 } | ^ { d } } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 5 } : = G \int \rho ^ { s } \nu ^ { 2 } \nu \frac { \nu ^ { 2 } } { | x - x ^ { 2 } | ^ { d } } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 5 } : = G \int \rho ^ { s } \nu _ { x } ^ { 2 } \nu \frac { ( x - x ^ { 2 } ) ^ { s } } { | x - x ^ { 2 } | ^ { d } } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi _ { 5 } : = G \int \rho ^ { s } \nu _ { x } ^ { 2 } \nu \frac { ( x - x ^ { 2 } ) ^ { s } ( x - x ^ { 2 } ) ^ { s } } { | x - x ^ { 2 } | ^ { s } } d ^ { 3 } x ^ { \prime } , } \\ & { \Phi ^ { \prime } : = G \int \rho ^ { s } \nu _ { x } ^ { 4 } \frac { ( x - x ^ { 2 } ) ^ { s } ( x - x ^ { 2 } ) ^ { s } } { | x - x ^ { 2 } | ^ { s } } d ^ { 3 } x ^ { \prime } . } \end{array}
$$

Again a primed variable such as $\rho ^ { * \prime }$ stands for $\rho ^ { * } ( t , x ^ { \prime } )$ , and $\partial _ { j ^ { \prime } } U ^ { \prime }$ stands for the partial derivative of $U ( t , { \boldsymbol { x } } ^ { \prime } )$ with respect to $x ^ { \prime j }$ .

Referring to Eq. (8.4b), we see immediately that

$$
\psi = \frac { 3 } { 2 } \Phi _ { 1 } - \Phi _ { 2 } + \Phi _ { 3 } + 3 \Phi _ { 4 } .
$$

In Sec. 8.4.4 we shall have occasion to prove that

$$
\begin{array} { r l } & { \partial _ { t j } X = \Phi _ { j } - U _ { j } , } \\ & { \partial _ { t t } X = \Phi _ { 1 } + 2 \Phi _ { 4 } - \Phi _ { 5 } - \Phi _ { 6 } . } \end{array}
$$

Another useful identity is

$$
\partial _ { j k } X = \delta _ { j k } U - G \int \rho ^ { * \prime } { \frac { ( x - x ^ { \prime } ) ^ { j } ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | ^ { 3 } } } d ^ { 3 } x ^ { \prime } .
$$

This equation follows directly from the definition of the superpotential, and taking its trace confirms that $\nabla ^ { 2 } X = 2 U$ . Combining Eqs. (8.3), (8.9), and (8.10b), we arrive at

$$
\Psi = 2 \Phi _ { 1 } - \Phi _ { 2 } + \Phi _ { 3 } + 4 \Phi _ { 4 } - \frac { 1 } { 2 } \Phi _ { 5 } - \frac { 1 } { 2 } \Phi _ { 6 } ,
$$

a useful decomposition of the post-Newtonian potential $\Psi$ in terms of the auxiliary potentials.

# 8.1.4 Geodesic equations

To conclude this section we derive the form of the geodesic equation that governs the motion of a test particle in the post-Newtonian spacetime. We examine both the case of a test body that moves slowly $( v / c \ll 1 )$ , and the case of a massless particle (such as a photon) that moves rapidly $( v / c \simeq 1 )$ .

In either case the geodesic equation is

$$
\frac { d ^ { 2 } r ^ { \alpha } } { d \lambda ^ { 2 } } + \Gamma _ { \beta \gamma } ^ { \alpha } \frac { d r ^ { \beta } } { d \lambda } \frac { d r ^ { \gamma } } { d \lambda } = 0 ,
$$

in which $r ^ { \alpha } ( \lambda )$ describes the particle’s world line in spacetime; the parameter $\lambda$ is proper time $\tau$ in the case of a massive body, and an arbitrary affine parameter in the case of a photon. For our purposes it is useful to alter the parameterization of the world line and adopt the time coordinate $t : = x ^ { 0 } / c$ instead of $\lambda$ . There is a practical reason for this change: the motion of a planet or spacecraft, or the trajectory of a light ray in space, is generally tracked by an external observer who employs a clock that measures external time $t$ instead of the planet’s proper time $\lambda$ ; a description of the motion in terms of $t$ is therefore much more useful to this observer. (We shall return to this theme in Chapter 10, and give a more precise description of the relation between $t$ and the observer’s clock time.) A straightforward application of the chain rule reveals that the geodesic equation becomes

$$
\frac { d v ^ { \alpha } } { d t } = - \bigg ( \Gamma _ { \beta \gamma } ^ { \alpha } - \frac { v ^ { \alpha } } { c } \Gamma _ { \beta \gamma } ^ { 0 } \bigg ) v ^ { \beta } v ^ { \gamma }
$$

when the world line is parameterized by $t$ ; here $v ^ { \alpha } : = d r ^ { \alpha } / d t = ( c , \pmb { v } )$ . The time component of Eq. (8.14) returns $0 = 0$ , and the motion of the particle is completely determined by the spatial components.

The Christoffel symbols required for the geodesic equation are obtained from Eq. (8.2), which we insert into Eq. (5.34). We get

$$
\begin{array} { l } { { \Gamma _ { 0 0 } ^ { 0 } = - \displaystyle \frac { 1 } { c ^ { 3 } } \partial _ { t } U + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \Gamma _ { 0 j } ^ { 0 } = - \displaystyle \frac { 1 } { c ^ { 2 } } \partial _ { j } U + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \Gamma _ { j k } ^ { 0 } = \displaystyle \frac { 2 } { c ^ { 3 } } \big ( \partial _ { j } U _ { k } + \partial _ { k } U _ { j } \big ) + \displaystyle \frac { 1 } { c ^ { 3 } } \delta _ { j k } \partial _ { t } U + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \Gamma _ { 0 0 } ^ { j } = - \displaystyle \frac { 1 } { c ^ { 2 } } \partial _ { j } U - \displaystyle \frac { 1 } { c ^ { 4 } } \big ( 4 \partial _ { j } U _ { j } + \partial _ { j } \Psi - 4 U \partial _ { j } U \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \Gamma _ { 0 k } ^ { j } = \displaystyle \frac { 1 } { c ^ { 3 } } \partial _ { j k } \partial _ { t } U - \displaystyle \frac { 2 } { c ^ { 3 } } \big ( \partial _ { k } U _ { j } - \partial _ { j } U _ { k } \big ) + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \Gamma _ { k n } ^ { j } = \displaystyle \frac { 1 } { c ^ { 2 } } \big ( \partial _ { j n } \partial _ { k } U + \partial _ { j k } \partial _ { n } U - \delta _ { k n } \partial _ { j } U \big ) + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

and making the substitution within Eq. (8.14), we obtain

$$
\begin{array} { c } { { \displaystyle { \frac { d v ^ { j } } { d t } } = \partial _ { j } U + \frac { 1 } { c ^ { 2 } } \bigg [ ( v ^ { 2 } - 4 U ) \partial _ { j } U - \big ( 4 v ^ { k } \partial _ { k } U + 3 \partial _ { t } U \big ) v ^ { j } } } \\ { { - 4 v ^ { k } \big ( \partial _ { j } U _ { k } - \partial _ { k } U _ { j } \big ) + 4 \partial _ { t } U _ { j } + \partial _ { j } \Psi \bigg ] + { \cal O } ( c ^ { - 4 } ) } } \end{array}
$$

when the particle is a massive body that moves slowly, so that $v / c \ll 1$ . In the first term we recognize the Newtonian acceleration field $\partial _ { j } U$ , and the remaining terms are post-Newtonian corrections. The 1pn terms are suppressed by factors of order $( v / c ) ^ { 2 }$ , $v v _ { c } / c ^ { 2 }$ , or $( v _ { c } / c ) ^ { 2 }$ , where $v$ is the magnitude of the particle’s velocity, while $v _ { c }$ is the characteristic velocity scale of the matter distribution. For example $\partial _ { t } U$ is of order $v _ { c }$ relative to $\partial _ { j } U$ , and this is multiplied by $v ^ { j } / c ^ { 2 }$ in the equations of motion; the contribution is therefore of order $v v _ { c } / c ^ { 2 }$ .

In the case of a photon we cannot take $v$ to be much smaller than $c$ , and the geodesic equation permits an expansion in powers of $v _ { c } / c$ only. The magnitude of $\pmb { v }$ can be determined from the lightlike condition $g _ { \alpha \beta } v ^ { \alpha } v ^ { \beta } = 0 .$ . To leading order in the post-Newtonian expansion we find that $( v / c ) ^ { 2 } = 1 - 4 U / c ^ { 2 }$ , and this relation neglects terms of order $v _ { c } U / c ^ { 3 }$ . This implies that $\pmb { v }$ can be expressed as

$$
\pmb { v } = c \Big ( 1 - \frac { 2 } { c ^ { 2 } } U \Big ) \pmb { n } + O ( c ^ { - 3 } ) ,
$$

in terms of a unit vector $\pmb { n }$ . This equation reveals that the coordinate velocity of a photon deviates from $c$ in curved spacetime. If we take $v / c$ to be of order unity but continue to treat $v _ { c } / c$ as a small quantity, Eq. (8.14) produces

$$
\frac { d v ^ { j } } { d t } = \bigg ( 1 + \frac { v ^ { 2 } } { c ^ { 2 } } \bigg ) \partial _ { j } U - \frac { 4 } { c ^ { 2 } } v ^ { j } v ^ { k } \partial _ { k } U + O ( c ^ { - 3 } ) .
$$

The geodesic equation becomes

$$
\frac { d n ^ { j } } { d t } = \frac { 2 } { c } \big ( \delta ^ { j k } - n ^ { j } n ^ { k } \big ) \partial _ { k } U + O ( c ^ { - 2 } )
$$

after making the substitution of Eq. (8.17). We note that the right-hand side of Eq. (8.19) is orthogonal to $n _ { j }$ ; this is as it should be, because $n _ { j } d n ^ { j } / d t = \textstyle { \frac { 1 } { 2 } } d ( n _ { j } n ^ { j } ) / d t = 0$ .

# Box 8.1 Maxwell-like formulation of post-Newtonian theory

The main equations of post-Newtonian theory can be written in a form that displays a remarkable parallel with the equations of electrodynamics. These consist of Maxwell’s equations,

$$
\begin{array} { l } { \displaystyle \nabla \cdot \boldsymbol { E } = \frac { 1 } { \epsilon _ { 0 } } \rho _ { e } , } \\ { \displaystyle \nabla \cdot \boldsymbol { B } = 0 , } \\ { \displaystyle \nabla \times \boldsymbol { E } = - \partial _ { t } \boldsymbol { B } , } \\ { \displaystyle \nabla \times \boldsymbol { B } = \frac { 1 } { c ^ { 2 } } \biggl ( \frac { 1 } { \epsilon _ { 0 } } j _ { e } + \partial _ { t } \boldsymbol { E } \biggr ) , } \end{array}
$$

which govern the behavior of the electric field $E$ and magnetic field $\pmb { B }$ in terms of the charge density $\rho _ { e } =$ $c ^ { - 1 } j _ { e } ^ { 0 }$ and the current density $j _ { e }$ , and the Lorentz-force law

$$
m \frac { d ( \gamma \pmb { v } ) } { d t } = q \big ( \pmb { E } + \pmb { v } \times \pmb { B } \big ) ,
$$

with $\gamma = d t / d \tau$ , which governs the behavior of a particle of mass m, charge $q$ , and velocity $\pmb { v }$ in the electromagnetic field.

From the post-Newtonian metric (8.2), we first define a gravito-electric potential $\begin{array} { r } { \Phi _ { \mathrm { g } } : = - \frac { 1 } { 2 } c ^ { 2 } ( 1 + } \end{array}$ $g _ { 0 0 } ) = - U - c ^ { - 2 } ( \Phi - U ^ { 2 } ) + O ( c ^ { - 4 } )$ and a gravito-magnetic potential $A _ { \mathrm { g } }$ with components $c g _ { 0 j } = - 4 c ^ { - 2 } U _ { j } + { \cal O } ( c ^ { - 4 } )$ . We next define a gravito-electric field $E _ { \mathrm { g } } : = - \nabla \Phi _ { \mathrm { g } } -$ $\partial _ { t } A _ { g } = \nabla U + c ^ { - 2 } ( \nabla \Psi - \nabla U ^ { 2 } + 4 \partial _ { t } U )$ and a gravito-magnetic field $\pmb { { \cal B } } _ { \mathrm { g } } : = \nabla \times { \cal A } _ { \mathrm { g } } =$ $- 4 c ^ { - 2 } \nabla \times \pmb { U } _ { \parallel }$ the relations between potentials and fields are the same as in electrodynamics. It is then a simple matter to show that the field equations of post-Newtonian theory can be put in the Maxwell-like form

$$
\begin{array} { r l } & { \tilde { \nabla } \cdot \boldsymbol { E } _ { \mathrm { g } } = - 4 \pi G \rho ^ { * } \bigg [ 1 + \cfrac { 1 } { c ^ { 2 } } \bigg ( \frac 3 2 v ^ { 2 } - 3 U + \Pi + 3 p / \rho ^ { * } \bigg ) \bigg ] - \frac 3 { c ^ { 2 } } \partial _ { t t } U + O ( c ^ { - 4 } ) , } \\ & { \nabla \cdot B _ { \mathrm { g } } = O ( c ^ { - 4 } ) , } \\ & { \nabla \times \boldsymbol { E } _ { \mathrm { g } } = - \partial _ { t } B _ { \mathrm { g } } , } \\ & { \nabla \times B _ { \mathrm { g } } = \frac 4 { c ^ { 2 } } \Big ( - 4 \pi G \rho ^ { * } v + \partial _ { t } E _ { \mathrm { g } } \Big ) + O ( c ^ { - 4 } ) , } \end{array}
$$

where $\tilde { \nabla } \cdot E _ { \mathrm { g } }$ denotes a “curved-space” divergence $( - g ) ^ { - 1 / 2 } \nabla [ ( - g ) ^ { 1 / 2 } E _ { \mathrm { g } } ] ,$ where $- g = 1 +$ $2 { U } / { c ^ { 2 } } + { O } ( { c ^ { - 4 } } )$ is the determinant of the post-Newtonian metric. It is also simple to show that the geodesic equation acquires a Lorentz-like form

$$
\frac { d ( g _ { s } \gamma \pmb { v } ) } { d t } = \gamma \Big ( E _ { \mathrm { g } } + \pmb { v } \times \pmb { B } _ { \mathrm { g } } + v ^ { 2 } \pmb { \nabla } g _ { s } \Big ) + O ( c ^ { - 4 } ) ,
$$

where $g _ { s } : = 1 + 2 U / c ^ { 2 }$ is the coefficient of the spatial part of the pn metric, and $\gamma : = d t / d \tau =$ $1 + c ^ { - 2 } ( { \textstyle { \frac { 1 } { 2 } } } v ^ { 2 } + U ) + { \cal O } ( c ^ { - 4 } )$ . This can be expressed in the more explicit form

$$
\frac { d } { d t } \left\{ \left[ 1 + \frac { 1 } { c ^ { 2 } } \Big ( \frac { 1 } { 2 } v ^ { 2 } + 3 U \Big ) \right] v \right\} = \left[ 1 + \frac { 1 } { c ^ { 2 } } \Big ( \frac { 3 } { 2 } v ^ { 2 } - U \Big ) \right] E _ { \mathrm { g } } + v \times B _ { \mathrm { g } } + O ( c ^ { - 4 } ) .
$$

Apart from additional post-Newtonian terms, the equations are indeed remarkably similar to those of the Maxwell–Lorentz theory, with $\rho ^ { * }$ playing the role of the charge density, $\rho ^ { * } \pmb { v }$ that of the current density, and $- 4 \pi G$ playing the role of the coupling constant $1 / \epsilon _ { 0 }$ .

There are, however, clear indications that gravity is different from electrodynamics. Apart from the additional post-Newtonian terms, the most important differences are seen in the sign of the coupling constant and the factor of 4 in the $\nabla \times  { \boldsymbol { B } } _ { \mathrm { g } }$ equation. The gravitational coupling constant $- 4 \pi G$ is negative instead of positive, reflecting the fact that in gravity, like charges attract instead of repel. The factor of 4 reminds us that the gravitational potentials $\Phi _ { \mathrm { g } }$ and $A _ { \mathrm { { g } } }$ originate from a tensor (the metric) instead of a vector; in quantum parlance we say that the graviton is a spin-2 particle, while the photon is a spin-1 particle. The Lorentz-like equation would be identical to that of electrodynamics through $O ( c ^ { - 2 } )$ were it not for the appearance of the spatial part of the metric, represented by the factor $g _ { s }$ and the extra factor of $\gamma 0 \mathsf { n }$ the right-hand-side of Eq. (1), reflecting its true origin in the geodesic equation.

Nevertheless, the Maxwell-like formulation of the post-Newtonian approximation to Einstein’s equations and the geodesic equation can be very useful in specific situations, particularly when some of the additional post-Newtonian terms can be neglected. This occurs, for example, when the fields are stationary, when nonlinear contributions (proportional to $\rho ^ { * } U$ ) can be ignored, or when the velocity field inside the source is particularly small. In such cases, solutions to the post-Newtonian equations can be imported with minimal modifications from electrodynamics, along with the attached intuition. The Maxwell-like formulation has been used to study everything from laboratory and space experiments to test general relativity to the behavior of matter around rotating black holes.

# 8.2 Classic approach to post-Newtonian theory

Before we proceed with our exploration of post-Newtonian theory, it is instructive to provide an alternative derivation of the metric based on the standard formulation of the Einstein field equations instead of the Landau–Lifshitz formulation reviewed in Chapter 6. We refer to this derivation as the classic approach to post-Newtonian theory, and our quick survey will reveal some of the ambiguities and conceptual difficulties associated with it. The modern approach to post-Newtonian theory, based on its post-Minkowskian foundation, is completely free of such ambiguities and conceptual difficulties.

We begin by postulating a form of the metric to 1pn order:

$$
\begin{array} { l } { { \displaystyle g _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \big ( \Psi - U ^ { 2 } \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { ~ } \\ { { \displaystyle g _ { 0 j } = - \frac { 4 } { c ^ { 3 } } U _ { j } + { \cal O } ( c ^ { - 5 } ) } , } \\ { { \displaystyle g _ { j k } = \bigg ( 1 + \frac { 2 } { c ^ { 2 } } U \bigg ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where $U , U ^ { j }$ , and $\Psi$ are gravitational potentials to be determined. The term of order $c ^ { - 2 }$ in $g _ { 0 0 }$ is a Newtonian term. The terms of order $c ^ { - 4 }$ in $g _ { 0 0 } , c ^ { - 3 }$ in $g _ { 0 j }$ , and $c ^ { - 2 }$ in $g _ { j k }$ are post-Newtonian terms. The insertion of $U ^ { 2 }$ within $g _ { 0 0 }$ simplifies the form of the field equations. A blind post-Newtonian expansion of $g _ { j k }$ would introduce a general tensorial potential $U _ { j k }$ instead of the specific expression $U \delta _ { j k }$ that involves the same potential $U$ as in $g _ { 0 0 }$ . To keep the algebra simple, we anticipate the result of an integration of the Einstein field equations at lowest order, which reveals that indeed, $U _ { j k }$ must be equal to $U \delta _ { j k }$ . (In fact, we have reached this conclusion already in Sec. 5.5, when we studied the linearized approximation of general relativity.) We impose a harmonic coordinate condition, as displayed in Eq. (6.47); this reduces to

$$
\partial _ { t } U + \partial _ { j } U ^ { j } = 0
$$

at the required post-Newtonian order. Again we state that at the outset, $U , U ^ { j }$ , and $\Psi$ are unknown functions to be determined by the field equations; apart from our assumption regarding the tensorial potential, there is no loss of generality in Eq. (8.20).

The standard formulation of the Einstein field equations is $G _ { \alpha \beta } = ( 8 \pi G / c ^ { 4 } ) T _ { \alpha \beta }$ , and recalling the definition of the Einstein tensor from Eq. (5.71), this is

$$
R _ { \alpha \beta } - { \frac { 1 } { 2 } } R g _ { \alpha \beta } = { \frac { 8 \pi G } { c ^ { 4 } } } T _ { \alpha \beta } ,
$$

in which $R _ { \alpha \beta }$ is the Ricci tensor and $R : = g ^ { \alpha \beta } R _ { \alpha \beta }$ the Ricci scalar. Taking the trace yields $R = - ( 8 \pi G / c ^ { 4 } ) T$ , in which $T : = g ^ { \alpha \beta } R _ { \alpha \beta }$ , and making the substitution back in the field equations produces

$$
R _ { \alpha \beta } = { \frac { 8 \pi G } { c ^ { 4 } } } \bar { T } _ { \alpha \beta } ,
$$

in which $\bar { T } _ { \alpha \beta } : = T _ { \alpha \beta } - { \textstyle \frac { 1 } { 2 } } T g _ { \alpha \beta }$ is the “trace-reversed” energy-momentum tensor. This form of the field equations is our starting point for the determination of the potentials $U , U ^ { j }$ , and $\Psi$ . It is advantageous because the computation of the Ricci tensor from the metric of Eq. (8.20) is relatively straightforward. The computation of the Einstein tensor would require additional steps and make the entire task more tedious.

A straightforward calculation using the Christoffel symbols of Eqs. (8.15) reveals that the components of the Ricci tensor are

$$
\begin{array} { l } { { \displaystyle R _ { 0 0 } = - \frac { 1 } { c ^ { 2 } } \nabla ^ { 2 } U + \frac { 1 } { c ^ { 4 } } \big ( \partial _ { t t } U + 4 U \nabla ^ { 2 } U - \nabla ^ { 2 } \Psi \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle R _ { 0 j } = \frac { 2 } { c ^ { 3 } } \nabla ^ { 2 } U _ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle R _ { j k } = - \frac { 1 } { c ^ { 2 } } \nabla ^ { 2 } U \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

We have used Eq. (8.21) to eliminate terms involving $\partial _ { j } U ^ { j }$ in favor of terms involving $\partial _ { t } U$ . Importing the components of the energy-momentum tensor from Eq. (8.7), we have that

$$
\begin{array} { l } { { \displaystyle T _ { 0 0 } = \rho ^ { * } c ^ { 2 } \bigg [ 1 + \frac { 1 } { c ^ { 2 } } \Big ( \frac { 1 } { 2 } v ^ { 2 } - 5 U + \Pi \Big ) \bigg ] + O ( c ^ { - 2 } ) , } } \\ { { \displaystyle T _ { 0 j } = - \rho ^ { * } v ^ { j } c + O ( c ^ { - 1 } ) , } } \\ { { \displaystyle T _ { j k } = \rho ^ { * } v ^ { j } v ^ { k } + p \delta ^ { j k } + O ( c ^ { - 2 } ) , } } \end{array}
$$

to the required post-Newtonian order. To leading order this produces $\begin{array} { r } { \bar { T } _ { 0 0 } = \frac { 1 } { 2 } \rho ^ { * } c ^ { 2 } + O ( 1 ) } \end{array}$ , and the $c ^ { - 2 }$ piece of the 00 component of the field equations yields

$$
\nabla ^ { 2 } U = - 4 \pi G \rho ^ { * } .
$$

We conclude that as expected, $U$ is the standard Newtonian potential defined by Eq. (8.4). Also to leading order, $\begin{array} { r } { \bar { T } _ { j k } = \frac { 1 } { 2 } \delta _ { j k } \rho ^ { * } c ^ { 2 } + O ( 1 ) } \end{array}$ , and we see that the $c ^ { - 2 }$ piece of the $j k$ components of the field equations is automatically satisfied; this validates our assumed form for the spatial part of the metric. The $c ^ { - 3 }$ piece of the $0 j$ components of the field equations yields

$$
\nabla ^ { 2 } U _ { j } = - 4 \pi G \rho ^ { * } \boldsymbol { v } _ { j } ,
$$

and $U _ { j }$ is the standard vector potential as defined by Eq. (8.4). Finally, the $c ^ { - 4 }$ piece of the 00 component of the field equations yields

$$
\partial _ { t t } U + 4 U \nabla ^ { 2 } U - \nabla ^ { 2 } \Psi = 4 \pi G \rho ^ { \ast } \left( \frac { 3 } { 2 } v ^ { 2 } - 5 U + \Pi + \frac { 3 p } { \rho ^ { \ast } } \right) .
$$

This is a Poisson equation for $\Psi$ , and after substituting $\nabla ^ { 2 } U = - 4 \pi G \rho ^ { * }$ on the left-hand side and rearranging, we see that $\Psi$ is given by

$$
\Psi = \psi + \frac { 1 } { 2 } \partial _ { t t } F ,
$$

with $\psi$ and $F$ required to satisfy

$$
\nabla ^ { 2 } \psi = - 4 \pi G \rho ^ { \ast } \left( \frac { 3 } { 2 } v ^ { 2 } - U + \Pi + \frac { 3 p } { \rho ^ { \ast } } \right) ,
$$

and

$$
\nabla ^ { 2 } F = 2 U .
$$

The solution to Eq. (8.30) is evidently the potential defined by Eq. (8.4b).

To identify the solution to Eq. (8.31) requires a more careful discussion, because the source term $2 U$ is not limited to the region occupied by the matter distribution; it is distributed over all space. This discussion has already been provided in Box. 7.3, where it was shown that the general solution is given by

$$
F = X - 2 m \mathcal { R } + F _ { 0 } ,
$$

in which $X ( t , x )$ is the standard superpotential as displayed in Eq. (8.4), $\begin{array} { r } { m : = \int \rho ^ { * } d ^ { 3 } x } \end{array}$ is the total rest-mass of the fluid system, $\mathcal { R }$ is a constant length, and $F _ { 0 } ( t , \boldsymbol { x } )$ is a solution to Laplace’s equation. Demanding that $F _ { 0 }$ does not depend on time implies that $\partial _ { t t } F = \partial _ { t t } X$ , so that $\Psi = \psi + \partial _ { t t } X$ as required by Eq. (8.3). Choosing $F _ { 0 } = 2 m \mathcal { R }$ returns the stronger equality $F = X$ , yielding the same expression for $\Psi$ .

The preceding discussion indicates that when appropriate choices are made, the solution to Eq. (8.31) returns the correct expression for $\Psi$ , as given by Eq. (8.3). The main question that arises is: which guiding principle can be invoked to justify the choices made to specify this solution? The answer is simply that no such principle exists within the strict context of the classic approach to post-Newtonian theory; the ambiguities associated with $F$ can only be resolved with ad hoc choices. For a more satisfying resolution, one must turn to the modern approach and its post-Minkowskian foundation.

In the classic approach, the superpotential arises as a particular solution to $\nabla ^ { 2 } F =$ $2 U$ , and the choice of solution is ambiguous because $U$ extends over all space. (The potentials $U , U ^ { j }$ , and $\psi$ do not share this ambiguity, because their source terms are tied to the matter distribution.) In the modern approach, the superpotential arises in an expansion of $h ^ { 0 0 }$ in powers of $c ^ { - 1 }$ in the near zone, and it is fundamentally defined as the integral $\int \rho ^ { * } \boldsymbol { \cdot } | \boldsymbol { x } - \boldsymbol { x } ^ { \prime } | d ^ { 3 } x ^ { \prime }$ ; the Poisson equation follows as a consequence of this definition. The advantages of the modern approach should be clear. First, the post-Minkowskian foundation provides a clear restriction of the post-Newtonian metric to the near zone, while no such restriction is immediately apparent in the classic approach. Second, while the classic approach features Poisson equations with ambiguous solutions, the modern approach defines all potentials in terms of near-zone integrals that are devoid of ambiguities.

A third advantage is concerned with the incorporation of retardation effects in the post-Newtonian metric. Our experience with post-Minkowskian theory allows us to locate the retardation in the $\partial _ { t t } { X }$ term, but we would be hard pressed to provide this understanding if we were only familiar with the classic approach. Indeed, because the classic approach defines each potential in terms of a Poisson equation, each potential will necessarily be instantaneous, and the retardation effects will be implicit and hidden from view. There is actually a deeper problem that is revealed at higher post-Newtonian orders. A systematic development of the classic approach to higher orders would continue to introduce potentials that satisfy Poisson equations, and the ambiguities would pile up. In particular, it would quickly become unclear how to impose a condition that the metric should describe outgoing gravitational waves at infinity. Because the post-Newtonian expansion is necessarily limited to the near-zone region of space, the wave zone is inaccessible, and the boundary conditions cannot be formulated in a clean way. In the modern approach, the post-Minkowskian formulation of the problem is based on wave equations instead of Poisson equations, and the selection of retarded solutions ensures that the waves are properly outgoing in the wave zone. It is this specific choice of solution that provides the retardation and makes the near-zone metric completely unambiguous.

In his sequence of papers on post-Newtonian hydrodynamics written between 1964 and 1969, Chandrasekhar employed the classic approach outlined in this section to derive the metric and the equations of motion. Working with his student Yavuz Nutku, he continued to employ this method to obtain the 2pn equations of hydrodynamics. But when it came time in 1970 to move on to the $2 . 5 \mathrm { { p N } }$ equations of motion, an order at which the selection of outgoing-wave boundary conditions is essential, Chandra and his student Paul Esposito finally recognized the limitations described here. They converted to the modern approach.

# 8.3 Coordinate transformations

# 8.3.1 Introduction

In this section we explore the freedom that post-Newtonian theory possesses to perform coordinate transformations that preserve the post-Newtonian ordering of the metric. We wish to find the most general class of transformations

$$
t = t ( \bar { t } , \bar { x } ^ { j } ) , \qquad x ^ { j } = x ^ { j } ( \bar { t } , \bar { x } ^ { j } ) ,
$$

that keeps the metric expressed as an expansion in powers of $c ^ { - 2 }$ . We call these post-Newtonian transformations, and construct them step-by-step in Secs. 8.3.2 and 8.3.3.

We shall find that in general, the post-Newtonian transformations do not preserve the harmonic coordinate condition of Eq. (8.21). In Sec. 8.3.4 we specialize them to a class that keeps the coordinates harmonic; we call this restricted class the harmonic transformations of post-Newtonian theory. We describe a simple application of this formalism in Sec. 8.3.5, in which we examine the Newtonian potential of a moving body in its own (non-inertial) reference frame.

The post-Newtonian and harmonic transformations typically produce gravitational potentials that contain spatially-growing terms, even when the original potentials vanish in the formal limit $r  \infty$ . In Sec. 8.3.6 we specialize them further by demanding that the transformed potentials continue to vanish in the limit $\bar { r } \to \infty$ ; this property defines what is known as the post-Galilean transformations of post-Newtonian theory.

Within the post-Newtonian class of transformations there exists an interesting subclass that corresponds very closely to the ordinary gauge transformations of electrodynamics. We examine these in Sec. 8.3.7, and introduce the so-called standard gauge of post-Newtonian theory. This was the gauge that was adopted by Chandrasekhar in his pioneering work on the subject, and much of the older post-Newtonian literature is framed in this gauge. The standard gauge, however, has become less popular of late, and the more recent literature is uniformly cast in the harmonic gauge. We adhere to this choice in most of the book, but the standard post-Newtonian gauge is featured in Chapter 13, in which we examine alternative theories of gravity.

In this section we follow closely the treatment of post-Newtonian coordinate transformations developed by our friends Etienne Racine and´ Eanna Flanagan (2005). We recall´ that under the transformation of Eq. (8.33), the components of the metric tensor change according to

$$
\begin{array} { l l } { \displaystyle \bar { g } _ { 0 0 } = \left( \frac { \partial t } { \partial \bar { t } } \right) ^ { 2 } g _ { 0 0 } + \frac { 2 } { c } \frac { \partial t } { \partial \bar { t } } \frac { \partial x ^ { j } } { \partial \bar { t } } g _ { 0 j } + \frac { 1 } { c ^ { 2 } } \frac { \partial x ^ { j } } { \partial \bar { t } } \frac { \partial x ^ { k } } { \partial \bar { t } } g _ { j k } , } \\ { \displaystyle \bar { g } _ { 0 j } = c \frac { \partial t } { \partial \bar { t } } \frac { \partial t } { \partial \bar { x } ^ { j } } g _ { 0 0 } + \bigg ( \frac { \partial t } { \partial \bar { t } } \frac { \partial x ^ { k } } { \partial \bar { x } ^ { j } } + \frac { \partial x ^ { k } } { \partial \bar { t } } \frac { \partial t } { \partial \bar { x } ^ { j } } \bigg ) g _ { 0 k } + \frac { 1 } { c } \frac { \partial x ^ { k } } { \partial \bar { t } } \frac { \partial x ^ { n } } { \partial \bar { x } ^ { j } } g _ { k n } , } \\ { \displaystyle \bar { g } _ { j k } = c ^ { 2 } \frac { \partial t } { \partial \bar { x } ^ { j } } \frac { \partial t } { \partial \bar { x } ^ { k } } g _ { 0 0 } + c \bigg ( \frac { \partial t } { \partial \bar { x } ^ { j } } \frac { \partial x ^ { n } } { \partial \bar { x } ^ { k } } + \frac { \partial x ^ { n } } { \partial \bar { x } ^ { j } } \frac { \partial t } { \partial \bar { x } ^ { k } } \bigg ) g _ { 0 n } + \frac { \partial x ^ { n } } { \partial \bar { x } ^ { j } } \frac { \partial x ^ { p } } { \partial \bar { x } ^ { k } } g _ { n p } . } \end{array}
$$

Our most important results are summarized in $\mathrm { B o x } 8 . 2$ . The reader is invited to peruse the summary before getting started with the details, so as to benefit from an overview of what is to come.

<table><tr><td>Box 8.2</td><td>Post-Newtonian transformations</td></tr><tr><td></td><td>The most general coordinate transformation that preserves the post-Newtonian orderingofthe metric is given by</td></tr><tr><td></td><td>1 1 t=t+ 3 a(t，xi)</td></tr><tr><td></td><td>x𝑗 =x+rj(t)+ hi(t,xi）+O(c-4)，</td></tr></table>

where

$$
\begin{array} { l } { { \displaystyle \alpha = { \cal A } ( \bar { t } ) + v _ { j } \bar { x } ^ { j } , } } \\ { { \displaystyle h ^ { j } = H ^ { j } ( \bar { t } ) + H _ { k } ^ { j } ( \bar { t } ) \bar { x } ^ { k } + \frac { 1 } { 2 } H _ { k n } ^ { j } ( \bar { t } ) \bar { x } ^ { k } \bar { x } ^ { n } , } } \end{array}
$$

with

$$
\begin{array} { l } { { H _ { j k } = \epsilon _ { j k n } R ^ { n } ( \bar { t } ) + \displaystyle \frac { 1 } { 2 } v _ { j } v _ { k } - \delta _ { j k } \Big ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } \Big ) , } } \\ { { H _ { j k n } = - \delta _ { j k } a _ { n } - \delta _ { j n } a _ { k } + \delta _ { k n } a _ { j } . } } \end{array}
$$

The functions $A , r ^ { j } , H ^ { j }$ , and $R ^ { j }$ are freely specifiable functions of time $\overline { { t } } _ { i }$ , while $\beta$ is a free function of all the coordinates. The transformation is therefore characterized by ten arbitrary functions of time, and one arbitrary function of all the coordinates. An overdot indicates differentiation with respect to $\bar { t } _ { + }$ , and we have introduced $v ^ { j } : = \dot { r } ^ { j }$ and $a ^ { j } : = \dot { v } ^ { j } = \ddot { r } ^ { j }$ . In addition, we let $v ^ { 2 } = \delta _ { j k } v ^ { j } v ^ { k }$ .

The transformation preserves the post-Newtonian ordering of the metric, but it does not necessarily keep the coordinates harmonic. To preserve this also we must set

$$
\beta = \frac { 1 } { 6 } \ddot { \cal A } \delta _ { j k } \bar { x } ^ { j } \bar { x } ^ { k } + \frac { 1 } { 3 0 } \big ( \delta _ { j k } \dot { a } _ { n } + \delta _ { j n } \dot { a } _ { k } + \delta _ { k n } \dot { a } _ { j } \big ) \bar { x } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } + \gamma ( \bar { t } , \bar { x } ^ { j } ) ,
$$

and $\gamma$ is required to satisfy Laplace’s equation: $\bar { \nabla } ^ { 2 } \gamma = 0$ , with ${ \bar { \nabla } } ^ { 2 }$ denoting the Laplacian operator in the coordinates ${ \bar { x } } ^ { j }$ . The arbitrary function $\beta$ has therefore been replaced by an arbitrary harmonic function $\gamma$ .

Under a harmonic coordinate transformation the potentials become

$$
\begin{array} { l } { { \displaystyle \bar { U } ( \bar { t } , \bar { x } ^ { j } ) = \hat { U } - \dot { A } + \frac { 1 } { 2 } v ^ { 2 } - a _ { j } \bar { x } ^ { j } , } } \\ { { \displaystyle \bar { U } ^ { j } ( \bar { t } , \bar { x } ^ { j } ) = \hat { U } ^ { j } - v ^ { j } \hat { U } + \frac { 1 } { 4 } \biggl ( V ^ { j } + V _ { k } ^ { j } \bar { x } ^ { k } + \frac { 1 } { 2 } V _ { k n } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } + { \partial } _ { j } \gamma \biggr ) , } } \\ { { \displaystyle \bar { \Psi } ( \bar { t } , \bar { x } ^ { j } ) = \hat { \Psi } - 4 v ^ { j } \hat { U } _ { j } + 2 v ^ { 2 } \hat { U } + \bigl ( A + v _ { k } \bar { x } ^ { k } \bigr ) { \partial } _ { \bar { t } } \hat { U } } } \\ { { \displaystyle \qquad + \biggl ( F ^ { j } + F _ { k } ^ { j } \bar { x } ^ { k } + \frac { 1 } { 2 } F _ { k n } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } \bigr ) { \partial } _ { j } \hat { U } } } \\ { { \displaystyle \qquad + G + G _ { j } \bar { x } ^ { j } + \frac { 1 } { 2 } G _ { j k } \bar { x } ^ { j } \bar { x } ^ { k } + \frac { 1 } { 6 } G _ { j k n } \bar { x } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } - { \partial } _ { \bar { t } } \gamma , } } \end{array}
$$

where

$$
\begin{array} { l } { { V ^ { j } = ( 2 \dot { A } - v ^ { 2 } ) v ^ { j } - \dot { H } ^ { j } + \epsilon _ { p q } ^ { j } v ^ { p } R ^ { q } , } } \\ { { V _ { k } ^ { j } = \displaystyle \frac { 3 } { 2 } v ^ { j } a _ { k } + \frac { 1 } { 2 } a ^ { j } v _ { k } + \delta _ { k } ^ { j } \Bigl ( \frac { 4 } { 3 } \ddot { A } - 2 v ^ { n } a _ { n } \Bigr ) - \epsilon _ { k p } ^ { j } \dot { R } ^ { p } , } } \\ { { V _ { k n } ^ { j } = \displaystyle \frac { 6 } { 5 } \bigl ( \delta _ { k } ^ { j } \dot { a } _ { n } + \delta _ { n } ^ { j } \dot { a } _ { k } \bigr ) - \frac { 4 } { 5 } \delta _ { k n } \dot { a } ^ { j } , } } \end{array}
$$

(continued overleaf)

$$
\begin{array} { l } { { F ^ { j } = H ^ { j } - { \cal A } v ^ { j } , } } \\ { { \displaystyle } } \\ { { F _ { k } ^ { j } = - \delta _ { k } ^ { j } \Big ( \dot { \cal A } - \frac 1 2 v ^ { 2 } \Big ) - \frac 1 2 v ^ { j } v _ { k } + \epsilon _ { k p } ^ { j } { \cal R } ^ { p } , } } \\ { { \displaystyle } } \\ { { F _ { k n } ^ { j } = - \big ( \delta _ { k } ^ { j } a _ { n } + \delta _ { n } ^ { j } a _ { k } \big ) + \delta _ { k n } a ^ { j } , } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle { G = \frac { 1 } { 2 } \dot { A } ^ { 2 } - \dot { A } v ^ { 2 } + \frac { 1 } { 4 } v ^ { 4 } + \dot { H } ^ { j } v _ { j } } , } } \\ { { \displaystyle { G _ { j } = \Big ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } \Big ) a _ { j } - \Big ( \ddot { A } - \frac { 3 } { 2 } v ^ { k } a _ { k } \Big ) v _ { j } - \epsilon _ { j p q } v ^ { p } \dot { A } ^ { q } } , } } \\ { { \displaystyle { G _ { j k } = a _ { j } a _ { k } - v _ { j } \dot { a } _ { k } - \dot { a } _ { j } v _ { k } + \delta _ { j k } ( v _ { n } \dot { a } ^ { n } ) - \frac { 1 } { 3 } \delta _ { j k } \ddot { A } } , } } \\ { { \displaystyle { G _ { j k n } = - \frac { 1 } { 5 } \big ( \delta _ { j k } \ddot { a } _ { n } + \delta _ { j n } \ddot { a } _ { k } + \delta _ { k n } \ddot { a } _ { j } \big ) } . } } \end{array}
$$

The “hatted” potentials are equal to the original potentials evaluated at time $t = \bar { t }$ and position $x ^ { j } =$ $\bar { x } ^ { j } + r ^ { j } ( \bar { t } )$ . For example,

$$
\hat { U } ( \bar { t } , \bar { x } ^ { j } ) : = U \big ( t = \bar { t } , x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } ) \big ) .
$$

Because $U$ now possesses, in addition to its original explicit time dependence, an implicit time dependence contained in $r ^ { j } ( \bar { t } )$ , some care must be exercised when taking time derivatives. We have

$$
\frac { \partial \hat { U } } { \partial \bar { t } } = \frac { \partial U } { \partial t } + v ^ { j } \frac { \partial U } { \partial x ^ { j } } , \qquad \frac { \partial \hat { U } } { \partial \bar { x } ^ { j } } = \frac { \partial U } { \partial x ^ { j } } ,
$$

in which the right-hand-sides are evaluated at $t = \bar { t }$ and $x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } )$

We begin with a search for a coordinate transformation that preserves the form of the metric at Newtonian order:

$$
g _ { 0 0 } = - 1 + { \frac { 2 } { c ^ { 2 } } } U + O ( c ^ { - 4 } ) , \qquad g _ { 0 j } = O ( c ^ { - 3 } ) , \qquad g _ { j k } = \delta _ { j k } + O ( c ^ { - 2 } ) .
$$

Specifically, we demand that the new metric takes the form

$$
\bar { g } _ { 0 0 } = - 1 + { \frac { 2 } { c ^ { 2 } } } \bar { U } + O ( c ^ { - 4 } ) , \qquad \bar { g } _ { 0 j } = O ( c ^ { - 3 } ) , \qquad \bar { g } _ { j k } = \delta _ { j k } + O ( c ^ { - 2 } ) ,
$$

with a new Newtonian potential $\bar { U }$ whose relation with the old one will be determined by the transformation.

Inspecting Eq. (8.34a) first, we note that the leading term in $\bar { g } _ { 0 0 }$ will have the correct value of $^ { - 1 }$ if and only if $\partial t / \partial \bar { t } = 1 + O ( c ^ { - 2 } )$ . Moving next to Eq. (8.34c), we see that $\bar { g } _ { j k }$ will contain unwanted terms of order $c ^ { 2 }$ unless $\partial t / \partial \bar { x } ^ { j } = { O } ( c ^ { - 2 } )$ . And the terms of order

$c ^ { 0 }$ will have the correct form if and only if

$$
\delta _ { j k } = \frac { \partial x ^ { p } } { \partial \bar { x } ^ { j } } \frac { \partial x ^ { q } } { \partial \bar { x } ^ { k } } \delta _ { p q } + O ( c ^ { - 2 } ) .
$$

The Newtonian transformation must preserve the form of the spatial metric, and this means that it must be the combination of a translation of the spatial origin with a rotation of the coordinate axes: $x ^ { j } = r ^ { j } + R _ { \ k } ^ { j } \bar { x } ^ { k } + O ( c ^ { - 2 } )$ . Here $r ^ { j } ( \bar { t } )$ are arbitrary functions of time, and $R _ { k } ^ { j } ( \bar { t } )$ are the components of a rotation matrix that satisfies $\delta _ { p q } R _ { j } ^ { p } R _ { k } ^ { q } = \delta _ { j k }$ . At this stage of our considerations we conclude that the transformation must take the form

$$
t = \bar { t } + \frac { 1 } { c ^ { 2 } } \alpha ( \bar { t } , \bar { x } ^ { j } ) + O ( c ^ { - 4 } ) , \qquad x ^ { j } = r ^ { j } ( \bar { t } ) + R _ { k } ^ { j } ( \bar { t } ) \bar { x } ^ { k } + O ( c ^ { - 2 } ) ,
$$

where $\alpha$ is (for now) an arbitrary function of the new coordinates, and $r ^ { j }$ , $\boldsymbol { R } _ { \ k } ^ { j }$ are arbitrary functions of time.

We next examine Eq. (8.34b), in which we make the substitutions of Eq. (8.38). After simplification we notice that $\bar { g } _ { 0 j }$ will contain unwanted terms at order $c ^ { - 1 }$ unless

$$
\partial _ { \bar { \boldsymbol { J } } } \alpha = \left( \boldsymbol { v } ^ { k } + { \dot { R } } _ { n } ^ { k } { \boldsymbol { \bar { x } } } ^ { n } \right) R _ { k j } ;
$$

an overdot indicates differentiation with respect to $\bar { t }$ , and we introduced the notation $v ^ { j } : = \dot { r } ^ { j }$ . The previously stated condition on the rotation matrix implies that ${ \dot { R } } _ { n } ^ { k } R _ { k j }$ is antisymmetric on $n$ and $j$ , and can therefore be expressed as $\dot { R } _ { n } ^ { k } R _ { k j } = \epsilon _ { n j m } \omega ^ { m } ( t )$ for some vector $\omega ^ { m }$ . The equation for $\alpha$ is now

$$
\partial _ { \bar { \jmath } } \alpha = v ^ { k } R _ { k j } + \epsilon _ { j m n } \omega ^ { m } \bar { x } ^ { n } ,
$$

and we see that the final term cannot be written as the gradient of any function. To eliminate the unwanted $c ^ { - 1 }$ term in $\bar { g } _ { 0 j }$ we must therefore set $\omega ^ { m } = 0$ , so that $\boldsymbol { R } _ { \ k } ^ { j }$ describes a time-independent rotation of the coordinate axes. We choose to discard this uninteresting coordinate freedom by setting

$$
R _ { j k } = \delta _ { j k } .
$$

The general solution for $\alpha$ is then

$$
\alpha = A ( \bar { t } ) + v _ { j } ( \bar { t } ) \bar { x } ^ { j } ,
$$

in which $A$ is an arbitrary function of time $\bar { t } .$ . The Newtonian transformation of Eq. (8.38) is now fully characterized.

<table><tr><td>Box 8.3</td><td>Rotating coordinates</td></tr><tr><td></td><td>Byforcing goj to vanishat order c-1,weare consciously excluding rotating coordinate systems from the allowed classofpost-Newtonian coordinates.Todescribea purelyrotating coordinate system, we would use the transformation</td></tr></table>

$$
t = \bar { t } + O ( c ^ { - 4 } ) , \qquad x ^ { j } = R _ { k } ^ { j } ( \bar { t } ) \bar { x } ^ { k } + O ( c ^ { - 2 } ) ,
$$

which leads to a metric of the form

$$
\begin{array} { l } { { \displaystyle \bar { g } _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } \bar { U } + \frac { 1 } { c ^ { 2 } } \big [ \omega ^ { 2 } - ( \omega \cdot \bar { n } ) ^ { 2 } \big ] \bar { r } ^ { 2 } + O ( c ^ { - 4 } ) , } } \\ { { \displaystyle \bar { g } _ { 0 j } = \frac { 1 } { c } ( \omega \times \bar { x } ) _ { j } + O ( c ^ { - 3 } ) , } } \\ { { \displaystyle \bar { g } _ { j k } = \delta _ { j k } + O ( c ^ { - 2 } ) , } } \end{array}
$$

where $\omega _ { j } ( t ) : = \frac 1 2 \epsilon _ { j l m } \dot { R } _ { l } ^ { k } R _ { k m }$ and $\bar { \pmb { n } } = \bar { \pmb { x } } / \bar { r }$ . From a relativistic point of view, this metric presents a number of problems. One of these is that it does not reduce to the Minkowski metric when $\bar { r } \to \infty$ . An even worse problem is that $g _ { 0 0 }$ vanishes when $\omega { \bar { r } } \sin \theta = c ( 1 - U / c ^ { 2 } )$ , where $\theta$ is the angle between $\pmb { \omega }$ and $\bar { n }$ . This “light cylinder” is a place where the speed of a particle at rest in the rotating frame equals the local speed of light as measured in the global, non-rotating frame; particles at rest outside the light cylinder exceed the local speed of light.

Other issues connected with the rotating frame include the inability to synchronize clocks consistently around a circle at rest in this frame (the Sagnac effect, reviewed in Sec. 10.3.4), and the common misconception that the circumference of a rotating disk is shortened compared to $2 \pi$ times its radius. These issues have generated so much misunderstanding that in the general relativity textbook by H.P. Robertson and T.W. Noonan (1968), there is a paragraph on this topic headed “That darned\* rotating disk,” with the asterisk indicating that the actual word selected by Robertson in his original lecture notes was much stronger!

As indicated in the text, we wish to preserve the post-Newtonian expansion of the metric, and therefore exclude rotating coordinate systems from our considerations. This doesn’t mean, however, that rotating coordinates are never appropriate. They can indeed be very useful, provided that one stays well within the light cylinder. For example, a coordinate system that rotates with the Earth is an extremely powerful tool to describe post-Newtonian gravity in and around the Earth, including its effects on geocentric satellites, atomic timekeeping, and the Global Positioning System. These applications are discussed in detail in Chapter 10.

To determine how the Newtonian potential changes under the transformation, we return to Eq. (8.34a) and examine the terms of order $c ^ { - 2 }$ after making the substitutions of Eq. (8.38). After simplification we find that the right-hand side is given by $- 1 + 2 c ^ { - 2 } ( U - \partial _ { \bar { t } } \alpha +$ $\frac { 1 } { 2 } v ^ { 2 } ) + O ( c ^ { - 4 } )$ , where $v ^ { 2 } : = \delta _ { j k } v ^ { j } v ^ { k }$ . The new potential must therefore be $\bar { U } = U - \partial _ { \bar { t } } \alpha +$ ${ \frac { \bar { 1 } } { 2 } } v ^ { 2 }$ . Here $\bar { U }$ is expressed in terms of the new coordinates $( \bar { t } , \bar { x } ^ { j } )$ , but $U$ is still written in terms of the old coordinates $( t , x ^ { j } )$ . To make the equation more useful we should express $U$ as a function of the new coordinates. To achieve this we write

$$
U ( t , x ^ { j } ) = U ( \bar { t } + c ^ { - 2 } \alpha + \cdots , \bar { x } ^ { j } + r ^ { j } + \cdots )
$$

and perform a Taylor expansion of the right-hand side about the point $( \bar { t } , \bar { x } ^ { j } + r ^ { j } )$ . This gives $U ( t , x ^ { j } ) = U ( \bar { t } , \bar { x } ^ { j } + r ^ { j } ) + O ( c ^ { - 2 } )$ , and we find that the terms of order $c ^ { - 2 }$ play no role in the transformation of the Newtonian potential. (They do, however, appear in the post-Newtonian transformation of the following subsection.)

To distinguish clearly between the sets of arguments $( \bar { t } , \bar { x } ^ { j } ) , ( \bar { t } , \bar { x } ^ { j } + r ^ { j } )$ , and $( t , x ^ { j } )$ we introduce the “hatted” potential

$$
{ \hat { U } } ( { \bar { t } } , { \bar { x } } ^ { j } ) : = U ( { \bar { t } } , { \bar { x } } ^ { j } + r ^ { j } ) .
$$

This is the original potential $U$ evaluated at time $t = \bar { t }$ and position $x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } )$ . In terms of this we have

$$
U ( t , x ^ { j } ) = \hat { U } ( \bar { t } , \bar { x } ^ { j } ) + O ( c ^ { - 2 } )
$$

and the transformed potential is $\begin{array} { r } { \bar { U } = \hat { U } - \partial _ { \bar { t } } \alpha + \frac { 1 } { 2 } v ^ { 2 } } \end{array}$ . Using Eq. (8.42), this is

$$
\bar { U } = \hat { U } - \dot { A } + \frac { 1 } { 2 } v ^ { 2 } - a _ { j } \bar { x } ^ { j } ,
$$

where $a ^ { j } : = \dot { v } ^ { j } = \ddot { r } ^ { j }$ . All members of this equation are functions of the new coordinates $( \bar { t } , \bar { x } ^ { j } )$ .

When it is expressed in terms of $U$ as in Eq. (8.44), the hatted potential $\hat { U }$ possesses both an explicit and an implicit dependence upon the time coordinate t¯. The explicit dependence is contained in $U$ ’s temporal argument, while the implicit dependence appears via $r ^ { j } ( \bar { t } )$ in the spatial arguments. Some care must therefore be exercised when computing partial derivatives. We have, for example,

$$
\frac { \partial \hat { U } } { \partial \bar { t } } = \left( \frac { \partial U } { \partial t } + v ^ { j } \frac { \partial U } { \partial x ^ { j } } \right) _ { t = \bar { t } , ~ x = \bar { x } + r } ,
$$

in which the substitutions $t = \bar { t }$ , $x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } )$ are made after differentiating $U$ with respect to its original variables $t$ and $x ^ { j }$ . Spatial derivatives, on the other hand, are given simply by

$$
\frac { \partial \hat { U } } { \partial \bar { x } ^ { j } } = \left( \frac { \partial U } { \partial x ^ { j } } \right) _ { t = \bar { t } , \ x = \bar { x } + r } .
$$

# 8.3.3 Post-Newtonian transformations

To proceed to the next order we write the coordinate transformation as

$$
\begin{array} { l } { { t = \displaystyle { \bar { t } } + \frac { 1 } { c ^ { 2 } } \alpha ( \bar { t } , \bar { x } ^ { j } ) + \frac { 1 } { c ^ { 4 } } \beta ( \bar { t } , \bar { x } ^ { j } ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } ) + \frac { 1 } { c ^ { 2 } } h ^ { j } ( \bar { t } , \bar { x } ^ { j } ) + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

where $\alpha$ is given by Eq. (8.42), while $\beta$ and $h ^ { j }$ represent the additional coordinate freedom that appears at 1pn order.

The function $\beta$ will remain arbitrary. To constrain $h ^ { j }$ we examine the $O ( c ^ { - 2 } )$ terms on the right-hand-side of Eq. (8.34c) and demand that, in accordance with Eq. (8.20), they be equal to $2 \bar { U } \delta _ { j k }$ . With Eqs. (8.45) and (8.46), we find after simplification that $h ^ { j }$ must be a

solution to the differential equation

$$
\partial _ { \bar { \jmath } } h _ { k } + \partial _ { \bar { k } } h _ { j } = - 2 \delta _ { j k } \bigg ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } + a _ { n } \bar { x } ^ { n } \bigg ) + v _ { j } v _ { k } .
$$

The general solution to this equation is the sum of a particular solution and the general solution to the homogeneous equation $\partial _ { \bar { \jmath } } h _ { k } + \partial _ { \bar { k } } h _ { j } = 0 .$ (The expert will recognize this as Killing’s equation in a flat, three-dimensional space.)

The form of the homogeneous equation reveals that $h _ { \mathrm { h o m } } ^ { j }$ must be linear in the coordinates: $h _ { \mathrm { h o m } } ^ { j } = H ^ { j } + A _ { \ k } ^ { j } \bar { x } ^ { k }$ , where $H ^ { j }$ and $\boldsymbol { A } _ { \boldsymbol { k } } ^ { j }$ are functions of $\bar { t }$ . Substitution within the differential equation reveals that $H ^ { j } ( \bar { t } )$ is arbitrary, but that $A _ { j k }$ must be an antisymmetric tensor. Such a tensor contains three independent components, and we can always express it as $A _ { j k } = \epsilon _ { j k n } R ^ { n }$ , in terms of a vector $R ^ { n }$ that also contains three independent components. We have obtained $h _ { \mathrm { h o m } } ^ { j } = H ^ { j } ( \bar { t } ) + \epsilon _ { \ : k n } ^ { j } \bar { x } ^ { k } R ^ { n } ( \bar { t } )$ . The first term represents a translational component to the coordinate transformation, which combines with the Newtonian translation to form the total translation $r ^ { j } + c ^ { - 2 } H ^ { j }$ . The second term represents a rotation of the coordinate axes, and the rotation matrix is $R _ { \ k } ^ { j } = c ^ { - 2 } \epsilon _ { \ k n } ^ { j } R ^ { n }$ .

The form of the inhomogeneous equation reveals that a particular solution $h _ { \mathrm { p a r t } } ^ { j }$ will be quadratic in the coordinates. We adopt $B _ { j k } { \bar { x } } ^ { k } + { \textstyle \frac { 1 } { 2 } } B _ { j k n } { \bar { x } } ^ { k } { \bar { x } } ^ { n }$ as a trial solution, and observe that $B _ { j k n }$ can be chosen to be symmetric in the last pair of indices. Substitution within the differential equation shows that $B _ { j k }$ is constrained by $B _ { j k } + B _ { k j } = - 2 \delta _ { j k } ( \dot { A } -$ $\frac { 1 } { 2 } \boldsymbol { v } ^ { 2 } ) + \boldsymbol { v } _ { j } \boldsymbol { v } _ { k }$ , while $B _ { j k n }$ is constrained by $B _ { j k n } + B _ { k j n } = - 2 \delta _ { j k } a _ { n } .$ . The solutions are readily identified as $\begin{array} { r } { B _ { j k } = - \delta _ { j k } ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } ) + \frac { 1 } { 2 } v _ { j } v _ { k } } \end{array}$ and $B _ { j k n } = - \delta _ { j k } a _ { n } - \delta _ { j n } a _ { k } + \delta _ { k n } a _ { j }$ .

Collecting results, we write our final expression for $h ^ { j } = h _ { \mathrm { h o m } } ^ { j } + h _ { \mathrm { p a r t } } ^ { j }$ as

$$
h ^ { j } = H ^ { j } ( \bar { t } ) + H _ { k } ^ { j } ( \bar { t } ) \bar { x } ^ { k } + \frac { 1 } { 2 } H _ { k n } ^ { j } ( \bar { t } ) \bar { x } ^ { k } \bar { x } ^ { n } ,
$$

with

$$
\begin{array} { l } { { H _ { j k } = \epsilon _ { j k n } R ^ { n } ( \bar { t } ) + \displaystyle \frac { 1 } { 2 } v _ { j } v _ { k } - \delta _ { j k } \Big ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } \Big ) , } } \\ { { H _ { j k n } = - \delta _ { j k } a _ { n } - \delta _ { j n } a _ { k } + \delta _ { k n } a _ { j } . } } \end{array}
$$

This piece of the coordinate transformation involves the six arbitrary functions of time that are contained in $H ^ { j } ( \bar { t } )$ and $R ^ { j } ( \bar { t } )$ .

To determine how the vector potential $U ^ { j }$ transforms under the post-Newtonian transformation of Eqs. (8.49), we make the substitutions in Eq. (8.34) and demand that $g _ { 0 j }$ keeps its post-Newtonian form of $- 4 c ^ { - 3 } U _ { j } + { \cal O } ( c ^ { - 5 } )$ . A careful evaluation of Eq. (8.34b) reveals that the new vector potential $\bar { U } _ { j }$ is given by

$$
4 { \bar { U } } _ { j } = 4 ( { \hat { U } } _ { j } - v _ { j } { \hat { U } } ) + \partial _ { \bar { \jmath } } \beta + v _ { j } \partial _ { \bar { t } } \alpha - v ^ { k } \partial _ { \bar { \jmath } } h _ { k } - \partial _ { \bar { t } } h _ { j } ,
$$

in which $\hat { U } _ { j }$ is defined by analogy with Eq. (8.44). Taking into account Eqs. (8.42) and (8.51), we finally arrive at

$$
\bar { U } _ { j } = \hat { U } _ { j } - v _ { j } \hat { U } + \frac { 1 } { 4 } \biggl ( V _ { j } + V _ { j k } \bar { x } ^ { k } + \frac { 1 } { 2 } V _ { j k n } \bar { x } ^ { k } \bar { x } ^ { n } + \partial _ { \bar { \jmath } } \beta \biggr ) ,
$$

with

$$
\begin{array} { l } { { V _ { j } = ( 2 \dot { A } - v ^ { 2 } ) v _ { j } - \dot { H } _ { j } + \epsilon _ { j p q } v ^ { p } R ^ { q } , } } \\ { { \displaystyle V _ { j k } = \frac 3 2 v _ { j } a _ { k } + \frac 1 2 v _ { k } a _ { j } + \delta _ { j k } \big ( \ddot { A } - 2 v ^ { n } a _ { n } \big ) - \epsilon _ { j k p } \dot { R } ^ { p } , } } \\ { { V _ { j k n } = \delta _ { j k } \dot { a } _ { n } + \delta _ { j n } \dot { a } _ { k } - \delta _ { k n } \dot { a } _ { j } . } } \end{array}
$$

We are now ready to derive the transformation equation for the post-Newtonian potential $\Psi$ . We proceed along the same lines as for the vector potential, but before we begin we must recover the $O ( c ^ { - 2 } )$ terms that were discarded back in Eq. (8.45); these were not needed previously, but they appear in the transformed version of $g _ { 0 0 }$ at order $c ^ { - 4 }$ . If we write $U ( t , x ^ { j } )$ as $U ( \bar { t } + c ^ { - 2 } \alpha + \cdot \cdot \cdot , \bar { x } ^ { j } + r ^ { j } + c ^ { - 2 } h ^ { j } + \cdot \cdot \cdot \cdot )$ and expand to first order in $c ^ { - 2 }$ , we obtain

$$
U ( t , x ^ { j } ) = \hat { U } + \frac { 1 } { c ^ { 2 } } \alpha \Bigl ( \partial _ { \bar { t } } \hat { U } - v ^ { j } \partial _ { \bar { \jmath } } \hat { U } \Bigr ) + \frac { 1 } { c ^ { 2 } } h ^ { j } \partial _ { \bar { \jmath } } \hat { U } + O ( c ^ { - 4 } ) ;
$$

the right-hand side is expressed as a function of $( \bar { t } , \bar { x } ^ { j } )$ , and we have used Eqs. (8.47) and (8.48) to relate the partial derivatives of $U$ to those of $\hat { U }$ . After substitution of Eq. (8.49) into Eq. (8.34a) we find that the new post-Newtonian potential must be given by

$$
\begin{array} { l } { { \displaystyle \bar { \Psi } = \hat { \Psi } + 2 v ^ { 2 } \hat { \cal U } + \alpha \partial _ { \bar { t } } \hat { \cal U } + ( h ^ { j } - \alpha v ^ { j } ) \partial _ { \bar { \cal J } } \hat { \cal U } - 4 v _ { j } \hat { \cal U } ^ { j } } } \\ { { \displaystyle ~ + \frac { 1 } { 2 } ( \partial _ { \bar { t } } \alpha ) ^ { 2 } - v ^ { 2 } \partial _ { \bar { t } } \alpha + \frac { 1 } { 4 } v ^ { 4 } - \partial _ { \bar { t } } \beta + v _ { j } \partial _ { \bar { t } } h ^ { j } . } } \end{array}
$$

After taking into account Eqs. (8.42) and (8.51), we finally arrive at

$$
\begin{array} { r l r } {  { \bar { \Psi } = \hat { \Psi } - 4 v _ { j } \hat { U } ^ { j } + 2 v ^ { 2 } \hat { U } + \bigl ( A + v _ { k } \bar { x } ^ { k } \bigr ) \partial _ { \bar { t } } \hat { U } + \Bigl ( F ^ { j } + F _ { k } ^ { j } \bar { x } ^ { k } + \frac 1 2 F _ { k n } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } \Bigr ) \partial _ { \bar { \jmath } } \hat { U } } } \\ & { } & \\ & { } & { \qquad + G + G _ { j } \bar { x } ^ { j } + \frac 1 2 G _ { j k } \bar { x } ^ { j } \bar { x } ^ { k } - \partial _ { \bar { t } } \beta , \qquad ( \hat { \tilde { \mathcal { E } } } ^ { j } + F _ { k } ^ { j } \bar { x } ^ { k } + \frac 1 2 F _ { k n } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } \Bigr ) \partial _ { \bar { \jmath } } \hat { U } } \end{array}
$$

with

$$
\begin{array} { l } { { F ^ { j } = H ^ { j } - A v ^ { j } , } } \\ { { F _ { k } ^ { j } = { - \delta _ { k } ^ { j } \Big ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } \Big ) - \frac { 1 } { 2 } v ^ { j } v _ { k } + \epsilon _ { k p } ^ { j } R ^ { p } , } } } \\ { { F _ { k n } ^ { j } = - { \big ( \delta _ { k } ^ { j } a _ { n } + \delta _ { n } ^ { j } a _ { k } \big ) + \delta _ { k n } a ^ { j } } , } } \\ { { G = \frac { 1 } { 2 } \dot { A } ^ { 2 } - \dot { A } v ^ { 2 } + \frac { 1 } { 4 } v ^ { 4 } + \dot { H } ^ { j } v _ { j } , } } \\ { { G _ { j } = \Big ( \dot { A } - \frac { 1 } { 2 } v ^ { 2 } \Big ) a _ { j } - \Big ( \ddot { A } - \frac { 3 } { 2 } v ^ { k } a _ { k } \Big ) v _ { j } - \epsilon _ { j p q } v ^ { p } \dot { R } ^ { q } , } } \\ { { G _ { j k } = a _ { j } a _ { k } - v _ { j } \dot { a } _ { k } - \dot { a } _ { j } v _ { k } + \delta _ { j k } ( v _ { n } \dot { a } ^ { n } ) . } } \end{array}
$$

The hatted potential $\hat { \Psi }$ is defined by analogy with Eq. (8.44).

Our task of constructing the most general coordinate transformation that preserves the post-Newtonian form of the metric is now complete. At Newtonian order the transformation is characterized by an arbitrary translation $r ^ { j } ( \bar { t } )$ and a shift $\alpha = A ( \bar { t } ) + v _ { j } ( \bar { t } ) \bar { x } ^ { j }$ of the time coordinate at order $c ^ { - 2 }$ . At post-Newtonian order the transformation involves an additional component $H ^ { j } ( \bar { t } )$ to the translation, as well as a rotation governed by the vector $R ^ { j } ( \bar { t } )$ . In addition, the transformation involves an arbitrary shift $\beta ( \bar { t } , \bar { x } ^ { j } )$ of the time coordinate at order $c ^ { - 4 }$ . All in all we have ten arbitrary functions of time, and one free function $\beta$ of all the coordinates. The transformed potentials $\bar { U }$ , $\bar { U } ^ { j }$ , and $\bar { \Psi }$ are obtained from the old ones by employing Eqs. (8.46), (8.54), and (8.58), respectively.

# 8.3.4 Harmonic transformations

The general transformation of the preceding subsection does not, in general, preserve the harmonic condition of Eq. (8.21). It is possible, however, to specialize $\beta ( \bar { t } , \bar { x } ^ { j } )$ so that we also have

$$
\partial _ { \bar { t } } { \bar { U } } + \partial _ { \bar { \jmath } } { \bar { U } } ^ { j } = 0
$$

in the new coordinates. This restriction of the coordinate freedom defines what we shall call the class of harmonic coordinate transformations.

In view of Eq. (8.47) we find that the harmonic condition is

$$
\partial _ { \bar { t } } \hat { U } - v ^ { j } \partial _ { \bar { \jmath } } \hat { U } + \partial _ { \bar { \jmath } } \hat { U } ^ { j } = 0
$$

when it is expressed in terms of the hatted potentials. If we substitute Eqs. (8.46) and (8.54) into Eq. (8.60) and make use of Eq. (8.61), we find that the harmonic condition is preserved when $\beta$ satisfies the Poisson equation

$$
\bar { \nabla } ^ { 2 } \beta = \ddot { A } + \dot { a } _ { j } \bar { x } ^ { j } .
$$

Here ${ \bar { \nabla } } ^ { 2 }$ is the Laplacian operator in the coordinates $\bar { x } ^ { j }$ . The general solution to this equation is the sum of a particular solution and the general solution to Laplace’s equation. The particular solution must be cubic in the coordinates, and we construct it with the help of the ansatz $\textstyle { \frac { 1 } { 2 } } C _ { j k } { \bar { x } } ^ { j } { \bar { x } } ^ { k } + { \frac { 1 } { 6 } } C _ { j k n } { \bar { x } } ^ { j } { \bar { x } } ^ { k } { \bar { x } } ^ { n }$ , in which $C _ { j k }$ and $C _ { j k m }$ depend on $\bar { t }$ and are completely symmetric tensors. This property and the differential equation imply that $\begin{array} { r } { C _ { j k } = \frac 1 3 \delta _ { j k } \ddot { A } } \end{array}$ and $\begin{array} { r } { C _ { j k n } = \frac { 1 } { 5 } ( \delta _ { j k } \dot { a } _ { n } + \delta _ { j n } \dot { a } _ { k } + \delta _ { k n } \dot { a } _ { j } ) } \end{array}$ . We have obtained

$$
\beta = \frac { 1 } { 6 } \ddot { \cal A } \delta _ { j k } \bar { x } ^ { j } \bar { x } ^ { k } + \frac { 1 } { 3 0 } \big ( \delta _ { j k } \dot { a } _ { n } + \delta _ { j n } \dot { a } _ { k } + \delta _ { k n } \dot { a } _ { j } \big ) \bar { x } ^ { j } \bar { x } ^ { k } \bar { x } ^ { n } + \gamma ( \bar { t } , \bar { x } ^ { j } ) ,
$$

where $\gamma$ is any harmonic function that satisfies $\bar { \nabla } ^ { 2 } \gamma = 0$ .

Making the substitution in Eqs. (8.46), (8.54), and (8.58), we obtain the results listed in Box 8.2. [Note that the expressions for $V _ { j k } , \mathrm { \Delta } V _ { j k n } , \mathrm { \Delta } G _ { j k }$ , and $G _ { j k n }$ that appear in the Box are different from those given by Eqs. (8.55) and (8.59). The differences are accounted for by the terms generated by $\partial _ { \bar { J } } \beta$ and $\partial _ { \bar { t } } \beta$ .] The transformation is still characterized by the ten arbitrary functions of time that are contained in $A ( \bar { t } ) , r ^ { j } ( \bar { t } ) , H ^ { j } ( \bar { t } )$ , and $R ^ { j } ( \bar { t } )$ , but the remaining freedom is now restricted to a harmonic function $\gamma ( \bar { t } , \bar { x } ^ { j } )$ .

# 8.3.5 Comoving frame of a moving body

The general post-Newtonian transformations, and the restricted class of harmonic transformations, contain an enormous amount of freedom, and the transformations introduce spatially-growing terms in the potentials. For example, the transformation of the Newtonian potential is

$$
\bar { U } = \hat { U } - \dot { A } + \frac { 1 } { 2 } v ^ { 2 } - a _ { j } \bar { x } ^ { j } ,
$$

and the last term grows linearly with $\bar { r }$ . Similarly, $\bar { U } ^ { j }$ contains terms that grow like $\bar { r } ^ { 2 }$ , and in the harmonic case, $\bar { \Psi }$ grows like $\bar { r } ^ { 3 }$ . In view of this situation, a natural question to ponder is: what purpose is there in all this coordinate freedom?

We shall have occasion to give a more complete answer to this question in Sec. 9.4, but here we consider a simple application of the formalism that should illustrate its usefulness. We consider a spherical body of mass $m$ whose center-of-mass it situated at $x ^ { j } = r ^ { j } ( t )$ i n an inertial frame of reference. The body creates a gravitational potential $U _ { \mathrm { b o d y } }$ , and it is surrounded by an external matter distribution that creates a potential $U _ { \mathrm { e x t } }$ . The total potential is $U = U _ { \mathrm { b o d y } } + U _ { \mathrm { e x t } }$ , and we wish to examine its form in the non-inertial frame attached to the moving body. The coordinate transformation is given by $t = \bar { t } + c ^ { - 2 } \alpha + O ( c ^ { - 4 } )$ and $x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } ) + O ( c ^ { - 2 } )$ , with $\alpha = A ( \bar { t } ) + v _ { j } \bar { x } ^ { j }$ .

In the original (inertial) coordinates we have that the potential outside the body is given by

$$
U _ { \mathrm { b o d y } } = \frac { G m } { | \pmb { x } - \pmb { r } ( t ) | } .
$$

To simplify its expression we expand the external potential in a Taylor series about $x ^ { j } =$ $r ^ { j } ( t )$ :

$$
U _ { \mathrm { e x t } } = U ( t , r ^ { j } ) + ( x - r ) ^ { j } \partial _ { j } U _ { \mathrm { e x t } } ( t , r ^ { j } ) + \frac { 1 } { 2 } ( x - r ) ^ { j } ( x - r ) ^ { k } \partial _ { j k } U _ { \mathrm { e x t } } ( t , r ^ { j } ) + \cdot \cdot \cdot
$$

The hatted potentials are

$$
\hat { U } _ { \mathrm { b o d y } } = \frac { G m } { \bar { r } }
$$

and

$$
{ \hat { U } } _ { \mathrm { e x t } } = U _ { \mathrm { e x t } } ( { \bar { t } } , r ^ { j } ) + { \bar { x } } ^ { j } \partial _ { j } U _ { \mathrm { e x t } } ( { \bar { t } } , r ^ { j } ) + { \frac { 1 } { 2 } } { \bar { x } } ^ { j } { \bar { x } } ^ { k } \partial _ { j k } U _ { \mathrm { e x t } } ( { \bar { t } } , r ^ { j } ) + \cdot \cdot \cdot
$$

We see that the total potential $\hat { U } = \hat { U } _ { \mathrm { b o d y } } + \hat { U } _ { \mathrm { e x t } }$ naturally contains growing terms that are associated with the external matter, in addition to the decaying term that is associated with the reference body. Note that after each differentiation, the external potential is evaluated at $t = \bar { t }$ and $x ^ { j } = r ^ { j } ( \bar { t } )$ .

The transformed potential in the comoving frame of the body is $\bar { U } = \bar { U } _ { \mathrm { b o d y } } + \bar { U } _ { \mathrm { e x t } }$ , with

$$
\bar { U } _ { \mathrm { b o d y } } = \frac { G m } { \bar { r } }
$$

and

$$
\begin{array} { l } { { \displaystyle \bar { U } _ { \mathrm { e x t } } = \left[ U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) - \dot { A } + \frac 1 2 v ^ { 2 } \right] + \bar { x } ^ { j } \left[ a _ { j } - \partial _ { j } U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) \right] } } \\ { { \displaystyle ~ + \frac 1 2 \bar { x } ^ { j } \bar { x } ^ { k } \partial _ { j k } U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) + \cdot \cdot \cdot } } \end{array}
$$

We simplify this by first exploiting the coordinate freedom, which allows us to set

$$
\dot { A } = \frac { 1 } { 2 } v ^ { 2 } + U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) ;
$$

this is a differential equation that determines $A ( \bar { t } )$ up to an uninteresting constant of integration. We also make use of the fact that our body moves according to the Newtonian equations of motion, so that

$$
a _ { j } = \partial _ { j } U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) .
$$

We recall that $a ^ { j }$ stands for $d ^ { 2 } r ^ { j } / d \bar { t } ^ { 2 }$ .

Our end result for the comoving-frame gravitational potential is

$$
\bar { U } = \frac { G m } { \bar { r } } + \bar { U } _ { \mathrm { t i d a l } } ,
$$

where

$$
\bar { U } _ { \mathrm { t i d a l } } = \frac { 1 } { 2 } \bar { x } ^ { j } \bar { x } ^ { k } \partial _ { j k } U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) + \cdot \cdot \cdot
$$

is what remains of the external potential. As its label indicates, it is this potential that is responsible for the tidal interaction between the moving body and the external matter distribution. The Newtonian physics of tidally deformed bodies was explored in some detail in Sec. 2.5.

The coordinate transformation that takes us from the inertial frame to the moving frame is

$$
t = \bar { t } + \frac { 1 } { c ^ { 2 } } \int \left[ \frac { 1 } { 2 } v ^ { 2 } + U _ { \mathrm { e x t } } ( \bar { t } , r ^ { j } ) \right] d \bar { t } + \frac { 1 } { c ^ { 2 } } v _ { j } ( \bar { t } ) \bar { x } ^ { j } + O ( c ^ { - 4 } )
$$

and

$$
x ^ { j } = \bar { x } ^ { j } + r ^ { j } ( \bar { t } ) + O ( c ^ { - 2 } ) .
$$

The transformation can of course be generalized to post-Newtonian order, and we go through this exercise in Sec. 9.4.

# 8.3.6 Post-Galilean transformations

As we have seen, it can prove useful to exploit the full freedom contained in the general post-Newtonian transformations, or the restricted class of harmonic transformations, when one considers a bounded domain of spacetime such as the neighborhood of a moving body. When the considerations are global, however, the general freedom is too vast, and one would like to constrain it so as to eliminate the spatially-growing terms in the potentials. In this section we assume that the original potentials $U , U ^ { j }$ , and $\Psi$ vanish in the formal limit $r  \infty$ , and we specialize the post-Newtonian transformations so that the new potentials $\bar { U }$ , $\bar { U } ^ { j }$ , and $\bar { \Psi }$ share this property. This restricted class of coordinate transformations is known as the post-Galilean transformations of post-Newtonian theory. The name was coined by Chandrasekhar and Contopoulos in their classic 1967 paper.

# Construction

Inspection of Eq. (8.46) reveals that the Newtonian potential will grow linearly with $\bar { r }$ unless $a ^ { j } = 0$ . Discarding an uninteresting constant translation of the coordinates, this means that $r ^ { j } ( \bar { t } )$ must be of the form

$$
r ^ { j } = V ^ { j } \bar { t } ,
$$

with $V ^ { j }$ a constant vector. To eliminate the spatially-constant term in $\bar { U }$ we must also set $\begin{array} { r } { \dot { A } = \frac { 1 } { 2 } V ^ { 2 } } \end{array}$ , so that

$$
A = \frac { 1 } { 2 } V ^ { 2 } \bar { t } .
$$

Here $V ^ { 2 } : = \delta _ { j k } V ^ { j } V ^ { k }$ , and we again discard an uninteresting integration constant. These results imply that the post-Galilean transformation leaves the Newtonian potential invariant:

$$
{ \bar { U } } = { \hat { U } } ,
$$

where $\hat { U } = U ( \bar { t } , \bar { x } ^ { j } + V ^ { j } \bar { t } )$ .

Our results can be used to simplify the general expression for $\bar { U } ^ { j }$ , as it appears in Eq. (8.54). To keep $\bar { U } ^ { j }$ from growing we must set $\dot { R } ^ { j } = 0$ . The rotation of the coordinate axes described by $R ^ { j } ( \bar { t } )$ must therefore be constant in time, and we choose to eliminate this uninteresting freedom by setting

$$
R ^ { j } = 0 .
$$

To eliminate the spatially-constant term in $\bar { U } ^ { j }$ we set $\partial _ { \bar { J } } \beta = \dot { H } ^ { j }$ , which integrates to $\beta = \beta _ { 0 } ( \bar { t } ) + \dot { H } _ { j } \bar { x } ^ { j }$ , where $\beta _ { 0 }$ and $H ^ { j }$ are arbitrary functions of time. We observe that $\beta$ is a harmonic function, and that its expression is compatible with Eq. (8.63); the transformation is therefore within the class of harmonic transformations. With this result we find that the vector potential transforms as

$$
\bar { U } ^ { j } = \hat { U } ^ { j } - V ^ { j } \hat { U }
$$

under a post-Galilean transformation.

Moving on to $\bar { \Psi }$ , as it appears in Eq. (8.58), we find that the removal of the growing term requires $\ddot { H } ^ { j } = 0$ , so that $\dot { H } ^ { j }$ must be a constant vector. This vector is in principle arbitrary, but we choose to restrict the coordinate freedom by making it proportional to $V ^ { j }$ . We write it as $\begin{array} { r } { \dot { H } ^ { j } = \frac { 1 } { 2 } V ^ { 2 } V ^ { j } } \end{array}$ , inserting an arbitrary numerical coefficient of $\frac { 1 } { 2 }$ for reasons that will be made clear below, and the factor of $V ^ { 2 }$ for proper dimensionality. Our choice for $H ^ { j } ( \bar { t } )$ is therefore

$$
H ^ { j } = \frac { 1 } { 2 } V ^ { 2 } V ^ { j } { \bar { t } } .
$$

To eliminate the spatially-constant term in $\bar { \Psi }$ we must set $\begin{array} { r } { \dot { \beta } _ { 0 } = - \frac { 1 } { 8 } V ^ { 4 } + \dot { H } _ { j } V ^ { j } } \end{array}$ . With our previous choice for $H ^ { j }$ this is $\begin{array} { r } { \dot { \beta } _ { 0 } = \frac { 3 } { 8 } V ^ { 4 } } \end{array}$ , and our final expression for $\beta$ is

$$
\beta = \frac { 3 } { 8 } V ^ { 4 } \bar { t } + \frac { 1 } { 2 } V ^ { 2 } V _ { j } \bar { x } ^ { j } .
$$

With all this we find that the post-Newtonian potential transforms as

$$
\bar { \Psi } = \hat { \Psi } - 4 V _ { j } \hat { U } ^ { j } + 2 V ^ { 2 } \hat { U } + \bigg ( \frac { 1 } { 2 } V ^ { 2 } \bar { t } + V _ { j } \bar { x } ^ { j } \bigg ) \partial _ { \bar { t } } \hat { U } - \bigg ( \frac { 1 } { 2 } V ^ { j } V _ { k } \bar { x } ^ { k } \bigg ) \partial _ { \bar { \jmath } } \hat { U }
$$

under a post-Galilean transformation. We note that the terms involving $\partial _ { \bar { t } } \hat { U }$ and $\partial _ { \bar { \jmath } } \hat { U }$ are multiplied by quantities that grow linearly with $\bar { r }$ . Because $\hat { U }$ decays as $\bar { r } ^ { - 1 }$ , and its derivatives as $\bar { r } ^ { - 2 }$ , we see that $\bar { \Psi }$ properly vanishes in the formal limit $\bar { r } \to \infty$ .

Collecting results, we find that the post-Galilean transformation is a three-parameter family described by

$$
\begin{array} { l } { { \displaystyle t = \left( 1 + \frac { 1 } { 2 } \frac { V ^ { 2 } } { c ^ { 2 } } + \frac { 3 } { 8 } \frac { V ^ { 4 } } { c ^ { 4 } } \right) \bar { t } + \frac { 1 } { c ^ { 2 } } \bigg ( 1 + \frac { 1 } { 2 } \frac { V ^ { 2 } } { c ^ { 2 } } \bigg ) V _ { j } \bar { x } ^ { j } + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle x ^ { j } = \bigg ( \delta _ { k } ^ { j } + \frac { 1 } { 2 } \frac { V ^ { j } V _ { k } } { c ^ { 2 } } \bigg ) \bar { x } ^ { k } + \bigg ( 1 + \frac { 1 } { 2 } \frac { V ^ { 2 } } { c ^ { 2 } } \bigg ) V ^ { j } \bar { t } + { \cal O } ( c ^ { - 4 } ) ; } } \end{array}
$$

the parameters are the three components of the vector $V ^ { j }$ . This is nothing but a Lorentz transformation expanded in powers of $( V / c ) ^ { 2 }$ . The coordinates $( \bar { t } , \bar { x } ^ { j } )$ define a frame $\bar { S }$ that is boosted with respect to the original frame $S$ ; the boost takes place in the direction of the velocity vector $V ^ { j }$ .

# Boosted potentials

In the foregoing discussion the boosted potentials $\bar { U } , \bar { U } ^ { j }$ , and $\bar { \Psi }$ were expressed in terms of the “hatted potentials” $\hat { U } , \hat { U } ^ { j }$ , and $\hat { \Psi }$ ; these, we recall, are the original potentials evaluated at time $t = \bar { t }$ and position $x ^ { j } = \bar { x } ^ { j } + V ^ { j } \bar { t } .$ . This representation of the transformed potentials was optimal in the context of the general theory of post-Newtonian transformations, as developed in the previous sections. It is not optimal in the restricted context of post-Galilean transformations, because of the schizophrenic nature of the hatted potentials, which live partly in the frame $S$ and partly in the frame $\bar { S } .$ . An indication that the representation is indeed not optimal comes from our previous expression for $\bar { \Psi }$ , which displays a curious and unwanted explicit dependence upon $\bar { t }$ and $\bar { x } ^ { j }$ .

We therefore proceed differently. We shall (i) postulate plausible expressions for the transformed potentials $\bar { U }$ , $\bar { U } ^ { j }$ , and $\bar { \Psi }$ ; (ii) relate these to the original potentials $U , U ^ { j }$ , and $\Psi$ ; and (iii) show that under the transformation of Eqs. (8.85), the transformed metric $\bar { g } _ { \alpha \beta }$ keeps the standard post-Newtonian form of Eq. (8.20), with the understanding that the new metric is expressed in terms of the new potentials.

Our proposed expressions for the transformed potentials are

$$
\begin{array} { l } { { \bar { U } ( \bar { t } , \bar { x } ) = G \displaystyle \int \displaystyle \frac { \bar { \rho } ^ { s } ( \bar { t } , \bar { x } ^ { \prime } ) } { | \bar { x } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } , } } \\ { { \bar { U } ^ { j } ( \bar { t } , \bar { x } ) = G \displaystyle \int \displaystyle \frac { \bar { \rho } ^ { s } \bar { v } ^ { j } ( \bar { t } , \bar { x } ^ { \prime } ) } { | \bar { x } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } , } } \\ { { \bar { \psi } ( \bar { t } , \bar { x } ) = G \displaystyle \int \displaystyle \frac { \bar { \rho } ^ { s } ( \frac { 3 } { 2 } \bar { v } ^ { 2 } - \bar { U } + \bar { \Pi } + 3 \bar { p } / \bar { \rho } ^ { * } ) ( \bar { t } , \bar { x } ^ { \prime } ) } { | \bar { x } - \bar { x } ^ { \prime } | } d ^ { 3 } \bar { x } ^ { \prime } , } } \\ { { \bar { X } ( \bar { t } , \bar { x } ) = G \displaystyle \int \rho ^ { * } ( \bar { t } , \bar { x } ^ { \prime } ) | \bar { x } - \bar { x } ^ { \prime } | d ^ { 3 } \bar { x } ^ { \prime } , } } \end{array}
$$

and the transformed post-Newtonian potential is $\begin{array} { r } { \bar { \Psi } = \bar { \psi } + \frac 1 2 \partial _ { \bar { t } \bar { t } } \bar { X } } \end{array}$ . These expressions are natural: the new potentials are defined just as the old potentials in terms of the boosted coordinates and the fluid variables $\bar { \rho } ^ { * } , \bar { p } , \bar { \Pi }$ , and $\bar { \pmb { v } }$ that would be measured in the frame $\bar { S }$ instead of the original frame $S$ . It is useful to introduce transformed versions of the auxiliary potentials listed in Eqs. (8.8); in terms of these we have $\bar { \Psi } = 2 \bar { \Phi } _ { 1 } - \bar { \Phi } _ { 2 } + \bar { \Phi } _ { 3 } +$ $4 \bar { \Phi } _ { 4 } - { \textstyle \frac 1 2 } \bar { \Phi } _ { 5 } - { \textstyle \frac 1 2 } \bar { \Phi } _ { 6 }$ .

Our first task is to express the old Newtonian potential $U ( t , { \boldsymbol { x } } )$ in terms of the new potentials. This is not entirely straightforward. A major source of subtlety is the important fact that in Eqs. (8.86), the integration variables $\bar { x } ^ { \prime }$ describe the position of a fluid element at time $\bar { t }$ , the same time at which the potentials are being evaluated. The spacetime events $P$ and $P ^ { \prime }$ , respectively labeled by the coordinates $( { \bar { t } } , { \bar { { \boldsymbol { x } } } } )$ and $( \bar { t } , \bar { { \boldsymbol { x } } } ^ { \prime } )$ , are simultaneous in the frame $\bar { S } .$ . But they are not simultaneous in the original frame $S$ , and we must take this property carefully into account.

We examine the situation in the original frame $S$ (see Fig. 8.1). The figure shows a spacetime diagram in which we display the field point $P$ as well as the world line of a selected fluid element. Two events are shown on this world line: the source point $Q ^ { \prime }$ is simultaneous with $P$ in the frame $S$ , while $P ^ { \prime }$ is simultaneous with $P$ in the frame $\bar { S }$ . In the frame $S$ the coordinates of $P$ are $( t , \boldsymbol { x } )$ , the coordinates of $Q ^ { \prime }$ are $( t , \boldsymbol { x } ^ { \prime } )$ , and the coordinates of $P ^ { \prime }$ are $( \tau , \pmb { \xi } )$ . In the frame $\bar { S }$ the coordinates of $P$ are $( { \bar { t } } , { \bar { { \boldsymbol { x } } } } )$ , the coordinates of $Q ^ { \prime }$ are $( \bar { \tau } , \bar { \pmb \xi } )$ , and the coordinates of $P ^ { \prime }$ are $( \bar { t } , \bar { { \boldsymbol { x } } } ^ { \prime } )$ . Note that the coordinates $( \tau , \pmb { \xi } )$ and $( \bar { \tau } , \bar { \pmb \xi } )$ refer to different events in spacetime. In the frame $S$ the world line is described by the time-dependent position vector $r$ ; we have that $x ^ { \prime } : = r ( t )$ and $\pmb { \xi } : = \pmb { r } ( \tau )$ . In the frame $\bar { S }$ the world line is described by $\bar { r }$ , and we have that $\bar { x } ^ { \prime } : = \bar { r } ( \bar { t } )$ and $\bar { \pmb \xi } : = \bar { \pmb r } ( \bar { \tau } )$ . In the frame $S$ the velocity of the fluid element at $Q ^ { \prime }$ is $\pmb { v } ^ { \prime } : = \pmb { \dot { r } } ( t )$ , while in $\bar { S }$ the velocity of the fluid element at $P ^ { \prime }$ is $\bar { \pmb { v } } ^ { \prime } : = \dot { \bar { \pmb { r } } } ( \bar { t } )$ ; the overdots indicate differentiation with respect to the relevant time variable.

The coordinates of the field point $P$ transform as in Eq. (8.85). The coordinates of the source point $Q ^ { \prime }$ transform as

$$
\begin{array} { l } { { \displaystyle t = \left( 1 + \frac { 1 } { 2 } \frac { V ^ { 2 } } { c ^ { 2 } } + \frac { 3 } { 8 } \frac { V ^ { 4 } } { c ^ { 4 } } \right) \bar { \tau } + \frac { 1 } { c ^ { 2 } } \biggl ( 1 + \frac { 1 } { 2 } \frac { V ^ { 2 } } { c ^ { 2 } } \biggr ) V _ { j } \bar { \xi } ^ { j } + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle x ^ { \prime j } = \biggl ( \delta _ { \ k } ^ { j } + \frac { 1 } { 2 } \frac { V ^ { j } V _ { k } } { c ^ { 2 } } \biggr ) \bar { \xi } ^ { k } + \biggl ( 1 + \frac { 1 } { 2 } \frac { V ^ { 2 } } { c ^ { 2 } } \biggr ) V ^ { j } \bar { \tau } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

![](images/7487b40fdde5f364b27e07d8c283c0a05afaea84047210d19e625e48a7eb956f.jpg)  
World line of a selected fluid element viewed in the frame S. The grey plane is a hypersurface $t =$ constant, and the white plane is a hypersurface $\bar { t } =$ constant. The field point $P { \bf i } s$ simultaneous with $Q ^ { \prime }$ in S, but it is simultaneous with $P ^ { \prime }$ in the frame ¯S.

We want to express $\mathbf { { \boldsymbol { x } } ^ { \prime } }$ in terms of $\bar { t } , \bar { x }$ , and $\bar { x } ^ { \prime }$ , and this requires elimination of $\bar { \tau }$ and $\bar { \pmb \xi }$ from Eqs. (8.87b). To achieve this we equate the $t$ of Eqs. (8.85) with the $t$ of Eqs. (8.87) and deduce that $\bar { \tau } = \bar { t } + c ^ { - 2 } V _ { j } ( \bar { x } - \bar { \xi } ) ^ { j } + O ( c ^ { - 4 } )$ . We substitute this into the world-line equation $\bar { \pmb \xi } = \bar { \pmb r } ( \bar { \tau } )$ and get $\bar { \xi } ^ { j } = \bar { x } ^ { \prime j } + c ^ { - 2 } \bar { v } ^ { \prime j } V _ { k } ( \bar { x } - \bar { \xi } ) ^ { k } + O ( c ^ { - 4 } )$ . Collecting results, we have obtained

$$
\begin{array} { l } { { \displaystyle \bar { \tau } = \bar { t } + \frac { V _ { k } } { c ^ { 2 } } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } + { \cal O } ( c ^ { - 4 } ) , } } \\ { { \displaystyle \bar { \xi } ^ { j } = \bar { x } ^ { \prime j } + \frac { v ^ { \prime j } V _ { k } } { c ^ { 2 } } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

These are the coordinates of $Q ^ { \prime }$ in the frame $\bar { S }$ , expressed in terms of the coordinates of both $P$ and $P ^ { \prime }$ . Making the substitution in Eq. (8.87b), we arrive at

$$
x ^ { \prime \dot { \jmath } } = \bar { x } ^ { \prime \dot { \jmath } } + V ^ { j } \bar { t } + \frac { 1 } { c ^ { 2 } } \big ( \bar { v } ^ { \prime \dot { \jmath } } + V ^ { j } \big ) V _ { k } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } + \frac { V ^ { j } } { 2 c ^ { 2 } } \big ( V ^ { 2 } \bar { t } + V _ { k } \bar { x } ^ { \prime k } \big ) + O ( c ^ { - 4 } ) ,
$$

the desired relation between $\mathbf { \Delta } _ { \mathbf { { x } ^ { \prime } } }$ and the coordinates of $P$ and $P ^ { \prime }$ in the frame $\bar { S }$ . To this equation we can adjoin

$$
v ^ { \prime j } = \bar { v } ^ { \prime j } + V ^ { j } + O ( c ^ { - 2 } ) ,
$$

the law of composition of velocities (truncated to the leading, Newtonian order). It follows from Eqs. (8.85) and (8.89) that

$$
\frac { 1 } { | x - x ^ { \prime } | } = \frac { 1 } { | \bar { x } - \bar { x } ^ { \prime } | } + \frac { 1 } { c ^ { 2 } } \Big ( \bar { v } _ { j } ^ { \prime } V _ { k } + \frac { 1 } { 2 } V _ { j } V _ { k } \Big ) \frac { ( \bar { x } - \bar { x } ^ { \prime } ) ^ { j } ( \bar { x } - \bar { x } ^ { \prime } ) ^ { k } } { | \bar { x } - \bar { x } ^ { \prime } | ^ { 3 } } + O ( c ^ { - 4 } ) ,
$$

and this is an important ingredient that enters the transformation of the Newtonian potential.

Another important ingredient is the statement that $\rho ^ { * } d ^ { 3 } x$ is invariant under the post-Galilean transformation. We express this as

$$
\rho ^ { * } ( t , x ^ { \prime } ) d ^ { 3 } x ^ { \prime } = \bar { \rho } ^ { * } ( \bar { t } , \bar { x } ^ { \prime } ) d ^ { 3 } \bar { x } ^ { \prime } .
$$

The invariance of $d m : = \rho ^ { * } d ^ { 3 } x$ reflects the simple fact that $d m$ is the conserved rest-mass of a fluid element. Because this cannot be altered by a coordinate transformation, we have that $d m ( Q ^ { \prime } ) = d \bar { m } ( Q ^ { \prime } )$ , or $d m ( t , x ^ { \prime } ) = d \bar { m } ( \bar { \tau } , \bar { \pmb { \xi } } )$ . And because dm¯ does not change as we follow the motion of the fluid element, we also have that $d \bar { m } ( Q ^ { \prime } ) = d \bar { m } ( P ^ { \prime } )$ , or $d \bar { m } ( \bar { \tau } , \bar { \pmb { \xi } } ) =$ $d \bar { m } ( \bar { t } , \bar { x } ^ { \prime } )$ . We therefore arrive at Eq. (8.92), which is just the combined statement that $d m ( Q ^ { \prime } ) = d \bar { m } ( P ^ { \prime } )$ .

More formally, $d m ( Q ^ { \prime } ) = d \bar { m } ( Q ^ { \prime } )$ is a consequence of the facts that (i) the proper mass density $\rho$ is a scalar quantity; (ii) the spacetime volume element ${ \sqrt { - g } } d t d ^ { 3 } x$ is invariant under a coordinate transformation; and (iii) the element of proper time $d \lambda$ along the world line also is an invariant. From all this it follows that $\rho \sqrt { - g } ( d t / d \lambda ) d ^ { 3 } x = : \rho ^ { * } d ^ { 3 } x$ is invariant under the transformation. On the other hand, that $d \bar { m } ( Q ^ { \prime } ) = \mathrm { d } \bar { m } ( P ^ { \prime } )$ follows formally from an application of the continuity equation, Eq. (7.3), to a single fluid element. The formal route also gives rise to the statement of Eq. (8.92).

When we substitute Eqs. (8.91) and (8.92) into the integral definition of the old Newtonian potential $U ( t , x )$ , we find that it can be expressed in terms of the new potentials as

$$
U = \left( 1 + \frac { V ^ { 2 } } { 2 c ^ { 2 } } \right) \bar { U } + \frac { V ^ { j } } { c ^ { 2 } } \bar { \Phi } _ { j } - \frac { V ^ { j } V ^ { k } } { 2 c ^ { 2 } } \partial _ { \bar { j } \bar { k } } \bar { X } + O ( c ^ { - 4 } ) .
$$

Here $\bar { \Phi } _ { j }$ is the transformed version of the auxiliary potential defined by Eq. (8.8), and we make use of the identity of Eq. (8.11).

The remaining potentials transform in an analogous way. In fact, their transformation properties are much easier to identify, because here we do not need to calculate the correction terms of order $c ^ { - 2 }$ ; these impact the metric beyond the first post-Newtonian order. Taking into account Eq. (8.90) and the fact that $p$ and $\Pi$ transform as scalar quantities, we quickly obtain

$$
U ^ { j } = \bar { U } ^ { j } + V ^ { j } \bar { U } + O ( c ^ { - 2 } ) ,
$$

as well as

$$
\begin{array} { l } { { \Phi _ { 1 } = \bar { \Phi } _ { 1 } + 2 V ^ { j } \bar { U } _ { j } + V ^ { 2 } \bar { U } + O ( c ^ { - 2 } ) , } } \\ { { \Phi _ { 2 } = \bar { \Phi } _ { 2 } + O ( c ^ { - 2 } ) , } } \\ { { \Phi _ { 3 } = \bar { \Phi } _ { 3 } + O ( c ^ { - 2 } ) , } } \\ { { \Phi _ { 4 } = \bar { \Phi } _ { 4 } + O ( c ^ { - 2 } ) , } } \\ { { \Phi _ { 5 } = \bar { \Phi } _ { 5 } + O ( c ^ { - 2 } ) , } } \\ { { \Phi _ { 6 } = \bar { \Phi } _ { 6 } + 2 V ^ { j } \bar { \Phi } _ { j } + V ^ { 2 } \bar { U } - V ^ { j } V ^ { k } \partial _ { j \bar { k } } \bar { X } + O ( c ^ { - 2 } ) . } } \end{array}
$$

These equations imply that the post-Newtonian potential transforms as

$$
\Psi = \bar { \Psi } + V ^ { j } \big ( 4 \bar { U } _ { j } - \bar { \Phi } _ { j } \big ) + \frac { 3 } { 2 } V ^ { 2 } \bar { U } + \frac { 1 } { 2 } V ^ { j } V ^ { k } \partial _ { \bar { j } \bar { k } } \bar { X } + O ( c ^ { - 2 } )
$$

under a post-Galilean transformation.

Our final task is to verify that the transformed metric $\bar { g } _ { \alpha \beta }$ takes the standard post-Newtonian form of Eq. (8.20) when it is expressed in terms of the transformed potentials $\bar { U } , \ \bar { U } ^ { j }$ , and $\bar { \Psi }$ . This is straightforward. We first specialize the general transformation equations (8.34) to the post-Galilean case of Eqs. (8.85) and get the components $\bar { g } _ { 0 0 } =$ $- 1 + 2 c ^ { - 2 } U + 2 c ^ { - 4 } ( \Psi - U ^ { 2 } - 4 V ^ { j } U _ { j } + 2 V ^ { 2 } U ) + O ( c ^ { - 6 } ) , \bar { g } _ { 0 j } = - 4 c ^ { - 3 } ( U _ { j } - V _ { j } U ) \ : .$ + $O ( c ^ { - 5 } )$ , and $\bar { g } _ { j k } = \delta _ { j k } ( 1 + 2 c ^ { - 2 } U ) + O ( c ^ { - 4 } )$ for the new metric tensor. This is still expressed in terms of the old potentials, and we complete the calculation by involving Eqs. (8.93), (8.94), and (8.96). Our final result is

$$
\begin{array} { l l l } { { \displaystyle \bar { g } _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } \bar { U } + \frac { 2 } { c ^ { 4 } } \big ( \bar { \Psi } - \bar { U } ^ { 2 } \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle } } \\ { { \bar { g } _ { 0 j } = - \frac { 4 } { c ^ { 3 } } \bar { U } _ { j } + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle } } \\ { { \bar { g } _ { j k } = \bigg ( 1 + \frac { 2 } { c ^ { 2 } } \bar { U } \bigg ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

the statement that the transformed metric does indeed take the standard post-Newtonian form in terms of the proposed new potentials of Eqs. (8.86).

This completes our discussion of post-Galilean transformations. To sum up, we have established that a post-Galilean transformation describes a boost from a frame $S$ to a new frame $\bar { S }$ that moves relative to $S$ with a constant velocity $V$ . In this new frame the metric keeps its standard post-Newtonian form, but the potentials are now defined by Eqs. (8.86); they refer to the fluid variables $\bar { \rho } ^ { * }$ , $\bar { p } , \bar { \Pi }$ , and $\bar { \pmb { v } }$ that are measured in the new frame.

# 8.3.7 Pure-gauge transformations

Another interesting subclass of post-Newtonian transformations is obtained by setting

$$
A = r ^ { j } = H ^ { j } = R ^ { j } = 0
$$

and retaining only the freedom contained in $\beta$ . This class of transformations is described by

$$
\begin{array} { c } { { t = \bar { t } + \displaystyle { \frac { 1 } { c ^ { 4 } } \beta ( \bar { t } , \bar { x } ^ { j } ) + O ( c ^ { - 6 } ) } , } } \\ { { x ^ { j } = \bar { x } ^ { j } + O ( c ^ { - 4 } ) , } } \end{array}
$$

and the potentials change according to

$$
\begin{array} { c } { { \bar { U } = U , } } \\ { { \displaystyle \bar { U } ^ { j } = U ^ { j } + \frac { 1 } { 4 } \partial _ { \bar { \jmath } } \beta , } } \\ { { \bar { \Psi } = \Psi - \partial _ { \bar { t } } \beta . } } \end{array}
$$

In this case we no longer need to distinguish between the hatted potentials and their original expressions. Equations (8.100) take the appearance of an electromagnetic-type gauge transformation that links the potentials $U ^ { j }$ and $\Psi$ . We refer to this subclass of transformations as the pure-gauge transformations of post-Newtonian theory. When $\beta$ is a harmonic function, the gauge transformation converts a set of harmonic coordinates to another set of harmonic coordinates.

The transformation may be exploited to remove the superpotential term from $g _ { 0 0 }$ and put it instead in $g _ { 0 j }$ . We refer to the decomposition of Eq. (8.2), and to eliminate the term $\textstyle { \frac { 1 } { 2 } } \partial _ { t t } X$ from $g _ { 0 0 }$ we choose

$$
\beta = \frac { 1 } { 2 } \partial _ { \bar { t } } X .
$$

Note that this is not a harmonic function (because $\nabla ^ { 2 } X = 2 U$ ), so that the transformation does not preserve the harmonic coordinate condition. With this expression for $\beta$ we find that the new metric is given by

$$
\begin{array} { l } { { \displaystyle \bar { g } _ { 0 0 } = - 1 + \frac { 2 } { c ^ { 2 } } U + \frac { 2 } { c ^ { 4 } } \big ( \psi - U ^ { 2 } \big ) + { \cal O } ( c ^ { - 6 } ) , } } \\ { { \displaystyle \bar { g } _ { 0 j } = - \frac { 4 } { c ^ { 3 } } U _ { j } - \frac { 1 } { 2 c ^ { 3 } } \partial _ { \bar { t } \bar { \jmath } } X + { \cal O } ( c ^ { - 5 } ) , } } \\ { { \displaystyle \bar { g } _ { j k } = \bigg ( 1 + \frac { 2 } { c ^ { 2 } } U \bigg ) \delta _ { j k } + { \cal O } ( c ^ { - 4 } ) . } } \end{array}
$$

This choice of coordinate system defines the so-called standard gauge of post-Newtonian theory. As we have pointed out in the introductory section, this choice of gauge was popularized by Chandrasekhar, and it was once widely utilized by researchers in the post-Newtonian community. Like most current workers in the field, however, we prefer to use the harmonic gauge, and we have made this choice consistently throughout the book, except in Chapter 13 where we examine alternative theories of gravity. To be sure, the choice of gauge is mostly a matter of taste and convenience. But there are, nevertheless, important advantages in using the harmonic coordinates: it is in this gauge that post-Newtonian theory can naturally be embedded within the wider context of post-Minkowskian theory. And as we explained back in Sec. 8.2, it is by doing this that the foundations of post-Newtonian theory can be made secure.

# 8.4 Post-Newtonian hydrodynamics

# 8.4.1 Introduction

The dynamics of perfect fluids has been a recurring topic in this book. We examined this first in the context of Newtonian physics in Sec. 1.4, we gave the theory a special-relativistic formulation in Sec. 4.2, and we promoted this to curved spacetime in Sec. 5.3. In Sec. 7.1.1 we introduced the variables $\{ \rho ^ { * } , p , \Pi , \pmb { v } \}$ and incorporated slowly-moving fluids within the post-Minkowskian approximation.

In Sec. 7.1.1 we saw that the behavior of a perfect fluid is governed by the continuity equation

$$
\partial _ { t } \rho ^ { * } + \partial _ { j } ( \rho ^ { * } v ^ { j } ) = 0 ,
$$

and in Sec. 7.3.2 we got re-acquainted with the Euler equation of Chapter 1,

$$
{ \rho ^ { * } } \frac { d v ^ { j } } { d t } = \rho ^ { * } \partial _ { j } U - \partial _ { j } p + O ( c ^ { - 2 } ) .
$$

We recall that $\rho ^ { * } : = \sqrt { - g } \gamma \rho$ , with $\gamma : = u ^ { 0 } / c$ , is the conserved mass density, and at Newtonian order there is no distinction between this and the proper density $\rho ; v ^ { j }$ is the fluid’s velocity field, defined with respect to the time coordinate $t , p$ is the pressure, and ${ d } / { d t } = \partial _ { t } + \boldsymbol { v } ^ { k } \partial _ { k }$ is the Lagrangian time derivative. We recall also that the exact statement of the first law of thermodynamics for perfect fluids is $d \Pi = ( p / \rho ^ { 2 } ) d \rho$ , which we write as

$$
\frac { d \Pi } { d t } = \frac { p } { \rho ^ { * 2 } } \frac { d \rho ^ { * } } { d t } + { \cal O } ( c ^ { - 2 } ) .
$$

Here $\Pi$ is the internal energy of a fluid element divided by its mass.

In this section we calculate the post-Newtonian corrections to Euler’s equation (8.104). In addition, we derive expressions for the fluid’s conserved mass-energy $M$ , its total momentum $P ^ { j }$ , and its center-of-mass position $R ^ { j }$ . We shall not alter Eq. (8.103), which is exact, and we shall not need the $O ( c ^ { - 2 } )$ corrections to Eq. (8.105). In Chapter 9 we apply these results to situations in which the fluid breaks up into a number of separated components; this defines the post-Newtonian $N$ -body problem.

# 8.4.2 Energy-momentum conservation

The components of the energy-momentum tensor of a perfect fluid were listed back in Eq. (8.7). The equation of energy-momentum conservation is

$$
0 = \nabla _ { \beta } T ^ { \alpha \beta } = \partial _ { \beta } T ^ { \alpha \beta } + \Gamma _ { \mu \beta } ^ { \alpha } T ^ { \mu \beta } + \Gamma _ { \mu \beta } ^ { \beta } T ^ { \alpha \mu } ,
$$

and this can be simplified if we recall from Sec. 5.2 that $\Gamma _ { \mu \beta } ^ { \beta } = ( - g ) ^ { - 1 / 2 } \partial _ { \beta } ( - g ) ^ { 1 / 2 }$ . We therefore have

$$
0 = \partial _ { \beta } \big ( \sqrt { - g } T ^ { \alpha \beta } \big ) + \Gamma ^ { \alpha } _ { \beta \gamma } \big ( \sqrt { - g } T ^ { \beta \gamma } \big ) ,
$$

and this form of the conservation equation is optimal for the following computations. We recall that the square root of the metric determinant is given by $\sqrt { - g } = 1 + 2 c ^ { - 2 } U +$ $O ( c ^ { - 4 } )$ .

The zeroth component of Eq. (8.107) gives rise to a statement of energy conservation. When fully expanded the equation is

$$
\begin{array} { l } { { \displaystyle 0 = \frac { 1 } { c } \partial _ { t } \big ( \sqrt { - g } T ^ { 0 0 } \big ) + \partial _ { j } \big ( \sqrt { - g } T ^ { 0 j } \big ) } } \\ { { \displaystyle \qquad + \Gamma _ { 0 0 } ^ { 0 } \big ( \sqrt { - g } T ^ { 0 0 } \big ) + 2 \Gamma _ { 0 j } ^ { 0 } \big ( \sqrt { - g } T ^ { 0 j } \big ) + \Gamma _ { j k } ^ { 0 } \big ( \sqrt { - g } T ^ { j k } \big ) , } } \end{array}
$$

and this becomes

$$
\begin{array} { l } { { \displaystyle 0 = c \Big [ \partial _ { t } \rho ^ { * } + \partial _ { j } ( \rho ^ { * } v ^ { j } ) \Big ] } } \\ { { \displaystyle \quad + \frac { 1 } { c } \Bigg \lbrace \partial _ { t } \bigg [ \rho ^ { * } \Big ( \frac { 1 } { 2 } v ^ { 2 } + U + \Pi \Big ) \bigg ] + \partial _ { j } \bigg [ \rho ^ { * } v ^ { j } \Big ( \frac { 1 } { 2 } v ^ { 2 } + U + \Pi \Big ) \bigg ] } } \\ { { \displaystyle \qquad + \partial _ { j } ( p v ^ { j } ) - \rho ^ { * } \partial _ { t } U - 2 \rho ^ { * } v ^ { j } \partial _ { j } U \Bigg \rbrace + { \cal O } ( c ^ { - 3 } ) , } } \end{array}
$$

after inserting the components of $T ^ { \alpha \beta }$ and the Christoffel symbols of Eq. (8.15). At order $c$ we recover the continuity equation (8.103), and at order $c ^ { - 1 }$ we get

$$
0 = \rho ^ { * } \partial _ { t } \Big ( \frac { 1 } { 2 } v ^ { 2 } + \Pi \Big ) + \rho ^ { * } v ^ { j } \partial _ { j } \Big ( \frac { 1 } { 2 } v ^ { 2 } + \Pi \Big ) + \partial _ { j } ( p v ^ { j } ) - \rho ^ { * } v ^ { j } \partial _ { j } U
$$

after simplification. This is the equation that expresses the local conservation of energy within the fluid.

The spatial components of Eq. (8.107) provide a statement of momentum conservation. We write the equation in fully expanded form as

$$
\begin{array} { l } { \displaystyle 0 = \frac 1 c \partial _ { t } \big ( \sqrt { - g } T ^ { 0 j } \big ) + \partial _ { k } \big ( \sqrt { - g } T ^ { j k } \big ) } \\ { \displaystyle + \Gamma _ { 0 0 } ^ { j } \big ( \sqrt { - g } T ^ { 0 0 } \big ) + 2 \Gamma _ { 0 k } ^ { j } \big ( \sqrt { - g } T ^ { 0 k } \big ) + \Gamma _ { k n } ^ { j } \big ( \sqrt { - g } T ^ { k n } \big ) , } \end{array}
$$

and we eventually arrive at

$$
\begin{array} { l } { { 0 = \partial _ { t } ( \mu \rho ^ { * } v ^ { j } ) + \partial _ { k } ( \mu \rho ^ { * } v ^ { j } v ^ { k } ) + \partial _ { j } p - \rho ^ { * } \partial _ { j } U - \displaystyle \frac { \rho ^ { * } } { c ^ { 2 } } \biggl ( \frac { 3 } { 2 } v ^ { 2 } - 3 U + \Pi + p / \rho ^ { * } \biggr ) \partial _ { j } U } } \\ { { \mathrm { } + \displaystyle \frac { \rho ^ { * } } { c ^ { 2 } } \biggl [ 2 v _ { j } ( \partial _ { t } U + v ^ { k } \partial _ { k } U ) - 4 \partial _ { t } U _ { j } - 4 v ^ { k } ( \partial _ { k } U _ { j } - \partial _ { j } U _ { k } ) - \partial _ { j } \Psi \biggr ] + { \cal O } ( c ^ { - 4 } ) } } \end{array}
$$

after some algebra and simplification. We have introduced

$$
\mu : = 1 + \frac { 1 } { c ^ { 2 } } \Big ( \frac { 1 } { 2 } v ^ { 2 } + U + \Pi + p / \rho ^ { * } \Big ) + { \cal O } ( c ^ { - 4 } ) ,
$$

and Eq. (8.112) expresses the local conservation of momentum within the fluid.

# 8.4.3 Post-Newtonian Euler equation

We next work on Eq. (8.112) and bring it to the form of a relativistic generalization of Eq. (8.104). We begin with the observation that the first two terms on the right-hand side of Eq. (8.112) can be expressed as

$$
\partial _ { t } ( \mu \rho ^ { * } v ^ { j } ) + \partial _ { k } ( \mu \rho ^ { * } v ^ { j } v ^ { k } ) = \mu \rho ^ { * } \frac { d v ^ { j } } { d t } + \rho ^ { * } v ^ { j } \frac { d \mu } { d t }
$$

after making use of the continuity equation (8.103). If we make the substitution in Eq. (8.112) and truncate the result at Newtonian order, we recover

$$
\rho ^ { * } \frac { d v ^ { j } } { d t } = \rho ^ { * } \partial _ { j } U - \partial _ { j } p + { \cal O } ( c ^ { - 2 } ) ,
$$

the correct expression of Euler’s equation. We are therefore on the right track, and we may now retrieve the neglected terms of order $c ^ { - 2 }$ .

Differentiation of Eq. (8.113) yields

$$
{ \frac { d \mu } { d t } } = { \frac { 1 } { c ^ { 2 } } } \bigg ( v _ { j } { \frac { d v ^ { j } } { d t } } + { \frac { d U } { d t } } + { \frac { d \Pi } { d t } } + { \frac { 1 } { \rho ^ { * } } } { \frac { d p } { d t } } - { \frac { p } { \rho ^ { * 2 } } } { \frac { d \rho ^ { * } } { d t } } \bigg ) + { \cal O } ( c ^ { - 4 } ) ,
$$

and this becomes

$$
\frac { d \mu } { d t } = \frac { 1 } { c ^ { 2 } } \bigg ( \partial _ { t } U + 2 v ^ { k } \partial _ { k } U + \frac { 1 } { \rho ^ { * } } \partial _ { t } p \bigg ) + O ( c ^ { - 4 } )
$$

after insertion of Euler’s equation and Eq. (8.105).

Substitution of Eqs. (8.114) and (8.117) into Eq. (8.112) produces

$$
\begin{array} { c } { { \mu \rho ^ { * } \displaystyle \frac { d v ^ { j } } { d t } = - \partial _ { j } p + \rho ^ { * } \partial _ { j } U - \displaystyle \frac { 1 } { c ^ { 2 } } v ^ { j } \partial _ { t } p + \displaystyle \frac { 1 } { c ^ { 2 } } \rho ^ { * } \biggl ( \frac 3 2 v ^ { 2 } - 3 U + \Pi + \frac { p } { \rho ^ { * } } \biggr ) \partial _ { j } U } } \\ { { - \displaystyle \frac 1 { c ^ { 2 } } \rho ^ { * } \biggl [ v ^ { j } \bigl ( 3 \partial _ { t } U + 4 v ^ { k } \partial _ { k } U \bigr ) - 4 \partial _ { t } U _ { j } - 4 v ^ { k } \bigl ( \partial _ { k } U _ { j } - \partial _ { j } U _ { k } \bigr ) - \partial _ { j } \Psi \biggr ] + { \cal O } ( c ^ { - 4 } ) , } } \end{array}
$$

and this becomes

$$
\begin{array} { l } { { \rho ^ { * } \frac { d v ^ { j } } { d t } = - \partial _ { j } p + \rho ^ { * } \partial _ { j } U } } \\ { { \ \qquad + \frac { 1 } { c ^ { 2 } } \biggl [ \biggl ( \frac 1 2 v ^ { 2 } + U + \Pi + \frac { p } { \rho ^ { * } } \biggr ) \partial _ { j } p - v ^ { j } \partial _ { t } p \biggr ] } } \\ { { \ \qquad + \frac { 1 } { c ^ { 2 } } \rho ^ { * } \biggl [ ( v ^ { 2 } - 4 U ) \partial _ { j } U - v ^ { j } \bigl ( 3 \partial _ { t } U + 4 v ^ { k } \partial _ { k } U \bigr ) } } \\ { { \qquad + 4 \partial _ { t } U _ { j } + 4 v ^ { k } \bigl ( \partial _ { k } U _ { j } - \partial _ { j } U _ { k } \bigr ) + \partial _ { j } \Psi \biggr ] } } \\ { { \ \qquad + O ( c ^ { - 4 } ) } } \end{array}
$$

after multiplication of each side by $\mu ^ { - 1 }$ . Equation (8.119) is the post-Newtonian version of Euler’s equation. This equation, together with the continuity equation (8.103) and an equation of state relating the pressure, density, and internal energy, completely determines the behavior of a slowly-moving fluid in a weak gravitational field.

# 8.4.4 Interlude: Integral identities

We now interrupt the main development and establish a number of identities that will be required in the following discussion. We first derive the results displayed back in Eqs. (8.10), and next we shall prove the integral identities

$$
\begin{array} { l } { \displaystyle \int \rho ^ { * } \partial _ { t } U ^ { i } d ^ { 3 } x = 0 , } \\ { \displaystyle \int \rho ^ { * } U ^ { i } d ^ { 3 } x = \int \rho ^ { * } U ^ { i } d ^ { 3 } x , } \\ { \displaystyle \int \rho ^ { * } \partial _ { t } \psi ^ { i } d ^ { 3 } x = - \int \rho ^ { * } ( \frac { \partial } { \partial x ^ { i } } ) ^ { 2 } d ^ { 3 } x , } \\ { \displaystyle \int \rho ^ { * } \nu ^ { * } \partial _ { t } U ^ { i } = \frac { 1 } { 2 } \frac { d } { d t } \int \rho ^ { * } U ^ { i } d ^ { 3 } x , } \\ { \displaystyle \int \rho ^ { * } \nu ^ { * } \partial _ { t } U _ { i } d ^ { 3 } x = 0 , } \\ { \displaystyle \int \rho ^ { * } \nu ^ { * } \partial _ { t } \Phi _ { t } d ^ { 3 } x = 0 , } \\ { \displaystyle \int \rho ^ { * } \nu ^ { * } \partial _ { t } U ^ { i } d ^ { 3 } x = 0 , } \\ { \displaystyle \int \rho ^ { * } \nu ^ { * } \partial _ { t } U ^ { i } d ^ { 3 } x = \int \rho ^ { * } \Phi ^ { i } d ^ { 3 } x . } \end{array}
$$

The potentials $U , U ^ { j } , \psi$ , and $X$ are expressed in terms of the fluid variables in Eqs. (8.4);   
the auxiliary potential $\Phi ^ { j }$ was introduced in Eq. (8.8).

As a consequence of Eqs. (8.10) and (8.120b) we also find that

$$
\int \rho ^ { * } \bigl ( U \boldsymbol { v } _ { j } + \partial _ { t j } X \bigr ) d ^ { 3 } x = \int \rho ^ { * } \Phi _ { j } d ^ { 3 } x .
$$

And combining Eqs. (8.10), (8.120e), and (8.120f) yields

$$
\int \rho ^ { * } \boldsymbol { v } ^ { k } \partial _ { t j k } X d ^ { 3 } x = 0 ,
$$

another useful integral identity.

# Box 8.4

# Integration and time differentiation

The integral tricks reviewed here were first introduced back in Sec. 1.4.3. We recall that

$$
\frac { d } { d t } \int \rho ^ { * } f ( t , x ) d ^ { 3 } x = \int \rho ^ { * } \frac { d f } { d t } d ^ { 3 } x
$$

comes as an immediate consequence of the continuity equation (8.103); here $\rho ^ { * }$ is a function of $t$ and $x , f$ is an arbitrary function of its arguments, and $d f / d t = \partial _ { t } f + v ^ { k } \partial _ { k } f$ is its total time derivative. We generalize this identity by allowing $f$ to be a function of $\mathbf { \Delta } _ { x ^ { \prime } }$ also, and we define $F ( t , x ) : =$ $\textstyle \int \rho ^ { * \prime } f ( t , \pmb { x } , \pmb { x } ^ { \prime } ) d ^ { 3 } x ^ { \prime }$ , with $\rho ^ { * \prime }$ standing for $\rho ^ { * } ( t , x ^ { \prime } )$ . If we keep $_ { x }$ fixed in this equation, Eq. (1) tells us that

$$
\partial _ { t } F = \int { \rho ^ { * } } ^ { \prime } { \left( \partial _ { t } f + v ^ { \prime } { } ^ { k } \partial _ { k ^ { \prime } } f \right) } d ^ { 3 } x ^ { \prime } ,
$$

where $v ^ { \prime k }$ is the velocity field expressed as a function of $t$ and $\mathbf { \Delta } _ { x ^ { \prime } }$ , and $\partial _ { k ^ { \prime } }$ indicates partial differentiation with respect to the primed coordinates. The total time derivative of $F$ is $\partial _ { t } F + v ^ { k } \partial _ { k } F .$ , and this can be expressed as $\begin{array} { r } { \dot { { \mathbf { \psi } } } \cdot d { \cal F } / d t = \int \rho ^ { * \prime } ( \partial _ { t } f + v ^ { k } \partial _ { k } f + v ^ { \prime k } \partial _ { k ^ { \prime } } f ) d ^ { 3 } x ^ { \prime } . } \end{array}$ . The quantity within brackets is recognized as the total time derivative of the function $f ( t , x , x ^ { \prime } )$ , and we write our identity as

$$
\frac { d F } { d t } = \int \rho ^ { * \prime } \frac { d f } { d t } d ^ { 3 } x ^ { \prime } ,
$$

with $d f / d t = \partial _ { t } f + v ^ { k } \partial _ { k } f + v ^ { \prime k } \partial _ { k ^ { \prime } } f .$ . Finally, we define the function $\mathcal { F } ( t ) : =$ $\begin{array} { r } { \int \rho ^ { * } F ( t , x ) d ^ { 3 } x = \int \rho ^ { * } \rho ^ { * \prime } f ( t , x , x ^ { \prime } ) d ^ { 3 } x ^ { \prime } d ^ { 3 } x } \end{array}$ and insert $F$ in place of $f$ within Eq. (1). After also using Eq. (3) we obtain

$$
\frac { d \mathcal { F } } { d t } = \int \rho ^ { * } \rho ^ { * \prime } \frac { d f } { d t } d ^ { 3 } x ^ { \prime } d ^ { 3 } x ,
$$

with $d f / d t$ defined as in Eq. (3).

To establish these results we rely on the integral tricks reviewed in $\mathrm { B o x } ~ 8 . 4$ . To obtain Eqs. (8.10) we first differentiate $\begin{array} { r } { X = G \int \rho ^ { * \prime } | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } } \end{array}$ with respect to time. Using Eq. (2) of $\mathrm { B o x } 8 . 4$ , we find $\begin{array} { r } { \partial _ { t } X = G \int \rho ^ { * \prime } v ^ { \prime k } \partial _ { k ^ { \prime } } | \pmb { x } - \pmb { x } ^ { \prime } | d ^ { 3 } x ^ { \prime } } \end{array}$ , or

$$
\partial _ { t } X = - G \int \rho ^ { * \prime } v _ { k } ^ { \prime } \frac { ( x - x ^ { \prime } ) ^ { k } } { | x - x ^ { \prime } | } d ^ { 3 } x ^ { \prime } .
$$

We next differentiate this with respect to $x ^ { j }$ and get

$$
\partial _ { t j } X = - G \int \rho ^ { * \prime } v _ { k } ^ { \prime } \partial _ { j } \frac { ( x - x ^ { \prime } ) ^ { k } } { \vert x - x ^ { \prime } \vert } d ^ { 3 } x ^ { \prime } ,
$$