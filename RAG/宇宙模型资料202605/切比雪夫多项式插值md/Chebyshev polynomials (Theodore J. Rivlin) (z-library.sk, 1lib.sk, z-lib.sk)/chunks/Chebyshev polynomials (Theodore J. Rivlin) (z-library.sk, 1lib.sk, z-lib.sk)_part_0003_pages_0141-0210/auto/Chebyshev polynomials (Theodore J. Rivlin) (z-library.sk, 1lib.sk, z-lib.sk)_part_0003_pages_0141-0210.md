and

$$
| p ^ { ( k + 1 ) } ( v ) | \leqslant | T _ { n } ^ { ( k - 1 ) } ( v ) | \sum _ { i = 1 } ^ { n - ( k - 1 ) } \frac { 1 } { ( v - u _ { i } ) ^ { 2 } } ,
$$

in view of (2.71). Putting $\begin{array} { r } { p = T _ { n } } \end{array}$ in (2.72) yields

$$
| T _ { n } ^ { ( k + 1 ) } ( v ) | = | T _ { n } ^ { ( k - 1 ) } ( v ) | \sum _ { i = 1 } ^ { n - ( k - 1 ) } \frac { 1 } { ( v - u _ { i } ) ^ { 2 } } .
$$

The induction is now completed by substituting (2.74) in (2.73). The possibility of equality is established by the induction,as well, since the inequality (2.73) is strict unless $\begin{array} { r } { p = T _ { n } } \end{array}$

It is not difficult to obtain a best uniform bound on $| p ^ { \prime } ( x ) |$ from (2.69). Suppose that $n > 1$ If

$$
| x | \leqslant \cos { \frac { \pi } { 2 n } } = \xi _ { 1 } ^ { ( n ) } ,
$$

then

$$
1 - x ^ { 2 } \geqslant 1 - \cos ^ { 2 } { \frac { \pi } { 2 n } } = \sin ^ { 2 } { \frac { \pi } { 2 n } } > \left[ { \frac { 2 } { \pi } } \left( { \frac { \pi } { 2 n } } \right) \right] ^ { 2 } = { \frac { 1 } { n ^ { 2 } } }
$$

and $\pmb { p } \in \pmb { B _ { n } }$ implies

$$
| p ^ { \prime } ( x ) | < n ^ { 2 } ,
$$

in view of (2.69). Next, suppose that $| x | > \xi _ { 1 } ^ { ( n ) }$ . If we recall(1.41), we se that

$$
p ^ { \prime } ( x ) = L _ { n - 1 } ( p ^ { \prime } , T ; x ) = \frac { T _ { n } ( x ) } { n } \sum _ { j = 1 } ^ { n } ~ ( - 1 ) ^ { j - 1 } ~ \frac { p ^ { \prime } ( \xi _ { j } ^ { ( n ) } ) ( 1 - ( \xi _ { j } ^ { ( n ) } ) ^ { 2 } ) ^ { 1 / 2 } } { ( x - \xi _ { j } ^ { ( n ) } ) } .
$$

In the interval $\zeta _ { 1 } ^ { ( n ) } < x \leqslant 1$ $T _ { n } ( x )$ is positive as is $( x - \xi _ { j } ^ { ( n ) } )$ for $j = 1 , \ldots , n ;$ hence, since $| p ^ { \prime } ( \xi _ { j } ^ { ( n ) } ) ( 1 - ( \xi _ { j } ^ { ( n ) } ) ^ { 2 } ) ^ { 1 / 2 } | \leqslant n$ [by (2.69) or,better stil, (2.70)], we obtain

$$
| p ^ { \prime } ( x ) | \leqslant T _ { n } ( x ) \sum _ { j = 1 } ^ { n } { \frac { 1 } { x - \xi _ { j } ^ { ( n ) } } } = T _ { n } ^ { \prime } ( x ) .
$$

Since $T _ { n } ^ { \prime } ( x )$ is monotone increasing in $\xi _ { 1 } ^ { ( n ) } \leqslant x \leqslant 1 ,$

$$
| p ^ { \prime } ( x ) | \leqslant T _ { n } ^ { \prime } ( 1 ) = n ^ { 2 } .
$$

The case $- 1 \leqslant x \leqslant - \xi _ { 1 } ^ { ( n ) } = \xi _ { n } ^ { ( n ) }$ is treated in the same way,and putting the

pieces together yields the theorem of A. A. Markov:

If $\pmb { p } \in \pmb { B } _ { n }$ then $\| \pmb { p } ^ { \prime } \| \leqslant n ^ { 2 }$ , with equality only for $p = \pm T _ { n }$

[The condition for equality stems from (2.70).] We shall have more to say about this theorem shortly.

Remark 5. $\mathbf { \Delta } _ { t \in \mathcal { T } _ { n } }$ and $\| t \| \leqslant 1$ imply $\big \| t ^ { ( k ) } \big \| \leqslant n ^ { k }$ by mathematical induction on the order of the derivative $\pmb { k }$ 、

Remark 6. Repeated application of A. A. Markov's theorem gives

$$
\| p ^ { ( k ) } \| \leqslant [ n ( n - 1 ) \cdot \cdot \cdot ( n - ( k - 1 ) ) ] ^ { 2 } , \qquad k = 1 , \ldots , n ,
$$

a bound that is much too large. To obtain a better bound we observe that if $\pmb { p } \in \pmb { B } _ { \pmb { n } }$ then for $0 < x _ { 0 } \leqslant 1$

$$
q ( x ) = p \biggl [ ( 1 + x _ { 0 } ) \frac { 1 + x } { 2 } - 1 \biggr ] \in B _ { n } ,
$$

and, since

$$
\left[ \left[ \frac { ( 1 + x _ { 0 } ) } { 2 } \right] ^ { k } p ^ { ( k ) } ( x _ { 0 } ) \right] = | q ^ { ( k ) } ( 1 ) | \leqslant T _ { n } ^ { ( k ) } ( 1 ) ,
$$

in view of (2.37), $| p ^ { ( k ) } ( x _ { 0 } ) | \leqslant 2 ^ { k } T _ { n } ^ { ( k ) } ( 1 ) .$ If $- 1 \leqslant x _ { 0 } < 0 .$ ，the same result is obtained by putting

$$
q ( x ) = p \left[ \left( 1 - x _ { 0 } \right) { \frac { x - 1 } { 2 } } + 1 \right] .
$$

Thus, recalling (1.97), we obtain

$$
\| p ^ { ( k ) } \| \leqslant 2 ^ { k } { \frac { n ^ { 2 } ( n ^ { 2 } - 1 ) \cdot \cdot \cdot ( n ^ { 2 } - ( k - 1 ) ^ { 2 } ) } { 1 \cdot 3 \cdot 5 \cdots ( 2 k - 1 ) } } .
$$

The truth of the matter is that (2.77) remains true with the factor $2 ^ { k }$ deleted.   
We establish this next, but it is no easy task.

# 5. V. A. Markov’s Theorem.

The direct generalization of A. A. Markov's theorem was provided by his brother, V.A. Markov [1] (see also Bernstein [3], Mohr [1], Voronovskaja [1],and Boas [1]), who showed that if $\pmb { p } \in \pmb { B _ { n } }$ then $\| p ^ { ( k ) } \| \leqslant T _ { n } ^ { ( k ) } ( 1$ 1), $0 \leqslant k \leqslant n$ We follow Duffin and Schaeffer [1] in proving the stronger result that ${ \pmb { p } } \in { \pmb { C } } _ { \pmb { n } }$ implies $\| p ^ { ( k ) } \| \leqslant T _ { n } ^ { ( k ) } ( 1 ) , 1 \leqslant k \leqslant n .$ . First let us see how far we can get with our representation formula for linear functionals. If $- 1 \leqslant \xi \leqslant 1$ ,let

$$
M _ { k } ( \xi ) = \operatorname* { m a x } _ { p \in C _ { n } } | p ^ { ( k ) } ( \xi ) | , \qquad 1 \leqslant k \leqslant n .
$$

We saw,(2.37), that M(1)= T(1). Hence M()= M(1)= T(1) = 2"-1. Note also that

$$
M _ { k } ( - \xi ) = M _ { k } ( \xi ) ,
$$

for if $p _ { \xi } ^ { ( k ) } ( \xi ) = M _ { k } ( \xi )$ and $q ( x ) = p _ { \xi } ( - x )$ then $q \in C _ { n }$ ， $M _ { k } ( - \xi ) \geqslant | q ^ { ( k ) } ( - \xi ) | =$ $\begin{array} { r } { p _ { \xi } ^ { ( k ) } ( \xi ) = M _ { k } ( \xi ) , } \end{array}$ and, reversing the roles of $\xi$ and $- \xi ,$ ,establishes (2.78).

Suppose then that $0 \leqslant \xi \leqslant 1$ ， $1 \leqslant k \leqslant n - 1 .$ , and let $B = \{ \eta _ { 0 } ^ { ( n ) } , \ldots , \eta _ { n } ^ { ( n ) } \}$ in Theorem 2.13.Let

$$
F p = p ^ { ( k ) } ( \xi ) = \sum _ { j = 1 } ^ { r } \alpha _ { j } p ( y _ { j } )
$$

be a canonical representation of $p ^ { ( k ) } ( \xi ) ,$ ,where, of course, the $y _ { j }$ come from $\pmb { B }$ Since $\pm 1$ is clearly no extremal for $F _ { : }$ ，(2.79) is its unique canonical representation according to Remark 3 following Theorem 2.15. We claim that $\pmb { r } \geqslant \pmb { n }$ f $r \leqslant n - 1$ and $\omega ( x ) = ( x - y _ { 1 } ) \cdots ( x - y _ { n - 1 } ) { \mathrm { , } }$ where $y _ { r + 1 } , \dotsc , y _ { n - 1 }$ are“new”distinct points of $\pmb { B } ,$ then ${ \pmb { \omega } } ^ { ( k ) } ( \xi ) = { \bf 0 }$ ，but $q ( x ) = x \omega ( x ) \in \mathcal { P } _ { n }$ and $0 = q ^ { ( k ) } ( \xi ) = \xi \omega ^ { ( k ) } ( \xi ) + k \omega ^ { ( k - 1 ) } ( \xi ) ,$ hence $\omega ^ { ( k - 1 ) } ( \xi ) = 0$ Rolle's theorem im-plies that $\omega ^ { ( k - 1 ) }$ has only simple zeros which contradicts the existence of a zero of order at least 2 at $\xi .$

Now the Lagrange interpolation formula yields

$$
F p = p ^ { ( k ) } ( \xi ) = \sum _ { i = 0 } ^ { n } p ( \eta _ { i } ) l _ { i } ^ { ( k ) } ( \xi ) ,
$$

which is a canonical representation of $\pmb { F }$ ,since

$$
\sum _ { i = 0 } ^ { n } | l _ { i } ^ { ( k ) } ( \xi ) | = M _ { k } ( \xi ) .
$$

Thus (2.80) and (2.79) must be identical, and we have $r = n + 1$ expect for the finite number of points $\xi$ which are zeros of some $l _ { i } ^ { ( k ) } ( x )$ (keep in mind that here $B \neq I$ ). Note that, since $r \geqslant n ,$ no two $l _ { i } ^ { ( k ) } ( x )$ are zero simultaneously for any $\pmb { x } .$ The fundamental polynomials $l _ { i } ^ { ( k ) } ( x )$ are given explicitly by

