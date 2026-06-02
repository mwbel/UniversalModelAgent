If $| x | \leq a , | x | \leq b / M ,$ then

$$
\left| S _ { 1 } ^ { ( i ) } ( x ) \right| \le \frac { b } { M } \overline { { { f } } } _ { i } ( a ; b , b , \ldots ) \le b .
$$

When $S _ { \mathbf { 1 } } ^ { ( i ) }$ are known, then $S _ { 2 } ^ { ( i ) }$ can be obtained from the formula (18) for $S _ { n + 1 } ^ { ( i ) }$ . Generally we have

$$
\left| S _ { n } ^ { ( i ) } ( { \pmb x } ) \right| \le b .
$$

Hence, as Wintner has shown, we can consider $d y _ { i } / d x = \overline { { f _ { i } } } ,$ in place of the equations (17).This is the way Weierstrass (l9l2) formulated the equations for the $\pmb { n }$ -body problem, in order to study the singularities.

Petrovskaya (1959,1963) applied this principle of Wintner for obtaining the radius of convergence of the series in powers of $\mathbf { m }$ for Hill's intermediary orbit. The upper bound she obtained is $\mathbf { m } < 0 . 2 1$ ,which is sharper than Wintner's $\mathbf { m } < 1 / 1 2$

With the variables $\xi = ( n - n ^ { \prime } ) ( t - t _ { 0 } ) , \zeta = \exp { \{ \sqrt { - 1 } \xi \} }$ the equations of motion for Hil's intermediary orbit are written (Sections 11.1 and 11.2)

$$
\frac { d ^ { 2 } u } { d \xi ^ { 2 } } = \sum _ { i = - \infty } ^ { \infty } ( 2 i + 1 ) ^ { 2 } a _ { 2 i } \zeta ^ { 2 i + 1 } , \frac { d ^ { 2 } s } { d \xi ^ { 2 } } = \sum _ { i = - \infty } ^ { \infty } ( 2 i + 1 ) ^ { 2 } a _ { - 2 i - 2 } \zeta ^ { 2 i + }
$$

or, if we put

$$
a _ { 2 j } = { \bf m } a _ { 0 } \frac { b _ { j } } { j ^ { 4 } } \qquad ( j = \pm 1 , \pm 2 , . . . ) ,
$$

then the equations take the form

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } u } { d \xi ^ { 2 } } = \sum _ { i = - \infty } ^ { \infty } \frac { { \bf m } a _ { 0 } ( 2 i + 1 ) ^ { 2 } b _ { i } } { i ^ { 4 } } \zeta ^ { 2 i + 1 } } , } } \\ { { \displaystyle { \frac { d ^ { 2 } s } { d \xi ^ { 2 } } = \sum _ { i = - \infty } ^ { \infty } \frac { { \bf m } a _ { 0 } ( 2 i + 1 ) ^ { 2 } b _ { - i - 1 } } { ( i + 1 ) ^ { 4 } } \zeta ^ { 2 i + 1 } } . } } \end{array}
$$

The solution is assumed to be of the form

$$
u = \sum _ { i = - \infty } ^ { \infty } \frac { { \bf m } a _ { 0 } b _ { i } } { i ^ { 4 } } \zeta ^ { 2 i + 1 } , \qquad s = \sum _ { i = - \infty } ^ { \infty } \frac { { \bf m } a _ { 0 } b _ { - i - 1 } } { ( i + 1 ) ^ { 4 } } \zeta ^ { 2 i + 1 } .
$$

If we substitute this solution in the differential equations,we can determine the coefficients $b _ { j }$ by an infinite number of simultaneous equations :

$$
\begin{array} { r l } { b _ { - 1 } = \mathbf { m } \phi _ { - 1 } ( \mathbf { m } ; b _ { - 1 } , b _ { 1 } , b _ { - 2 } , b _ { 2 } , \ldots ) , } & { } \\ { b _ { 1 } = \mathbf { m } \phi _ { 1 } ( \mathbf { m } ; b _ { - 1 } , b _ { 1 } , b _ { - 2 } , b _ { 2 } , \ldots ) , } & { } \\ { b _ { j } = \mathbf { m } \phi _ { j } ( \mathbf { m } ; b _ { - 1 } , b _ { 1 } , b _ { - 2 } , b _ { 2 } , \ldots ) \quad } & { ( j = \pm 2 , \pm 3 , \ldots ) , } \end{array}
$$

where $\phi$ are of the form:

$$
\begin{array} { r l } & { - \mathcal { J } _ { 1 } ^ { - 3 } \langle \mathbf { n } \rangle \Bigg ( \frac { 3 } { 1 6 } + \frac { 3 } { 8 } \mathbf { n } ^ { 2 } \delta _ { - 1 } \delta _ { 1 } + \frac { 3 } { 1 6 } \mathbf { n } ^ { 2 } \delta _ { - 2 } ^ { 2 } \frac { \delta _ { - 1 } \delta _ { - 2 } } { 4 \delta _ { - 1 } } \Bigg ) } \\ & { \qquad - \mathcal { J } _ { 2 } ^ { - - 2 } \langle \mathbf { n } \rangle \Bigg ( \frac { 3 } { 1 2 8 } \mathbf { n } ^ { 2 } \kappa _ { - 2 } + \frac { 3 } { 1 6 } \mathbf { n } ^ { 2 } \kappa _ { - 2 } ^ { 2 } + \frac { 1 } { 2 1 6 } \mathbf { n } ^ { 2 } \kappa _ { - 1 } ^ { 3 } \delta _ { - 3 } } \\ & { \qquad \quad \qquad \quad + \frac { 3 } { 1 6 } \mathbf { n } ^ { 2 } \kappa _ { - 1 } \sum _ { \frac { \delta = - \delta } { 1 } } ^ { \infty } \frac { \tilde { \nu } _ { - \delta } ^ { \delta } _ { - 1 } \delta _ { - 2 } } { 4 ( ( \frac { 1 - 2 \pi ) ^ { 2 } } { 2 } ) ^ { 3 } } \Bigg ) } \\ & { \qquad \quad - \frac { 1 } { 8 } \mathcal { n } ^ { 2 } \kappa _ { - 3 } ^ { - 3 } \langle \mathbf { n } \rangle \Bigg ( \kappa _ { - 1 } ^ { 3 } \delta _ { 1 } \delta _ { - 2 } } \\ & { \qquad \quad - \frac { 1 } { 8 } \mathcal { f } _ { 1 } ^ { - 3 } ( \mathbf { n } ) \delta _ { - 1 } \delta _ { 2 } + \frac { 1 } { 1 6 } \mathbf { n } ^ { 2 } \kappa _ { - 1 } ^ { 3 } \langle \mathbf { n } \rangle \delta _ { 1 } \delta _ { 2 } } \\ & { \qquad \quad + \quad \sum _ { \frac { \delta = - \delta } { 1 6 } } ^ { \infty } \mathcal { f } _ { 1 } ^ { - 3 } ( \mathbf { n } ) \frac { \delta _ { - 1 } \delta _ { 1 } \delta _ { - 2 } } { 2 ( \frac { 1 - 2 \pi } { 2 } + 1 ) ^ { 3 } } \cdot } \\ &  \qquad \quad \quad \mathrm { e t e r } \sum _ { \frac { \delta = - \delta } { 1 6 } } ^ { \infty } \mathcal { J } _ { 1 } ^ { - 1 } ( \mathbf { n } ^ { 2 } \kappa _ { - 1 } ^ \end{array}
$$

$$
\begin{array} { l } { { \displaystyle { \phi _ { j } = - \sum _ { i = 1 } ^ { 6 } f _ { i } ^ { ( j ) } ( { \bf m } ) \chi _ { i } ( { \bf m } ; b _ { - 1 } , b _ { 1 } , \dots ) } } \ ~ } \\ { { \displaystyle ~ - j ^ { 3 } \cdot \sum _ { \substack { i \ne 0 , \pm 1 , j , j \pm 1 } } ^ { \infty } f _ { i } ^ { ( j ) } ( { \bf m } ) \frac { b _ { i } b _ { - 1 } } { i ^ { 2 } ( i - 1 ) \cdot i + 1 } } \ ~ } \\ { { \displaystyle ~ ( j = \ \pm 2 , \pm 3 , . } } \end{array}
$$

and

$$
\mathrm {  ~ \Gamma ~ } _ { 1 } ^ { ( - 1 ) } ( { \bf m } ) = \frac { 3 8 + 2 8 { \bf m } + 9 { \bf m } ^ { 2 } } { 6 - 4 { \bf m } + { \bf m } ^ { 2 } } , \qquad f _ { 2 } ^ { ( - 1 ) } ( { \bf m } ) = \frac { 1 0 - 4 { \bf m } - 9 { \bf m } ^ { 2 } } { 6 - 4 { \bf m } + { \bf m } ^ { 2 } } ,
$$

$$
f _ { 1 } ^ { ( j ) } ( { \bf { m } } ) = \frac { { 2 0 j ^ { 2 } - 1 6 j + 2 - 4 ( 5 j - 2 ) { \bf { m } } + 9 { \bf { m } } ^ { 2 } } } { { 2 ( 4 j ^ { 2 } - 1 ) - 4 { \bf { m } } + { \bf { m } } ^ { 2 } } }
$$

$$
f _ { i } ^ { ( j ) } ( { \bf { m } } ) = \frac { { 4 ( j - 1 ) + \frac { { 4 j ^ { 2 } + 4 j - 2 } } { i } - 4 \bigg ( 1 - \frac { { j - i } } { i } \bigg ) { \bf { m } } + \frac { 1 } { i } { \bf { m } } ^ { 2 } } } { { 2 ( 4 j ^ { 2 } - 1 ) - 4 { \bf { m } } + { \bf { m } } ^ { 2 } } }
$$

$$
( i \ne 0 , \pm 1 , j , j \pm 1 ; j = \pm 1 , \pm 2 , . . . ) .
$$

Petrovskaya proved that these functions are holomorphic for

$$
| { \bf m } | < \sqrt { 2 ( 4 j - 1 ) } , \qquad | b _ { j } | < \infty \qquad ( j = \pm 1 , \pm 2 , \ldots ) .
$$

The functions $f _ { 1 } ^ { ( - 1 ) } ( { \bf { m } } ) , f _ { 2 } ^ { ( - 1 ) } ( { \bf { m } } ) , f _ { i } ^ { ( j ) } ( { \bf { m } } ) , ( i , j = \pm 1 , \pm 2 , . . . ) _ { ! }$ are of the form

$$
f ( x ) = { \frac { A + B x + C x ^ { 2 } } { a - b x + c x ^ { 2 } } } \qquad ( A , a , b , c > 0 ) .
$$

We expand in the form

$$
f ( { \boldsymbol { x } } ) = \sum _ { k = 0 } ^ { \infty } a _ { k } x ^ { k }
$$

and compute the coefficients $a _ { k }$ .Thus we obtain for $f _ { \mathbf { 1 } } ^ { ( - \mathbf { 1 } ) } ( \mathbf { m } )$ ，for example,

$$
\begin{array} { r l r l r l r l } { a _ { 0 } = { \frac { 1 9 } { 3 } } , } & { } & { a _ { 1 } = { \frac { 8 0 } { 9 } } , } & { } & { a _ { 2 } = { \frac { 1 7 2 } { 2 7 } } , } & { } & { a _ { 3 } = { \frac { 2 2 4 } { 8 1 } } , } & { } & { a _ { 4 } = { \frac { 1 9 0 } { 2 4 3 } } , } \\ & { } & { a _ { 5 } = { \frac { 4 4 } { 7 2 9 } } , } & { } & { a _ { 6 } = - { \frac { 1 9 7 } { 2 1 8 7 } } . } & { } & & { } \end{array}
$$

Inserting these expressions in the equations for $b _ { - 1 } , b _ { 1 } , b _ { j } ,$ we find

$$
\begin{array} { r l } & { \phi _ { - 1 } = A + B b _ { - 1 } ^ { 2 } + C b _ { - 1 } b _ { 1 } + D b _ { - 1 } b _ { j } + \cdot \cdot \cdot , } \\ & { \phi _ { 1 } = A _ { 1 } + B _ { 1 } b _ { - 1 } ^ { 2 } + C _ { 1 } b _ { - 1 } b _ { 1 } + D _ { 1 } b _ { - 1 } b _ { j } + \cdot \cdot \cdot , } \\ & { \phi _ { j } = C _ { 2 } b _ { - 1 } b _ { 1 } + D _ { 2 } b _ { - 1 } b _ { j } + \cdot \cdot \cdot , } \end{array}
$$

where

$$
\begin{array} { r l } & { 4 = ( \frac { S _ { 7 } ^ { 2 } } { 8 } + \frac { 2 _ { 1 } } { 4 } \mathbf { m } + \frac { 2 _ { 7 } } { 1 6 } \mathbf { m } ^ { 2 } + \frac { 1 9 } { 8 } \mathbf { q } _ { 4 } \mathbf { m } ^ { 6 } + \dots \cdot \cdot \cdot ) ( 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } ) ^ { - 1 } } \\ & { \qquad + ( \frac { 3 \cdot 3 \cdot 4 \mathbf { m } ^ { 6 } } { 4 } \mathbf { m } ^ { 6 } + \dots \cdot ) ( 6 - 4 \mathbf { m } - \mathbf { m } ^ { 2 } ) } \\ & { B = ( \frac { 1 5 } { 4 } \mathbf { m } ^ { 2 } - \frac { 3 } { 4 } \mathbf { m } ^ { 3 } + \frac { 4 6 \cdot 9 \mathbf { m } ^ { 4 } } { 8 } ) ( 6 - 4 \mathbf { m } - \mathbf { m } ^ { 2 } ) ^ { - 1 } , } \\ & { C = ( \frac { S _ { 7 } ^ { 2 } } { 4 } \mathbf { m } ^ { 2 } + \frac { 2 _ { 1 } } { 2 } \mathbf { m } ^ { 3 } + \frac { 2 _ { 7 } } { 8 } \mathbf { m } ^ { 4 } + \dots \cdot ) ( 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } ) ^ { - 1 } } \\ & { \qquad + ( \frac { 3 \cdot 7 } { 8 } ) ^ { \frac { 3 } { 2 } } \mathbf { m } ^ { 8 } + \dots \cdot ) ( 6 - 4 \mathbf { m } - \mathbf { m } ^ { 2 } ) } \\ & { \qquad \cdot \dots , } \\ & { 1 _ { 1 } = ( \frac { 9 } { 8 } + \frac { 9 } { 4 } \mathbf { m } + \frac { 2 _ { 7 } } { 1 6 } \mathbf { m } ^ { 2 } + \frac { 1 } { 6 4 8 } \mathbf { m } ^ { 5 } + \dots \cdot ) ( 6 - 4 \mathbf { m } + \mathbf { m } ^ { 2 } ) ^ { - 1 } } \\ & { \qquad + ( \frac { 1 6 } { 4 4 } \mathbf { m } ^ { 6 } + \dots ) ( 6 - 4 \mathbf { m } - \mathbf { m } ^ { 2 } ) } \\ & { \qquad \cdot \dots = \frac { 3 } { 4 4 } \mathbf { m } ^ { 2 } + \dots } \\ & { \qquad \frac { 3 } { 2 } } \\ & { \underset { \mathrm { \scriptsize { \ell = 0 } } } { \overset { \mathrm { \scriptsize ~ . } } { \mathrm { \scriptsize ~ . } } } } \end{array}
$$

Petrovskaya proved that the series for $b _ { - 1 } , b _ { 1 } , b _ { - 2 } , b _ { 2 } , . . .$ are absolutely convergent for $| { \bf m } | < \sqrt { 2 ( 4 j ^ { 2 } - 1 ) }$ $| b _ { j } | < \infty$ ， $j = \pm 1 , \pm 2 , \ldots$ and thus that the minimum radius of convergence is $| { \bf m } | \le 0 . 2 1$

Petrovskaya (l963) further examined the errors when the series are truncated at the nth term $( n = 2 , 3 , 4 , 5 , 6 )$ ·

Hopf (l929) proved the existence of closed periodic orbits in the lunar theory on the basis of Poincaré's theory of periodic solutions,as will be discussed in Section 18.13. The expansion is valid in the form

$$
\begin{array} { l } { { \displaystyle \xi ( t ; { \bf m } ) = { \bf m } ^ { 2 / 3 } \Biggl [ \cos \tau + \sum _ { \nu = 1 } ^ { \infty } { \bf m } ^ { \nu / 3 } \phi _ { \nu } ( \tau ) \Biggl ] M _ { E } ^ { 1 / 3 } , \qquad \gamma = { \bf m } \tau , } } \\ { { \displaystyle \eta ( t ; { \bf m } ) = { \bf m } ^ { 2 / 3 } \Biggl [ \sin \tau + \sum _ { \nu = 1 } ^ { \infty } { \bf m } ^ { \nu / 3 } \psi _ { \nu } ( \tau ) \Biggl ] M _ { E } ^ { 1 / 3 } , } } \end{array}
$$

where $M _ { E }$ denotes the earth's mass, and $\phi _ { \nu } ( \tau ) , \psi _ { \nu } ( \tau )$ are periodic with period $2 \pi$ with respect to $\boldsymbol { \tau }$ .The series are convergent for small values of $| \mathbf { m } _ { \mathrm { i } } ^ { \mathrm { l } }$ and are uniformly and absolutely convergent for all values of $\tau$

The orbits are Keplerian in the immediate neighborhood of $M _ { E }$ and $^ { a }$ is of the order $\mathbf { m } ^ { 2 / 3 }$ .Hopf transformed from $x , y$ to $\xi , \eta$ by

$$
\xi = \mu X , \qquad \eta = \mu ^ { 2 } Y , \qquad t = \mu ^ { 3 } \tau , \qquad \mu ^ { 3 } = { \bf m } .
$$

The differential equations reduce to the Keplerian for $\mu = 0$ .The period is $2 \pi$ in $\pmb { \tau } .$ .The question is whether there exists a disturbed orbit with the same period $2 \pi$

Wintner (1930) (see Section 20.14) showed that Strömgren's classification（1925,1934,1938） of periodic orbits explains the orbits computed by von Haerdtl (l894) (Section l0.4l);that is, von Haerdtl's orbit can be changed into a periodic orbit by a slight change of the integration constants,and the orbit is an analytical continuation of Darwin's orbits for Satellites $B$ and $C ,$ by the change of the mass ratio from l0 to 1 (Section 17.4).

# THE MOTION OF PERIGEE AND NODE

# II.5EQUATIONS FOR VARIATIONS

We have computed a particular solution corresponding to $e = 0$ as the intermediary orbit of Hil's lunar theory. If we put further $\mathbf { m } = 0$ ， then we obtain ${ \bf x } = { \bf a } \cos \xi _ { \mathrm { { \scriptscriptstyle M } } }$ ${ \textbf { Y } } = { \textbf { a } }$ sin $\xi _ { : }$ ，which is a Keplerian circular orbit.Hill's variational curve is the orbit distorted from a Keplerian circular orbit by the presence of $\mathbf { m }$ .The orbit of the moon has an eccentricity of about $\scriptstyle { \frac { 1 } { 2 0 } } =$ 、We now consider the deviation from Hill's variational curve due to the supposition of $\epsilon \neq 0$ .Hill's intermediary orbit contains two arbitrary constants,a and $C$ or $\mathbf { m }$ . The general solution of the equations (8) should contain four arbitrary constants in which $e ^ { \prime }$ ， $1 / a ^ { \prime }$ ， $_ z$ are as yet neglected, that is, in which $\Omega = 0$

Consider a system of equations

