# 355 Order arrows and the Ehle barrier

For a stability function $R ( z )$ of order $p$ , define two types of ‘order arrows’ as follows:

Definition 355A The locus of points in the complex plane for which $\phi ( z ) =$ $R ( z ) \exp ( - z )$ is real and positive is said to be the ‘order web’ for the rational function $R$ . The part of the order web connected to 0 is the ‘principal order web’. The rays emanating from 0 with increasing value of $\phi$ are ‘up arrows’ and those emanating from 0 with decreasing $\phi$ are ‘down arrows’.

The up and down arrows leave the origin in a systematic pattern:

Theorem 355B Let $R$ be a rational approximation to exp of exact order $p$ so that

$$
R ( z ) = \exp ( z ) - C z ^ { p + 1 } + O ( z ^ { p + 2 } ) ,
$$

where the error constant $C$ is non-zero. If $C ~ < ~ 0$ ( $C ~ > ~ 0$ ) there are up (down) arrows tangential at $0$ to the rays with arguments $k 2 \pi i / ( p + 1 )$ , $k ~ = ~ 0 , 1 , \ldots , p$ , and down (up) arrows tangential at $0$ to the rays with arguments $( 2 k + 1 ) \pi i / ( p + 1 )$ , $k = 0 , 1 , \dotsc , p$ .

Proof. If, for example, $C ~ < ~ 0$ , consider the set $\{ r \exp ( i \theta ) : r > 0 , \theta \in$ $[ k 2 \pi i / ( p + 1 ) - \epsilon , k 2 \pi i / ( p + 1 ) + \epsilon \}$ , where $\epsilon$ and $r$ are both small and $k \in \{ 0 , 1 , 2 , \ldots , p \}$ . We have

$$
R ( z ) \exp ( - z ) = 1 + ( - C ) r ^ { p + 1 } \exp ( ( p + 1 ) \theta ) + O ( r ^ { p + 2 } ) .
$$

For $r$ sufficiently small, the last term is negligible and, for $\epsilon$ sufficiently small, the real part of $( - C ) r ^ { p + 1 } \exp ( ( p + 1 ) \theta ) )$ is positive. The imaginary part changes sign so that an up arrow lies in this wedge. The cases of the down arrows and for $C > 0$ are proved in a similar manner. $\boxed { \begin{array} { r l } \end{array} }$

Where the arrows leaving the origin terminate is of crucial importance.

Theorem 355C The up arrows terminate either at poles of $R$ or at $- \infty$ .   
The down arrows terminate either at zeros of $R$ or at $+ \infty$ .

Proof. Consider a point on an up arrow for which $| z |$ is sufficiently large to ensure that it is not possible that $z$ is a pole or that $z$ is real with $( d / d z ) ( R ( z ) \exp ( - z ) ) ~ = ~ 0$ . In this case we can assume without loss of generality that $\operatorname { I m } ( z ) \geq 0$ . Write $R ( z ) = K z ^ { n } + O ( \vert z \vert ^ { n - 1 } )$ and assume that $K > 0$ (if $K < 0$ , a slight change is required in the details which follow). If $z = x + i y = r \exp ( i \theta )$ , then

$$
\begin{array} { l } { w ( z ) = R ( z ) \exp ( - z ) } \\ { \quad = K r ^ { n } \exp ( - x ) \big ( 1 + O ( r ^ { - 1 } ) \big ) \exp \big ( i ( n \theta - y + O ( r ^ { - 1 } ) ) \big ) . } \end{array}
$$

Because $\theta$ cannot leave the interval $[ 0 , \pi ]$ , then for $w$ to remain real, $y$ is bounded as $z \longrightarrow \infty$ . Furthermore, $w \to \infty$ implies that $x \to - \infty$ .

The result for the down arrows is proved in a similar way.

We can obtain more details about the fate of the arrows from the following result.

