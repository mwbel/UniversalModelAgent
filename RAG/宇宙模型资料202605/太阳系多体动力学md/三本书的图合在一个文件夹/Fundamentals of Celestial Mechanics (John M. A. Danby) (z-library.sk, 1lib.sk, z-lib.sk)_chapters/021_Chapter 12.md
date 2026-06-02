# Chapter 12

# The Motion of the Moon

# 12.1Introduction

Roughly speaking, we can say that the Moon revolves around the Earth in an ellptic orbit with eccentricity 0.0549 and semimajor axis 0.002570 astronomical units,or 384,400 kilometers. The plane of the orbit is inclined to the ecliptic at an angle of $5 ^ { \circ } 9 ^ { \beta ^ { \prime } }$ ,but the node is regressing around the ecliptic, taking 18.60 years for a complete revolution. In the plane of the orbit the line of apsides advances,taking 8.85 years fora complete revolution. But if this information were used in the computation of an ephemeris of the Moon,the results would be hopelessly inadequate. In addition to the secular motions of the apsides and nodes,each element has considerable periodic variations; the position of the node can vary about its average motion by $\pm \sum \limits _ { i } ^ { n } 0 \sum \limits _ { j } ^ { n }$ ,and that of the line of apsides by $\pm 1 2 ^ { \circ } 2 0 ^ { \prime }$ The eccentricity varies by $\pm 0 . 0 1 7$ The inclination varies by $\pm \mathbb { 9 } ^ { \prime }$ Our ephemeris could be out by several degrees.

An adequate account of even any one lunar theory is outside the scope of this text. Instead we shall give a descriptive account based largely on the use of equations (11.5.13) for the variation of the elements. (Equations (11.9.9) were used by Poisson to investigate the motion of the Moon, but not to any great purpose.） To represent the Moon's motion adequately, solutions of a high order of approximation are needed; these require a prodigious amount of labor anyway, but the amount of work required in using the method of the variation of the elements would be prohibitive. But if this approach is almost useless for the development of an accurate lunar theory, it offers quick descriptions of the principal perturbations involved,and of their orders of magnitude.

The principal part of the problem of the lunar motion is to find the solution to the particular instance of the three-body problem presented by the system of the Earth,the Moon,and the Sun. A refined theory also includes the effects of the Earth's equatorial bulge, and of perturbations by the other planets. Here we shall consider only some first-order effects of the perturbations by the Sun on the motion of the Moon around the Earth. We shall adopt the provincial attitude of considering the Earth to be the most important body， and of referring to the

orbit of the Sun about the Earth.

# 12.2 The Perturbing Forces

In the notation of Figure 12.1, $E , M$ and $s$ are the Earth, Moon, and Sun, respectively， the perturbing function due to the action of the Sun is

$$
R = \vec { \kappa } ^ { 2 } \left\{ \frac { 1 } { \rho } - \frac { \mathbb { R } \cdot \vec { \kappa } } { \vec { \kappa } ^ { 3 } } \right\}
$$

and the perturbing force is

$$
\begin{array} { l } { { \displaystyle { \cal F } = { \cal S } { \mathbb { \tilde { \kappa } } } ^ { 2 } \left[ \frac { \rho } { \rho ^ { 3 } } - \frac { { \bf R } } { R ^ { 3 } } \right] } \ ~ } \\ { { \displaystyle ~ = { \cal S } k ^ { 2 } \left[ \frac { { \bf R } - { \bf r } } { \rho ^ { 3 } } - \frac { { \bf R } } { R ^ { 3 } } \right] } \ ~ } \\ { { \displaystyle ~ = { \cal S } k ^ { 2 } \left[ - \frac { { \bf r } } { \rho ^ { 3 } } + { \bf R } \left( \frac { 1 } { \rho ^ { 3 } } - \frac { 1 } { R ^ { 3 } } \right) \right] } , } \end{array}
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0161-0200/ocr/images/aa7989cd1a7ce05d7679509d0f8c0148772b44428dccb3aa6161ab3864c3c6f0.jpg)  
Figure 12.1

where $s$ is the mass of the Sun. This must be resolved in the usual directions to find the components Fr,Fb,and Fn.

Take a set of axes with directions x, $\hat { \mathbb { y } } , \hat { \mathbf { z } } ,$ where X points toward the vernal equinox and $\hat { \pmb z }$ toward the north pole of the ecliptic; also take a set with directions $\hat { \hat { \mathbf { z } } } , \hat { \mathbf { g } } , \hat { \mathbf { z } }$ where $\hat { \pmb { \xi } }$ points toward the ascending node $\underset { i = 1 } { \overset { \triangledown } { \mathbf { y } } }$ of the Moon's orbit, and $\hat { \bf \Phi } _ { \bf k }$ is perpendicular to the plane of the orbit, in the usual sense. Then

and

$$
\begin{array} { r } { \hat { \bar { \mathbf { r } } } = \hat { \bar { \mathbf { r } } } \cos { \psi } + \hat { \bar { \mathbf { g } } } \sin { \psi } , \quad \quad \quad } \\ { \quad \quad \quad } \\ { \hat { \bar { \mathbf { s } } } = \hat { \bar { \mathbf { r } } } \cos { \psi } + \left( \hat { \bar { \mathbf { z } } } \times \hat { \bar { \mathbf { f } } } \right) \sin { \psi } , \quad \quad \quad } \end{array}
$$

![](../chunks/Fundamentals of Celestial Mechanics (John M. A. Danby) (z-library.sk, 1lib.sk, z-lib.sk)_part_0005_pages_0161-0200/ocr/images/21374aeab3241e9a0385a6c2f3cb5cdf7ba14a443d5d34e23d6dd780e13771f8.jpg)  
Figure 12.2