$$
\frac { d x _ { i } } { d t } = \Phi _ { i } ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) \qquad ( i = 1 , 2 , . . . , n ) ,
$$

for which a particular solution $x _ { i } = X _ { i } ( t ) ( i = 1 , 2 , . . . , n )$ is known. Let the solution for a varied initial condition be $x _ { i } = X _ { i } ( t ) + \xi _ { i } ( t )$ $( i = 1 , 2 , . . . , n )$ . The unknown functions for the deviation from the generating particular solution $x _ { i } = X _ { i } ( t )$ satisfy

$$
\frac { d \xi _ { i } } { d t } = \sum _ { j } \frac { \partial f _ { i } } { \partial x _ { j } } \bigg | _ { x _ { j } = x _ { j } ( t ) } \cdot \xi _ { j } ( t ) ,
$$

where the generating particular solution is substituted in $\partial f _ { i } / \partial x _ { j }$ on the right-hand side, if we neglect higher-degree terms in $\xi _ { 1 } , \xi _ { 2 } , . . . , \xi _ { n } ,$ which are supposed to be always small. This last system of equations was called the equations for variations or the variational equations (equations aux variations) by Poincaré (1889,1892).

Our differential equations for the motion of the moon are

$$
\begin{array} { l } { { \displaystyle { \frac { d ^ { 2 } X } { d t ^ { 2 } } } - 2 n ^ { \prime } \frac { d Y } { d t } } = \frac { \partial F } { \partial X } , } \\ { ~ } \\ { { \displaystyle { \frac { d ^ { 2 } Y } { d t ^ { 2 } } } + 2 n ^ { \prime } \frac { d X } { d t } } = \frac { \partial F } { \partial Y } , } \end{array}
$$

$$
V ^ { 2 } = \left( { \frac { d X } { d t } } \right) ^ { 2 } + \left( { \frac { d Y } { d t } } \right) ^ { 2 } = 2 F + \mathrm { c o n s t a n t } = { \frac { 2 \mu } { r } } + 3 n ^ { \prime 2 } X ^ { 2 } + \mathrm { c o n s t a n t }
$$

The variational equations were derived from (20) by Darwin (1916) in the following manner.From (l） we obtain

$$
{ \dot { X } } { \ddot { Y } } - { \ddot { X } } { \dot { Y } } + 2 n ^ { \prime } ( { \dot { X } } ^ { 2 } + { \dot { Y } } ^ { 2 } ) = { \dot { X } } { \frac { \partial F } { \partial Y } } - { \dot { Y } } { \frac { \partial F } { \partial X } } .
$$

Denote by $\psi$ the angle between the tangent $_ { \pmb { T } }$ to the orbital curve and the $X$ axis in the $X Y .$ -plane. Then,

$$
\begin{array} { r } { \dot { X } = V \cos \psi , \qquad \dot { Y } = V \sin \psi , \qquad V ^ { 2 } = \dot { X } ^ { 2 } + \dot { Y } ^ { 2 } , } \\ { \frac { d \psi } { d T } = \frac { ( \dot { X } \ddot { Y } - \ddot { X } \dot { Y } ) } { V ^ { 2 } } , \qquad } \end{array}
$$

or, since the derivative in the direction of the normal is

$$
\frac { \partial } { \partial N } = - \cos \psi \frac { \partial } { \partial Y } + \sin \psi \frac { \partial } { \partial X } = \frac { 1 } { V } \bigg \{ - \dot { X } \frac { \partial } { \partial Y } + \dot { Y } \frac { \partial } { \partial X } \bigg \} ,
$$

we have

$$
V \left( { \frac { d \psi } { d t } } + 2 n ^ { \prime } \right) \mathrm { ~ = ~ } - { \frac { \partial F } { \partial N } } \cdot
$$

From the third equation of (20) we obtain

$$
V \frac { \partial V } { \partial T } = \frac { \partial F } { \partial T } = \frac { d V } { d t } , \qquad V \frac { \partial V } { \partial N } = \frac { \partial F } { \partial N } \cdot
$$

Denote the arc length to a point $P$ on the curve by ${ \pmb \sigma } _ { : }$ ,and the deviation of a varied point $P ^ { \prime }$ from $P$ along the arc length by $\delta \sigma$ and in the normal direction $N$ by $\delta \mathbfit { p }$ .The TN-plane is in rotation around the $z \cdot$ -axis with angular velocity $d \psi / d t$ ，referred to the $X Y .$ -plane.The components of the velocity referred to the TN-axes are

$$
V + \frac { d \ : \delta \sigma } { d t } + \frac { d \psi } { d t } \ : \delta \phi , ~ 0 + \frac { d \ : \delta \phi } { d t } - \frac { d \psi } { d t } \ : \delta \sigma , ~ 0 .
$$

Hence,

$$
( V + \delta V ) ^ { 2 } = \left( V + \frac { d \ : \delta \sigma } { d t } + \frac { d \psi } { d t } \ : \delta \phi \right) ^ { 2 } + \ : \left( \frac { d \ : \delta \phi } { d t } - \frac { d \psi } { d t } \ : \delta \sigma \right) ^ { 2 } .
$$

To the frst order we have

$$
\frac { d \hat { \delta } \sigma } { d t } + \frac { d \psi } { d t } \hat { \delta } \boldsymbol { p } = \hat { \delta } V ,
$$

or, from (22),

$$
= \frac { 1 } { V } \frac { \partial F } { \partial T } \delta \sigma + \frac { 1 } { V } \frac { \partial F } { \partial N } \delta \pounds ,
$$

or, from (21),

$$
= { \frac { 1 } { V } } { \frac { d V } { d t } } \delta \sigma - \left( { \frac { d \psi } { d t } } + 2 n ^ { \prime } \right) \delta \phi .
$$

Hence,

$$
2 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) \thinspace \delta p = \frac { 1 } { V } \frac { d V } { d t } \thinspace \delta \sigma - \frac { d \thinspace \delta \sigma } { d t } = \mathrm { ~ - ~ } V \frac { d } { d t } \Big ( \frac { \delta \sigma } { V } \Big ) .
$$

Let the velocity of $P$ in the directions of $_ { T }$ and $\boldsymbol { \mathscr { N } }$ with reference to the fixed axes be $d T / d t$ and $d N / d t .$ ，respectively; then the kinetic energy of $P$ is

$$
\frac { 1 } { 2 } \left[ \frac { d T } { d t } + \frac { d \delta \sigma } { d t } + \left( \frac { d \psi } { d t } + n ^ { \prime } \right) \delta p \right] ^ { 2 } + \frac { 1 } { 2 } \left[ \frac { d N } { d t } + \frac { d \delta \rho } { d t } - \left( \frac { d \psi } { d t } + n ^ { \prime } \right) \delta \sigma \right]
$$

The true force function devoid of the Coriolis force is

$$
U = F - { \textstyle \frac { 1 } { 2 } } n ^ { \prime 2 } ( X ^ { 2 } + Y ^ { 2 } ) .
$$

Hence the Lagrangian equations of motion are

$$
\begin{array} { c } { { \displaystyle \frac { d ^ { 2 } N } { d t ^ { 2 } } + \frac { d ^ { 2 } } { d t ^ { 2 } } - 2 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) \frac { d \delta \sigma } { d t } - \frac { d ^ { 2 } \psi } { d t ^ { 2 } } \delta \sigma - \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) \frac { d T } { d t } } } \\ { { - \left( \frac { d \psi } { d t } + n ^ { \prime } \right) ^ { 2 } \delta p = \frac { \partial U } { \partial N } + \frac { \partial ^ { 2 } U } { \partial N ^ { 2 } } \delta p + \frac { \partial ^ { 2 } U } { \partial N \partial T } \delta \sigma , } } \\ { { \displaystyle \frac { d ^ { 2 } T } { d t ^ { 2 } } + \frac { d ^ { 2 } \delta \sigma } { d t ^ { 2 } } + 2 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) \frac { d \delta p } { d t } + \frac { d ^ { 2 } \psi } { d t ^ { 2 } } \delta p + \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) \frac { d N } { d t } } } \\ { { - \left( \frac { d \psi } { d t } + n ^ { \prime } \right) ^ { 2 } \delta \sigma = \frac { \partial U } { \partial T } + \frac { \partial ^ { 2 } U } { \partial T \partial N } \delta p + \frac { \partial ^ { 2 } U } { \partial T ^ { 2 } } \delta \sigma . } } \end{array}
$$

The equation (24) should hold also for $\delta \ p = \delta \sigma = 0$ ，so that

$$
\frac { d ^ { 2 } N } { d t ^ { 2 } } - \left( \frac { d \psi } { d t } + n ^ { \prime } \right) \frac { d T } { d t } = \frac { \partial U } { \partial N } \cdot
$$

Subtracting this from (24), we obtain

$$
\begin{array} { c } { \displaystyle \frac { d ^ { 2 } \delta \phi } { d t ^ { 2 } } - 2 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) \frac { d \delta \sigma } { d t } - \frac { d ^ { 2 } \psi } { d t ^ { 2 } } \delta \sigma - \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) ^ { 2 } \delta p } \\ { = \frac { \partial ^ { 2 } U } { \partial N ^ { 2 } } \delta \phi + \frac { \partial ^ { 2 } U } { \partial T \partial N } \delta \sigma . } \end{array}
$$

The equation (24) should hold also for $\delta \mathbf { \boldsymbol { p } } = 0 , \delta \sigma = V \delta t .$ so that

$$
{ \frac { \ l ^ { 2 } N } { d t ^ { 2 } } } - 2 \left( { \frac { d \psi } { d t } } + n ^ { \prime } \right) { \frac { d \delta \sigma } { d t } } - { \frac { d \ o ^ { 2 } \psi } { d t ^ { 2 } } } \delta \sigma - \left( { \frac { d \psi } { d t } } + n ^ { \prime } \right) { \frac { d T } { d t } } = { \frac { \partial U } { \partial N } } + { \frac { \partial \ o ^ { 2 } U } { \partial N \partial T } }
$$

Subtracting from (24a) we obtain

$$
- 2 \Bigl ( \frac { d \psi } { d t } + n ^ { \prime } \Bigr ) \frac { d \hat { \delta } \sigma } { d t } - \frac { d ^ { 2 } \psi } { d t ^ { 2 } } \hat { \delta } \sigma = \frac { \hat { \partial } ^ { 2 } U } { \partial N \partial T } \hat { \delta } \sigma ,
$$

or

$$
- 2 \Bigl ( { \frac { d \psi } { d t } } + n ^ { \prime } \Bigr ) { \frac { d V } { d t } } - { \frac { d ^ { 2 } \psi } { d t ^ { 2 } } } V = { \frac { \partial ^ { 2 } U } { \partial N \partial T } } V .
$$

Combining with (24b), we obtain

$$
{ \frac { d ^ { 2 } } { d t ^ { 2 } } } - 2 \Big ( { \frac { d \psi } { d t } } + n ^ { \prime } \Big ) \Big ( { \frac { d \delta \sigma } { d t } } - { \frac { 1 } { V } } { \frac { d V } { d t } } \delta \sigma \Big ) - \Big ( { \frac { d \psi } { d t } } + n ^ { \prime } \Big ) ^ { 2 } \delta p = { \frac { \partial ^ { 2 } U } { \partial N ^ { 2 } } } \delta p .
$$

Combining with (23),we find

$$
\frac { d ^ { 2 } \hat { \delta } \phi } { d t ^ { 2 } } + 3 \Big ( \frac { d \psi } { d t } + \eta ^ { \prime } \Big ) ^ { 2 } \hat { \delta } \phi = \frac { \partial ^ { 2 } U } { \partial N ^ { 2 } } \hat { \delta } \phi .
$$

Put

$$
( n - n ^ { \prime } ) ^ { 2 } \Theta = 3 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) ^ { 2 } - \frac { \partial ^ { 2 } U } { \partial N ^ { 2 } } ;
$$

then,

$$
\begin{array} { r } { \frac { d ^ { 2 } \delta \phi } { d t ^ { 2 } } + ( n - n ^ { \prime } ) ^ { 2 } \Theta \cdot \delta \phi = 0 . } \end{array}
$$

This is Hill's equation,which will be discussed in detail in Chapter l2. The generating particular periodic solution should be substituted in $\Theta$ ， so that $\Theta$ can be expanded in Fourier series

$$
\Theta = \Theta _ { 0 } + 2 \Theta _ { 1 } \cos 2 t + 2 \Theta _ { 2 } \cos 4 t + \cdot \cdot \cdot .
$$

Let $\Theta _ { j } = \Theta _ { - j }$ then

$$
\frac { d ^ { 2 } ~ \hat { \delta } \hat { \rho } } { d t ^ { 2 } } + ~ ( n - n ^ { \prime } ) ^ { 2 } \bigg ( \sum _ { j = - \infty } ^ { \infty } ~ \Theta _ { j } \cos 2 j t \bigg ) \cdot \hat { \delta } \hat { \rho } = 0 .
$$

Similarly, puting $\delta \pmb { \mathscr { p } } = \delta \sigma = 0$ and then $\delta { p } = 0 , \delta { \sigma } = V \delta { t }$ in (25), and referring to

$$
\frac { d ^ { 2 } V } { d t ^ { 2 } } - V \bigg ( \frac { d \psi } { d t } + n ^ { \prime } \bigg ) ^ { 2 } = V \frac { \partial ^ { 2 } U } { \partial T ^ { 2 } } ,
$$

we obtain

$$
\begin{array} { c } { { ( n - n ^ { \prime } ) ^ { 2 } \Theta = \displaystyle \frac { 1 } { V } \frac { d ^ { 2 } V } { d t ^ { 2 } } + 2 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) ^ { 2 } - \nabla ^ { 2 } U , } } \\ { { \nabla ^ { 2 } = \displaystyle \frac { \partial ^ { 2 } } { \partial T ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial N ^ { 2 } } = \frac { \partial ^ { 2 } } { \partial X ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial Y ^ { 2 } } . } } \end{array}
$$

Since

$$
{ \cal F } = { \cal U } + { \scriptstyle \frac { 1 } { 2 } } n ^ { \prime 2 } ( X ^ { 2 } + Y ^ { 2 } ) ,
$$

and

$$
U = \frac { \mu } { r } + \frac { 3 } { 2 } n ^ { \prime 2 } X ^ { 2 } - \frac { n ^ { \prime 2 } } { 2 } ( X ^ { 2 } + Y ^ { 2 } ) ,
$$

we have

$$
\nabla ^ { 2 } U = \nabla ^ { 2 } F - 2 n ^ { \prime 2 } .
$$

Hence,

$$
( n - n ^ { \prime } ) ^ { 2 } \Theta = \frac { 1 } { V } \frac { d ^ { 2 } V } { d t ^ { 2 } } + 2 \Big ( \frac { d \psi } { d t } + n ^ { \prime } \Big ) ^ { 2 } - \nabla ^ { 2 } F + 2 n ^ { \prime 2 } .
$$

If we use the variables $\boldsymbol { u }$ and $\pmb { \mathscr { s } }$ in place of $X$ and $Y$ , then we obtain

$$
V ^ { 2 } = \dot { X } ^ { 2 } + \dot { Y } ^ { 2 } = \dot { u } \dot { s } = - \nu ^ { 2 } D u D s ,
$$

$$
\frac { d \psi } { d t } = \frac { \ddot { Y } \dot { X } - \ddot { X } \dot { Y } } { V ^ { 2 } } = \frac { \sqrt { - 1 } } { 2 V ^ { 2 } } \left( \ddot { s } \dot { u } - \dot { s } \ddot { u } \right) = \frac { 1 } { 2 } \nu \bigg ( \frac { D ^ { 2 } u } { D u } - \frac { D ^ { 2 } s } { D s } \bigg ) ,
$$

$$
\begin{array} { r c l } { { \displaystyle \frac { 1 } { V } \frac { d ^ { 2 } V } { d t ^ { 2 } } = \frac { 1 } { V } \frac { d } { d t } \left( \frac { 1 } { 2 V } \frac { d V ^ { 2 } } { d t } \right) = \frac { d } { d t } \left( \frac { 1 } { 2 V ^ { 2 } } \frac { d V ^ { 2 } } { d t } \right) + \frac { 1 } { 4 V ^ { 4 } } \left( \frac { d V ^ { 2 } } { d t } \right) ^ { 2 } } } \\ { { } } & { { } } \\ { { } } & { { = - \nu ^ { 2 } D \left( \frac { D V ^ { 2 } } { 2 V ^ { 2 } } \right) - \nu ^ { 2 } \left( \frac { D V ^ { 2 } } { 2 V ^ { 2 } } \right) ^ { 2 } } } \\ { { } } & { { } } \\ { { } } & { { = - \displaystyle \frac { 1 } { 2 } \nu ^ { 2 } D \left( \frac { D ^ { 2 } u } { D u } + \frac { D ^ { 2 } s } { D s } \right) - \frac { 1 } { 4 } \nu ^ { 2 } \left( \frac { D ^ { 2 } u } { D u } + \frac { D ^ { 2 } s } { D s } \right) ^ { 2 } , } } \\ { { } } & { { } } \\ { { } } & { { } } & { { \nabla ^ { 2 } F = \left( \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial \tau ^ { 2 } } \right) \left( \frac { \mu } { \tau } + \frac { 3 } { 2 } n ^ { \prime 2 } X ^ { 2 } \right) = \frac { \mu } { 2 } + 3 n ^ { \prime 2 } , } } \end{array}
$$$$
\nabla ^ { 2 } F = \bigg ( \frac { \partial ^ { 2 } } { \partial X ^ { 2 } } + \frac { \partial ^ { 2 } } { \partial Y ^ { 2 } } \bigg ) \bigg ( \frac { \mu } { r } + \frac { 3 } { 2 } n ^ { \prime 2 } X ^ { 2 } \bigg ) = \frac { \mu } { r ^ { 3 } } + 3 n ^ { \prime 2 } ,
$$

and finally

$$
\begin{array} { r } { \Theta = - \frac { \kappa } { r ^ { 3 } } - \mathbf { m } ^ { 2 } + 2 \Big [ \frac { 1 } { 2 } \left( \frac { D ^ { 2 } u } { D u } - \frac { D ^ { 2 } s } { D s } \right) + \mathbf { m } \Big ] ^ { 2 } } \\ { - \frac { 1 } { 2 } D \Big ( \frac { D ^ { 2 } u } { D u } + \frac { D ^ { 2 } s } { D s } \Big ) - \frac { 1 } { 4 } \left( \frac { D ^ { 2 } u } { D u } + \frac { D ^ { 2 } s } { D s } \right) ^ { 2 } . } \end{array}
$$

Substituting

$$
u = { \bf a } \cdot \sum _ { j = - \infty } ^ { \infty } a _ { 2 i } \zeta ^ { 2 i + 1 } , \qquad s = { \bf a } \cdot \sum _ { j = - \infty } ^ { \infty } a _ { - 2 i - 2 } \zeta ^ { 2 i + 1 } ,
$$

we find

$$
D ^ { 2 } \ S \rlap { / } \delta p = \left( \sum _ { j = - \infty } ^ { \infty } \breve { \Theta } _ { j } \zeta ^ { 2 j } \right) \cdot \delta p , \qquad \Theta _ { - j } = \Theta _ { j } .
$$

