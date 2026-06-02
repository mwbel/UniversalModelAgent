# 454 Concluding remarks on $G$ -stability

It might be suspected that amongst A-stable linear multistep methods, Gstable methods stand out as being in some way superior. Such considerations turn out to be vacuous because a linear multistep method is A-stable if and only if it is G-stable. That G-stable methods are A-stable is shown simply as in Theorem 454A below. However, the converse result is much deeper. This was proved in Dahlquist (1978). Now the easy result:

Theorem 454A A $G$ -stable linear multistep method is $A$ -stable.

Proof. We use the criterion that if $| w | < 1$ , then $z = \alpha ( w ) / \beta ( w )$ is in the right half-plane. Form the inner product $W ^ { * } M W$ , where $M$ is the matrix given by (451e) and

$$
\begin{array} { r } { W = \left[ \begin{array} { c } { 1 } \\ { w } \\ { w ^ { 2 } } \\ { \vdots } \\ { w ^ { k } } \end{array} \right] . } \end{array}
$$

We find that

$$
\alpha ( \overline { { { w } } } ) \beta ( w ) + \alpha ( w ) \beta ( \overline { { { w } } } ) = W ^ { \ast } M W + ( 1 - | w | ^ { 2 } ) \sum _ { j , l = 1 } ^ { k } g _ { j l } \overline { { { w } } } ^ { j - 1 } w ^ { l - 1 } > 0 ,
$$

so that $\mathrm { R e } \big ( \alpha ( w ) / \beta ( w ) \big ) > 0$ .

# Exercises 45

45.1 Show that the method defined by $\begin{array} { r } { \alpha ( z ) = 1 - \frac { 3 } { 2 } z + \frac { 1 } { 2 } z ^ { 2 } } \end{array}$ , $\begin{array} { r } { \beta ( z ) = \frac { 3 } { 4 } - \frac { 1 } { 4 } z } \end{array}$ , is G-stable, by finding the corresponding matrix $G$ .

45.2 Show that if $q _ { 1 } + i q _ { 2 }$ is in the left half-plane, then the differential equation

$$
y ^ { \prime } ( x ) = q y ( x )
$$

can be written as a system

$$
\left[ \begin{array} { c } { y _ { 1 } ^ { \prime } ( x ) } \\ { y _ { 2 } ^ { \prime } ( x ) } \end{array} \right] = \left[ \begin{array} { c c } { q _ { 1 } } & { - q _ { 2 } } \\ { q _ { 2 } } & { q _ { 1 } } \end{array} \right] \left[ \begin{array} { c } { y _ { 1 } ( x ) } \\ { y _ { 2 } ( x ) } \end{array} \right] ,
$$

where $y ( x ) = y _ { 1 } ( x ) + i y _ { 2 } ( x ) .$ . Furthermore, show that this system satisfies (451b), using the usual inner product.