where ∠NEM = u, and ∠NES= U. (See Figure 12.2.） Now (2× f） is a unit vector lying in the ecliptic, perpendicular to the ascending node,so that we have

$$
\hat { { \mathbf { z } } } \times \hat { { \mathbf { f } } } = \hat { { \mathbf { g } } } \cos i - \hat { { \mathbf { h } } } \sin i .
$$

Then

$$
\begin{array} { r } { \hat { \bf R } = \hat { \bf f } \cos \theta + \sin \theta ( \hat { \bf g } \cos i - \hat { \bf h } \sin i ) . } \end{array}
$$

The directions of F, Fb, and Fn are f, (h × r),and h,so that multiplying (12.2.1) scalarly by each of these in turn, and using (12.2.2),we find

$$
\begin{array} { r l r } & { } & { F _ { r } = S k ^ { 2 } \left[ - \cfrac { r } { \rho ^ { 3 } } + R ( \cos U \cos u + \sin U \sin u \cos i ) \left( \cfrac { 1 } { \rho ^ { 3 } } - \cfrac { 1 } { R ^ { 3 } } \right) \right] , } \\ & { } & { F _ { b } = S k ^ { 2 } \left[ \cfrac { R ( - \cos U \sin u + \sin U \cos u \cos i ) \left( \cfrac { 1 } { \rho ^ { 3 } } - \cfrac { 1 } { R ^ { 3 } } \right) } \right] , } \\ & { } & { F _ { \pi } = S k ^ { 2 } \left[ \cfrac { - R \sin U \sin i \left( \cfrac { 1 } { \rho ^ { 3 } } - \cfrac { 1 } { R ^ { 3 } } \right) } \right] . } \end{array}
$$

$\tilde { \psi }$ is the angle $\mathcal { S Z } ^ { \sharp / \sharp }$ , so that, from (12.2.1),

$$
F _ { r } = S \vec { \kappa } ^ { 2 } \left[ - \frac { \tau } { \rho ^ { 3 } } + \mathcal { R } \cos \psi \left( \frac { 1 } { \rho ^ { 3 } } - \frac { 1 } { R ^ { 3 } } \right) \right] ,
$$

and

$$
\cos \psi = \cos U \cos u + \sin U \sin u \cos i .
$$

Now

$$
\rho ^ { 2 } = \mathcal { R } ^ { 2 } + \ r ^ { 2 } - 2 r \mathcal { R } \cos \psi ;
$$

hence

$$
\begin{array} { c } { { \displaystyle \frac { \hat { \bf \Pi } _ { 1 } } { \rho ^ { 3 } } = \frac { \hat { \bf \Pi } _ { 1 } } { R ^ { 3 } } \left[ 1 - 2 \frac { r } { R } \cos \psi + \left( \frac { r } { R } \right) ^ { 2 } \right] ^ { - 3 / 2 } } } \\ { { = \displaystyle \frac { 1 } { R ^ { 3 } } \left[ \hat { \bf \Pi } ^ { \dagger } + 3 \frac { r } { R } \cos \psi \right] , } } \end{array}
$$

where terms in $( r / R ) ^ { 2 }$ have been neglected. Since $\Im \int \Re$ is approximately equal to $2 . 6 \times 1 0 ^ { - 3 }$ ,this neglect is well justified because we are dealing only in orders of magnitude. But this is equivalent to putting

$$
R = \rho \div \operatorname { v c o s } \psi ,
$$

or to assuming that $\mathbb { E } S$ is parallel to $\mathbb { M } S$ ;i.e.,we are neglecting the angle $\Xi S \tilde { \varepsilon }$ this is referred to as “neglecting the solar parallax.”From (12.2.9) we have

$$
{ \frac { \mathrm { i } } { \rho ^ { 3 } } } - { \frac { \mathrm { i } } { R ^ { 3 } } } = 3 { \frac { r } { R ^ { 4 } } } \cos \psi .
$$

Now $j$ expressed inradians,isapproximately $0 . 0 9$ Fora first approximation we can ignore terms in $i ^ { 2 }$ ,in which case we can put cos $\dot { z } = \vec { \mathfrak { z } }$ Then substituting (12.2.9) and (12.2.11) into the expressions for the $\pmb { \xi } ^ { \dagger } \mathbf { s }$ we find,eventually,

$$
\begin{array} { r l } & { F _ { r } = \frac { 1 } { 2 } N ^ { 2 } r \left[ \mathbb { 1 } + 3 \cos 2 ( u - U ) \right] , } \\ & { F _ { b } = - \frac { 3 } { 2 } N ^ { 2 } r \sin 2 ( u - U ) , } \\ & { F _ { n } = - 3 N ^ { 2 } r \sin i \sin U \cos ( u - U ) . } \end{array}
$$

Here we have put

$$
N ^ { 2 } = \frac { S \bar { \kappa } ^ { 2 } } { \bar { \kappa } ^ { 3 } } ,
$$

so that $\mathcal { N }$ is the mean motion of the Sun, assuming it to move in a circular orbit.

# 12.3 The Perturbation of the Nodes

The equation for the variation of $\Omega$ can be written

$$
{ \frac { d { \mathcal { D } } } { d t } } = { \frac { n a r } { \mu { \sqrt { 1 - e ^ { 2 } } } } } { \frac { \sin u } { \sin i } } { \mathcal { F } } _ { \pi } ,
$$

where $\mu = \mathbb { E } \bar { \mathbb { k } } ^ { 2 }$ ： $E$ being the mass of the Earth. If $\mathfrak { x }$ is the mean motion of the $N \sin 0 0 \pi$ ： $z i = n ^ { 2 } a ^ { 3 }$ Define m by

$$
\gamma \gamma = { \frac { N } { \gamma } } ;
$$

then $\mathfrak { m } = \mathfrak { O } . 0 7 4 8$ Substituting from (12.2.14) and introducing $\gamma _ { \parallel }$ we find

$$
\frac { 1 } { n } \frac { d \Omega } { d t } = - 3 m ^ { 2 } \frac { r ^ { 2 } } { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } \sin u \sin U \cos ( u - U ) .
$$

To find the first-order solution,we assume that all the elements involved on the right of (12.3.2) are constant; then the left-hand side is $\sin \beta / \sin \beta$ Also $u = \omega \pmb { \div } v$ and $\bar { \mathcal { V } } = \mathbb { V } \ne$ constant, where $\mathbb { V }$ applies to the orbit of the Sun. $\textit { \textbf { F } , \textit { \textbf { v } } }$ and $\bar { \pmb { \zeta } }$ can be expanded in powers of $\pmb { e }$ and $e _ { 3 }$ (the eccentricity of the orbit of the Sun), using the series of Section 6.14, so that the right-hand side of (12.3.2) can be expanded in such a series. (Allowance should also be made for the fact that (12.2.15) is not valid fora non-circular orbit.) This is simple in principle but laborious,even for low powers of e. For present purposes we shall neglect the eccentricities entirely; since $e = 0 . 0 5$ and $e _ { 1 } = \emptyset . 0 2$ we should expect, by neglecting the e's and their powers, to run the risk of an error of up to 8 percent. To this order of accuracy we have $z = a$ $v = M$ ,and $\gamma = \pi \lambda \mathcal { M }$ where we can put $U = \mathbb { V }$ (12.3.2) becomes

$$
\frac { d \Omega } { d t } = - 3 m ^ { 2 } \sin u \sin U \cos ( u - U ) ,
$$

which,after using some elementary trigonometry in order to sort out the constant from the purely periodic terms,we find to be

$$
\frac { d \Omega } { d M } = - { \textstyle \frac { 3 } { 4 } } m ^ { 2 } \left\{ 1 + \cos 2 ( u - U ) - \cos 2 u - \cos 2 U \right\} .
$$

Remembering the expressions for $\mathfrak { V }$ and $\pmb { \updownarrow }$ , we can integrate this to give

$$
\mathcal { Q } - \mathcal { D } _ { 0 } = - \frac { 3 } { 4 } m ^ { 2 } \left\{ M + \frac { 1 } { 2 ( 1 - m ) } \sin ( u - U ) - \frac { 1 } { 2 } \sin 2 u - \frac { 1 } { 2 m } \sin 2 U \right\} .
$$

The secular term is

$$
- \frac { 3 } { 4 } \pi ^ { 2 } \mathcal { M } .
$$

This gives a regression of the nodes through $2 \pi { \frac { 3 } { 4 } } m ^ { 2 }$ per anomalistic month. (The anomalistic month is measured from perigee to perigee, or by a complete cyele of $\Im$ due to the motion of the line of apsides, it is approximately 0.233 of a day longer than a sidereal month.） Then the nodes will move through 2πm per year, so that the time taken for a complete revolution is $4 / 3 m$ years, or 17.8 years. The error here is about 5 per cent; well within the margin we allowed. Tofind a more accurate value,e and e1 would have to be included. For a more accurate value still, we would proceed to a second-order solution, allowing for the variations of all the elements on the right of the equations.

The remaining terms in (12.3.3) are all periodic. The term with largest amplitude is

$$
\frac { 3 } { 8 } \pi \sin 2 \pi ,
$$

which has period half an anomalistic year (measured from perihelion to perihelion)and amplitude m radians or 1.6.

The time elapsing between successive passages of the Moon through a node is called a nodical or draconitic month,its length being 27.212 days.Since an eclipse of the Sun or Moon can only occur when the Sun,Earth,and Moon are nearly in a straight line, it must happen when the Moon is near a node and is either new or full. The term “draconitic” is due to the theory held at one time that the Sun is swallowed bya dragon at a time of total eclipse.Since the Sun must be near the line of nodes for an eclipse to take place,the interval between two successive passages of the Sun through a node is important in the prediction of eclipses; this interval is called an eclipse year and is equal to 346.62 days. Now

$$
\mathrm { 1 9 \ e c l i p s e \ y e a g s = 6 5 8 5 . 7 8 \ d a y s , }
$$

The period $6 5 8 5 \frac { 1 } { 3 }$ days,or about 18 years and $1 1 \frac { 1 } { 3 }$ days (depending on leap years), is called the Saros; it was known to ancient astronomers and,reputedly, used in the prediction of eclipses.It should not be confused with the period of the revolution of the nodes,although the two periods are indirectly related.

# 12.4The Perturbation of the Inclination

The equation for the variation of $\textit { \textbf { z } }$ can be written

$$
\frac { d i } { d \tilde { \mathcal { M } } } = \frac { a \tau } { \mu \sqrt { 1 - e ^ { 2 } } } \tilde { F } _ { n } \cos { \psi } .
$$

After substitution for $F _ { \pi }$ ,this becomes

$$
\frac { d i } { d \lambda M } = - 3 m ^ { 2 } \frac { r ^ { 2 } } { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } \sin i \sin U \cos u \cos ( u - U ) .
$$

Ignoring the eccentricities as before and simplifying the right-hand side, we find

$$
\frac { d i } { d M } = - \frac { 3 } { 4 } m ^ { 2 } \sin i \left\{ \sin 2 u + \sin 2 U - \sin ( u - U ) \right\} ,
$$

so that

$$
i - i _ { 0 } = \frac { 3 } { 8 } m ^ { 2 } \sin i \left\{ \cos 2 u + \frac { 1 } { m } \cos 2 U + \frac { 1 } { 1 - m } \cos 2 ( u - U ) \right\} .
$$

These terms are all periodic. That with largest amplitude is

$$
\frac { 3 } { 8 } \Im \Im \Im \Im \Im \Im \Im \Im \Im \Im \Im \Im \Im ,
$$

which has period half an anomalistic year and amplitude approximately ${ \mathfrak { G } } ^ { \prime }$

12.5 The Perturbations of $\omega$ and $\pmb { \mathcal { C } }$

Ignoring the square of the inclination, the equation for the variation of $\omega$ is

$$
\begin{array} { c } { { \displaystyle \frac { d \omega } { d M } = \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { \mu e } \left\{ - F _ { r } \cos v + F _ { b } \left( 1 + \frac { r } { p } \right) \sin v \right\} } } \\ { { = \displaystyle \frac { 1 } { 2 } m ^ { 2 } \frac { \sqrt { 1 - e ^ { 2 } } } { e } \frac { r } { a } \left\{ - \left[ 1 + 3 \cos 2 ( u - U ) \right] \cos v \right. } }  \\ { { \left. - 3 \sin 2 ( u - U ) \sin v \left( 1 + \frac { r } { p } \right) \right\} . } } \end{array}
$$

To find the secular terms, it is simplest to make use of the fact that we know that w does increase,so that over a long enough period of time (long, that is, compared with the period of rotation of the line of apsides), the terms with argument $2 ( \mathfrak { z } - \mathfrak { U } )$ or $2 \{ \omega \div v - \bar { U } \}$ in (12.5.1) will cancel themselves out and make no secular contribution (although they may be responsible for variations of long period). It follows that the secular variation comes only from

$$
\frac { d \omega ^ { \prime } } { d M } = - \frac { 1 } { 2 } \pi ^ { 2 } \frac { \sqrt { 1 - e ^ { 2 } } } { e } \frac { r } { a } \cos v .
$$

Now

$$
{ \boldsymbol { \tau } } \cos { \boldsymbol { v } } = a ( \cos { \mathcal { E } } - e ) ,
$$

and

$$
d \bar { M } = d \bar { E } ( \mathbb { 1 } - e \cos \bar { E } ) .
$$

So,

$$
\begin{array} { c } { { d \omega ^ { \prime } = - \displaystyle \frac 1 2 m ^ { 2 } \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } } { e } \left\{ \cos { E ( 1 + e ^ { 2 } ) } - e ( 1 + \cos ^ { 2 } { E } ) \right\} d E } } \\ { { = - \displaystyle \frac 1 2 m ^ { 2 } \displaystyle \frac { \sqrt { 1 - e ^ { 2 } } } { e } \left\{ \cos { E ( 1 + e ^ { 2 } ) } - \displaystyle \frac e 2 ( 3 + \cos { 2 E } ) \right\} d E . } } \end{array}
$$

We reject all periodic terms on the right-hand side and put E= M (since the difference between them is periodic), so that finally we find

$$
\begin{array} { r } { \omega _ { \mathrm { s e c } } = \omega _ { \mathrm { 0 ~ s e c } } + \frac { 3 } { 4 } \eta n ^ { 2 } M \sqrt { \mathrm { 1 } - e ^ { 2 } } . } \end{array}
$$

Certainly the line of apsides advances; but the motion given by (12.5.3) is nearly the same, in magnitude, as that found for the nodes: yet, the line of apsides actually moves over twice as fast as the line of nodes. The inability of the first-order solution to explain the observed motion was recognized by Newton: for many years after his death he was reputed to have given up the problem as a bad job, but it was found later that he had accounted for most of the observed motion by taking second-order effects into consideration. The most seriously perturbed element is e, which changes altogether by some 40 per cent. In fnding (12.5.3) we assumed that e was constant, and it is not surprising that the result is unreliable. It is usual to expand expressions in the lunar motion in powers of m; in the series for the rate of advance of perigee the first two terms are

$$
\textstyle { \frac { 3 } { 4 } } \mathtt { m } ^ { 2 } + { \frac { 2 2 5 } { 3 2 } } \mathtt { m } ^ { 3 } ;
$$

.this combination nearly accounts for the observed motion.

The right-hand side of (12.5.1) can be developed in powers of $\mathscr { e }$ in the form

$$
\frac { A } { e } + B + C e + D e ^ { 2 } + \cdots
$$

and if

$$
\omega = \frac { \omega _ { 1 } } { e } + \omega _ { 2 } + \omega _ { 3 } e + \omega _ { 4 } e ^ { 2 } + \cdot \cdot \cdot
$$

then we have

$$
{ \frac { 1 } { e } } { \frac { d \omega _ { 1 } } { d M } } = { \frac { A } { e } } = - { \frac { 1 } { 2 } } { \frac { m ^ { 2 } } { e } } \left\{ \left[ 1 + 3 \cos 2 ( u - U ) \right] \cos { M } + 6 \sin 2 ( u - U ) \sin { M } \right\} .
$$

Because of the appearance of $e$ in the denominator,we should expect this to provide the largest periodic perturbations of $\omega$ Substituting for $\gnapprox$ and simplifying,we find

$$
\frac { \mathtt { l } } { e } \frac { d \omega _ { 1 } } { d M } = - \frac { 1 } { 4 } \frac { m ^ { 2 } } { e } \left\{ 2 \cos M - 3 \cos ( 2 \omega - 2 U + 3 M ) + 9 \cos ( 2 \omega - 2 U + M ) \right\}
$$

which can be integrated to give

$$
\begin{array} { l } { \displaystyle \frac { 1 } { e } \big ( \omega _ { 1 } - \omega _ { 1 0 } \big ) = - \frac { 1 } { 4 } \frac { m ^ { 2 } } { e } \Bigg \{ 2 \sin { M } - \frac { 3 } { 3 - 2 m } \sin ( 2 \omega - 2 U + 3 M ) } \\ { \displaystyle \qquad + \frac { 9 } { 1 - 2 m } \sin ( 2 \omega - 2 U + { M } ) \Bigg \} . } \end{array}
$$

Finally, neglecting $\mathfrak { W }$ in the denominators,we find

$$
\frac { 1 } { e } ( \omega _ { 1 } - \omega _ { 1 0 } ) = - \frac { 1 } { 4 } \frac { m ^ { 2 } } { e } \left\{ 2 \sin { M } - \sin ( 2 \omega - 2 U + 3 M ) \right.  \\  \left. + 9 \sin ( 2 \omega - 2 U + M ) \right\} .
$$

From inspection it can be seen that the right-hand side achieves its maximum numerical value of $1 2 m ^ { 2 } / 4 e$ when $M = \pm 9 0 ^ { \circ }$ and $2 _ { \{ \omega - \ell \} } ^ { \prime } = 0$ The total amplitude of the oscillation is given by $\pm 3 m ^ { 2 } / e$ or士 $1 7 . 5 0$ ,which is too large by some 50 per cent.

The equation for the variation of $\varepsilon$ is

$$
\begin{array} { l } { \displaystyle \frac { d e } { d M } = \frac { a ^ { 2 } \sqrt { 1 - e ^ { 2 } } } { \mu } \left\{ \bar { F } _ { r } \sin v + \bar { F } _ { b } ( \cos v + \cos \bar { E } ) \right\} } \\ { = \displaystyle \frac { 1 } { 2 } m ^ { 2 } \sqrt { 1 - e ^ { 2 } } \frac { r } { a } \left\{ \left[ 1 + 3 \cos 2 ( u - U ) \right] \sin v \right. } \\ { \displaystyle \qquad \left. - 3 \sin 2 ( u - U ) ( \cos v + \cos \bar { E } ) \right\} . } \end{array}
$$

There are no secular terms. When powers of e on the right-hand side are ignored, this becomes

$$
\frac { d e } { d M } = \frac { 1 } { 4 } m ^ { 2 } \left\{ 2 \sin M - 3 \sin \left\{ 2 \omega - 2 U + 3 M \right\} - 9 \sin ( 2 \omega - 2 U + M ) \right\} .
$$

Integrating, and ignoring m in the denominators as before, we find

$$
\begin{array} { r } { e - e _ { 0 } = \frac { \frac { 1 } { 4 } m ^ { 2 } } { \left\{ - 2 \cos M + \cos ( 2 \omega - 2 U + 3 M ) + 9 \cos ( 2 \omega - 2 U + M ) \right\} } . } \end{array}
$$

Here the right-hand side achieves its greatest numerical value when $\hbar \pmb { \mathscr { f } } = \emptyset$ or $\exists 8 0 ^ { \circ }$ ,and $2 \{ \omega - U \} = 1 8 0 ^ { \circ }$ But again the amplitude is too great, although (12.5.6) at least shows that substantial periodic perturbations of e are to be expected.

These results are very inaccurate and have no intrinsic value; they illustrate the danger of using rough solutions. From an inspection of the results for $\omega$ and e,we should expect that the largest fuctuation of each would have a period equal to half the time between two successive passages of the Sun through perigee, even when perigee is not fixed. This assumption is correct; the period of these variations is approximately 206 days.

If we assume that the Moon moves in an eliptic orbit, the frst term in the equation of the center is

$$
\begin{array} { r } { v - \tilde { \mathcal { M } } = 2 e \sin \tilde { \mathcal { M } } } \\ { = ( 6 ^ { \circ } 1 7 ^ { \prime } ) \sin \tilde { M } . } \end{array}
$$

But if periodic perturbations in $\omega$ and $\pmb { \mathcal { E } }$ are allowed for, we must add (to this order) the term

$$
( 1 ^ { \circ } 1 \mathfrak { E } ^ { \prime } ) \sin ( 2 \omega - 2 \mathcal { V } \div M ) .
$$

(The argument of this term appears reasonable from a consideration of the terms of largest amplitudes in the solutions (12.5.4) and (12.5.6).） This term causes very considerable periodic departures from eliptic motion,which were first noticed by Hipparchus; it constitutes the evection. The period is 31.81 days.

# 12.6 The Variation

The equation for the variation of $\pmb { \mathcal { a } }$ is

$$
\frac { d a } { d \tilde { M } } = \frac { 2 a ^ { 3 } } { \mu } \left\{ \frac { e } { \sqrt { 1 - e ^ { 2 } } } F _ { r } \sin v \div \frac { a } { r } \sqrt { \mathrm { i } - e ^ { 2 } } F _ { \dot { b } } \right\} .
$$

We are to neglect $\mathcal { C }$ so the term in $\mathbf { \mathcal { F } _ { r } }$ vanishes,and we are left with

$$
\frac { d a } { d M } = - 3 m ^ { 2 } a \sin 2 ( u - U ) .
$$

Then

$$
a - a _ { 0 } = \frac { 3 } { 2 } m ^ { 2 } a \frac { 1 } { 1 - m } \cos 2 ( u - U ) .
$$

ence α executes small oscillations with period half a synodic month.

α has its maximum value at new and full moon, and it is tempting to reason that the orbit is slightly elongated toward and away from the Sun,as though tidally distorted; but this reasoning is worthless because we have assumed that the radius vector at any time has the value $\pmb { \mathcal { Z } }$ In fact the reverse is the case,as can be seen in the following qualitative way. Assume that,solar perturbations apart,the orbit of the Moon would be circular. It can be seen from (12.2.12) and(12.2.13) that $\mathcal { F } _ { \tau }$ hasmaxima at new and full moon and minima at the quarters; at each of these positions Fb = 0. This means that,as far as the Moonis concerned, there is less pull in the radial direction from the Earth at new and full moon than at the quarters; hence the curvature of its path will be least at new and full moon and greatest at the quarters, so that the orbit will be elongated, with its longer axis at right angles to the direction of the Sun.

We also see from the changing signs of $F _ { b }$ that the Moon will run late from new to the frst quarter,but will then make up speed to full; it will again run late to the last quarter but will speed up and arrive at new on time. The gain or loss in longitude, compared with unperturbed motion,has period half a synodic month and can be written

$$
\{ 3 9 ^ { \prime } \} \sin 2 \{ u - \bar { U } \} .
$$

This perturbation is known as the variation; it was discovered by Tycho Brahe (before the time of Newton).

# 12.7 The Perturbation of the Period and the Annual Equation

At any instant the Moon is apparently experiencing a radial attraction

$$
\frac { { \mathscr E } _ { { \sf R } } ^ { { \tilde { k } } ^ { 2 } } } { { \bf r ^ { 2 } } } - \mathscr F _ { \tau }
$$

toward the Earth. Supposing the Moon to move in a circular orbit, the average value of this radial force is,from (12.2.12),

or

$$
\frac { \Xi \bar { \kappa } ^ { 2 } } { a ^ { 2 } } - \frac { \mathbb { i } } { 2 } \bar { \kappa } ^ { 2 } a
$$

$$
\frac { E k ^ { 2 } } { a ^ { 2 } } \left( 1 - \frac { 1 } { 2 } \pi z ^ { 2 } \right) .
$$

So the Sun detracts, on the average, from the pull of the Earth on the Moon. (The average values of $z _ { b }$ and $E _ { \pi }$ are zero.） If this were forgotten, we might

arrive at too low a value for $( \Xi + \mathbb { M } ) \bar { \kappa } ^ { 2 }$ if we were to calculate it from the formula for the period,

$$
\bar { g } = 2 \pi { \frac { a ^ { 3 / 2 } } { \bar { k } ( \bar { E } + \hat { M } ) ^ { 1 / 2 } } } .
$$

In effect, the action of the Sun seems to have decreased $( E + M ) k ^ { 2 }$ by the factor $( \mathtt { I } - \mathtt { \Pi } _ { 2 } ^ { 1 } \mathtt { m } ^ { 2 } )$ ; alternatively it has the effect of increasing the period by the factor $\scriptstyle \{ { \frac { 1 } { 4 } } - { \frac { 1 } { 2 } } \pi ^ { 2 } \} ^ { - 1 / 2 }$ ，or $( \ I + \frac { 1 } { 4 } \pi z ^ { 2 } )$ , or 0.14 per cent. This amounts to nearly one hour;the correct figure is slightly over one hour.

Now let us continue to assume that the Moon moves in a circular orbit, but take into account that the Sun does not. Let ${ \mathfrak { g } } _ { 1 }$ be the semimajor axis of the Sun's orbit； then $N ^ { 2 }$ is no longer given by (12.2.15) but by

$$
N ^ { 2 } = { \frac { S k ^ { 2 } } { a _ { 1 } ^ { 3 } } } = { \frac { S k ^ { 2 } } { R ^ { 3 } } } \left( { \frac { R } { a _ { 1 } } } \right) ^ { 3 }
$$

and

$$
F _ { r } = \frac { 1 } { 2 } N ^ { 2 } \left( \frac { a _ { 1 } } { R } \right) ^ { 3 } \vec { \tau } \left[ \vec { \mathrm { 1 } } + 3 \cos 2 ( u - U ) \right] .
$$

The average value of the radial force, taken over one month (during which we assume $\scriptstyle { \mathcal { R } }$ to be constant), is

$$
\frac { { \mathscr { E } } k ^ { 2 } } { a ^ { 2 } } \left\{ 1 - \frac { 1 } { 2 } m ^ { 2 } \left\{ \frac { a _ { 1 } } { R } \right\} ^ { 3 } \right\} ;
$$

so we find the period of the Moon's orbit to be increased by the factor

$$
\frac { 1 } { 3 } + \frac { 1 } { 4 } m ^ { 2 } \left\{ \frac { a _ { 1 } } { 2 } \right\} ^ { 3 } .
$$

Now $\Re$ varies by some 3 per cent during the course of the year,so the length of the month varies, becoming less from perihelion to aphelion (January to June) and then greater. This means that the Moon is apparently running ahead of time for the first six months and behind for the last six months of the (anomalistic) year. The resulting difference in longitude is given by

$$
- \left\{ 1 \vdots ^ { \prime } 1 5 ^ { \prime \prime } \right\} \sin V .
$$

This is the annual equation.

# 12.8The Parallactic Inequality

If terms in $\{ \vec { r } / \mathcal { R } \} ^ { 2 }$ are included in (12.2.9) and the work following, then slight modifications will be called for in the results. The principal change is that a term is introduced into the longitude with period equal to a synodic month,and a coefficient that involves the ratio

$$
\begin{array} { r l } { \underline { { \underline { { E } } } } + \underline { { M } } \underline { { \underline { { a } } } } , } & { { } } \\ { \underline { { \underline { { s } } } } _ { 1 } , \underline { { \underline { { s } } } } _ { 2 } , \underline { { \underline { { s } } } } _ { 3 } , \underline { { \underline { { s } } } } _ { 3 } , \underline { { \underline { { s } } } } _ { 3 } , } & { { } } \\ { \underline { { \underline { { s } } } } _ { 1 } , \underline { { \underline { { s } } } } _ { 3 } , \underline { { \underline { { s } } } } _ { 3 } , \underline { { \underline { { s } } } } _ { 3 } , } & { { } } \end{array}
$$

this term is called the parallactic inequality. An accurate observational determination of its value would lead to a value for a1, the astronomical unit; the drawback to this is that the ratio M/E must be known first.

# 12.9 The Secular Acceleration of the Moon

The Moon's mean longitude is

$$
\begin{array} { r } { \vec { \mathfrak { z } } = \mathfrak { n } \vec { \mathfrak { z } } \ \pm \varepsilon . } \end{array}
$$

If we neglect all periodic perturbations,we can take n as constant,and it remains to investigate the changes in e. In an investigation of the Moon's mean motion,Halley used records of ancient eclipses and found $\pmb { \check { \ell } }$ to be represented empirically by

$$
l = l _ { 0 } + n _ { 0 } t + \sigma \left( \frac { t } { 1 0 0 } \right) ^ { 2 } + \mathrm { \ p e r i o d i c ~ t e r m s } .
$$

Here $\ddagger$ ismeasured in Julian years (365.25 days) from some epoch. $\sigma$ is called the coefficient of the secular acceleration; its value is approximately $1 \ I ^ { \prime \prime }$ ·

An explanation for this term was frst given by Laplace. The average pull of the Earth on the Moon depends on the average value of $\Xi _ { r }$ ，which depends in turn on the average value of $\hbar ^ { - 3 }$ .This can be shown to depend on the eccentricity of the Sun's orbit, which is known to be gradually changing.

To put this into some sort of quantitative form,we see that if (12.9.1） and (12.9.2) are differentiated,then $\pmb { \sigma }$ depends on the presence of a secular term in the expression for de/dt. Neglecting the squares of $\ Y _ { \pm }$ and $e$ for the orbit of the Moon, the equation for $d \in \int d t$ (assuming $\mathfrak { z }$ to be constant) is

$$
\cdot \ \frac { d \varepsilon } { d \xi } = - \frac { 2 \pi a \gamma } { \mu } \mathcal { F } _ { \tau } .
$$

Ignoring periodic terms in $\pmb { \xi } _ { \tau }$ and giving $\mathfrak { F }$ its mean value, we have

$$
\frac { d \varepsilon } { d \vec { t } } = - \gamma \gamma ^ { 2 } \eta \left( \frac { a _ { 1 } } { \vec { R } } \right) ^ { 3 } .
$$

The mean value of $\Re ^ { - 3 }$ is

$$
\begin{array} { c } { { \overline { { { R ^ { - 3 } } } } = \displaystyle \frac { \int _ { 0 } ^ { P _ { 1 } } R ^ { - 3 } d t } { \int _ { 0 } ^ { P _ { 1 } } d t } } } \\ { { = \displaystyle \frac { 1 } { P _ { 1 } } \int _ { 0 } ^ { 2 \pi } \frac { 1 } { \hbar _ { 1 } } \frac { 1 } { R } d v } } \end{array}
$$

$$
\begin{array} { l } { { \displaystyle = \frac { 1 } { P _ { 1 } h _ { \bar { 1 } } a _ { 1 } ( 1 - e _ { \bar { 1 } } ^ { 2 } ) } \int _ { 0 } ^ { 2 \pi } ( \bar { 1 } + e \cos v ) d v } } \\ { { \displaystyle = \frac { 1 } { a _ { 1 } ^ { 3 } ( 1 - e _ { \bar { 1 } } ^ { 2 } ) ^ { 3 / 2 } } . } } \end{array}
$$

Hence over long periods we have

$$
\frac { \dot { a } \varepsilon } { \dot { a } \dot { \varepsilon } } = - \frac { \hbar ^ { 2 } \pi } { ( \frac { 1 } { 2 } - e _ { 1 } ^ { 2 } ) ^ { 3 / 2 } } .
$$

This would be constant but for the fact that $e _ { 1 }$ is slowly changing due to planetary perturbations. The value of $e _ { 3 }$ is given,for the (astronomically) near future,by

$$
e _ { \bar { \bf 3 } } = e _ { \bar { \bf 3 } 0 } - \alpha \hat { \bf \ t } ,
$$

where $e _ { \tt i 0 } = 0 . 0 1 6 7 7 1$ and $\alpha = 4 . 2 4 5 \times 1 0 ^ { - 7 }$ , for the epoch 1850.0. Hence, expanding the right-hand side of (12.9.3) and ignoring $\alpha ^ { 2 }$ we have

$$
\frac { \dot { d } \varepsilon } { \dot { d } \dot { t } } = \mathrm { c o n s t a n } \dot { \mathrm { a } } \dot { \mathrm { a } } \dot { \mathrm { a } } \dot { \mathrm { a } } \dot { \mathrm { \Omega } } + 3 m \mathrm { a } ^ { 2 } n e _ { \frac { 1 } { 2 } 0 } \alpha \dot { \mathrm { z } } .
$$

Integrating, we see that $\boldsymbol { \sigma }$ of (12.9.2) is given by

$$
\begin{array} { r } { \sigma = \frac { 3 } { 2 } \mathbb { i } \mathbb { j } ^ { \frac { 4 } { 2 } } \mathfrak { m } ^ { 2 } \mathfrak { n } e _ { 1 0 } \alpha . } \end{array}
$$

The numerical evaluation of this is left to the reader;the result is that $\sigma$ is approximately equal to 10".4, and this appears to account satisfactorily for the observations.

The formula (12.9.4） is misleading; $\epsilon _ { \lambda }$ actually fluctuates periodically,the principal period being 24,000 years; the term at in (12.9.4) is merely the first term in the expansion of some trigonometric function. Hence the secular acceleration will fuctuate with $\mathcal { C } _ { \mathfrak { T } }$

We have seen how first-order results by themselves can be misleading. The apparent agreement between theory and observation found above was shown to be illusory by Adams. If higher order terms are taken into account, $\sigma$ can be expanded asa power series in m (of which the right-hand side of (12.9.5) is the first term) which converges slowly； furthermore, the terms following the first arenegative.Adams arrived at the value $5 ^ { \prime \prime } . 7 2$ for $\pmb { \sigma }$ ,and this does not fully account for the observations.

A formula of the type (12.9.2) assumes that $\ddagger$ is the “evenly flowing” time always taken for granted in mechanics. But the eclipse observations used to determine $\sigma$ use the rotatingEarth asa clock,and the discrepancy between the values of g can be explained if we assume that the rate of rotation of the Earth about its axis is gradually diminishing. This slowing down is now generally accepted.The usual explanation is that it is due to tidal friction in shallow seas between the sea beds and the water. Quantitative agreement has been found for this theory,but discussion on the subject is by no means closed


<!-- chunk 0006: pages 201-240 -->
It is of interest to consider the evolution of the Moon's motion in the light of the tidal theory for the slowing down of the Earth's rotation. At present the angular momentum lost to the Earth by tidal friction must be transferred to the orbital angular momentum of the Moon; the latter is therefore receding from the Earth,and the month is becoming longer.This will continue (in theory,at any rate) until the month and the day are of equal length, when the friction involved in the lunar tides must cease. But the solar tides will continue to cause friction, now robbing the Earth-Moon system of angular momentum, and causing the Moon to approach the Earth again. In the past,we go back to a time when the Moon was close to the Earth,and the day and month were short and nearly equal. It was the latter circumstance that was considered by Darwin to be the result of the Moon just having broken away from the Earth (a view that is not without its challengers today).

# 12.10 Theories of the Motion of the Moon

The history of theories of the motion of the Moon starts with the publication of the Principia by Newton in 1687,includes contributions from mathematicians such as Euler,Laplace,and Poisson,and culminates in the Hill-Brown lunar theory that has led to the very accurate expressions for the lunar motion used today in the almanacs.

Newton showed that the observed inequalities in the motion of the Moon were due to perturbations by the Sun,and he predicted some inequalities that had not been observed up to that time. He had diffculty over the motion of perigee,but eventually explained this to within 8 per cent of the observed motion by taking second-order terms into account. (Newton is reputed to have told Halley that the lunar theory “made his head ache and kept him awake so often that he would think of it no more.") His arguments were cast in abstruse geometrical form, but were almost certainly first worked out analytically, using the theory of fuxions.

Clairaut applied analytical methods to the problem and in 1749 succeeded in explaining the motion of perigee by using second-order approximations. In 1752 he published his Theorie de la Lune and in 1754 he published a set of numerical tables for the computation of the position of the Moon.

Euler published some tables in 1746.In 1753 he published a lunar theory that included a partial exposition of the method of variation of elements. His most significant contribution came in 1772 when he published his second lunar theory. In this his equations of motion were referred to axes rotating with the mean motion of the Moon.

Laplace's theory was evolved toward the end of the eighteenth century and published in 1802. He transformed the equations of motion so that the true longitude was the independent variable. His reference orbit was a Keplerian ellipse modified to avoid terms proportional to the time in the coefficients. He gave the explanation for the secular acceleration of the Moon noted above. Laplace's methods were carried to a higher degree of accuracy by several mathematicians, including Damoiseau,whose theory was published in 1827,and who published tables that were used until they were superseded by those of Hansen.

Another important theory stemming directly from the equations of motion, and carried through to a high degree of accuracy,was that published by de Pontecoulant in 1846.

Returning to chronological order,we come to one of the most important lunar theories,that of Hansen.His reference system is mentioned in Section 11.8.Hansen's work extended over forty years from 1829.His tables were published in 1857 and were used generally for over fifty years.

In 1860 Delaunay published the results of a lunar theory involving the removal, by analytical means, of the terms of the disturbing function, one by one, and the gradual building up of the solution. His expression for the disturbing function included 320 terms (including all terms of the seventh order of small quantities and some of the eighth).The analytical work took twenty years. The solution is not numerical but analytical, and can be applied not only to the motion of the Moon but also to any satellite motion (of the three-body type). It is the most perfect solution yet found for this type of motion. This theory was later made the basis of lunar tables. Delaunay's work has since been continued to a much higher order by the use of symbolic algebraic manipulation on the computer.

In 1878 Hill published the first paper introducing a new method using rectangular coordinates based on axes rotating with the mean motion of the Sun. Hill first found a closed solution,symmetrical about the axes; this is an oval, with the longer axis perpendicular to the direction of the Sun (see Section 12.6.), and is known as Hill's variational curve. This curve was used as a reference orbit in describing the actual motion of the Moon. The work was further developed by Brown,who published tables in 1919 which have been used since 1923 in the preparation of lunar ephemerides.In the future his series solutions will probably be used for this purpose.

# 12.11 Problems

1.Show that the locus of the point at which the attractions of the Sun and Earth are equal is a sphere whose radius is

$$
R \frac { ( S E ) ^ { 1 / 2 } } { S - E }
$$

and whose center is on the line joining the Sun and Earth,at the distance $\Xi { \mathcal { B } } / ( S - { \Xi } )$ from the center of the Earth,opposite to the Sun;where $S$ and $\pmb { \mathcal { E } }$ represent the masses of the Sun and Earth,respectively,and $\Re$ is the distance from the Sun to the Earth.Calculate these values and show that the Moon is always attracted more by the Sun than by the Earth. Why,then,does the Moon continue to move in orbit around the Earth？

2.Consider the problem of the motion of the Moon in terms of motion around the Sun disturbed by the Earth.

3.Show that the ratio of the greatest disturbing effect of the Sun to the least disturbing effect of the Earth is approximately 0.0114.

4. Show that the ratios of the maximum value of the Sun's disturbing force to the attractions of the Sun and Earth are 0.0o5 and O.011, respectively.

5.Because it is the center of mass of the Earth-Moon system, which describes a Keplerian orbit about the Sun (neglecting planetary perturbations), the Sun,as observed from the Earth,will not apparently move in a Keplerian orbit,but will have displacements △β and △X in latitude and longitude with respect to that Keplerian motion. Show that the former of these has period equal to the nodical month,and the latter has period equal to the synodic month,and that their observation can yield information about the ratio of the masses of the Earth and Moon. Taking this ratio as 81.27, find the amplitudes of △β and △x.

6.Find the secular perturbations caused by the Earth's oblateness on the motion of the Moon,and compare these with the perturbations produced by the Sun.

7.Investigate very approximately the perturbations produced by Jupiter on the motion of the Moon.

8.An artificial satellite revolving around the Earth,outside the atmosphere, isacted upon by the Earth's oblateness, the Sun,and the Moon,apart from the Newtonian attraction of the Earth,considered as a sphere. Assuming that it moves in a nearly circular orbit, compare the perturbations produced by the three effects for various major axes of the satellite's orbit. Find the ratio of the perturbations produced by the Sun and the Moon. Find the order of magnitude of the period of the satellite for which the perturbations produced by the Sun and Moon roughly equal in magnitude those produced by the Earth'soblateness.

9.Investigate the first-order motion of the Moon's nodes, taking into account the eccentricities of the orbits of the Sun and Moon.

10.(a） Derivea formula for the length of the nodical month in terms of the sidereal month and the rate of recesson of the nodes. Check this with the numerical values. (b)Derive a formula for the length of the eclipse year in terms of the sidereal year and the motion of the nodes of the Moon'sorbit. Check this with the numerical values. (c) Taking into account the precession of the equinoxes, find the time that will elapse between two successive passages of the ascending node through the vernal equinox. (d) Why is it the Saros, and not the period of nodal revolution, that can beused in predicting eclipses?

(e) Derive a formula for the period of the evection in terms of the sidereal and anomalistic months. Check this with the numerical values.

11. Investigate the perturbation in the period by considering the secular perturbation of M.

12. Find the average value of $\mathbf { \varPsi } _ { r }$ over an elliptic orbit. What modifications, if any,must be made to the work of Section 12.7if the eccentricity of the Moon's orbit is taken into account?

13.The observed motion of the Moon might be used to relate the quantities $\Xi + \lambda$ with $\pmb { \mathcal { Q } }$ ,and one of these might be found from the other. If the perturbations due to the Sun are ignored (and therefore the resulting perturbation of the period), find the errors that might be introduced.

14. How will the secular acceleration of the Moon affect the time of an eclipse 4000 years ago as predicted by contemporary clocks, compared with the timerecorded at the event?

15. Use first-order theory to find the annual equation. Compare your result with the formula (12.7.2).

16.Assuming that the discrepancy between the observed value of $\sigma$ and Adamsvalue of $\sigma$ is the result of a slowing down of the Earth's rate ofrotation,and that the angular momentum lost to the Earth is added to the orbital angular momentum of the Moon, calculate the increases in a century of the Moon's mean distance from the Earth and the length of the sidereal month.Comment on the observability of these.

17.Assuming that the total angular momentum of the Earth-Moon system is conserved, investigate possible configurations in the past and future such that the lengths of the month and day are equal. If some angular momentum were lost through the tidal action of the Sun,what effect would this have on your results?

18.Assume that the orbit of the Sun is a circle, and neglect $( \gamma / R ) ^ { 2 }$ in the expression for the disturbing force. Define a system of rotating axes such that $O z$ always points toward the Sun,and $\partial z$ is perpendicular to the ecliptic. Show that the equations of motion of the Moon with respect to these axes can be written

$$
\begin{array} { r l r } & { } & { \ddot { z } - 2 n _ { \mathrm { 1 } } \dot { y } - 3 n _ { \mathrm { 1 } } ^ { 2 } x = - \mu \frac { x } { r ^ { 3 } } , ~ } \\ & { } & \\ & { } & { \ddot { y } + 2 n _ { \mathrm { 1 } } \dot { x } ~ = - \mu \frac { y } { r ^ { 3 } } , ~ } \\ & { } & \\ & { \ddot { z } ~ } & { + ~ n _ { \mathrm { 1 } } ^ { 2 } z ~ = - \mu \frac { z } { r ^ { 3 } } , ~ } \end{array}
$$

where $\mathfrak { R } _ { 3 }$ is the angular motion of the Sun.

19. Write down the equations of motion of the Moon with respect to axes rotating with the mean motion of the Moon.