Hill (1886） and Brown (1893,1896c） gave alternative methods for arriving at this equation.

Hill (1886) took the equations

$$
\begin{array} { l } { { \displaystyle D ^ { 2 } u + 2 { \bf m } D u + 2 \frac { \partial \Omega } { \partial s } = 0 , } } \\ { ~ } \\ { { \displaystyle D ^ { 2 } s - 2 { \bf m } D s + 2 \frac { \partial \Omega } { \partial u } = 0 , } } \\ { { \displaystyle \Omega = \frac { \kappa } { \sqrt { u s } } + \frac { 3 } { 8 } { \bf m } ^ { 2 } ( u + s ) ^ { 2 } } , } \end{array}
$$

with the Jacobi integral

$$
D u D s + 2 \Omega = 2 C .
$$

If we operate with δ on these equations, we find

$$
\begin{array} { r } { D ^ { 2 } \delta u + 2 \mathbf { m } D \delta u + 2 \frac { \partial ^ { 2 } \Omega } { \partial u \partial s } \delta u + 2 \frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } \delta s = 0 , } \\ { D ^ { 2 } \delta s - 2 \mathbf { m } D \delta s + 2 \frac { \partial ^ { 2 } \Omega } { \partial u \partial s } \delta s + 2 \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } \delta u = 0 , } \\ { D u D \delta s + D s D \delta u + 2 \frac { \partial \Omega } { \partial u } \delta u + 2 \frac { \partial \Omega } { \partial s } \delta s = 0 . } \end{array}
$$

In these equations δ can be changed to $\pmb { D }$ ; that is, the system $\delta u = D u ,$ $\delta s = D s$ forms a particular solution. Take new variables $\boldsymbol { v }$ and w defined by $\delta u = D u \cdot v _ { \mathrm { ; } }$ $\delta s = D s \cdot w$ ； then after eliminating $\pmb { u }$ and $\pmb { \mathscr { s } }$ by (30), we obtain

$$
\begin{array} { r l r } & { } & { D u D ^ { 2 } v - 2 \bigg [ 2 \frac { \partial \Omega } { \partial s } + \mathbf { m } D u \bigg ] D v - 2 \frac { \partial ^ { 2 } D } { \partial s ^ { 2 } } D s \cdot ( v - w ) = 0 , } \\ & { } & { D s D ^ { 2 } w - 2 \bigg [ 2 \frac { \partial \Omega } { \partial u } - \mathbf { m } D s \bigg ] D w - 2 \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u \cdot ( w - v ) = 0 , } \\ & { } & { D u D s D ( v + w ) - 2 \bigg [ \frac { \partial \Omega } { \partial s } D s - \frac { \partial \Omega } { \partial u } D u + \mathbf { m } D u D s \bigg ] ( v - w ) = 0 . } \end{array}
$$

If the first and the second equations are multiplied respectively by $\mathit { D s }$ and $\ b { D u }$ and added, then the resulting equation is the derivative of the third equation. Subtracting the products we obtain

$$
\begin{array} { r } { D u D s D \rho - 2 \Delta \cdot \tau = 0 , } \\ { D [ D u D s D \tau ] - 2 \Delta \cdot D \rho - 2 \Big [ \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u ^ { 2 } + \frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } D s ^ { 2 } \Big ] \tau = 0 , } \end{array}
$$

where

$$
\Delta = \frac { \partial \Omega } { \partial s } D s - \frac { \partial \Omega } { \partial u } D u + \mathbf { m } D u D s ,
$$

$$
\rho = v + w , \qquad \tau = v - w .
$$

Eliminating $D _ { \rho }$ gives

$$
D [ D u D s D \tau ] \mathrm { ~ - ~ } 2 \Big [ \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u ^ { 2 } + \frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } D s ^ { 2 } + \frac { 2 \Delta ^ { 2 } } { D u D s } \Big ] \tau = 0 .
$$

Put

$$
\tau = \frac { W } { \sqrt { D u D s } } ;
$$

then,

$$
D ^ { 2 } W = \Theta W ,
$$

$$
\Theta = \frac { 2 } { D u D s } \left[ \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u ^ { 2 } + \frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } D s ^ { 2 } \right] + \left( \frac { 2 \Delta } { D u D s } \right) ^ { 2 } - \frac { D ^ { 2 } \Omega } { D u D s } - \left[ \frac { D \Omega } { D u D s } \right]
$$

Since

$$
\begin{array} { r } { D \Omega = \cfrac { \partial \Omega } { \partial u } D u + \cfrac { \partial \Omega } { \partial s } D s , \qquad } \\ { D ^ { 2 } \Omega = \cfrac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u ^ { 2 } + 2 \cfrac { \partial ^ { 2 } \Omega } { \partial u \partial s } D u D s + \cfrac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } D s ^ { 2 } \qquad } \\ { + 2 \mathbf { m } \Delta - 2 \mathbf { m } ^ { 2 } D u D s - 4 \cfrac { \partial \Omega } { \partial u } \cfrac { \partial \Omega } { \partial s } , } \end{array}
$$

we obtain

$$
\backprime = \frac { 1 } { D u D s } \left[ \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u ^ { 2 } - 2 \frac { \partial ^ { 2 } \Omega } { \partial u \partial s } D u D s + \frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } D s ^ { 2 } \right] + 3 \left( \frac { \Delta } { D u D s } \right) ^ { 2 } + { \bf \Delta } \mathbf { r }
$$

From the relation

$$
\frac { \partial \Omega } { \partial u } = - \frac { \kappa } { 2 r ^ { 3 } } s + \frac { 3 } { 4 } { \bf { m } } ^ { 2 } ( u + s ) , \frac { \partial \Omega } { \partial s } = - \frac { \kappa } { 2 r ^ { 3 } } u + \frac { 3 } { 4 } { \bf { m } } ^ { 2 } ( u + s ) ,
$$

$$
\frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } = \frac { 3 } { 4 } \frac { \kappa } { r ^ { 5 } } s ^ { 2 } + \frac { 3 } { 4 } { \bf m } ^ { 2 } , \frac { \partial ^ { 2 } \Omega } { \partial u \partial s } = \frac { 1 } { 4 } \frac { \kappa } { r ^ { 3 } } + \frac { 3 } { 4 } { \bf m } ^ { 2 } ,
$$

$$
\frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } = \frac { 3 } { 4 } \frac { \kappa } { r ^ { 5 } } u ^ { 2 } + \frac { 3 } { 4 } { \bf m } ^ { 2 } ,
$$

we find

$$
= \frac { \kappa } { r ^ { 3 } } + \frac { 3 } { 8 } \frac { \frac { \kappa } { r ^ { 5 } } [ u D s - s D u ] ^ { 2 } + \mathbf { m } ^ { 2 } ( D u - D s ) ^ { 2 } } { C - \Omega } + \frac { 3 } { 4 } \left[ \frac { \Delta } { C - \Omega } \right] ^ { 2 } + \mathbf { m } ^ { 2 } ,
$$

$$
= \bigg [ - \frac { \kappa } { 2 r ^ { 3 } } + \frac { 3 } { 4 } { \bf m } ^ { 2 } \bigg ] [ u D s - s D u ] - \frac { 3 } { 4 } { \bf m } ^ { 2 } ( u D u - s D s ) + 2 { \bf m } ( C - \Omega _ { \mathrm { N } } ) ,
$$

If it is desired to have $\mathbf { m }$ left indeterminate in the expansion of $\Theta$ ， it will be more advantageous to proceed in the following manner. From (30a) for $D ^ { 2 } \Omega$ we have

$$
\begin{array} { c } { { \frac { 2 } { u D s } \left[ \frac { \partial ^ { 2 } \Omega } { \partial u ^ { 2 } } D u ^ { 2 } + \frac { \partial ^ { 2 } \Omega } { \partial s ^ { 2 } } D s ^ { 2 } \right] = - 4 \frac { \partial ^ { 2 } \Omega } { \partial u \partial s } - 2 \Big ( \frac { \Delta } { D u D s } \Big ) ^ { 2 } + 2 { \bf m } ^ { 2 } } } \\ { { - \frac { D ^ { 2 } ( D u D s ) } { D u D s } + \frac { 1 } { 2 } \left[ \frac { D ( D u D s ) } { D u D s } \right. } } \end{array}
$$

Substituting this in @ and noting that

$$
4 \frac { \partial ^ { 2 } \Omega } { \partial u \partial s } = \frac { \kappa } { r ^ { 3 } } + 3 \mathbf { m } ^ { 2 } ,
$$

and

$$
\Delta = { \scriptstyle \frac { 1 } { 2 } } [ D u D ^ { 2 } s - D s D ^ { 2 } u ] - { \bf m } D u D s ,
$$

we obtain

$$
\begin{array} { c } { { \displaystyle \mathrm {  ~ \rho ~ } = - \left[ \frac { \kappa } { r ^ { 3 } } + { \bf m } ^ { 2 } \right] + 2 \left[ \frac { 1 } { 2 } \left( \frac { D ^ { 2 } u } { D u } - \frac { D ^ { 2 } s } { D s } \right) + { \bf m } \right] ^ { 2 } } } \\ { { \displaystyle - \left[ \frac { 1 } { 2 } \left( \frac { D ^ { 2 } u } { D u } + \frac { D ^ { 2 } s } { D s } \right) \right] ^ { 2 } - D \left[ \frac { 1 } { 2 } \left( \frac { D ^ { 2 } u } { D u } + \frac { D ^ { 2 } s } { D s } \right) \right] } } \end{array}
$$

which is the same as was given in (28). For the expansion of the frst term of this expression we may use

$$
\begin{array} { r } { \frac { \kappa } { r ^ { 3 } } + \mathbf { m } ^ { 2 } = \frac { D ^ { 2 } u + 2 \mathbf { m } D u + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } s } { u } + \frac { 5 } { 2 } \mathbf { m } ^ { 2 } } \\ { = \frac { D ^ { 2 } s - 2 \mathbf { m } D s + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } u } { s } + \frac { 5 } { 2 } \mathbf { m } ^ { 2 } , } \end{array}
$$

derived from (30),or

$$
\begin{array} { r } { \frac { \kappa } { r ^ { 3 } } + \mathbf { m } ^ { 2 } = \Big [ \frac { D u } { u } + \mathbf { m } \Big ] ^ { 2 } + D \Big [ \frac { D u } { u } + \mathbf { m } \Big ] + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } \Big [ 1 + \frac { s } { u } \Big ] } \\ { = \Big [ \frac { D s } { s } - \mathbf { m } \Big ] ^ { 2 } + D \Big [ \frac { D s } { s } - \mathbf { m } \Big ] + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } \Big [ 1 + \frac { u } { s } \Big ] . } \end{array}
$$

Hill's equation (29) is solved,as will be shown in Chapter 12, by means of Hill's infinite determinant, where $\Theta _ { j }$ is supposed to be a small quantity of order $2 j .$ Substitute

$$
\delta { p } = \sum _ { j = - \infty } ^ { \infty } b _ { j } \zeta ^ { 2 j + c }
$$

with an unknown constant $\pmb { c }$ in (29); then,

$$
\sum _ { j } b _ { j } ( c + 2 j ) ^ { 2 } \zeta ^ { 2 j + c } = \sum _ { i } \sum _ { j } \Theta _ { i } b _ { j - i } \zeta ^ { 2 j + c } ,
$$

or

$$
\begin{array} { l } { \frac { b _ { j } [ ( c + 2 j ) ^ { 2 } - \Theta _ { 0 } ] } { ( 2 j ) ^ { 2 } - \Theta _ { 0 } } - \displaystyle \sum _ { i = 0 } ^ { \infty } \frac { \Theta _ { i } b _ { j - i } } { ( 2 j ) ^ { 2 } - \Theta _ { 0 } } = 0 } \\ { \qquad ( j = - \infty , \ldots , 0 , \ldots , + \infty ) . } \end{array}
$$

These equations are infinite in number and contain an infinite number of unknown coefficients $b _ { j }$ $\textit { \ i } ( j = - \infty , . . . , 0 , . . . , + \infty )$ . Hill solved this infinite set of linear equations as if the numbers of the equations and of the unknown coefficients were finite.Put

$$
\begin{array} { r } { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \bf \Pi } \\ { \cdots \quad } \\ { \frac { 6 _ { 2 } } { 2 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 1 } } { 2 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 2 } } { 4 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 2 } } { 4 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 3 } } { 4 ^ { 2 } - 6 _ { 0 } } \quad \cdots } \\ { \frac { 6 _ { 1 } } { 4 ^ { 2 } - 6 _ { 0 } } \frac { \left( \iota - 2 \right) ^ { 2 } - 6 _ { 0 } } { 6 } \quad \frac { 6 _ { 1 } } { 2 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 1 } } { 2 ^ { 2 } - 6 _ { 1 } } \quad - \frac { 6 _ { 2 } } { 2 ^ { 2 } - 6 _ { 0 } } \quad \cdots } \\ { \bf \Pi } \\ { \cdots \quad } \\ { \bf \Pi } \\ { \cdots \quad } \\ { \quad \frac { 6 _ { 2 } } { 1 - 5 } \quad - \frac { 6 _ { 2 } } { 0 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 1 } } { 2 ^ { 2 } - 6 _ { 0 } } \quad \frac { \mathfrak { c } ^ { 2 } - 6 _ { 0 } } { 0 ^ { 2 } - 6 _ { 0 } } \quad - \frac { 6 _ { 1 } } { 0 ^ { 2 } - 6 _ { 0 } } \quad \cdots } \\ { \cdots \quad } \\ { \cdots \quad } \\ { \cdots \quad } \end{array}
$$

This equation determines the constant $\pmb { c }$ .The convergence of the process will be proved in Chapter 12. Any root $\pmb { c }$ can be shown to satisfy

$$
\sin ^ { 2 } \frac { \pi c } { 2 } = \Delta ( 0 ) \sin ^ { 2 } \frac { \pi \sqrt { \Theta _ { 0 } } } { 2 } ,
$$

where $\Delta ( 0 )$ is the value of $\Delta ( c )$ for ${ \mathfrak { c } } = 0$ and is expanded in the form

$$
\Delta ( 0 ) = 1 + \frac { \pi } { 4 } [ \Theta _ { 1 } ^ { 2 } ( 1 - \Theta _ { 0 } ) ^ { - 1 } \Theta _ { 0 } ^ { - 1 / 2 } ] \cot \frac { \pi \sqrt { \Theta _ { 0 } } } { 2 }
$$

up to the sixth order of the small quantity $\mathbf { m }$

Hil's variational equations were rigorously derived in terms of the regularizing variables (Section 17.9) by Wintner (l93la) and Rosenthal (1931).Let the equations for the variations $ { \boldsymbol { u } } ( t ) ,  { \boldsymbol { v } } ( t )$ be

$$
\begin{array} { r l } & { \frac { d ^ { 2 } u } { d t ^ { 2 } } - 2 \lambda _ { 0 } \frac { d v } { d t } = \Big [ \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial x ^ { 2 } } + 2 \frac { \partial \lambda _ { 0 } } { \partial x } \frac { d y _ { 0 } } { d t } \Big ] u + \Big [ \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial x ^ { 2 } } + 2 \frac { \partial \lambda _ { 0 } } { \partial y } \frac { d y _ { 0 } } { d t } \Big ] v , } \\ & { \frac { d ^ { 2 } v } { d t ^ { 2 } } + 2 \lambda _ { 0 } \frac { d u } { d t } = \Big [ \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial x \partial y } - 2 \frac { \partial \lambda _ { 0 } } { \partial x } \frac { d x _ { 0 } } { d t } \Big ] u + \Big [ \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial y ^ { 2 } } - 2 \frac { \partial \lambda _ { 0 } } { \partial y } \frac { d x _ { 0 } } { d t } \Big ] v , } \end{array}
$$

where the given periodic solution $x = x _ { 0 } ( t ) , y = y _ { 0 } ( t )$ is substituted in the coeffcients. This system of equations admits a homogeneous linear relation

$$
\frac { d x _ { 0 } } { d t } \frac { d u } { d t } + \frac { d y _ { 0 } } { d t } \frac { d v } { d t } - \frac { \partial \Omega _ { 0 } } { \partial x } u - \frac { \partial \Omega _ { 0 } } { \partial y } ^ { . } v = c ,
$$

which can be derived from the Jacobi integral

$$
{ \frac { 1 } { 2 } } \left( { \frac { d x } { d t } } \right) ^ { 2 } + { \frac { 1 } { 2 } } \left( { \frac { d y } { d t } } \right) ^ { 2 } - \Omega ( x , y ) = C ,
$$

if $c = \delta C .$ A solution of (35) is called an isoenergetic or Maupertuisian variation if the integration constant $\pmb { c }$ determined by the initial values of the solution vanishes; hence for all values of $\pmb { t }$ we have

$$
\frac { d x _ { 0 } } { d t } \frac { d u } { d t } + \frac { d y _ { 0 } } { d t } \frac { d v } { d t } - \frac { \partial \Omega _ { 0 } } { \partial x } u ( t ) - \frac { \partial \Omega _ { 0 } } { \partial y } v ( t ) = 0 .
$$

This represents the isoenergetic variation of the periodic solution $\begin{array} { r } { \pmb { u } = d \pmb { x } _ { 0 } / d t , } \end{array}$ $v = d y _ { 0 } / d t$ .It is possible to choose the origin $t = 0$ so that for the given solution we have ${ \pmb x } _ { 0 } ( 0 ) \neq 0$ ， $y _ { 0 } ( 0 ) \neq 0 .$ ， $d { x _ { 0 } } ( 0 ) / d t \ne 0 .$ $d y _ { 0 } ( 0 ) / d t \ne 0$ . The solution $\pmb { u } = \pmb { u } ( t )$ ， $v = v ( t )$ defined by the initial condition $u ( 0 ) , v ( 0 ) , d u ( 0 ) / d t , d v ( 0 ) / d t$ is an isoenergetic variation if and only if

$$
\begin{array} { r } { \frac { d x _ { 0 } ( 0 ) } { d t } \frac { d u ( 0 ) } { d t } + \frac { d y _ { 0 } ( 0 ) } { d t } \frac { d v ( 0 ) } { d t } - \frac { \partial \Omega _ { 0 } ( 0 ) } { \partial x } u ( 0 ) - \frac { \partial \Omega _ { 0 } ( 0 ) } { \partial y } v ( 0 ) = 0 . } \end{array}
$$

Thus the manifold of the isoenergetic variations depends on three of the four arbitrary constants in the initial condition.

The projection of the variation $\boldsymbol { u } = \boldsymbol { \delta x } ,$ $\boldsymbol { v } = \delta \boldsymbol { y }$ on the oriented normal of the curve $x = x _ { 0 } ( t ) , y = y _ { 0 } ( t )$ , belonging to a fixed value of $t _ { \ast }$ is

$$
\zeta ( t ) = \frac { - d y _ { 0 } / d t } { \sqrt { ( d x _ { 0 } / d t ) ^ { 2 } + ( d y _ { 0 } / d t ) ^ { 2 } } } u ( t ) + \frac { d x _ { 0 } / d t } { \sqrt { ( d x _ { 0 } / d t ) ^ { 2 } + ( d y _ { 0 } / d t ) ^ { 2 } } } v ( t ) .
$$

We call a given function of $t$ an isoenergetic normal displacement of the curve ${ \boldsymbol x } = { \boldsymbol x } _ { 0 } ( t )$ ， $y = y _ { 0 } ( t )$ if and only if there exists at least one isoenergetic variation $u = u ( t ) , v = v ( t )$ ，by means of which the given function is represented in this form $\zeta ( t )$

It can be shown that the isoenergetic normal displacements are characterized as the solutions of a linear differential equation of the second order, called the Jacobi equation,