Theorem 355D Let $R$ be a rational approximation to exp of order $p$ with numerator degree $n$ and denominator degree $d$ . Let $\widehat { n }$ denote the number of down arrows terminating at zeros and $\hat { d }$ the number of up arrows terminating at poles of R. Then

$$
\widehat { n } + \widehat { d } \geq p .
$$

Proof. There are $p + 1 - \widehat { n }$ down arrows and $p + 1 - { \acute { d } }$ up arrows terminating at $+ \infty$ and $- \infty$ , respectively. Let $\theta$ and $\phi$ be the minimum angles with the properties that all the down arrows which terminate at $+ \infty$ lie within $\theta$ on either side of the positive real axis and all the up arrows which terminate at $- \infty$ lie within an angle $\phi$ on either side of the negative real axis. Hence

$$
2 \theta \geq \frac { ( p - \widehat { n } ) 2 \pi } { p + 1 } , 2 \phi \geq \frac { ( p - \widehat { d } ) 2 \pi } { p + 1 } .
$$

Because up arrows and down arrows cannot cross and, because there is a wedge with angle equal to at least $\pi / ( p + 1 )$ between the last down arrow and the first up arrow, it follows that $2 \theta + 2 \phi + 2 \pi / ( p + 1 ) \le 2 \pi$ . Hence we obtain the inequality

$$
\frac { 2 p + 1 - \widehat { n } - \widehat { d } } { p + 1 } 2 \pi \leq 2 \pi ,
$$

and the result follows.

For Pad´e approximations we can obtain precise values of $\widehat { n }$ and $\hat { d }$ .

Theorem 355E Let $R ( z )$ denote a Pad´e approximation to $\exp ( z )$ , with degrees n (numerator) and d (denominator). Then n of the down arrows terminate at zeros and $d$ of the up arrows terminate at poles.

Proof. Because $p = n + d$ , $n \geq \widetilde n$ and $d \geq \widehat { d }$ , it follows from Theorem 355D that

$$
p = n + d \geq \widetilde { n } + \widetilde { d } \geq p
$$

and hence that $( n - \widetilde { n } ) + ( d - \overset { . } { d } ) = 0$ . Since both terms are non-negative they must be zero and the result follows. 

Before proving the ‘Ehle barrier’, we establish a criterion for A-stability based on the up arrows that terminate at poles.

Theorem 355F A Runge–Kutta method is A-stable only if all poles of the stability function $R ( z )$ lie in the right half-plane and no up arrow of the order web intersects with or is tangential to the imaginary axis.

Proof. The requirement on the poles is obvious. If an up arrow intersects or is tangential to the imaginary axis then there exists $y$ such that

$$
| R ( i y ) \exp ( - i y ) | > 1 .
$$

Because $| \exp ( - i y ) | = 1$ , it follows that $| R ( i y ) | > 1$ and the method is not A-stable. $\sqcup$

We are now in a position to prove the result formerly known as the Ehle conjecture (Ehle, 1973),but which we will also refer to as the ‘Ehle barrier’.

Theorem 355G Let $R ( z )$ denote the stability function of a Runge–Kutta method. If $R ( z )$ is an $( n , d )$ Pad´e approximation to $\exp ( z )$ then the Runge– Kutta is not $A$ -stable unless $d \leq n + 2$ .

Proof. If $d \geq n + 3$ and $p = n + d$ , it follows that $d \geq \frac { 1 } { 2 } ( p + 3 )$ . By Theorem 355E, at least $d$ up arrows terminate at poles. Suppose these leave zero in directions between $- \theta$ and $+ \theta$ from the positive real axis. Then

$$
2 \theta \geq \frac { 2 \pi ( d - 1 ) } { p + 1 } \geq \pi ,
$$

and at least one up arrow, which terminates at a pole, is tangential to the imaginary axis or passes into the left half-plane. If the pole is in the left halfplane, then the stability function is unbounded in this half-plane. On the other hand, if the pole is in the right half-plane, then the up arrow must cross the imaginary axis. In either case, the method cannot be A-stable, by Theorem 355F. 
