# 525 $G$ -symplectic methods

In the special case of Runge–Kutta methods, the matrix $M$ , given by (357d), which arose in the study of non-linear stability, had an additional role. This was in Section 37 where $M$ was used in the characterization of symplectic behaviour. This leads to the question: ‘does $M$ , given by (523b), have any significance in terms of symplectic behaviour’?.

For methods for which $M \ = \ 0$ , although we cannot hope for quadratic invariants to be conserved, a ‘ $G$ extension’ of such an invariant may well be conserved. Although we will show this to be correct, it still has to be asked if there is any computational advantage in methods with this property. The author believes that these methods may have beneficial properties, but it is too early to be definite about this.

The definition, which we now present, will be expressed in terms of the submatrices making up $M$ .

Definition 525A A general linear method $( A , U , B , V )$ is $G$ -symplectic if there exists a positive semi-definite symmetric $r \times r$ matrix $G$ and an $s \times s$ diagonal matrix $D$ such that

$$
\begin{array} { r } { G = V ^ { \top } G V , } \\ { D U = B ^ { \top } G V , } \\ { D A + A ^ { \top } D = B ^ { \top } G B . } \end{array}
$$

The following example of a G-symplectic method was presented in Butcher (2006):

$$
\left[ { \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} } \right] = \left[ { \frac { - { \frac { 3 + { \sqrt { 3 } } } { 6 } } } { \frac { 3 + { \sqrt { 3 } } } { 6 } } } \left| { \begin{array} { c c } { 1 } & { - { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { 1 } & { { \frac { 3 + 2 { \sqrt { 3 } } } { 3 } } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 2 } } } & { - { \frac { 1 } { 2 } } } \end{array} } \right| { \mathrm { . ~ } } \right.
$$

It can be verified that (525d) satisfies (525a)–(525c) with $G = \mathrm { d i a g } ( 1 , 1 + \textstyle { \frac { 2 } { 3 } } { \sqrt { 3 } } )$ and $\begin{array} { r } { D = \mathrm { d i a g } ( \frac { 1 } { 2 } , \frac { 1 } { 2 } ) } \end{array}$ .

Although this method is just one of a large family of such methods which the author, in collaboration with Laura Hewitt and Adrian Hill of Bath University, is trying to learn more about, it is chosen for special attention here. An analysis in Theorem 534A shows that it has order 4 and stage order 2. Although it is based on the same stage abscissae as for the order 4 Gauss Runge–Kutta method, it has a convenient structure in that $A$ is diagonally implicit.

For the harmonic oscillator, the Hamiltonian is supposed to be conserved, and this happens almost exactly for solutions computed by this method for any number of steps. Write the problem in the form $y ^ { \prime } = i y$ so that for stepsize $h$ , $y ^ { \left[ n \right] } = M ( i h ) y ^ { \left[ n - 1 \right] }$ where $M$ is the stability matrix. Long term conservation requires that the characteristic polynomial of $M ( i h )$ has both zeros on the unit circle. This characteristic polynomial is:

![](../chunks/Numerical Methods for Differential Equations, Butcher_part_0007_pages_0421-0484/auto/images/67eaa37cf75bf7430eda4519b0e7a089692ba72a5463178ea47a45705b8540a7.jpg)  
Variation in $| y _ { 1 } ^ { \lfloor n \rfloor } |$ for $n = 0 , 1 , \ldots , 1 4 0$ , with $h = 0 . 1$ ; note that $\epsilon = 0 . 0 0 0 2 7 6$

$$
\begin{array} { r } { w ^ { 2 } \Big ( 1 - i h \frac { 3 + \sqrt { 3 } } { 6 } \Big ) ^ { 2 } + w \Big ( \frac { 2 } { 3 } i \sqrt { 3 } \Big ) h - \Big ( 1 + i h \frac { 3 + \sqrt { 3 } } { 6 } \Big ) ^ { 2 } . } \end{array}
$$

Substitute

$$
w = \frac { 1 + i h \frac { 3 + \sqrt { 3 } } { 6 } } { 1 - i h \frac { 3 + \sqrt { 3 } } { 6 } } i W ,
$$

and we see that

$$
W ^ { 2 } + h \frac { 2 \frac { \sqrt { 3 } } { 3 } } { 1 + h ^ { 2 } ( \frac { 3 + \sqrt { 3 } } { 6 } ) ^ { 2 } } W + 1 .
$$

The coefficient of $W$ lies in $( - \sqrt { 3 } + 1 , \sqrt { 3 } - 1 )$ and the zeros of this equation are therefore on the unit circle for all real $h$ . We can interpret this as saying that the two terms in

$$
\Big ( \big ( p _ { 1 } ^ { [ n ] } \big ) ^ { 2 } + \big ( q _ { 1 } ^ { [ n ] } \big ) ^ { 2 } \Big ) + \big ( 1 + { \textstyle \frac { 2 } { 3 } } \sqrt { 3 } \big ) \Big ( \big ( p _ { 2 } ^ { [ n ] } \big ) ^ { 2 } + \big ( q _ { 2 } ^ { [ n ] } \big ) ^ { 2 } \Big )
$$

are not only conserved in total but are also approximately conserved individually, as long as there is no round-off error. The justification for this assertion is based on an analysis of the first component of $y _ { 1 } ^ { \lfloor n \rfloor }$ as $n$ varies. Write the eigenvalues of $M ( i h )$ as $\lambda ( h ) = 1 + O ( h )$ and $\mu ( h ) = - 1 + O ( h )$ and suppose the corresponding eigenvectors, in each case scaled with first component equal to 1, are $u ( h )$ and $v ( h )$ respectively. If the input $y ^ { [ 0 ] }$ is $a u ( h ) + b v ( h )$ then $y _ { 1 } ^ { \lfloor n \rfloor } = a \lambda ( h ) ^ { n } + b \mu ( h ) ^ { n }$ with absolute value

$$
\vert y _ { 1 } ^ { [ n ] } \vert = \Big ( a ^ { 2 } + b ^ { 2 } + 2 a b \mathrm { R e } \big ( ( \overline { { \lambda ( h ) } } \mu ( h ) ) ^ { n } \big ) \Big ) ^ { 1 / 2 } .
$$

If $| b / a |$ is small, as it will be for small $h$ if a suitable starting method is used, $| y _ { 1 } ^ { n } |$ will never depart very far from its initial value. This is illustrated in Figure 525(i) in the case $h = 0 . 1$ .

# Exercises 52

52.1 Find the stability matrix and stability function for the general linear method

$$
\begin{array}{c} \left[ \frac { \frac { 1 } { 2 } } { \frac { 4 } { 3 } } \quad \frac { 1 } { 2 } \left| \begin{array} { r r } { 1 } & { - \frac { 1 } { 2 } } \\ { 1 } & { - \frac { 5 } { 6 } } \\ { \frac { 1 9 } { 1 6 } } & { \frac { 9 } { 1 6 } } \end{array} \right| \right. 1 \quad - \frac { 3 } { 4 }  \\ { \left. \frac { 1 } { 4 } \quad \frac { 3 } { 4 } \quad \right| \left. 0 \quad \quad 0 \right] } \end{array} .
$$

Show that this method A-stable.

52.2 Find a general linear method with stability function equal to the $[ 2 , 0 , 0 ]$ generalized Pad´e approximation to exp.

52.3 Find the $[ 3 , 0 , 1 ]$ generalized Pad´e approximation to exp.

52.4 Show that the $[ 2 , 0 , 1 ]$ generalized Pad´e approximation to exp is A-stable.