$$
\begin{array} { r l } { \sqrt { \frac { d x _ { 0 } } { d t } \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } + \frac { d y _ { 0 } } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } } \bigg | } & { } \\ { - [ \frac { d u } { d t } \frac { d x _ { 0 } } { d t } + \frac { d v } { d t } \frac { d y _ { 0 } } { d t } - u \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } - v \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } ] [ \frac { d x _ { 0 } } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } - \frac { d y _ { 0 } } { d t } \frac { d ^ { 2 } } { d }  } \\ { +  [ \frac { d u } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } - \frac { d v } { d t } \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } ] [ ( \frac { d x _ { 0 } } { d t } ) ^ { 2 } + ( \frac { d y _ { 0 } } { d t } ) ^ { 2 } ]  } & { } \\ {  - \vartheta [ ( \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } ) ^ { 2 } + ( \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } ) ^ { 2 } ] = 0 , } & { ( \frac { d x _ { 0 } } { d t ^ { 2 } } ) ^ { 2 } } \end{array}
$$

where

$$
\vartheta ( t ) = \left| { \frac { d x _ { 0 } } { d t } } \quad { \frac { d y _ { 0 } } { d t } } \right| = \left[ \left( { \frac { d x _ { 0 } } { d t } } \right) ^ { 2 } + \left( { \frac { d y _ { 0 } } { d t } } \right) ^ { 2 } \right] ^ { 1 / 2 } \zeta .
$$

In fact, let $u = u ( t ) , v = v ( t )$ be an isoenergetic variation so that (35) and (36) are satisfied. Since

$$
\frac { \partial \Omega _ { 0 } } { \partial x } = \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } - 2 \lambda _ { 0 } \frac { d y _ { 0 } } { d t } , \qquad \frac { \partial \Omega _ { 0 } } { \partial y } = \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } + 2 \lambda _ { 0 } \frac { d x _ { 0 } } { d t } ,
$$

we have, from (36),

$$
- 2 \lambda _ { 0 } \vartheta = \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } u + \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } v - \frac { d x _ { 0 } } { d t } \frac { d u } { d t } - \frac { d y _ { 0 } } { d t } \frac { d v } { d t } \cdot
$$

The definition of $\vartheta$ gives

$$
\frac { { { \bf \Pi } ^ { 2 } } { \vartheta } } { { { l } { t } ^ { 2 } } } + 2 \Bigl [ \frac { d u } { d t } \frac { d ^ { 2 } y _ { 0 } } { d { { t } ^ { 2 } } } - \frac { d v } { d t } \frac { d ^ { 2 } x _ { 0 } } { d { { t } ^ { 2 } } } \Bigr ] = v \frac { d ^ { 3 } x _ { 0 } } { d t ^ { 3 } } - v \frac { d ^ { 3 } y _ { 0 } } { d t ^ { 3 } } + \frac { d ^ { 2 } v } { d t ^ { 2 } } \frac { d x _ { 0 } } { d t } - \frac { d ^ { 2 } u } { d t ^ { 2 } } \frac { d y _ { 0 } } { d t } ,
$$

or

$$
\frac { d ^ { 2 } \vartheta } { d t ^ { 2 } } + 2 \biggl [ \frac { d u } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } - \frac { d v } { d t } \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } \biggr ] = L ( t ) \cdot \vartheta ,
$$

where

$$
L ( t ) = - 4 [ \lambda _ { 0 } ] ^ { 2 } + \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial y ^ { 2 } } - \biggl \{ \frac { d x _ { 0 } } { d t } \frac { \partial \lambda _ { 0 } } { \partial y } - \frac { d y _ { 0 } } { d t } \frac { \partial \lambda _ { 0 } } { \partial x } \biggr \} .
$$

Substituting (38) and (39) in (37), we obtain

$$
\alpha ( t ) \frac { d ^ { 2 } \vartheta } { d t ^ { 2 } } + \beta ( t ) \frac { d \vartheta } { d t } + \gamma ( t ) \vartheta = 0 ,
$$

where

$$
\begin{array} { r l } & { \alpha ( t ) \ : = \ : - \ : \frac { 1 } { 2 } \left[ \left( \frac { d x _ { 0 } } { d t } \right) ^ { 2 } + \left( \frac { d y _ { 0 } } { d t } \right) ^ { 2 } \right] , } \\ & { \beta ( t ) \ : = \ : \frac { d x _ { 0 } } { d t } \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } + \frac { d y _ { 0 } } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } , } \\ & { \gamma ( t ) \ : = 2 \lambda _ { 0 } \bigg [ \frac { d x _ { 0 } } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } - \frac { d y _ { 0 } } { d t } \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } \bigg ] \ : - \ : \left[ \left( \frac { d ^ { 2 } x _ { 0 } } { d t ^ { 2 } } \right) ^ { 2 } + \left( \frac { d ^ { 2 } y _ { 0 } } { d t ^ { 2 } } \right) ^ { 2 } \right] } \\ & { \hphantom { \frac { 2 } { = \lambda _ { 0 } } } + \frac { 1 } { 2 } \left[ \left( \frac { d x _ { 0 } } { d t } \right) ^ { 2 } + \left( \frac { d y _ { 0 } } { d t } \right) ^ { 2 } \right] \bigg [ - 4 ( \lambda _ { 0 } ) ^ { 2 } + \frac { \partial ^ { 2 } \Omega _ { 0 } } { \partial x ^ { 2 } } + } \\ & { \hphantom { \frac { 2 } { = } } - \left( \frac { d x _ { 0 } } { d t } \frac { \partial \lambda _ { 0 } } { \partial y } - \frac { d y _ { 0 } } { d t } \frac { d ^ { 2 } y _ { 0 } } { d t } \right) } \end{array}
$$

Referring to the definition of $\vartheta$ , the self-adjoint equation

$$
\frac { d ^ { 2 } \zeta } { d t ^ { 2 } } + \nu ( t ) \zeta = 0
$$

is derived, where $\nu ( t )$ is a given function of $t .$ .This is the required equation for any isoenergetic normal displacement.

The converse of the theorem can be shown, that is,any solution of the differential equation (4l） is an isoenergetic normal displacement of ${ \boldsymbol x } = { \boldsymbol x } _ { 0 } ( t )$ ， $y = y _ { 0 } ( t )$ ; that is, there exists for any solution $\vartheta = \vartheta ( t )$ of (40) at least one pair $\pmb { u } = \pmb { u } ( t )$ ， $\boldsymbol { v } = \boldsymbol { v } ( t )$ ,such that for the three functions $\vartheta ( t ) , u ( t ) , v ( t )$ ,the conditions (35) and (36)are satisfied by the foregoing definition of $\vartheta ( t )$

In fact, an arbitrary given solution $\vartheta = \vartheta ( t )$ of (30) is characterized by the initial values $\vartheta ( 0 )$ and $d \vartheta ( 0 ) / d t$ The four initial values $u ( 0 ) , v ( 0 )$ ， $d u ( 0 ) / d t , \ d v ( 0 ) / d t$ are obtained, if one of them, for example $u ( 0 )$ ，is arbitrarily chosen, from the three conditions

$$
\begin{array} { r l } & { \quad \quad [ - \vartheta ( 0 ) - \frac { d y _ { 0 } ( 0 ) } { d t } u ( 0 ) ] + \frac { d x _ { 0 } ( 0 ) } { d t } v ( 0 ) = 0 , } \\ & { \quad \quad \frac { d \vartheta ( 0 ) } { d t } - \frac { d ^ { 2 } y _ { 0 } ( 0 ) } { d t ^ { 2 } } u ( 0 ) ] + \frac { d ^ { 2 } x _ { 0 } ( 0 ) } { d t ^ { 2 } } v ( 0 ) - \frac { d y _ { 0 } ( 0 ) } { d t } \frac { d u ( 0 ) } { d t } } \\ & { \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad + \frac { d x _ { 0 } ( 0 ) } { d t } \frac { d v ( 0 ) } { d t } = 0 } \\ & { \quad \quad \quad \quad - \frac { \partial \Omega _ { 0 } ( 0 ) } { \partial x } u ( 0 ) \Big ] - \frac { \partial \Omega _ { 0 } ( 0 ) } { \partial x _ { t } } v ( 0 ) + \frac { d x _ { 0 } ( 0 ) } { d t } \frac { d u ( 0 ) } { d t } + \frac { d y _ { 0 } ( 0 ) } { d t } \frac { d v ( 0 ) } { d t } = 0 , } \end{array}
$$

which determine $u ( 0 ) , v ( 0 ) , d v ( 0 ) / d t$ uniquely. Let $u = u ^ { * } ( t )$ ， $v = v ^ { * } ( t )$ denote the solution of (35) with the initial values $u ( 0 ) , v ( 0 ) , d u ( 0 ) / d t ,$ $d v ( 0 ) / d t$ .The integration constant $c$ for this solution is by the third equation of (42) equal to zero; that is,(42) is an isoenergetic variation and

$$
\vartheta ^ { * } ( t ) = \left| \begin{array} { c c } { \frac { d x _ { 0 } } { d t } } & { \frac { d y _ { 0 } } { d t } } \\ { u ^ { * } ( t ) } & { v ^ { * } ( t ) } \end{array} \right|
$$

is a solution of (40). From (42), we have

$$
\vartheta ( 0 ) = \vartheta ^ { \ast } ( 0 ) , \frac { d \vartheta ( 0 ) } { d t } = \frac { d \vartheta ^ { \ast } ( 0 ) } { d t } \cdot
$$

Hence the given solution $\vartheta ( t )$ of (40) has the same initial value as this solution $\vartheta ^ { \ast } ( t )$ . Accordingly $\vartheta ( t ) = \vartheta ^ { \ast } ( t )$ ，and hence the arbitrarily given solution $\vartheta ( t )$ ， can be represented by the use of an isoenergetic variation $u = u ( t )$ ， $v = v ( t )$

Thus the theorem is rigorously proved, that a function $f ( t )$ of $t$ is an isoenergetic normal displacement of ${ \pmb x } = { \pmb x } _ { 0 } ( t )$ ， $y = y _ { 0 } ( t )$ if and only if $\zeta = f ( t )$ satisfies the differential equation (41), namely, Hil's equation.

So far，we have considered isoenergetic displacements that Hil, Poincaré,and Wintner have dealt with. Now we shall study nonisoenergetic displacements for the generalization.Suppose that the equations of motion,by generalizing (20),are

$$
\ddot { X } = 2 A \dot { Y } + F _ { x } , \qquad \ddot { Y } = - 2 A \dot { X } + F _ { x } ,
$$

where $\pmb { A }$ and ${ \pmb F }$ are functions of $X , Y ,$ obtained by a regularizing transformation, for example of Birkhoff (1914; Section 17.13),and the corresponding Jacobi integral is

$$
C = F - { \textstyle \frac { 1 } { 2 } } ( \dot { X } ^ { 2 } + \dot { Y } ^ { 2 } ) .
$$

Consider a nonisoenergetic displacement $\xi ( t ) , \eta ( t )$ in the directions of $X , ~ Y ,$ respectively, from the periodic solution $X ( t ) , ~ Y ( t )$ of (43),such that

$$
\begin{array} { r l } & { \ddot { \xi } = 2 A \dot { \eta } + ( F _ { X X } + 2 A _ { X } \dot { Y } ) \xi + ( F _ { X Y } + 2 A _ { Y } \dot { Y } ) \eta , } \\ & { \ddot { \eta } = - 2 A \dot { \xi } + ( F _ { X Y } - 2 A _ { X } \dot { X } ) \xi + ( F _ { Y Y } - 2 A _ { Y } \dot { X } ) \eta , } \end{array}
$$

with the Jacobi constant $C ^ { \prime }$ . Write $\gamma = C - C ^ { \prime }$ ; then,

$$
\gamma = F _ { x } \xi + F _ { Y } \eta - \dot { X } \dot { \xi } - \dot { Y } \dot { \eta } .
$$

Put $\dot { X } = V \cos \psi , \dot { Y } = V \sin \psi _ { ; }$ and define the corresponding normal and tangential displacements $\delta \mathbfit { p }$ and $\delta \sigma$ by

$$
\xi = \hat { \delta } \sigma \cdot \cos \psi - \delta \pmb { \dot { p } } \cdot \sin \psi , ~ \eta = \hat { \delta } \sigma \cdot \sin \psi + \hat { \delta } \pmb { \dot { p } } \cdot \cos \psi ;
$$

then,

$$
\begin{array} { r l } & { \Dot { X } \eta - \Dot { Y } \xi = V \delta p , } \\ & { \Ddot { X } \xi + \Ddot { Y } \eta = \Dot { V } \delta \sigma + V \Dot { \psi } \delta p , } \\ & { \Ddot { X } \eta - \Ddot { Y } \xi = ( \Ddot { V } - V \Dot { \psi } ^ { 2 } ) \ \delta p - ( 2 \Dot { V } \Dot { \psi } + V \Ddot { \psi } ) \ \delta \sigma . } \end{array}
$$

We also have

$$
\dot { X } \dot { \xi } + \dot { Y } \dot { \eta } = V \frac { d } { d t } \left( \delta \sigma \right) - V \dot { \psi } \ \delta \pounds _ { \mathbf { \cdot } }
$$

On the other hand, the equations for $\xi , \ddot { \eta }$ are transformed to

$$
\begin{array} { r l } & { \ddot { \xi } = \cos \psi \displaystyle \frac { d ^ { 2 } } { d t ^ { 2 } } \delta \sigma - \sin \psi \displaystyle \frac { d ^ { 2 } } { d t ^ { 2 } } \delta \phi + \xi \dot { \psi } ^ { 2 } - 2 \dot { \eta } \dot { \psi } - \eta \ddot { \psi } , } \\ & { \ddot { \eta } = \sin \psi \displaystyle \frac { d ^ { 2 } } { d t ^ { 2 } } \delta \sigma + \cos \psi \displaystyle \frac { d ^ { 2 } } { d t ^ { 2 } } \delta \phi + \eta \dot { \psi } ^ { 2 } + 2 \dot { \xi } \dot { \psi } + \xi \ddot { \psi } . } \end{array}
$$

Hence,

$$
\dot { X } \ddot { \eta } - \dot { Y } \dot { \xi } = V \Big ( \frac { d ^ { 2 } } { d t ^ { 2 } } \delta \rlap { / } p - \dot { \psi } ^ { 2 } \delta p + 2 \dot { \psi } \frac { d } { d t } \delta \sigma + \ddot { \psi } \delta \sigma \Big ) .
$$

Substituting these relations (45), (46), (47), (48) in the equations

$$
\begin{array} { r } { \dot { \gamma } _ { \eta } - \ddot { Y } \xi + \dot { X } \ddot { \eta } - \dot { Y } \xi = 2 A ( \ddot { X } \xi + \ddot { Y } \eta - \dot { X } \dot { \xi } - \dot { Y } \dot { \eta } ) \qquad } \\ { + ( \dot { X } \eta - \dot { Y } \xi ) ( F _ { x x } + F _ { \mathrm { { Y } } \tau } + 2 A _ { x } \dot { Y } - 2 A _ { \mathrm { { Y } } } \dot { \zeta } ) \qquad } \end{array}
$$

