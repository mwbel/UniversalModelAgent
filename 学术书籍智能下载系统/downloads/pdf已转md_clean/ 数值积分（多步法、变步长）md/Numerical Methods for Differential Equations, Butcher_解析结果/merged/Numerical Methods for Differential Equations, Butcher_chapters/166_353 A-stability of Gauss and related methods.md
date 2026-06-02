# 353 A-stability of Gauss and related methods

We consider the possible A-stability of methods whose stability functions correspond to members on the diagonal and first two sub-diagonals of the Pad´e table for the exponential function. These include the Gauss methods and the Radau IA and IIA methods as well as the Lobatto IIIC methods. A corollary is that the Radau IA and IIA methods and the Lobatto IIIC methods are L-stable.

Theorem 353A Let s be a positive integer and let

$$
R ( z ) = { \frac { N ( z ) } { D ( z ) } }
$$

denote the $( s - d , s )$ member of the Pad´e table for the exponential function, where $d = 0$ , $1$ or 2. Then

$$
| R ( z ) | \leq 1 ,
$$

for all complex $\mathcal { L }$ satisfying $\mathrm { R e } z \le 0$ .

Proof. We use the E-polynomial. Because $N ( z ) = \exp ( z ) D ( z ) + O ( z ^ { 2 s - d + 1 } )$ , we have

$$
\begin{array} { l } { { E ( y ) = D ( i y ) D ( - i y ) - N ( i y ) N ( - i y ) \nonumber } } \\ { { \nonumber } } \\ { { = D ( i y ) D ( - i y ) - \exp ( i y ) D ( i y ) \exp ( - i y ) D ( - i y ) + { \cal O } ( y ^ { 2 s - d + 1 } ) } } \\ { { \nonumber } } \\ { { = { \cal O } ( y ^ { 2 s - d + 1 } ) . } } \end{array}
$$

Because $E ( y )$ has degree not exceeding $2 s$ and is an even function, either $E ( y ) = 0$ , in the case $d = 0$ , or $E ( y ) = C y ^ { 2 s }$ with $C > 0$ , in the cases $d = 1$ and $d = 2$ . In all cases, $E ( y ) \ge 0$ for all real $y$ .

To complete the proof, we must show that the denominator of $R$ has no zeros in the left half-plane. Without loss of generality, we assume that $\mathrm { R e } z < 0$ and we prove that $D ( z ) \neq 0$ . Write $D _ { 0 }$ , $D _ { 1 }$ , $\cdot \cdot \cdot$ , $D _ { s }$ for the denominators of the sequence of Pad´e approximations given by

$$
V _ { 0 0 } , V _ { 1 1 } , \ldots , V _ { s - 1 , s - 1 } , V _ { s - d , s } ,
$$

so that $D ( z ) = D _ { s } ( z )$ . From Theorems 352C, 352D and 352E, we have

$$
D _ { k } ( z ) = D _ { k - 1 } ( z ) + \frac { 1 } { 4 ( 2 k - 1 ) ( 2 k - 3 ) } z ^ { 2 } D _ { k - 2 } , \quad k = 2 , 3 , \ldots , s - 1 ,
$$

and

$$
D _ { s } ( z ) = ( 1 - \alpha z ) D _ { s - 1 } + \beta z ^ { 2 } D _ { s - 2 } ,
$$

where the constants $\alpha$ and $\beta$ will depend on the value of $d$ and $s$ . However, $\alpha = 0$ if $d = 0$ and $\alpha > 0$ for $d = 1$ and $d = 2$ . In all cases, $\beta > 0$ .

Consider the sequence of complex numbers, $\zeta _ { k }$ , for $k = 1 , 2 , \dots , s$ , defined by

$$
\begin{array} { l } { \displaystyle \zeta _ { 1 } = 1 - \frac 1 2 z , } \\ { \displaystyle \zeta _ { k } = 1 + \frac 1 { 4 ( 2 k - 1 ) ( 2 k - 3 ) } z ^ { 2 } \zeta _ { k - 1 } ^ { - 1 } , \qquad k = 2 , 3 , \ldots , s - 1 , } \\ { \displaystyle \zeta _ { s } = ( 1 - \alpha z ) + \beta z ^ { 2 } \zeta _ { s - 1 } ^ { - 1 } . } \end{array}
$$

This means that $\zeta _ { 1 } / z = - 1 / 2 + 1 / z$ has negative real part. We prove by induction that $\zeta _ { k } / z$ also has negative real part for $k = 2 , 3 , \ldots , s$ . We see this by noting that

$$
\begin{array} { l } { \displaystyle \frac { \zeta _ { k } } { z } = \frac { 1 } { z } + \frac { 1 } { 4 ( 2 k - 1 ) ( 2 k - 3 ) } \left( \frac { \zeta _ { k - 1 } } { z } \right) ^ { - 1 } , \qquad k = 2 , 3 , \dots , s - 1 , } \\ { \displaystyle \frac { \zeta _ { s } } { z } = \frac { 1 } { z } - \alpha + \beta \left( \frac { \zeta _ { s - 1 } } { z } \right) ^ { - 1 } . } \end{array}
$$

The fact that $D _ { s } ( z )$ cannot vanish now follows by observing that

$$
\begin{array} { r } { D _ { s } ( z ) = \zeta _ { 1 } \zeta _ { 2 } \zeta _ { 3 } \cdot \cdot \cdot \zeta _ { s } . } \end{array}
$$

Hence, $D = D _ { s }$ does not have a zero in the left half-plane.

Alternative proofs of this and related results have been given byAxelsson (1969, 1972), Butcher (1977), Ehle (1973), Ehle and Picel (1975), Watts and Shampine (1972) and Wright (1970).