$$
l _ { i } ( x ) = \left\{ \begin{array} { l l } { \displaystyle \frac { ( - 1 ) ^ { i + 1 } ( 1 - x ^ { 2 } ) T _ { n } ^ { \prime } ( x ) } { n ^ { 2 } ( x - \eta _ { i } ) } , } & { i = 1 , \ldots , n - 1 } \\ { \displaystyle \frac { ( - 1 ) ^ { i + 1 } ( 1 - x ^ { 2 } ) T _ { n } ^ { \prime } ( x ) } { 2 n ^ { 2 } ( x - \eta _ { i } ) } , } & { i = 0 , n . } \end{array} \right.
$$

Therefore,if we put

$$
\varepsilon _ { i } ( \xi ) = \operatorname { s g n } l _ { i } ^ { ( k ) } ( \xi )
$$

so that (2.81) reads

$$
\sum _ { i = 0 } ^ { n } \varepsilon _ { i } ( \xi ) l _ { i } ^ { ( k ) } ( \xi ) = M _ { k } ( \xi ) ,
$$

we see that

$$
\varepsilon _ { i } ( 1 ) = ( - 1 ) ^ { i } , \qquad i = 0 , \ldots , n ,
$$

and since $p _ { \xi } ( \eta _ { i } ) = \varepsilon _ { i } ( \xi )$ we recover the fact that $\begin{array} { r } { p _ { 1 } ( x ) = T _ { n } ( x ) . } \end{array}$ But,if $\pmb { \tau }$ denotes the largest zero of any of $l _ { i } ^ { ( k ) } ( x ) , i = 0 , . . . , n$ (hence $- 1 < \tau < 1 \}$ , then

$$
\varepsilon _ { i } ( \xi ) = ( - 1 ) ^ { i } , \qquad i = 0 , \ldots , n ,
$$

for $\tau < \xi < 1$ and we know that

$$
p _ { \xi } ( x ) = T _ { n } ( x )
$$

and

$$
M _ { k } ( \xi ) = T _ { n } ^ { ( k ) } ( \xi ) , \qquad \mathrm { f o r } ~ \tau \leqslant 1 .
$$

We claim next that $\pmb { \tau }$ is the largest zero of $l _ { n } ^ { ( k ) } ( x )$ .To establish this we need the following preliminary result.

Lemma 2.7.1. If $p ( x ) = ( x - a _ { 1 } ) \cdots ( x - a _ { m } )$ and $q ( x ) = ( x - b _ { 1 } ) \cdots ( x - b _ { m } ) ,$ where $b _ { 1 } > a _ { 1 } > b _ { 2 } > a _ { 2 } > \dots > b _ { m } > a _ { m }$ ,then,if $t _ { 1 } , \ldots , t _ { m - 1 }$ are the zeros of $\pmb { p } ^ { \prime }$ and $z _ { 1 } , \dotsc , z _ { m - 1 }$ are the zeros of $\pmb q ^ { \prime }$ (each set arranged in decreasing order), we have $z _ { 1 } > t _ { 1 } > z _ { 2 } > t _ { 2 } > \dots > z _ { m - 1 } > t _ { m - 1 }$

Proof. Since $p ( x ) - q ( x ) \in \mathcal { P } _ { m - 1 }$ , the Lagrange interpolation formula gives

$$
p ( x ) - q ( x ) = \sum _ { j = 1 } ^ { m } { \frac { p ( b _ { j } ) - q ( b _ { j } ) } { q ^ { \prime } ( b _ { j } ) } } { \frac { q ( x ) } { x - b _ { j } } } = \sum _ { j = 1 } ^ { m } { \frac { p ( b _ { j } ) } { q ^ { \prime } ( b _ { j } ) } } { \frac { q ( x ) } { x - b _ { j } } } .
$$

Suppose $\pmb q ^ { \prime } ( z ) = \mathbf { 0 } ;$ ，then (2.84) implies that

$$
{ \frac { p ^ { \prime } ( z ) } { q ( z ) } } = - \sum _ { j = 1 } ^ { m } { \frac { p ( b _ { j } ) } { q ^ { \prime } ( b _ { j } ) } } { \frac { 1 } { ( z - b _ { j } ) ^ { 2 } } } .
$$

We observe that for $j = 1 , \ \ldots , \ m , \ \mathrm { s g n } q ^ { \prime } ( b _ { j } ) = ( - 1 ) ^ { j - 1 }$ and $\mathsf { s g n } p ( b _ { j } ) =$

$( - 1 ) ^ { j - 1 }$ . Thus for $i = 1 , \ldots , m - 1$

$$
\frac { p ^ { \prime } ( z _ { i } ) } { q ( z _ { i } ) } < 0 .
$$

Now sgn $q ( z _ { i } ) = ( - 1 ) ^ { i }$ and so sgn $p ^ { \prime } ( z _ { i } ) = ( - 1 ) ^ { i - 1 }$ . Hence $\pmb { p } ^ { \prime }$ has exactly one zero in each interval $( z _ { i + 1 } , z _ { i } ) , i = 1 , . . . , m - 2$ (for if it has more than one zero in one such interval it has at least three there),and since $\pmb { p } ^ { \prime }$ is positive at both $z _ { 1 }$ and $a _ { 1 }$ its remaining zero is not in $( z _ { 1 } , a _ { 1 } ) .$ Thus $\pmb { p } ^ { \prime }$ has its remaining zero in $( a _ { m } , z _ { m - 1 } )$ .This establishes the lemma.

Remark. It is easy to see, using mathematical induction, that the hypothesis of the lemma implies that the zeros of $\pmb { p } ^ { ( k ) }$ and $\pmb q ^ { ( k ) }$ for $k = 2 , \ldots , m - 1$ interlace in exactly the same way as those of $\pmb { p } ^ { \prime }$ and $\pmb q ^ { \prime }$

Let us consider $l _ { i } ( x )$ and $l _ { j } ( \boldsymbol { x } )$ fundamental polynomials for any set of nodes $x _ { 0 } > x _ { 1 } > \cdots > x _ { n }$ where $i > j .$ There exists a nonzero constant, $c ,$ such that $l _ { j } - c l _ { i } \in \mathcal { P } _ { n - 1 }$ .Applying the Lagrange interpolation formula, as in the proof of Lemma 2.7.1, yields

$$
\frac { l _ { j } ^ { \prime } ( z ) } { l _ { i } ( z ) } = - \frac { 1 } { l _ { i } ^ { \prime } ( x _ { j } ) } \frac { 1 } { ( z - x _ { j } ) ^ { 2 } } ,
$$

where $z$ is any zero of $l _ { i } ^ { \prime }$ . The leading coefficient of $l _ { i } ( x )$ has the sign of $( - 1 ) ^ { i }$ as Exercise 1.3.6 reveals; hence

$$
\operatorname { s g n } l _ { i } ^ { \prime } ( x _ { i } ) = ( - 1 ) ^ { i + j }
$$

and

$$
\ s g n \ \frac { l _ { j } ^ { \prime } ( z ) } { l _ { i } ( z ) } = ( - 1 ) ^ { i + j + 1 } .
$$

Now we can conclude, exactly as we did in the proof of Lemma 2.7.1, that the zeros of $l _ { i } ^ { \prime }$ and $l _ { j } ^ { \prime }$ interlace strictly. This fact, together with the lemma, applied to $l _ { i } ^ { \prime }$ and $l _ { j } ^ { \prime }$ leads us to the following conclusion.

Theorem 2.21. Given any nodes $x _ { 0 } > x _ { 1 } > \cdots > x _ { n }$ and $l _ { i } ( x ) , i = 0 , \ldots , n ,$ the fundamental polynomials for the nodes; if $z _ { i , 1 } > z _ { i , 2 } > \cdots > z _ { i , n - k }$ are the zeros of $l _ { i } ^ { ( k ) } ( x ) , 1 \leqslant k \leqslant n - 1 ,$ then

$$
\begin{array} { r l } & { \phantom { { \sum } } _ { 1 } > z _ { n - 1 , 1 } > \cdots > z _ { 0 , 1 } > z _ { n , 2 } > z _ { n - 1 , 2 } > \cdots > z _ { 0 , 2 } > \cdots } \\ & { \phantom { { \sum } } _ { 1 } > z _ { n - 1 , 1 } > \cdots > z _ { 0 , 1 } > \cdots > z _ { 0 , n - k } , } \end{array}
$$

In particular, then, the $\pmb { \tau }$ in (2.83) is the largest zero of $l _ { n } ^ { ( k ) } ( x )$ or, equivalently, of $[ ( 1 - x ) T _ { n } ^ { \prime } ( x ) ] ^ { ( k ) } = ( 1 - x ) T _ { n } ^ { ( k + 1 ) } ( x ) - k T _ { n } ^ { ( k ) } ( x ) = \left( [ ( k - 1 ) x - k ] T _ { n } ^ { ( k ) } ( x ) - \right.$ $[ n ^ { 2 } - ( k - 1 ) ^ { 2 } ] \ T _ { n } ^ { ( k - 1 ) } ( x ) ) / ( 1 + x ) ,$ in view of Exercise1.5.5.Note that if $\pmb { u }$ is the largest zero of $T _ { n } ^ { ( k - 1 ) } ( x )$ then certainly $\pmb { \tau } < \pmb { u }$ (cf. Exercise 1.5.10).

The choice of $x _ { i } = \eta _ { i }$ in Theorem 2.21 enables us to describe $M _ { k } ( \xi )$ more fully. In each interval $( z _ { n - i , j } , z _ { n - i + 1 , j } ) , i = 1 , . . . , n ; j = 1 , . . . , n - k$ or $( z _ { n , j } ,$ $z _ { 0 , j - 1 } ) , \mathbf { j } = 2 , \dots , n - k ,$ none of $\varepsilon _ { i } ( \xi ) , i = 0 , \ldots , n ,$ changes sign and $M _ { k } ( \xi )$ is given by the polynomial (2.82).

As we have just seen for $z _ { n , 1 } < \xi < 1$

$$
\varepsilon _ { i } ( \xi ) = ( - 1 ) ^ { i } , \qquad i = 0 , \ldots , n .
$$

f $\xi$ now passes into the interval $( z _ { n - 1 , 1 } , z _ { n , 1 } )$ the sign configuration becomes

$$
\begin{array} { l l } { { \varepsilon _ { i } ( \xi ) = ( - 1 ) ^ { i } , } } & { { i = 0 , . . . , n - 1 } } \\ { { } } & { { } } \\ { { \varepsilon _ { n } ( \xi ) = ( - 1 ) ^ { n - 1 } . } } \end{array}
$$

As $\xi$ continues to move to the left, an alternation of sign percolates through the sequence $\varepsilon _ { n } , \varepsilon _ { n - 1 } , \ldots , \varepsilon _ { 0 } ,$ until $\xi$ passes through the point $\pmb { z _ { 0 , 1 } }$ into $( z _ { n , 2 } ,$ $z _ { 0 , 1 } )$ in which

$$
\varepsilon _ { i } ( \xi ) = ( - 1 ) ^ { i - 1 } , \qquad i = 0 , \ldots , n .
$$

Thus in $( z _ { n , 2 } , z _ { 0 , 1 } ) , p _ { \xi } ( x ) = - T _ { n } ( x )$ and $M _ { k } ( \xi ) = - T _ { n } ^ { ( k ) } ( \xi ) .$ Now, when ${ \pmb \xi }$ moves past $z _ { n , 2 }$ ,the percolation process is repeated, starting with

$$
\begin{array} { l } { \varepsilon _ { i } ( \xi ) = ( - 1 ) ^ { i - 1 } , \qquad i = 0 , \ldots , n - 1 , } \\ { \varepsilon _ { n } ( \xi ) = ( - 1 ) ^ { n } , } \end{array}
$$

for $\xi$ in $( z _ { n - 1 , 2 } , z _ { n , 2 } )$ . Thus, if $\pmb { p } _ { \xi } = \pmb { q }$ in $( z _ { n - 1 , 1 } , z _ { n , 1 } ) ;$ then $p _ { \xi } = - q$ in $( z _ { n - 1 , 2 } ,$ $z _ { n , 2 } )$ ,and so on.

In the case $k = n - 1$ analysis of (2.81) leads to an easy proof of the Duffin-Schaeffer-Markov result.

Theorem 2.22. If ${ \pmb { p } } \in C _ { \pmb { n } }$ , then for $- 1 \leqslant x \leqslant 1$

$$
\vert p ^ { ( n - 1 ) } ( x ) \vert \leqslant T _ { n } ^ { ( n - 1 ) } ( 1 ) = 2 ^ { n - 1 } n ! ,
$$

with equality possible only if $p = \pm T _ { n }$ and $x = \pm 1$

Proof. As an easy consequence of (2.82) we see that

$$
l _ { i } ^ { ( n - 1 ) } ( x ) = \left\{ \begin{array} { l l } { { ( - 1 ) ^ { i } 2 ^ { n - 1 } ( n - 1 ) ! \bigg ( x + \frac { \eta _ { i } } { n } \bigg ) , } } & { { i = 1 , \ldots , n - 1 , } } \\ { { } } & { { } } \\ { { ( - 1 ) ^ { i } 2 ^ { n - 2 } ( n - 1 ) ! \bigg ( x + \frac { \eta _ { i } } { n } \bigg ) , } } & { { i = 0 , n . } } \end{array} \right.
$$

Therefore

$$
M _ { n - 1 } ( \xi ) = \sum _ { i = 0 } ^ { n } | l _ { i } ^ { ( n - 1 ) } ( \xi ) | = 2 ^ { n - 1 } ( n - 1 ) ! \sum _ { i = 0 } ^ { n } \biggl | \xi + \frac { \eta _ { i } } { n } \biggr | .
$$

We claim that

$$
f ( \xi ) = \sum _ { i = 0 } ^ { n } \left| \xi + \frac { \eta _ { i } } { n } \right|
$$

attains its maximum on [0,1] at $\xi = 1 . f ( \xi )$ is a polygonal line with possible changes in direction at $- \eta _ { i } / n , i = 0 ,$ .， $\pmb { n } ,$ ，and its slope in $- \eta _ { j } / n < x < - \eta _ { j + 1 } / n , j = 0 , \ldots , n - 1 ,$ is

$$
\sum _ { i = 0 } ^ { j } { 1 - \sum _ { i = j + 1 } ^ { n - 1 } 1 - \frac { 1 } { 2 } } = 2 j + 1 - n .
$$

Since only breaks corresponding to $j \geqslant [ n / 2 ]$ fall in $0 \leqslant \xi \leqslant 1$ ,the slopes of consecutive segments of $f ( \xi )$ as $\xi$ moves from $- \eta _ { [ n / 2 ] } / n$ to 1 are nonnegative and increasing so that $f ( \xi )$ is monotone increasing in $\begin{array} { r } { [ - \pmb { \eta } _ { [ n / 2 ] } / n , } \end{array}$ 1]; but $- \eta _ { [ n / 2 ] } / n \leqslant 0 .$ hence $| f ( \xi ) | \leqslant | f ( 1 ) | , 0 \leqslant \xi \leqslant 1$ ，with equality only at $\xi = 1$ Thus, if $0 \leqslant \xi < 1$ ，

$$
M _ { n - 1 } ( \xi ) < M _ { n - 1 } ( 1 ) = T _ { n } ^ { ( n - 1 ) } ( 1 ) .
$$

The conditions for equality follow from Example 1, p. 108.

Note that $M _ { n - 1 } ( \xi )$ is a convex function of $\xi$ on[-1,1]. For $\pmb { k }$ other than $n - 1$ this need not be the case; indeed,it may happen that $M _ { k } ( \xi )$ is not even monotone increasing on [O,1]. Let us look at some examples.

1. Suppose that ${ \pmb n } = 2 .$ . Clearly

$$
M _ { 1 } ( \xi ) = \left\{ { \begin{array} { l l } { 2 \xi + 1 , \quad } & { 0 \leqslant \xi \leqslant { \frac { 1 } { 2 } } , } \\ { 4 \xi , \quad } & { { \frac { 1 } { 2 } } \leqslant \xi \leqslant 1 . } \end{array} } \right.
$$

Let us compare this with the case in which we seek to maximize $\| \pmb { p } ^ { \prime } \|$ subject to $\pmb { \cal p } \in { \pmb { { \cal B } } } _ { 2 }$ (rather than $c _ { 2 } )$ .If $- 1 \leqslant \xi \leqslant 1$ put

$$
N _ { k } ( \xi ) = \operatorname* { m a x } _ { p \in B _ { n } } \vert p ^ { ( k ) } ( \xi ) \vert , \qquad 1 \leqslant k \leqslant n .
$$

Of course, since $B _ { n } \subset C _ { n }$ , we have $N _ { k } ( \xi ) \leqslant M _ { k } ( \xi ) .$ . Suppose that $\pmb { n = 2 }$ Let us find $N _ { 1 } ( \xi )$ .The remark immediately following Theorem 2.21, with $k = 1$ and $n = 2 ,$ ，shows that

$$
N _ { 1 } ( \xi ) = T _ { 2 } ^ { \prime } ( \xi ) = 4 \xi , \qquad { \scriptstyle \frac { 1 } { 2 } } \leqslant \xi \leqslant 1 .
$$

Suppose, then, that $0 < \xi < \frac { 1 } { 2 } ,$ and

$$
\begin{array} { r } { q _ { \xi } ^ { \prime } ( \xi ) = N _ { 1 } ( \xi ) . } \end{array}
$$

Then for all $\pmb q \in { \pmb B } _ { 2 }$ we have

$$
q ^ { \prime } ( \xi ) = \alpha _ { 1 } q ( x _ { 1 } ) + \alpha _ { 2 } q ( x _ { 2 } )
$$

and $q _ { \xi } ^ { \prime } ( \xi ) = | \alpha _ { 1 } | + | \alpha _ { 2 } | .$ Both $\mathbf { x _ { 1 } }$ and $\mathbf { \boldsymbol { x } } _ { 2 }$ cannot be interior points of [-1,1], for in that case $q _ { \xi } ^ { \prime } ( x _ { 1 } ) = q _ { \xi } ^ { \prime } ( x _ { 2 } ) = 0 \nonumber $ Putting $q ( x ) = ( x - x _ { 1 } ) ( x - x _ { 2 } )$ reveals that $\xi = ( x _ { 1 } + x _ { 2 } ) / 2$ ,hence neither of $\mathbf { x _ { 1 } }$ and $\mathbf { \boldsymbol { x } } _ { 2 }$ is -1. Suppose that $\mathbf { \boldsymbol { x } _ { 1 } } = 1$ ， then $\begin{array} { r } { x _ { 2 } = 2 \xi - 1 _ { \cdot } } \end{array}$ ， $q = 1$ and $\pmb q = \pmb x$ imply that $\alpha _ { 1 } + \alpha _ { 2 } = 0$ and ${ \pmb { \alpha } } _ { 1 } +$ $\alpha _ { 2 } ( 2 \xi - 1 ) = 1$ ; hence

$$
\alpha _ { 1 } = \frac { 1 } { 2 ( 1 - \xi ) } , ~ \alpha _ { 2 } = - \frac { 1 } { 2 ( 1 - \xi ) }
$$

and $q _ { \xi } ^ { \prime } ( \xi ) = ( 1 - \xi ) ^ { - 1 } > 4 \xi = T _ { 2 } ^ { \prime } ( \xi ) .$ The polynomial

$$
q _ { \xi } ( x ) = \frac { 1 } { 2 ( 1 - \xi ) ^ { 2 } } \left( x ^ { 2 } - 2 ( 2 \xi - 1 ) x + ( 2 \xi ^ { 2 } - 1 ) \right)
$$

is in $B _ { 2 }$ for $0 \leqslant \xi \leqslant \frac { 1 } { 2 }$ Hence

$$
N _ { 1 } ( \xi ) = \left\{ { \frac { 1 } { 1 - \xi } } , \qquad 0 \leqslant \xi \leqslant { \frac { 1 } { 2 } } , \right.
$$

Note that $M _ { k } ( \xi )$ for any $\pmb { n }$ is, in view of (2.81),a piecewise polynomial function, whereas (2.86) shows that $N _ { 1 } ( \xi )$ for $\pmb { n = 2 }$ is not.

2. Suppose that $\pmb { n = 3 }$ An easy calculation yields

$$
\begin{array} { r l } { M _ { 1 } ( \xi ) = \displaystyle \frac { \biggl ( - 1 2 \xi ^ { 2 } + 3 , \xi } { 8 } , \qquad } & { 0 \leqslant \xi \leqslant \frac { \sqrt { 7 } - 2 } { 6 } , } \\ { \displaystyle - \frac { 8 } { 3 } ( 3 \xi ^ { 2 } - \xi - 1 ) , \quad } & { \frac { \sqrt { 7 } - 2 } { 6 } \leqslant \xi \leqslant \frac { \sqrt { 1 3 } - 1 } { 6 } , } \\ { M _ { 1 } ( \xi ) = \displaystyle \frac { 1 6 } { 3 } \xi , \qquad } & { \frac { \sqrt { 1 3 } - 1 } { 6 } \leqslant \xi \leqslant \frac { \sqrt { 1 3 } + 1 } { 6 } , } \\ { \displaystyle \frac { 8 } { 3 } ( 3 \xi ^ { 2 } + \xi - 1 ) , \qquad } & { \frac { \sqrt { 1 3 } + 1 } { 6 } \leqslant \xi \leqslant \frac { \sqrt { 7 } + 2 } { 6 } , } \\ { \displaystyle \frac { 1 2 \xi ^ { 2 } - 3 } { 6 } , \qquad } & { \frac { \sqrt { 7 } + 2 } { 6 } \leqslant \xi \leqslant 1 . } \end{array}
$$

By contrast Boas [1] gives

$$
\begin{array} { r } { N _ { 1 } ( \xi ) = \left\{ \begin{array} { l l } { - 1 2 \xi ^ { 2 } + 3 , \quad } & { 0 \leqslant \xi \leqslant \frac { \sqrt { 7 } - 2 } { 6 } , } \\ { \frac { 7 } { 9 ( 1 + \xi ) } , } & { \frac { \sqrt { 7 } - 2 } { 6 } \leqslant \xi \leqslant \frac { 2 \sqrt { 7 } - 1 } { 9 } , } \\ { \frac { 1 6 \xi ^ { 3 } } { 9 ( 9 \xi ^ { 2 } - 1 ) ( 1 - \xi ^ { 2 } ) } , } & { \frac { 2 \sqrt { 7 } - 1 } { 9 } \leqslant \xi \leqslant \frac { 2 \sqrt { 7 } + 1 } { 9 } , } \\ { \frac { 7 } { 9 ( 1 - \xi ) } , } & { \frac { 2 \sqrt { 7 } + 1 } { 9 } \leqslant \xi \leqslant \frac { \sqrt { 7 } + 2 } { 6 } , } \\ { \frac { 1 2 \xi ^ { 2 } - 3 } { 9 ( 1 - \xi ) } , } & { \frac { \sqrt { 7 } + 2 } { 6 } \leqslant \xi \leqslant \frac { \sqrt { 7 } + 2 } { 6 } , } \end{array} \right. } \end{array}
$$

The graph of $M _ { 1 } ( \xi )$ is shown in Figure 2.1. Observe that $M _ { 1 } ( \xi )$ in this case is neither convex nor monotone increasing.

A detailed characterization of $N _ { \pmb { k } } ( \pmb { \xi } )$ is found in Voronovskaja [1], where implicitly, much information about $M _ { k } ( \xi )$ can also be found. We next present Duffin and Schaeffer's improved version of V. A. Markov's theorem, which, surprisingly, requires an excursion into the complex plane and the elementary theory of analytic functions. The following lemmas are needed.

Lemma 2.7.2 (Rouché's Theorem). $\mathbf { I f } f ( z )$ and $g ( z )$ are analytic inside and on a simple closed Jordan curve, $c _ { i }$ and $| g ( z ) | < | f ( z ) |$ for all $z$ on $c$ then $g ( z ) + f ( z )$ and $f ( z )$ have the same number of zeros inside $\pmb { C } .$

![](images/b7245f3508466c134f3fbcc06702dcb8adc71db1240d882c972d14d4a9c2e569.jpg)  
Figure 2.1

Proof. See any text on complex function theory; e.g., Titchmarsh [1].

Lemma 2.7.3. If all the zeros of $p ( z ) \in \mathcal { P } _ { n }$ are in the half-plane $x < a ,$ , then all the zeros of ${ \pmb p } ^ { \prime } ( z )$ are in $x < a$

Proof. Suppose that $\mathbb { R } \in w \geqslant a ;$ then $p ( w ) \neq 0 .$ Let $z _ { 1 } , \ldots , z _ { n }$ be the zeros of $\pmb { p } ;$ ,each zero appearing in the sequence according to its multiplicity. Each of the complex numbers $z _ { i } - w$ satisfies

$$
\frac { \pi } { 2 } < \arg { ( z _ { i } - w ) } < \frac { 3 \pi } { 2 } ,
$$

and the same is true of the complex numbers $( \bar { z } _ { i } - \bar { w } ) ^ { - 1 } = | z _ { i } - w | ^ { - 2 } ( z _ { i } - w ) ,$ but then

$$
{ \biggl [ } - { \frac { p ^ { \prime } ( w ) } { p ( w ) } } { \biggr ] } = \sum _ { i = 1 } ^ { n } { \frac { 1 } { z _ { i } - w } } \neq 0 ,
$$

since the sum of complex numbers,all of which lie in $\tt R e z < 0$ ,must also lie in $R e z < 0$ Thus $\begin{array} { r } { p ^ { \prime } ( w ) \neq 0 } \end{array}$ ,and the lemma is proved.(This is a special case of the Gauss-Lucas theorem: the zeros of $\pmb { p } ^ { \prime }$ lie in the convex hull of the zeros of $\pmb { p }$ ） ■

Lemma 2.7.4. Let $a _ { 1 } , \ldots , a _ { 2 n }$ be nonnegative numbers and $a _ { 1 } ^ { \prime } , \ldots , a _ { 2 n } ^ { \prime }$ a rearrangement of these according to size so that $a _ { 1 } ^ { \prime } \geqslant a _ { 2 } ^ { \prime } \geqslant \cdots \geqslant a _ { 2 n } ^ { \prime } \geqslant 0 .$ Then for $t \geqslant 0$

$$
\begin{array} { r l r } & { } & { ( a _ { 1 } a _ { 2 } + t ) ( a _ { 3 } a _ { 4 } + t ) \cdots ( a _ { 2 n - 1 } a _ { 2 n } + t ) } \\ & { } & { \qquad \leqslant ( a _ { 1 } ^ { \prime } a _ { 2 } ^ { \prime } + t ) ( a _ { 3 } ^ { \prime } a _ { 4 } ^ { \prime } + t ) \cdots ( a _ { 2 n - 1 } ^ { \prime } a _ { 2 n } ^ { \prime } + t ) . } \end{array}
$$

Proof.The lemma is certainly true if $\pmb { n = 1 }$ . Suppose that it is true for ${ \pmb n } - 1$ Let

$$
a _ { 1 } ^ { \prime } = a _ { i } , \qquad a _ { 2 } ^ { \prime } = a _ { j } .
$$

Case $\imath$ If $_ i$ is odd and $j = i + 1$ or $_ i$ is even and $j = i - 1$ ，then either $a _ { 1 } ^ { \prime } a _ { 2 } ^ { \prime } + t = a _ { i } a _ { i + 1 } + t$ or $a _ { 1 } ^ { \prime } a _ { 2 } ^ { \prime } + t = a _ { i - 1 } a _ { i } + t .$ Either equality together with the inductive hypothesis applied to the set ${ \pmb a } _ { { \pmb k } }$ ， $k = 1 .$ ，...，2n, $k \neq i , j ,$ establishes (2.88).

Case 2. i and $j$ are not as in Case 1. Therefore, if we put

$$
i ^ { \prime } = \{ { \begin{array} { l l } { i - 1 , \quad } & { i \ \mathrm { e v e n } } \\ { i + 1 , \quad } & { i \ \mathrm { o d d } } \end{array} } , \quad \quad j ^ { \prime } = \{ { \begin{array} { l l } { j - 1 , \quad } & { j \ \mathrm { e v e n } , } \\ { j + 1 , \quad } & { j \ \mathrm { o d d } , } \end{array} } 
$$

no two of the indices $i , i ^ { \prime } , j ,$ and $j ^ { \prime }$ coincide and $( a _ { i } a _ { i ^ { \prime } } + t )$ and $( a _ { j } a _ { j ^ { \prime } } + t )$ both appear among the factors on the left-hand side of (2.8). However,

$$
( a _ { 1 } ^ { \prime } a _ { 2 } ^ { \prime } + t ) ( a _ { i ^ { \prime } } a _ { j ^ { \prime } } + t ) - ( a _ { i } a _ { i ^ { \prime } } + t ) ( a _ { j } a _ { j ^ { \prime } } + t ) = t ( a _ { 1 } ^ { \prime } - a _ { j } ^ { \prime } ) ( a _ { 2 } ^ { \prime } - a _ { i ^ { \prime } } ) \geqslant 0 .
$$

Thus, if $( a _ { i } a _ { i ^ { \prime } } + \dot { t } ) ( a _ { j } a _ { j ^ { \prime } } + t )$ is replaced by $( a _ { 1 } ^ { \prime } a _ { 2 } ^ { \prime } + t ) ( a _ { i ^ { \prime } } a _ { j ^ { \prime } } + t ) ,$ the product on the left-hand side of (2.88) does not decrease. By the inductive hypothesis the lemma holds for the set of $a _ { k } , k = 1 , \ldots , 2 n , k \neq i , j$ ；hence the modified lefthand side does not exceed the right-hand side and (2.88) is established.■

Lemma 2.7.5. For each $\pmb { n } \geqslant \mathbf { 0 }$

$$
\vert T _ { n } ( x + i y ) \vert \leqslant \vert T _ { n } ( 1 + i y ) \vert , \qquad - 1 \leqslant x \leqslant 1 , - \infty < y < \infty .
$$

Proof. Putting $\mathbf { \boldsymbol { x } } = \cos { \theta }$ ,we have

$$
\begin{array} { l } { \displaystyle | T _ { n } ( x + i y ) | ^ { 2 } = 4 ^ { n - 1 } \frac { x } { j - 1 } | x + i y - \cos \theta _ { j } | ^ { 2 } } \\ { \displaystyle = 4 ^ { n - 1 } \frac { { \cal M } } { j - 1 } [ ( \cos \theta - \cos \theta _ { j } ) ^ { 2 } + y ^ { 2 } ] } \\ { \displaystyle = 4 ^ { n - 1 } \frac { { \cal M } } { j - 1 } [ 4 \sin ^ { 2 } \frac { \theta - \theta _ { j } } { 2 } \sin ^ { 2 } \frac { \theta + \theta _ { j } } { 2 } + y ^ { 2 } ] } \\ { \displaystyle = 4 ^ { n - 1 } \frac { { \cal M } } { j - 1 } [ ( 1 - \cos ( \theta - \theta _ { j } ) ) ( 1 - \cos ( \theta + \theta _ { j } ) ) + y ^ { 2 } ] } \\ { \displaystyle = \frac { 1 } { 4 } \frac { \cal M } { j - 1 } [ \epsilon ^ { \mu } - \epsilon ^ { \omega _ { l } } ] ^ { 2 } ( \epsilon ^ { \omega } - \epsilon ^ { - i \theta _ { j } } ] ^ { 2 } + 3 y ^ { 2 } ] , } \end{array}
$$

where the last step follows from the law of cosines. Let $a _ { 2 j - 1 } = | e ^ { i \theta } - e ^ { i \theta _ { j } } | ^ { 2 }$ and $a _ { 2 j } = \vert e ^ { i \theta } - e ^ { - i \theta _ { j } } \vert ^ { 2 } , j = 1 , . . . , n ,$ so that the sequence $a _ { 1 } , \ : a _ { 2 } , \ldots , \ : a _ { 2 n }$ consists of the squares of the distance from a point of the unit circle, $e ^ { i \theta }$ ,to the vertices of a regular $_ { 2 n }$ -gon inscribed in the unit circle.If $\pmb \theta$ is increased or decreased by ${ \pmb { \pi } } / { \pmb { n } }$ ， the resulting sequence of squares of distances is a rearrangement of $a _ { 1 } , \ldots , a _ { 2 n }$ Therefore, if $\varphi = \theta \pm ( k \pi ) / n$ satisfies

$$
| \varphi | \leqslant \frac { \pi } { 2 n }
$$

and $b _ { 2 j - 1 } = | e ^ { i \varphi } - e ^ { i \theta _ { j } } | ^ { 2 }$ ， $b _ { 2 j } = | e ^ { i \varphi } - e ^ { - i \theta _ { j } } | ^ { 2 } , j = 1 , \dots , n , b _ { 1 } , b _ { 2 } , \dots , b _ { 2 n }$ is a rearrangement of $a _ { 1 } , \ldots , a _ { 2 n } ;$ moreover, if $\varphi \geqslant 0$ ， $0 \leqslant b _ { 1 } \leqslant b _ { 2 } \leqslant \cdots \leqslant b _ { 2 n } ,$ whereas, if $\varphi \leqslant 0$ ， $0 \leqslant b _ { 2 } \leqslant b _ { 1 } \leqslant b _ { 4 } \leqslant b _ { 3 } \leqslant \cdots \leqslant b _ { 2 n } \leqslant b _ { 2 n - 1 }$ . In either case Lemma 2.7.4 yields

$$
\begin{array} { c } { { | T _ { n } ( x + i y ) | ^ { 2 } \leqslant \frac { 1 } { 4 } \displaystyle \prod _ { j = 1 } ^ { n } ~ [ | e ^ { i \varphi } - e ^ { i \theta _ { j } } | ^ { 2 } | e ^ { i \varphi } - e ^ { - i \theta _ { j } } | ^ { 2 } + 4 y ^ { 2 } ] } } \\ { { = | T _ { n } ( \bar { x } + i y ) ^ { 2 } | , } } \end{array}
$$

where ${ \bar { \boldsymbol { x } } } = \cos \varphi$ . Since $\bar { \boldsymbol { x } } +$ iy lies in the strip $\xi _ { 1 } \leqslant x \leqslant 1 ,$ ，

$$
| \bar { x } + i y - \xi _ { j } | \leqslant | 1 + i y - \xi _ { j } | , \qquad j = 1 , \ldots , n
$$

![](images/b9ea77037c12da9429c33e7717bd26a0165f23a6e7fa0603b05200db724a0e4f.jpg)  
Figure 2.2

(see Figure 2.2); hence

$$
| T _ { n } ( \bar { x } + i y ) | \leqslant | T _ { n } ( 1 + i y ) | ,
$$

and, in view of (2.89), the lemma is proved.

The key to the proof of the Duffin-Schaeffer-Markov theorem is the following interesting result.

Theorem 2.23. Let $x _ { 1 } < x _ { 2 } < \cdots < x _ { m } < 1$ be the zeros of $\pmb { v } \in \mathcal { P } _ { m }$ and suppose that

$$
| v ( x + i y ) | \leqslant | v ( 1 + i y ) | , \qquad - 1 \leqslant x \leqslant 1 , - \infty < y < \infty .
$$

f $q \in \mathcal { P } _ { m }$ satisfies

$$
| q ^ { \prime } ( x _ { i } ) | \leqslant | v ^ { \prime } ( x _ { i } ) | , \qquad i = 1 , \ldots , m ,
$$

then

$$
| q ^ { \prime } ( x + i y ) | \leqslant | v ^ { \prime } ( 1 + i y ) | , \qquad - 1 \leqslant x \leqslant 1 , \qquad - \infty < y < \infty .
$$

Proof. Let $\xi + i \eta$ be a fixed point such that $- 1 \leqslant \xi \leqslant 1$ If $v ( x ) =$ $c ( { \pmb x } - { \pmb x } _ { 1 } ) \cdots ( { \pmb x } - { \pmb x } _ { m } ) ,$ let $r ( x ) = c ( x - u _ { 1 } ) \cdot \cdot \cdot ( x - u _ { m } ) ,$ where the zeros of $r$ are obtained from those of $\pmb { v }$ by reflecting about $\xi$ those zeros of $\pmb { v }$ that lie to the

right of $\xi ;$ i.e.,

$$
\begin{array} { l l } { { u _ { i } = x _ { i } , } } & { { \quad x _ { i } \leqslant \xi , } } \\ { { u _ { i } = 2 \xi - x _ { i } , } } & { { \quad x _ { i } > \xi . } } \end{array}
$$

Clearly, every point $z = \xi + i y$ is equidistant from ${ \pmb u } _ { i }$ and $x _ { i } , i = 1 , \ldots , m _ { i }$ ie., $| z - u _ { i } | = | z - x _ { i } | ;$ hence

$$
| r ( \xi + i y ) | = | v ( \xi + i y ) | .
$$

We claim next that $| r ^ { \prime } ( \xi + i \eta ) | \geqslant | q ^ { \prime } ( \xi + i \eta ) |$ . Put $\zeta = \xi + i \eta$ . The Lagrange interpolation formula with nodes at the $x _ { i }$ gives

$$
q ^ { \prime } ( \zeta ) = v ( \zeta ) \sum _ { i = 1 } ^ { m } \frac { q ^ { \prime } ( x _ { i } ) } { v ^ { \prime } ( x _ { i } ) } \frac { 1 } { \zeta - x _ { i } } .
$$

In view of (2.91), $q ^ { \prime } ( x _ { i } ) / v ^ { \prime } ( x _ { i } ) = \delta _ { i }$ with $| \delta _ { i } | \leqslant 1 , i = 1 , \ldots , m$ Thus, if $\eta \neq 0 ,$

$$
\begin{array} { l } { | q ^ { \prime } ( \zeta ) = | v ( \zeta ) | \cdot \left| \displaystyle \sum _ { i = 1 } ^ { m } \frac { \delta _ { i } } { \xi + i \eta - x _ { i } } \right| } \\ { = | v ( \zeta ) | \left| \displaystyle \sum _ { i = 1 } ^ { m } \frac { \delta _ { i } ( \xi - x _ { i } ) } { ( \xi - x _ { i } ) ^ { 2 } + \eta ^ { 2 } } - i \displaystyle \sum _ { i = 1 } ^ { m } \frac { \delta _ { i } \eta } { ( \xi - x _ { i } ) ^ { 2 } + \eta ^ { 2 } } \right| } \\ { = | v ( \zeta ) | | A - i B | , } \end{array}
$$

where

$$
A = \sum _ { i = 1 } ^ { m } \frac { \delta _ { i } ( \xi - x _ { i } ) } { ( \xi - x _ { i } ) ^ { 2 } + \eta ^ { 2 } } , \qquad B = \sum _ { i = 1 } ^ { m } \frac { \delta _ { i } \eta } { ( \xi - x _ { i } ) ^ { 2 } + \eta ^ { 2 } } .
$$

By construction $| \xi - x _ { i } | = \xi - u _ { i }$ ；hence $( \xi - x _ { i } ) ^ { 2 } = ( \xi - u _ { i } ) ^ { 2 }$ ,18i(5-xi) $\leqslant \xi - u _ { i }$ ,and therefore

$$
| A | \leqslant \sum _ { i = 1 } ^ { m } { \frac { \xi - u _ { i } } { ( \xi - u _ { i } ) ^ { 2 } + \eta ^ { 2 } } } = \alpha , \qquad | B | \leqslant \sum _ { i = 1 } ^ { m } { \frac { | \eta | } { ( \xi - u _ { i } ) ^ { 2 } + \eta ^ { 2 } } } = \beta
$$

and $| A - i B | = ( A ^ { 2 } + B ^ { 2 } ) ^ { 1 / 2 } \leqslant ( \alpha ^ { 2 } + \beta ^ { 2 } ) ^ { 1 / 2 } = | \alpha \pm i \beta |$ . By choosing the plus sign if $\pmb { \eta } < \mathbf { 0 }$ and the minus sign if $\pmb { \eta } > \mathbf { 0 }$ we obtain

$$
\begin{array} { l } { | q ^ { \prime } ( \zeta ) \leqslant | v ( \zeta ) | \cdot \left| \displaystyle \sum _ { i = 1 } ^ { m } \frac { ( \zeta - u _ { i } ) - i \eta } { ( \zeta - u _ { i } ) ^ { 2 } + \eta ^ { 2 } } \right| = | v ( \zeta ) | \left| \displaystyle \sum _ { i = 1 } ^ { m } \frac { 1 } { \zeta - u _ { i } } \right| } \\ { = | v ( \zeta ) | \displaystyle \frac { | r ^ { \prime } ( \zeta ) | } { ( r ( \zeta ) | } = | r ^ { \prime } ( \zeta ) | , } \end{array}
$$

the last equality because of (2.93), thus establishing our claim for $\pmb { \eta } \neq \mathbf { 0 }$ The case of $\pmb { \eta } = \mathbf { 0 }$ now follows by continuity.

Let w be any complex number satisfying

$$
| w | < 1 .
$$

Put $s ( z ) = v ( z ) - w r ( z + \xi - 1 )$ Let $\Gamma _ { R }$ be the simple closed curve consisting of the semicircle $C _ { R } \colon | z - 1 | = R \colon$ $\pmb { \mathrm { R e } } z \geqslant 1$ , and the line segment $D _ { R }$ joining $1 + i R$ and $1 - i R$ If $ { \boldsymbol { z } } \in D _ { R }$ ,(2.94), (2.93),and (2.90) imply that

$$
| w r ( z + \xi - 1 ) | < | r ( \xi + i y ) | = | v ( \xi + i y ) | \leqslant | v ( 1 + i y ) | = | v ( z ) | .
$$

Also on $C _ { R }$ ,for $\pmb R$ sufficiently large,

$$
| w r ( z + \xi - 1 ) | < | v ( z ) | ,
$$

since $\boldsymbol { r }$ and $\pmb { v }$ have the same leading coefficient and $| w | < 1 ,$ Thus by Rouche's theorem (Lemma 2.7.2), $s ( z )$ has the same number of zeros as $v ( z )$ inside $\Gamma _ { R }$ ， i.e., none. Since $\pmb R$ is arbitrary, we see that $s ( z )$ has no zero in $x \geqslant 1$ ; hence by Lemma 2.7.3 neither has $s ^ { \prime } ( z )$ In particular, $s ^ { \prime } ( z ) \neq 0$ at $z = 1 + i \eta$ ,i.e.,

$$
v ^ { \prime } ( 1 + i \eta ) - w r ^ { \prime } ( \xi + i \eta ) \neq 0
$$

for all $| w | < 1$ If $| v ^ { \prime } ( 1 + i \eta ) | < | r ^ { \prime } ( \xi + i \eta ) | .$ ，then (2.95) is violated for $w = v ^ { \prime } ( 1 + i \eta ) / r ^ { \prime } ( \xi + i \eta )$ Hence

$$
| v ^ { \prime } ( 1 + i \eta ) | \geqslant | r ^ { \prime } ( \xi + i \eta ) | \geqslant | q ^ { \prime } ( \xi + i \eta ) | . \quad =
$$

Corollary 2.23.1. For $k = 1 , 2 , . . . , n$

$$
\vert T _ { n } ^ { ( k ) } ( x + i y ) \vert \leqslant \vert T _ { n } ^ { ( k ) } ( 1 + i y ) \vert , \qquad - 1 \leqslant x \leqslant 1 , \qquad - \infty < y < \infty .
$$

Proof. When $k = 1$ ,(2.96) follows from Lemma 2.7.5 and the theorem with $v = q = T _ { n }$ . If (2.96) holds for $k - 1$ ,then it holds for $k$ by the theorem with $v = q = T _ { n } ^ { ( k - 1 ) }$

Theorem 2.24 (Dufin and Schaefer [1]). If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ and

$$
| p ( \eta _ { i } ) | \leqslant 1 , \qquad i = 0 , \ldots , n ,
$$

then for $- 1 \leqslant x \leqslant 1$ and $1 \leqslant k \leqslant n$

$$
| p ^ { ( k ) } ( x ) | \leqslant T _ { n } ^ { ( k ) } ( 1 ) = { \frac { n ^ { 2 } ( n ^ { 2 } - 1 ^ { 2 } ) ( n ^ { 2 } - 2 ^ { 2 } ) \cdots ( n ^ { 2 } - ( k - 1 ) ^ { 2 } ) } { 1 . 3 . 5 \cdots ( 2 k - 1 ) } } ,
$$

with equality holding only if $p = \pm T _ { n }$ and $x = \pm 1$

Proof. Suppose ${ \pmb { p } } \in C _ { \pmb { n } }$ and $p \neq \pm T _ { n }$ .Then, in view of (2.71), there exists a constant $c > 1$ such that

$$
| c p ^ { ( k ) } ( u _ { i } ) | \leqslant | T _ { n } ^ { ( k ) } ( u _ { i } ) | , \qquad i = 1 , \ldots , n - ( k - 1 ) ,
$$

where the $u _ { i } , i = 1 , \ldots , n - ( k - 1 ) ,$ , are the zeros of $T _ { n } ^ { ( k - 1 ) }$ . We now apply Theorem 2.23 with $m = n - ( k - 1 ) , \ u _ { i } = x _ { i } , \ v = T _ { n } ^ { ( k - 1 ) }$ and $q = c p ^ { ( k - 1 ) }$ Observe that (2.91) holds because of (2.99) and (2.90) is simply (2.96). Thus

$$
c | p ^ { ( k ) } ( x + i y ) | \leqslant | T _ { n } ^ { ( k ) } ( 1 + i y ) | , \qquad - 1 \leqslant x < 1 , \qquad - \infty < y < \infty .
$$

Since $c > 1$ , we have, finally,

$$
\vert p ^ { ( k ) } ( x + i y ) \vert < \vert T _ { n } ^ { ( k ) } ( 1 + i y ) \vert , \qquad - 1 \leqslant x \leqslant 1 , \qquad - \infty < y < \infty .
$$

Choosing $y = 0$ yields

$$
| p ^ { ( k ) } ( x ) | < | T _ { n } ^ { ( k ) } ( 1 ) | = T _ { n } ^ { ( k ) } ( 1 ) .
$$

The observations about equality and the evaluation of $T _ { n } ^ { ( k ) } ( 1 )$ are consequences of Exercises 1.5.35 and 1.5.6.

Remark 1. Note that we have really proved (2.100) which is more general than (2.98).

Remark 2. If $\pmb { p }$ is a polynomial of degree at most $\pmb { n }$ with complex coefficients, which satisfies (2.97), the conclusion of Theorem 2.24 still holds. To show this we note that the $l _ { i } ( x )$ with respect to the points $\pmb { \eta } _ { 0 } , \dots , \pmb { \eta } _ { n }$ are real valued.

$$
| p ^ { ( k ) } ( \xi ) | = \left| \sum _ { i = 0 } ^ { n } p ( \eta _ { i } ) l _ { i } ^ { ( k ) } ( \xi ) \right| \leqslant \sum _ { i = 0 } ^ { n } | l _ { i } ^ { ( k ) } ( \xi ) | = \sum _ { i = 0 } ^ { n } \varepsilon _ { i } ( \xi ) l _ { i } ^ { ( k ) } ( \xi ) .
$$

If

$$
p _ { \xi } ( x ) = \sum _ { i = 0 } ^ { n } \varepsilon _ { i } ( \xi ) l _ { i } ( x ) ,
$$

then $p _ { \xi } \in C _ { n }$ ,since $\varepsilon _ { i } ( \xi ) = \pm 1$ .Thus

$$
| p ^ { ( k ) } ( \xi ) | \leqslant p _ { \xi } ^ { ( k ) } ( \xi ) ,
$$

and the result follows from the theorem aplid to $\pmb { p } _ { \xi }$

Remark 3. Duffin and Schaeffer [1] also show that if $\pmb { { \cal E } }$ is any closed subset of [-1,1] that does not contain one of the points $\eta _ { i } , i = 0 , \ldots , n ,$ there exists $\pmb { p } \in \pmb { \mathcal { P } _ { n } }$ satisfying

$$
| p ( x ) | \leqslant 1 , \qquad x \in E ,
$$

and

$$
| p ^ { ( k ) } ( 1 ) | > T _ { n } ^ { ( k ) } ( 1 ) , \qquad k = 1 , 2 , \ldots , n .
$$

There is an interesting application of Theorem 2.24 to the theory of numerical diferentiation. Suppose that we wish to approximate the derivative $f ^ { ( k ) } ( x )$ for $\boldsymbol { x } \in \boldsymbol { I }$ by $L _ { n } ^ { ( k ) } ( f , X ; x )$ (cf. p. 12), $k = 1 , 2 , \ldots , n .$ How shall we choose $\pmb { X } 2$ The norm of the operator

$$
f \to L _ { n } ^ { ( k ) } ( f )
$$

is

$$
\Lambda _ { n + 1 } ^ { ( k ) } ( X ) = \operatorname* { m a x } _ { \| f \| = 1 } \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | L _ { n } ^ { ( k ) } ( f , X ; x ) | = \operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } \sum _ { j = 1 } ^ { n + 1 } | l _ { j , n + 1 } ^ { ( k ) } ( x ) | .
$$

It therefore seems desirable to choose $\pmb { X }$ so that $\Lambda _ { n + 1 } ^ { ( k ) } ( X )$ is as small as possible.

In the case that $k = 0$ (2.101) is what we called the Lebesgue constant of order $n + 1$ of $\pmb { X }$ 、A set of nodes that minimizes $\Lambda _ { n + 1 } ( X )$ is not known. For $k = 1 , \ldots , n ,$ however,

$$
T _ { n } ^ { ( k ) } ( 1 ) = \Lambda _ { n + 1 } ^ { ( k ) } ( U ) \leqslant \Lambda _ { n + 1 } ^ { ( k ) } ( X ) ,
$$

where $\pmb { U }$ is the array of nodes whose $( n + 1 ) { \mathsf { s t } }$ row is $\eta _ { 0 } ^ { ( n ) } , \ldots , \eta _ { n } ^ { ( n ) }$ . This result is due to Berman [1]. To prove (2.102) we first observe that on the one hand

$$
T _ { n } ^ { ( k ) } ( 1 ) = \bigg | \sum _ { i = 0 } ^ { n } T _ { n } ( x _ { i } ) l _ { i } ^ { ( k ) } ( X ; 1 ) \bigg | \leqslant \sum _ { i = 0 } ^ { n } | l _ { i } ^ { ( k ) } ( X ; 1 ) | \leqslant \Lambda _ { n + 1 } ^ { ( k ) } ( X ) ,
$$

whereas on the other Theorem 2.24 implies that

$$
\sum _ { i = 0 } ^ { n } | l _ { i } ^ { ( k ) } ( U ; x ) | \leqslant T _ { n } ^ { ( k ) } ( 1 ) , \qquad - 1 \leqslant x \leqslant 1 .
$$

# EXERCISES 2.7.1-2.7.14

2.7.1. Let

$$
V = \big \{ p \in \mathcal { P } _ { n } / p ( \pm \xi _ { 1 } ^ { ( n ) } ) = 0 \big \} .
$$

If $\pmb { p } \in { V }$ and

$$
| p ( x _ { i } ) | = \operatorname* { m a x } _ { \substack { - \xi _ { 1 } \leqslant x \leqslant \xi _ { 1 } } } | p ( x ) | , \quad \quad i = 1 , \ldots , n - 1 ,
$$

where $- \xi _ { 1 } \leqslant x _ { 1 } < x _ { 2 } < \dots < x _ { n - 1 } \leqslant \xi _ { 1 }$ ，then $p ( x ) = \pm T _ { n } ( x ) .$

2.7.2. If $p \in V \ [ V$ is defined by (2.103)],

$$
\left| p \left( \cos { \frac { j \pi } { n } } \right) \right| \leqslant 1 , \qquad j = 1 , . . . , n - 1 ,
$$

and $\left| t \right| \geqslant \xi _ { 1 } ^ { ( n ) }$ , then $| p ^ { ( k ) } ( t ) | \leqslant T _ { n } ^ { ( k ) } ( t )$

2.7.3. Give an example of $p \in \mathcal { P } _ { 2 } \ ( p \not = \pm T _ { 2 } )$ for which equality occurs in (2.45) for $j = 1$

2.7.4.Discuss the problem of minimizing $\| { \pmb x } { \pmb p } ^ { \prime } - { \bf 1 } \|$ for $\pmb { p } \in \mathcal { P } _ { n } , \pmb { p } ( 1 ) = 0 ;$ ，the norm being taken on the interval $[ 1 , \alpha ]$

2.7.5. (Lepson [1]) When $\begin{array} { r } { p = T _ { n } } \end{array}$ ,(2.69) becomes

$$
| T _ { n } ^ { \prime } ( x ) | \leqslant { \frac { n } { ( 1 - x ^ { 2 } ) ^ { 1 / 2 } } } , \qquad - 1 < x < 1 .
$$

Show that (2.104) can be improved to

$$
| T _ { n } ^ { \prime } ( x ) | < { \frac { n } { ( 2 x ) ^ { ( n - 1 ) / 3 } } } , 0 < x < { \frac { 1 } { 2 } } , n > 1 .
$$

Hint. Using the 3-term recurrence formula for $S _ { k } ( t ) = U _ { k } ( t / 2 )$ (cf. Exercise 1.5.54), show by mathematical inducation that

$$
| S _ { k } ( t ) | \leqslant t ^ { - k / 3 } , \qquad 0 < t < 1 .
$$

For some other improvements on (2.104) see Askey [3].

2.7.6. Show that there exists $p \in C _ { n } , p \notin B _ { n } , n > 1 .$

2.7.7.With the notation used in Theorem 2.21 and $x _ { i } = \eta _ { i }$ show that each interval $( z _ { n , j } , z _ { 0 , j - 1 } ) , j = 2 , \ldots , n - k ; ( z _ { n , 1 } , 1 )$ and $( - 1 , z _ { 0 , n - k } )$ contains a zero of $T _ { n } ^ { ( k - 1 ) } ( x ) .$

2.7.8. Show that if $p \in C _ { n }$ ,then

$$
| p ^ { \prime } ( x ) | \leqslant T _ { n } ^ { \prime } ( x )
$$

for $x \geqslant \beta$ ，where $\xi _ { 1 } = \cos { ( \pi / 2 n ) }$ and

$$
\beta = \xi _ { 1 } - \frac { 1 - \xi _ { 1 } ^ { 2 } } { \xi _ { 1 } + n ^ { 2 } ( 1 - \xi _ { 1 } ^ { 2 } ) } .
$$

2.7.9.(Ehlich and Zeller [1]) Suppose that $- 1 = x _ { 1 } < x _ { 2 } < \cdots < x _ { m } = 1$ and $d _ { m } = \operatorname { m a x } _ { i = 1 , \ldots , m - 1 } \left( x _ { i + 1 } - x _ { 1 } \right)$ f $\pmb { p } \in \pmb { \mathcal { P } _ { n } }$ and $| p ( x _ { i } ) | \leqslant 1 , i = 1 , \ldots , m ,$ then

$$
\| p \| \leqslant { \frac { 1 } { 1 - ( d _ { m } ^ { 2 } / 2 4 ) n ^ { 2 } ( n ^ { 2 } - 1 ) } } .
$$

Hint. If $\| p \| = | p ( t ) | , - 1 < t < 1$ and $\boldsymbol { x } _ { j }$ is the $\pmb { x _ { i } }$ closest to $\pmb { t } ,$ ，then

$$
p ( x _ { j } ) = p ( t ) + { \frac { ( x _ { j } - t ) ^ { 2 } } { 2 } } p ^ { \prime \prime } ( \theta ) ,
$$

where $\pmb \theta$ is in $\pmb { I } .$ Note that $| x _ { j } - t | \leqslant d _ { m } / 2$ and apply Theorem 2.24.

Suppose a function, $f ( x ) ,$ is sampled at points $x _ { i } , i = 1 , . . . , n + 1$ of I with error $\pmb { \mathscr { E } _ { i } }$ at $\boldsymbol { x } _ { i }$ An estimate for $f ( t ) , t > 1$ ，can be obtained by evaluating the interpolating polynomial $\pmb { p } \in \mathcal { P } _ { \pmb { \eta } }$ ,which satisfies $p ( { x } _ { i } ) = f ( { x } _ { i } ) + \varepsilon _ { i }$ at $\pmb { t . }$ f

$$
\varepsilon = \operatorname* { m a x } | \varepsilon _ { i } | , \quad \quad i = 1 , \dots , n + 1 ,
$$

then the error in the extrapolation, $p ( t )$ ,due to the $\pmb { \mathscr { E } } _ { i }$ does not exceed

$$
\begin{array} { r } { \varepsilon \sum _ { i = 1 } ^ { n + 1 } | l _ { i } ( t ) | = \varepsilon \lambda _ { r + 1 } ( X ; t ) . } \end{array}
$$

2.7.10. Show that $\lambda _ { n + 1 } ( X ; t ) \geqslant \lambda _ { n + 1 } ( U ; t ) ,$ with equality only for $\ b { \ b { x } } = \ b { U }$

Hint. If $- 1 \leqslant x _ { n + 1 } < x _ { n } < \cdots < x _ { 1 } \leqslant 1$ then

$$
\lambda _ { n + 1 } ( U ; t ) = | T _ { n } ( t ) | \leqslant \lambda _ { n + 1 } ( X ; t ) .
$$

2.7.11. If $- 1 \leqslant x _ { n + 1 } < x _ { n } < \cdots < x _ { 1 } \leqslant 1 ,$

$$
V ( X ) = \{ p \in { \mathcal P } _ { n } / | p ( x _ { i } ) | \leqslant 1 , i = 1 , . . . , n + 1 \} ,
$$

and for $t \geqslant 1 , 0 \leqslant k \leqslant n$

$$
\operatorname* { m i n } _ { x } \operatorname* { m a x } _ { p \in V ( X ) } | p ^ { ( k ) } ( t ) | = m ,
$$

then show that the minimal $\pmb { X }$ is $\pmb { U }$ and $m = T _ { n } ^ { ( k ) } ( t )$

2.7.12. (Cavaretta [1],Matorin [1]) Let $p _ { n } ( x ) = T _ { n } ( x - 1 ) ,$ the Chebyshev polynomial relative to $[ 0 , 2 ] ; p _ { n } ^ { ( n ) } ( x ) = n ! 2 ^ { n - 1 }$ .Let $f$ be an $\pmb { n }$ times differentiable function on $[ 0 , \infty )$ that satisfies $\| f \| \leqslant 1$ and $\| f ^ { ( n ) } \| \leqslant n ! 2 ^ { n - 1 }$ ,where, if $\pmb { \mathscr { g } }$ is defined on $[ 0 , \infty )$ we put

$$
\| g \| = \operatorname* { s u p } _ { 0 \leqslant x < \infty } | g ( x ) |
$$

(this notation is used in this exercise only). Show that

$$
\| f ^ { ( j ) } \| \leqslant p _ { n } ^ { ( j ) } ( 2 ) = T _ { n } ^ { ( j ) } ( 1 ) , \qquad j = 1 , \ldots , n - 1 .
$$

Hint. If (2.105) does not hold for some $j$ and $f ,$ there exists t $\cdot , 0 \leqslant t < \infty$ , and ${ \pmb a } > 1$ such that $f ^ { ( j ) } ( t ) = a p _ { n } ^ { ( j ) } ( 0 ) .$

Consider $h ( x ) = p _ { n } ( x ) - a ^ { - 1 } f ( x + t ) ; h$ has n zeros in [O,2], hence by Rolles theorem $\pmb { h } ^ { ( i ) }$ has ${ \pmb n } - i$ zeros in (0,2).

2.7.13. Show that the bound in (2.105) is sharp for $n = 2 , 3$

Hint. Do some appropriate surgery on ${ \pmb p } _ { 2 }$ and extend it periodically.

2.7.14. Show that if $\pmb { p } \in \mathcal { P } _ { { \pmb { n } } - 1 }$ satisfies $( 1 - x ^ { 2 } ) ^ { 1 / 2 } | p ( x ) | \leqslant 1 ,$ $- 1 < x < 1$ then $| p ( x ) | \leqslant n$ for $x \in { I } .$

Hint. If $| x | \leqslant \xi _ { 1 } ^ { ( n ) }$ then $( 1 - x ^ { 2 } ) ^ { 1 / 2 } \geqslant 1 / n .$ If $| x | > \zeta _ { 1 } ^ { ( n ) }$ repeat the discussion following (2.75) with $\pmb { p }$ in place of $\pmb { p } ^ { \prime }$ ,and obvious appropriate changes.

# 2.8. Additional Extremal Problems

We wish to present next some additional examples of extremal properties of the Chebyshev polynomials,and related material, without relying on the methodology of Theorem 2.16.

1.More About the Bernstein and Markov Inequalities. In Remark 2 of Section 2.7.4, we gave a complex analog of Bernstein's inequality. An elegant and simple method for obtaining this and other inequalities for polynomials in the complex plane is due to de Bruijn [1].

1.1. Polynomial Inequalities in the Complex Plane. We begin with a complex analog of Rolle's theorem, the Gauss-Lucas theorem, of which Lemma 2.7.3 is a special case.

Theorem 2.25. If

$$
p ( z ) = c ( z - z _ { 1 } ) \cdots ( z - z _ { n } ) ,
$$

then the zeros of $p ^ { \prime } ( z )$ are in the convex hull of $\left\{ z _ { 1 } , \ldots , z _ { n } \right\}$

Proof. Suppose that $p ^ { \prime } ( \zeta ) = 0$ and $\zeta \neq z _ { j } , j = 1 , . . . , n ,$ then

$$
\frac { p ^ { \prime } ( \zeta ) } { p ( \zeta ) } = \sum \sp n _ { j = 1 } \frac { 1 } { \zeta - z _ { j } } = 0 .
$$

Thus

$$
0 = \sum _ { j = 1 } ^ { n } { \frac { 1 } { \zeta - z _ { j } } } = \sum _ { j = 1 } ^ { n } { \frac { \zeta - z _ { j } } { | \zeta - z _ { j } | ^ { 2 } } } ,
$$

and there exist nonnegative numbers,

$$
\lambda _ { j } = \frac { \displaystyle { \frac { 1 } { | \zeta - z _ { j } | ^ { 2 } } } } { \displaystyle { \sum _ { j = 1 } ^ { n } \frac { 1 } { | \zeta - z _ { j } | ^ { 2 } } } } > 0 , ~ j = 1 , \ldots , n
$$

satisfying

$$
\sum _ { j = 1 } ^ { n } \lambda _ { j } = 1 \qquad \mathrm { a n d } \qquad \zeta = \sum _ { j = 1 } ^ { n } \lambda _ { j } z _ { j } .
$$

$\zeta$ is therefore in (the interior of) the convex hull of $\left\{ z _ { 1 } , \ldots , z _ { n } \right\}$ . (Recall Definitions 2.2 and 2.3). If $p ^ { \prime } ( z _ { j } ) = 0$ the conclusion of the theorem is obviously true.

We next obtain a generalization of the complex Bernstein inequality.

Theorem 2.26 (de Bruijn [1]).Let $\pmb R$ be a convex region in the plane, and $\pmb { B }$ its boundary. Suppose $\pmb { p } \in \mathcal { P } _ { m }$ and $\ b { q } \in \mathcal { P } _ { n }$ ,with $m \leqslant n ,$ ,and the zeros of $\pmb q$ are all in $R \cup B ,$ If $| p ( z ) | \leqslant | q ( z ) | , z \in B ,$ then $| p ^ { \prime } ( z ) | \leqslant | q ^ { \prime } ( z ) | , z \in B .$

Proof. Let $E$ be the complement of $R \cup B$ in $\hat { \mathbb { C } }$ (the extended complex plane, i.e., $\mathbb { C }$ with the “point at infinity”adjoined to it). Since $\pmb q$ has no zeros in $\pmb { { \cal E } }$ and the degree of $\pmb { p }$ does not exceed the degree of ${ \pmb q } , { \pmb p } / { \pmb q }$ is analytic in $\pmb { { \cal E } }$ and the maximum principle implies that $| p ( z ) | \leqslant | q ( z ) | .$ ， $z \in B \cup E$ since $| p ( z ) | \leqslant$ $| q ( z ) | , z \in B .$ Thus,if $| \zeta | > 1$ the zeros of the polynomial $\pmb { p } ( z ) - \zeta \pmb { q } ( z )$ are all in $\pmb R$ But the same must be true of $p ^ { \prime } ( z ) - \zeta q ^ { \prime } ( z )$ in view of the convexity of $\pmb R$ and Theorem 2.25,and the proof is complete.

In particular, if $\pmb R$ is $| z | < 1$ , so that $\pmb { B }$ ${ \mathfrak { i } } { \mathfrak { s } } \left| z \right| = 1 , m = n$ and $q ( z ) = z ^ { n }$ then we again obtain the complex analog of Bernstein's inequality: If $p \in \mathcal { P } _ { n } , | p ( z ) | \leqslant 1$ for $| z | \leqslant 1$ ,then $| p ^ { \prime } ( z ) | \leqslant n$ for $| z | \leqslant 1$

We need next a useful result of Szego.

Definition 2.5. A set in $\hat { \mathbb { C } }$ is called $^ { a }$ "circular” domain if it is the image of $| z | < 1$ or $| z | \leqslant 1$ under a linear fractional transformation,

$$
z  { \frac { a z + b } { c z + d } } .
$$

For example, $| z | < 1 , | z | \geqslant 1$ Re $z \leqslant a$ are “circular” domains.

Theorem 2.27 (Szeg [3]). Let $c$ be a"circular” domain in $\hat { \mathbb { C } } .$ If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ has no zeros in ( $\gamma ( z = \infty$ is a zero of $p ( z )$ if the coefficient of $z ^ { n }$ is zero) and if $\zeta , z$ are points of $c$ then

$$
( \zeta - z ) p ^ { \prime } ( z ) + n p ( z ) \neq 0 .
$$

(If $\zeta = \infty$ ,(2.106) is to be replaced by $p ^ { \prime } ( z ) \neq 0 .$ ）

Proof. Since $p ( z ) \neq 0$ it suffices to show that

$$
n + ( \zeta - z ) { \frac { p ^ { \prime } ( z ) } { p ( z ) } } \neq 0 .
$$

Let $z _ { 1 } , \ldots , z _ { n }$ be the zeros of $\pmb { p }$ then

$$
n + ( \zeta - z ) \frac { p ^ { \prime } ( z ) } { p ( z ) } = n + \sum _ { j = 1 } ^ { n } \frac { \zeta - z } { z - z _ { j } } = \sum _ { j = 1 } ^ { n } \frac { \zeta - \zeta _ { j } } { z - z _ { j } } .
$$

Consider the linear fractional transformation

$$
W ( w ) = \frac { \zeta - w } { z - w } .
$$

(f $\zeta = \infty$ ， we put $W ( w ) = 1 / ( z - w ) . ) \ K .$ ，the complement of $c$ in ${ \hat { \mathbb { C } } } ,$ is a "circular” domain as is $K ^ { \prime } = W ( K )$ Since neither $\zeta$ nor $z$ is in $\pmb { K }$ we may conclude that neither O nor $\infty$ is in $\kappa ^ { \prime }$ .Thus $\pmb { K } ^ { \prime }$ is a disk which does not contain the origin.But

$$
\frac { \zeta - z _ { j } } { z - z _ { j } } \in K ^ { \prime } ,
$$

hence, since $\pmb { K } ^ { \prime }$ is surely convex

$$
{ \frac { 1 } { n } } \sum _ { j = 1 } ^ { n } { \frac { \zeta - z _ { j } } { z - z _ { j } } } \in K ^ { \prime } ,
$$

and so

$$
\sum _ { j = 1 } ^ { n } { \frac { \zeta - z _ { j } } { z - z _ { j } } } \neq 0 .
$$

Corollary 2.27.1 (de Bruijn [1]). Let $c$ be a“circular” domain in the $\pmb { z }$ -plane and S an arbitrary point set in the $\pmb { w }$ -plane. If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ satisfies $p ( z ) = w \in S$ for

any $z \in C$ ,then for any $z , \zeta \in C$ we have

$$
{ \frac { \zeta } { n } } p ^ { \prime } ( z ) + p ( z ) - { \frac { z p ^ { \prime } ( z ) } { n } } \epsilon S .
$$

Proof. Suppose the complex number $\lambda$ is not in S.Then $p ( z ) \neq \lambda$ for $z \in C$ The polynomial $p ( z ) - \lambda$ satisfies the hypotheses of the theorem and so

$$
( \zeta - z ) p ^ { \prime } ( z ) + n p ( z ) \neq n \lambda
$$

for $z , \zeta \in C$ and any $\lambda$ not in S, thus proving (2.107).

Equation (2.107) can be used to give strikingly simple proofs of polynomial inequalities of the Bernstein variety. We give two examples.

Example 1 (Erdos-Lax; cf. Lax [1]). If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ ， $| p ( z ) | \leqslant 1$ for $| z | \leqslant 1$ and $p ( z )$ has no zeros in $| z | \leqslant 1$ ,then $| p ^ { \prime } ( z ) | \leqslant n / 2$ for $| z | \leqslant 1$

Proof. Let $c$ be the open disk, $| z | < 1$ and choose $\pmb { s }$ to be the set $0 < | w | < 1$ in Corollary 2.27.1. Equation (2.107) now holds for the polynomial we are considering. If $\zeta = 0$ we see that for $z \in C$

$$
p ( z ) - \frac { z p ^ { \prime } ( z ) } { n } \epsilon S .
$$

Thus as $\zeta$ ranges over $c$ we may conclude from (2.107) that an open disk with center at $p ( z ) - z p ^ { \prime } ( z ) / n$ and radius $| p ^ { \prime } ( z ) / n |$ is contained in S. But the maximum radius of such a disk is $^ { 1 / 2 , }$ and the result follows.

Example 2. If $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ and $| \mathsf { R e } p ( z ) | \leqslant 1$ for $| z | \leqslant 1$ then

$$
| p ^ { \prime } ( z ) | \leqslant n , \qquad | z | \leqslant 1 .
$$

Equality holds in (2.108)if,and only if, $p ( z ) = e ^ { i \alpha } z ^ { n } + i t , \alpha , t$ real.

Proof. Let $c$ be the closed disk, $| z | \leqslant 1$ ,and $\pmb { s }$ the strip $- 1 \leqslant \mathbf { R e } w \leqslant 1$ Note that $p ( z ) = w \in S ;$ if, and only if, $| \mathbf { R e } p ( z ) | \leqslant 1$ .Thus (2.107) holds under our assumptions. If $\zeta = 0$ we see that $p ( z ) - z p ^ { \prime } ( z ) / n \in S ,$ ,and so when $\zeta$ ranges over $C _ { i }$ 。(2.107) informs us that a closed disk of radius $| p ^ { \prime } ( z ) / n | ,$ centered at $p ( z ) - z p ^ { \prime } ( z ) / n$ is contained in $- 1 \leqslant \mathbf { R e } w \leqslant 1$ for $| z | \leqslant 1$ . The maximum radius of such a disk is 1, and our result follows.

The result in Example 2, which implies the usual complex Bernstein inequality, is due to Szego [2] (our approach is given in Malik [1]). An easy consequence is a generalization of the Bernstein inequality for real trig-

onometric polynomials. Namely,

$$
t ( \theta ) = \sum _ { j = 0 } ^ { n } { \bigl ( } a _ { j } \cos j \theta + b _ { j } \sin j \theta { \bigr ) }
$$

has real coefficients and satisfies $\left\| t \right\| \leqslant 1$ if, and only if,

$$
p ( z ) = \sum _ { j = 0 } ^ { n } ~ ( a _ { j } - i b _ { j } ) z ^ { j }
$$

satisfies $| \mathsf { R e } p ( z ) | \leqslant 1$ for $| z | = 1$ Thus,

$$
| e ^ { i \theta } p ^ { \prime } ( e ^ { i \theta } ) | = \left| \sum _ { j = 0 } ^ { n } j ( a _ { j } \cos j \theta + b _ { j } \sin j \theta ) - i \sum _ { j = 0 } ^ { n } j ( b _ { j } \cos j \theta - a _ { j } \sin j \theta ) \right| .
$$

Consider the trigonometric polynomial

$$
\widetilde t ( \theta ) = \sum _ { j = 1 } ^ { n } \ ( - b _ { j } \cos j \theta + a _ { j } \sin j \theta ) ,
$$

called the conjugate to $t ( \theta )$ .Then (2.109) yields

$$
| p ^ { \prime } ( e ^ { i \theta } ) | ^ { 2 } = ( \widetilde { t } ^ { \prime } ( \theta ) ) ^ { 2 } + ( t ^ { \prime } ( \theta ) ) ^ { 2 } ,
$$

and from Example 2 we deduce that

$$
( \widetilde t ^ { \prime } ( \theta ) ) ^ { 2 } + ( t ^ { \prime } ( \theta ) ) ^ { 2 } \leqslant n ^ { 2 } ,
$$

the desired generalization. The condition for equality to hold in (2.108) implies that equality holds in (2.110) only if $t ( \theta ) = \cos n ( \theta - \theta _ { 0 } )$

The reader who is interested in learning more about the type of material we have examined in this subsection is advised to consult the excellent survey of Rahman and Schmeisser [1].

1.2. Polynomials with Curved Majorants. In studying extremal problems we have frequently normalized the set of competing polynomials by stipulating that $\pmb { p } \in \pmb { B _ { n } }$ ,i.e., $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ and $| p ( x ) | \leqslant 1$ for $- 1 \leqslant x \leqslant 1$ .We thus require that the graph of $y = p ( x )$ be contained in the square square $- 1 \leqslant x \leqslant 1 ,$ ， $- 1 \leqslant y \leqslant 1$ 、At a conference in Varna, Bulgaria in 1970, Turan raised the problem of obtaining results of the Markov kind if the graph of $y = p ( x )$ was required to be contained in the disk $x ^ { 2 } + y ^ { 2 } \leqslant 1 ,$ i.e.，if $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ and $| p ( x ) | \leqslant ( 1 - x ^ { 2 } ) ^ { 1 / 2 } , - 1 \leqslant x \leqslant 1$ . Indeed, he suggested generalizing the normalization of $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ by requiring that $| p ( x ) | \leqslant \varphi ( x ) , - 1 \leqslant x \leqslant 1$ , for a given $\varphi ( x ) ,$ ，a curved majorant. We wish to investigate several examples of such problems next.

We begin with Turan's first problem. Let ${ \pmb { D } } _ { \pmb { n } }$ denote the set of $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ such that $| p ( x ) | \leqslant ( 1 - x ^ { 2 } ) ^ { 1 / 2 }$ for $\boldsymbol { x } \in \boldsymbol { I } .$ As usual $\| \cdot \|$ is the maximum norm on $I .$

Theorem 2.28 (Rahman [1]). If $\pmb { p } \in D _ { n } ( n \geqslant 2 )$ then

$$
\| p ^ { \prime } \| \leqslant 2 ( n - 1 ) .
$$

Equality is attained in (2.11)for

$$
p ( x ) = ( 1 - x ^ { 2 } ) U _ { n - 2 } ( x ) = { \frac { T _ { n - 2 } ( x ) - T _ { n } ( x ) } { 2 } } .
$$

Proof. If $\pmb { p } \in \pmb { D } _ { \pmb { n } }$ then $p ( x ) = ( 1 - x ^ { 2 } ) q ( x ) , \quad q \in \mathcal { P } _ { n - }$ Put $f ( x ) =$ $( 1 - x ^ { 2 } ) ^ { 1 / 2 } q ( x )$ so that $p ( x ) = ( 1 - x ^ { 2 } ) ^ { 1 / 2 } f ( x )$ Then

$$
| p _ { n } ^ { \prime } ( x ) | \leqslant | x q ( x ) | + ( 1 - x ^ { 2 } ) ^ { 1 / 2 } | f ^ { \prime } ( x ) | , \qquad x \in I .
$$

$t ( \theta ) = f ( \cos \theta ) = \sin \theta q ( \cos \theta ) \in \mathcal { T } _ { n - 1 }$ and $\| t \| \leqslant 1$ Bernstein's inequality yields $\| t ^ { \prime } \| \leqslant n - 1$ which implies $( 1 - x ^ { 2 } ) ^ { 1 / 2 } | f ^ { \prime } ( x ) | \leqslant n - 1$ ， $\boldsymbol { x } \in \boldsymbol { I }$ Also $( 1 - x ^ { 2 } ) ^ { 1 / 2 } | q ( x ) | \leqslant 1$ and so $\| q \| \leqslant n - 1$ according to Exercise 2.7.14.Equation (2.113) is now seen to yield (2.11).

Consider $\pmb { p }$ as defined in (2.112). The right-hand equality is just Exercise 1.2.15c and $| p ^ { \prime } ( \pm 1 ) | = 2 ( n - 1 )$ follows.The bound in (2.11) cannot, therefore, be lowered.

Remark 1. For $\pmb { p } \in \pmb { D } _ { \pmb { n } }$ we can obtain a point-wise estimate of ${ p } _ { n } ^ { \prime } ( x )$ analogous to (2.69). If we retain the notation of the proof then the inequality of van der Corput and Schaake (see Remark 1 following (2.68)) yields

$$
( n - 1 ) ^ { 2 } f ^ { 2 } ( x ) + ( 1 - x ^ { 2 } ) ( f ^ { \prime } ( x ) ) ^ { 2 } \leqslant ( n - 1 ) ^ { 2 } , \qquad x \in I .
$$

Using this inequality in (2.113) we obtain, for $- 1 < x < 1$

$$
\begin{array} { r } { | p ^ { \prime } ( x ) | \leqslant | x | ( 1 - x ^ { 2 } ) ^ { - 1 / 2 } | f ( x ) | + ( n - 1 ) ( 1 - | f ( x ) | ^ { 2 } ) ^ { 1 / 2 } } \\ { \leqslant \underset { 0 \leqslant y \leqslant 1 } { \operatorname* { m a x } } ~ [ | x | ( 1 - x ^ { 2 } ) ^ { - 1 / 2 } y + ( n - 1 ) ( 1 - y ^ { 2 } ) ^ { 1 / 2 } ] . } \end{array}
$$

The expression on the right-hand side of the second inequality in (2.114), with $_ { x }$ fixed,is $[ x ^ { 2 } ( 1 - x ^ { 2 } ) ^ { - 1 } + ( n - 1 ) ^ { 2 } ] ^ { 1 / 2 }$ ，which is attained for $y =$

$| x | [ ( n - 1 ) ^ { 2 } ( 1 - x ^ { 2 } ) + x ^ { 2 } ] ^ { - 1 / 2 }$ . We thus arrive at the conclusion that

$$
| p ^ { \prime } ( x ) | \leqslant { \frac { ( n - 1 ) } { \sqrt { 1 - x ^ { 2 } } } } \left[ 1 - \left( 1 - { \frac { 1 } { ( n - 1 ) ^ { 2 } } } \right) x ^ { 2 } \right] ^ { 1 / 2 } , \qquad - 1 < x < 1 .
$$

Remark 2. If $\pmb { p } \in \pmb { B _ { n } }$ then the bounds on its coefficients given by (2.44) and (2.45) may be expressed in the following succinct form. If

$$
p ( x ) = \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } ,
$$

then $| a _ { k } | , k = 0 , \ldots , n ,$ is bounded from above by the absolute value of the coefficients of $x ^ { k }$ in $T _ { n } ( x ) + T _ { n - 1 } ( x ) .$ In Rahman [2], the author shows that if $\pmb { p } \in \pmb { D } _ { \pmb { n } }$ is given by (2.115) then $| a _ { k } | , k { = } 0 , \ldots , n ,$ is bounded from above by the absolute value of the coefficient of $x ^ { k }$ in ${ \frac { 1 } { 2 } } ( T _ { n } ( x ) + T _ { n - 1 } ( x ) - T _ { n - 2 } ( x )$ $\phantom { } - T _ { n - 3 } ( x ) )$ . In both cases equality occurs in an obvious way, depending on the parity of $\pmb { n } - \pmb { k } .$

# EXERCISES 2.8.1-2.8.8

Let ${ \pmb F } _ { \pmb n }$ here denote the set of $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ such that $| p ( x ) | \leqslant | x | , x \in I .$

2.8.1. Show that if $\pmb { p } \in \pmb { F } _ { \pmb { \mathfrak { n } } }$ then $\| p ^ { \prime } \| \leqslant 1 + ( n - 1 ) ^ { 2 }$ , and this upper bound cannot be lowered.

Hint. If $\pmb { p } \in \pmb { F } _ { \pmb { n } }$ then $p ( z ) = z g ( z )$ where ${ \pmb g } \in { \pmb B } _ { n }$ . Now apply A. A. Markov's theorem to $\pmb { g }$

Hint. Apply the inequality of van der Corput and Schaaketo $g ( \cos \theta ) = p ( \cos \theta ) / \cos \theta$ and proceed as in Remark 1 following Theorem 2.28.

Let $G _ { n }$ here denote the set of $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ such that $| p ( x ) | \leqslant ( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$ ， $- 1 < x < 1$

2.8.3. If $\pmb { p } \in \pmb { G } _ { n }$ and $| x | \leqslant \eta _ { 1 } ^ { ( n + 1 ) } = \cos \left( \pi / ( n + 1 ) \right)$ then

$$
| p ^ { \prime } ( x ) | \leqslant n ( n + 1 ) ^ { 2 } .
$$

Hint.Apply Bernstein's inequality to $t ( \theta ) = \sin \theta p ( \cos \theta ) \in \mathcal { T } _ { n + 1 }$ to obtain $| x p ( x )$ $- ( 1 - x ^ { 2 } ) p ^ { \prime } ( x ) | \leqslant n + 1 , x \in I .$ If we now apply Exercise 2.7.14 to $p ( { \boldsymbol { x } } )$ we obtain $\| { \pmb p } \| \leqslant n + 1$ and hence the inequality in the preceding sentence yields $| ( 1 - x ^ { 2 } ) p ^ { \prime } ( x ) | \leqslant 2 ( n + 1 ) .$ .The result now follows,in view of the restriction on $\pmb { x } ,$ by an application of Exercise 2.7.14 to $p ^ { \prime } ( x ) / ( n + 1 ) ^ { 2 }$

2.8.4. Put

$$
q _ { j } ( x ) = { \frac { T _ { n + 1 } ( x ) } { x - \xi _ { j } ^ { ( n + 1 ) } } } , \qquad j = 1 , \ldots , n + 1 .
$$

Show that

$$
q _ { j } ^ { \prime } ( x ) > 0 , \qquad j = 1 , \ldots , n + 1 , \qquad \eta _ { 1 } ^ { ( n + 1 ) } \leqslant x \leqslant 1 .
$$

Hint. Verify by direct computation that $q _ { j } ^ { \prime } ( \eta _ { 1 } ^ { ( n + 1 ) } ) > 0$ and $q / ( 1 ) > 0 .$ Note that $q ^ { \prime } ( x )$ has at least $n - 2$ zeros to the left of $\eta _ { 1 } ^ { ( n + 1 ) }$ ：

2.8.5. Show that if $\pmb { p } \in \pmb { G } _ { \pmb { n } }$ then

$$
| p ^ { \prime } ( x ) | \leqslant { \frac { 1 } { n + 1 } } \sum _ { j = 1 } ^ { n + 1 } q _ { j } ^ { \prime } ( x ) , \qquad \eta _ { 1 } ^ { ( n + 1 ) } < x \leqslant 1 .
$$

Hint. If $\pmb { p } \in \mathcal { P } _ { n }$ then

$$
p ^ { \prime } ( x ) = L _ { n } ^ { \prime } ( p , T ; x ) = { \frac { 1 } { n + 1 } } \sum _ { j = 1 } ^ { n + 1 } { ( - 1 ) ^ { j - 1 } ( 1 - ( \xi _ { j } ^ { ( n + 1 ) } ) ^ { 2 } ) ^ { 1 / 2 } } p ( \xi _ { j } ^ { ( n + 1 ) } ) q _ { j } ^ { \prime } ( x ) .
$$

Now use the hypothesis and (2.118).

2.8.6. (Pierre and Rahman [1]) If $\pmb { p } \in \pmb { G } _ { n }$ then

$$
\Vert p ^ { \prime } \Vert \leqslant \frac { T _ { n + 1 } ^ { \prime \prime } ( 1 ) } { n + 1 } = \frac { n ( n + 1 ) ( n + 2 ) } { 3 } .
$$

Equality holds for $p = \pm U _ { n }$

Hint. If we put $p = T _ { n + 1 } ^ { \prime } / n + 1$ in (2.120) and recall Exercise 1.2.3 we obtain

$$
\frac { T _ { n + 1 } ^ { \prime \prime } ( x ) } { n + 1 } = \frac { 1 } { n + 1 } \sum _ { j = 1 } ^ { n + 1 } q _ { j } ^ { \prime } ( x ) .
$$

We may then conclude from (2.119) that if $\eta _ { 1 } ^ { ( n + 1 ) } < x \leqslant 1 , | p ^ { \prime } ( x ) | \leqslant T _ { n + 1 } ^ { \prime } ( 1 ) / ( n + 1 ) .$ Indeed,it is nothard to see that thesameresult holds for $- 1 \leqslant x < \eta _ { n } ^ { ( n + 1 ) }$ ,and so the required result follows from (2.116).

Note that if $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ and $p ^ { \prime } / n \in G _ { n - 1 }$ then Exercise 2.8.6 implies that

$$
\| p ^ { \prime \prime } \| \leqslant \frac { n ^ { 2 } ( n ^ { 2 } - 1 ) } { 3 } .
$$

In particular if $\pmb { \bar { p } } \in \pmb { B } _ { \pmb { \bar { n } } }$ then $p ^ { \prime } / n \in G _ { n - 1 }$ ，according to (2.69),and we recover V. A. Markov's theorem for the second derivative.A brief survey of the topic of polynomials with curved majorants, as well as further references, may be found in Rahman and Schmeisser [1].

2.8.7. Results having the same geometric flavor as provided by curved majorants can be obtained in the complex case by using Corollary 2.27.1. If $\pmb { p } \in \mathcal { P } _ { \pmb { \pi } }$ and $\begin{array} { r } { p ( z ) = w \in S , } \end{array}$ find the exact upper bound for $| p ^ { \prime } ( z ) | , | z | \leqslant 1$ when S is defined by:

(i $\begin{array} { r l } & { | w | \leqslant 1 , } \\ & { 0 \leqslant r < | w | < R , } \\ & { | \mathbf { R e } w | \leqslant a , | \mathbf { I m } w | \leqslant b } \end{array}$ (ii) (ii)

2.8.8. A. A. Markov's theorem says that if $\pmb { p } \in \pmb { B _ { n } }$ then $\| \pmb { p } ^ { \prime } \| \leqslant \| \pmb { T } _ { \pmb { n } } ^ { \prime } \|$ . Bojanov [1] showed that if $\pmb { p } \in \pmb { B _ { n } }$ then $\| p ^ { \prime } \| _ { q } \leqslant \| T _ { n } ^ { \prime } \| _ { q }$ ， $1 \leqslant q < \infty$ ,where

$$
\| f \| _ { q } = { \biggl ( } \int _ { - 1 } ^ { 1 } | f ( x ) | ^ { q } d x { \biggr ) } ^ { 1 / q } .
$$

A. A. Markov's theorem is the case $q = \infty$ . Prove the case $q = 1$ ,i.e., show that if $\pmb { p } \in \pmb { B } _ { \pmb { n } }$ then

$$
\int _ { - 1 } ^ { 1 } | p ^ { \prime } ( x ) | d x \leqslant \int _ { - 1 } ^ { 1 } | T _ { n } ^ { \prime } ( x ) | d x = 2 n ,
$$

with equality only if $p = \pm T _ { n }$

Hint. Suppose $\pmb { p } ^ { \prime } ( \pmb { x } )$ changes sign in （-1,1） only at $\pmb { x } _ { 1 } , ~ . . . , ~ \pmb { x } _ { k }$ where $x _ { 0 } = - 1 < x _ { 1 } < \cdots < x _ { k } < 1 = x _ { k + 1 }$ so that

$$
\int _ { - 1 } ^ { 1 } | p ^ { \prime } ( x ) | d x = \left| \sum _ { j = 0 } ^ { k } { \bigl ( } - 1 { \bigr ) } ^ { j } \int _ { x _ { j } } ^ { x _ { j + 1 } } p ^ { \prime } ( x ) d x \right| .
$$

2.Miscellaneous Extremal Properties. In this section we wish to mention some results about extremal properties of Chebyshev polynomials, with most proofs omitted because of length and/or difficulty. The reader is directed to the original sources for the details.

2.1. The Remez Inequality for Polynomials. Suppose that $\pmb { p } \in \mathcal { P } _ { \pmb { n } }$ . Let $M ( p )$ denote the set of all $x \in I ( = [ - 1 , 1 ] )$ such that $| p ( x ) | \leqslant 1$ Then $M ( p )$ is the union of mutually disjoint closed subintervals of $, I _ { 1 } , \ldots , I _ { k }$ .If $l _ { j }$ is the length of $I _ { j } , j = 1 , \ldots , k ,$ . then we say that $| M ( p ) |$ , the measure of $M ( p )$ is $l _ { 1 } + \cdots + l _ { k }$ · (If $| p ( x ) | \geqslant 1$ for all $\boldsymbol { x } \in \boldsymbol { I }$ then $| M ( p ) | = 0 .$ ） The Remez inequality states that

$$
\| p \| \leqslant T _ { n } \left( { \frac { 4 } { | M ( p ) | } } - 1 \right) .
$$

Note that equality holds in (2.121) if, and only if, $\| { \pmb p } \| \leqslant 1 ,$ ,while if $| M ( p ) | = 0$ the inequality is trivial. A detailed proof of (2.121) can be found in Freud [2, pp. 119-122].

2.2. The Longest Polynomial. Suppose (real) $\mathbf { \Delta } _ { t \in \mathcal { T } _ { n } }$ satisfies $\| t \| \leqslant 1$ Erdos [3] proved that if $l ( t )$ denotes the arc length of the graph of $y = t ( x ) ,$

$0 < x < 2 \pi ,$ ，then $\boldsymbol { l } ( t )$ attains its maximum if, and only if, $t ( x ) = \cos { ( n x + \alpha ) } ,$ where $\pmb { \alpha }$ is any real constant. Here is a sketch of Erdos'proof.

Suppose $\mathbf { \Delta } _ { t \in \mathcal { T } _ { n } }$ satisfies $\| \mathbfcal { t } \| \leqslant 1$ and we put ${ \pmb s } ( { \pmb x } ) =$ cos nx. Let

$$
- 1 < t ( x _ { 1 } ) = s ( x _ { 2 } ) < 1
$$

hold, then in view of the inequality of van der Corput and Schaake, we have

$$
| t ^ { \prime } ( x _ { 1 } ) | \leqslant n ( 1 - t ^ { 2 } ( x _ { 1 } ) ) ^ { 1 / 2 } = n ( 1 - s ^ { 2 } ( x _ { 2 } ) ) ^ { 1 / 2 } = | s ^ { \prime } ( x _ { 2 } ) | ,
$$

and if the sign of equality holds for one pair $\mathbf { { x } _ { 1 } } , \mathbf { { x } _ { 2 } } .$ ,it holds for all pairs, i.e., $t ( x ) = \cos { ( n x + \alpha ) }$

Suppose $t ( x ) \neq \cos { ( n x + \alpha ) }$ Let $\pmb { \tau }$ and $\pmb { \sigma }$ be monotone arcs of $y = t ( x )$ and $y = s ( { \boldsymbol { x } } ) ,$ , respectively, with the endpoints of each having the same ordinates, $y _ { 1 }$ and $y _ { 2 }$ Let $| \tau |$ and $| \pmb { \tau _ { x } } |$ denote the arc length of $\pmb { \tau }$ and the length of the projection of $\pmb { \tau }$ on the $\pmb { x }$ -axis, respectively,and similarly for $| \pmb { \sigma } |$ and $| \pmb { \sigma _ { x } } | .$ .Then

$$
| \tau | < | \sigma | + ( | \tau _ { x } | - | \sigma _ { x } | )
$$

follows from (2.123) by approximating $\pmb { \tau }$ and $\pmb { \sigma }$ by means of a polygonal line corresponding to a subdivision of $( y _ { 1 } , y _ { 2 } )$

Let $\tau ^ { ( 1 ) } , \ldots , \tau ^ { ( m ) }$ be the monotone arcs which constitute the curve $y = t ( x )$ over an interval of length $2 \pi$ 、It is obvious that we may choose disjoint monotone arcs $\sigma ^ { ( 1 ) } , . . . , \sigma ^ { ( m ) }$ of $y = s ( { \boldsymbol { x } } )$ so that the arcs $\tau ^ { ( j ) }$ and $\pmb { \sigma } ^ { ( j ) }$ have endpoints having the same ordinates, for $j = 1 , \ldots , m$ .Thus, according to (2.124),

$$
| \tau ^ { ( j ) } | < | \sigma ^ { ( j ) } | + ( | \tau _ { x } ^ { ( j ) } | - | \sigma _ { x } ^ { ( j ) } | )
$$

and hence

$$
\sum _ { j = 1 } ^ { m } | \tau ^ { ( j ) } | < \sum _ { j = 1 } ^ { m } | \sigma ^ { ( j ) } | + \Bigg ( 2 \pi - \sum _ { j = 1 } ^ { m } | \sigma _ { x } ^ { ( j ) } | \Bigg ) .
$$

The left-hand side of(2.125) is the arc length of $y = t ( x ) , 0 < x < 2 \pi ,$ while the expression in the parentheses on the right-hand side is the sum of the lengths of the projections on the $\pmb { x }$ -axis of the arcs that remain in the graph of $y = \cos n x$ when the arcs $\pmb { \sigma } ^ { ( 1 ) } , \ldots , \pmb { \sigma } ^ { ( m ) }$ have been deleted. If this expression is replaced by the sum of the lengths of these remaining arcs, the right-hand side of(2.125) increases and becomes the arc length of $y = \cos n x$ ， $0 < x < 2 \pi$ and the proof is complete.

Erdos [3] concludes as follows: “I conjecture that the following theorem holds. Let $f ( x )$ be a polynomial of the ${ \pmb n } ^ { \mathrm { t h } }$ degree, $| f ( x ) | \leqslant 1$ in $( - 1 , 1 )$ . Of the graphs of all these polynomials that of the ${ \pmb n } ^ { \mathrm { t h } }$ Chebisheff polynomial has the maximum length of arc.”

The Erdos conjecture was later proved by Kristiansen [1] and Bojanov [2], independently. Both proofs are elaborate. I find Bojanov's proof a bit easier to follow.

2.3. An Iterative Solution of a System of Linear Equations. Let $\pmb { A }$ be a nonsingular $n \times n$ matrix whose entries are complex numbers. Then if $b = ( b _ { 1 } ,$ $\cdots , b _ { n } ) ^ { T }$ is any given column vector of complex numbers there exists a unique solution, $\pmb { x } = ( \pmb { x } _ { 1 } , . . . , \pmb { x } _ { n } ) ^ { T }$ , of the system of linear equations

$$
A { \boldsymbol { x } } = b .
$$

The invention of numerical procedures for “solving"(2.126) (i.e., calculating good approximate solutions of (2.126)) on computers is an important aspect of contemporary numerical analysis. We wish to describe an iterative procedure, which is sometimes used, whose implementation depends on solving an interesting polynomial extremal problem. For notions of com-putational matrix theory mentioned in what follows we refer the reader to Golub and Van Loan [1] and the references given there.

In the iterative scheme under consideration we start with an initial guess, $\mathbf { x } ^ { ( 1 ) }$ ,of the solution and modify it successively so as to obtain a sequence of approximations $x ^ { ( 1 ) } , x ^ { ( 2 ) } , \ldots , x ^ { ( j ) } , .$ ..to ${ \pmb x } .$ If $e ^ { ( j ) } = x - x ^ { ( j ) }$ is the discrepancy of the jth iterate then we arrive at a “solution”, $\pmb { x } ^ { ( m ) }$ ，when the size of $e ^ { ( m ) }$ ， measured in an appropriate norm in $\mathbb { C } ^ { n }$ ， gets to whatever preassigned tolerance is required. In the method we wish to examine, the iterates are defined by

$$
\begin{array} { r } { x ^ { ( j + 1 ) } = x ^ { ( j ) } - \alpha _ { j } ( A x ^ { ( j ) } - b ) , j = 1 , 2 , \ldots , } \end{array}
$$

that is, $\boldsymbol { x } ^ { ( j + 1 ) }$ is obtained from $\boldsymbol { x } ^ { ( j ) }$ by subtracting a strategically chosen multiple of $\pmb { A } \pmb { x } ^ { ( j ) } - \pmb { b }$ 、Such a method is called Richardson iteration (cf. Anderssen and Golub [1]) or Chebyshev iteration (cf. Marchuk [1]), with iteration parameters $\alpha _ { j } , j = 1 , 2 , \ldots$ ·

If I denotes the $\pmb { n } \times \pmb { n }$ identity matrix then, in view of (2.127),a straightforward computation yields

$$
e ^ { ( k + 1 ) } = \prod _ { j = 1 } ^ { k } { \big ( } I - \alpha _ { j } A { \big ) } e ^ { ( 1 ) } .
$$

In order to choose the parameters $\alpha _ { 1 } , \ldots , \alpha _ { k }$ we consider

$$
p ( z ) = \prod _ { j = 1 } ^ { k } \left( 1 - \alpha _ { j } z \right) = 1 - \sum _ { j = 1 } ^ { k } \beta _ { j } z ^ { j } ,
$$

and note that $p ( 0 ) = 1$ .Equation (2.128) can now be rewritten as

$$
e ^ { ( k + 1 ) } = p ( A ) e ^ { ( 1 ) } .
$$

Let $\| \cdot \|$ denote a vector norm in $\mathbb { C } ^ { n }$ as well as the natural associated matrix norm. That is, if $\pmb { B }$ is an $\pmb { n } \times \pmb { n }$ matrix and $\| \cdot \|$ is a norm in $\mathbb { C } ^ { n }$ we put

$$
\| B \| = \operatorname* { s u p } _ { \stackrel { y \in \mathbb { C } ^ { n } } { \| y \| = 1 } } \| A y \| .
$$

Then (2.130) implies

$$
\| e ^ { ( k + 1 ) } \| \leqslant \| p ( A ) \| \| e ^ { ( 1 ) } \| ,
$$

thus suggesting that we choose $\alpha _ { 1 } , \ldots , \alpha _ { k } \ s o$ as to minimize $\| p ( A ) \|$ .If $\pmb { B }$ is an $\pmb { n } \times \pmb { n }$ square matrix whose eigenvalues are $\lambda _ { 1 } , \ldots , \lambda _ { n }$ (not necessarily distinct) and $\pmb { p _ { k } } \in \mathcal { P } _ { \pmb { k } }$ , then the eigenvalues of $p _ { k } ( B )$ are $p _ { k } ( \lambda _ { 1 } ) , \ldots , p _ { k } ( \lambda _ { n } ) .$ Hence if $\sigma ( A )$ denotes the spectrum of $\pmb { A }$ (i.e., the set of eigenvalues of $\pmb { A }$ and $\pmb { \rho } ( A )$ its spectral radius (i.e., $\rho ( A ) = \operatorname* { m a x } { \{ | \lambda _ { i } | \colon \lambda _ { i } \in \sigma ( A ) \} } )$ we obtain

$$
\rho ( p ( A ) ) = \operatorname* { m a x } _ { z \in \sigma ( A ) } | p ( z ) | .
$$

But it is known (cf. John [1]) that given $\pmb \varepsilon > \mathbf 0$ ，there exists a natural norm such that

$$
\| p ( A ) \| \leqslant \rho ( p ( A ) ) + \varepsilon .
$$

Thus, in view of (2.129), (2.131), (2.132), and (2.133), the nmbers $\alpha _ { 1 } , \ldots , \alpha _ { k }$ may be chosen to make $\| e ^ { ( k + 1 ) } \|$ small by solving the best uniform approximation problem

$$
\operatorname* { m i n } _ { \beta _ { 1 } , \dots , \beta _ { k } } \operatorname* { m a x } _ { z \in \sigma ( A ) } | 1 - ( \beta _ { 1 } z + \cdots + \beta _ { k } z ^ { k } ) | .
$$

However, the determination of $\sigma ( A )$ is no easy task and generally involves more computational effort than is needed to determine $\pmb { A } ^ { - 1 } \pmb { b }$ numerically. For this reason we replace $\sigma ( A )$ in (2.134) by a compact set, $\pmb { S } ,$ in $\mathbb { C }$ which is known to contain ${ \pmb \sigma } ( A ) .$ Equation (2.134) is then replaced by

$$
\operatorname* { m i n } _ { v \in V _ { 0 } } \operatorname* { m a x } _ { z \in S } | v ( z ) | ,
$$

where $V _ { 0 } = \{ v \in \mathcal { P } _ { k } \colon v ( 0 ) = 1 \}$ ·

Suppose $\boldsymbol 0 \not \oplus \boldsymbol S$ .Then $V _ { 0 }$ satisfies the Chebyshev condition with respect to S and (2.135) has a unique solution according to Theorem 2.8. We see that $v = 1$ is a competitor in (2.135) and so, unless $v = 1$ is the solution to (2.135), there is a unique solution to (2.135), ${ \pmb v } ^ { * }$ ， satisfying $\| v ^ { * } \| _ { s } < 1$ ，and the reciprocals of the zeros of ${ \pmb v } ^ { * }$ provide optimal parameters, $\alpha _ { 1 } ^ { * } , \ldots , \alpha _ { k } ^ { * }$ This sequence of parameters can now be extended (cyclically) as follows: if $s = 1 , 2 ,$ ...， put $\alpha _ { s k + j } ^ { * } = \alpha _ { j } ^ { * }$ ， $j = 1 ,$ 。.， $\pmb { k } .$ ，Equation (2.132) now implies that $\rho ( p ( A ) ) < 1$ If we chooseε to satisfy $0 < \varepsilon < 1 - \rho ( p ( A ) )$ and use the matrix norm for which (2.133) holds (and the vector norm associated with it) then (2.131) and (2.133) yield

$$
\| e ^ { ( s k + 1 ) } \| \leqslant \| p ( A ) \| \| e ^ { ( 1 ) } \| , \qquad s = 1 , 2 , \ldots .
$$

Note that since vector norms on $\mathbb { C } ^ { n }$ are equivalent inequality (2.136) holds for .any vector norm provided that a constant, $c ( \geqslant 1 )$ ，which depends on the norm, multiplies the right-hand side. Thus if $\| \pmb { v } \| _ { \pmb { s } } < 1$ then (2.136) informs us that the sequence of iterates in (2.127), with the starred parameters, converges to a solution in any norm in $\mathbb { C } ^ { n }$

Having arrived at this positive conclusion we must add that in the world of actual computation the situation is not as encouraging. The Richardson iteration,as presented above, suffers from numerical instability due to round-off error. This unpleasantnesscan be mitigated by an appropriate reordering of the optimal parameters. An excellent exposition of these issues is to be found in Anderssen and Golub [1].

We now turn to the extremal problem, (2.135). When the nonsingular matrix, $A _ { i }$ ，is Hermitian its eigenvalues are real and nonzero. If $\pmb { A }$ is also positive definite then its eigenvalues are positive. Suppose that they are in the interval $\pmb { S } \colon [ \alpha , \beta ] .$ ，where $0 < \alpha < \beta .$ ，Then we obtain an exact solution of (2.135) from Exercise 2.5.12, namely,

$$
v ^ { * } ( x ) = \frac { T _ { k } \left( \displaystyle \frac { 2 x - ( \alpha + \beta ) } { \beta - \alpha } \right) } { T _ { k } \left( \displaystyle \frac { \alpha + \beta } { \alpha - \beta } \right) }
$$

and

$$
\| v ^ { * } \| _ { S } = \frac { 1 } { T _ { k } \bigg ( \frac { \alpha + \beta } { \beta - \alpha } \bigg ) } .
$$

The optimal parameters are now seen to be given by

$$
\alpha _ { j } ^ { * } = \frac { 2 } { ( \alpha + \beta ) + ( \beta - \alpha ) \xi _ { j } ^ { ( k ) } } , ~ j = 1 , . . . , k .
$$

When (nonsingular) $\pmb { A }$ is Hermitian but indefinite, its spectrum is a subset of two closed intervals of R $\lceil \alpha , \beta \rceil$ and $[ \gamma , \delta ]$ where $\alpha < \beta < 0 < \gamma < \delta$ .When S is a pair of intervals of the type just described an exact solution of (2.135) is not generally available. An interesting and readable discussion of this case, which also contains an effective numerical method for the solution of (2.135) can be found in de Boor and Rice [1].

An explicit solution of(2.135) was given by Freund and Ruscheweyh [1] in the case that $A = I - N$ ,where $\pmb { N }$ is real and skew-symmetric, i.e., $N = - N ^ { T }$ In this case the eigenvalues of $\pmb { A }$ are contained in a vertical segment of the complex plane, $S = [ 1 - i r , 1 + i r ]$ where $\pmb { r } = \pmb { \rho } ( N )$ .Following Freund and Ruscheweyh, we rewrite (2.135) by using a linear transformation to replace S by the interval [-1, 1]. Namely, we put

$$
w = \frac { i } { r } \left( 1 - z \right) ,
$$

and obtain

$$
M _ { k } ( r ) = \operatorname* { m i n } _ { v \in V _ { 0 } } \ \operatorname* { m a x } _ { w \in [ - 1 , 1 ] } | v ( w ) | , \qquad V _ { 0 } = \big \{ v \in \mathcal { P } _ { k } : v \left( \frac { i } { r } \right) = 1 \big \}
$$

as the extremal problem equivalent to (2.135).

If we put $r ^ { - 1 } = ( R - R ^ { - 1 } ) / 2 , R > 1$ (so that $R = ( 1 + ( 1 + r ^ { 2 } ) ^ { 1 / 2 } ) / r )$ then the solution to (2.138) is

$$
v ^ { * } ( w ) = \frac { 1 } { c } ( R ^ { 2 } T _ { k } ( w ) + 2 i R T _ { k - 1 } ( w ) - T _ { k - 2 } ( w ) ) ,
$$

where

$$
\begin{array} { r } { c = - \frac 1 2 ( i R ) ^ { k - 2 } ( R ^ { 2 } + 1 ) ^ { 2 } } \end{array}
$$

and

$$
M _ { k } ( r ) = \frac { 2 } { R ^ { k } + R ^ { k - 2 } } .
$$

To recover the solution of (2.135) we need only substitute (2.137) in (2.139). This striking result has stimulated further work on generalizations of the extremal problem given by (2.138). The interested reader should see Freund [1],Fischer and Freund [1],as well as Freund and Ruscheweyh [1],of which we have presented only a taste. Another useful survey of Richardson iteration is Opfer and Schober [1].

# 3

# EXPANSION OF FUNCTIONS IN SERIES OF CHEBYSHEV POLYNOMIALS

The Chebyshev polynomial has extremal properties in both the uniform sense (cf. Theorem 2.1) and the least squares sense [cf. (1.109)]. In Chapter 2 our main theme was extremal properties of the Chebyshev polynomials in the uniform norm. This chapter focuses on the expansion theory of Chebyshev polynomials considered as orthogonal polynomials. Particular attention is paid to the uniform approximating power of the partial sums of Chebyshev expansions.

# 3.1. Polynomials in Chebyshev Form

The representation of a polynomial in terms of Chebyshev polynomials (cf. Exercise 1.2.6),a particularly simple example of the expansion of a function in a series of Chebyshev polynomials, has some interesting properties; for example, let

$$
p ( x ) = 1 + x + x ^ { 2 } + x ^ { 3 } + x ^ { 4 } + x ^ { 5 } ;
$$

then, according to Exercise 1.5.32,

$$
\begin{array} { r } { p ( x ) = \frac { 1 5 } { 8 } + \frac { 1 9 } { 8 } T _ { 1 } ( x ) + T _ { 2 } ( x ) + \frac { 9 } { 1 6 } T _ { 3 } ( x ) + \frac { 1 } { 8 } T _ { 4 } ( x ) + \frac { 1 } { 1 6 } T _ { 5 } ( x ) . } \end{array}
$$

It is clear from (3.2) that

$$
\begin{array} { r } { p _ { 4 } ( x ) = \frac { 1 5 } { 8 } + \frac { 1 9 } { 8 } T _ { 1 } ( x ) + T _ { 2 } ( x ) + \frac { 9 } { 1 6 } T _ { 3 } ( x ) + \frac { 1 } { 8 } T _ { 4 } ( x ) } \end{array}
$$

satisfies

$$
| p ( x ) - p _ { 4 } ( x ) | \leqslant { \frac { 1 } { 1 6 } } , \qquad - 1 \leqslant x \leqslant 1 ,
$$

and

$$
\begin{array} { r } { p _ { 3 } ( x ) = \frac { 1 5 } { 8 } + \frac { 1 9 } { 8 } T _ { 1 } ( x ) + T _ { 2 } ( x ) + \frac { 9 } { 1 6 } T _ { 3 } ( x ) } \end{array}
$$

satisfies

$$
| p ( x ) - p _ { 3 } ( x ) | \leqslant { \frac { 3 } { 1 6 } } , \qquad - 1 \leqslant x \leqslant 1 .
$$

Thus (3.2) provides us with handy approximations of (3.1). We can rewrite

$$
p _ { 3 } ( x ) = { \textstyle { \frac { 7 } { 8 } } } + { \textstyle { \frac { 1 1 } { 1 6 } } } x + 2 x ^ { 2 } + { \textstyle { \frac { 9 } { 4 } } } x ^ { 3 }
$$

and

$$
\begin{array} { r } { p _ { 4 } ( x ) = 1 + \frac { 1 1 } { 1 6 } x + x ^ { 2 } + \frac { 9 } { 4 } x ^ { 3 } + x ^ { 4 } , } \end{array}
$$

which [like the remaining partial sums of (3.2)] are called economizations of (3.1)(cf. Lanczos [1]), but it is by no means necessary to rewrite (3.3) and (3.4) as power polynomials, since they can be evaluated expeditiously in the Chebyshev form (3.2). Let us determine how to do this in general.

# 3.2. Evaluating Polynomials in Chebyshev Form

Let

$$
q ( x ) = A _ { 0 } + A _ { 1 } T _ { 1 } ( x ) + \cdots + A _ { n } T _ { n } ( x ) , \qquad n \geqslant 2 .
$$

$T _ { n } ( x ) = 2 x T _ { n - 1 } ( x ) - T _ { n - 2 } ( x )$ for $n \geqslant 2 ;$ hence

$$
{ \begin{array} { r l } & { q ( x ) = A _ { 0 } + A _ { 1 } T _ { 1 } ( x ) + \cdots + ( A _ { n - 2 } - A _ { n } ) T _ { n - 2 } ( x ) + ( A _ { n - 1 } + 2 x A _ { n } ) } \\ & { \qquad \times T _ { n - 1 } ( x ) } \\ & { \qquad = A _ { 0 } ^ { ( 1 ) } + A _ { 1 } ^ { ( 1 ) } T _ { 1 } ( x ) + \cdots + A _ { n - 2 } ^ { ( 1 ) } T _ { n - 2 } ( x ) + A _ { n - 1 } ^ { ( 1 ) } T _ { n - 1 } ( x ) , } \end{array} }
$$

where $A _ { j } ^ { ( 1 ) } = A _ { j } , ~ j = 0 , ~ . . . , ~ n - 3 , ~ A _ { n - 2 } ^ { ( 1 ) } = A _ { n - 2 } - A _ { n }$ and $A _ { n - 1 } ^ { ( 1 ) } =$ $A _ { n - 1 } + 2 x A _ { n }$ . We now continue to apply the three-term recurrence formula to obtain the general form

$$
q ( x ) = A _ { 0 } ^ { ( k ) } + A _ { 1 } ^ { ( k ) } T _ { 1 } ( x ) + \cdots + A _ { n - k } ^ { ( k ) } T _ { n - k } ( x )
$$

by means of

$$
\begin{array} { r l } & { \quad A _ { j } ^ { ( k ) } = A _ { j } ^ { ( k - 1 ) } , \qquad j = 0 , \ldots , n - ( k + 2 ) , } \\ & { \quad A _ { n - ( k + 1 ) } ^ { ( k ) } = A _ { n - ( k + 1 ) } ^ { ( k - 1 ) } - A _ { n - ( k - 1 ) } ^ { ( k - 1 ) } , } \\ & { \quad \quad A _ { n - k } ^ { ( k ) } = A _ { n - k } ^ { ( k - 1 ) } + 2 x A _ { n - ( k - 1 ) } ^ { ( k - 1 ) } , } \end{array}
$$

as long as $k \leqslant n - 1$ . If we put $B _ { k } = A _ { n - k } ^ { ( k ) }$ ,then we conclude from (3.5) that for $k = n , n - 1 , . . . , 1 ,$

$$
B _ { k } = 2 x B _ { k + 1 } - B _ { k + 2 } + A _ { k } ,
$$

where

$$
B _ { n + 1 } = B _ { n + 2 } = 0 .
$$

When $k = n - 1 ;$ we have

$$
\begin{array} { r l } & { q ( x ) = A _ { 0 } ^ { ( n - 1 ) } + A _ { 1 } ^ { ( n - 1 ) } T _ { 1 } ( x ) } \\ & { \qquad = [ A _ { 0 } ^ { ( n - 2 ) } - A _ { 2 } ^ { ( n - 2 ) } ] + A _ { 1 } ^ { ( n - 1 ) } x } \\ & { \qquad = ( A _ { 0 } - B _ { 2 } ) + B _ { 1 } x , } \end{array}
$$

which yields, after defining $\scriptstyle B _ { 0 }$ by putting $k = 0 ;$ in (3.6),

$$
q ( x ) = \frac { A _ { 0 } } { 2 } + \frac { B _ { 0 } - B _ { 2 } } { 2 } .
$$

Thus

$$
p ( x ) = \sum _ { j = 0 } ^ { n } { } ^ { \prime } A _ { j } T _ { j } ( x ) = { \frac { B _ { 0 } - B _ { 2 } } { 2 } } ,
$$

where $\pmb { B _ { 0 } }$ and $\pmb { B _ { 2 } }$ are determined by the backwards recurrence formula (3.6) with starting conditions (3.7).

In an actual computation using (3.6) errors wil necessarily be introduced because of imprecisions in the $\pmb { A } _ { k }$ or rounding and the impossibility of doing exact arithmetic. Such errors are propagated and compounded by the recurrence. Let us attempt to estimate the resulting error in $p ( { \boldsymbol { x } } )$ (cf. Fox and Parker [1]). Suppose that $\pmb { \varepsilon _ { k } }$ is the local error occurring in computing $\pmb { B _ { k } }$ by (3.6), i.e., the error in $\pmb { B _ { k } }$ , assuming that $B _ { k + 1 } , B _ { k + 2 }$ and $\pmb { A } _ { k }$ are correct. Let $\pmb { E _ { m } ( k ) }$ denote the error in $B _ { m }$ due to exactly one unit error in the $\pmb { k }$ th step $( k \geqslant m )$ .Thus the total error in $B _ { m }$ is given by

$$
\sum _ { k = m } ^ { n } \varepsilon _ { k } E _ { m } ( k ) ;
$$

but $\phantom { } E _ { m } ( k )$ satisfies

$$
E _ { m } ( k ) = 2 x E _ { m + 1 } ( k ) - E _ { m + 2 } ( k )
$$

with $E _ { k + 1 } ( k ) = 0$ and $E _ { k } ( k ) = 1$

The three-term recurrence (3.11) has as solution

$$
E _ { m } ( k ) = A T _ { m } ( x ) + B U _ { m } ( x ) ,
$$

and the boundary conditions then imply that

$$
E _ { m } ( k ) = \frac { U _ { k + 1 } ( x ) T _ { m } ( x ) - T _ { k + 1 } ( x ) U _ { m } ( x ) } { U _ { k + 1 } ( x ) T _ { k } ( x ) - U _ { k } ( x ) T _ { k + 1 } ( x ) } .
$$

This last expression can be considerably simplified by using the appropriate trigonometric identities and we obtain

$$
E _ { m } ( k ) = U _ { k - m } ( x ) .
$$

Thus, in view of (3.9)and (3.10), the eror in $p ( { \boldsymbol { x } } )$ is bounded by

$$
\frac { 1 } { 2 } \biggl [ | \varepsilon _ { 0 } E _ { 0 } ( 0 ) | + | \varepsilon _ { 1 } E _ { 0 } ( 1 ) | + \sum _ { k = 2 } ^ { n } | \varepsilon _ { k } ( E _ { 0 } ( k ) - E _ { 2 } ( k ) ) | \biggr ] ,
$$

and since $E _ { 0 } ( k ) - E _ { 2 } ( k ) = U _ { k } ( x ) - U _ { k - 2 } ( x ) = 2 T _ { k } ( x ) ,$ we obtain, finally, the bound

$$
\sum _ { k = 0 } ^ { n } | \varepsilon _ { k } | .
$$

Thus the proposed method is stable in the sense that the resulting error is no larger than the sum of the absolute values of the local errors.

If $p ( { \boldsymbol { x } } )$ in (3.9) is an even function,

$$
p ( x ) = \sum _ { j = 0 } ^ { m } A _ { 2 j } T _ { 2 j } ( x ) ,
$$

then, since $T _ { 2 j } ( x ) = T _ { j } ( T _ { 2 } ( x ) ) = T _ { j } ( 2 x ^ { 2 } - 1 ) { \mathrm { , } }$ ，we need only put $t = 2 x ^ { 2 } - 1$ and evaluate

$$
p ( x ) = \sum _ { j = 0 } ^ { m } D _ { j } T _ { j } ( t )
$$

by (3.9), where $D _ { j } = A _ { 2 j } , j = 0 , . . . , m .$

f $p ( { \boldsymbol { x } } )$ is given by (3.12), then

$$
x p ( x ) = \sum _ { j = 0 } ^ { m } \spadesuit A _ { 2 j } \frac { T _ { [ 2 j - 1 | } ( x ) + T _ { 2 j + 1 } ( x ) } { 2 } = \sum _ { j = 0 } ^ { m } C _ { 2 j + 1 } T _ { 2 j + 1 } ( x ) ,
$$

where

$$
C _ { 2 j + 1 } = { \frac { A _ { 2 j } + A _ { 2 j + 2 } } { 2 } } , \qquad j = 0 , \ldots , m , \qquad A _ { 2 m + 2 } = 0 .
$$

If $t = 2 x ^ { 2 } - 1$ and $p ( { \boldsymbol { \mathbf { x } } } ) _ { : }$ ,writen in the form (3.13)is evaluated by

$$
B _ { k } = 2 t B _ { k + 1 } - B _ { k + 2 } + D _ { k } , \qquad B _ { m + 1 } = B _ { m + 2 } = 0 ,
$$

then

$$
\sum _ { j = 0 } ^ { m } C _ { 2 j + 1 } T _ { 2 j + 1 } ( x ) = x { \frac { B _ { 0 } - B _ { 2 } } { 2 } } .
$$

If, however, we consider the recurrence

$$
\beta _ { k } = 2 t \beta _ { k + 1 } - \beta _ { k + 2 } + C _ { 2 k + 1 } , \qquad \beta _ { m + 1 } = \beta _ { m + 2 } = 0 ,
$$

which is obtained by putting $\beta _ { k } = ( B _ { k } + B _ { k + 1 } ) / 2$ in (3.14)， then $( B _ { 0 } - B _ { 2 } ) / 2 = \beta _ { 0 } - \beta _ { 1 }$ .Thus the odd polynomial in (3.15) has the value $x ( \beta _ { 0 } - \beta _ { 1 } ) ,$ which is calculable by the recurrence formula (3.16).

# EXERCISES 3.2.1-3.2.5

3.2.1. Suppose the coefficients of $p ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { n } x ^ { n }$ satisfy $0 < a _ { 0 }$ $< a _ { 1 } < \cdots < a _ { n }$ . Show that all zeros of $p ( { \boldsymbol { x } } )$ lie in $| z | < 1$

Hint. Consider $q ( x ) = x ^ { n } p ( 1 / x ) = a _ { n } + a _ { n - 1 } x + \cdots + a _ { 0 } x ^ { n }$ . It sufices to show that $q ( z )$ has no zero in $| z | \leqslant 1$ But when $| z | \leqslant 1 , ( z \neq 1 )$ ，

$$
\begin{array} { r l } & { | ( 1 - z ) q ( z ) | = | a _ { n } - ( a _ { n } - a _ { n - 1 } ) z - \cdots - ( a _ { 1 } - a _ { 0 } ) z ^ { n } - a _ { 0 } z ^ { n + 1 } | } \\ & { ~ \geqslant a _ { n } - | ( a _ { n } - a _ { n - 1 } ) z + \cdots + ( a _ { 1 } - a _ { 0 } ) z ^ { n } + a _ { 0 } z ^ { n + 1 } | } \\ & { ~ > a _ { n } - ( ( a _ { n } - a _ { n - 1 } ) + \cdots + ( a _ { 1 } - a _ { 0 } ) + a _ { 0 } ) = 0 , } \end{array}
$$

thelast iequality being aconsequence of the positivity of $a _ { n } - a _ { n - 1 } , \ldots , ( a _ { 1 } - a _ { 0 } ) , a _ { 0 } .$ The result for ${ \pmb q } ( { \pmb x } )$ is called the Enestrom-Kakeya theorem.

In the next few exercises we give an analog of Exercise 3.2.1 for a polynomial represented in a basis of Chebyshev polynomials, rather than the conventional power basis. The result is due to Szego [4].

3.2.2. Verify that if $0 \leqslant \theta \leqslant 2 \pi$

$$
\sum _ { k = 0 } ^ { n } \sin ( k + { \scriptstyle { \frac { 1 } { 2 } } } ) \theta = { \frac { 1 - \cos ( n + 1 ) \theta } { 2 \sin \theta / 2 } } , \qquad n = 0 , 1 , 2 , \ldots .
$$

Hint. Multiply both sides by $2 \sin ( \theta / 2 )$

3.2.3. Suppose that $0 \leqslant A _ { 0 } \leqslant A _ { 1 } \leqslant \cdots \leqslant A _ { n - 1 } < A _ { n } ,$

$$
t ( \theta ) = A _ { 0 } + A _ { 1 } \cos \theta + \cdots + A _ { n } \cos n \theta
$$

and

$$
s ( \theta ) = A _ { 1 } \sin \theta + \cdots + A _ { n } \sin n \theta .
$$

Show that

$$
t ( \theta ) \sin ( n + { \frac { 1 } { 2 } } ) \theta - s ( \theta ) \cos ( n + { \frac { 1 } { 2 } } ) \theta = \sum _ { k = 0 } ^ { n } A _ { k } \sin ( n - k + { \frac { 1 } { 2 } } ) \theta , \qquad 0 \leqslant \theta \leqslant 2 \pi .
$$

$$
\begin{array} { r } { t ( \theta ) \sin { ( n + \frac { 1 } { 2 } ) } \theta - s ( \theta ) \cos { ( n + \frac { 1 } { 2 } ) } \theta = - \operatorname { I m } { ( e ^ { - i ( n + 1 / 2 ) \theta } ( t ( \theta ) + i s ( \theta ) ) . } } \end{array}
$$

3.2.4. If $0 \leqslant A _ { 0 } \leqslant A _ { 1 } \leqslant \cdots \leqslant A _ { n - 1 } < A _ { n }$ show that

$$
\sum _ { k = 0 } ^ { n } A _ { k } \sin { ( n - k + \frac { 1 } { 2 } ) } \theta > 0 , 0 < \theta < 2 \pi .
$$

Hint. The sum in question may be writen as

$$
\sum _ { k = 0 } ^ { n } A _ { n - k } \sin { ( k + { \frac { 1 } { 2 } } ) } \theta = \sigma _ { 0 } ( \theta ) ( A _ { n } - A _ { n - 1 } ) + \cdots + \sigma _ { n - 1 } ( \theta ) ( A _ { 1 } - A _ { 0 } ) + \sigma _ { n } ( \theta ) A _ { 0 } ,
$$

where

$$
\sigma _ { j } ( \theta ) = \sum _ { k = 0 } ^ { j } \sin { ( k + \frac { 1 } { 2 } ) } \theta , \qquad j = 0 , 1 , . . . , n .
$$

But ${ \pmb \sigma } _ { j } ( \theta )$ is positive for $j = 0 , 1 , . . . , n$ and $0 < \theta < \pi$ in view of Exercise 3.2.2 and $A _ { n } > A _ { n - 1 }$

3.2.5. Suppose the coefficientsof $p ( x ) = A _ { 0 } + A _ { 1 } T _ { 1 } ( x ) + \cdots + A _ { n } T _ { n } ( x )$ satisfy $0 \leqslant A _ { 0 } \leqslant A _ { 1 } \leqslant \cdots \leqslant A _ { n - 1 } < A _ { n }$ .Show that all the zeros of $p ( { \boldsymbol { x } } )$ are distinct and lie in $( - 1 , 1 )$ Moreover, if $x _ { 1 } , \ldots , x _ { n }$ are the zeros, arranged in increasing order, then

$$
\begin{array} { r } { \begin{array} { r l } { \quad } & { { } \quad \Big | } \\ { \eta _ { 2 j + 1 } ^ { ( 2 n + 1 ) } < x _ { j } < \eta _ { 2 j - 1 } ^ { ( 2 n + 1 ) } , \quad } & { j = 1 , 2 , . . . , n . } \end{array} } \end{array}
$$

Hint. In view of Exercises 3.2.3 and 3.2.4, if we put $t ( \theta ) = p ( \cos { \theta } )$

$$
\begin{array} { r } { p ( \cos { \theta } ) \sin { ( n + \frac { 1 } { 2 } ) } \theta - s ( \theta ) \cos { ( n + \frac { 1 } { 2 } ) } \theta > 0 , \qquad 0 < \theta < \pi . } \end{array}
$$

Let $\theta _ { j } = ( ( 2 j - 1 ) / ( 2 n + 1 ) ) \pi , \ j = 1 , \ldots , n ,$ then we obtain $( - 1 ) ^ { j } p ( \eta _ { 2 j - 1 } ^ { ( n ) } ) > 0 ,$ ，which yields the desired results.

Note that a similar result follows, from the same inequality，, for $\pmb q ( \pmb x ) = \pmb B _ { 0 }$ ${ } + B _ { 1 } U _ { 1 } ( x ) + \cdots + B _ { n - 1 } U _ { n - 1 } ( x )$ when $0 \leqslant B _ { 0 } \leqslant B _ { 1 } \leqslant \cdots \leqslant B _ { n - 2 } < B _ { n - 1 }$ .Namely, the zeros of $q ( x ) , y _ { 1 } , . . . , y _ { n - 1 } ,$ must satisfy

$$
\eta _ { 2 j + 2 } ^ { ( 2 n + 1 ) } < y _ { j } < \eta _ { 2 j } ^ { ( 2 n + 1 ) } , \qquad j = 1 , \ldots , n - 1 .
$$

These striking results follow from the positivity of the trigonometric sum in Exercise 3.2.2.Some later variations on this theme may be found in Askey and Steinig [1].

# 3.3. Chebyshev Series

We call an infinite series of the form

$$
{ \frac { B _ { 0 } } { 2 } } + B _ { 1 } T _ { 1 } ( x ) + \cdots + B _ { n } T _ { k } ( x ) + \cdots
$$

a Chebyshev series.If

$$
\sum _ { k = 0 } ^ { \infty } \left| B _ { k } \right| < \infty ,
$$

then the series (3.12) is absolutely convergent for each $\pmb { x }$ on $I \colon [ - 1 , 1 ]$ and is also uniformly convergent on $\pmb { I }$ (by the Weierstrass $\pmb { M }$ test), so that the series (3.17) converges to a function continuous on $I .$ If we denote the set of absolutely convergent Chebyshev series, i.e., series (3.17) satisfying (3.18), by $A ( I )$ and denote the set of uniformly convergent Chebyshev series by $U ( I ) ,$ then $A ( I ) \subset U ( I ) .$ However, $A ( I ) \neq U ( I )$ ，We show this by the following example.

Let $\pmb { z }$ be a complex variable and put

$$
f _ { 1 } ( z ) = 1 + z , \qquad g _ { 1 } ( z ) = 1 - z .
$$

We define two sequences of polynomials $f _ { 1 } , f _ { 2 } , \ldots ,$ and $g _ { 1 } , g _ { 2 } , \ldots$ ,by

$$
\begin{array} { l l } { { f _ { n + 1 } = f _ { n } + z ^ { 2 ^ { n } } g _ { n } , } } & { { \quad n = 1 , 2 , \ldots , } } \\ { { { } } } & { { { } } } \\ { { g _ { n + 1 } = f _ { n } - z ^ { 2 ^ { n } } g _ { n } , } } & { { \quad n = 1 , 2 , \ldots . } } \end{array}
$$

It is easy to establish, by mathematical induction that $f _ { n }$ and ${ \pmb g } _ { \pmb n }$ are polynomials of degree $2 ^ { n } - 1$ with coefficients that are $\pm 1 .$ Moreover, given

$f _ { n } ,$ the first $2 ^ { n }$ coefficients of $f _ { n + 1 }$ are precisely the coefficients of $f _ { n } ,$ whereas the next $2 ^ { n }$ are obtained by recopying the first $2 ^ { n - 1 }$ coefficients of $f _ { n } ,$ followed by the negatives of the next $2 ^ { n - 1 }$ coefficients of $f _ { n }$ . Thus we have,for example,

$$
\begin{array} { l } { { f _ { 1 } ( z ) = 1 + z , \quad f _ { 2 } ( z ) = 1 + z + z ^ { 2 } - z ^ { 2 } , } } \\ { { f _ { 3 } ( z ) = 1 + z + z ^ { 2 } - z ^ { 3 } + z ^ { 4 } + z ^ { 5 } - z ^ { 6 } + z ^ { 7 } ; } } \\ { { f _ { 4 } ( z ) = 1 + z + z ^ { 2 } - z ^ { 3 } + z ^ { 4 } + z ^ { 5 } - z ^ { 6 } + z ^ { 7 } + z ^ { 8 } + z ^ { 9 } + z ^ { 1 0 } - z ^ { 1 1 } } } \\ { { \qquad - z ^ { 1 2 } - z ^ { 1 3 } + z ^ { 1 4 } - z ^ { 1 5 } . } } \end{array}
$$

In this fashion we obtain an infinite series

$$
\varepsilon _ { 0 } + \varepsilon _ { 1 } z + \cdots + \varepsilon _ { k } z ^ { k } + \cdots
$$

with $\pm _ { k } = \pm 1$ and

$$
f _ { n } ( z ) = \sum _ { k = 0 } ^ { 2 ^ { n } - 1 } \varepsilon _ { k } z ^ { k } .
$$

This series was first considered by Shapiro [1]. We denote the partial sums of this series by

$$
{ \mathcal { S } } _ { k } ( z ) = \sum _ { j = 0 } ^ { k } \varepsilon _ { j } z ^ { j } , \qquad k = 1 , 2 , . . . .
$$

The Shapiro polynomials have the following remarkable property (cf. Rudin [1]).

Lemma 3.3.1. For $\pmb { n = 1 , 2 , \dots }$ , and $0 \leqslant \theta < 2 \pi ,$

$$
| { \mathcal { S } } _ { n } ( e ^ { i \theta } ) | \leqslant 5 n ^ { 1 / 2 } .
$$

Proof. We recall the identity for complex numbers

$$
| \alpha + \beta | ^ { 2 } + | \alpha - \beta | ^ { 2 } = 2 [ | \alpha | ^ { 2 } + | \beta | ^ { 2 } ] ,
$$

which yields,in viewof (3.19),for $| z | = 1 , k = 1 , 2 , \ldots ,$

$$
\begin{array} { c } { { | f _ { k + 1 } ( z ) | ^ { 2 } + | g _ { k + 1 } ( z ) | ^ { 2 } = | f _ { k } ( z ) + z ^ { 2 ^ { k } } g _ { k } ( z ) | ^ { 2 } + | f _ { k } ( z ) - z ^ { 2 ^ { k } } g _ { k } ( z ) | ^ { 2 } } } \\ { { { } } } \\ { { = 2 [ | f _ { k } ( z ) | ^ { 2 } + | g _ { k } ( z ) | ^ { 2 } ] . } } \end{array}
$$

Since (for $| z | = 1 \AA$ $| f _ { 1 } ( z ) | ^ { 2 } + | g _ { 1 } ( z ) | ^ { 2 } = | 1 + z | ^ { 2 } + | 1 - z ^ { 2 } | = 2 ^ { 2 }$ , we obtain for $| z | = 1$ and $k = 1 , 2 , \ldots$ ，

$$
| f _ { k } ( z ) | ^ { 2 } + | g _ { k } ( z ) | ^ { 2 } = 2 ^ { k + 1 } .
$$

Thus, surely,

$$
| f _ { k } ( e ^ { i \theta } ) | \leqslant 2 ^ { 1 / 2 } 2 ^ { k / 2 } ,
$$

which, since

$$
f _ { k } = \mathcal { S } _ { 2 ^ { k } - 1 } ,
$$

-establishes (3.21) for $\displaystyle n = 2 ^ { k } - 1 , k = 1 , 2 , \ldots .$

Let ${ \mathcal { R } } _ { n } ( z )$ be the partial sum of order $n \geqslant 1$ of $g _ { k } ( z ) _ { i }$ where $n \leqslant 2 ^ { k } - 1$ We claim that if $1 \leqslant n \leqslant 2 ^ { k } - 1$

$$
\begin{array} { r } { | \mathcal { S } _ { n } ( e ^ { i \theta } ) | \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { k / 2 } , } \\ { | \mathcal { R } _ { n } ( e ^ { i \theta } ) | \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { k / 2 } . } \end{array}
$$

To verify this we use mathematical induction on $\pmb { k }$ Formula (3.23) obviously holds for $k = 1$ 、Suppose it holds for $\pmb { k }$ and suppose $1 \leqslant n \leqslant 2 ^ { k + 1 } - 1 .$ if $n \leqslant 2 ^ { k } - 1$ $1 , | \mathcal { S } _ { n } | = | \mathcal { R } _ { n } | \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { k / 2 } \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { ( k + 1 ) / 2 }$ by the inductive hypothesis,whereas if $2 ^ { k } \leqslant n \leqslant 2 ^ { k + 1 } - 1$

$$
| \mathcal { S } _ { n } | \leqslant | f _ { k } | + | \mathcal { R } _ { n - 2 ^ { k } } | \leqslant 2 ^ { ( k + 1 ) / 2 } + ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { k / 2 } \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { ( k + 1 ) / 2 }
$$

and

$$
| \mathcal { R } _ { n } | \leqslant | f _ { k } | + | \mathcal { R } _ { n - 2 ^ { k } } | \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { ( k + 1 ) / 2 } ,
$$

in view of (3.19), (3.22), and the inductive hypothesis (since $n - 2 ^ { k } \leqslant 2 ^ { k } - 1 \}$ Thus (3.23) is established,and if $2 ^ { k - 1 } \leqslant n \leqslant 2 ^ { k } - 1$

$$
| \mathcal { S } _ { n } ( e ^ { i \theta } ) | \leqslant ( 2 + 2 ^ { 1 / 2 } ) 2 ^ { k / 2 } \leqslant 2 ^ { 1 / 2 } ( 2 + 2 ^ { 1 / 2 } ) n ^ { 1 / 2 } \leqslant 5 n ^ { 1 / 2 } . \quad
$$

We have calld this result remarkable, since any polynomial of degree $\pmb { n }$ ， $p ( z ) = a _ { 0 } + \cdots + a _ { n } z ^ { n } ;$ ，with all coefficients of absolute value 1, satisfies

$$
{ \frac { 1 } { 2 \pi } } \int _ { 0 } ^ { 2 \pi } | p ( e ^ { i \theta } ) | ^ { 2 } d \theta = | a _ { 0 } | ^ { 2 } + \cdots + | a _ { n } | ^ { 2 } = n + 1 ,
$$

hence

$$
\operatorname* { m a x } _ { 0 \leqslant \theta < 2 \pi } | p ( e ^ { i \theta } ) | \geqslant ( n + 1 ) ^ { 1 / 2 } > n ^ { 1 / 2 } .
$$

Thus the Shapiro polynomials exhibit extremely small norm on the unit circle. With the $\varepsilon _ { j }$ as defined above we can now give our example.

# Theorem 3.1

$$
\sum _ { k = 1 } ^ { \infty } { \frac { \varepsilon _ { k } } { k } } \ T _ { k } ( x )
$$

is uniformly convergent on $I _ { \cdot }$ ，but not absolutely convergent.

Proof. Consider

$$
\begin{array} { r l } { \displaystyle \sum _ { k = n } ^ { n + m } \frac { 1 } { k } \varepsilon _ { k } e ^ { i k \theta } = \displaystyle \sum _ { k = n } ^ { n + m } \frac { 1 } { k } \left( \mathcal { S } _ { k } ( e ^ { i \theta } ) - \mathcal { S } _ { k - 1 } ( e ^ { i \theta } ) \right) } & { { } } \\ { = \displaystyle \frac { \mathcal { S } _ { n + m } ( e ^ { i \theta } ) } { n + m } - \frac { \mathcal { S } _ { n - 1 } ( e ^ { i \theta } ) } { n } } & { { } } \\ { + \displaystyle \sum _ { j = 0 } ^ { m - 1 } \mathcal { S } _ { n - j } ( e ^ { i \theta } ) \frac { 1 } { ( n + j ) ( n + j + 1 ) } . } & { { } } \end{array}
$$

Then applying (3.21) and the triangle inequality yields

$$
\left| \sum _ { k = n } ^ { n + m } \frac { 1 } { k } \ : \varepsilon _ { k } \ : e ^ { i k \theta } \right| \leqslant \frac { 1 0 } { n ^ { 1 / 2 } } + 5 \ : \sum _ { j = 1 } ^ { m } \frac { 1 } { ( n + j ) ^ { 3 / 2 } } \leqslant \frac { 1 0 } { n ^ { 1 / 2 } } + 5 \ : \sum _ { k = n + 1 } ^ { \infty } \frac { 1 } { k ^ { 3 / 2 } } ,
$$

but

$$
\sum _ { k = n + 1 } ^ { \infty } { \frac { 1 } { k ^ { 3 / 2 } } } \leqslant \int _ { n } ^ { \infty } x ^ { - 3 / 2 } d x = { \frac { 2 } { n ^ { 1 / 2 } } } ,
$$

so that

$$
\left| \sum _ { k = n } ^ { n + m } \frac { 1 } { k } \ : \varepsilon _ { k } e ^ { i k \theta } \right| \leqslant \frac { 2 0 } { n ^ { 1 / 2 } } .
$$

Since $| \pmb { \mathrm { R e } } z | \leqslant | z |$ for complex numbers, we have

$$
\left| \sum _ { k = n } ^ { n + m } \frac { 1 } { k } \ : \varepsilon _ { k } \cos k \theta \right| \leqslant \frac { 2 0 } { n ^ { 1 / 2 } } ,
$$

and putting $\boldsymbol { x } = \cos { \theta }$ we obtain the uniform convergence of (3.24). The failure of absolute convergence is obvious, since $| \pmb { \varepsilon } _ { j } | = 1$ for all $j$

To each function $f ( x ) ,$ integrable on $I _ { \ast }$ ，there is associated its Chebyshev expansion, a relationship we denote by

$$
f ( x ) \sim \sum _ { k = 0 } ^ { \infty } \spadesuit A _ { k } T _ { k } ( x ) ,
$$

where

$$
A _ { k } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } f ( x ) T _ { k } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } , \qquad k = 0 , 1 , \ldots .
$$

If a Chebyshev series (3.17) converges uniformly on $\pmb { I }$ and its sum is called ${ \pmb g } ( { \pmb x } ) ,$ then $g ( x ) \in C ( I )$ and the series is the Chebyshev expansion of ${ \pmb g } _ { : }$ for if

$$
g ( x ) = \sum _ { k = 0 } ^ { \infty } { B _ { k } T _ { k } ( x ) }
$$

then uniform convergence implies that

$$
\frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \dot { g } ( x ) T _ { m } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = B _ { m } , \qquad m = 0 , 1 , . . . ,
$$

in view of the orthogonality of the Chebyshev polynomials. However, not every Chebyshev series is a Chebyshev expansion, for by the Riemann-Lebesgue lemma (cf. Zygmund [1, I, p. 45].) the coefficients in a Chebyshev expansion must satisfy $\scriptstyle \operatorname* { l i m } _ { k \to \infty } A _ { k } = 0$

Given $f \in C ( I ) ,$ we put

$$
s _ { n } ( f ; x ) = s _ { n } ( x ) = \sum _ { k = 0 } ^ { n } A _ { k } T _ { k } ( x ) ;
$$

$s _ { n } ( f ; x )$ is the nth partial sum of the Chebyshev expansion of $f$ and certainly $s _ { n } ( x ) \in \mathcal { P } _ { n } . ~ s _ { n } ( f )$ is a linear operator which has an explicit expression. If $\boldsymbol { x } \in \boldsymbol { I }$ put $\begin{array} { r } { \mathbf { \boldsymbol { x } } = \cos \theta , } \end{array}$ ， $0 \leqslant \theta \leqslant \pi ,$ ， then $f ( x ) = f ( \cos \theta ) = F ( \theta )$ is defined on $[ 0 , \pi ]$ and we extend its definition to $[ - \pmb { \pi } , \pmb { 0 } ]$ by $F ( - \theta ) = F ( \theta )$ . Thus we may consider $F ( \theta )$ to be defined for all $\pmb \theta$ and have period $2 \pi$ .Now

$$
\begin{array} { l } { { \displaystyle s _ { n } ( x ) = s _ { n } ( f ; \cos \theta ) = \frac { 1 } { \pi } \sum _ { k = 0 } ^ { n } \int _ { - \pi } ^ { \pi } F ( \varphi ) \cos k \varphi \cos k \theta d \varphi } } \\ { { \displaystyle ~ = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } F ( \varphi ) \biggl [ \sum _ { k = 0 } ^ { n } \frac { \cos k ( \varphi + \theta ) + \cos k ( \varphi - \theta ) } { 2 } \biggr ] d \varphi } } \\ { { \displaystyle ~ = \frac { 1 } { \pi } \int _ { - \pi } ^ { \pi } F ( \varphi ) \biggl [ \sum _ { k = 0 } ^ { n } \cos k ( \varphi + \theta ) \biggr ] d \varphi , } } \end{array}
$$

where in the first and last steps we use the evenness of $\pmb { F }$ . It is easy to verify that

$$
2 \sin { \frac { u } { 2 } } \sum _ { k = 0 } ^ { n } { \cos { k u } } \equiv \sin { ( n + \frac { 1 } { 2 } ) } u ,
$$

and therefore

$$
s _ { n } ( x ) = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } F ( \varphi ) { \frac { \sin \left[ ( n + { \frac { 1 } { 2 } } ) ( \varphi + \theta ) \right] } { 2 \sin \left( \varphi + \theta \right) / 2 } } d \varphi .
$$

Since $s _ { n } ( f )$ is obtainable in this relatively simple manner, we may ask how well it serves as a polynomial approximation to $f$ on I. A first observation is that $s _ { n } ( f ; x )$ is the least squares approximation to $f$ with respect to the weight function $( 1 - x ^ { 2 } ) ^ { - 1 / 2 }$

Theorem 3.2. Given $f \in C ( I ) ,$

$$
\int _ { - 1 } ^ { 1 } { [ f ( x ) - s _ { n } ( f ; x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } \leqslant \int _ { - 1 } ^ { 1 } { [ f ( x ) - p ( x ) ] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } }
$$

for every $\pmb { p } \in \mathcal { P } _ { \pmb { n } } .$ ， with equality holding only for $\pmb { p } = s _ { n } ( f ) .$

Proof. Let $p ( x ) = B _ { 0 } / 2 + B _ { 1 } T _ { 1 } ( x ) + \cdots + B _ { n } T _ { n } ( x ) ;$ then

$$
\begin{array} { c } { { { \displaystyle \int _ { - 1 } ^ { 1 } ~ [ f ( x ) - p ( x ) ] ^ { 2 } { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } = \int _ { - 1 } ^ { 1 } ~ [ f ^ { 2 } ( x ) - 2 p ( x ) f ( x ) + p ^ { 2 } ( x ) ] ~ { \frac { d x } { \sqrt { 1 - x } } } } } } \\ { { { = \displaystyle \int _ { - 1 } ^ { 1 } f ^ { 2 } ( x ) { \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } - \pi ~ { \underset { k = 0 } { \overset { n } { \sum } } } ^ { \prime } A _ { k } B _ { k } + { \frac { \pi } { 2 } } ~ { \underset { k = 0 } { \overset { n } { \sum } } } ^ { \prime } B _ { k } ^ { 2 } . } } } \end{array}
$$

If we use this formula for $\boldsymbol { p } = \pmb { S _ { n } }$ as well as for arbitrary $\pmb { p } ;$ ， we obtain

$$
\begin{array} { l } { \displaystyle \int _ { - 1 } ^ { 1 } \left[ f ( x ) - p ( x ) \right] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } - \int _ { - 1 } ^ { 1 } \left[ f ( x ) - s _ { n } ( x ) \right] ^ { 2 } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } \\ { \displaystyle \phantom { \frac { 1 } { 1 } } = \frac { \pi } { 2 } \sum _ { k = 0 } ^ { n } ( B _ { k } - A _ { k } ) ^ { 2 } , } \end{array}
$$

which proves the theorem.

# 3.4. The Relationship of ${ \pmb S } _ { \pmb { \mathrm { \pmb { \ n } } } }$ t0 $\pmb { { \cal E } } _ { \pmb { \mathrm { \imath } } }$

We wish to investigate the relationship between $s _ { n } ( f )$ and the best uniform approximation to $f .$

If $f \in C ( I ) ,$ we put

$$
S _ { n } ( f ) = \| f - s _ { n } ( f ) \| \qquad { \mathrm { a n d } } \qquad E _ { n } ( f ) = \| f - p _ { n } ^ { * } \| ,
$$

where $\pmb { p _ { n } ^ { * } }$ is the best uniform approximation on $\pmb { I }$ to $f$ out of $\mathcal { P } _ { n } \left( \parallel \cdot \parallel \right.$ denotes the uniform norm).

# Theorem 3.3

$$
E _ { n } ( f ) \leqslant S _ { n } ( f ) < \left( 4 + { \frac { 4 } { \pi ^ { 2 } } } \log n \right) E _ { n } ( f ) .
$$

Proof.

$$
\begin{array} { r l r } & { } & { | f - s _ { n } ( f ) | = | f - p _ { n } ^ { * } + p _ { n } ^ { * } - s _ { n } ( f ) | } \\ & { } & { \quad \quad = | f - p _ { n } ^ { * } + s _ { n } ( p _ { n } ^ { * } - f ) | } \\ & { } & { \quad \quad \leqslant E _ { n } ( f ) + | s _ { n } ( p _ { n } ^ { * } - f ) | , } \end{array}
$$

but, according to (3.27),

$$
s _ { n } ( g ; \cos \theta ) = \frac { 1 } { 2 \pi } \int _ { 0 } ^ { \pi } \left[ G ( \varphi + \theta ) + G ( \varphi - \theta ) \right] \frac { \sin { ( ( 2 n + 1 ) / 2 ) \varphi } } { \sin { ( \varphi / 2 ) } } d \varphi ,
$$

and applying (3.29) with $g = p _ { n } ^ { * } - f$ yields

$$
| s _ { n } ( p _ { n } ^ { * } - f ) | \leqslant E _ { n } ( f ) \cdot { \frac { 1 } { \pi } } \int _ { 0 } ^ { \pi } { \frac { | \sin { ( ( 2 n + 1 ) / 2 ) } \varphi | } { \sin { ( \varphi / 2 ) } } } d \varphi .
$$

The numbers

$$
L _ { n } = \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } \frac { | \sin { ( ( 2 n + 1 ) / 2 ) } \varphi | } { \sin { ( \varphi / 2 ) } } d \varphi
$$

are known as the Lebesgue constants (of Fourier series theory) and it can be shown (cf. Rivlin [1]) that they satisfy the inequality

$$
L _ { n } < 3 + { \frac { 4 } { \pi ^ { 2 } } } \log n ,
$$

whereupon the theorem is proved.

This theorem informs us that the loss in using $s _ { n } ( f )$ as a best approximation rather than $\pmb { p _ { n } ^ { * } }$ is small for an arbitrary continuous $f \circ \mathfrak { n } [ - 1 , 1$ . It also provides us with a convergence criterion for Chebyshev expansions if we recall Jackson's theorem (cf. Rivlin [1]); namely, if $f ( x )$ is defined on $[ a , b ]$ we put

$$
\omega ( f ; [ a , b ] ; \delta ) = \omega ( \delta ) = \operatorname* { s u p } _ { \stackrel { x _ { 1 } , x _ { 2 } \in [ a , b ] } { | x _ { 1 } - x _ { 2 } | \leqslant \delta } } | f ( x _ { 1 } ) - f ( x _ { 2 } ) | ;
$$

$\omega ( \delta )$ is called the modulus of continuity of $f$ and is defined for $\delta > 0$ It is clear that $f$ is continuous on $[ a , b ]$ if, and only if, $\omega ( \delta ) \to 0$ as ${ \pmb \delta } \to { \bf 0 } .$ Jackson's

theorem asserts that if $f \in C ( I )$ then $E _ { n } ( f ) \leqslant 6 \omega ( n ^ { - 1 } ) ;$ hence,in view of (3.28), we obtain the following.

Theorem 3.4 (Dini-Lipschitz Test). If $f \in C ( I )$ satisfies

$$
\operatorname* { l i m } _ { n \to \infty } ( \log n ) \omega \left( { \frac { 1 } { n } } \right) = 0 ,
$$

then $s _ { n } ( f )$ converges uniformly to $f$ in $\pmb { I }$

In particular, if $f$ satisfies a Lipschitz condition of order $\alpha ( 0 < \alpha \leqslant 1 )$ its Chebyshev expansion is uniformly convergent in $\pmb { I }$

# EXERCISES 3.4.1-3.4.7

# 3.4.1. Verify the following Chebyshev expansions:

$$
\frac { 1 } { a ^ { 2 } - x ^ { 2 } } = \frac { 2 } { a \sqrt { a ^ { 2 } - 1 } } \sum _ { j = 0 } ^ { \infty } ( a - \sqrt { a ^ { 2 } - 1 } ) ^ { 2 j } T _ { 2 j } ( x ) , \qquad a ^ { 2 } > 1 .
$$

$$
\operatorname { s g n } x = \frac { 4 } { \pi } \sum _ { j = 1 } ^ { \infty } \ ( - 1 ) ^ { j - 1 } \frac { T _ { 2 j - 1 } ( x ) } { 2 j - 1 } .
$$

$$
( 1 - x ^ { 2 } ) ^ { 1 / 2 } = \frac { 2 } { \pi } - \frac { 4 } { \pi } \sum _ { j = 1 } ^ { \infty } \frac { 1 } { 4 j ^ { 2 } - 1 } T _ { 2 j } ( x ) .
$$

$$
e ^ { x } = J _ { 0 } ( i ) + 2 \sum _ { k = 1 } ^ { \infty } i ^ { k } J _ { k } ( - i ) T _ { k } ( x ) .
$$

$( J _ { k } ( { \boldsymbol { x } } )$ is the Bessel function of order $\pmb { k }$

(f）If ${ \pmb a } , { \pmb b }$ are nonnegative integers and ${ \pmb a } > { \bf 0 }$ , then for $| t | < 1$

$$
\frac { T _ { b } ( x ) - t T _ { b - a } ( x ) } { 1 + t ^ { 2 } - 2 t T _ { a } ( x ) } = \sum _ { k = 1 } ^ { \infty } ~ t ^ { j } T _ { a j + b } ( x ) .
$$

$$
\frac { 1 } { x - a } = ( a ^ { 2 } - 1 ) ^ { - 1 / 2 } - 2 ( a ^ { 2 } - 1 ) ^ { - 1 / 2 } \sum _ { j = 0 } ^ { \infty } ( a - ( a ^ { 2 } - 1 ) ^ { 1 / 2 } ) ^ { j } T _ { j } ( x ) ; a > 1 .
$$

3.4.2. (Johnson and Riess [1]) If $f$ has an absolutely convergent Chebyshev expansion, then $L _ { n } ( f , T ; x )$ converges uniformly to $f$ on $\pmb { I }$ (cf. Theorem 1.7).

Hint.Use Exercise 1.3.3 to show that

$$
| f ( x ) - L _ { n } ( f , T ; x ) | \leqslant 2 \sum _ { i = n + 1 } ^ { \infty } | A _ { i } | .
$$

3.4.3. Let

$$
\sigma _ { n } ( f ; x ) = { \frac { s _ { 0 } ( f ; x ) + \dots + s _ { n } ( f ; x ) } { n + 1 } } .
$$

Show that

$$
\sigma _ { n } ( f ; \cos \theta ) = \frac { 1 } { \pi } \int _ { 0 } ^ { \pi } \frac { F ( \varphi + \theta ) + F ( \varphi - \theta ) } { 2 } K _ { n } ( \varphi ) d \varphi ,
$$

where

$$
K _ { n } ( \varphi ) = \frac { 1 } { n + 1 } \left( \frac { \sin \displaystyle \frac { n + 1 } { 2 } \varphi } { \sin \displaystyle \frac { \varphi } { 2 } } \right) ^ { 2 } ,
$$

and $F ( t ) = f ( \cos t ) . \ K _ { n } ( \varphi )$ satisfies

$$
\frac { 1 } { \pi } \int _ { 0 } ^ { \pi } K _ { n } ( \varphi ) d \varphi = 1 .
$$

# 3.4.4. Show that

$$
\sigma _ { n } ( f ; x ) = \sum _ { j = 0 } ^ { n } { \bigg ( } 1 - { \frac { j } { n + 1 } } { \bigg ) } A _ { j } T _ { j } ( x ) .
$$

Hence, if $f \in { \mathcal { P } } _ { n } , \sigma _ { n } ( f ) \not = f ,$ unless $f$ is a constant.

3.4.5. If $m \leqslant f ( x ) \leqslant M$ for $\boldsymbol { x } \in \boldsymbol { I }$ ,show that

$$
m \leqslant \sigma _ { n } ( f ; x ) \leqslant M , \qquad x \in I , n = 0 , 1 , 2 , \ldots .
$$

The Fejer means defined in (3.30) have the property of staying within the bounds of the function,unlike the Fourier-Chebyshev partial sums $s _ { n } ( f ) ,$ ，which may become unbounded for a bounded $f .$ They do not, however,reproduce polynomials, which the $s _ { n } ( f )$ do. An average of the partial sums $s _ { n } ( f )$ which reproduces polynomials of appropriate degree and which remains bounded for bounded $f$ was discovered by de La Vallee Poussin [1].

# 3.4.6. Let

$$
\tau _ { 2 n - 1 } ( f ; x ) = { \frac { s _ { n } ( f ; x ) + \dots + s _ { 2 n - 1 } ( f ; x ) } { n } } .
$$

Show that if $\dot { \ b { f } } \in \mathcal { P } _ { n } , \tau _ { 2 n - 1 } ( { \ b { f } } ) = { \ b { f } } .$ Moreover, for any $f \in C ( I ) ,$

$$
| \tau _ { 2 n - 1 } ( f ; x ) | \leqslant 3 \| f \| , \qquad - 1 \leqslant x \leqslant 1 .
$$

Hint. Show that $\tau _ { 2 n - 1 } = 2 \sigma _ { 2 n - 1 } - \sigma _ { n - 1 }$

3.4.7. Show that $\| f - \tau _ { 2 n - 1 } ( f ) \| \leqslant 4 E _ { n } ( f ) .$

There are functions for which $\pmb { S _ { n } } = \pmb { E _ { n } }$ ; for example, if $f \in \mathcal { P } _ { n + 1 }$ ,then

$$
f ( x ) = \sum _ { j = 0 } ^ { n + 1 } A _ { j } T _ { j } ( x )
$$

and

$$
f ( x ) - s _ { n } ( x ) = A _ { n + 1 } T _ { n + 1 } ( x ) .
$$

Thus, if $A _ { n + 1 } \neq 0$ ,in view of Theorem 2.10, $s _ { n } = p ^ { * }$ ,hence ${ \pmb S } _ { \pmb n } = { \pmb E } _ { \pmb n }$ . Another class of functions for which ${ \pmb S } _ { n } = { \pmb E } _ { n }$ is described in the following theorem.

Theorem 3.5. If $f \in C ( I )$ has the convergent Chebyshev expansion

$$
\sum _ { k = 0 } ^ { \infty } \sp { \prime } A _ { k } T _ { n _ { k } } ( x )
$$

with $A _ { k } > 0 , k = 0 , 1 , 2 , . . .$ ,then $S _ { n } ( f ) = E _ { n } ( f )$ for $\pmb { n = 0 , 1 , 2 , . . . , i f }$ ,and only if,

$$
\frac { n _ { k + 1 } } { n _ { k } } = 2 m _ { k } + 1 , \qquad k = 0 , 1 , . . . ,
$$

where $\pmb { m _ { k } }$ is a positive integer.

Proof. If $n _ { k } \leqslant n < n _ { k + 1 }$

$$
f ( x ) - s _ { n } ( x ) = \sum _ { j = k + 1 } ^ { \infty } A _ { j } T _ { n _ { j } } ( x )
$$

and then

$$
S _ { n } ( f ) = \| f - s _ { n } \| = \sum _ { j = k + 1 } ^ { \infty } A _ { j } .
$$

Suppose that (3.33) holds and

$$
x _ { i } = \eta _ { i } ^ { ( n _ { k + 1 } ) } , \qquad i = 0 , \ldots , n _ { k + 1 } .
$$

Then

$$
T _ { n _ { k + s } } ( x _ { i } ) = \cos n _ { k + s } { \frac { i \pi } { n _ { k + 1 } } } , \qquad s = 1 , 2 , . . . ,
$$

and since

$$
{ \frac { n _ { k + s } } { n _ { k + 1 } } } = { \frac { n _ { k + s } } { n _ { k + s - 1 } } } \cdot { \frac { n _ { k + s - 1 } } { n _ { k + s - 2 } } } \cdot \cdot \cdot { \frac { n _ { k + 2 } } { n _ { k + 1 } } }
$$

is an odd number by (3.33)

$$
T _ { n _ { k + s } } ( x _ { i } ) = ( - 1 ) ^ { i } , \qquad i = 0 , \ldots , n _ { k + 1 } .
$$

Thus $f - s _ { n }$ assumes the value $\pmb { S _ { n } }$ with alternating sign at $n _ { k + 1 } + 1 \geqslant n + 2$ points of $\pmb { I }$ ,hence $s _ { n } = p _ { n } ^ { * }$ by Theorem 2.10.

For this part of the proof the requirement that (3.32) be convergent is superfluous, for the gap condition (3.33) implies the convergence of (3.32) (cf. Zygmund [1, I, VI, Theorem 6.1]).

If $\pmb { S _ { n } } = \pmb { E _ { n } }$ ,then

$$
E _ { n } = \sum _ { j = k + 1 } ^ { \infty } A _ { j }
$$

and there exist points of $I , x _ { 0 } < x _ { 1 } < \cdots < x _ { n + 1 }$ such that for $\pmb { \varepsilon } = 1$ or $^ { - 1 }$

$$
T _ { n _ { j } } ( x _ { i } ) = \varepsilon ( - 1 ) ^ { i } , \qquad i = 0 , \ldots , n + 1 , \qquad j = k + 1 , \ldots .
$$

Therefore each $\mathbf { { x } } _ { i }$ is among the $\eta _ { m } ^ { ( n _ { k + 1 } ) } , m = 0 , \ldots , n _ { k + 1 } ,$ and $T _ { n _ { k + 2 } } ( x _ { i } ) =$ $T _ { n _ { k + 1 } } ( x _ { i } ) .$ so that, say,

$$
\cos \ n _ { k + 2 } { \frac { m \pi } { n _ { k + 1 } } } = \cos \ m \pi ,
$$

which holds only if $n _ { k + 2 } / n _ { k + 1 }$ is an odd integer.

If the Chebyshev expansion of $f$ is absolutely convergent, it is clear that

$$
E _ { n } ( f ) \leqslant S _ { n } ( f ) < | A _ { n + 1 } | + | A _ { n + 2 } | + \ldots .
$$

Lower bounds for $E _ { n } ( f )$ in terms of the Chebyshev coefficients can also be obtained.

Theorem 3.6. If $\mathbf { \mu } : f \in C ( I ) ,$

$$
E _ { n } ( f ) \geqslant \frac { \pi } { 4 } | A _ { n + 1 } | ,
$$

and if the Chebyshev expansion of $f$ is convergent

$$
\begin{array} { c } { { E _ { n } ( f ) \geqslant \displaystyle \frac { 1 } { 4 } | \frac { A _ { n + 1 } T _ { n + 1 } ( x ) } { n } + \frac { 2 A _ { n + 2 } T _ { n + 2 } ( x ) } { n } + \cdots  } } \\ { {  + \frac { n - 1 } { n } A _ { 2 n - 1 } T _ { 2 n - 1 } ( x ) + \sum _ { j = 2 n } ^ { \infty } A _ { j } T _ { j } ( x ) | , \quad  - 1 \leqslant x \leqslant 1 . } } \end{array}
$$

Proof. In view of (3.26)

$$
\begin{array} { l } { \displaystyle { A _ { n + 1 } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } f ( x ) T _ { n + 1 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } } \\ { \displaystyle { \phantom { \frac { 2 } { \pi + 1 } } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \left[ f ( x ) - p _ { n } ^ { * } ( x ) \right] T _ { n + 1 } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } ; } } \end{array}
$$

hence

$$
| A _ { n + 1 } | \leqslant \frac { 2 } { \pi } \ : E _ { n } ( f ) \int _ { - 1 } ^ { 1 } | T _ { n + 1 } ( x ) | \ : \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \frac { 4 } { \pi } \ : E _ { n } ( f ) ,
$$

where we have used Exercise 1.5.2.

Let

$$
\tau _ { 2 n - 1 } ( x ) = { \frac { s _ { n } ( x ) + \cdots + s _ { 2 n - 1 } ( x ) } { n } }
$$

be the de La Vallee Poussin mean of $f$ (cf. Exercise 3.4.6). Then

$$
\begin{array} { l } { \displaystyle \tau _ { 2 n - 1 } ( x ) = s _ { n } ( x ) + \left( 1 - \frac 1 n \right) A _ { n + 1 } T _ { n + 1 } ( x ) + \left( 1 - \frac 2 n \right) A _ { n + 2 } T _ { n + 2 } ( x ) + \cdots } \\ { \displaystyle \qquad + \left( 1 - \frac { n - 1 } n \right) A _ { 2 n - 1 } T _ { 2 n - 1 } ( x ) ; } \end{array}
$$

hence

$$
\begin{array} { c l c r } { { f ( x ) - \tau _ { 2 n - 1 } ( x ) = \displaystyle { \frac { 1 } { n } } { \cal A } _ { n + 1 } T _ { n + 1 } ( x ) + \displaystyle { \frac { 2 } { n } } { \cal A } _ { n + 2 } T _ { n + 2 } ( x ) + \cdots } } \\ { { + \displaystyle { \frac { n - 1 } { n } } { \cal A } _ { 2 n - 1 } T _ { 2 n - 1 } ( x ) + \sum _ { j = 2 n } ^ { \infty } { \cal A } _ { j } T _ { j } ( x ) . } } \end{array}
$$

Therefore, since $| f ( x ) - \tau _ { 2 n - 1 } ( x ) | \leqslant \| f - \tau _ { 2 n - 1 } \| < 4 E _ { n } ( f ) ,$ in view of Exercise 3.4.7, (3.36) is established.

Remark. The bound in (3.35)cannot, in general, be improved,for, given n, consider the function sgn $T _ { n + 1 } ( x )$ Given $\pmb \varepsilon > 0$ , it can be “smoothed” to a continuous function $f ( x ) ,$ having zero as a best approximation and satisfying $| A _ { n + 1 } | > ( 4 / \pi ) ( 1 - \varepsilon ) E _ { n } ( f ) .$

An abundant source of lower bounds for ${ \cal E } _ { n } ( f )$ in terms of the Chebyshev coefficients of $f$ is the observation that if $\rho _ { n } ( \mathbf { f } ; X )$ is the error of the best approximation on a set of $n + 2$ points $\pmb { X }$ ，contained in I， then $\rho _ { n } ( f ; X ) \leqslant E _ { n } ( f )$ (cf. the remark following Theorem 2.10).

Theorem 3.7. If the Chebyshev expansion of $f$ is uniformly convergent on I, then

$$
E _ { n } ( f ) \geqslant \frac { ( n + 2 ) \sin \pi / ( 2 ( n + 2 ) ) } { 2 }  \\  \qquad \times \left| \begin{array} { l } { \displaystyle \sum _ { m = 1 } ^ { \infty } \left( - 1 \right) ^ { m - 1 } \left( A _ { ( 2 m - 1 ) ( n + 2 ) - 1 } - A _ { ( 2 m - 1 ) ( n + 2 ) + 1 } \right| } \end{array} \right|
$$

and

$$
E _ { n } ( f ) \geqslant | A _ { n + 1 } + A _ { 3 ( n + 1 ) } + A _ { 5 ( n + 1 ) } + \cdots | .
$$

Proof. Let $\xi _ { 1 } , \ldots , \xi _ { n + 2 }$ be the zeros of $T _ { n + 2 } ( x ) .$ Then

$$
\begin{array} { r l } { f ( \xi _ { 1 } , \dots , \xi _ { n + 2 } ) = 2 ^ { n + 1 } \displaystyle \sum _ { i = 1 } ^ { n + 2 } \displaystyle \frac { f ( \xi _ { i } ) } { T _ { n + 2 } ^ { \prime } ( \xi _ { i } ) } } & { } \\ { = \displaystyle \frac { 2 ^ { n + 1 } } { n + 2 } \displaystyle \sum _ { i = 1 } ^ { n + 2 } ( - 1 ) ^ { i - 1 } \sin \displaystyle \frac { ( 2 i - 1 ) \pi } { 2 ( n + 2 ) } f ( \xi _ { i } ) . } \end{array}
$$

Thus, if $g ( \xi _ { i } ) = ( - 1 ) ^ { i } , i = 1 , \ldots , n + 2 ,$

$$
g ( \xi _ { 1 } , \ldots , \xi _ { n + 2 } ) = - { \frac { 2 ^ { n + 1 } } { n + 2 } } \sum _ { i = 1 } ^ { n + 2 } \sin { \frac { ( 2 i - 1 ) \pi } { 2 ( n + 2 ) } } = - { \frac { 2 ^ { n + 1 } } { ( n + 2 ) \sin \pi / ( 2 ( n + 2 ) ) } } .
$$

Also,in view of (3.39), Exercises 1.2.3 and1.2.7,and (1.141),

$$
\begin{array} { r } { \ j ( \xi _ { 1 } , \ldots , \xi _ { n + 2 } ) = \left\{ \begin{array} { l l } { ( - 1 ) ^ { m - 1 } 2 ^ { n } , \quad } & { j = ( 2 m - 1 ) ( n + 2 ) - 1 , m = 1 , 2 , \ldots , } \\ { ( - 1 ) ^ { m } 2 ^ { n } , \quad } & { j = ( 2 m - 1 ) ( n + 2 ) + 1 , m = 1 , 2 , \ldots , } \\ { 0 , \quad } & { \mathrm { a l l ~ o t h e r ~ } j ; } \end{array} \right. } \end{array}
$$

hence

$$
f ( \xi _ { 1 } , \ldots , \xi _ { n + 2 } ) = 2 ^ { n } \sum _ { m = 1 } ^ { \infty } ( - 1 ) ^ { m - 1 } ( A _ { ( 2 m - 1 ) ( n + 2 ) - 1 } - A _ { ( 2 m - 1 ) ( n + 2 ) + 1 } )
$$

and

$$
\begin{array} { r l r } {  { E _ { n } ( f ) \geqslant \rho _ { n } ( f ; T ) = | \frac { f ( \xi _ { 1 } , \dots , \xi _ { n + 2 } ) } { g ( \xi _ { 1 } , \dots , \xi _ { n + 2 } ) } | = \frac { ( n + 2 ) \sin \pi / ( 2 ( n + 2 ) ) } { 2 } } } \\ & { } & { \times | \sum _ { m = 1 } ^ { \infty } ( - 1 ) ^ { m - 1 } ( A _ { ( 2 m - 1 ) ( n + 2 ) - 1 } - A _ { ( 2 m - 1 ) ( n + 2 ) + 1 } ) | } \end{array}
$$

thus establishing (3.37).

As for (3.38), let $\eta _ { 0 } , \ldots , \eta _ { n + 1 }$ be the extrema of $T _ { n + 1 } ( x ) .$ Then [cf. (1.98)]

$$
f ( \eta _ { 0 } , . . . , \eta _ { n + 1 } ) = { \frac { 2 ^ { n } } { n + 1 } } \sum _ { j = 0 } ^ { n + 1 } { } ^ { \prime } ( - 1 ) ^ { j } f ( \eta _ { j } )
$$

and, if $g ( \eta _ { i } ) = ( - 1 ) ^ { i + 1 } , i = 0 , \ldots , n + 1 , g ( \eta _ { 0 } , \ldots , \eta _ { n + 1 } ) = - 2 ^ { n }$ ,but

$$
\begin{array} { l } { { \displaystyle T _ { j } ( \eta _ { 0 } , \dots , \eta _ { n + 1 } ) = \frac { 2 ^ { n } } { n + 1 } \sum _ { i = 0 } ^ { n + 1 } T _ { n + 1 } ( \eta _ { i } ) T _ { j } ( \eta _ { i } ) } } \\ { { \displaystyle \qquad = \left\{ \begin{array} { l l } { { \displaystyle 2 ^ { n } , \ } } & { { \displaystyle j = ( 2 k - 1 ) ( n + 1 ) , k = 1 , 2 , \dots , } } \\ { { 0 , \ } } & { { \mathrm { o t h e r w i s e } ; } } \end{array} \right. } } \end{array}
$$

hence

$$
f ( \eta _ { 0 } , \ldots , \eta _ { n + 1 } ) = 2 ^ { n } \sum _ { k = 1 } ^ { \infty } A _ { ( 2 k - 1 ) ( n + 1 ) }
$$

and

$$
E _ { n } ( f ) \geqslant \rho _ { n } ( f ; U ) = { \frac { | f ( \eta _ { 0 } , \ldots , \eta _ { n + 1 } ) | } { | g ( \eta _ { 0 } , \ldots , \eta _ { n + 1 } ) | } } = | A _ { n + 1 } + A _ { 3 ( n + 1 ) } + \cdots | . \quad = { \mathrm { ~ } }
$$

Remark. When all of $A _ { n + k } , k = 1 , 2 , \ldots$ ，are nonnegative,(3.38) is an improvement on (3.35), since it implies that

$$
E _ { n } ( f ) \geqslant A _ { n + 1 } .
$$

Also in this case (3.36) with ${ \boldsymbol { x } } = 1$ yields

$$
E _ { n } ( f ) \geqslant { \frac { 1 } { 4 } } \left( { \frac { A _ { n + 1 } } { n } } + 2 { \frac { A _ { n + 2 } } { n } } + \cdots + { \frac { n - 1 } { n } } A _ { 2 n - 1 } + \sum _ { j = 2 n } ^ { \infty } A _ { j } \right) .
$$

If the sequence of $| A _ { j } |$ converges to zero rapidly,say so rapidly that

$$
\sum _ { j = 2 } ^ { \infty } | A _ { n + j } | \leqslant \theta | A _ { n + 1 } | ,
$$

then, in view of (3.34) and (3.35),

$$
S _ { n } ( f ) \leqslant ( 1 + \theta ) | A _ { n + 1 } | \leqslant { \frac { 4 } { \pi } } \left( 1 + \theta \right) E _ { n } ( f )
$$

and

$$
1 \leqslant \frac { S _ { n } ( f ) } { E _ { n } ( f ) } \leqslant \frac { 4 } { \pi } \left( 1 + \theta \right) ,
$$

so that the truncated Chebyshev expansion is “asymptotically" as good as the best approximation. Of course, if $A _ { n + j } \geqslant 0 , j = 1 , 2 , \ldots , 4 / \pi$ can be replaced by 1 in (3.44). When the function $f ( x )$ is the restriction of an analytic function to $I _ { : }$ ，we can estimate how fast its Chebyshev coefficients go to zero. To this end we must make a brief excursion into the complex plane.

The function

$$
w ( z ) = { \frac { ( z + 1 / z ) } { 2 } }
$$

maps the exterior as well as the interior of $| z | = 1$ in a 1-1 conformal fashion on the whole (extended) $\pmb { w } \cdot$ -plane with the interval $[ - 1 , 1 ]$ deleted.Each pair of circles $| z | = \rho , 1 / \rho$ is mapped onto the same ellipse in the w-plane, $c _ { \rho }$ , with foci at $( \pm 1 , 0 )$ and the sum of major and minor axes equal to $2 \rho$ . The mapping extends to the boundary $| z | = 1$ whose image is the interval [1,1] (traversed twice). If $\Gamma$ denotes the unit circle $| z | = 1$ ，then on putting $\boldsymbol { x } = \cos { \theta } ,$ ， $0 \leqslant \theta \leqslant \pi ,$ ,in (3.26) we obtain

$$
A _ { j } = { \frac { 1 } { \pi } } \int _ { - \pi } ^ { \pi } f ( \cos \theta ) \cos j \theta d \theta = { \frac { 1 } { 2 \pi i } } \int _ { \Gamma } f \left( { \frac { z + z ^ { - 1 } } { 2 } } \right) ( z ^ { j } + z ^ { - j } ) { \frac { d z } { z } } .
$$

Theorem 3.8. Iff is analytic inside and on the ellipse $C _ { \rho }$ for some $\pmb { \rho } ( > 1 ) .$ then

$$
| A _ { j } | \leqslant \frac { 2 M } { \rho ^ { j } } ,
$$

where $M = \operatorname* { m a x } | f ( z ) | , z \in C _ { \rho }$

Proof

$$
\begin{array} { r l r } {  {  \int _ { \Gamma } f ( \frac { z + z ^ { - 1 } } { 2 } ) ( z ^ { j } + z ^ { - j } ) \frac { d z } { z }  } } \\ & { } & { \leqslant  \int _ { \Gamma } f ( \frac { z + z ^ { - 1 } } { 2 } ) z ^ { j - 1 } d z  +  \int _ { \Gamma } f ( \frac { z + z ^ { - 1 } } { 2 } ) z ^ { - j - 1 } d z  . } \end{array}
$$

By Cauchy's theorem we can replace the path of integration $\Gamma$ in the integrals on the right-hand side of(3.48) by $\Gamma _ { \rho ^ { - 1 } } { : } | z | = \rho ^ { - 1 }$ and $\Gamma _ { \rho } \colon | z | = \rho$ ,respectively, thus obtaining (3.47) in view of (3.45).

Corollary 3.8.1. Let $\pmb { \rho }$ be the largest number such that $f$ is analytic inside $c _ { \rho }$ (if $f$ is entire, $\pmb { \rho } = \infty$ ), then

$$
\operatorname* { l i m } _ { j  \infty } | A _ { j } | ^ { 1 / j } \leqslant 1 / \rho ,
$$

where the right-hand side of (3.49) is taken to be zero if $\pmb { \rho } = \infty$

Corollary 3.8.2. If infinitely many of the Chebyshev coefficients of $f$ are nonzero, then, given $\varepsilon > 0 , \varepsilon < \rho$ ，

$$
( \rho - \varepsilon ) ^ { n + j } | A _ { n + j } | < | A _ { n } | , \qquad j = 1 , 2 , \ldots ,
$$

holds for infnitely many $\pmb { n } .$

Proof

$$
( \rho - \varepsilon ) ^ { n + j } \vert A _ { n + j } \vert \leqslant 2 M \bigg ( \frac { \rho - \varepsilon } { \rho } \bigg ) ^ { n + j } ,
$$

and if

$$
2 M \left( \frac { \rho - \varepsilon } { \rho } \right) ^ { n + j } \geqslant | A _ { n } | , \qquad j = 1 , 2 , . . . ,
$$

for all $\pmb { n } > N$ then $A _ { n } = 0$ for all ${ \pmb n } > N$

Corollary 3.8.1 suggests that ellipses $C _ { \rho }$ might play the role of circles in the theory of Taylor series for Chebyshev expansions of analytic functions. That is indeed the case as we shall see next.

Lemma 3.4.1. If $\pmb { p } \in \pmb { \mathcal { P } _ { n } }$ satisfies $| p ( x ) | \leqslant M$ on $- 1 \leqslant x \leqslant 1$ ,then $| p ( z ) | \leqslant M \rho ^ { n }$ on $c _ { \rho }$ for each $\pmb { \rho } \geqslant 1$

Proof. Suppose $w \in C _ { \rho }$ ; then $p ( w ) = p ( ( z + z ^ { - 1 } ) / 2 ) ;$ where $| z | = \rho$ ,but

$$
\frac { p [ ( z + z ^ { - 1 } ) / 2 ] } { z ^ { n } }
$$

is analytic in $| z | \geqslant 1$ , and so the maximum of its modulus on $| z | = \rho$ cannot exceed its maximum modulus on $| z | = 1$ (the boundary).

Theorem 3.9. If, for some $\pmb { \rho } > 1$

$$
\operatorname* { l i m } _ { n \to \infty } \ [ E _ { n } ( f ) ] ^ { 1 / n } \leqslant { \frac { 1 } { \rho } } ,
$$

then $f$ is analytic inside the ellipse $c _ { \rho }$

Proof. Suppose that $\rho _ { 0 } < \rho$ so that $E _ { n } ( f ) \leqslant \rho _ { 0 } ^ { - n }$ for $n > N$ Let ${ \pmb p } _ { \pmb n }$ be the best approximation to $f$ out of $\mathcal { P } _ { \pmb { n } }$ on I, ${ \pmb n } = 0 ;$ ,1, 2,.... Thus

$$
f = p _ { 0 } + ( p _ { 1 } - p _ { 0 } ) + \cdots + ( p _ { n + 1 } - p _ { n } ) + \cdots
$$

uniformly on $\pmb { I }$ and on $\pmb { I }$ (for ${ \pmb n } > { \pmb N }$ ），

$$
\begin{array} { r l } & { | p _ { n + 1 } - p _ { n } | = | f - p _ { n } + p _ { n + 1 } - f | \leqslant E _ { n } ( f ) + E _ { n + 1 } ( f ) } \\ & { \qquad \leqslant \rho _ { 0 } ^ { - n } + \rho _ { 0 } ^ { - ( n + 1 ) } \leqslant 2 \rho _ { 0 } ^ { - n } . } \end{array}
$$

Lemma 3.4.1 now implies that

$$
| p _ { n + 1 } ( z ) - p _ { n } ( z ) | \leqslant 2 \rho _ { 0 } ^ { - n } \rho _ { 1 } ^ { n + 1 } = 2 \rho _ { 1 } \bigg ( \frac { \rho _ { 1 } } { \rho _ { 0 } } \bigg ) ^ { n } ,
$$

on the ellipse $c _ { \rho _ { 1 } }$ . Choose $\rho _ { 1 } < \rho _ { 0 } ;$ then the series in (3.50) is uniformly convergent inside and on $c _ { \rho _ { 1 } }$ ,hence $f$ is analytic, and since $\pmb { \rho _ { 1 } }$ may be chosen arbitrarily close to $\pmb { \rho }$ the theorem is proved.

Theorem 3.10. The following are equivalent:

i $f$ is analytic inside the ellpse $c _ { \rho }$ with $\rho > 1$ ，but not inside $c _ { \rho ^ { \prime } }$ with $\rho ^ { \prime } > \rho ,$   
(i) $\begin{array} { l } { \displaystyle \overline { { \operatorname* { l i m } _ { n  \infty } } } ~ [ E _ { n } ( f ) ] ^ { 1 / n } = 1 / \rho , ~ \rho > 1 , } \end{array}$

$$
\operatorname* { l i m } _ { n  \infty \atop n  \infty } | A _ { n } | ^ { 1 / n } = 1 / \rho , \rho > 1
$$

(with the usual interpretations if $\pmb { \rho } = \infty$ ）

Proof. We shall prove that $( \mathbf { i i i } ) \Rightarrow ( \mathbf { i i } ) \Rightarrow ( \mathbf { i } ) \Rightarrow ( \mathbf { i i } ) \Rightarrow ( \mathbf { i i i } ) .$ $( \mathrm { i i i } ) \Rightarrow$ (ii): In view of (3.35)

$$
\overline { { \operatorname* { l i m } } } E _ { n } ^ { 1 / n } \geqslant \overline { { \operatorname* { l i m } } } \left[ \left( \frac { \pi } { 4 } \right) ^ { 1 / n } ( | A _ { n + 1 } | ^ { 1 / n + 1 } ) ^ { ( n + 1 ) / n } \right] ,
$$

so that

$$
\widetilde { \mathrm { l i m } } E _ { n } ^ { 1 / n } \geqslant \frac 1 \rho .
$$

If $1 < \rho ^ { \prime } < \rho _ { ; }$ then for $\pmb { n }$ sufficiently large $| A _ { n + 1 } | + | A _ { n + 2 } | + \cdots \leqslant$ $( \rho ^ { \prime } ) ^ { - n } ( \rho ^ { \prime } - 1 ) ^ { - 1 }$ ; hence,in view of (3.34),

$$
\overline { { \operatorname* { l i m } } } E _ { n } ^ { 1 / n } \leqslant \frac { 1 } { \rho ^ { \prime } } , \qquad \mathrm { e a c h } \ \rho ^ { \prime } < \rho .
$$

Thus (ii) is established.

(ii) $\Rightarrow \mathrm { ( i ) }$ :According to Theorem 3.9, $f$ is analytic inside $c _ { \rho }$ .If $f$ is analytic inside $C _ { \rho ^ { \prime } } , \rho ^ { \prime } > \rho$ ,then by Corollary 3.8.1

$$
\widetilde { \| m \| } \vert { \cal A } _ { n } \vert ^ { 1 / n } \leqslant \frac { 1 } { \rho ^ { \prime } } < \frac { 1 } { \rho } ,
$$

which contradicts (i),since we have shown that ( $\mathrm { i } \mathrm { i } ) \Rightarrow \mathrm { ( i i ) }$

$( \mathbf { i } ) \Rightarrow$ (i): Again by Corollary 3.8.1

$$
\widetilde { \| \mathbf { m } } \ | A _ { n } | ^ { 1 / n } \leqslant \frac { 1 } { \rho } .
$$

If the inequality holds, then

$$
\overline { { { \mathrm { l i m } } } } E _ { n } ^ { 1 / n } = \overline { { { \mathrm { l i m } } } } | A _ { n } | ^ { 1 / n } = \frac { 1 } { \rho ^ { \prime } } , \qquad \rho ^ { \prime } > \rho ,
$$

implies that $f$ is analytic inside $c _ { \rho ^ { \prime } }$ ， contradicting (i).

We shall call $\pmb { \rho }$ , as defined in Theorem 3.10, the index of convergence off.

The index of convergence of an entire function is infinite. If $f$ is not a polynomial, has the index of convergence $\pmb { \rho } < \infty$ ,and $0 < \varepsilon < \rho - 1 ;$ ,then in

# view of Corollary 3.8.2

$$
\sum _ { j = 2 } ^ { \infty } \left| A _ { n + j } \right| \leqslant { \frac { 1 } { \rho - \varepsilon - 1 } } \left| A _ { n + 1 } \right|
$$

for infinitely many ${ \pmb n } _ { \pmb { \imath } }$ ，so that according to (3.44)

$$
1 \leqslant \frac { S _ { n } ( f ) } { E _ { n } ( f ) } \leqslant \frac { 4 } { \pi } \frac { \rho - \varepsilon } { \rho - \varepsilon - 1 } ,
$$

for infinitely many $\pmb { n }$ Also, since

$$
| A _ { n + 1 } + A _ { 3 ( n + 1 ) } + \cdots | \geqslant | A _ { n + 1 } | - \sum _ { j = 2 } ^ { \infty } | A _ { n + j } | \geqslant \left( 1 - { \frac { 1 } { \rho - \varepsilon - 1 } } \right) | A _ { n + 1 } |
$$

and

$$
\sum _ { j = 1 } ^ { \infty } | A _ { n + j } | \leqslant \left( 1 + \frac { 1 } { \rho - \varepsilon - 1 } \right) | A _ { n + 1 } | ,
$$

we find, in view of (3.34) and (3.38), that

$$
\left( 1 - \frac { 1 } { \rho - \varepsilon - 1 } \right) \left| A _ { n + 1 } \right| \leqslant E _ { n } ( f ) \leqslant S _ { n } ( f ) \leqslant \left( 1 + \frac { 1 } { \rho - \varepsilon - 1 } \right) \left| A _ { n + 1 } \right|
$$

holds for infinitely many n.

$\mathbf { I f } f$ is an entire function, then as a consequence of(3.53) we have a result of Bernstein [2],

$$
E _ { n } ( f ) \sim | A _ { n + 1 } |
$$

as n goes to infinity through some sequence of integers. Whether (3.54) can hold for a function that is not entire is not known.

# EXERCISES 3.4.8-3.4.12

# 3.4.8. With

$$
\eta _ { j } = \cos { \frac { j \pi } { k + 1 } } , ~ j = 1 , . . . , k ,
$$

show that if $g ( \eta _ { j } ) = ( - 1 ) ^ { j } , j = 1 , \ldots , k ,$

$$
{ \frac { | f ( \eta _ { 1 } , \ldots , \eta _ { k } | } { | g ( \eta _ { 1 } , \ldots , \eta _ { k } | } } = \left| \sum _ { j = 0 } ^ { \infty } \Delta _ { 2 } ^ { 2 } A _ { ( 2 j + 1 ) ( k + 1 ) - 2 } \right| ,
$$

where $\Delta _ { 2 } ^ { 2 } A _ { m } = A _ { m } - 2 A _ { m + 2 } + A _ { m + 4 }$

# 3.4.9. Show that

$$
E _ { n } ( f ) \geqslant \left| \sum _ { j = 0 } ^ { \infty } \Delta _ { 2 } ^ { 2 } A _ { ( 2 j + 1 ) ( n + 3 ) - 2 } \right| .
$$

# 3.4.10. Show that

$$
S _ { n } ( | x | ) = { \frac { 2 } { \pi ( 2 [ n / 2 ] + 1 ) } } .
$$

Hint. Exercise 3.4.1c.

3.4.11. Show that for ${ \pmb n } > 1$

$$
E _ { n } ( \vert x \vert ) \geqslant \frac { 1 } { 2 \pi ( 2 n - 1 ) } .
$$

Hint. Put $\mathbf { x } = \mathbf { 0 }$ in (3.36) and use Exercise 3.4.10.

# 3.4.12. Show that

$$
\frac { 1 } { 4 \pi } \leqslant n E _ { n } ( | x | ) \leqslant \frac { 2 } { \pi } .
$$

# S.N. Bernstein [1] showed that

$$
\operatorname * { l i m } _ { n  \infty } 2 n E _ { 2 n } ( | x | ) = c = 0 . 2 8 2 \cdot \cdot \cdot \cdot
$$

In a footnote to this result Bernstein remarks: “It would be very interesting to determine if $\pmb { c }$ is a new transcendental or if it can be expressed in terms of known transcendentals.Inote,asa curious coincidence, that $1 / ( 2 \pi ^ { 1 / 2 } ) = 0 . 2 8 2 .$ ..” However, Varga and Carpenter [1] showed in 1983 that $c \neq 1 / ( 2 \pi ^ { 1 / 2 } )$ ：

# 3.5. The Evaluation of Chebyshev Coefficients

The usefulness of the partial sums $s _ { n } ( f )$ of the Chebyshev expansion of $f$ has been established in the preceding section and so it becomes important to examine methods of obtaining these partial sums, i.e., methods of evaluating the coefficients $A _ { k } = A _ { k } ( f )$ defined in (3.26). Since these coefficients are defined by integrals,our approach is to examine various methods of quadrature, or numerical integration, as applied to (3.26).

Our first approach is to apply the Gaussan quadrature formula given by (1.123)to (.26)If weusethfoula basedon $\xi _ { 1 } ^ { ( m ) } , \ldots , \xi _ { m } ^ { ( m ) }$ we obtain as an approximation to $\pmb { A } _ { k }$

$$
\alpha _ { k } ^ { ( m ) } = \frac { 2 } { m } \sum _ { i = 1 } ^ { m } \ f ( \xi _ { i } ^ { ( m ) } ) T _ { k } ( \xi _ { i } ^ { ( m ) } ) ,
$$

and since the quadrature formula is exact for $f T _ { k } \in \mathcal { P } _ { 2 m - 1 }$ we have

$$
\alpha _ { k } ^ { ( m ) } = A _ { k } ( f )
$$

for fe92m-1-k

Let us observe at once that if $0 \leqslant k \leqslant 2 m$ (3.55) can be rewritten in the form

$$
\alpha _ { k } ^ { ( m ) } = \frac { 2 } { m } \sum _ { i = 1 } ^ { m } f ( \xi _ { i } ^ { ( m ) } ) T _ { 2 i - 1 } ( \eta _ { k } ^ { ( 2 m ) } ) ,
$$

since

$$
\begin{array} { l } { \displaystyle T _ { k } ( \xi _ { i } ^ { ( m ) } ) = T _ { k } \left( \cos \left( 2 i - 1 \right) \frac { \pi } { 2 m } \right) = T _ { k } \left( T _ { 2 i - 1 } \left( \cos \frac { \pi } { 2 m } \right) \right) } \\ { = } & { T _ { 2 i - 1 } \left( T _ { k } \left( \cos \frac { \pi } { 2 m } \right) \right) = T _ { 2 i - 1 } \left( \cos \frac { k \pi } { 2 m } \right) } \end{array}
$$

in view of $T _ { m } ( T _ { n } ( x ) ) = T _ { n } ( T _ { m } ( x ) )$ (cf. Exercise 1.1.6).

The advantage of the form (3.57) is that $\alpha _ { k } ^ { ( m ) }$ can be evaluated by using the recurrence formula (3.16).

If the Chebyshev expansion of $f$ converges uniformly to $f$ in [-1,1] and $m > k ,$

$$
\begin{array} { c } { { \displaystyle { \alpha _ { k } ^ { ( m ) } = \frac { 2 } { m } \sum _ { i = 1 } ^ { m } \left( \sum _ { j = 0 } ^ { \infty } A _ { j } T _ { j } ( \xi _ { i } ^ { ( m ) } ) \right) T _ { k } ( \xi _ { i } ^ { ( m ) } ) } } } \\ { { = \displaystyle { \sum _ { j = 0 } ^ { \infty } A _ { j } \left( \frac { 2 } { m } \sum _ { i = 1 } ^ { m } T _ { j } ( \xi _ { i } ^ { ( m ) } ) T _ { k } ( \xi _ { i } ^ { ( m ) } ) \right) } } } \\ { { = A _ { k } + \displaystyle { \sum _ { j = 1 } ^ { \infty } ( - 1 ) ^ { j } ( A _ { 2 j m - k } + A _ { 2 j m + k } ) } } } \end{array}
$$

in view of(1.141). Note that if we put ${ \pmb m } = { \pmb k }$ in (3.58) we obtain $\alpha _ { k } ^ { ( k ) } = 0$ which is, of course, obvious from (3.55). Formula (3.58) provides an estimate for the error $A _ { k } - \alpha _ { k } ^ { ( m ) }$

Let us put

$$
u _ { n } ^ { ( m ) } ( x ) = \sum _ { k = 0 } ^ { n } \alpha _ { k } ^ { ( m ) } T _ { k } ( x ) ,
$$

which is the approximate value of $s _ { n } ( x )$ obtained by using the approximation (3.55) to the $\pmb { A } _ { k }$ . The polynomials $u _ { n } ^ { ( m ) } ( x )$ are also related to interpolating polynomials.

Theorem 3.11. If $n < m$

$$
u _ { n } ^ { ( m ) } ( x ) = s _ { n } ( L _ { m - 1 } ( f , T ) ; x ) .
$$

Proof. Let

$$
L _ { m - 1 } ( x ) = \sum _ { j = 0 } ^ { m - 1 } b _ { j } T _ { j } ( x )
$$

so that

$$
b _ { j } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } L _ { m - 1 } ( x ) T _ { j } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } , j = 0 , \ldots , m - 1 .
$$

Thus, according to (3.56), we have

$$
\begin{array} { c } { { b _ { j } = \displaystyle \frac { 2 } { m } \sum _ { i = 1 } ^ { m } L _ { m - 1 } ( \xi _ { i } ^ { ( m ) } ) T _ { j } ( \xi _ { i } ^ { ( m ) } ) } } \\ { { \ } } \\ { { = \displaystyle \frac { 2 } { m } \sum _ { i = 1 } ^ { m } f ( \xi _ { i } ^ { ( m ) } ) T _ { j } ( \xi _ { i } ^ { ( m ) } ) = \alpha _ { j } ^ { ( m ) } } } \end{array}
$$

for $j = 0 , . . . , m - 1 .$ Since $m - 1 \geqslant n ,$ (3.60) follows.

Remark. If $m = n + 1$ ，then $u _ { n } ^ { ( n + 1 ) } ( x ) = L _ { n } ( f , T ; x ) ,$ i.e., $u _ { n } ^ { ( n + 1 ) }$ is the polynomial that interpolates $f$ at the zeros of $T _ { n + 1 }$

Since, for $- 1 \leqslant x \leqslant 1$ and $n < m$

$$
\begin{array} { r l } { | s _ { n } ( x ) - u _ { n } ^ { ( m ) } ( x ) | = \displaystyle | \sum _ { k = 0 } ^ { n } ( A _ { k } - \alpha _ { k } ^ { ( m ) } ) T _ { k } ( x ) | } & { } \\ & { = \displaystyle | \sum _ { k = 0 } ^ { n } ( \displaystyle \sum _ { j = 1 } ^ { \infty } ( - 1 ) ^ { j - 1 } ( A _ { 2 j m - k } + A _ { 2 j m + k } ) T _ { k } ( x ) | } \\ & { \leqslant \displaystyle \sum _ { j = 1 } ^ { \infty } \sum _ { k = 0 } ^ { n } ( | A _ { 2 j m - k } | + | A _ { 2 j m + k } | ) } \\ & { \leqslant \displaystyle \sum _ { j = 1 } ^ { \infty } \sum _ { i = 2 j m - n } ^ { 2 j m + n } | A _ { i } | , } \end{array}
$$

we obtain

Theorem 3.12. If $m > n ,$

$$
\| s _ { n } - u _ { n } ^ { ( m ) } \| \leqslant \sum _ { j = 1 } ^ { \infty } \sum _ { i = 2 j m - n } ^ { 2 j m + n } | A _ { i } | .
$$

Our second approach is to use the integration formula of Lobatto-Markov [cf. (1.145), Exercise 1.5.29],

$$
\int _ { - 1 } ^ { 1 } g ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \frac { \pi } { n } \sum _ { i = 0 } ^ { n } g ( \eta _ { i } ^ { ( n ) } ) , \qquad g \in \mathcal { P } _ { 2 n - 1 } ,
$$

to evaluate $A _ { k } ( f )$

Putting $\begin{array} { r } { g = f T _ { k } } \end{array}$ in (3.62) leads to an approximation to $\pmb { A } _ { \pmb { k } }$ ，

$$
\beta _ { k } ^ { ( m ) } = \frac { 2 } { m } \sum _ { i = 0 } ^ { m } T _ { k } ( \boldsymbol { \eta } _ { i } ^ { ( m ) } ) f ( \boldsymbol { \eta } _ { i } ^ { ( m ) } ) ,
$$

and since the quadrature formula is exact for $f T _ { k } \in \mathcal { P } _ { 2 m - 1 }$ we have

$$
\beta _ { k } ^ { ( m ) } = A _ { k } ( f )
$$

for feP2m-1-k

We observe, once again, that if $0 \leqslant k \leqslant m$ (3.63) can be written in the form

$$
\beta _ { k } ^ { ( m ) } = \frac { 2 } { m } \sum _ { i = 0 } ^ { m } f ( \eta _ { i } ^ { ( m ) } ) T _ { i } ( \eta _ { k } ^ { ( m ) } ) ,
$$

which allows $\beta _ { k } ^ { ( m ) }$ to be evaluated by means of the recurrence formula (3.6).

If the Chebyshev expansion of $f$ converges uniformly to $f$ in $[ - 1 , 1 ]$ and we replace $f$ by its expansion in (3.63), we obtain, recalling (1.144), for $m \geqslant k$

$$
\beta _ { k } ^ { ( m ) } = A _ { k } + \sum _ { j = 1 } ^ { \infty } { \left( { A _ { 2 j m - k } } + { A _ { 2 j m + k } } \right) } .
$$

Let us choose $m \geqslant n$ and consider

$$
v _ { n } ^ { ( m ) } ( x ) = \sum _ { k = 0 } ^ { n } \beta _ { k } ^ { ( m ) } T _ { k } ( x )
$$

as an approximation to $s _ { n } ( x ) ; v _ { n } ^ { ( n ) }$ is an interpolating polynomial to f.

Theorem 3.13. If ${ \pmb n } > { \bf 0 } ;$

$$
v _ { n } ^ { ( n ) } ( x ) = L _ { n } ( f , U ; x ) .
$$

Proof. Let

$$
L _ { n } ( f , U ; x ) = \sum _ { j = 0 } ^ { n } c _ { j } T _ { j } ( x ) ,
$$

so that

$$
c _ { j } = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } L _ { n } ( x ) T _ { j } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } , j = 0 , \ldots , n - 1 .
$$

According to (3.64), we have, for $j = 0 , . . . , n - 1 ;$

$$
\begin{array} { l } { { \displaystyle c _ { j } = \frac { 2 } { n } \sum _ { i = 0 } ^ { n } L _ { n } ( \eta _ { i } ^ { ( n ) } ) T _ { j } ( \eta _ { i } ^ { ( n ) } ) } } \\ { { \displaystyle ~ } } \\ { { \displaystyle ~ = \frac { 2 } { n } \sum _ { i = 0 } ^ { n } f ( \eta _ { i } ^ { ( n ) } ) T _ { j } ( \eta _ { i } ^ { ( n ) } ) = \beta _ { j } ^ { ( n ) } . } } \end{array}
$$

Equation (3.65) implies that $\beta _ { n } ^ { ( n ) } = 2 c _ { n }$ and so (3.67) is established.

Comparing (3.65) with (3.58) suggests that

$$
\gamma _ { k } ^ { ( m ) } = \frac { \alpha _ { k } ^ { ( m ) } + \beta _ { k } ^ { ( m ) } } { 2 }
$$

is a more useful approximation to $\pmb { A } _ { k }$ than either $\alpha _ { k } ^ { ( m ) }$ or $\beta _ { k } ^ { ( m ) }$ ，since

$$
\gamma _ { k } ^ { ( m ) } = A _ { k } + \sum _ { j = 1 } ^ { \infty } { \bigl ( } A _ { 4 j m - k } + A _ { 4 j m + k } { \bigr ) } .
$$

Put

$$
w _ { n } ^ { ( m ) } ( x ) = \sum _ { k = 0 } ^ { n } \gamma _ { k } ^ { ( m ) } T _ { k } ( x ) ;
$$

we then have Theorem 3.14 as an immediate consequence of (3.69).

Theorem 3.14. If $m \geqslant n ,$

$$
\| s _ { n } - w _ { n } ^ { ( m ) } \| \leqslant \sum _ { j = 1 } ^ { \infty } \sum _ { i = 0 } ^ { 2 n } | A _ { 4 j m - n + i } | \leqslant \sum _ { i = 0 } ^ { \infty } | A _ { 4 m - n + i } | .
$$

Note that if we choose ${ \pmb m } = { \pmb n }$ , in which case ${ \pmb \alpha } _ { n } ^ { ( n ) } = { \pmb 0 } ,$ ， we obtain

$$
\| s _ { n } - w _ { n } ^ { ( n ) } \| \leqslant \sum _ { i = 0 } ^ { \infty } | A _ { 3 n + i } | .
$$

When $k = m \neq 0$ (3.63) takes on a particularly simple form,

$$
\beta _ { k } ^ { ( k ) } = \frac { 2 } { k } \sum _ { i = 0 } ^ { k } { ( - 1 ) ^ { i } f ( \eta _ { i } ^ { ( k ) } ) } .
$$

However, $\beta _ { k } ^ { ( k ) } = A _ { k } ( f )$ only for $f \in \mathcal P _ { k - 1 }$ , when both are zero. It turns out that we can get equality for the largest possible class of polynomials by simply using $\gamma _ { k } ^ { ( k ) } = \beta _ { k } ^ { ( k ) } / 2 ( \alpha _ { k } ^ { ( k ) } = 0 )$

Theorem 3.15. The quadrature formula

$$
A _ { k } ( f ) = \frac { \beta _ { k } ^ { ( k ) } } { 2 } = \gamma _ { k } ^ { ( k ) } = \frac { 1 } { k } \sum _ { i = 0 } ^ { k } ( - 1 ) ^ { i } f ( \eta _ { i } ^ { ( k ) } )
$$

is valid for $f \in \mathcal { P } _ { 3 k - 1 } , ~ k = 1 , ~ 2$ ，....Moreover， when $k > 1$ ，there is no quadrature formula

$$
A _ { k } ( f ) = \sum _ { i = 0 } ^ { k } c _ { i } f ( x _ { i } )
$$

holding for all $f \in \mathcal { P } _ { 3 k }$ ,and (3.71) is the only formula of type (3.72) valid for $f \in \mathcal { P } _ { 3 k - 1 }$

Proof. The validity of (3.71) for $f \in \mathcal { P } _ { 3 k - 1 }$ follows from (3.69) by choosing $m = k ,$

Suppose (3.72) holds for $f \in \mathcal { P } _ { 3 k - 1 }$ . Put $\omega ( x ) = ( x - x _ { 0 } ) \cdots ( x - x _ { k } )$ and consider $f ( x ) = ( 1 - x ^ { 2 } ) T _ { k } ^ { \prime } ( x ) \omega ( x ) / ( x - x _ { i } ) \in \mathcal { P } _ { 2 k + 1 }$ . Note that, since $k \geqslant 2 ,$ $2 k + 1 \leqslant 3 k - 1 .$ Equations (3.72) and (3.71) imply that $0 = A _ { k } ( f ) =$ $c _ { i } f ( x _ { i } ) = c _ { i } ( 1 - x _ { i } ^ { 2 } ) T _ { k } ^ { \prime } ( x _ { i } ) \omega ^ { \prime } ( x _ { i } ) .$ Since $c _ { i } \omega ^ { \prime } ( x _ { i } ) \neq 0 ,$ $x _ { i }$ must be a zero of $( 1 - x ^ { 2 } ) T _ { k } ^ { \prime } ( x ) ,$ and this must be true for $i = 0 , ~ . . . , ~ k$ Taking $f ( x ) =$ ${ \omega ( x ) } / ( x - x _ { i } )$ in (3.71) and (3.72), we obtain the uniqueness of (3.71). Finally (3.71) does not hold for $f ( x ) = ( 1 - x ^ { 2 } ) [ T _ { k } ^ { \prime } ( x ) ] ^ { 2 } T _ { k } ( x ) \in \mathcal { P } _ { 3 k }$

Remark 1. Equation (3.71) may be writen as

$$
A _ { k } ( f ) = 2 ^ { 1 - n } f ( \eta _ { 0 } ^ { ( k ) } , \ldots , \eta _ { k } ^ { ( k ) } ) .
$$

Remark 2. When $k = 1$ ， we can improve on (3.71). There is a unique formula of the form (3.72) valid for $f \in \mathcal { P } _ { 4 }$ but none valid for $f \in \mathcal { P } _ { 5 }$ This highest degree of precision formula is given by $x _ { 0 } = \sqrt { 3 } / 2 , x _ { 1 } = - \sqrt { 3 } / 2 ,$ $\begin{array} { r } { c _ { 0 } = \frac { 2 } { 3 } , c _ { 1 } = - \frac { 2 } { 3 } , } \end{array}$ as the reader may readily verify.

Consider the quadrature formula

$$
A _ { k } ( f ) = \sum _ { i = 0 } ^ { l } c _ { i } f ( x _ { i } ) .
$$

Let $\pmb { h } ( l )$ be the largest integer such that there exists a formula (3.74) valid for $f \in \mathcal P _ { h }$ . We say such a formula is of the highest degree of precision. We have just seen that, for $k > 1 , h ( k ) = 3 k - 1 .$ Let us examine the behavior of $\pmb { h } ( l )$ as l varies.

# Theorem 3.16

$$
h ( l ) = l - 1 , l = 1 , . . . , k - 1 .
$$

2. For $m = 1 , 2 , \ldots$

(a) $h ( ( 2 m - 1 ) k ) = ( 4 m - 1 ) k - 1 , k > 1 ,$ (b) $h ( 2 m k - 1 ) = ( 4 m + 1 ) k - 1 ,$

3. (a) If $( 2 m k - 1 ) < l < ( 2 m + 1 ) k _ { : }$ m =1,2,.,h(l)< 2mk + l. (b) If (2m - 1)k <l< 2mk - 1,m = 1,2,..,h(l)<(2m - 1)k + l+ 1.

Proof. 1. If $h ( l ) \geqslant l$ and $1 \leqslant l \leqslant k - 1$ , then, in view of the orthogonality property of the Chebyshev polynomials,

$$
0 = A _ { k } ( f ) = \sum _ { i = 0 } ^ { l } c _ { i } f ( x _ { i } )
$$

for $f \in \mathcal { P } _ { l }$ Put $\omega ( x ) = ( x - x _ { 0 } ) \cdots ( x - x _ { l } )$ and $f = \omega ( \boldsymbol { x } ) / ( \boldsymbol { x } - \boldsymbol { x } _ { i } ) \in \mathcal { P } _ { l }$ ；then $c _ { i } = 0 ;$ ,which is a contradiction. Thus $h ( l ) \leqslant l - 1 .$ Given any set of nodes, $\pmb { x _ { 0 } } .$ ， $\cdots , x _ { l }$ ,the $\iota$ linear homogeneous equations in $l + 1$ unknowns

$$
\sum _ { i = 0 } ^ { l } c _ { i } x _ { i } ^ { j } = 0 , \qquad j = 0 , . . . , l - 1 ,
$$

have a nontrivial solution and, indeed, one for which no $c _ { i } = 0 ;$ for if, say, $c _ { q } = 0 ;$ ，the system

$$
\sum _ { i = 0 \atop i \not = q } ^ { l } c _ { i } x _ { i } ^ { j } = 0 , \qquad j = 0 , \ldots , l - 1 ,
$$

has only the trivial (zero) solution, since its matrix is of Vandermonde type. Since $A _ { k } ( f ) = 0$ for $f \in \mathcal { P } _ { \imath - 1 } $ we have $h ( l ) = l - 1$

2(a). Replace m by 2mk and ${ \_ g } \ b y f T _ { k }$ in (3.62). Since each zero of $T _ { k }$ is found among the $\eta _ { j } ^ { ( 2 m k ) }$ ,we obtain from (3.62)

$$
A _ { k } ( f ) = \sum _ { j = 0 } ^ { ( 2 m - 1 ) k } b _ { j } f ( \lambda _ { j } )
$$

(where the $\lambda _ { j }$ are the $\pmb { \eta } _ { j }$ that are not zeros of $T _ { k }$ valid for $f \in \mathscr { P } _ { ( 4 m - 1 ) k - 1 }$ .If there isaformula(3.74) validfor $f \in \mathcal { P } _ { ( 4 m - 1 ) k }$ ，then" weput $\Omega ( x ) = ( x - \lambda _ { 0 } ) \cdots ( x - \lambda _ { ( 2 m - 1 ) k } )$ and $\omega ( x ) = ( x - x _ { 0 } ) \cdots ( x - x _ { ( 2 m - 1 ) k } )$ Thus

$$
f ( x ) = \Omega ( x ) \frac { \omega ( x ) } { x - x _ { i } } { \in } \mathcal { P } _ { ( 4 m - 1 ) k - 1 } ,
$$

since $k > 1 .$ Hence $A _ { k } ( f ) = 0$ by (3.75) and therefore

$$
c _ { i } \omega ^ { \prime } ( x _ { i } ) \Omega ( x _ { i } ) = 0 ,
$$

which implies that $\pmb { \Omega } = \pmb { \omega }$ ,but (3.75) cannot be exact for $f \in \mathcal { P } _ { ( 4 m - 1 ) k }$ ,as the choice

$$
f ( x ) = ( 1 - x ^ { 2 } ) [ ( x - \lambda _ { 1 } ) ^ { \cdots } ( x - \lambda _ { ( 2 m - 1 ) k - 1 } ) ] ^ { 2 } T _ { k } ( x ) \in \mathcal { P } _ { ( 4 m - 1 ) k }
$$

demonstrates.

2(b). $h ( 2 m k - 1 ) < ( 4 m + 1 ) k ,$ since $\omega ^ { 2 } T _ { k } \in \mathcal { P } _ { ( 4 m + 1 ) k }$ . By Gaussian quadrature [Ccf. (1.108)]

$$
\int _ { - 1 } ^ { 1 } g ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \frac { \pi } { ( 2 m + 1 ) k } \sum _ { j = 1 } ^ { ( 2 m + 1 ) k } g ( \xi _ { j } ^ { ( ( 2 m + 1 ) k ) } ) ,
$$

is exact for $g \in \mathcal { P } _ { 2 ( 2 m + 1 ) k - 1 }$ . Hence

$$
A _ { k } ( f ) = \sum _ { j = 0 } ^ { 2 m k - 1 } d _ { j } f ( \mu _ { j } ) ,
$$

where the $\mu _ { j }$ are the zeros of $T _ { ( 2 m + 1 ) k }$ which are not also zeros of $T _ { k }$ , is exact for f ∈P(4m+1)k-1:

3(a).Equation (3.74) holds for $f \in \mathcal { P } _ { h ( l ) }$ Let $\Omega ( x ) = ( x - \mu _ { 0 } ) \cdots ( x -$ $\mu _ { 2 m k - 1 } ) \in \mathcal { P } _ { 2 m k }$ and $\omega ( x ) = ( x - x _ { 0 } ) \cdots ( x - x _ { l } ) \in \mathcal { P } _ { l + 1 } ,$ then

$$
f ( x ) = \Omega ( x ) \frac { \omega ( x ) } { x - x _ { 1 } } \in \mathcal { P } _ { 2 m k + l } ,
$$

and in view of (3.77) we conclude in a now familiar fashion that $h ( l ) < 2 m k + l .$

3(b). The argument resembles 3(a) and we omit it.

Remark. This theorem has the surprising implication that the addition of nodes to a quadrature formula may result in reducing the highest degree of precision. The last two theorems are more interesting when we seek approximations of individual $\pmb { A } _ { k }$ rather than of ${ \pmb S } _ { \pmb n }$ ， since they require a different set of nodes for each $\pmb { k }$

# EXERCISES 3.5.1-3.5.4

3.5.1. Show that

$$
u _ { n } ^ { ( n ) } ( x ) = L _ { n - 1 } ( f , T ; x ) .
$$

3.5.2. Show that if $f$ has an absolutely convergent Chebyshev expansion

$$
\lVert f - u _ { n } ^ { ( n + 1 ) } \rVert \leqslant 2 \sum _ { i = n + 1 } ^ { \infty } | A _ { i } | - \sum _ { i = 1 } ^ { \infty } | A _ { ( 2 i - 1 ) ( n + 1 ) } | .
$$

3.5.3. Let

$$
p _ { n - 1 } ( x ) = \sum _ { k = 0 } ^ { n - 1 } \beta _ { k } ^ { ( n ) } T _ { k } ( x ) .
$$

Show that $\pmb { p _ { n - 1 } }$ is the best approximation to $f$ on $\big \{ \eta _ { 0 } ^ { ( n ) } , \dots , \eta _ { n } ^ { ( n ) } \big \}$

Hint. $p _ { n - 1 } = v _ { n } ^ { ( n ) } - ( \beta _ { n } ^ { ( n ) } / 2 ) T _ { n } ,$ recall Exercise 2.4.26.

3.5.4. Show that if $f$ has an absolutely convergent Chebyshev expansion

$$
\| f - w _ { n } ^ { ( n ) } \| \leqslant 2 \sum _ { i = n + 1 } ^ { \infty } | A _ { i } | - \sum _ { i = n + 1 } ^ { 3 n - 1 } | A _ { i } | .
$$

# 3.6. An Optimal Property of Chebyshev Expansions

As mentioned in Chapter 1, Section 1.5, the Chebyshev polynomials are members of larger families of sets of orthogonal polynomials. Each integrable function has an associated expansion in orthogonal polynomials of these other sets as well. We want to show next that in certain cases the Chebyshev expansion is best.

Let us recall that the ultraspherical polynomials $\{ p _ { n } ^ { ( \lambda ) } ( x ) \} _ { n = 0 } ^ { \infty }$ consist of polynomials $( p _ { n } ^ { ( \lambda ) }$ being of degree n) orthogonal on $\pmb { I }$ with respect to the weight function $w _ { \lambda } ( x ) = ( 1 - x ^ { 2 } ) ^ { \lambda - 1 / 2 }$ ,where $\lambda > - ( \frac { 1 } { 2 } )$ Thus, if we normalize the ultraspherical polynomials so that $p _ { n } ^ { ( \lambda ) } ( 1 ) = 1$ ,then $p _ { n } ^ { ( 0 ) } = T _ { n }$ ,and the case $\begin{array} { r } { \lambda = \frac { 1 } { 2 } } \end{array}$ gives the Legendre polynomials,whereas $\lambda = 1$ corresponds to the Chebyshev polynomials of the second kind. For our present purposes we add the convention that $p _ { n } ^ { ( \infty ) } ( x ) = x ^ { n }$ , i.e., the expansion of a function in terms of $\pmb { p _ { n } ^ { ( \infty ) } }$ , is its Taylor expansion about the origin. Szego [1,p.93] shows that for $0 < \lambda < \infty$

$$
p _ { n } ^ { ( \lambda ) } ( x ) = \sum _ { j = 0 } ^ { n } a _ { j , n } ^ { ( \lambda ) } T _ { j } ( x )
$$

with

$$
a _ { j , n } ^ { ( \lambda ) } \geqslant 0 , \qquad j = 0 , \ldots , n , \qquad n = 0 , 1 , 2 , \ldots , \qquad a _ { 0 , n } ^ { ( \lambda ) } + a _ { 1 , n } ^ { ( \lambda ) } > 0 ,
$$

and (3.79) also holds when $\lambda = \infty$ according to Exercise 1.5.31. An obvious consequence of (3.78) and (3.79) is that for $\lambda > 0$

$$
| p _ { n } ^ { ( \lambda ) } ( x ) | \leqslant p _ { n } ^ { ( \lambda ) } ( 1 ) = 1 , \qquad - 1 \leqslant x \leqslant 1 .
$$

Let

$$
s _ { n , \lambda } ( f ; x ) = \sum _ { k = 0 } ^ { n } f _ { k } ( \lambda ) p _ { k } ^ { ( \lambda ) } ( x ) , \qquad n = 0 , 1 , 2 , . . . ,
$$

be the partial sums of the expansion of $f$ in terms of the $\pmb { p } _ { \pmb { k } } ^ { ( \lambda ) }$ , and let us put

$$
\operatorname* { m a x } _ { - 1 \leqslant x \leqslant 1 } | f ( x ) - s _ { n , \lambda } ( f ; x ) | = \| f - s _ { n , \lambda } ( f ) \| = S _ { n } ( f ; \lambda ) .
$$

Theorem 3.17 (Rivlin and Wilson [1]). If $\lambda > 0 , f _ { k } ( \lambda ) \geqslant 0$ for $k > n ,$ and

$$
\sum _ { k = 0 } ^ { \infty } f _ { k } ( \lambda )
$$

converges, then

$$
S _ { n } ( f ; \lambda ) \geqslant S _ { n } ( f ; 0 ) = S _ { n } ( f ) .
$$

Equality holds in (3.82) only if $f \in { \mathcal { P } } _ { n }$

Proof

$$
S _ { n } ( f ; \lambda ) = f ( 1 ) - s _ { n , \lambda } ( 1 ) = \sum _ { k = n + 1 } ^ { \infty } f _ { k } ( \lambda ) .
$$

Now,

$$
\begin{array} { l } { \displaystyle { A _ { j } ( f ) = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } f ( x ) T _ { j } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } } \\ { \displaystyle { \quad = \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } \left[ \sum _ { k = 0 } ^ { \infty } f _ { k } ( \lambda ) p _ { k } ^ { ( \lambda ) } ( x ) \right] T _ { j } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } } } \\ { \displaystyle { \quad = \sum _ { k = 0 } ^ { \infty } f _ { k } ( \lambda ) \left[ \frac { 2 } { \pi } \int _ { - 1 } ^ { 1 } p _ { k } ^ { ( \lambda ) } ( x ) T _ { j } ( x ) \frac { d x } { \sqrt { 1 - x ^ { 2 } } } \right] } } \\ { \displaystyle { \quad = \sum _ { k = j } ^ { \infty } f _ { k } ( \lambda ) a _ { j , k } ^ { ( \lambda ) } } , } \end{array}
$$

where the ${ a } _ { j , k } ^ { ( \lambda ) }$ are defined in (3.78) and the term-by-term integration is justified by the convergence of (3.81), bearing in mind our normalization of the $\pmb { p _ { k } ^ { ( \lambda ) } }$ . Also, by (3.78) we have

$$
\sum _ { j = 0 } ^ { n } a _ { j , k } ^ { ( \lambda ) } = 1 ;
$$

hence

$$
\begin{array} { r l } { \underset { k = n + 1 } { \overset { \infty } { \sum } } f _ { k } ( \lambda ) = \underset { k = n + 1 } { \overset { \infty } { \sum } } f _ { k } ( \lambda ) \underset { j = 0 } { \overset { n } { \sum } } ^ { \prime } a _ { j , k } ^ { ( \lambda ) } = \underset { j = 0 } { \overset { \infty } { \sum } } ^ { \prime } \underset { k = n + 1 } { \overset { \infty } { \sum } } f _ { k } ( \lambda ) a _ { j , k } ^ { ( \lambda ) } } & { } \\ { = \underset { j = 0 } { \overset { n } { \sum } } ^ { \prime } \Bigg [ \underset { k = n + 1 } { \overset { \infty } { \sum } } f _ { k } ( \lambda ) a _ { j , k } ^ { ( \lambda ) } \Bigg ] + \underset { j = n + 1 } { \overset { \infty } { \sum } } \Bigg [ \underset { k = j } { \overset { \infty } { \sum } } f _ { k } ( \lambda ) a _ { j , k } ^ { ( \lambda ) } \Bigg ] } & { } \\ { = C + \underset { j = n + 1 } { \overset { \infty } { \sum } } A _ { j } ( f ) , } \end{array}
$$

in view of (3.84), with ${ \pmb C } \geqslant { \pmb 0 } .$ Since $A _ { j } ( f ) \geqslant 0$ for $j = n + 1 , \ldots$ ,by (3.84), we have

$$
\sum _ { j = n + 1 } ^ { \infty } A _ { j } ( f ) = S _ { n } ( f ; 0 )
$$

and the first part of the theorem is proved.

If $f \notin \mathcal { P } _ { n }$ so that, say, $f _ { m } ( \lambda ) > 0$ for $m > n ,$ , then, since either $a _ { 0 , m } ^ { ( \lambda ) }$ of $a _ { 1 , m } ^ { ( \lambda ) }$ is positive according to (3.79), either $f _ { m } ( \lambda ) a _ { 0 , m } ^ { ( \lambda ) }$ or $f _ { m } ( \lambda ) a _ { 1 , m } ^ { ( \lambda ) }$ is positive and the quantity $c$ in (3.85) is positive,which implies that the inequality holds in (3.82).

Remark $\pmb { I }$ As a matter of fact (3.82)can be replaced by

$$
S _ { n } ( f ; \mu ) \geqslant S _ { n } ( f ; 0 ) , \qquad 0 \leqslant \mu \leqslant \lambda .
$$

To see this we need the information (cf. Askey [1], but correct a misprint by reversing the inequality on the fourth line from the bottom of p. 301,and Rainville [1] for the case $\lambda = \infty$ that if $- ( \frac { 1 } { 2 } ) < \mu \leqslant \lambda$ and

$$
p _ { n } ^ { ( \lambda ) } ( x ) = \sum _ { j = 0 } ^ { n } a _ { j , n } ^ { ( \lambda , \mu ) } p _ { n } ^ { ( \mu ) } ( x )
$$

then

$$
a _ { j , n } ^ { ( \lambda , \mu ) } \geqslant 0 , \qquad j = 0 , \ldots , n , \qquad n = 0 , 1 , 2 , \ldots .
$$

Thus mimicking (3.84) yields

$$
f _ { j } ( \mu ) = \sum _ { k = j } ^ { \infty } f _ { k } ( \lambda ) a _ { j , k } ^ { ( \lambda , \mu ) } ,
$$

hence $f _ { k } ( \lambda ) \geqslant 0$ for $k > n$ implies $f _ { k } ( \mu ) \geqslant 0$ for $k > n ,$ ,and the theorem can be applied with $\lambda$ replaced by $\pmb { \mu } ,$ provided that

$$
\sum _ { k = 0 } ^ { \infty } f _ { k } ( \mu ) < \infty .
$$

This follows from the analog of (3.85) (with ${ a } _ { j , k } ^ { ( \lambda ) }$ replaced by $a _ { j , k } ^ { ( \lambda , \mu ) }$ and so on).

Remark 2. The theorem remains true if the coefficients $f _ { k } ( \lambda )$ alternate in sign for $k > n .$ To see this we observe that the $\pmb { p } _ { \pmb { k } } ^ { ( \lambda ) }$ are even functions for even $\pmb { k }$ and odd functions for odd $k ;$ thus applying the theorem to $f ( - x )$ proves the analogous result for alternating coefficients.

Remark 3. If the coeffcients are neither positive nor alternate in sign, (3.86) need not hold, as the example $f ( x ) = x ^ { 3 } - ( { \textstyle { \frac { 3 } { 2 } } } ) x ^ { 2 } - x , \lambda = \infty$ ， ${ \pmb n } = { \bf 0 } ;$ ， shows. We have for $0 \leqslant \alpha < \infty$

$$
\begin{array} { c l } { f _ { 0 } ( \alpha ) = \displaystyle \frac { \displaystyle \int _ { - 1 } ^ { 1 } f ( x ) ( 1 - x ^ { 2 } ) ^ { \alpha - 1 / 2 } d x } { \displaystyle \int _ { - 1 } ^ { 1 } \left( 1 - x ^ { 2 } \right) ^ { \alpha - 1 / 2 } d x } } \\ { \displaystyle = \frac { - \frac { 3 } { 2 } \displaystyle \int _ { - 1 } ^ { 1 } x ^ { 2 } ( 1 - x ^ { 2 } ) ^ { \alpha - 1 / 2 } d x } { \displaystyle \int _ { - 1 } ^ { 1 } \left( 1 - x ^ { 2 } \right) ^ { \alpha - 1 / 2 } d x } = - \frac { 3 } { 4 } \frac { 1 } { 1 + \alpha } . } \end{array}
$$

A small calculation gives

$$
\begin{array} { c } { { S _ { 0 } ( f ; 0 ) = 0 . 8 9 \ldots , } } \\ { { { } } } \\ { { S _ { 0 } ( f ; \infty ) = 1 . 5 , } } \\ { { { } } } \\ { { S _ { 0 } ( f ; 0 . 1 ) = 0 . 8 2 \ldots . } } \end{array}
$$