obtained by differentiating (43） with respect to $t ,$ ， we can derive the equation

$$
\begin{array} { r } { \frac { d ^ { 2 } } { d t ^ { 2 } } \mathring { \partial } \dot { p } + \biggl [ \frac { \ddot { V } } { V } - 2 \dot { \psi } ( 2 A + \dot { \psi } ) - F _ { X X } - F _ { Y Y } - 2 A _ { X } \dot { Y } + 2 A _ { Y } \dot { X } \biggr ] \mathring { \partial } \dot { p } } \\ { = 2 ( A + \dot { \psi } ) \biggl ( \dot { V } \delta \sigma - V \frac { d } { d t } \mathring { \partial } \sigma \biggr ) \biggl / V . } \end{array}
$$

From the definition

$$
\delta \phi = - \xi \sin \psi + \eta \cos \psi , \qquad \delta \sigma = \xi \cos \psi + \eta \sin \psi
$$

and the equations of motion (43), we se that

$$
{ \cal F } _ { X } \xi + { \cal F } _ { Y } \eta = \dot { V ^ { } } \delta \sigma + V \dot { \psi } \delta \sigma + 2 V A \delta \rho .
$$

Thus, using (48), we obtain from the nonconservative integral (44) the relation

$$
V \frac { d } { d t } \delta \sigma - \dot { V } \delta \sigma = - \gamma + 2 V ( A + \dot { \psi } ) \delta \rho ,
$$

or Hil's equation for nonisoenergetic displacements

$$
\frac { d ^ { 2 } } { d t ^ { 2 } } \delta { \dot { p } } + ( n - n ^ { \prime } ) ^ { 2 } \Theta \delta { \dot { p } } = \frac { 2 \gamma ( A + { \dot { \psi } } ) } { V } ,
$$

with

$$
\begin{array} { c } { { ( n - n ^ { \prime } ) ^ { 2 } { \Theta } = \displaystyle \frac { \ddot { V } } { V } + 2 ( A + \dot { \psi } ) ^ { 2 } + 2 A ^ { 2 } - F _ { x x } - F _ { \mathrm { Y Y } } } } \\ { { - 2 V ( A _ { x } \sin \psi - A _ { \mathrm { Y } } \cos \psi ) , } } \end{array}
$$

and the corresponding tangential displacement

$$
\frac { d } { d t } \left( \frac { \delta \sigma } { V } \right) = 2 ( A + \dot { \psi } ) \frac { \delta \phi } { V } - \frac { \gamma } { V ^ { 2 } } \cdot
$$

These relations were derived by Deprit and Henrard (l966; Section 18.25).

From (43) we obtain

$$
\begin{array} { l } { { F _ { X } ^ { 2 } + F _ { Y } ^ { 2 } = { \dot { V } } ^ { 2 } + V ^ { 2 } ( 2 A + { \dot { \psi } } ) ^ { 2 } , } } \\ { { { \ddot { X } } ^ { 2 } + { \ddot { Y } } ^ { 2 } = { \dot { V } } ^ { 2 } ( 1 + { \dot { \psi } } ^ { 2 } ) . } } \end{array}
$$

Since

$$
{ \cal V } \ddot { \cal V } + \dot { \cal V } ^ { 2 } = \dot { \cal X } \ddot { \cal X } + \dot { \cal Y } \ddot { \cal Y } + \ddot { \cal X } ^ { 2 } + \ddot { \cal Y } ^ { 2 } ,
$$

we have

$$
{ \frac { \ddot { V } } { V } } = { \dot { \psi } } ^ { 2 } + { \frac { { \dot { X } } { \ddot { X } } + { \dot { Y } } { \ddot { Y } } } { V ^ { 2 } } } .
$$

Hence, substituting in (5la),we find

$$
\begin{array} { c } { { \displaystyle - n ^ { \prime } ) ^ { 2 } \Theta = \displaystyle \frac { ( \dot { X } \ddot { X } + \dot { Y } \ddot { Y } ) } { V ^ { 2 } } + 3 \dot { \psi } ^ { 2 } + 4 A \dot { \psi } + 4 A ^ { 2 } } } \\ { { - F _ { X X } - F _ { Y Y } - 2 V ( A _ { x } \sin \psi + A _ { Y } \cos \psi _ { \mathrm { . } } } } \end{array}
$$

This formula with $\scriptstyle A \equiv 0$ was derived by Poincaré (1899). Since

$$
\begin{array} { c } { { F _ { x } ^ { 2 } = F _ { Y } ^ { 2 } + 2 A ( F _ { x } \dot { Y } - F _ { Y } \dot { X } ) } } \\ { { = \dot { V } ^ { 2 } + V ^ { 2 } \dot { \psi } ^ { 2 } + 2 V A \dot { \psi } , } } \end{array}
$$

we see that

$$
\begin{array} { r l } & { V ^ { 2 } ( n - n ^ { \prime } ) ^ { 2 } \Theta = V \ddot { V } - 2 \dot { V } ^ { 2 } + 2 ( F _ { X } ^ { 2 } + F _ { Y } ^ { 2 } ) } \\ & { \phantom { V ^ { 2 } ( n - n ^ { \prime } ) ^ { 2 } \Theta } + 4 A ( F _ { X } \dot { Y } - F _ { \mathrm { Y } } \dot { X } ) + 4 A ^ { 2 } } \\ & { \phantom { V ^ { 2 } ( n - n ^ { \prime } ) ^ { 2 } \Theta } - F _ { X X } - F _ { \mathrm { Y } Y } - 2 ( A _ { X } \dot { Y } - A _ { \mathrm { Y } } \dot { X } ) . } \end{array}
$$

# 11.6 TERMS DEPENDING ON m AND $e$

Now we consider the general solution of (8). The solution of Hill's equation (26) with an arbitrary constant $t _ { 1 }$ is

$$
\delta p = \zeta _ { 1 } ^ { \pm c } \cdot \sum _ { j } b _ { j } \zeta ^ { 2 j } , \qquad \zeta _ { 1 } = \exp { \{ \sqrt { - 1 } ( n - n ^ { \prime } ) ( t - t _ { 1 } ) \} } ,
$$

where $t _ { 1 }$ gives an arbitrary phase and one of the $b _ { j }$ is an arbitrary amplitude. We have from (23)

$$
2 { \left( { \frac { d \psi } { d t } } + n ^ { \prime } \right) } ~ \delta \beta = ~ - ~ V { \frac { d } { d t } } \left( { \frac { \delta \sigma } { V } } \right) ,
$$

or from (27)

$$
\bigg ( \frac { D ^ { 2 } u } { D u } - \frac { D ^ { 2 } s } { D s } + 2 \mathbf { m } \bigg ) \ : \delta p = - \sqrt { - 1 } \ : V D \bigg ( \frac { \delta \sigma } { \overline { { V } } } \bigg ) ,
$$

where $V$ is an even function of $\zeta$ and $\sqrt { - 1 } \ \delta \sigma$ is of a form similar to $\delta \boldsymbol { p }$ We have, also,

$$
\begin{array} { r } { \tau \exp \left\{ \sqrt { - 1 } \psi \right\} = \sqrt { - 1 } \nu D u , \qquad V \exp \left\{ - \sqrt { - 1 } \psi \right\} = \sqrt { - 1 } \nu D s . } \end{array}
$$

Since

$$
\begin{array} { l } { { \displaystyle \delta \boldsymbol { \phi } = \delta { \boldsymbol { X } } \cdot \sin \psi - \delta { \boldsymbol { Y } } \cdot \cos \psi } } \\ { { \displaystyle ~ = \frac { \sqrt { - 1 } } { 2 } ( \delta \boldsymbol { u } \cdot \exp \{ - \sqrt { - 1 } \psi \} - \delta \cdot \exp \{ \sqrt { - 1 } \psi \} ) } , }  \\ { { \displaystyle \delta \sigma = \delta { \boldsymbol { X } } \cdot \cos \psi + \delta { \boldsymbol { Y } } \cdot \sin \psi } } \\ { { \displaystyle ~ = \frac { \sqrt { - 1 } } { 2 } ( \delta \boldsymbol { u } \cdot \exp \{ - \sqrt { - 1 } \psi \} + \delta \cdot \exp \{ \sqrt { - 1 } \psi \} ) } , } \end{array}
$$

we obtain

$$
\delta u = \frac { \nu D u } { V } ( \delta \phi + \sqrt { - 1 } \delta \sigma ) , \qquad \delta s = \frac { \nu D s } { V } ( \sqrt { - 1 } \delta \sigma - \delta \phi ) .
$$

Hence Su and $\delta \varsigma$ are odd functions of $\zeta$ with real coefficients, so that we can write

$$
\delta u = \zeta _ { 1 } ^ { \pm c } \zeta \cdot \sum _ { i } b _ { 2 i } \zeta ^ { 2 i } , \qquad \delta s = \zeta _ { 1 } ^ { \pm c } \zeta ^ { - 1 } \cdot \sum _ { i } b _ { 2 i } \zeta ^ { - 2 i } .
$$

The coefficients are the same for both of these series, since $\delta \boldsymbol { u } + \delta \boldsymbol { s } = 2 \delta \boldsymbol { X }$ is real.We should associate $+ c$ with $\delta \boldsymbol { u }$ and $- c$ with Ss. $( \zeta _ { 1 } / \zeta ) ^ { \pm c }$ are conjugate imaginaries with absolute value l,which have been regarded as external factors of the series with real coefficients for $\delta \pmb { \phi }$ ， $\sqrt { - 1 } \delta \sigma ,$ Su, and δs. Also, $\delta u - \delta s$ is pure imaginary. Hence the general solution of (8),differing slightly from the variational curve,can be written

$$
\begin{array} { r l } & { u = \mathbf { a } \zeta \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } \sum _ { p = 0 , \pm 1 } A _ { 2 i + p c } \zeta ^ { 2 i } \zeta _ { 1 } ^ { p c } , } \\ & { s = \mathbf { a } \zeta ^ { - 1 } \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } \sum _ { p = 0 , \pm 1 } A _ { - 2 i - p c } \zeta ^ { 2 i } \zeta _ { 1 } ^ { p c } , } \end{array}
$$

where $A _ { 2 i } = a _ { 2 i }$ of (10) as in the variational curve,and $\pmb { c }$ is a determinate function ofm and is now denoted by $c _ { 0 }$ .However, the solution in question differs by a finite amount from the variational curve. Thus this form must be regarded as merely the beginning of the full expansion.Hence the restriction on the value of $\pmb { \mathscr { p } }$ is withdrawn and the values are extended to $\pm \infty$ .The coeffcients of the first order $A _ { 2 i \pm c }$ contain a small arbitrary parameter, which we denote by ${ \bf e }$ ,and the higher coefficients $A _ { 2 i \pm p c }$ are obtained by successive approximation, so that $A _ { 2 i \pm p c }$ is of the order $| { \pmb \phi } |$ in e.The introduction of $\pmb { e }$ into the solution affects both $A _ { 2 i }$ and $\pmb { c }$ ; the $\pmb { a } _ { 2 i }$ and $c _ { 0 }$ represent only those parts that are functions of m alone, i.e., those parts that are independent of e.

It has been seen that the disturbing function is expanded in trigonometric series proceeding with cosines of multiples of the longitude difference. The true longitude is of the form $n t + \epsilon +$ periodic terms, where the periodic terms are expanded in trigonometric series with the sum of integral multiples of $\phi = n t + \epsilon - \varpi _ { : }$ $\phi ^ { \prime } = n ^ { \prime } t + \epsilon ^ { \prime } - \varpi ^ { \prime }$ ，and $\eta = n t + \epsilon - \Omega$ ，where $\eta$ is the longitude of the node counted on the orbital plane of the disturbing planet.Hence the disturbing function is expanded in a cosine series with the sum of integral multiples of $\xi = ( n - n ^ { \prime } ) t + \epsilon - \epsilon ^ { \prime } , \phi , \phi ^ { \prime }$ ,and $\eta$ ,and with power series in $m ^ { \prime } , a , a ^ { \prime } , { \tt e } ,$ $e ^ { \prime } , \gamma$ as coefficients,where $\gamma$ is the tangent of the mutual inclination of the two orbital planes. Since we have assumed that $z = e ^ { \prime } = 1 / a = 0 _ { : }$ the arguments are now $\xi$ and $\phi$ .We have thus

$$
\frac { a } { r } = \sum _ { i = - \infty } ^ { \infty } \sum _ { p = 0 } ^ { \infty } b _ { 2 i + p c } \cos { ( 2 i \xi + \rlap / p \phi ) } ,
$$

Hence,

$$
\begin{array} { r } { X = \mathbf a \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } \displaystyle \sum _ { p = - \infty } ^ { \infty } A _ { 2 i + p c } \cos { [ ( 2 i + 1 ) \xi + p \phi ] } , } \\ { Y = \mathbf a \cdot \displaystyle \sum _ { i = - \infty } ^ { \infty } \displaystyle \sum _ { p = - \infty } ^ { \infty } A _ { 2 i + p c } \sin { [ ( 2 i + 1 ) \xi + p \phi ] } ; } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle { u = { \bf a } \cdot \sum _ { i = - \infty } ^ { \infty } \sum _ { p = - \infty } ^ { \infty } A _ { 2 i + p c } \exp \left\{ \sqrt { - 1 } \left[ ( 2 i + 1 ) \xi + p \phi \right] \right\} } , } } \\ { { \displaystyle { s = { \bf a } \cdot \sum _ { i = - \infty } ^ { \infty } \sum _ { p = - \infty } ^ { \infty } A _ { - 2 i - 2 - p c } \exp \left\{ \sqrt { - 1 } \left[ ( 2 i + 1 ) \xi + p \phi \right] \right\} } } } \end{array}
$$

If we write

$$
\begin{array} { c } { \phi = \mathbf { c } n t + \epsilon - \varpi = c ( n - n ^ { \prime } ) ( t - t _ { 1 } ) , } \\ { \mathbf { c } n = c ( n - n ^ { \prime } ) , \qquad \varpi - \epsilon = c t _ { 1 } ( n - n ^ { \prime } ) , } \\ { c = \mathbf { c } ( 1 + \mathbf { m } ) , \qquad \exp { \{ ( n - n ^ { \prime } ) ( t - t _ { 1 } ) \sqrt { - 1 } \} } = \zeta _ { 1 } , } \end{array}
$$

we obtain the expansions (53) for $\pmb { u }$ and $\pmb { S } .$

If, furthermore, $t _ { 1 }$ is included in the coefficients $A$ ,then,

$$
\begin{array} { l } { { \displaystyle { u = { \bf a } \cdot \sum _ { i = - \infty } ^ { \infty } \sum _ { p = - \infty } ^ { \infty } A _ { 2 i + p c } \zeta ^ { 2 i + 1 + p c } , } } } \\ { { \displaystyle { s = { \bf a } \cdot \sum _ { i = - \infty } ^ { \infty } \sum _ { p = - \infty } ^ { \infty } A _ { - 2 i - 2 - p c } \zeta ^ { 2 i + 1 + p c } . } } } \end{array}
$$

From these we have

$$
\begin{array} { c } { { \displaystyle { D u = \mathbf { a } \cdot \sum _ { i = - \infty } ^ { \infty } \sum _ { p = - \infty } ^ { \infty } ( 2 i + 1 + p c ) A _ { 2 i + p c } \zeta ^ { 2 i + 1 + p c } , \mathrm { e t c . } _ { \star } } } } \\ { { \displaystyle { u s = \mathbf { a } ^ { 2 } \cdot \sum _ { j } \sum _ { q } \sum _ { i } \sum _ { p } ^ { } A _ { 2 i + p c } A _ { 2 i - 2 j + p c - q c } \zeta ^ { 2 j + q c } , \mathrm { e t c . } } } } \end{array}
$$

Substitute (54) in (8) and equate the coeffcients of $\zeta ^ { 2 j + q c }$ ; then we obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { i } \sum _ { p } [ ( 2 j + q c ) ^ { 2 } + ( 2 i + p c + 1 ) ( 2 i + p c - 2 j - q c + 1 ) } } \\ { { \displaystyle ~ + ~ 2 ( 4 i + 2 p c - 2 j - q c + 2 ) { \bf m } + \frac { 9 } { 2 } { \bf m } ^ { 2 } ] A _ { 2 i + p c } A _ { 2 i - 2 j + p c - q c } } } \\ { { \displaystyle ~ + ~ \frac { 9 } { 4 } { \bf m } ^ { 2 } \cdot \sum _ { i } \sum _ { p } [ A _ { 2 i + p c } A _ { 2 i - 2 i - 2 + q c - p c } + A _ { 2 i + p c } A _ { - 2 j - 2 i - 2 - q c - p c } } } \end{array}
$$

$$
2 j + q c ) \cdot \sum _ { i } \sum _ { p } ( 4 i + 2 p c - 2 j - q c + 2 + 2 { \bf m } ) A _ { 2 i + p c } A _ { 2 i - 2 j + p c - q }
$$

$$
- \frac { 3 } { 2 } { \bf m } ^ { 2 } \cdot \sum _ { i } \sum _ { p } \left[ A _ { 2 i + p c } A _ { 2 j - 2 i - 2 + q c - p c } - A _ { 2 i + p c } A _ { - 2 j - 2 i - 2 - q c - p c } \right] =
$$

except for $j = 0 = q$ ,in which case the right-hand member of the frst equation is $C / { \bf a } ^ { 2 }$

Combine these equations with (10) and (l1); the latter equations retain their form if the symbols

$$
a , \quad 2 j , \quad 2 i , \quad \sum _ { i }
$$

are replaced respectively by

$$
A , \operatorname { \rho } _ { 2 j } + q c , 2 i + p c , \sum _ { i } \sum _ { p } .
$$

Hence we can use the previous result also in the present case. Multiply the second equation of (55） by $( 2 \mathbf { m } + 1 ) / ( 2 j + q c )$ and subtract from the first.Divide the second equation by $2 ( 2 j + c )$ . A pair of the corresponding coefficients are $A _ { 2 i + p c } , A _ { - 2 i - p c }$ By an operation similar to that for the variational curve we finally obtain

$$
\begin{array} { l } { { \displaystyle \sum _ { i } \sum _ { p } \{ [ 2 j + q c , 2 i + \hbar c ] A _ { 2 i + p c } A _ { 2 i - 2 j + p c - q c } } }  \\ { { + \ [ 2 j + q c , ] A _ { 2 i + p c } A _ { 2 j - 2 i - 2 + q c - p c } } } \\ { { + \ ( 2 j + q c , ) A _ { 2 i + p c } A _ { - 2 j - 2 i - 2 - q c - p c } \} = 0 , } } \end{array}
$$

the value $j = 0 = q$ being excluded. We have

$$
[ 2 j + q c , 2 j + q c ] = - 1 , [ 2 j + q c , 0 ] = 0 .
$$

Hence the coefficient of the form $A _ { 0 } A _ { 2 i + p c }$ is -1, and that of $A _ { 0 } A _ { - 2 i - p c }$ is O. The equations for $C$ and a can be obtained similarly.

If we retain only the first power of e and neglect higher powers, then we write

$$
A _ { 2 i } = a _ { 2 i } , \qquad A _ { 2 i + c } = \epsilon _ { i } , \qquad A _ { 2 i - c } = \epsilon _ { i } ^ { \prime } ,
$$

where $\epsilon _ { i } , \epsilon _ { i } ^ { \prime }$ are of the form $\mathbf { e } f ( \mathbf { m } )$ , since the coefficients of the variational terms contain only even powers of e.In (56) the index $q$ takes the values $+ 1$ and $^ { - 1 }$ only. When $q = + 1$ ,then $\pmb { \mathscr { p } }$ has the values l, O in the frst two terms and the values $0 , - 1$ in the third term.Any other value of $\pmb { \mathscr { p } }$ gives terms of orders $\mathbf { e } ^ { 3 }$ ， $\bullet ^ { 5 }$ ，.... Similarly,when $q = - 1$ ,then $\pmb { \mathscr { p } }$ takes the values $- 1 , 0$ in the frst two terms and the values O,1 in the third term. Hence the equations for $\epsilon _ { j }$ and $\epsilon _ { j } ^ { \prime }$ are

$$
\begin{array} { l } { { \sum _ { i } ^ { > } \{ [ 2 j + c , 2 i + c ] \epsilon _ { i } a _ { 2 i - 2 j } + [ 2 j + c , 2 i ] a _ { 2 i } \epsilon _ { i - j } ^ { \prime } } } \\  { \ = \begin{array} { r l } { { \frac { 1 } { 2 } } } & { { \ } } \\ { { \frac { 1 } { 6 } } } & { { \left( { \bf 2 } j + c , { \bf 2 } i - { \bf 2 } \right) ( \epsilon _ { i } a _ { 2 j - 2 i - 2 } + { \bf \epsilon } _ { 2 i } \epsilon _ { j - i - 1 } ) } } \\ { { + \ } } & { { \left( { \bf 2 } j + c , \right) \left( a _ { 2 i } \epsilon _ { - i - j - 1 } ^ { \prime } + \epsilon _ { i } ^ { \prime } a _ { - 2 j - 2 i - 2 } \right) \} = } \end{array} } } \\ { { \sum _ { i } \{ [ 2 j - c , 2 i - c ] \epsilon _ { i } ^ { \prime } a _ { 2 i - 2 j } + \ [ 2 j - c , 2 i ] a _ { 2 i } \epsilon _ { i - j } } } \\ { { \qquad + \ [ 2 j - c , ] ( \epsilon _ { i } ^ { \prime } a _ { 2 j - 2 i - 2 } + \ a _ { 2 i } \epsilon _ { j - i - 1 } ^ { \prime } ) } } \\  { \qquad + \ \left( { \bf 2 } j - c , \right) \left( a _ { 2 i } \epsilon _ { - j - i - 1 } + \epsilon _ { i } a _ { - 2 j - 2 i - 2 } \right) \} = } \end{array}
$$

Since $j$ takes positive and negative values, these equations can be put in a more symmetrical form by combining the equations for $\epsilon _ { j }$ and $\epsilon _ { j } ^ { \prime }$ Put $- i + j$ for $_ i$ in the second term of the first equation,and $j - i - 1$

for $_ i$ in the second part of the third term, and so on. Similarly operate on the second equation. Then,

$$
\begin{array} { l } { { \sum _ { i } \{ [ 2 j + c , 2 i + c ] \epsilon _ { i } a _ { 2 i - 2 j } + [ 2 j + c , 2 j - 2 i ] \epsilon _ { - i } ^ { \prime } a _ { 2 j - 2 i } } } \\ { { \qquad + \ 2 [ 2 j + c , ] \epsilon _ { i } a _ { 2 j - 2 i - 2 } + 2 ( 2 j + c , ) \epsilon _ { - i } ^ { \prime } a _ { 2 i - 2 j - 2 } ] = 0 , } } \\ { { \sum _ { i } \{ [ - 2 j - c , - 2 i - c ] \epsilon _ { - i } ^ { \prime } a _ { 2 j - 2 i } + [ - 2 j - c , 2 i - 2 j ] \epsilon _ { i } a _ { 2 i - 2 j } } } \\ { { \qquad + \ 2 [ - 2 j - c , ] \epsilon _ { - i } ^ { \prime } a _ { 2 i - 2 j - 2 } + 2 ( - 2 j - c , ) \epsilon _ { i } a _ { 2 j - 2 i - } } } \end{array}
$$

These equations determine the ratios of the unknown coefficients to a chosen one of them, say $\epsilon _ { 0 }$ or $\epsilon _ { 0 } ^ { \prime }$ . When $\pmb { c }$ is determined, the ratios of $\epsilon _ { j } ,$ $\epsilon _ { \mathrm { } - j } ^ { \prime }$ can be calculated by successive approximation. One of them is an arbitrary constant, and this corresponds to the arbitrary constant usually denoted by $e$ in other theories.

Brown (1936) computed the principal part of the motion of the lunar perigee and node,and then he (1938) computed the term in the motion of the lunar perigee with the characteristic $e ^ { \prime 4 }$ on the basis of his new method (Section 9.16 and the end of Section 11.7).

# 11.7OTHER INEQUALITIES

The procedure described in the preceding section should be continued by successive approximations in order to obtain other inequalities corre-sponding to each term of the expansion of the disturbing function (Brown, 1894,1895,1895a,l896).The integration constant e is, however,not the same as e in Delaunay's lunar theory. We examine three cases.

I. The terms whose coefficients depend only on m and $e ^ { \prime }$ are obtained by neglecting the terms depending on the solar parallax $1 / a ^ { \prime }$ and on the latitude $z _ { \mathrm { { s } } }$ ，that is,by putting $\Omega = \Omega _ { 2 }$ ， $z = 0$ in (7)and (5).Thus we should add to the right-hand members of the equations (8) the terms

$$
- 3 \Omega _ { 2 } + D ^ { - 1 } ( D _ { t } \Omega _ { 2 } ) \qquad \mathrm { a n d } \qquad s \frac { \partial \Omega _ { 2 } } { \partial s } - u \frac { \partial \Omega _ { 2 } } { \partial u } ,
$$

respectively. Since $_ z$ is neglected, we have

$$
\Omega _ { 2 } = A u ^ { 2 } + 2 B u s + C s ^ { 2 } ,
$$

where $A , B , C$ depend only on the coordinates of the sun.Thus the terms to be added to (8) are

$$
- 3 ( A u ^ { 2 } + 2 B u s + C s ^ { 2 } ) + D ^ { - 1 } ( u ^ { 2 } D A + 2 u s D B + s ^ { 2 } D C )
$$

and

$$
2 C s ^ { 2 } - 2 A u ^ { 2 } .
$$

Now

$$
\Omega _ { 2 } = 3 { \bf m } ^ { 2 } \Big [ \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } r ^ { 2 } S ^ { 2 } - \frac { 1 } { 4 } ( u + s ) ^ { 2 } \Big ] - { \bf m } ^ { 2 } u s \Big ( \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } - 1 \Big ) ,
$$

where

$$
= { \frac { 1 } { 2 } } \left( u + s \right) \cos \left( v ^ { \prime } - n ^ { \prime } t - \epsilon ^ { \prime } \right) - { \frac { \sqrt { - 1 } } { 2 } } \left( u - s \right) \sin \left( v ^ { \prime } - n ^ { \prime } t - \epsilon ^ { \prime } \right)
$$

After computation (Brown, 1896) we obtain

$$
A = \frac { 3 } { 4 } { \bf m } ^ { 2 } \Big [ \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } \exp \left\{ - 2 V ^ { \prime } \sqrt { - 1 } \right\} - 1 \Big ] , \qquad B = \frac { 1 } { 4 } { \bf m } ^ { 2 } \Big ( \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } - 1 \Big ) ,
$$

$$
C = \frac { 3 } { 4 } { \bf m } ^ { 2 } \biggl [ \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } \exp { \{ 2 V ^ { \prime } \sqrt { - 1 } \} } - 1 \biggr ] ,
$$

where

$$
V ^ { \prime } = v ^ { \prime } - n ^ { \prime } t - \epsilon ^ { \prime } = ( v ^ { \prime } - \varpi ^ { \prime } ) - ( n ^ { \prime } t + \epsilon ^ { \prime } - \varpi ^ { \prime } ) = f ^ { \prime } - w ^ { \prime } .
$$

Put

$$
\frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } - 1 = \sum _ { p } \alpha _ { p } ^ { \prime } \cos { p w ^ { \prime } } ,
$$$$
\begin{array} { r l } { { \displaystyle \qquad \frac { 1 } { r ^ { \prime 3 } } - 1 = \sum _ { p } \alpha _ { p } \cos p w , } } & { { } } \\ { { } } & { { } } \\ { { \displaystyle \frac { a ^ { \prime 3 } } { r ^ { \prime 3 } } \cos 2 V ^ { \prime } - 1 = \sum _ { p } \beta _ { p } ^ { \prime } \cos p w ^ { \prime } , \qquad \alpha _ { - p } ^ { \prime } = \alpha _ { p } ^ { \prime } , } } & { { } } \\ { { \displaystyle \qquad \frac { \alpha ^ { \prime 3 } } { r ^ { \prime 3 } } \sin 2 V ^ { \prime } = \sum _ { p } \beta _ { p } ^ { \prime } \sin p w ^ { \prime } \qquad ( \not p = - \infty , \cdot \cdot , + \infty ) } } & { { } } \end{array}
$$

where $\alpha _ { p } ^ { \prime } , \beta _ { p } ^ { \prime }$ are known functions of $e ^ { \prime }$ . Then we obtain

$$
\begin{array} { l } { { \displaystyle { \cal A } = \frac { 3 } { 4 } { \bf m } ^ { 2 } \cdot \sum _ { p } \beta _ { p } ^ { \prime } \exp { \{ - \sqrt { - 1 } \ p w ^ { \prime } \} } , } } \\ { { \displaystyle { \cal B } = \frac { 1 } { 4 } { \bf m } ^ { 2 } \cdot \sum _ { p } \alpha _ { p } ^ { \prime } \exp { \{ \sqrt { - 1 } \ p w ^ { \prime } \} } , } } \\ { { \displaystyle { \cal C } = \frac { 3 } { 4 } { \bf m } ^ { 2 } \cdot \sum _ { p } \beta _ { p } ^ { \prime } \exp { \{ \sqrt { - 1 } \ p w ^ { \prime } \} } . } } \end{array}
$$

Since the coefficients of $t$ in $\zeta ^ { m }$ and exp $\{ \sqrt { - 1 } w ^ { \prime } \}$ are the same, we can put $\zeta ^ { m }$ for exp $\{ \sqrt { - 1 } w ^ { \prime } \}$ ,by remembering that exp $\{ \sqrt { - 1 } \ p w ^ { \prime } \}$ replaces $\zeta ^ { p m }$ when we return to real variables. The value of $\mathbf { m }$ is not substituted in the index of $\zeta$ Hence

$$
A = \frac { 3 } { 4 } { \bf m } ^ { 2 } \cdot \sum _ { p } \beta _ { - p } ^ { \prime } \zeta ^ { p m } , \qquad B = \frac { 1 } { 4 } { \bf m } ^ { 2 } \cdot \sum _ { p } \alpha _ { p } ^ { \prime } \zeta ^ { p m } ,
$$

$$
C = \frac { 3 } { 4 } \mathbf { m } ^ { 2 } \cdot \sum _ { p } \beta _ { p } ^ { \prime } \zeta ^ { p m } .
$$

After we substitute these expressions in the right-hand members of (8), the required solution should take the form

$$
u = \mathbf { a } A _ { 2 i + p m } \zeta ^ { 2 i + 1 + p m } , \qquad s = \mathbf { a } A _ { - 2 i - 2 - p m } \zeta ^ { 2 i + 1 + p m } ,
$$

where e is neglected.We substitute these expansions in the equations and equate the coefficients of $\zeta ^ { 2 j + q m }$ ; then we obtain a series of equations for determining the unknown coefficients. This procedure is quite similar to that described in Section 11.6.

II. The terms whose coefficients depend only on m and $1 / a ^ { \prime }$ are obtained by neglecting $e ^ { \prime }$ (parallactic inequalities),so that

$$
\Omega _ { 2 } = 0 , ~ D _ { t } \Omega = 0 .
$$

The terms to be added to the right-hand members of(8) are,respectively,

$$
- \sum _ { p = 3 } ^ { \infty } ( \rho + 1 ) \Omega _ { p } , \qquad s \frac { \partial \Omega } { \partial s } - u \frac { \partial \Omega } { \partial u } \cdot
$$

After computation (Brown,l896) we find

$$
\begin{array} { l } { { \displaystyle \Omega = \frac { { \bf m } ^ { 2 } } { a ^ { \prime } } \left[ \frac { 5 } { 8 } ( u ^ { 3 } + s ^ { 3 } ) + \frac { 3 } { 8 } u s ( u + s ) \right] } } \\ { { \displaystyle \qquad + \frac { { \bf m } ^ { 2 } } { a ^ { \prime 2 } } \left[ \frac { 3 5 } { 6 4 } ( u ^ { 4 } + s ^ { 4 } ) + \frac { 5 } { 1 6 } u s ( u ^ { 2 } + s ^ { 2 } ) + \frac { 9 } { 3 2 } u ^ { 2 } s ^ { 2 } \right] } } \\ { { \displaystyle \qquad + \cdot \cdot \cdot . } } \end{array}
$$

The terms to be added are those of the third and higher degrees in u and $s _ { \scriptscriptstyle \mathrm { : } }$ ，corresponding to terms of the first and higher degrees with respect to $1 / a ^ { \prime }$ . If, in the added terms, the values of $u _ { 0 } , \ s _ { 0 } ,$ which are odd power series in $\zeta$ and correspond to the intermediary orbit,are substituted for $u , s ,$ then the terms produced by $\Omega _ { p }$ should be odd or even power series in $\zeta$ according as $\pmb { \mathscr { p } }$ is odd or even.Hence,when terms dependent on the solar parallax are included, the values of $\pmb { u }$ and $\pmb { \mathscr { s } }$ should contain even as well as odd powers of $\zeta .$ ，Thus we assume

$$
u = { \bf a } \cdot \sum _ { i } A _ { i - 1 } \zeta ^ { i } , \qquad s = { \bf a } \cdot \sum _ { i } A _ { - i - 1 } \zeta ^ { i } .
$$

This solution includes the intermediary orbit. When $1 / a ^ { \prime }$ is neglected, we have $A _ { 2 i } = a _ { 2 i }$ and $A _ { 2 i - 1 } = 0$ . The procedure is similar to that in (I) (Brown,1892,1892a).

II. The terms whose coeffcients depend only on m and $\gamma$ can be obtained by neglecting $e ^ { \prime }$ and $1 / a ^ { \prime }$ ，so that $\Omega = 0$ The equations (7), (5), (4) become,respectively,

$$
\begin{array} { r } { D ^ { 2 } ( u s + z ^ { 2 } ) - D u D s - ( D z ) ^ { 2 } - 2 \mathbf { m } ( u D s - s D u ) \qquad } \\ { + \frac { 9 } { 4 } \mathbf { m } ^ { 2 } ( u + s ) ^ { 2 } - 3 \mathbf { m } ^ { 2 } z ^ { 2 } = C , } \\ { D ( u D s - s D u - 2 \mathbf { m } u s ) + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } ( u ^ { 2 } - s ^ { 2 } ) = 0 , } \\ { D ^ { 2 } z - z \Big ( \mathbf { m } ^ { 2 } + \frac { \kappa } { r ^ { 3 } } \Big ) = 0 . } \end{array}
$$

It can be seen that the solution of the third equation contains a small constant factor which is denoted by $\gamma .$ . If terms of order $\gamma ^ { 2 }$ are neglected in the frst two equations, then they reduce to (8). The new parts are factored by $\gamma ^ { 2 }$ at least.We neglect the eccentricity constant e and con-sider the first approximation to (57) to be the intermediary. The procedure for the solution is similar to the above.

We suppose that the intermediary orbit is known and consider the first power of $\gamma$ 、Substitute the value of $_ r$ corresponding to the intermediary orbit in the third equation of (57)； then we see that only the terms whose coefficients are of the order $\gamma ^ { 2 }$ occur in $\boldsymbol { \mathscr { u } }$ and s. Hence they are obtained from the first two equations of (57) when the coefficients of the order $\gamma$ are known. Thus the solution is written

$$
\begin{array} { c } { { u = u _ { 0 } + u _ { 2 } \gamma ^ { 2 } + \cdot \cdot \cdot , \qquad s = s _ { 0 } + s _ { 2 } \gamma ^ { 2 } + \cdot \cdot \cdot , } } \\ { { z = z _ { 1 } \gamma + z _ { 3 } \gamma ^ { 3 } + \cdot \cdot \cdot . } } \end{array}
$$

To the third power of $\gamma$ we find, by remembering that $r ^ { 2 } = u s + z ^ { 2 }$ ， $\begin{array} { r } { r _ { 0 } ^ { 2 } = u _ { 0 } s _ { 0 } , } \end{array}$ where $r _ { 0 } , u _ { 0 } , s _ { 0 }$ are the values for the intermediary orbit,

$$
\begin{array} { r l r } & { } & { \frac { 1 } { r ^ { 3 } } = [ ( u _ { 0 } + \gamma ^ { 2 } u _ { 2 } ) ( s _ { 0 } + \gamma ^ { 2 } s _ { 2 } ) + \gamma ^ { 2 } z _ { 1 } ^ { 2 } ] ^ { - 3 / 2 } } \\ & { } & \\ & { } & { \qquad = \frac { 1 } { r _ { 0 } ^ { 3 } } \left[ 1 - \frac { 3 } { 2 } \frac { u _ { 0 } \gamma ^ { 2 } s _ { 2 } + s _ { 0 } \gamma ^ { 2 } u _ { 2 } + \gamma ^ { 2 } z _ { 1 } ^ { 2 } } { r _ { 0 } ^ { 2 } } \right] . } \end{array}
$$

Thus the third equation of (57) becomes

$$
\begin{array} { r l r } {  { \gamma z _ { 1 } + \gamma ^ { 3 } z _ { 3 } ) - ( \mathbf { m } ^ { 2 } + \frac { \kappa } { r _ { 0 } ^ { 3 } } ) ( \gamma z _ { 1 } + \gamma ^ { 3 } z _ { 3 } ) } } \\ & { } & \\ & { } & { \qquad = - \frac { 3 } { 2 } \frac { \kappa \gamma Z _ { 1 } } { r _ { 0 } ^ { 5 } } ( u _ { 0 } \gamma ^ { 2 } s _ { 2 } + s _ { 0 } \gamma ^ { 2 } u _ { 2 } + \gamma ^ { 2 } z _ { 1 } ^ { 2 } ) } \end{array}
$$

We may derive directly from (3) and (4) the equations free from $\gamma ^ { 3 }$ ， such as

$$
\begin{array} { r } { D ( z D u - u D z ) + 2 \mathbf { m } z D u + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } z ( u + s ) + \mathbf { m } ^ { 2 } z u = 0 , } \\ { D ( z D s - s D z ) - 2 \mathbf { m } z D s + \frac { 3 } { 2 } \mathbf { m } ^ { 2 } z ( u + s ) + \mathbf { m } ^ { 2 } z s = 0 . } \end{array}
$$

These equations are convenient for literal solution in powers of m.

If we retain only the frst power of $\gamma _ { : }$ ,then we find

$$
\begin{array} { r } { D ^ { 2 } z _ { 1 } - \Big ( \mathbf { m } ^ { 2 } + \frac { \kappa } { r _ { 0 } ^ { 3 } } \Big ) z _ { 1 } = 0 . } \end{array}
$$

Write

$$
{ { \bf m } ^ { 2 } } + \frac { \kappa } { r _ { 0 } ^ { 3 } } = 2 \cdot \sum _ { i } M _ { i } \zeta ^ { i } , \qquad M _ { - i } = M _ { i } \qquad ( i = - \infty , . . . , + \infty ) ;
$$

then,

$$
D ^ { 2 } z _ { 1 } - 2 z _ { 1 } \cdot \sum _ { i } M _ { i } \zeta ^ { 2 i } = 0 ,
$$

where $M _ { i }$ is of the order $\mathbf { m } ^ { | 2 i | }$ at least. This equation is again Hill's equation. The root of the infinite determinant is denoted by g.

Put

$$
\begin{array} { r l r } {  { \zeta ^ { 2 j } = \exp { \{ 2 j ( n - n ^ { \prime } ) ( t - t _ { 0 } ) \sqrt { - 1 } \} } , } } \\ & { } & { \bf { g } = { g n } / ( n - n ^ { \prime } ) = { g ( 1 + m ) } , \qquad g } t _ { 2 } ( n - n ^ { \prime } ) = \theta - \epsilon ,  \\ & { } & { \zeta _ { 2 } ^ { e } = \exp { \{ \sqrt { - 1 } \eta \} } = \exp { \{ ( g n t + \epsilon - \theta ) \sqrt { - 1 } \} } } \\ & { } & { = \exp { \{ \bf g } ( n - n ^ { \prime } ) ( t - t _ { 2 } ) \sqrt { - 1 } \} ; } \end{array}
$$

then the solution is writen

$$
z = 2 \mathbf { a } \cdot \sum _ { j } K _ { j } \sin { ( 2 j \xi + \eta ) } \qquad ( j = - \infty , \cdot \cdot , + \infty ) ,
$$

or

$$
z { \sqrt { - 1 } } = { \bf a } \cdot \sum _ { j } { \textstyle \left( K _ { j } \zeta ^ { 2 j + g } + K _ { - j } ^ { \prime } \zeta ^ { - 2 j - g } \right) } , \qquad K _ { - j } ^ { \prime } = - K _ { j } .
$$

Substitute this in (54); then, from the coefficients of $\zeta ^ { 2 j + \tt g }$ ,we obtain

$$
( 2 j + 9 ) ^ { 2 } K _ { j } - 2 \sum _ { i } M _ { j - i } K _ { i } = 0 ( i , j = - \infty , . . . , + \infty ) .
$$

Eliminating $K _ { j }$ from these equations,we find an infinite determinant $\Delta ( { \bf g } )$ . The roots of $\Delta ( \pmb { \mathsf { g } } ) = 0$ are represented,similarly to (55) in the case of the perigee motion, by

$$
\sin ^ { 2 } \frac { \pi } { 2 } \mathbf { g } = \Delta ( 0 ) \sin ^ { 2 } \frac { \pi } { 2 } \sqrt { 2 M _ { 0 } } ,
$$

where $\Delta ( 0 )$ denotes the determinant (55) of Section l1.6, in which $\Theta _ { j }$ are replaced by $M _ { j }$ and $\pmb { c }$ by $\pmb { \mathrm { g } }$

When $\pmb { \mathrm { g } }$ is found, the coefficients $K _ { j } , \ j = 0$ being excluded,are determined in terms of $K _ { \mathfrak { o } }$ from (59). We obtain $2 \gamma = 2 \mathbf { a } K$ This method of solution is due to Adams (1877),and was completed by Cowell (1896).

If we include higher-degree terms with respect to $\gamma _ { : }$ , then the value of $\pmb { \mathrm { g } }$ should be modified.

The equation (58) is a linear differential equation with periodic coefficients.Levi-Civita (l9ll） posed the problem of whether there exists the mean motion in the motion of the lunar node,and Levi (1911) and Trevisani (l9l2) discussed the problem.The question is concerned with the existence of mean motion, which will be discussed in Chapter 27 in connection with almost periodic motions.

Thus the coefficients of the terms of any order in $\mathbf { e } , e ^ { \prime } , \gamma , 1 / a ^ { \prime }$ are determined by a set of linear equations when the terms of lower order have been found.At each stage all powers of m are included.Brown worked out the theory of the motion of the moon (1899,1904,1905, 1905a,l908)and compiled the Tables of the Motion of the Moon (1919, 1915a)，which are now in full use for predicting the moon's position. Brown took three arbitrary constants $t _ { 0 } , t _ { 1 } , t _ { 2 } ,$ and three out of the four arbitrary constants $n , \mathbf { a } , \mathbf { e } , \mathbf { k }$ where $\mathbf { \delta k }$ denotes the constant of inclination. The expansion is made in powers of $\mathbf { m } , \ \mathbf { e } , \ e ^ { \prime } , \ \mathbf { k } ;$ and $\alpha = \ a / a ^ { \prime }$ . The general term is of the form

$$
\mathbf { a } { \left[ \begin{array} { l } { } \end{array} \right] } \mathbf { e } ^ { p + 2 p ^ { \prime } } e ^ { \prime \tau + 2 r ^ { \prime } } \mathbf { k } ^ { q + 2 q ^ { \prime } } \alpha ^ { s ^ { \prime } } \zeta ^ { 2 i \pm p c \pm r m \pm q g } .
$$

The coefficients ${ \bf e } ^ { p + 2 p ^ { \prime } } e ^ { \prime \tau + 2 r ^ { \prime } } { \bf k } ^ { q + 2 q ^ { \prime } } \alpha ^ { s ^ { \prime } }$ are called the characteristics. The sum of the exponents of these coefficients is called the order of the term.

Poincaré （l900, l909） considered canonical transformation of the equations of motion.

A series of important works on the lunar theory is being continued by Eckert and his colleagues. Because ofits high quality and long acceptance as the standard of comparison, Brown's lunar theory will, for years to come, play a key role in the discussion of the observed lunar motion and in the critical examination of new and more precise theoretical developments.In the earlier modifications of Brown's basic solution to facilitate the comparison with observations, the full precision of the solution was not preserved since this was not at first considered necessary. Some of the precision was regained by the Improved Lunar Ephemeris of l952-1959 published by Eckert, Jones,and Clark (l954).This has been compared with observations by Klock and Scott (1965).Eckert (l964) and Eckert and Smith (l966,1966a) were still continuing to work on Brown's lunar theory by extremely elaborate calculation and checking the coefficients of various terms up to higher orders of precision. Eckert, Walker, and Eckert (l966) have made the full accuracy of Brown's solution available for the comparison with observations and for increasing the precision of the relation between the computed coordinates and the parameters on which they are based.The precision of the solar terms in the sine of the parallax has been improved by more than one order of magnitude.

Eckert and Eckert (1967) considered the use of the Hill-Brown method for obtaining the increased precision now required in the lunar theory. They included the effects of the forces containing the ratio of the mass of the earth-moon system to that of the sun, i.e., $( m _ { E } + m _ { M } ) / m ^ { \prime }$ ，which were neglected by Hill, and the higher-order terms depending on the ratio of the mass of the moon to that of the earth,which were neglected by Brown.The variational orbit and the principal parts of the motions of the perigee and node for various values of m and $( m _ { E } + m _ { M } ) / m ^ { \prime }$ are given with the accuracy of 18 decimal places.

Recently Eckert (l965) found a large concentration of mass near the surface of the moon by comparing the observed values of the motions of the lunar perigee and node with his newly calculated values on the basis of the mechanical ellipticity of the earth as determined by artificial earth satellites.This settled a long-cherished problem on the concentration of mass inside the moon. The motions of the lunar perigee and node are,besides other causes,affected by the radial distribution of mass through the parameters

$$
g ^ { \prime } = { \frac { 3 C ^ { \prime } } { 2 M b ^ { \prime 2 } } } , ~ f = { \frac { C ^ { \prime } - B ^ { \prime } } { C ^ { \prime } - A ^ { \prime } } } ,
$$

where $C ^ { \prime }$ is the moment of inertia around the polar axis of the moon, $A ^ { \prime } , B ^ { \prime }$ are the other components of the moments of inertia,and ${ \pmb b } ^ { \prime }$ is the equatorial radius of the moon; whence $g ^ { \prime } = 0 . 6$ for a homogeneous sphere and $g ^ { \prime } = 1 . 0 0$ for a hollow spherical shell. Observations showed that $g ^ { \prime }$ is nearly equal to 1.Brown (1915a),for his Tables of the Motion of the Moon of 1919,assumed $g ^ { \prime } = 0 . 5 0 2$ ，similarly to the earth.In consequence of this assumption the ellipticity of the earth became of a large value, 1/294,while Heyford's accepted value is 1/297. Spencer Jones （1932） obtained $g ^ { \prime } = 0 . 8 7$ from the ellipticity 1/297. By adopting the ellipticity $1 / 2 9 8 . 2 5 $ determined from the satellite observations we obtain $g ^ { \prime } = 1 . 0 5 , f = 0 . 6 3 8$ if the residuals of the motion of the perigee and node $d \pi = - 3 . 7$ ， $d \Omega = - 2 7 . 9$ are attributed to the mass distribution inside the moon.

# 11.8CONVERGENCE OF HILL'S SERIES

Wintner (1925,l929),by neglecting the eccentricities and the solar parallax,proved the convergence of Hill's series for his intermediary orbit.Hill determined the variation from the intermediary orbit and hence the motion of the lunar perigee (Section l1.6).Wintner (1937) gave the mathematical proof for the convergence of the series on the basis of almost periodic functions (Sections 2.1l-2.13). It is known according to Bohr (1930) that,if $\zeta ( t )$ is a complex-valued almost periodic function of a real variable $t ,$ and $| \zeta ( t ) | < \alpha$ holds for a constant $\alpha > 0$ and for every $t .$ ,then the real continuous function arg $\zeta ( t )$ can be decomposed into a sum of a linear secular term $\mu t$ and a recurrent term which is almost periodic, while $\mu$ is a constant (Sections 14.22, 27.l,and 27.9).

The equations of motion of Hill

$$
\frac { d ^ { 2 } X } { d t ^ { 2 } } \stackrel { \bullet } { - } 2 \frac { d Y } { d t } = \frac { \partial \Omega } { \partial X } , \frac { d ^ { 2 } Y } { d t ^ { 2 } } + 2 \frac { d X } { d t } = \frac { \partial \Omega } { \partial Y } ,
$$

are satisfied,according to ll, by

$$
X = \sum _ { k = - \infty } ^ { \infty } a _ { k } \cos { ( 2 k + 1 ) } \xi , \qquad Y = \sum _ { k = - \infty } ^ { \infty } a _ { k } \sin { ( 2 k + 1 ) } \xi ,
$$

where the Fourier coefficients $a _ { k } ( \mathbf { m } )$ are analytic functions of $\mathbf { m }$ and vanish at $\mathbf { m } = 0$ with increasing rapidity as $k  \pm \infty$ .This procedure of Hill was justified by Wintner (1925,1929） for $| \mathbf { m } | < 0 . 0 8 3 3 3 \ldots$ by Petrovskaya (1959） for $| \mathbf { m } | < 0 . 2 1 \ldots$ ，and by Riabov（1962） for $| { \bf m } | < 0 . 2 5 8$ (Section 11.4). The convergence of the variation from Hil's intermediary orbit is justified for all values of $\mathbf { m }$ ,since the problem is linear, except for the points on the zero-velocity curve, because the equation for the normal displacement has singularities there.The actual case of this exception occurs only for the cuspidal orbit of maximum lunation (Section 11.3).

Write $X = X ^ { ( 0 ) } + v , ~ Y = Y ^ { ( 0 ) } + w ,$ The variational equations become

$$
\begin{array} { r l } & { \cfrac { d ^ { 2 } v } { d t ^ { 2 } } - 2 \cfrac { d w } { d t } = \cfrac { \hat { \partial } ^ { 2 } } { \partial X ^ { ( 0 ) 2 } } \Omega ( t ; \mathbf { m } ) \cdot v + \cfrac { \hat { \partial } ^ { 2 } } { \partial X ^ { ( 0 ) } \partial Y ^ { ( 0 ) } } \Omega ( t ; \mathbf { m } ) \cdot w , } \\ & { \cfrac { d ^ { 2 } w } { d t ^ { 2 } } + 2 \cfrac { d v } { d t } = \cfrac { \hat { \partial } ^ { 2 } } { \partial X ^ { ( 0 ) } \partial Y ^ { ( 0 ) } } \Omega ( t ; \mathbf { m } ) \cdot v + \cfrac { \hat { \partial } ^ { 2 } } { \partial Y ^ { ( 0 ) 2 } } \Omega ( t ; \mathbf { m } ) \cdot w . } \end{array}
$$

There are four linearly independent solutions, of which two are trivial and the other two represent the general solution for the normal displacements.The trivial solutions correspond to the solutions with zero characteristic exponents (see Sections 19.1-19.5).The solutions for $X$ and $\pmb { Y }$ mentioned above are symmetric with respect to the $X \mathrm { - }$ and the $\pmb { Y } .$ -axes. If $\pmb { c }$ and $- \pmb { c }$ are the pair of the nontrivial characteristic exponents, that is, if $2 \pi c$ is the period of the motion of the perigee, then the two nontrivial solutions for these variational equations are

$$
{ \begin{array} { r l } & { v ( t ; \mathbf { m } ) = \gamma \cdot \displaystyle \sum _ { k = - \infty } ^ { \infty } A _ { k } \cos { [ ( 2 k + 1 + c ) \xi + \delta ] } , } \\ & { w ( t ; \mathbf { m } ) = \gamma \cdot \displaystyle \sum _ { k = - \infty } ^ { \infty } B _ { k } \sin { [ ( 2 k + 1 + c ) \xi + \delta ] } \quad \quad ( \gamma \neq 0 ) , } \end{array} }
$$

δ being an arbitrary constant, and $\pmb { c }$ $A _ { k } , B _ { k } ,$ analytic functions of m.

As $\mathbf { m } \to 0 _ { \cdot }$ ，the coefficients $A _ { k } ( \mathbf { m } )$ and $B _ { \kappa } ( \mathbf { m } )$ behave similarly to $a _ { k } ( \mathbf { m } )$ in the expression for $X$ for a large value of $| k |$ . The limiting values $\left( A _ { k } \right) _ { \mathbf { m } = 0 }$ and $( B _ { k } ) _ { \bf m = 0 }$ vanish unless $| 2 k + 1 | = 1$ .If $| 2 k + 1 | = 1$ ，so that $k = 1$ or $k = - 1$ , then

$$
\begin{array} { c c } { { ( A _ { 0 } ) _ { \bf m = 0 } \ne 0 , } } & { { ( B _ { 0 } ) _ { \bf m = 0 } = ( A _ { 0 } ) _ { \bf m = 0 } , } } \\ { { ( A _ { - 1 } ) _ { \bf m = 0 } = - 3 ( A _ { 0 } ) _ { \bf m = 0 } , } } & { { ( B _ { - 1 } ) _ { \bf m = 0 } = 3 ( B _ { 0 } ) _ { \bf m = 0 } . } } \end{array}
$$

Thus the expressions for $v ( t ; \mathbf { m } )$ and $w ( t ; \mathbf { m } )$ become,by omitting the nonzero constant factor ${ \pmb \gamma }$ ，

$$
\begin{array} { r l r } & { } & { [ v ( t ; \mathbf { m } ) ] _ { \mathbf { m } = 0 } = - \cos \xi \cos [ ( c ) _ { \mathbf { m } = 0 } \xi + \delta ] - 2 \sin \xi \sin [ ( c ) _ { \mathbf { m } = 0 } \xi + } \\ & { } & { ( } \\ & { w ( t ; \mathbf { m } ) ] _ { \mathbf { m } = 0 } = - \sin \xi \cos [ ( c ) _ { \mathbf { m } = 0 } \xi + \delta ] + 2 \cos \xi \sin [ ( c ) _ { \mathbf { m } = 0 } \xi + } \end{array}
$$

Hence,

$$
\begin{array} { r l r } {  { [ { \boldsymbol v } ^ { 2 } ( t ; { \mathbf m } ) + { \boldsymbol w } ^ { 2 } ( t ; { \mathbf m } ) ] _ { { \mathbf m } = { \boldsymbol 0 } } } } \\ & { } & { = \cos ^ { 2 } \big [ \big ( c \big ) _ { { \mathbf m } = { \boldsymbol 0 } } \xi + \mathfrak { s } \big ] + 4 \sin ^ { 2 } \big [ ( c ) _ { { \mathbf m } = { \boldsymbol 0 } } \xi + \mathfrak { s } \big ] . } \end{array}
$$

Since this continuous and nonvanishing functin of $\xi$ is periodic, there exists a sufficiently small constant $\alpha _ { 0 }$ which depends on the integration constant δ and $\gamma \neq 0$ but is such that

$$
[ v ^ { 2 } ( t ; { \bf m } ) + w ^ { 2 } ( t ; { \bf m } ) ] _ { { \bf m } = 0 } > \alpha _ { 0 } > 0 ( - \infty < \xi < + \infty ) .
$$

Hence, for a sufficiently small value of $\mathbf { m } ^ { * } > 0$ such that

$$
- \mathbf { m } ^ { * } < \mathbf { m } < \mathbf { \tau } + \mathbf { m } ^ { * } ,
$$

we can choose a positive constant $\alpha = \alpha _ { \mathrm { m } }$ for which the almost periodic functions $v ( t ; \mathbf { m } )$ and $w ( t ; \mathbf { m } )$ of $\xi$ .or of $t = \mathbf { m } \xi$ satisfy

$$
[ v ( t ; \mathbf { m } ) ] ^ { 2 } + [ w ( t ; \mathbf { m } ) ] ^ { 2 } > \alpha _ { \mathbf { m } } > 0 \qquad ( - \infty < t < + \infty ) ,
$$

where $\alpha _ { \mathbf { m } }$ is supposed to be a function of the integration constants $\gamma$ and δ for a fixed value of $\mathbf { m }$ ,but $\mathbf { m } ^ { * }$ is independent of $\gamma$ and 8.

Now we introduce $\varpi = \varpi ( t )$ as a function of $t$ or $\xi$ by

$$
v ( t ; \mathbf { m } ) = \rho \cos \varpi , \qquad w ( t ; \mathbf { m } ) = \rho \sin \varpi ;
$$

then $\varpi = \varpi ( t )$ is determined for every $t$ by continuity, if an initial normalizing condition $0 \leq \varpi ( 0 ) < 2 \pi$ is assigned. Put

$$
z ( t ) = v + { \sqrt { - 1 } } w = ( v ^ { 2 } + w ^ { 2 } ) ^ { 1 / 2 } \exp { \{ \sqrt { - 1 } } \varpi \} .
$$

Then $z ( t )$ is an almost periodic function (Section 2.12). Furthermore, we have seen that $| z ( t ) | > \alpha _ { \mathbf { m } } ^ { 1 / 2 } > 0$ for every $t .$ Hence Bohr's theorem (1930; Section 27.7) can be applied to $\begin{array} { r } { z ( t ) = | z | \exp { \{ \sqrt { - 1 } \varpi \} } . } \end{array}$ where ${ \pmb { \varpi } } ( t )$ should be of the form

$$
\begin{array} { c } { { \pmb { \sigma } ( t ) = \mu t + \mathrm { a n ~ a l m o s t ~ p e r i o d i c ~ f u n c t i o n ~ o f ~ } t , } } \\ { { \pmb { \mu } = \mathrm { c o n s t a n t . } } } \end{array}
$$

From the definition we see that

$$
{ \pmb { \varpi } } ^ { \prime } \equiv { \frac { d { \pmb { \varpi } } } { d t } } = { \frac { v \dot { v } - w \dot { v } } { v ^ { 2 } + w ^ { 2 } } }
$$

is an almost periodic function. Since the integral of an almost periodic function is almost periodic if it is bounded (Section 2.l2),this expression (63) for ${ \boldsymbol { \varpi } } ( t )$ can be infered from the latter expression (64) for ${ \pmb { \varpi } } ^ { \prime }$ by integration, if and only if $\varpi ( t ) \ : - \ : \mu t$ is bounded, where $\pmb { \mu }$ denotes the constant term in the Fourier series of the almost periodic function $\scriptstyle { \overline { { \pmb { \varpi } } } } ^ { \prime }$ ， such that

$$
\mu = \operatorname* { l i m } _ { T \to \infty } \frac { 1 } { T } \int _ { 0 } ^ { T } \varpi ^ { \prime } ( t ) \ d t .
$$

On the other hand, the integral of an almost periodic function that has no constant term in its Fourier expansion is, according to Favard (1932; Section l4.25), almost periodic if there is no arbitrary smallfrequency, that is, if there is no small divisor. Otherwise nothing can be said about the almost periodicity,as is known by classical perturbation theory.Thus the expressions (6l)， (64) and the inequality (62) show that the frequencies of the almost periodic function $\varpi ^ { \prime } ( \mathbf { m } \xi )$ or $\varpi ^ { \prime } ( \mathbf { m } \xi ) - \mu$ are contained in the double sequence

$$
\nu _ { 1 } c + \nu _ { 2 } \qquad ( \nu _ { 1 } , \nu _ { 2 } = 0 , \pm 1 , \pm 2 , . . . ) .
$$

Since $c = c ( \mathbf { m } )$ is a continuous and nonconstant function of $\mathbf { m }$ ,and can be supposed to be irrational, this double sequence is identical with small divisors in classical perturbation theory.All frequencies of the almost periodic function $\varpi ^ { \prime } ( \mathbf { m } \xi )$ are contained in this double sequence.Hence the Fourier series of the almost periodic function of the right-hand member of (63) is of the form

$$
\varpi ( t ) \mathrm { ~ - ~ } \mu t \approx \sum _ { j = - \infty } ^ { \infty } \sum _ { k = - \infty } ^ { \infty } C _ { j k } \cos \left[ \frac { c ( \mathbf { m } ) j + k } { \mathbf { m } } t + \delta _ { j k } \right] .
$$

We have

$$
\mu = \frac { c r + s } { \bf m } , \qquad c = c ( \bf m ) ,
$$

where $r$ and $\pmb { \mathscr { s } }$ are integers. This agrees with Bohr's theorem (1932) on an almost periodic motion, as will be described in Chapter 27 (see also Section 2.12).

Hill considered only the secular part $\mu$ of the motion of the perigee and put $\varpi ( t ) = \mu t$ ， $\varpi ^ { \prime } ( t ) = \mu$ . This assumption of Hill is now justified by the relation (65),although Hill has not written the periodic part in the form of (65).The mathematical postulates of the lunar theory of Hill and Brown,in which higher powers of the eccentricities and inclination are taken into account, should be studied by an entirely different approach.

# THE PLANETARY ACTIONS

# 11.9ACTION DUE TO PLANETS

The effect of any disturbing cause on the motion of the moon can be studied by inserting the appropriate additional periodic and constant terms in the disturbing function.The planetary action was studied by

Hansen (l862,l864). The period and the coeffcients of such terms in the disturbing function can be determined with sufficient accuracy for practical purposes; thus,Hill's method (1883,1885,1886a)ofintegration for the lunar inequalities due to Jupiter, founded on Delaunay's formulas (1867)，is recommended.The coefficients of the inserted terms are generally small, and it is scarcely necessary to consider the changes produced in the inserted terms due to those changes of the elements which occur when any one of the original or the inserted periodic terms is eliminated by Delaunay's procedures. The operations are similar to those described in Section 9.1, but the operations can be abridged owing to the circumstance that the numerical values of the moon's orbit can be used. The numerical procedure was given by Radau (1892,1895) by modifying Hill's method.

We suppose that the periodic terms arising only from the action of the sun, supposed to be moving in an elliptic orbit, have been eliminated, and that the disturbing function contains only the remaining constant portion together with the inserted periodic term in question.

Let $x ^ { \prime } , y ^ { \prime } , z ^ { \prime } , r ^ { \prime }$ be the coordinates of the sun, $x , y , z , r$ those of the moon,referred to the axes fixed in direction and passing through the earth, and let $S$ be the cosine of the angle between the vectors $r$ and $\scriptstyle { \pmb { r } } ^ { \prime }$ The disturbing function due to the sun for the motion of the moon is

$$
R = { \frac { m ^ { \prime } r ^ { 2 } } { r ^ { \prime 3 } } } \left( { \frac { 3 } { 2 } } S ^ { 2 } - { \frac { 1 } { 2 } } \right) + { \frac { m ^ { \prime } r ^ { 3 } } { r ^ { \prime 4 } } } \left( { \frac { 5 } { 2 } } S ^ { 3 } - { \frac { 3 } { 2 } } S \right) + \cdot \cdot \cdot .
$$

If $x ^ { \prime } , y ^ { \prime } , z ^ { \prime } , r ^ { \prime }$ are considered to be the sun's position referred to the center of mass of the earth and moon, then the second term should be multiplied by the mass ratio $( m _ { E } - m _ { M } ) / ( m _ { E } + m _ { M } )$ . Let $\xi , \eta , \zeta , D$ be the coordinates of a planet $P$ referred to the same axes,and $m ^ { \prime \prime }$ be the planet's mass.The corresponding disturbing function for the moon's motion is

$$
R ^ { \prime } = \frac { m ^ { \prime \prime } r ^ { 2 } } { D ^ { 3 } } \left( \frac 3 2 S ^ { \prime 2 } - \frac 1 2 \right) + \frac { m ^ { \prime \prime } r ^ { 3 } } { D ^ { 4 } } \left( \frac 5 2 S ^ { \prime 3 } - \frac 3 2 S ^ { \prime } \right) + \cdot \cdot \cdot ,
$$

$S ^ { \prime }$ being the cosine of the angle between the vectors $\pmb { r }$ and $D , \operatorname { I f } \xi , \eta , \zeta , D$ are referred to the center of mass of the earth and moon,then the second term should be multiplied by $( m _ { E } - m _ { M } ) / ( m _ { E } + m _ { M } )$

Since the ratios $r / r ^ { \prime } , r / D , m ^ { \prime \prime } / m ^ { \prime }$ are small, it is practically sufficient to consider only the first term of $R ^ { \prime }$ . The inequalities produced by $R ^ { \prime }$ are said to be due to the direct action of the planet.In considering the effect due to several planets, the terms produced by the combination of two terms, each belonging to the disturbing function due to the corresponding two planets, can be neglected, so that the effects of different planets can be added after computing the effect of each planet separately. The solar inequalities due to the purely elliptic motion of the sun are supposed to have been determined. The actions of planets on the motion of the earth may produce small deviations from this purely elliptic motion. These actions,when substituted in $R$ ，are small corrections $\delta \boldsymbol { x } ^ { \prime }$ ，8y'， $\delta \boldsymbol { z ^ { \prime } }$ to the solar coordinates $x ^ { \prime } , y ^ { \prime } ,$ $z ^ { \prime }$ .Hence it is sufficient to limit $R$ to its first term for the inequalities produced in the moon's motion. The lunar inequalities produced due to such causes are said to be due to the indirect action of the planets. Since $m ^ { \prime \prime }$ is very small compared with $m ^ { \prime }$ ，these corrections $\delta \boldsymbol { x } ^ { \prime }$ ，8y'， $\delta { z } ^ { \prime }$ are not necessary in $R ^ { \prime }$

Thus we confine ourselves to consider in $\pmb { R }$ and $\pmb { R ^ { \prime } }$ only their first terms:

$$
\begin{array} { l c r } { { \displaystyle \frac { 1 } { m ^ { \prime } } R = \frac { 3 } { 2 } \frac { ( x x ^ { \prime } + y y ^ { \prime } + z z ^ { \prime } ) ^ { 2 } } { r ^ { \prime 5 } } - \frac { 1 } { 2 } \frac { r ^ { 2 } } { r ^ { \prime 3 } } , } } \\ { { \displaystyle \frac { 1 } { m ^ { \prime \prime } } R ^ { \prime } = \frac { 3 } { 2 } \frac { ( x \xi + y \eta + z \zeta ) ^ { 2 } } { D ^ { 5 } } - \frac { 1 } { 2 } \frac { r ^ { 2 } } { D ^ { 3 } } ; } } \end{array}
$$

or

$$
\begin{array} { r l r } { \displaystyle \frac { 1 } { m ^ { \prime } } R = \frac { r ^ { 2 } - 3 z ^ { 2 } } { 4 } \left( \frac { 1 } { r ^ { \prime 3 } } - \frac { 3 z ^ { \prime 2 } } { r ^ { \prime 5 } } \right) \ + \ 3 \frac { x ^ { 2 } - y ^ { 2 } } { 4 } \frac { x ^ { \prime 2 } - y ^ { \prime 2 } } { r ^ { \prime 5 } } } & { } & \\ { \displaystyle + \ 3 x y \left( \frac { x ^ { \prime } y ^ { \prime } } { r ^ { \prime 5 } } \right) \ + \ 3 x z \left( \frac { x ^ { \prime } z ^ { \prime } } { r ^ { \prime 5 } } \right) \ + \ 3 y z \left( \frac { y ^ { \prime } z ^ { \prime } } { r ^ { \prime 5 } } \right) , } & { } & \\ { \displaystyle \frac { 1 } { m ^ { \prime } } R ^ { \prime } = \frac { r ^ { 2 } - 3 z ^ { 2 } } { 4 } \left( \frac { 1 } { D ^ { 3 } } - \frac { 3 \zeta ^ { 2 } } { D ^ { 5 } } \right) \ + \ 3 \frac { x ^ { 2 } - y ^ { 2 } } { 4 } \frac { \xi ^ { 2 } - \eta ^ { 2 } } { D ^ { 5 } } } & { } & \\ { \displaystyle + \ 3 x y \Big ( \frac { \xi \eta } { D ^ { 5 } } \Big ) \ + \ 3 x z \Big ( \frac { \xi \zeta } { D ^ { 5 } } \Big ) \ + \ 3 y z \Big ( \frac { \eta \zeta } { D ^ { 5 } } \Big ) , } \end{array}
$$

in which the moon's coordinates are separated from the sun's or the planet's coordinates.

Suppose the ecliptic to be fixed perpendicular to the $z \mathrm { . }$ -axis. Let $\scriptstyle L$ denote the distance of the moon from its node, $\pmb { h }$ the longitude of the node, and $\gamma$ the sine of half the inclination $\pmb { I }$ of the moon's orbit; then,

$$
\begin{array} { l } { x = r \cos L \cos h - r \cos I \sin L \sin h , } \\ { y = r \cos L \sin h + r \cos I \sin L \cos h , } \\ { z = r \sin L \sin I ; } \end{array}
$$

or

$$
\begin{array} { r l } & { x = ( 1 - \gamma ^ { 2 } ) r \cos { ( L + h ) } + \gamma ^ { 2 } r \cos { ( L - h ) } , } \\ & { y = ( 1 - \gamma ^ { 2 } ) r \sin { ( L + h ) } - \gamma ^ { 2 } r \sin { ( L - h ) } , } \\ & { z = z \gamma \sqrt { 1 - \gamma ^ { 2 } } \cdot r \sin { L } . } \end{array}
$$

Denote by $V ^ { \prime }$ the longitude of the earth as seen from the sun; then we have

$$
x ^ { \prime } = - r ^ { \prime } \cos V ^ { \prime } , { } ~ y ^ { \prime } = - r ^ { \prime } \sin V ^ { \prime } , { } ~ z ^ { \prime } = 0 .
$$

The coordinates of $P$ relative to the earth are $\xi , \eta , \zeta ,$ which are the sums of the coordinates of $P$ relative to the sun and those of the sun relative to the earth.Let $\gamma ^ { \prime \prime }$ be the sine of half the inclination of the planet's orbit to the ecliptic, $h ^ { \prime \prime }$ the longitude of the planet's node on the ecliptic, $V ^ { \prime \prime }$ the longitude of $\pmb { P }$ as seen from the sun,counted along the ecliptic to its node and then along the orbit,and $\pmb { r } ^ { \prime \prime }$ the planet's distance from the sun; then,

$$
\begin{array} { r l } & { \xi = - r ^ { \prime } \cos V ^ { \prime } + ( 1 - \gamma ^ { \prime \prime 2 } ) r ^ { \prime \prime } \cos V ^ { \prime \prime } + \gamma ^ { \prime \prime 2 } r ^ { \prime \prime } \cos \left( V ^ { \prime \prime } - 2 h ^ { \prime \prime } \right) ; } \\ & { \eta = - r ^ { \prime } \sin V ^ { \prime } + ( 1 - \gamma ^ { \prime \prime 2 } ) r ^ { \prime \prime } \sin V ^ { \prime } - \gamma ^ { \prime \prime 2 } r ^ { \prime \prime } \sin \left( V ^ { \prime \prime } - 2 h ^ { \prime \prime } \right) , } \\ & { \zeta = 2 \gamma ^ { \prime \prime } \sqrt { 1 - \gamma ^ { \prime \prime 2 } } . r ^ { \prime \prime } \sin \left( V ^ { \prime \prime } - h ^ { \prime \prime } \right) ; } \end{array}
$$

and

$$
\begin{array} { l } { { \displaystyle { D ^ { 2 } = \xi ^ { 2 } + \eta ^ { 2 } + \zeta ^ { 2 } = D _ { 0 } ^ { 2 } + 4 \gamma ^ { \prime \prime } r ^ { \prime } \sin \left( V ^ { \prime } - h ^ { \prime \prime } \right) \sin \left( V ^ { \prime \prime } - h ^ { \prime \prime } \right) } , } } \\ { { \displaystyle { D _ { 0 } ^ { 2 } = r ^ { \prime 2 } + r ^ { \prime \prime } - 2 r ^ { \prime } r ^ { \prime \prime } \cos \left( V ^ { \prime } - V ^ { \prime \prime } \right) } , } } \\ { { \displaystyle { \frac { 1 } { D ^ { q } } = \frac { 1 } { D _ { 0 } ^ { q } } + \frac { q \gamma ^ { \prime \prime } r ^ { \prime } r ^ { \prime \prime } } { D _ { 0 } ^ { q } + 2 } \left[ \cos \left( V ^ { \prime } + V ^ { \prime } - 2 h ^ { \prime } \right) - \cos \left( V ^ { \prime } - V ^ { \prime \prime } \right) \right] + \cdot } . } } \end{array}
$$

By means of these formulas the disturbing functions $\pmb { R }$ and $\scriptstyle { R ^ { \prime } }$ can be expressed in terms of $r , r ^ { \prime } , r ^ { \prime \prime } , L , V ^ { \prime } , V ^ { \prime \prime } , h , h ^ { \prime } , h ^ { \prime \prime } , \gamma , \gamma ^ { \prime \prime }$ .Then the elliptic values for the coordinates of the three bodies are substituted in various parts of the disturbing function.The terms arising in $\pmb R$ from nonelliptic terms in the coordinates of the three bodies are taken into account. Finally the disturbing function can be expressed as a sum of periodic terms.

Let $g$ be the distance of the moon's perigee from its node and $f$ be the true anomaly; then we have, up to the order $\gamma ^ { 4 }$ ，

$$
\frac { 1 } { 4 } \frac { r ^ { 2 } - 3 z ^ { 2 } } { r ^ { 2 } } = \frac { 1 } { 4 } \left( 1 - 6 \gamma ^ { 2 } + 6 \gamma ^ { 4 } \right) + \frac { 3 } { 2 } \gamma ^ { 2 } ( 1 - \gamma ^ { 2 } ) \cos 2 L ,
$$

$$
{ \frac { 3 } { 4 } } { \frac { x ^ { 2 } - y ^ { 2 } } { r ^ { 2 } } } = { \frac { 3 } { 4 } } ( 1 - \gamma ^ { 2 } ) ^ { 2 } \cos { ( 2 L + 2 h ) } + { \frac { 3 } { 4 } } \gamma ^ { 4 } \cos { ( 2 L - 2 h ) }
$$

$$
L = g + f ,
$$

and similar expressions for ${ \scriptstyle \frac { 3 } { 2 } } ( x y / r ^ { 2 } ) , { \scriptstyle \frac { 3 } { 2 } } ( x z / r ^ { 2 } ) , { \scriptstyle \frac { 3 } { 2 } } ( y z / r ^ { 2 } )$ ,and

$$
{ \frac { r ^ { 2 } } { a ^ { 2 } } } = 1 + { \frac { 3 } { 2 } } e ^ { 2 } - \left( 2 e - { \frac { 1 } { 4 } } e ^ { 3 } \right) \sin l + \cdot \cdot \cdot ,
$$

By giving suitable values to $\propto$ we can express ${ \scriptstyle { \frac { 1 } { 4 } } } ( r ^ { 2 } - 3 z ^ { 2 } )$ ， ${ \frac { 3 } { 4 } } ( x ^ { 2 } - y ^ { 2 } )$ ， and similar expressions in $R$ and $R ^ { \prime }$ in series of cosines or sines with $l , g , h$ as arguments and $\boldsymbol { e } , \gamma$ as coefficients. Thus we obtain (Brown, 1896)

$$
r ^ { 2 } - 3 z ^ { 2 } = \sum A _ { 0 } e ^ { k } \cos k l + \gamma ^ { 2 } \cdot \sum B _ { 0 } e ^ { k } \cos { ( 2 M _ { 0 } - 2 h \pm k l ) } ,
$$

$$
M _ { 0 } = l + g + h ,
$$

where $A _ { 0 } , B _ { 0 }$ are the coeffcients of the zero-th order containing powers and products of $e ^ { 2 }$ ， $\gamma ^ { 2 }$ . Thus the portions of the disturbing function that depend only on the coordinates of the moon are expressed as sums of periodic terms.

Denote by $M _ { 0 } ^ { \prime }$ and $M _ { 0 } ^ { \prime \prime }$ the mean longitudes of the earth and the planet, respectively; then,

$$
\begin{array} { c } { { \displaystyle { \mathrm { } ^ { 2 } - \eta ^ { 2 } = \sum A _ { 0 } \gamma ^ { \prime \prime } { } ^ { 2 { i } } e ^ { \prime \kappa ^ { \prime } } e ^ { \prime \pi \kappa ^ { \prime } } } } } \\ { { \mathrm { } \times \cos { [ 2 M _ { 0 } ^ { \prime } - 2 i M _ { 0 } ^ { \prime } + j ( M _ { 0 } ^ { \prime } - M _ { 0 } ^ { \prime \prime } ) + 2 i l ^ { \prime \prime } \pm k ^ { \prime } l ^ { \prime } \pm k ^ { \prime \prime } ] } } } \end{array}
$$

where $A _ { 0 }$ is the coefficient of the zero-th order, $k ^ { \prime } , k ^ { \prime \prime }$ are positive integers or zero,and $i , j$ are positive integers or zero such that $i + j < 3$ Thus the portions of the disturbing function that involve the coordinates of the sun and the planet in the second degree are expressed as sums of periodic terms.

The divisors $D _ { 0 } ^ { q }$ are functions which cause the great difficulty in finding the planetary inequalities in the moon's motion.This is caused by the near equality of $r ^ { \prime } , r ^ { \prime \prime }$ or of $n ^ { \prime } , n ^ { \prime \prime }$ for those planets which are not far from the earth.The expression $D _ { 0 } ^ { - q }$ is expanded in the form

$$
D _ { 0 } ^ { - q } = { \textstyle \frac { 1 } { 2 } } B _ { q } ^ { ( 0 ) } + B _ { q } ^ { ( 1 ) } \cos \left( V ^ { \prime } - V ^ { \prime \prime } \right) + B _ { q } ^ { ( 2 ) } \cos 2 ( V ^ { \prime } - V ^ { \prime \prime } ) + \cdot \cdot \cdot ,
$$

where $B _ { 0 } ^ { ( j ) }$ are homogeneous functions of $\scriptstyle { \pmb { r } } ^ { \prime }$ and $r ^ { \prime \prime }$ . When $\scriptstyle { \pmb { r } } ^ { \prime }$ and $\pmb { r } ^ { \prime \prime }$ are of comparable magnitude, the formal convergence of the expansion is very slow and higher terms must be taken into account.For a superior planet the expansion should be made in powers of $r ^ { \prime } / r ^ { \prime \prime }$ ；and for an inferior planet, in powers of $r ^ { \prime \prime } / r ^ { \prime }$ . Substitute the elliptic expansions f $\mathrm { { } } \operatorname { x } r ^ { \prime } / a ^ { \prime } , r ^ { \prime \prime } / a ^ { \prime \prime } ;$ ， $V ^ { \prime } , V ^ { \prime \prime }$ in terms of $l ^ { \prime } , l ^ { \prime }$ ; then, we see that

$$
D _ { 0 } ^ { - q } = \sum A _ { 0 } e ^ { \prime k ^ { \prime } } e ^ { \prime \prime k ^ { \prime \prime } } \cos { [ i ( M _ { 0 } ^ { \prime } - M _ { 0 } ^ { \prime \prime } ) \pm k ^ { \prime } l ^ { \prime } \pm k ^ { \prime \prime } l ^ { \prime } ] } ,
$$

where $A _ { 0 }$ is a homogeneous function of $\scriptstyle { a ^ { \prime } }$ and $a ^ { \prime \prime }$ and of the zero-th order with respect to $e ^ { \prime }$ and $e ^ { \prime \prime }$ ; and $j , k ^ { \prime }$ ,and $k ^ { \prime \prime }$ are positive integers or zero. Thus the parts of $R ^ { \prime }$ arising from the divisor $D _ { 0 } ^ { q }$ are expressed as sums of periodic terms.

For the terms arising in $R$ from nonelliptic terms present in the coordinates of the three bodies, we may either suppose that $\scriptstyle { \boldsymbol { r } } ^ { \prime }$ ， $v ^ { \prime }$ receive corresponding small increments $\delta r ^ { \prime } , \delta v ^ { \prime }$ ，or suppose that the additional terms are given as small corrections to the elements of the sun's orbit. In the process of eliminating the periodic terms of $R$ due to the solar action by Delaunay's theory, the moon's elements present in $R ^ { \prime }$ should be changed at each operation.

The indirect action of a planet is taken into account by an abridged form of the disturbing function,

$$
\delta R = - \frac { 3 R } { r ^ { \prime } } \delta r ^ { \prime } - \frac { \partial R } { \partial v } \delta V ^ { \prime } ,
$$

by neglecting the perturbation of the plane of the ecliptic and the ratio of the parallaxes. Most of the larger inequalities of long periods arise from the term $m ^ { \prime } r ^ { 2 } / ( 4 r ^ { \prime 3 } )$ of $R$ .We neglect the eccentricity of the sun's orbit,and obtain

$$
\delta R = - { \frac { 3 } { 4 } } { \frac { n ^ { \prime 2 } a ^ { 2 } } { a ^ { \prime } } } \delta r ^ { \prime } \approx - { \frac { 3 } { 4 } } n ^ { \prime 2 } a ^ { 2 } A \cos \theta ,
$$

where $\delta r ^ { \prime } = a ^ { \prime } A$ cos $\theta$ with constants $\pmb { A }$ and $\theta$ independent of the moon's elements, and

$$
\delta M _ { 0 } = \delta l \approx \frac { 2 } { 9 } \rlap / p A \sin \theta , ~ \phi = \frac { n ^ { \prime } } { \bf w } ,
$$

where M is the motion of the argument $\theta _ { , }$ ， such that $\theta = \mathbf { \boldsymbol { \mathsf { u } } } t +$ constant, in Delaunay's theory. Furthermore, we have approximately

$$
\begin{array} { r l r } { { \displaystyle \mathfrak { z } r ^ { \prime } = \ \delta a ^ { \prime } , \quad } } & { { } { 2 a ^ { \prime } \ \delta n ^ { \prime } = \ - 3 n ^ { \prime } \ \delta a ^ { \prime } = \ - 3 n ^ { \prime } a ^ { \prime } A \cos \theta , } } & { { } } \\ { { } } & { { } } & { { \displaystyle \delta V ^ { \prime } = \int \delta n ^ { \prime } \ \delta t = \ - \frac { 3 } { 2 } \rlap / p A \sin \theta . } } \end{array}
$$

Combining these, we obtain approximately

$$
\delta v = \delta M _ { 0 } = - { \textstyle \frac { 4 } { 2 7 } } \delta V ^ { \prime } .
$$