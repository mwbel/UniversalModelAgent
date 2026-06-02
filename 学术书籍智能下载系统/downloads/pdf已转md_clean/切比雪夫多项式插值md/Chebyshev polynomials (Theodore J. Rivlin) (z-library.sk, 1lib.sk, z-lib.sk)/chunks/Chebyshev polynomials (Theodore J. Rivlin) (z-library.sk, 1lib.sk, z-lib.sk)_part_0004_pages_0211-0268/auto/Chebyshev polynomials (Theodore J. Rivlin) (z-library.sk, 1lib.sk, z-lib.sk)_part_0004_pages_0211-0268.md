# 4

# ITERATIVE PROPERTIESAND SOME REMARKSABOUT THE GRAPHS OFTHE Tn

One of the most remarkable properties of the Chebyshev polynomials is the semi-group property (cf. Exercise 1.1.6)

$$
T _ { m } ( T _ { n } ( x ) ) = T _ { m n } ( x ) .
$$

An immediate consequence of the semigroup property is that the Chebyshev polynomials commute under composition; i.e.,

$$
T _ { m } ( T _ { n } ) = T _ { n } ( T _ { m } ) .
$$

The first section of this chapter is devoted to this property. In the second section we shall study the ergodic and mixing properties of the Chebyshev polynomials considered as transformations of $\pmb { I }$ onto itself, a study in which the semigroup property plays a role. In the third section the graphs of $y = T _ { n } ( x ) , \ - 1 \leqslant x \leqslant 1 _ { \cdot }$ for ${ n = 1 , 2 , . . . , 3 0 }$ are shown and some “white” curves are evident. These curves are identifed and an explanation of the phenomenon is proposed.

# 4.1. Permutable Polynomials

Two polynomials, $\pmb { p }$ and $\pmb q$ ,are called permutable if $p ( q ( x ) ) = q ( p ( x ) )$ for all $\pmb { x } .$ If we adopt the notation $p \cdot q$ to indicate the composition $p ( q ( x ) )$ ,then $\pmb { p }$ and $\pmb q$ are permutable if $p \cdot q = q \cdot p .$ If $\pmb { p }$ and $\pmb q$ are permutable, we shall also say that $\pmb { p }$ commutes with $\pmb q$ and, of course, $\pmb q$ commutes with $\pmb { p }$ . Composition satisfies

the associative law

$$
p \cdot ( q \cdot r ) = ( p \cdot q ) \cdot r .
$$

We shall write $p ^ { \{ n \} }$ for the $\pmb { n }$ fold composition $p \cdot p \cdots p .$ Since

$$
T _ { m } ( T _ { n } ( x ) ) = T _ { n } ( T _ { m } ( x ) ) = T _ { m n } ( x ) ,
$$

we see that any two Chebyshev polynomials are permutable. Our first result is that no polynomials other than Chebyshev polynomials can commute with a given $T _ { n }$ if $\pmb { n } \geqslant 2$

Theorem 4.1 (Bertram [1]). If $\pmb { n } \geqslant 2$ and the polynomial $\pmb { p }$ of degree $k \geqslant 1$ commutes with $T _ { n }$ ,then $\begin{array} { r } { p = T _ { k } } \end{array}$ if $\pmb { n }$ is even and $p = \pm T _ { k }$ if $\pmb { n }$ is odd.

Proof. We know (cf. Exercise 2.4.6) that $\pm T _ { m } ( x )$ are the only polynomial solutions of

$$
( 1 - x ^ { 2 } ) ( y ^ { \prime } ) ^ { 2 } = m ^ { 2 } ( 1 - y ^ { 2 } )
$$

for $m > 0$

The theorem is proved by showing that, if $\pmb { p }$ commutes with $T _ { n } , y = p$ satisfies (4.1) with $m = k$

The polynomial

$$
q ( x ) = ( 1 - x ^ { 2 } ) ( p ^ { \prime } ( x ) ) ^ { 2 } - k ^ { 2 } ( 1 - p ^ { 2 } ( x ) )
$$

is in $\mathcal { P } _ { 2 k - 1 }$ ，since the coefficient of $x ^ { 2 k }$ is zero, but

$$
\begin{array} { c } { { n ^ { 2 } q \cdot T _ { n } = n ^ { 2 } ( 1 - T _ { n } ^ { 2 } ) ( p ^ { \prime } \cdot T _ { n } ) ^ { 2 } - n ^ { 2 } k ^ { 2 } ( 1 - ( p \cdot T _ { n } ) ^ { 2 } ) } } \\ { { { } } } \\ { { = ( 1 - x ^ { 2 } ) ( T _ { n } ^ { \prime } ) ^ { 2 } ( p ^ { \prime } \cdot T _ { n } ) ^ { 2 } - k ^ { 2 } ( 1 - p ^ { 2 } ) ( T _ { n } ^ { \prime } \cdot p ) ^ { 2 } , } } \end{array}
$$

where we have used the permutability of $\pmb { p }$ and $T _ { n }$ and the fact that $T _ { n }$ satisfies (4.1) with ${ \pmb m } = { \pmb n } ,$ Now,

$$
( p ^ { \prime } \cdot T _ { n } ) T _ { n } ^ { \prime } = ( p \cdot T _ { n } ) ^ { \prime } = ( T _ { n } \cdot p ) ^ { \prime } = ( T _ { n } ^ { \prime } \cdot p ) p ^ { \prime } ,
$$

hence

$$
\begin{array} { r l } & { n ^ { 2 } q \cdot T _ { n } = ( 1 - x ^ { 2 } ) ( p ^ { \prime } ) ^ { 2 } ( T _ { n } ^ { \prime } \cdot p ) ^ { 2 } - k ^ { 2 } ( 1 - p ^ { 2 } ) ( T _ { n } ^ { \prime } \cdot p ) ^ { 2 } } \\ & { \phantom { n } = ( T _ { n } ^ { \prime } \cdot p ) ^ { 2 } ( ( 1 - x ^ { 2 } ) ( p ^ { \prime } ) ^ { 2 } - k ^ { 2 } ( 1 - p ^ { 2 } ) ) } \\ & { \phantom { n } = ( T _ { n } ^ { \prime } \cdot p ) ^ { 2 } q . } \end{array}
$$

Suppose that $q \neq 0$ has degree s $( \leqslant 2 k - 1 )$ ，then (4.2) implies that $s n = 2 ( n - 1 ) k + s$ so that $s = 2 k > 2 k - 1$ ， a contradiction. Thus $\pmb q$ is identically zero and $p = \pm T _ { k }$ .f $\pmb { n }$ is even, $T _ { n } \cdot ( - T _ { k } ) = T _ { n } \cdot T _ { k } = T _ { k } \cdot T _ { n } \nearrow$ $- T _ { k } \cdot T _ { n }$ ，hence $\begin{array} { r } { p = T _ { k } } \end{array}$ .If $\pmb { n }$ is odd, $T _ { n } \cdot ( - T _ { k } ) = { } - T _ { n } \cdot T _ { k } = { } - T _ { k } \cdot T _ { n }$ ，hence $p = \pm T _ { k }$ ■

A sequence of polynomials, each of positive degree, containing at least one of each positive degree and such that every two polynomials in it are permutable is called a chain. The Chebyshev polynomials $T _ { 1 } ( x ) , \ldots , T _ { n } ( x ) , \ldots ,$ form a chain. So do the powers $\pi _ { j } ( x ) \equiv x ^ { j } , j = 1 , 2 , \ldots ,$ ,as is easily verified. We shall see that these are essentially the only chains.

Suppose that

$$
\lambda ( x ) = a x + b , \qquad a \neq 0 ,
$$

so that

$$
\lambda ^ { - 1 } ( x ) = { \frac { x - b } { a } } .
$$

If $\pmb { p }$ and $\pmb q$ commute, it is clear that $\lambda ^ { - 1 } \cdot p \cdot \lambda$ and $\lambda ^ { - 1 } \cdot q \cdot \lambda$ also commute. Thus for any $\lambda$ of the form (4.3) the sequences $\lambda ^ { - 1 } \cdot T _ { j } \cdot \lambda , j = 1 , 2 , \ldots$ and $\lambda ^ { - 1 } \cdot \pi _ { j } \cdot \lambda , j = 1 , 2 , \ldots ,$ ，are also chains,and this is the reason the word “essentially” was needed above. We shall say that $\pmb { p }$ and $\lambda ^ { - 1 } \cdot p \cdot \lambda$ are similar; hence our goal is to show that the sequences $\left\{ T _ { j } \right\}$ and $\left\{ \pi _ { j } \right\}$ are the only chains, up to similarities. A first step in this direction is a companion piece to Theorem 4.1.

Theorem 4.2. If $\pmb { n } \geqslant 2$ and the polynomial $\pmb { p }$ of degree $k \geqslant 1$ commutes with $\pi _ { n } ( x ) ( = x ^ { n } )$ then $\mathfrak { p } = \pi _ { k }$ if $\pmb { n }$ is even and $p = \pm \pi _ { k }$ if $\pmb { n }$ is odd.

Proof. $y = \pi _ { n } ( x )$ satisfies

$$
x y ^ { \prime } = n y .
$$

The polynomial $q ( x ) = x p ^ { \prime } ( x ) - k p ( x )$ is in $\mathcal { P } _ { k - 1 }$ ,since the coefficient of $\scriptstyle x ^ { k }$ is zero. An argument analogous to that given in the proof of Theorem 4.1 yields $\pmb { n q } \cdot \pmb { \pi _ { n } } = ( \pmb { \pi _ { n } ^ { \prime } } \cdot \pmb { p } ) \pmb { q } .$ and if $\pmb q$ is of degree ${ \pmb s } \geqslant { \pmb 0 }$ then $s n = k ( n - 1 ) + s$ implies that $\pmb { s } = \pmb { k } ,$ a contradiction; $\pmb q$ must therefore be the zero polynomial. Hence ${ \boldsymbol { y } } = { \boldsymbol { p } }$ satisfies (4.4) with $\pmb { n }$ replaced by $k ,$ .which means that $p ( x ) = c x ^ { k } ( c \neq 0 )$ .The requirement that $\pmb { p }$ commute with $\pmb { \pi } _ { \pmb { \pi } }$ implies that $c x ^ { k n } = c ^ { n } x ^ { k n }$ ,i.e., $c ^ { n - 1 } = 1$ Since c must be real, $c = 1$ if $\pmb { n }$ is even and $c = \pm 1$ if $\pmb { n }$ is odd.

Theorem 4.3. There is at most one polynomial of degree $k \geqslant 1$ permutable with a given quadratic, $s ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 }$ ， ${ \pmb a } _ { 2 } \neq { \pmb 0 } .$

Proof. If we put

$$
\lambda ( x ) = \frac { x } { a ^ { 2 } } - \frac { a _ { 1 } } { 2 a _ { 2 } } ,
$$

we obtain

$$
( \lambda ^ { - 1 } \cdot s \cdot \lambda ) ( x ) = x ^ { 2 } + c ,
$$

where $c = a _ { 0 } a _ { 2 } + ( a _ { 1 } / 2 ) - ( a _ { 1 } ^ { 2 } / 4 ) .$ ，Thus to prove the theorem it suffices to show that there cannot be two distinct polynomials of degree $\pmb { k }$ commuting with $x ^ { 2 } + c$ for,if $f$ and $\pmb { g }$ are distinct polynomials of degree $\pmb { k }$ commuting with $\pmb { S } ,$ there are distinct polynomials of degree $\pmb { k }$ similar to $f$ and $\pmb { g }$ via (4.5) that commute with $x ^ { 2 } + c$

Suppose that $\pmb { p }$ and $\pmb q$ are distinct polynomials that satisfy

$$
\begin{array} { r } { p ( x ^ { 2 } + c ) = p ^ { 2 } ( x ) + c , } \\ { q ( x ^ { 2 } + c ) = q ^ { 2 } ( x ) + c ; } \end{array}
$$

then comparing leading coefficients on both sides of each equality reveals that $\pmb { p }$ and $\pmb q$ both have leading coefficient 1. Thus $r = p - q \in \mathcal { P } _ { k - 1 }$ . Also

$$
r ( x ^ { 2 } + c ) = p ^ { 2 } ( x ) - q ^ { 2 } ( x ) = r ( x ) ( p ( x ) + q ( x ) ) .
$$

If the degree of $r$ is $\mathbf { \Gamma } _ { t } \geqslant \mathbf { 0 } _ { : }$ ，then according to (4.7), $2 t = t + k$ or $\pmb { t = k } ,$ a contradiction. Therefore $\pmb { r }$ is the zero polynomial and $\pmb { p } = \pmb { q }$ This contradiction establishes the theorem.■

An immediate consequence of Theorem 4.3 is that a chain contains exactly one polynomial of each positive degree; i.e., a chain is a sequence $\left\{ p _ { j } \right\} , j = 1 ,$ $2 , \ldots$ ，where $\pmb { p } _ { j }$ is of degree $j$ and each pair of polynomials commutes. Two chains are called similar if there exists a $\lambda ( x )$ satisfying (4.3) such that each polynomial in one is similar via $\lambda$ to the polynomial of the other of the same degree. We can now prove our main result.

Theorem 4.4. Every chain is either similar to $\{ x ^ { j } \} , j = 1 , 2 , \ldots ,$ or $\bigl \{ T _ { j } \bigr \} , j = 1 ,$ 2,....

Proof. Let $\{ p _ { j } \} , j = 1 , 2 , \ldots$ , be a chain, with $p _ { 2 } ( x ) = a _ { 0 } + a _ { 1 } x + a _ { 2 } x ^ { 2 }$ .Let $\{ q _ { j } \} , j = 1 , 2 , \ldots ,$ ,be the chain similar to $\left\{ p _ { j } \right\}$ with $\lambda$ as defined in (4.5). Then $q _ { 2 } ( x ) = x ^ { 2 } + c ; q _ { 3 }$ commutes with $\pmb q _ { 2 }$ ,hence

$$
q _ { 3 } ( x ^ { 2 } + c ) = q _ { 3 } ^ { 2 } ( x ) + c .
$$

Thus $q _ { 3 } ^ { 2 } ( - x ) = q _ { 3 } ^ { 2 } ( x ) ,$ and since $\pmb { q _ { 3 } }$ is of degree 3 we see that $\begin{array} { r } { q _ { 3 } ( - x ) = - q _ { 3 } ( x ) ; } \end{array}$ i.e., $\pmb { q _ { 3 } }$ is an odd polynomial, say,

$$
q _ { 3 } ( x ) = b _ { 1 } x + b _ { 3 } x ^ { 3 } .
$$

If we substitute (4.9) into (4.8) and equate coefficients of like powers, we obtain $b _ { 3 } = 1 , b _ { 1 } = ( \textstyle { \frac { 3 } { 2 } } ) c ,$

$$
c ( c + 2 ) = 0 \qquad \mathrm { a n d } \qquad c ( 2 + c ) ( 2 c - 1 ) = 0 .
$$

Therefore the only possible values of $^ { c }$ are -2 and 0. If $\pmb { c = 0 }$ ,then $q _ { 2 } ( x ) = x ^ { 2 }$ and, according to Theorem 4.2, $q _ { j } ( x ) = x ^ { j } \operatorname { f o r } j = 1 , 2 , \ldots ,$ and $\left\{ p _ { j } \right\}$ is similar to $\{ x ^ { j } \}$

If $c = - 2$ consider the chain $\{ \mu ^ { - 1 } \cdot q _ { j } \cdot \mu \}$ ,where $\mu ( x ) = 2 x .$ Since

$$
( \mu ^ { - 1 } \cdot q _ { 2 } \cdot \mu ) = T _ { 2 } ,
$$

Theorem 4.1 informs us that

$$
\begin{array} { r } { \mu ^ { - 1 } \cdot q _ { j } \cdot \mu = T _ { j } , \qquad j = 1 , 2 , \ldots . } \end{array}
$$

Thus $\{ p _ { j } \}$ is similar to $\left\{ T _ { j } \right\}$ via the linear transformation $\lambda \cdot \mu .$

This theorem is proved by Block and Thielman [1] and Jacobsthal [1], and the proof given here is an amalgam of their work.

# EXERCISES 4.1.1-4.1.9

4.1.1. If $\pmb { p }$ commutes with $\pmb { q _ { 1 } }$ and $\pmb { q } _ { 2 }$ , it commutes with $\pmb { q } _ { 1 } \cdot \pmb { q } _ { 2 }$ and $\pmb { q } _ { 2 } \cdot \pmb { q } _ { 1 }$

4.1.2. If $\pmb q _ { 1 }$ and $\pmb { q } _ { 2 } ,$ , each of positive degree, commute with the same polynomial of degree 2, they are permutable.

A set of polynomials is called a $\pmb { P }$ -set if every two polynomials are permutable.A $\mathbf { \delta } _ { P } .$ set is closed if together with $\pmb { p }$ and $\pmb q$ it contains $\pmb { p } \cdot \pmb { q } ;$ it is called complete if no polynomial of positive degree that is not in the set commutes with all members of the set.

4.1.3. A complete $\pmb { P }$ -set is closed.

4.1.4. A chain is a complete $\pmb { P }$ -set.

4.1.5. $\pmb { p }$ commutes with every polynomial if, and only if, $\pmb { p } = \pmb { x }$

4.1.6. $\{ x + a \}$ where a runs over the reals is a complete $\pmb { P }$ -set.

4.1.7. $\{ t ( x - \alpha ) + \alpha \}$ where $\pmb { \alpha }$ is fixed and $\pmb { t }$ runs over the reals is a complete $\pmb { P }$ -set.

4.1.8. If $\pmb { p }$ of degree 2 and $\pmb q$ of degree 3 are permutable, then $\pmb { p }$ and $\pmb q$ are similar, via a common linear transformation, to either $x ^ { 2 }$ and $\scriptstyle { \pmb { x } } ^ { 3 }$ or $\pmb { T _ { 2 } }$ and $\pmb { T _ { 3 } }$

4.1.9. If $\pmb { p }$ of degree and $\pmb q$ of degree 4 are permutable, then ${ \pmb q } = { \pmb p } \cdot { \pmb p }$

A complete description can be given of permutable polynomials. Julia [1] and Ritt [1] showed that if $\pmb { p }$ and $\pmb q$ commute, either both are iterates of the same polynomial or both are similar, with respect to the same $\lambda ,$ to either Chebyshev polynomials or powers. Thus Theorem 4.4 is an immediate consequence of this definitive result. Unfortunately the methods of Julia and Ritt are formidably complicated and we cannot present them here. What we shall do next is give a complete description of all polynomials that commute with a given quadratic, a task that is amenable to elementary analysis.

In view of the proof of Theorem 4.3, it suffces to consider polynomials $\pmb { p }$ that commute with $x ^ { 2 } - c$ .Theorem 4.3 tells us that there is at most one polynomial of degree $k \geqslant 1$ that commutes with $x ^ { 2 } - c$ $\pmb { p } ;$ of degree $\pmb { k } ,$ commutes with $x ^ { 2 } - c ,$ then

$$
p ( x ^ { 2 } - c ) = p ^ { 2 } ( x ) - c
$$

and the leading coefficient of $\pmb { p }$ is 1. Also, if we replace $\pmb { x }$ by $- { \pmb x }$ in (4.10), we obtain $p ( x ^ { 2 } - c ) = p ^ { 2 } ( - x ) - c ,$ hence $p ^ { 2 } ( x ) = p ^ { 2 } ( - x )$ or $p ( x ) = \pm p ( - x ) .$ Thus $\pmb { p }$ is even if $\pmb { k }$ is even and odd if $\pmb { k }$ is odd. If $k = 1 , p = x ,$ ,which, of course, commutes with every polynomial. Putting this trivial case aside, we wish to establish the Julia-Ritt result in the special case that (4.1O) holds with $k \geqslant 2$ To this end some lemmas are useful.

Lemma 4.1.1. If $c < 0$ or $c > 2$ ， the sequence defined by

$$
t _ { n + 1 } = ( t _ { n } - c ) ^ { 2 } , \qquad n = 1 , 2 , \ldots ,
$$

with $t _ { 1 } = c ^ { 2 }$ , is strictly monotone increasing.

Proof. We note first that (4.11) implies that

$$
t _ { 2 } = ( c ^ { 2 } - c ) ^ { 2 } = c ^ { 2 } ( c - 1 ) ^ { 2 } > c ^ { 2 } = t _ { 1 } .
$$

Next we claim that $t _ { n } > c ^ { 2 }$ for $\begin{array} { r } { n \geqslant 2 . } \end{array}$ As we have just seen, this is the case for ${ \pmb n } = 2 .$ 、Suppose that $t _ { k } > c ^ { 2 }$

$$
t _ { k + 1 } = ( t _ { k } - c ) ^ { 2 } = t _ { k } ( t _ { k } - 2 c ) + c ^ { 2 } .
$$

Since $t _ { k } > c ^ { 2 }$ ， $t _ { k } - 2 c > c ^ { 2 } - 2 c = c ( c - 2 ) > 0 ;$ hence $t _ { k + 1 } > c ^ { 2 }$ and by mathematical induction $t _ { n } > c ^ { 2 }$ for $\pmb { n } \geqslant 2$ Finally, $t _ { n + 1 } > t _ { n }$ ， $n = 1 , 2 , \ldots .$ The case of $\pmb { n = 1 }$ has been established. Suppose $t _ { k } > t _ { k - 1 }$

$$
t _ { k + 1 } - t _ { k } = ( t _ { k } - c ) ^ { 2 } - ( t _ { k - 1 } - c ) ^ { 2 } = ( t _ { k } - t _ { k - 1 } ) ( t _ { k } + t _ { k - 1 } - 2 c ) ,
$$

but

$$
( t _ { k } + t _ { k - 1 } - 2 c ) > 2 c ^ { 2 } - 2 c = 2 c ( c - 1 ) > 0 ;
$$

thus $t _ { k + 1 } - t _ { k } > 0$ and the lemma is established.

Lemma 4.1.2. If $0 < c < 2 \AA$ , the sequence defined by

$$
t _ { n + 1 } = \sqrt { t _ { n } } + c , \qquad n = 1 , 2 , . . . ,
$$

with $t _ { 1 } = c ^ { 2 }$ , is strictly monotone increasing and $t _ { n } > c ^ { 2 }$ for $\pmb { n } \geqslant 2 .$

Proof. We have

$$
t _ { 2 } = 2 c > c ^ { 2 } = t _ { 1 } .
$$

We claim that $t _ { n } \geqslant 2 c$ ， $\pmb { n } \geqslant 2$ .This is true for $\pmb { n = 2 }$ 、Suppose it is true for ${ \pmb n } = { \pmb k } .$ Since $2 c > c ^ { 2 }$ , we see that $\sqrt { 2 c } > c$ and ${ \sqrt { 2 c } } + c > 2 c$ If $t _ { k } \geqslant 2 c$ ,then

$$
t _ { k + 1 } = { \sqrt { t _ { k } } } + c \geqslant { \sqrt { 2 c } } + c > 2 c ,
$$

establishing our claim by mathematical induction. Hence $t _ { n } > c ^ { 2 } , \ n \geqslant 2 .$ Suppose next that $t _ { k } > t _ { k - 1 }$ . We have

$$
t _ { k } = ( t _ { k + 1 } - c ) ^ { 2 } , \qquad t _ { k - 1 } = ( t _ { k } - c ) ^ { 2 } ,
$$

and therefore

$$
\begin{array} { c } { 0 < t _ { k } - t _ { k - 1 } = ( t _ { k + 1 } - c ) ^ { 2 } - ( t _ { k } - c ) ^ { 2 } } \\ { = ( t _ { k + 1 } - t _ { k } ) ( t _ { k + 1 } + t _ { k } - 2 c ) . } \end{array}
$$

We have seen that $t _ { k } \geqslant 2 c ;$ hence $t _ { k + 1 } + t _ { k } > 2 c$ and $t _ { k + 1 } - t _ { k } > 0$ Since $t _ { 2 } > t _ { 1 } ,$ ，the strict monotone increase of $\left\{ t _ { n } \right\}$ is established.

Theorem 4.4. If ${ \pmb p } ( { \pmb x } ) _ { : }$ , a polynomial of degree $k \geqslant 2 ,$ ， commutes with $x ^ { 2 } - c ,$ then either $\pmb { p } = \pmb { x } ^ { k }$ or $p = 2 T _ { k } ( x / 2 )$ or $\pmb { p }$ is an iterate of $( x ^ { 2 } - c )$

Proof. (i) Suppose that $k = 2 m - 1 , m \geqslant 2$ Then $\pmb { p }$ is odd and we can write

$$
p ( x ) = x q ( x ^ { 2 } ) ,
$$

where $\pmb q$ is of degree $m - 1 .$ .Equation (4.10) implies that

$$
( x ^ { 2 } - c ) q ( ( x ^ { 2 } - c ) ^ { 2 } ) = x ^ { 2 } q ^ { 2 } ( x ^ { 2 } ) - c ,
$$

and if we put $\scriptstyle x ^ { 2 } = t$

$$
( t - c ) q ( ( t - c ) ^ { 2 } ) = t q ^ { 2 } ( t ) - c .
$$

Suppose that $c < 0$ or $c > 2$ and $\left\{ t _ { n } \right\}$ is defined by (4.11). We claim that

$$
q ( t _ { n } ) = 1 , ~ n = 1 , 2 , \ldots .
$$

Putting $\pmb { t = 0 }$ in (4.13) yields $- c q ( c ^ { 2 } ) = - c ,$ and since $c < 0$

$$
q ( c ^ { 2 } ) = 1 ,
$$

establishing our claim for $\pmb { n = 1 }$ . Suppose that $q ( t _ { k } ) = 1$ Putting $t = t _ { k }$ in (4.13) yields

$$
( t _ { k } - c ) q ( ( t _ { k } - c ) ^ { 2 } ) = t _ { k } q ^ { 2 } ( t _ { k } ) - c
$$

or

$$
t _ { k + 1 } ^ { 1 / 2 } q ( t _ { k + 1 } ) = t _ { k } - c = t _ { k + 1 } ^ { 1 / 2 } .
$$

Since, in view of Lemma 4.1.1, $t _ { k + 1 } > 0$ we obtain

$$
q ( t _ { k + 1 } ) = 1 .
$$

Thus (4.14) is proved by mathematical induction. Therefore $q ( t )$ takes on the value 1 at least at $\pmb { m }$ distinct (distinct, since monotone increasing by Lemma 4.1.1) points $t _ { 1 } , \ldots , t _ { m }$ , hence is identically 1,contradicting the fact that it is of degree $m - 1 \geqslant 1 .$ .Thus we must have $0 \leqslant c \leqslant 2$

Suppose then that $0 < c < 2 $ Now let $\left\{ t _ { n } \right\}$ be defined by (4.12). We claim that again $q ( t _ { n } ) = 1 , n = 1 , \ldots$ . In view of(4.15),this is true for ${ \pmb n } = 1$ . Suppose $q ( t _ { k } ) = 1$ Then

$$
( t _ { k + 1 } - c ) q ( ( t _ { k + 1 } - c ) ^ { 2 } ) = t _ { k + 1 } q ^ { 2 } ( t _ { k + 1 } ) - c
$$

or

$$
t _ { k } ^ { 1 / 2 } = ( t _ { k } ^ { 1 / 2 } + c ) q ^ { 2 } ( t _ { k + 1 } ) - c .
$$

Since $t _ { k } ^ { 1 / 2 } + c = t _ { k + 1 } > 0 ;$ we obtain

$$
q ^ { 2 } ( t _ { k + 1 } ) = 1 .
$$

f $q ( t _ { k + 1 } ) = - 1$ putting $t _ { k + 2 } = t$ in (4.13) yields

$$
- ( t _ { k + 2 } - c ) = t _ { k + 2 } q ^ { 2 } ( t _ { k + 2 } ) - c \geqslant - c
$$

or $t _ { k + 1 } ^ { 1 / 2 } \leqslant c$ and $t _ { k + 1 } \leqslant c ^ { 2 }$ , contradicting Lemma 4.1.2. Thus $q ( t _ { k + 1 } ) = 1$ and by mathematical induction we have shown that $q ( t _ { n } ) = 1 , n = 1 , \ldots , m _ { ! }$ where according to Lemma 4.1.2, $t _ { 1 } < \cdots < t _ { m }$ . Therefore $q = 1$ ,contradicting the fact that the degree of $\pmb q$ is at least 1.

The only possible values of $\pmb { c }$ are therefore seen to be 0, 2. If $c = 0 .$ ,then $\pmb { p } = \pmb { x } ^ { k }$ according to Theorem 4.2, whereas, if $c = 2 , x ^ { 2 } - 2 = 2 T _ { 2 } ( x / 2 )$ and so $p = 2 T _ { k } ( x / 2 )$ certainly commutes with $x ^ { 2 } - 2$ .This concludes our proof in the case of odd $\pmb { k }$

(ii) Suppose that $k = 2 m , m \geqslant 1 .$ If $2 m = 2 ^ { \circ }$ then $p = ( x ^ { 2 } - c ) ^ { \{ s \} }$ (the sth iterate of $x ^ { 2 } - c )$ .Suppose that

$$
2 m = 2 ^ { s } l ,
$$

where $l \geqslant 3$ is odd. Since $\pmb { p }$ is an even function,

$$
p _ { 1 } ( x ) = p ( \sqrt { x + c } )
$$

is a polynomial of degree $2 ^ { s - 1 } l$ which satisfies

$$
p _ { 1 } ( x ^ { 2 } - c ) = p _ { 1 } ^ { 2 } ( x ) - c ;
$$

i.e., it commutes with $x ^ { 2 } - c$ If $\pmb { s = 1 }$ ， ${ \pmb p } _ { 1 }$ is of odd degree $\mathbf { \xi } _ { l , \textrm { \textbf { \xi } } }$ and therefore $c = 0 ;$ ，2 according to (i) above. If $s > 1 , p$ is of even degree, hence an even function, and $p _ { 2 } ( x ) = p _ { 1 } ( \sqrt { x + c } )$ commutes with $\ x ^ { 2 } - c$ and is of degree $2 ^ { s - 1 } l .$ Continuing in this fashion, we see that $p _ { s } ( x )$ is of degree l and commutes with $x ^ { 2 } - c$ Therefore $c = 0$ ,2 and we conclude as in part (i).

# 4.2. Ergodic and Mixing Properties

The Chebyshev polynomial $T _ { n } ( x )$ defines a mapping

$$
x \to T _ { n } ( x )
$$

of $\pmb { I }$ (the interval[-1,1]) onto $\pmb { I }$ for each $n = 1 , 2 , \ldots _ { \mathrm { ~ \scriptsize ~ { ~ 1 ~ } ~ , ~ 2 ~ } }$ ， which we denote by

$$
T _ { n } \colon I  I .
$$

Under this mapping each point of $I _ { \ast }$ except $\pm 1$ ,is the image of $\pmb { n }$ distinct points of $\pmb { I }$ ， since the mapping

$$
T _ { n } \colon ( \eta _ { i } ^ { ( n ) } , \eta _ { i - 1 } ^ { ( n ) } ) \to ( - 1 , 1 ) , \qquad i = 1 , \ldots , n
$$

is one-to-one and onto. The mapping inverse to $T _ { n }$ is written $T _ { n } ^ { - 1 }$ and is an nvalued mapping except at $\pm 1$ .The effect of the mapping (4.16) onto the subinterval $[ 0 , \frac { 1 } { 2 } ]$ of $\pmb { I }$ for ${ \pmb n } = 5$ is shown schematically in Figure 4.1.

The questions we shall be answering concern “metric” and “mixing” properties of the mapping $T _ { n } ^ { - 1 }$ ,the sequence of mappings $T _ { 1 } ^ { - 1 } , \ldots , T _ { n } ^ { - 1 } , \ldots ,$ and the iterates $T _ { n } ^ { - k }$ (meaning here and henceforth the $k$ -fold composition of $T _ { n } ^ { - 1 } )$ 0. We shall try to make precise the vague notions that the image intervals of $\pmb { A }$ in Figure 4.1 under $T _ { 5 } ^ { - 1 }$ combined have the same “length”as $\pmb { A }$ and that the mappings $T _ { n } ^ { - 1 } A , n = 1 , 2 , . . . ,$ and $T _ { 5 } ^ { - k } A , k = 1 , 2 , . . . ,$ increasingly homogenize or mix $\pmb { A }$ throughout $\pmb { I }$

![](images/1c41e8fe6454f26552a53242e3f9a245c98ca4d68b8d638051bbfa7a03672582.jpg)  
Figure 4.1

The vocabulary appropriate for making these notions precise is that of measure theory (cf. Halmos [1]). Let $( X , { \mathcal { B } } , \mu )$ be a separable finite measure space and let $\pmb { \tau }$ be a mapping of $\pmb { X }$ onto itself that is measurable,i.e., such that $\pmb { B } \in \mathcal { B }$ implies $\tau ^ { - 1 } B \in \mathcal { B } , \tau$ is said to be measure preserving if

$$
\mu ( \tau ^ { - 1 } B ) = \mu ( B ) , \qquad B \in \mathcal { B } ;
$$

and if $\pmb { \tau }$ is measure preserving it is called strongly mixing if

$$
\operatorname* { l i m } _ { k \to \infty } \mu ( \tau ^ { - k } A \cap B ) = { \frac { \mu ( A ) \mu ( B ) } { \mu ( X ) } }
$$

for all $A , B \in { \mathcal { B } } .$ .Every strongly mixing transformation is ergodic; i.e., if

$$
\pmb { \tau } ^ { - 1 } \pmb { A } = \pmb { A }
$$

for some $\pmb { A } \in \mathcal { B } ,$ , then either $\mu ( A ) = 0$ or $\mu ( A ) = \mu ( X ) .$ for if (4.19) holds (4.18) implies that

$$
\mu ( A \cap B ) = { \frac { \mu ( A ) \mu ( B ) } { \mu ( X ) } }
$$

for all $\pmb { B } \in \mathcal { B } .$ Hence, if $B = A$ ，

$$
\mu ( A ) \left( \frac { \mu ( A ) } { \mu ( X ) } - 1 \right) = 0 ,
$$

and either $\mu ( A ) = 0$ or $\mu ( A ) = \mu ( X )$

Finally, a sequence $\tau _ { 1 } , \tau _ { 2 } , \ldots , \tau _ { n } , \ldots ,$ of measurable transformations of $\pmb { X }$ onto itself, each of which preserves the measure $\mu ,$ is called strongly mixing if

$$
\operatorname * { l i m } _ { n \to \infty } \ ( \tau _ { n } ^ { - 1 } A \cap B ) = \frac { \mu ( A ) \mu ( B ) } { \mu ( X ) }
$$

for any A, $\pmb { { \cal B } } \in \mathcal { B } .$ The condition (4.17), that $\pmb { \tau }$ be measure preserving, has an equivalent functional form.

Lemma 4.2.1. $\pmb { \tau }$ is measure preserving if, and only if,

$$
\int _ { X } f ( \tau x ) d \mu = \int _ { X } f ( x ) d \mu
$$

for all $f \in L ^ { 1 } ( X , { \mathcal { B } } , \mu ) .$

Proof. (i) If (4.21) holds for all integrable $f ,$ then it holds when $f$ is the characteristic function of $\pmb { B } \in \mathcal { B }$ (the characteristic function of a set has the value 1 on the set and the value O off the set). But when $f$ is such

$$
\int _ { X } f ( \tau x ) d \mu = \mu ( \tau ^ { - 1 } B )
$$

and

$$
\int _ { X } f ( x ) d \mu = \mu ( B ) .
$$

(ii) Suppose that (4.17) holds. Then (4.21) holds when $f$ is the characteristic function of any $B \in { \mathcal { B } } _ { \mathrm { : } }$ ,as we have just seen in (i). Similarly,(4.21) holds when f is a simple function, i.e., a function that takes on only finitely many distinct values and is therefore a finite linear combination of characteristic functions. If $f$ is a nonnegative integrable function, then

$$
{ \begin{array} { r l } { { \displaystyle \int _ { X } f ( x ) d \mu = \operatorname* { s u p } \left[ \int _ { X } g ( x ) d \mu ; g \ \operatorname { s i m p l e } , \quad } & { 0 \leqslant g ( x ) \leqslant f ( x ) \right] } } \\ { = \operatorname* { s u p } \left[ \int _ { X } g ( \tau x ) d \mu ; g \ \operatorname { s i m p l e } , \quad } & { 0 \leqslant g ( x ) \leqslant f ( x ) \right] . } \end{array} }
$$

Now $g ( x ) \leqslant f ( x )$ for all $\pmb { x } \in \pmb { X }$ if, and only if, $g ( \tau x ) \leqslant f ( \tau x )$ for all ${ \pmb x } \in { \pmb X }$ ; hence

$$
{ \begin{array} { r l } { \displaystyle \int _ { X } f ( x ) d \mu = \operatorname* { s u p } \left[ \int _ { X } g ( \tau x ) d \mu ; g { \mathrm { ~ s i m p l e , ~ } } \quad } & { 0 \leqslant g ( \tau x ) \leqslant f ( \tau x ) \right] } \\ { \displaystyle = \operatorname* { s u p } \left[ \int _ { X } h ( x ) d \mu ; h { \mathrm { ~ s i m p l e , ~ } } \quad } & { 0 \leqslant h ( x ) \leqslant f ( \tau x ) \right] } \\ { \displaystyle = \int _ { X } f ( \tau x ) d \mu , } \end{array} }
$$

and (4.21) is established for nonnegative integrable functions. Equation (4.21) is now seen to hold for any integrable function by writing it as a difference of its positive and negative parts.

We shall also need a functional form for strong mixing.

Lemma 4.2.2. The sequence $\tau _ { 1 } , \ldots , \tau _ { n } , \ldots .$ , is strongly mixing with respect to the measure $\pmb { \mu }$ if, and only if,

$$
\operatorname* { l i m } _ { n \to \infty } \int _ { X } f ( \tau _ { n } x ) g ( x ) d \mu = { \frac { 1 } { \mu ( X ) } } \int _ { X } f ( x ) d \mu \int _ { X } g ( x ) d \mu
$$

for every $f , g \in L ^ { 2 } ( X , { \mathcal { B } } , \mu ) .$

Proof. (i) If we take $f$ to be the characteristic function of $\pmb { A }$ and $\pmb { g }$ to be the characteristic function of $\pmb { B } _ { i }$ ,then (4.22) implies (4.20).

(ii) If (4.20) holds, then (4.22) is valid when $f$ and $\pmb { g }$ are characteristic functions of any A, $\pmb { B } \in \mathcal { B }$ ,respectively. Hence (4.22) also holds when $f$ and $\pmb { g }$ are simple functions and we recall that the simple functions are dense in $L ^ { 2 } ( X , { \mathcal { B } } , \mu )$

At this point we consider a more general situation. Let $h _ { 0 } , h _ { 1 } , \ldots , h _ { k } , \ldots ,$ be functions in $L ^ { 2 } ( X , \beta , \mu )$ such that, given any $h \in L ^ { 2 } ( X , { \mathcal { B } } , \mu )$ and $\pmb \varepsilon > 0 ;$ , there exists

$$
w = \sum _ { i = 0 } ^ { m } c _ { i } h _ { i }
$$

such that

$$
\int _ { X } { ( h ( x ) - w ( x ) ) ^ { 2 } d \mu } < \varepsilon .
$$

We shall show next that if (4.22) holds when $\begin{array} { r } { g = h _ { i } , f = h _ { j } , } \end{array}$ for every $\pmb { i } = \pmb { 0 }$ ,1, $\ldots , j = 0 , 1 , \ldots$ ,then (4.22) holds for allf, $g \in L ^ { 2 } ( X , { \mathcal { B } } , \mu ) .$ Choosing the $\pmb { h _ { i } }$ to be the appropriate characteristic functions $[ ( X , { \mathcal { B } } , \mu )$ is separable] then proves the lemma.

Suppose then that (4.22) holds when $\begin{array} { r } { g = h _ { i } , f = h _ { j } } \end{array}$ for every $i = 0 , 1 , \ldots ,$ $j = 0 , 1 , \ldots$ ; then it clearly holds when $f$ and $\pmb { g }$ are finite linear combinations, say $\pmb { u }$ and $v ,$ of the $\pmb { h _ { i } }$ . Now suppose that $f$ and $\pmb { g }$ are any functions in $L ^ { 2 } ( X , { \mathcal { B } } , \mu )$ and, given $\pmb \varepsilon > 0$ ， $\pmb { u }$ and $\pmb { v }$ are finite linear combinations of the $\pmb { h _ { i } }$ such that

$$
\int _ { X } { \bigl ( } f ( x ) - u ( x ) { \bigr ) } ^ { 2 } d \mu < \varepsilon ^ { 2 } , \qquad \int _ { X } { \bigl ( } g ( x ) - v ( x ) { \bigr ) } ^ { 2 } d \mu < \varepsilon ^ { 2 } .
$$

We have

$$
\begin{array} { l l l } { C = \displaystyle \int _ { X } f ( \tau _ { u } x ) { \theta } ( x ) d { \mu } - \frac { 1 } { { \mu } ( X ) } \int _ { X } f ( x ) d { \mu } \displaystyle \int _ { X } { \theta } ( x ) d { \mu } } \\ { \ } \\ { \displaystyle } \\ { =  \displaystyle \int _ { X } [ f ( \tau _ { u } x ) - u ( \tau _ { u } x ) ] [ g ( x ) - v ( x ) ] d { \mu } + \displaystyle \int _ { X } v ( x ) ( f ( \tau _ { u } x ) - u ( \tau _ { u } x ) ) d { \mu }  } \\ { \displaystyle } \\ { \displaystyle } \\ { \displaystyle } \\ { \displaystyle } { \qquad + \displaystyle \int _ { X } u ( \tau _ { u } x ) ( g ( x ) - v ( x ) ) d { \mu } \Big \rbrace } \\ { \displaystyle } \\ { \displaystyle } {  \qquad +  \int _ { X } u ( \tau _ { u } x ) v ( x ) d { \mu } - \frac { 1 } { { \mu } ( X ) } \int _ { X } u ( x ) d { \mu } \int _ { X } v ( x ) d { \mu }  } \\ { \displaystyle } { \displaystyle } \\ { \displaystyle } { \qquad +  \frac { 1 } { { \mu } ( X ) } \int _ { X } u ( x ) d { \mu } \int _ { X } v ( x ) d { \mu } - \frac { 1 } { { \mu } ( X ) } \int _ { X } f ( x ) d { \mu } \int _ { X } g ( x ) d { \mu }  } \\ { \displaystyle } { \displaystyle } \\ { \displaystyle } { \displaystyle } \end{array}
$$

We observe that (4.21) implies that

$$
\int _ { X } { [ f ( \tau _ { n } x ) - u ( \tau _ { n } x ) ] ^ { 2 } d \mu } = \int _ { X } { [ f ( x ) - u ( x ) ] ^ { 2 } d \mu }
$$

and

$$
\int _ { X } { [ u ( \tau _ { n } x ) ] ^ { 2 } d \mu } = \int _ { X } { [ u ( x ) ] ^ { 2 } d \mu } .
$$

Thus Schwarz's inequality, together with (4.23), implies that $| D | < c _ { 1 } \varepsilon$ for some constant $c _ { 1 }$ . Moreover, if $\pmb { n }$ is sufficiently large $| E | < \varepsilon ,$ ，since we have seen that the lemma is valid for $\pmb { u }$ and ${ \pmb v } .$ Finally,

$$
\begin{array} { c } { { F = \displaystyle \frac { 1 } { \mu ( X ) } \Biggl [ \int _ { X } \left( f - u \right) d \mu \ \int _ { X } \left( g - v \right) d \mu - \int _ { X } g d \mu \int _ { X } \left( f - u \right) d \mu } } \\ { { - \displaystyle \int _ { X } f d \mu \ \int _ { X } \left( g - v \right) d \mu \Biggr ] } } \end{array}
$$

and Schwarz's inequality and (4.23) yield $| F | < c _ { 2 } \varepsilon$ for some constant $\scriptstyle { c _ { 2 } }$ . Thus $| \mathbf { C } | < c _ { 3 } \varepsilon$ for some constant $\pmb { c _ { 3 } }$ and $\pmb { n }$ sufficiently large,establishing the lemma.

Let us turn now to the Chebyshev transformations.

Theorem 4.5. Let $\mathcal { B }$ denote the family of Borel subsets of $I _ { : }$ and let $\lambda$ be Lebesgue measure. If $\pmb { \mu }$ is the measure defined by

$$
\mu ( B ) = \frac { 2 } { \pi } \int _ { B } \frac { \lambda ( d x ) } { \sqrt { 1 - x ^ { 2 } } } , \qquad B \in \mathcal { B } ,
$$

then each $T _ { n } , n = 1 , 2 , \ldots .$ preserves the measure $\pmb { \mu }$

Proof. Consider the measure space $( X ^ { \prime } , { \mathcal { B } } ^ { \prime } , \lambda ^ { \prime } ) ,$ where $\pmb { X ^ { \prime } }$ is the interval $[ 0 , \pi ] , \mathcal { B } ^ { \prime }$ ,the Borel subsets of $X ^ { \prime }$ ,and $\lambda ^ { \prime }$ is Lebesgue measure on ${ \mathcal { B } } ^ { \prime }$ .Let $\pmb R$ be the one-to-one measurable mapping of $\pmb { X }$ onto $\mathbf { \nabla } _ { \mathbf { X ^ { ' } } }$ defined by

$$
R : x \to x ^ { \prime } = \operatorname { a r c } \cos x .
$$

Put

$$
V _ { n } = R T _ { n } R ^ { - 1 } .
$$

f

$$
\frac { k \pi } { n } \leqslant x ^ { \prime } \leqslant \frac { ( k + 1 ) \pi } { n } , \qquad k = 0 , 1 , . . . , n - 1 ,
$$

we see that

$$
V _ { n } ( x ^ { \prime } ) = { \left\{ \begin{array} { l l } { n x ^ { \prime } - k \pi , } & { \quad k { \mathrm { ~ e v e n } } } \\ { - n x ^ { \prime } + ( k + 1 ) \pi , } & { \quad k { \mathrm { ~ o d d } } } \end{array} \right. }
$$

$[ V _ { s } ( x ^ { \prime } )$ is depicted in Figure 4.2]. An open subinterval of $[ 0 , \pi ]$ having length l is seen to be the image under $V _ { n }$ of $\pmb { n }$ intervals, each of length $l / n$ (as Figure 4.2 illustrates in the case $\pmb { n = 5 }$ .Thus $V _ { n }$ preserves Lebesgue measure. But if $- 1 \leqslant a < b < 1$ then

$$
\int _ { a } ^ { b } \frac { d x } { \sqrt { 1 - x ^ { 2 } } } = \int _ { R ( a ) } ^ { R ( b ) } d x ^ { \prime } ;
$$

hence for $A \in { \mathcal { B } } , \mu ( A ) = ( 2 / \pi ) \lambda ^ { \prime } ( R A )$ .Therefore $\mu ( T _ { n } ^ { - 1 } A ) = ( 2 / \pi ) \lambda ^ { \prime } ( R T _ { n } ^ { - 1 } A ) =$ $( 2 / \pi ) \lambda ^ { \prime } ( R T _ { n } ^ { - 1 } R ^ { - 1 } R A ) = ( 2 / \pi ) \lambda ^ { \prime } ( V _ { n } ^ { - 1 } R A ) = ( 2 / \pi ) \lambda ^ { \prime } ( R A ) = \mu ( A ) .$

Theorem 4.6 (Adler and Rivlin [1]). The sequence $T _ { 1 } , \ T _ { 2 } , . . . , T _ { n } , . . .$ is strongly mixing with respect to the measure $\pmb { \mu }$ defined in (4.24).

![](images/5b173ca36caa63680bc708977c77b66ed8777a26ff32ce5de1c49781a6c3fb56.jpg)  
Figure 4.2

Proof. Suppose that $h \in L ^ { 2 } ( X , { \mathcal { B } } , \mu ) ,$ Let $s _ { k } ( h ; x )$ be the partial sum of order $k$ of the Chebyshev expansion of $\pmb { h }$ (cf. p. 165). Familiar facts about Fourier series (cf. Zygmund [1,I, Chapter IV]) imply that, given $\pmb \varepsilon > 0$ ,there exists $\pmb { k }$ such that

$$
\int _ { I } [ h ( x ) - s _ { k } ( h ; x ) ] ^ { 2 } d \mu < \varepsilon .
$$

If we recall the argument in part (ii) of the proof of Lemma 4.2.2 and choose $h _ { j } = T _ { j } ( x ) ,$ the theorem follows from Lemma 4.2.2 and the observation that, given any $i = 0 , 1 , . . . , j = 0 , 1 , . . . ,$

$$
\int _ { I } T _ { i } ( T _ { n } ( x ) ) T _ { j } ( x ) d \mu = { \scriptstyle { \frac { 1 } { 2 } } } \int _ { I } T _ { i } ( x ) d \mu \int _ { I } T _ { j } ( x ) d \mu
$$

for all sufficiently large $\pmb { n }$ ，in view of the semigroup and orthogonality properties of the Chebyshev polynomials.

Corollary 4.6.1. Each $T _ { n } , n > 1 ,$ ,is strongly mixing,hence ergodic.

Proof. It is clear that the semigroup property implies that

$$
T _ { n } ^ { - k } = T _ { n k } ^ { - 1 } ,
$$

and so (4.18), with $\tau = T _ { n }$ ,follows from the theorem.

As an amusing application of Theorem 4.6 we shalldetermine the limiting value as $n  \infty$ of the area under the graph of $T _ { n } ( x )$ in the square with center at the origin and side 2 (see Figure 4.3). Let $K _ { n } ( y _ { 2 } )$ be the area under the graph of $y = T _ { n } ( x )$ contained between the lines $x = - 1 , x = 1 , y = - 1 ,$ $y = y _ { 2 } ,$ where $- 1 < y _ { 2 } \leqslant 1$ .We shall establish the existence and determine the value of

$$
K ( y _ { 2 } ) = \operatorname* { l i m } _ { n  \infty } K _ { n } ( y _ { 2 } ) .
$$

Put $g ( x ) = ( 1 - x ^ { 2 } ) ^ { 1 / 2 }$ and

$$
f ( x ) = \left\{ { \begin{array} { l l } { x , \qquad } & { - 1 \leqslant x \leqslant y _ { 2 } , } \\ { y _ { 2 } , } & { \quad y _ { 2 } \leqslant x \leqslant 1 . } \end{array} } \right.
$$

Then

$$
\begin{array} { c } { { \displaystyle { K _ { n } ( y _ { 2 } ) = \int _ { - 1 } ^ { 1 } \left( 1 + f ( T _ { n } ( x ) ) d x \right. } } } \\ { { \displaystyle { \phantom { \bigg | } } } } \\ { { \displaystyle { \phantom { \bigg | } } = 2 + \frac { \pi } { 2 } \int _ { I } f ( T _ { n } ( x ) ) g ( x ) d \mu . } } \end{array}
$$

![](images/c0adba7caf3ba17f3c6110cff7ffa33d14dde555b1b4869267c5d5ff473478f4.jpg)  
Figure 4.3

Thus, according to Theorem 4.6 and Lemma 4.2.2,

$$
K ( y _ { 2 } ) = \operatorname* { l i m } _ { n \to \infty } \ K _ { n } ( y _ { 2 } ) = 2 + { \frac { \pi } { 2 } } \int _ { I } f d \mu \int _ { I } g d \mu .
$$

Performing the integrations yields

$$
K ( y _ { 2 } ) = 2 + y _ { 2 } - \frac { 2 } { \pi } ( ( 1 - y _ { 2 } ^ { 2 } ) ^ { 1 / 2 } + y _ { 2 } \arcsin y _ { 2 } ) .
$$

Thus $K ( 1 ) = 2$ and the limiting area under $T _ { n } ( x )$ as $n  \infty$ is half the area of the square.

Moreover, by taking $g ( x )$ to be the product of the characteristic function of $[ x _ { 1 } , x _ { 2 } ]$ and $( 1 - x ^ { 2 } ) ^ { 1 / 2 }$ we see that the limit as ${ \pmb n }  \infty$ of the area under $y = T _ { n } ( x )$ contained in the box $( - 1 \leqslant ) x _ { 1 } \leqslant x \leqslant x _ { 2 } ( \leqslant 1 ) , \ - 1 \leqslant y \leqslant y _ { 2 }$ is $( x _ { 2 } - x _ { 1 } ) K ( y _ { 2 } ) / 2$ .Therefore the limit as ${ \pmb n }  \infty$ of the area under $y = T _ { n } ( x )$ bounded by the vertical lines $\mathbf { x } = \mathbf { x _ { 1 } }$ and ${ \boldsymbol { x } } = { \boldsymbol { x } } _ { 2 } ,$ ,and the continuous curves ${ y } = { y } _ { 1 } ( { x } )$ and $y = y _ { 2 } ( x ) ,$ ，where $- 1 \leqslant x _ { 1 } < x _ { 2 } \leqslant 1$ and $- 1 \leqslant y _ { 1 } ( x ) <$ $y _ { 2 } ( x ) \leqslant 1$ (for $x _ { 1 } \leqslant x \leqslant x _ { 2 } )$ is

$$
\begin{array} { r } { \frac { 1 } { 2 } \displaystyle \int _ { x _ { 1 } } ^ { x _ { 2 } } \left[ K ( y _ { 2 } ( x ) ) - K ( y _ { 1 } ( x ) ) \right] d x . } \end{array}
$$

# 4.3. The “White” Curves and Intersection Points of Pairs of Chebyshev Polynomials

It is obvious that the graph of $y = T _ { n } ( x ) , \ - 1 \leqslant x \leqslant 1 _ { : }$ $n = 1 , 2 , \ldots ,$ lies entirely in the square $A \colon - 1 \leqslant x \leqslant 1 .$ ， $- 1 \leqslant y \leqslant 1$ .In Figure 4.4 the graphs of $y = T _ { n } ( x ) , - 1 \leqslant x \leqslant 1$ ， $n = 1 , 2 , \ldots , 3 0$ are shown. Some“white”curves are seen streaking through A. For example, what appear to be a parabola with vertex at $( - 1 , 0 )$ and a straight line connecting $( - 1 , 1 )$ to $( 1 , - 1 )$ are clearly visible. Our purpose in this section is to identify the white curves and explain the phenomenon by relating it to the locus of intersection points of pairs of polynomials, $T _ { m } , \ T _ { n }$ .Therefore,we begin by considering such intersection points.

Suppose $1 \leqslant m < n .$ The zeros of $T _ { n } ( x ) - T _ { m } ( x )$ are easily determined by putting $\boldsymbol { x } = \cos { \theta }$ and solving cos $n \theta - \cos m \theta = 0$ . They are

$$
a _ { j } = \cos \frac { 2 j \pi } { m } , ~ j = 0 , 1 , . . . , \left[ \frac { n + m } { 2 } \right]
$$

and

$$
b _ { k } = \cos { \frac { 2 k \pi } { n - m } } , \qquad j = 1 , \ldots , \left[ { \frac { n - m - 1 } { 2 } } \right] .
$$

# A

![](images/8bc8480135122c5547b2fd6e997a7d2b9c14188d2f5e1edaa6e5030ef6a8318d.jpg)  
Figure 4.4

Thus all n zeros (counting multiplicities) are seen to lie in I. Moreover, it is easy to verify that

$$
m T _ { n } ^ { \prime } ( a _ { j } ) + n T _ { m } ^ { \prime } ( a _ { j } ) = 0 , \qquad - 1 < a _ { j } < 1
$$

and

$$
m T _ { n } ^ { \prime } ( b _ { k } ) - n T _ { m } ^ { \prime } ( b _ { k } ) = 0 , \qquad - 1 < b _ { k } < 1 .
$$

If $( x , T _ { n } ( x ) )$ is an intersection point of $T _ { m }$ and $T _ { n }$ which lies in the interior of $\pmb { A }$ then $T _ { n } ^ { \prime } ( x ) T _ { m } ^ { \prime } ( x ) \neq 0 .$ For if this were not the case then (4.27) and (4.28) would imply that $T _ { n } ^ { \prime } ( x ) = T _ { m } ^ { \prime } ( x ) = 0$ ，and, therefore, $T _ { n } ( x ) = T _ { m } ( x ) = \pm 1 _ { : }$ 、 contradicting the assumption that $( x , T _ { n } ( x ) )$ is inside $\pmb { A }$ Thus (4.27) and (4.28) yield

$$
{ \frac { T _ { n } ^ { \prime } ( x ) } { T _ { m } ^ { \prime } ( x ) } } = \left\{ \begin{array} { l l } { { - { \frac { n } { m } } , } } & { { \quad x = a _ { j } , } } \\ { { } } & { { { } } } \\ { { { \frac { n } { m } } , } } & { { \quad x = b _ { k } , } } \end{array} \right.
$$

at intersection points inside $\pmb { A }$

For $1 \leqslant m < n , m , n \leqslant 3 0 .$ ,intersection points of type $a _ { j }$ are more frequent than those of type $\boldsymbol { b } _ { \boldsymbol { k } }$ ,in view of (4.25) and (4.26). Equation (4.29) informs us that at each intersection point of type $a _ { j }$ of $T _ { m }$ and $T _ { n }$ which lies inside A the slopes of $T _ { m }$ and $T _ { n }$ are of opposite signs and,in magnitude,in the ratio m to n. Our explanation of the white curves is based on this observation. The chain of blank spaces resulting from the separation of slopes at these intersections is what is seen as a white curve in Figure 4.4. This asserted connection between the white curves and points of intersection of the graphs of pairs of Chebyshev polynomials receives support from the following considerations.

Theorem 4.7. If $0 < m \leqslant n$ and $T _ { m } ( x ) = T _ { n } ( x ) = y ,$ then

$$
( 1 - T _ { n - m } ( x ) ) ( T _ { 2 } ( y ) - T _ { n - m } ( x ) ) = 0 .
$$

Proof. The result is an easy consequence of the following identity:

$$
T _ { n } ^ { 2 } - 2 T _ { n - m } T _ { n } T _ { m } + T _ { m } ^ { 2 } = 1 - T _ { n - m } ^ { 2 } , \qquad 0 \leqslant m < n .
$$

(The special case, $m = 1$ of (4.31) can be found in Schur [1].) To establish (4.31) we recal (Exercise 1.1.3)that for $\pmb { p } \geqslant \pmb q$

$$
2 T _ { p } T _ { q } = T _ { p + q } + T _ { p - q } .
$$

Hence

$$
( T _ { n } - T _ { m } ) ^ { 2 } = ( 1 - T _ { n + m } ) ( 1 - T _ { n - m } )
$$

and

$$
2 ( 1 - T _ { m } T _ { n } ) = ( 1 - T _ { n + m } ) + ( 1 - T _ { n - m } ) .
$$

Equation (4.31) follows upon multiplying (4.33) by $1 - T _ { n - m }$ and subtracting the result from (4.32). If we then put $T _ { m } ( x ) = T _ { n } ( x ) = y$ in (4.31) the result is (4.30).

Remark. An identity analogous to (4.31) holds for the Chebyshev polynomials of the second kind. Namely,

$$
U _ { n } ^ { 2 } - 2 T _ { n - m } U _ { m } U _ { n } + U _ { m } ^ { 2 } = U _ { n - m - 1 } ^ { 2 } , \qquad 0 \leqslant m < n .
$$

The theorem informs us that the intersection points of the graphs of $T _ { m } ( x )$ and $\pmb { T _ { n } } ( \pmb { x } )$ lie on an algebraic curve whose equation is (4.30). But $T _ { n - m } ( x ) = 1$ precisely for $x = b _ { k } , k = 0 , 1 , \ldots , [ ( n - m ) / 2 ] .$ Thus the points of type $a _ { j }$ all lie on the curve

$$
T _ { 2 } ( y ) = T _ { n - m } ( x ) .
$$

![](images/087ac79941c86b215cfb7dd64d2a9c3f74defd3ba35c435fae51abb527d6b91d.jpg)  
Figure 4.5

This curve is symmetric with respect to the $\pmb { x }$ -axis. Figure 4.5 shows the part of the curve (4.34), contained in $\pmb { A }$ ,for n -m = q, $q = 1$ ,2, 3, 4. When $\pmb { q } = 2 p$ we have $y = \pm T _ { p } ( x )$ while for odd $\pmb q$

$$
y = \pm \bigg ( \frac { 1 + T _ { q } ( x ) } { 2 } \bigg ) ^ { 1 / 2 } .
$$

In particular, $T _ { 2 } ( y ) = T _ { 1 } ( x )$ is a parabola and $T _ { 2 } ( y ) = T _ { 3 } ( x )$ is the folium of Decartes given by $x = T _ { 2 } ( t ) , y = T _ { 3 } ( t ) , - 1 \leqslant t \leqslant 1 \leqslant$

Observe that the curves in Figure 4.5 seem identical to the brightest white curves in Figure 4.4. Lower values of $n - m = q$ correspond to higher numbers of intersection points of $T _ { n }$ and $T _ { m }$ . Hence for $1 \leqslant m < n \leqslant 3 0$ we cannot expect to see the curves corresponding to $q > 4$ very clearly in Figure 4.4. We next obtain another view of the white curves by applying a suitable homeomorphism to the square $\pmb { A }$

As we saw in the proof of Theorem 4.5, the mapping $\pmb { S } \colon ( \mathbf { x } , y ) $ $( x ^ { \prime } , y ^ { \prime } ) = ( \operatorname { a r c } \cos x ,$ arc cos y) is a homeomorphism of $\pmb { A }$ onto the square $\pmb { B } \mathrm { : }$

$0 \leqslant x ^ { \prime } \leqslant \pi , 0 \leqslant y ^ { \prime } \leqslant \pi$ which maps $( x , T _ { n } ( x ) )$ to $( x ^ { \prime } , V _ { n } ( x ^ { \prime } ) ) .$ where if

$$
\frac { k \pi } { n } \leqslant x ^ { \prime } \leqslant \frac { ( k + 1 ) \pi } { n } , \qquad k = 0 , 1 , . . . , n - 1 ,
$$

then

$$
V _ { n } ( x ^ { \prime } ) = { \left\{ \begin{array} { l l } { n x ^ { \prime } - k \pi , } & { \quad k { \mathrm { ~ e v e n } } , } \\ { - n x ^ { \prime } + ( k + 1 ) \pi , } & { \quad k \ \mathrm { o d d } } \end{array} \right. }
$$

(see Figure 4.2 for the case $n = 5$ . In short, $y ^ { \prime } = V _ { n } ( x ^ { \prime } )$ is a polygonal line (contained in $\pmb { B }$ ） issuing from the origin with slope $\pmb { n }$ ，whose slope changes sign-but maintains magnitude $\pmb { n }$ —consecutively at the top and bottom of $\pmb { B }$ (i.e., at $x ^ { \prime } = ( j \pi ) / n , j = 1 , \ldots , n - 1 ) .$

The orientation of $y ^ { \prime } = V _ { n } ( x ^ { \prime } )$ differs from that of its preimage $y = T _ { n } ( x ) ,$ a blemish which we correct by placing the polygonal lines on $\pmb { A }$ and making

# A

![](images/49c238eb613d9f00969a6903674578fdf8959431f420fc5f943e50f1dd2299af.jpg)  
Figure 4.6

their orientation agree with that of the Chebyshev polynomials. This is done by a linear mapping of $\pmb { B }$ onto $A , T \colon ( x ^ { \prime } y ^ { \prime } ) \to ( x , y )$ defined by

$$
x = 1 - \frac { 2 } { \pi } x ^ { \prime } , \qquad y = 1 - \frac { 2 } { \pi } y ^ { \prime } ,
$$

which gives as an image of $y ^ { \prime } = V _ { n } ( x ^ { \prime } ) ,$

$$
y = v _ { n } ( x ) = 1 - { \frac { 2 } { \pi } } V _ { n } \left( { \frac { \pi } { 2 } } \left( 1 - x \right) \right) .
$$

We call the resulting piecewise linear curve (contained in $\pmb { A }$ ), the stylized Chebyshev polynomial of degree $\pmb { n }$ .The mapping $L S : ( x , T _ { n } ( x ) ) \to ( x , v _ { n } ( x ) )$ is a homeomorphism of $\pmb { A }$ onto itself. Figure 4.6 shows $y = v _ { n } ( x ) , n = 1 , 2 , \ldots , 5 ,$ which should be compared to Figure 1.1. Figure 4.7 shows the same curves

#

![](images/0272ac5165fd23d1580135386d83c955981ec5039cc4e744d0a1af473c89dad4.jpg)  
Figure 4.7

for $n = 1 , 2 , \ldots , 3 0$ . The white curves now appear to be piecewise linear. Let us examine the intersection points of a pair of stylized Chebyshev polynomials.

f $v _ { n } ( x ) = v _ { m } ( x ) , 1 \leqslant m < n ,$ then $\pmb { x }$ is either

$$
c _ { j } = 1 - { \frac { 4 j } { n + m } } , \qquad j = 0 , . . . , \left[ { \frac { n + m } { 2 } } \right]
$$

or

$$
d _ { i } = 1 - { \frac { 4 i } { n - m } } , \qquad i = 1 , \ldots , \left[ { \frac { n - m - 1 } { 2 } } \right] .
$$

![](images/50f8a42157d7bd797f70147f3e3618e8875600e736fc12747b5a9d03b8eef20a.jpg)  
Figure 4.8

![](images/0271ef962c06c7a70e60c2c0e644f35ec5f3f67cd77368f47d6aa8665741bd62.jpg)  
Figure 4.9

We claim that at each $c _ { j }$ such that $( c _ { j } , v _ { n } ( c _ { j } ) )$ is an interior point of $\pmb { A }$ , the slope of ${ \pmb v } _ { \pmb n }$ (which is $\pm n )$ and the slope of $v _ { m }$ (which is $\pm m )$ have opposite signs. For, if they had the same signs and we suppose

$$
k < \frac { 2 j n } { n + m } < k + 1 \qquad \mathrm { a n d } \qquad k ^ { \prime } < \frac { 2 j m } { n + m } < k ^ { \prime } + 1 ,
$$

then $\pmb { k }$ and $k ^ { \prime }$ must have the same parity and $k + k ^ { \prime }$ is even. Since $k + k ^ { \prime } < 2 j < k + k ^ { \prime } + 2 ,$ .we have arrived at a contradiction. It is this substantial separation of slope (from $\pmb { n }$ to $- \pmb { m }$ or m to $- n )$ which, we believe, causes the blank areas that are seen as white lines in Figure 4.7.

The curve $T _ { 2 } ( y ) = T _ { n - m } ( x )$ contains the intersection points $\displaystyle ( a _ { j } , T _ { n } ( a _ { j } ) )$ of $y = T _ { n } ( x ) = T _ { m } ( x )$ which are inside $\pmb { A }$ according to Theorem 4.7. Its image under the homeomorphism, $\pmb { L S }$ of $\pmb { A }$ onto $\pmb { A }$ is

$$
v _ { 2 } ( y ) = v _ { n - m } ( x ) , - 1 \leqslant x \leqslant 1
$$

which, therefore, contains the intersection points $( c _ { j } , v _ { n } ( c _ { j } ) )$ of ${ y } = { v } _ { n } ( x )$ which are inside A. (4.35) is a piecewise linear curve which is.symmetric with respect to the $\pmb { x }$ axis. For $y \geqslant 0$ its equation is

$$
y = { \frac { 1 + v _ { n - m } ( x ) } { 2 } } .
$$

The curves (4.36) are shown in Figure 4.8 for $n - m = q = 1 , 2 , 3 , 4 ,$ and a depiction of (4.35) is given in Figure 4.9, the full symmetric version of (4.36). Observe that the curves in Figure 4.9 agree with the brightest white curves in Figure 4.7.

We have suggested that a natural phenomenon, the white curves in Figures 4.4 and 4.7, are the loci of intersection points of pairs of Chebyshev polynomials. Strong support is lent to this view by the observation that the curves shown in Figures 4.5 and 4.9 seem to coincide with the white curves in Figures 4.4 and 4.7 respectively. This section is based on Oritz and Rivlin [1].

# 5

# SOME ALGEBRAIC ANDNUMBER THEORETICPROPERTIES OFTHE CHEBYSHEVPOLYNOMIALS

In this final chapter we examine some elementary algebraic and number theoretic properties of the Chebyshev polynomials. The major result is the explicit complete factorization of the Chebyshev polynomials into irreducible factors with rational coefficients.

# 5.1. The Discriminant of the Chebyshev Polynomials

If $z _ { 1 } , \ldots , z _ { n }$ are complex numbers then we call

$$
d ( z _ { 1 } , \ldots , z _ { n } ) = \prod _ { 1 \leqslant i < j \leqslant n } ( z _ { j } - z _ { j } ) ^ { 2 }
$$

the discriminant of $( z _ { 1 } , \ldots , z _ { n } )$ .This name derives from the obvious fact that $d ( z _ { 1 } , \ldots , z _ { n } ) \neq 0$ if,and only if, the points $z _ { 1 } , \ldots , z _ { n }$ are distinct. $d ( z _ { 1 } , \ldots , z _ { n } )$ is a symmetric (polynomial) function of $z _ { 1 } , \ldots , z _ { n }$ and is, therefore,a polynomial in $a _ { n - 1 } = - \sigma _ { 1 } ,$ $a _ { n - 2 } = \sigma _ { 2 } ,$ …， $a _ { 0 } = ( - 1 ) ^ { n } \sigma _ { n }$ ，where $\sigma _ { 1 } , ~ . . . , ~ \sigma _ { n }$ are the elementary symmetric functions (cf. van der Waerden [1]). Then if $q ( z ) = z ^ { n } + a _ { n - 1 } z ^ { n - 1 } + \cdots + a _ { 0 } , d ( z _ { 1 } , \ldots , z _ { n } )$ is also called the discriminant of ${ \pmb q } , { \pmb d } ( { \pmb q } )$ . Of course, $d ( q ) = 0$ if, and only if $\pmb q$ has a multiple zero. If $p ( z )$ is any polynomial of degree $\pmb { n } ,$ ,i.e., $p ( z ) = a _ { 0 } + a _ { 1 } z + \cdots + a _ { n } z ^ { n }$ ， $\pmb { a _ { n } \neq 0 }$ , and its zeros are $z _ { 1 } , \ldots , z _ { n }$ ,then we define the discriminant of $\pmb { p } , \pmb { D } ( \pmb { p } )$ by

$$
D ( p ) = a _ { n } ^ { 2 n - 2 } d ( z _ { 1 } , . . . , z _ { n } ) .
$$

(The factor $a _ { n } ^ { 2 n - 2 }$ makes $D ( p )$ a polynomial in $a _ { 0 } , \ldots , a _ { n } .$

A useful tool in calculating the discriminant of a polynomial is provided by the following result.

Theorem 5.1. If $p ( z ) = a _ { n } ( z - z _ { 1 } ) \cdots ( z - z _ { n } ) , a _ { n } \neq 0 ,$ then

$$
D ( p ) = ( - 1 ) ^ { \frac { n ( n - 1 ) } { 2 } } a _ { n } ^ { n - 2 } \prod _ { j = 1 } ^ { n } p ^ { \prime } ( z _ { j } ^ { . } ) .
$$

Proof. For $j = 1 , \ldots , n$ we have

$$
\begin{array} { r l } & { p ^ { \prime } ( z _ { j } ) = a _ { n } ( z _ { j } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { j } - z _ { j - 1 } ) ( z _ { j } - z _ { j + 1 } ) \cdot \cdot \cdot ( z _ { j } - z _ { n } ) } \\ & { \qquad = ( - 1 ) ^ { n - j } ( z _ { j } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { j } - z _ { j - 1 } ) ( z _ { j + 1 } - z _ { j } ) \cdot \cdot \cdot ( z _ { n } - z _ { j } ) . } \end{array}
$$

Hence

$$
\prod _ { j = 1 } ^ { n } p ^ { \prime } ( z _ { j } ) = ( - 1 ) ^ { n ( n - 1 ) / 2 } a _ { n } ^ { n } d ( z _ { 1 } , . . . , z _ { n } )
$$

since every factor $z _ { k } - z _ { i }$ ， $k > i ,$ appears exactly twice in the product, once when $j = k$ and once when $j = i .$ Equation (5.3) now follows from (5.4) and (5.2).

Let us next calculate some discriminants using (5.3).

$$
\begin{array} { r l } & { p ^ { \prime } ( z _ { 1 } ) p ^ { \prime } ( z _ { 2 } ) = ( 2 a _ { 2 } z _ { 1 } + a _ { 1 } ) ( 2 a _ { 2 } z _ { 2 } + a _ { 1 } ) } \\ & { \qquad = 4 a _ { 2 } ^ { 2 } z _ { 1 } z _ { 2 } + 2 a _ { 1 } a _ { 2 } ( z _ { 1 } + z _ { 2 } ) + a _ { 1 } ^ { 2 } } \\ & { \qquad = 4 a _ { 0 } a _ { 2 } - a _ { 1 } ^ { 2 } . } \end{array}
$$

Thus (5.3) yields $D ( a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } ) = a _ { 1 } ^ { 2 } - 4 a _ { 0 } a _ { 2 } ,$ ，the familiar discriminant of a quadratic polynomial.

Example 2. $p ( z ) = z ^ { n } - 1$

$$
p ( z ) = \prod _ { j = 1 } ^ { n } ~ ( z - e ^ { 2 \pi i j / n } )
$$

and so

$$
\prod _ { j = 1 } ^ { n } p ^ { \prime } ( e ^ { 2 \pi i j / n } ) = n ^ { n } \prod _ { j = 1 } ^ { n } e ^ { - 2 \pi i j / n } = ( - 1 ) ^ { n - 1 } n ^ { n } ,
$$

and

$$
D ( z ^ { n } - 1 ) = ( - 1 ) ^ { ( n - 1 ) ( n - 2 ) / 2 } n ^ { n } .
$$

Example 3. $p ( z ) = T _ { n } ( z ) , n \geqslant 2 .$ $T _ { n } ( z ) = 2 ^ { n - 1 } ( z - \xi _ { 1 } ) \cdot \cdot \cdot ( z - \xi _ { n } )$ where $\xi _ { j } = \cos { ( ( 2 j - 1 ) \pi / 2 n ) } , j = 1 , \ldots , n .$   
We know (Exercise 1.2.3) that

$$
T _ { n } ^ { \prime } ( \xi _ { j } ) = ( - 1 ) ^ { j - 1 } n ( 1 - \xi _ { j } ^ { 2 } ) ^ { - 1 / 2 } , \qquad j = 1 , \ldots , n .
$$

Thus

$$
\prod _ { j = 1 } ^ { n } \ T _ { n } ^ { \prime } ( \xi _ { j } ) = ( - 1 ) ^ { n ( n - 1 ) / 2 } n ^ { n } \prod _ { j = 1 } ^ { n } ( 1 - \xi _ { j } ^ { 2 } ) ^ { - 1 / 2 } .
$$

But as $\xi _ { n + 1 - j } = - \xi _ { j } , j = 1 , . . . , n ,$ and $( 1 - \xi _ { j } ^ { 2 } ) = ( 1 - \xi _ { j } ) ( 1 + \xi _ { j } )$ we get

$$
\prod _ { j = 1 } ^ { n } ( 1 - \xi _ { j } ^ { 2 } ) ^ { - 1 / 2 } = \left( \prod _ { j = 1 } ^ { n } ( 1 - \xi _ { j } ) \right) ^ { - 1 } = { \frac { 2 ^ { n - 1 } } { T _ { n } ( 1 ) } } = 2 ^ { n - 1 } ,
$$

and upon substituting in (5.3) obtain

$$
D ( T _ { n } ) = 2 ^ { ( n - 1 ) ^ { 2 } } n ^ { n } .
$$

# EXERCISES 5.1.1-5.1.4

5.1.1. If $p ( z ) = 1 + z + \cdots + z ^ { n - 1 }$ show that

$$
D ( p ) = ( - 1 ) ^ { n ( n - 1 ) / 2 } n ^ { n - 2 } .
$$

# 5.1.2. Show that

$$
D ( U _ { n } ) = 2 ^ { n ^ { 2 } } ( n + 1 ) ^ { n - 2 } .
$$

Hint. Determine $U _ { n } ^ { \prime } ( \eta _ { j } ^ { ( n + 1 ) } )$ from (1.92) and then use (5.3). We define the Vandermonde determinant of $z _ { 1 } , \ldots , z _ { n }$ by

$$
V _ { n } = V _ { n } ( z _ { 1 } , . . . , z _ { n } ) = { \left| \begin{array} { l l l l } { 1 } & { 1 } & { \cdots } & { 1 } \\ { z _ { 1 } } & { z _ { 2 } } & { \cdots } & { z _ { n } } \\ { \vdots } & & & { \vdots } \\ { z _ { 1 } ^ { n - 1 } } & { z _ { 2 } ^ { n - 1 } } & { \cdots } & { z _ { n } ^ { n - 1 } } \end{array} \right| } .
$$

# 5.1.3. Show that

$$
V _ { n } = \prod _ { 1 \leqslant i < j \leqslant n } ( z _ { j } - z _ { i } ) ,
$$

hence $d ( z _ { 1 } , . . . , z _ { n } ) = V _ { n } ^ { 2 }$

Hint. First show that $V _ { n } ( z _ { 1 } , \ldots , z _ { n } ) = ( z _ { n } - z _ { 1 } ) \cdot \cdot \cdot ( z _ { n } - z _ { n - 1 } ) V _ { n - 1 } ( z _ { 1 } , \ldots , z _ { n - 1 } ) .$

In the paragraph immediately after Exercise 2.4.13 we introduced the transfinite diameter, $\delta ( B ) ,$ of an infinite compact set, $\pmb { B } _ { \mathrm { i } }$ ,in the plane.The transfinite diameter of such a $\pmb { B }$ can also be related to Vandermonde determinants (and hence discriminants) of a sequence of finite subsets of B. Consider the maximum of the geometric mean of the distances between pairs of points of the set $\left\{ z _ { 1 } , \ldots , z _ { n } \right\} \subset B$ over all choices of such points, i.e.,

$$
\mu _ { n } ( B ) = \operatorname* { m a x } _ { z _ { 1 } , \ldots , z _ { n } \in B } | V _ { n } ( z _ { 1 } , \ldots , z _ { n } ) | ^ { 2 / n ( n - 1 ) } .
$$

It can be shown that $\mu _ { n }$ decreases monotonically to $\delta ( B )$ as $n  \infty$ (cf.Hille [1]). It is of interest to determine the ${ \pmb \mu } _ { \pmb { n } } ( \pmb { B } )$ and the values of $z _ { 1 } , \ldots , z _ { n }$ (known as Fekete points) for which the maximum in (5.6) is attained.

5.1.4. Show that if $\pmb { B }$ is the closed unit disk $D ; | z | \leqslant 1 , \mu _ { n } ( B ) = n ^ { 1 / ( n - 1 ) }$ , and the zeros of $z ^ { n } - 1$ maximize $| V _ { \pmb { n } } |$

Hint. It is clear that we need to examine only distinct points of $| z | = 1$ Suppose $| z _ { j } | = 1 , j = 1 , \ldots , n .$ Recall Hadamard's determinant inequality: If $\pmb { A } = ( a _ { i j } )$ is an $\pmb { n } \times \pmb { n }$ determinant of complex numbers then

$$
| A | ^ { 2 } \leqslant \sum _ { j = 1 } ^ { n } | a _ { 1 j } | ^ { 2 } \sum _ { j = 1 } ^ { n } | a _ { 2 j } | ^ { 2 } \cdot \cdot \cdot \sum _ { j = 1 } ^ { n } | a _ { n j } | ^ { 2 } .
$$

Thus if we choose $A = V _ { n } ( z _ { 1 } , \ldots , z _ { n } )$ then $| V _ { n } | ^ { 2 } \leqslant n ^ { n }$ ,and conclude by invoking (5.5) and Exercise 5.1.3.Note that we have “reproved” that $\delta ( D ) = 1$ (Exercise 2.4.14).

# 5.2. The Factorization of the Chebyshev Polynomials into Polynomials with Rational Coefficients

This section is inspired by a remark of Schur [1, p. 423]. After observing that the zeros of $\pmb { T _ { n } } ( \pmb { x } )$ satisfy

$$
2 \xi _ { j } ^ { ( n ) } = e ^ { ( 2 j - 1 ) \pi i / 2 n } + e ^ { - ( 2 j - 1 ) \pi i / 2 n } , \qquad j = 1 , \ldots , n ,
$$

Schur remarks: “We are dealing with $( 4 n ) t \mathbf { h }$ roots of unity. The manner of the factorization of $T _ { n } ( x )$ over the field of rational numbers follows from this, since for every primitive mth root of unity, $\pmb { \rho }$ $( m > 4 )$ the sum $\pmb { \rho } + \pmb { \rho } ^ { - 1 }$ is of degree $\varphi ( m ) / 2$ ” We wish to provide the background and details that will expand Schur's remark into a complete description.

1.Preliminary Definitions and Results. We begin by reminding the reader of some notation, definitions and elementary facts of number theory and algebra. Let $\mathbb { C }$ and $\mathbb { Q }$ denote the felds of the complex numbers and rational numbers, respectively. $\mathbb { Z }$ is the set (ring) of all integers and $\ N$ the set of positive integers. If $\mathbf { \mu } _ { a , b \in \mathbb { N } }$ and $c \in \mathbb { N }$ is the greatest common divisor of $\pmb { a }$ and $\pmb { b }$ we write $( a , b ) = c .$ If $( a , b ) = 1$ we say that $\pmb { a }$ and $\pmb { b }$ are relatively prime. If $\pmb { n } \in \mathbb { N }$ then $\varphi ( n )$ is the number of integers j, $1 \leqslant j \leqslant n ,$ which are relatively prime to n. Thus $\varphi ( 1 ) = 1$ ， $\varphi ( 2 ) = 1$ ， $\varphi ( 3 ) = 2 ,$ $\varphi ( 4 ) = 2$ and $\varphi ( 5 ) = 4 .$ If $a , b \in \mathbb { Z }$ the notation ${ \pmb a } / { \pmb b }$ means that $\pmb { a }$ divides $\pmb { b }$ ,that is,there exists $c \in \mathbb { Z }$ such that $\pmb { b } = \pmb { a c }$ If $\mathbf { \Gamma } _ { a , b \in \mathbb { Z } }$ and $k \in \mathbb { N }$ ,we say that $\pmb { a }$ is congruent to $\pmb { b }$ modulo $\pmb { k }$ if $k / ( a - b )$ and we write $a \equiv b ( { \bmod { k } } )$ Suppose $a _ { j } , b _ { j } \in \mathbb { Z } ,$ $j = 0 ,$ ....，m， $a ( x ) = a _ { 0 } + a _ { 1 } x +$ $\cdots + a _ { m } x ^ { m }$ and $b ( x ) = b _ { 0 } + b _ { 1 } x + \cdots + b _ { m } x ^ { m }$ .Then if $k \in \mathbb { N }$ ， ${ \pmb a } ( { \pmb x } ) \equiv { \pmb b } ( { \pmb x } )$ $( \boldsymbol { \mathbf { m o d } } k )$ is defined to mean that $a _ { j } \equiv b _ { j } ( \mathrm { m o d } k ) , j = 0 , 1 , . . . , m .$

Let $\mathbb { Q } [ x ]$ denote the ring of polynomials with rational coefficients. $\dot { \pmb q } \in \mathbb { Q } [ { \pmb x } ]$ is said to be reducible over $\mathbb { Q }$ ,if there exist polynomials in $\mathbb { Q } [ \pmb { x } ]$ of positive degree, $r$ and $\pmb { s } ,$ such that $q ( x ) = r ( x ) s ( x )$ If $\pmb q \in \mathbb { Q } [ { \pmb x } ]$ is not reducible over $\mathbb { Q }$ we call it irreducible over $\mathbb { Q }$ . The complete factorization of a polynomial into its irreducible factors is what Schur is referring to above.

${ \pmb { \alpha } } \in \mathbb { C }$ is called an algebraic number if it is a zero of a polynomial with rational coefficients. If $\pmb { \alpha }$ is an algebraic number then it is clear that there exists a polynomial with rational coeffcients of least degree of which $\pmb { \alpha }$ is a zero, say $p ( { \boldsymbol { x } } )$ . We may assume, with no loss of generality, that $p ( { \boldsymbol { x } } )$ is monic. Such a $p ( { \boldsymbol { x } } )$ is called a minimal polynomial for $\pmb { \alpha } .$ Obviously, $p ( { \boldsymbol { x } } )$ is irreducible over $\mathbb { Q }$ If $p ( { \boldsymbol { x } } )$ is of degree $\pmb { k }$ we say that $\pmb { \alpha }$ is of degree $\pmb { k }$ over $\mathbb { Q }$ . An algebraic integer is an algebraic number which has a (monic) minimal polynomial with integer coefficients. We wish also to record the fact (cf.Pollard and Diamond [1]) that if $\pmb { \alpha }$ and $\beta$ are algebraic integers then so are $\alpha + \beta , \alpha - \beta$ and $\alpha \beta ,$ ,i.e., the algebraic integers form a ring.

# EXERCISES 5.2.1-5.2.23

5.2.1. Show that if $\pmb { p }$ is prime $\varphi ( p ) = p - 1$

5.2.2. Show that ${ \pmb \varphi } ( { \pmb n } )$ is even for ${ \pmb n } > 2$

Hint. If $k < n$ and $( k n ) = 1$ , then $( n - k , n ) = 1$

5.2.3. Show that modulo k we have: (1) ${ \pmb a } \equiv { \pmb a } _ { 3 } ^ { * }$ (2) $\pmb { a } \equiv \pmb { b } \Rightarrow \pmb { b } \equiv \pmb { a } ;$ (3) ${ \pmb a } \equiv { \pmb b }$ and $b \equiv c \Rightarrow a \equiv c ;$ (4) ${ \pmb a } \equiv { \pmb b }$ and $c \equiv d \Rightarrow a \pm c \equiv b \pm d _ { \mathrm { } }$ (5) $a \equiv b \Rightarrow a c \equiv b c ,$ Also verify that rules (1)-(5) remain valid for polynomials modulo $\mathbf { k }$

524. 10 $\pmb { p }$ isaprine $p \mathord { / { \vphantom { p } ( \binom { p } { j } ) } , j = 1 , . . . , p - 1 } .$

Hint.Mathematical induction on $j .$ Note that

$$
k \binom { p } { k } = ( p - ( k - 1 ) ) \binom { p } { k - 1 } , \qquad k < p .
$$

5.2.5. If $\pmb { a } \in \mathbb { Z }$ and $\pmb { p }$ is a prime

$$
a ^ { p } \equiv a ( \mathrm { m o d } p ) { \pmod { s { \mathrm { ~ T h e o r e m } } } } .
$$

Hint.Suppose (5.8) holds for $a = k \geqslant 1$ Let $f ( x ) = x ^ { p } - x .$ $f ( k + 1 ) =$ $f ( k ) + ( k + 1 ) ^ { p } - k ^ { p } - 1$ implies that $p / f ( k + 1 )$ by Exercise 5.2.4. Thus (5.8) can be verified for $a \geqslant 1$ by mathematical induction. But the case ${ \pmb a } < { \pmb 0 }$ now follows since $a ^ { p } - a = - ( ( - a ) ^ { p } - ( - a ) .$

5.2.6. If $q ( x ) = a _ { 0 } + a _ { 1 } x + \cdots + a _ { m } x ^ { m } , a _ { j } \in \mathbb { Z } , j = 0 , \ldots , m ,$ and $\pmb { \mathrm { p } }$ is a prime then

$$
q ( x ^ { p } ) \equiv ( q ( x ) ) ^ { p } ( { \bmod { p } } ) .
$$

Hint. Put $s _ { k } ( x ) = a _ { 0 } + \cdots + a _ { k } x ^ { k } , k = 0 , 1 , \ldots , m .$ When $\pmb q = \pmb { s } _ { 0 }$ (5.9) follows from (5.8). Suppose (5.9) holds for $q = s _ { k - 1 } , k - 1 < m .$ Then

$$
( s _ { k } ( x ) ) ^ { p } = ( s _ { k - 1 } ( x ) + a _ { k } x ^ { k } ) ^ { p } = ( s _ { k - 1 } ( x ) ) ^ { p } + a _ { k } ^ { p } x ^ { k p } + \sum _ { j = 1 } ^ { p - 1 } { \binom { p } { j } } \left( s _ { k - 1 } ( x ) \right) ^ { p - j } a _ { k } ^ { j } x ^ { k j } ,
$$

and conclude by mathematical induction and Exercises 5.2.3, 5.2.4 and 5.2.5.

It is worth mentioning here that if $r , q \in \mathbb { Z } [ x ]$ then $r ( x ) \equiv q ( x ) ( { \bmod { k } } )$ implies that $r ( a ) \equiv q ( a ) ( { \bmod { k } } )$ for all $\pmb { a } \in \mathbb { Z }$ .However,the converse is false as the example $r ( x ) = x ^ { p }$ ， $q ( x ) = x ,$ ${ \pmb k } = { \pmb p } ;$ ,a prime, shows.

5.2.7. Show that $T _ { 2 j + 1 } ( x ) , j = 1 , 2 , . . .$ is reducible over $\mathbb { Q }$

5.2.8. Show that an algebraic number has a unique minimal polynomial.

Hint. Let $\pmb { \alpha }$ be an algebraic number, $\pmb { \mathrm { p } } ( \pmb { x } )$ a minimal polynomial for it and $q \in \mathbb { Q } [ x ]$ also satisfy ${ \pmb q } ( { \pmb \alpha } ) = { \pmb 0 } .$ Then $q ( x ) = p ( x ) r ( x ) + s ( x )$ where $s ( x )$ is of lower degree than $\mathfrak { p } ( { \boldsymbol { x } } )$ Thus ${ \pmb s } ( \pmb { \alpha } ) = \pmb 0$ implies $\pmb { s = 0 }$ and ${ p / q }$ (meaning p is a factor of $\pmb q$ ). Now suppose $\pmb q$ were also a minimal polynomial and repeat the argument.

5.2.9. If p is the minimal polynomial of $\pmb { \alpha }$ and ${ \pmb q } ( { \pmb \alpha } ) = { \bf 0 }$ for $q \in \mathbb { Q } [ x ] ,$ then ${ p / q }$

5.2.10. If the algebraic integer $\pmb { \alpha }$ is a rational number then it is an integer.

Hint.What is the minimal polynomial of the algebraic number $\pmb { \alpha ? }$

5.2.11. Show that if $r , q \in \mathbb { Z } [ x ]$ satisfy

$$
r ( x ) q ( x ) \equiv 0 ( { \bmod { p } } ) , \qquad p \ { \mathrm { p r i m e } } ,
$$

then either $r ( x ) \equiv 0 ( { \mathrm { m o d } } p )$ or $q ( x ) \equiv 0 ( { \bmod { p } } )$

Hint. Suppose false.Delete all the terms in $\pmb { r }$ and $\pmb q$ which are divisible by p. Then polynomials $\pmb R$ and $\scriptstyle Q ,$ with no coefficients divisible by $\mathfrak { p }$ remain. But ${ \pmb r } ( { \pmb x } ) \equiv$ $R ( x ) ( { \bmod { p } } )$ and $q ( x ) \equiv Q ( x ) ( { \bmod { p } } )$ imply $R ( x ) Q ( x ) \equiv 0 ( { \bmod { p } } )$ ,a contradiction.

$\pmb { q } \in \mathbb { Z } [ \pmb { x } ]$ is called primitive if its coefficients have only $\pm 1$ as a common factor.

5.2.12. (Gauss Theorem) If $r , q \in \mathbb { Z } [ x ]$ are primitive polynomials so is rq.

5.2.13. If $p ( x ) = x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 0 }$ with $a _ { j } \in \mathbb { Z } , j = 0 , . . . , n - 1$ and $\pmb { p } ( \pmb { \alpha } ) = \mathbf { 0 }$ then $\pmb { \alpha }$ is an algebraic integer.

Hint. $\pmb { \alpha }$ is an algebraic number which is a zero of a primitive polynomial of minimal degree, $r ( x ) = b _ { n } x ^ { n } + \cdots + b _ { 0 } ,$ with $b _ { j } \in \mathbb { Z } , j = 0 , . . . , n$ and $\pmb { b _ { n } } > \mathbf { 0 } .$ Since $r / p$ (Exercise 5.2.9) $p ( x ) / r ( x ) = ( a / b ) s ( x )$ with $\mathbf { \Gamma } _ { a , b \in \mathbb { Z } }$ chosen so that $\pmb { s } \in \mathbb { Z } [ \pmb { x } ]$ is primitive. Then $\begin{array} { r } { b p ( x ) = a s ( x ) r ( x ) } \end{array}$ But Exercise 5.2.12 implies that $\pmb { s } ( \pmb { x } ) \pmb { r } ( \pmb { x } )$ is primitive and so is $\mathbf { p } ( { \pmb x } ) ,$ yielding ${ \pmb a } = { \pmb b }$ ， $\ b _ { \ n } = 1$

5.2.14. Suppose $p ( x ) = x ^ { n } + p _ { n - 1 } x ^ { n - 1 } + \cdots + p _ { 0 }$ and $q ( x ) = x ^ { m } + q _ { m - 1 } x ^ { m - 1 } + \cdots$ $+ q _ { 0 } , m < n ,$ ,have integer coefficients. Show that if

$$
q ( x ) = \prod _ { j = 1 } ^ { m } ( x - z _ { j } ) , \qquad p ( z _ { j } ) = 0 , \qquad j = 1 , \ldots , m
$$

then

$$
p = q r
$$

where $\pmb { r } \in \mathbb { Z } [ \pmb { x } ]$ and is monic.

Hint. $p - x ^ { n - m } q = g _ { 1 }$ ${ \pmb g } _ { 1 } \in \mathbb { Z } [ x ]$ is of degree $k _ { 1 } < n$ with leading coefficient ${ \pmb a } _ { \mathbf { 1 } }$ and $g _ { 1 } ( z _ { j } ) = 0 , j = 1 , \ldots , m .$ If $k _ { 1 } < m$ then $\pmb { g _ { 1 } = 0 }$ and we take $r = x ^ { n - m }$ If $k _ { 1 } \geqslant m$ put $g _ { 1 } - a _ { 1 } x ^ { k _ { 1 } - m } q = g _ { 2 }$ ${ \pmb g } _ { 2 } \in \mathbb { Z } [ x ]$ is of degree $k _ { 2 } < k _ { 1 }$ with leading coefficient ${ \pmb a } _ { \pmb { 2 } }$ and $g _ { 2 } ( z _ { j } ) = 0 , j = 1 , \ldots , m .$ f $k _ { 2 } < m$ then $\mathbf { \nabla } g _ { 2 } = \mathbf { 0 }$ and we take $r ( x ) = x ^ { n - m } + a _ { 1 } x ^ { k _ { 1 } - m }$ If $k _ { 2 } \geqslant m$ put $g _ { 2 } - a _ { 2 } x ^ { k _ { 2 } - m } q = g _ { 3 }$ etc.

Suppose n e N. Consider $\omega _ { k } = e ^ { 2 \pi i k / n }$ ， $k = 1 , \ldots , n ,$ the $\pmb { n }$ (distinct) nth roots of unity, i.e., the zeros of $z ^ { n } - 1 .$ It is clear that $\omega _ { 1 } ^ { k } = \omega _ { k }$ ， $k = 1 , \ldots , n .$ If $\omega _ { j } , j = 1 , . . . , n$ is such that for each $k = 1 , \ldots , n$ there exists an integer $m ( k )$ such that $\omega _ { k } = \omega _ { j } ^ { m }$ then ${ \pmb { \omega } } _ { j }$ is called a primitive nth root of unity. ${ \pmb { \omega } } _ { 1 }$ is an example of a primitive nth root of unity.

5.2.15. Show that if ${ \pmb { \omega } } _ { j }$ is a primitive nth root of unity then $m ( k )$ can always be chosen to satisfy $0 \leqslant m \leqslant n - 1$

Hint. Suppose not, then $m ( k ) = n q + r , 0 \leqslant r \leqslant n - 1 .$

5.2.16. If $\omega _ { j }$ is a primitive nth root of unity then $\omega _ { j } ^ { 0 } , \omega _ { j } ^ { 1 } , \ldots , \omega _ { j } ^ { n - 1 }$ are all the nth roots of unity.

5.2.17. $\omega _ { j }$ is a primitive nth root of unity,if and only if $( j , n ) = 1$

Hint. (i) If $\omega _ { j }$ is a primitive nth root of unity and $( j , n ) = d > 1$ then $j = k d , n = l d .$ But $\omega _ { j } ^ { l } = \omega _ { 1 } ^ { j l } = \stackrel { \cdot \cdot } { \omega _ { 1 } ^ { k d l } } = \omega _ { 1 } ^ { n k } = 1 ,$ ， contradicting $0 < l < n$

(ii)If $( j , n ) = 1$ show that if $\omega _ { j } ^ { 0 } , \ \omega _ { j } ^ { 1 }$ ，…， $\omega _ { j } ^ { n - 1 }$ are not distinct, we get a contradiction.

5.2.18. There are $\varphi ( n )$ primitive nth units of unity.

5.2.19. (i) If $\pmb { \omega }$ is a primitive nth root of unity it is not a kth root of unity for $k < n$ (ii) If $\pmb { \omega }$ is an nth root ofunity which is not primitive then it is a kth root of unity for $k < n$

5.2.20. If $\omega _ { j }$ is a primitive nth root of unity so is $\omega _ { j } ^ { - 1 }$ 5.2.21. If $\zeta _ { 1 } , \ldots , \zeta _ { _ { \varphi ( n ) } }$ are the primitive nth roots of unity then $\{ \zeta _ { 1 } , . . . , \zeta _ { \varphi ( n ) } \} = \{ \zeta _ { 1 } ^ { - 1 }$ ， $\cdots , \zeta _ { \varphi ( n ) } ^ { - 1 } \}$ . Also, if $\pmb { n } > 2$ ， $\zeta _ { 1 } \ldots \zeta _ { \varphi ( n ) } = 1$

Let $C _ { n } ( x ) = 2 T _ { n } ( x / 2 )$ ,n = 0,1,... . It is an obvious consequence of Exercise 1.5.54a that $C _ { n } ( x )$ is a monic polynomial with integer coefficients.

# 5.2.22. Show that

$$
C _ { n } ( x + x ^ { - 1 } ) = x ^ { n } + x ^ { - n } .
$$

Hint. See Exercise 2.4.11.

5.2.23. Suppose $p ( x ) = x ^ { 2 k } + a _ { 2 k - 1 } x ^ { 2 k - 1 } + \cdots + a _ { 1 } x + a _ { 0 } , a _ { 0 } \neq 0 ,$ has integer coeffcients and satisfies

$$
p ( x ) = x ^ { 2 k } p \left( { \frac { 1 } { x } } \right) .
$$

Then

$$
x ^ { - k } p ( x ) = q ( x + x ^ { - 1 } )
$$

where $\pmb q$ is a monic polynomial of degree $\pmb { k }$ with integer coefficients.

Hint. (5.11) implies that $a _ { 2 k - j } = a _ { j }$ $: a _ { j } , \ j = 0 , \ 1 , \ \ldots , \ k , \ a _ { 2 k } = 1 ,$ Thus $x ^ { - k } p ( x ) =$ $C _ { k } ( x + x ^ { - 1 } ) + a _ { 1 } C _ { k - 1 } ( x + x ^ { - 1 } ) + \cdots + a _ { k - 1 } C _ { 1 } ( x + x ^ { - 1 } ) + a _ { k }$ in view of (5.10).

2. The Irreducibility of the Cyclotomic Polynomials.For $\pmb { n } \geqslant 1$ let $\zeta _ { 1 } , \ldots , \zeta _ { { \varphi } ( n ) }$ denote the primitive nth roots of unity. The polynomial

$$
\Phi _ { n } ( x ) = ( x - \zeta _ { 1 } ) \cdot \cdot \cdot ( x - \zeta _ { \varphi ( n ) } )
$$

is called the cyclotomic polynomial of index n. Observe that the degree of $\Phi _ { n } ( x )$ is $\varphi ( n )$ . The subscript $\pmb { n }$ is a reminder that its zeros are nth roots of unity. Indeed we shall now show that $x ^ { n } - 1$ may be factored into a product of cyclotomic polynomials.

Theorem 5.2. If $\pmb { n } \geqslant 1$

$$
x ^ { n } - 1 = \prod _ { d / n } \Phi _ { d } ( x ) .
$$

Proof. If $\omega _ { k } , k = 1 , \ldots , n ,$ is an nth root of unity then it is a primitive dth root of unity for

$$
d = { \frac { n } { ( k , n ) } } ,
$$

a divisor of $\pmb { n } .$ . This is a consequence of Exercise 5.2.17 since

$$
\omega _ { k } = e ^ { 2 \pi i j / d } , \qquad j = \frac { k } { ( k , n ) }
$$

and $( j , d ) = 1$ Since $x ^ { n } - 1 = ( x - \omega _ { 1 } ) \cdot \cdot \cdot ( x - \omega _ { n } )$ we see that each of its linear factors is a factor of some $\Phi _ { d }$ .Conversely, if $\zeta$ is a primitive dth root of unity $( { \pmb x } - { \pmb \zeta } )$ is a factor of $\Phi _ { d }$ . But as ${ d / n }$ every such $\zeta$ is also a zero of $x ^ { n } - 1$ Furthermore, the linear factors appearing on the right-hand side of (5.13) are distinct, since if $d _ { 1 }$ and $d _ { 2 }$ are distinct divisors of $\pmb { n }$ no primitive $d _ { 1 }$ th root of unity can be a primitive $d _ { 2 } \operatorname { t h }$ root of unity, in view of Exercise 5.2.19.■

As an aside we notice that (5.13) yields

$$
\sum _ { d / n } \varphi ( d ) = n .
$$

The coefficients of $\Phi _ { n } ( x )$ are certainly complex numbers. We show next that, in fact, they are integers.

Theorem 5.3. $\Phi _ { n } ( x )$ has integer coefficients.

Proof. We proceed by mathematical induction on n. $\Phi _ { 1 } ( x ) = x - 1$ Assume that $\Phi _ { k } ( x )$ has integer coefficients for $k \leqslant n - 1 .$ Theorem 5.2 implies that

$$
q ( x ) = \frac { x ^ { n } - 1 } { \Phi _ { n } ( x ) } = \prod _ { d / n \atop d < n } \Phi _ { d } ( x ) ,
$$

and so $\pmb q$ ,as a product of monic polynomials with integer coefficients, is monic and has integer coeffcients. We now apply Exercise 5.2.4 with $p ( x ) = x ^ { n } - 1$ and $q ( x )$ as defined in (5.14). Then $x ^ { n } - 1 = q ( x ) r ( x )$ and $\pmb { r } \in \mathbb { Z } [ \pmb { x } ]$ But $\Phi _ { n } ( x ) = r ( x )$

We show next that the cyclotomic polynomials are irreducible over $\mathbb { Q }$ Our approach is to show that $\Phi _ { n } ( x )$ is equal to the minimal polynomial of $\zeta$ a primitive nth root of unity. Since $\zeta$ is a zero of ${ \mathfrak { x } } ^ { n } - 1$ ,Exercise 5.2.13 informs us that it is an algebraic integer. Let $q ( x ) = x ^ { k } + a _ { k - 1 } x ^ { k - 1 } + \cdots + a _ { 0 }$ be its minimal polynomial. Since $\zeta$ is a zero of $\pmb q$ as well as of $\Phi _ { n }$ ， $\pmb q$ is a divisor of $\Phi _ { n }$ according to Exercise 5.2.9. Thus all the zeros of $\pmb q$ are primitive nth roots of unity. We wish to show that allthe primitive nth roots of unity are zeros of $\pmb q$ To this end we follow Schur [2] in proving

Lemma 5.2.1. If $\pmb { p }$ is a prime and $( p , n ) = 1$ then if $\zeta$ is a zero of $\pmb q$ so is $\zeta ^ { p }$

Proof. Let $q ( x ) = ( x - \zeta ) ( x - \alpha _ { 1 } ) \cdot \cdot \cdot ( x - \alpha _ { k - 1 } )$ and suppose that $q ( \zeta ^ { p } ) { \neq } 0 .$ Then

$$
q ( \zeta ^ { p } ) = ( \zeta ^ { p } - \zeta ) ( \zeta ^ { p } - \alpha _ { 1 } ) \cdots ( \zeta ^ { p } - \alpha _ { k - 1 } ) ,
$$

a product of differences of nth roots of unity. Since the algebraic integers form a right the right-hand side of (5.15) is an algebraic integer, a divisor of the discriminant of $x ^ { n } - 1$ ，which according to (5.5) is $\pm { \pm } n ^ { \pm }$ .That is, there is an algebraic integer, $\beta _ { : }$ ，such that $\beta q ( \zeta ^ { p } ) = \pm n ^ { n }$

But (5.9) tells us that

$$
q ( \zeta ^ { p } ) \equiv ( q ( \zeta ) ) ^ { p } ( { \bmod { p } } ) .
$$

Thus $\pmb { p }$ divides ${ \pmb q } ( \zeta ^ { p } )$ 、That is, there is an algebraic integer,γ, such that $q ( \zeta ^ { p } ) = \gamma p$ Hence $( \gamma \beta ) p = \pm n ^ { n }$ or

$$
\gamma \beta = \frac { \pm n ^ { n } } { p } .
$$

But then the algebraic integer $\gamma \beta$ is a rational number and hence, according to Exercise 5.2.10,an integer. Thus ${ \pmb p } / n ^ { n }$ ,hence $( p , n ) > 1$ ,a contradiction which establishes the lemma.

We are now in a position to establish

Theorem 5.4. The cyclotomic polynomial, $\Phi _ { n } ( x ) ,$ is irreducible over the rational numbers.

Proof. Let $\pmb q$ be as above, the minimal polynomial of $\zeta$ ,a primitive nth root of unity. We need only show that every primitive nth root of unity is a zero of $\pmb q .$ . Since $\zeta$ is a primitive nth root of unity any other primitive nth root of unity is a power of $\zeta ,$ say $\zeta ^ { m } { } _ { ; }$ and $( m , n ) = 1$ Suppose $\pmb { m } = \pmb { p _ { 1 } } \ldots \pmb { p _ { t } }$ is the prime decomposition of $\pmb { m } ,$ ，with primes repeated according to their multiplicity. Clearly, $( p _ { j } , n ) = 1 , j = 1 , \ldots , t .$ In view of Lemma 5.21, $\zeta ^ { p _ { 1 } }$ is a zero of $\pmb q$ Hence upon replacing $\zeta$ by $\zeta ^ { p _ { 1 } }$ we observe that $\zeta ^ { p _ { 1 } p _ { 2 } }$ is a zero of $\pmb q$ Repetition of this procedure produces a proof, by mathematical induction， that $q ( \zeta ^ { m } ) = 0 .$ Thus $\Phi _ { n } ( x ) = q ( x )$ and is, therefore, irreducible over $\mathbb { Q }$

# EXERCISES 5.2.24-5.2.25

5.2.24. Show that if $\pmb { n } \geqslant 2$

$$
\Phi _ { n } ( x ) = x ^ { \varphi ( n ) } \Phi _ { n } \left( { \frac { 1 } { x } } \right) .
$$

Hint.Exercise 5.2.21.

5.2.25. If $\pmb { n } > 2$ and $\varphi ( n ) = 2 k$ then

$$
x ^ { - k } \Phi _ { n } ( x ) = q _ { n } ( x + x ^ { - 1 } )
$$

where $\pmb { q _ { n } }$ is a monic polynomial of degree $\pmb { k }$ with integer coefficients, and irreducible over $\pmb { \mathbb { Q } }$

Hint. (i) Exercises 5.2.23 and 5.2.24 (with $\pmb { p } = \pmb { \Phi _ { n } }$ and $\smash { q = q _ { n } }$ (ii) If $\pmb { q _ { n } }$ is reducible then $q _ { n } = u v$ and $\pmb { u }$ has degree $\pmb { \mu } ,$ $1 < \mu < k .$ Then $\Phi _ { n } ( x ) = ( x ^ { \mu } u ( x + x ^ { - 1 } ) ) ( x ^ { k - \mu } v ( x + x ^ { - 1 } ) ) ,$ ，contradicting Theorem 5.4.

3. The Factorization of the Chebyshev Polynomials over $\pmb { \mathbb { Q } }$ We are now in a position to justify Schur's remark quoted at the beginning of Section 5.2. First we observe that $\pmb { T _ { n } } ( \pmb { x } )$ is irreducible over $\mathbb { Q }$ if, and only if, the same is true of $C _ { n } ( x ) = 2 T _ { n } ( x / 2 )$ Thus we restrict our attention to $C _ { n } ( x ) , n = 1 , 2 , \ldots$ . Clearly $C _ { 1 } ( x ) = x$ and $C _ { 2 } ( x ) = x ^ { 2 } - 2$ are irreducible over $\mathbb { Q }$ Henceforth we suppose that $\pmb { n } > 2$ .The zeros of $C _ { n } ( { \boldsymbol { x } } )$ are

$$
x _ { j } ^ { ( n ) } = 2 \xi _ { j } ^ { ( n ) } = e ^ { ( 2 j - 1 ) \pi i / 2 n } + e ^ { - ( 2 j - 1 ) \pi i / 2 n } , \qquad j = 1 , \ldots , n ,
$$

so that

$$
C _ { n } ( x ) = ( x - x _ { 1 } ) \cdots ( x - x _ { n } )
$$

is the factorization of $C _ { n } ( { \pmb x } )$ over $\mathbb { R } .$ By judicious grouping of the factors in (5.18) we shall,following Hsiao [1] (see also Kimberling [1]), determine when $C _ { n } ( { \boldsymbol { x } } )$ is irreducible over $\mathbb { Q }$ and what its irreducible factors are when it is reducible.

Let $\pmb { h }$ denote an odd divisor of n. Put

$$
F _ { h } ( t ) = \prod _ { \substack { j = 1 } } ^ { n } ( t - x _ { j } ) .
$$

Keep in mind that the index $\pmb { n }$ is tacit in $\pmb { F _ { h } }$

Lemma 5.2.2. $F _ { h } ( t )$ is monic, has integer coefficients and is irreducible over $\mathbb { Q }$

Proof. (i) Suppose $\pmb { h } = 1$ .Put $m = 4 n$ (5.16) yields

$$
x ^ { - \varphi ( m ) / 2 } \Phi _ { m } ( x ) = Q _ { 1 } ( x + x ^ { - 1 } )
$$

(where we write $Q _ { 1 }$ in place of $q _ { m }$ since we wish the subscript to reflect that we are putting $h = 1 \mathrm { \dagger }$ )，where $Q _ { 1 }$ is monic, of degree $\varphi ( m ) / 2 ,$ has integer coefficients and is irreducible over $\mathbb { Q }$ But in view of (5.17), $x _ { j } , j = 1 , . . . , n$ with $( 2 j - 1 , 4 n ) = ( 2 j - 1 , 2 n ) = 1 ,$ , are zeros of $Q _ { 1 } ( t )$ according to (5.20), since $e ^ { 2 \pi i ( 2 j - 1 ) / 4 n }$ is a primitive (4n)th root of unity and thus a zero of $\Phi _ { m }$ . Now $\varphi ( 4 n ) = 2 \varphi ( 2 n )$ (cf. Exercise 5.2.2) hence $Q _ { 1 }$ is of degree $\varphi ( 2 n )$ and so the $\boldsymbol { x } _ { j }$ such that $( 2 j - 1 , 2 n ) = 1$ are all the zeros of $\pmb { Q _ { 1 } }$ . Thus, $Q _ { 1 } ( t ) = F _ { 1 } ( t ) ,$ and the lemma is proved for $\pmb { h } = 1$

(ii) Suppose $h > 1$ $( 2 j - 1 , 2 n ) = h ;$ $1 \leqslant j \leqslant n ,$ then $2 j - 1 = ( 2 i - 1 ) h$ where

$$
\left( 2 i - 1 , { \frac { 2 n } { h } } \right) = 1 , \qquad 1 \leqslant i \leqslant { \frac { n } { h } } ,
$$

and if (5.21) holds then $2 j - 1 = ( 2 i - 1 ) h$ satisfies $( 2 j - 1 , 2 n ) = h , 1 \leqslant j \leqslant n .$ As (5.21) suggests we now repeat the argument in (i) with $m = 4 n / h$ Equation (5.16) now yields

$$
x ^ { - \varphi ( m ) / 2 } \Phi _ { m } ( x ) = Q _ { h } ( x + x ^ { - 1 } )
$$

(where we write $Q _ { h }$ in place of $\pmb { q _ { m } }$ to indicate that $( 2 j - 1 , 2 n ) = h , j = 1 , \ldots , n ) ,$ where $Q _ { h }$ is monic of degree $\varphi ( m ) / 2 = \varphi ( 2 n / \hbar ) ,$ has integer coefficients and is irreducible over $\mathbb { Q }$ .We now conclude, as in (i), that $Q _ { h } ( t ) = F _ { h } ( t ) ,$ ,and the proof of the lemma is complete.

We now have what Schur's remark,quoted at the beginning of this section, suggested: the complete factorization of the Chebyshev polynomials over $\mathbb { Q }$ ·

Theorem 5.5. If ${ \pmb n } > 2$ then

$$
C _ { n } ( t ) = \prod _ { h / n \atop h o d d } F _ { h } ( t ) .
$$

Proof. Each $x _ { j } , j = 1 , . . . , n$ is a zero of $F _ { h } ( t )$ exactly when $( 2 j - 1 , 2 n ) = h ,$ and for each $\pmb { h }$ which is an odd divisor of $\pmb { n }$ there exists at least one j, $1 \leqslant j \leqslant n$ such that $( 2 j - 1 , 2 n ) = h , ( { \mathrm { e . g . } } , j = ( h + 1 ) / 2 )$ .Thus Lemma 5.2.2 implies that (5.22) is the factorization of $C _ { n } ( t )$ over $\mathbb { Q }$ ：

Remark 1. $T _ { n } ( x )$ is irreducible over $\pmb { \mathbb { Q } }$ only if $\displaystyle n = 2 ^ { k } , k = 0 , 1 , 2 , \ldots .$

Remark 2. Suppose $n \geqslant 3$ is odd. Then $T _ { n } ( x ) / x$ is irreducible over $\mathbb { Q }$ ,if and only if, $\pmb { n }$ is a prime. For, $\smash {  { F _ { n } } ( t ) = t }$ Hence if $\pmb { n }$ is a prime $C _ { n } ( t ) = t F _ { 1 } ( t ) ;$ while if $\pmb { n }$ is not a prime it has a prime factor, $p , 1 < p < n _ { \cdot }$ ,and the factors $F _ { h } ( t )$ with $h = 1 , p , n$ are present on the right-hand side of (5.22).

We turn next to the Chebyshev polynomials of the second kind. An immediate remark is that $U _ { \pmb { n } } ( \pmb { x } )$ is reducible over $\mathbb { Q }$ for every $n \geqslant 2 ,$ as is obvious from the elementary identities

$$
U _ { 2 k + 1 } = 2 T _ { k + 1 } U _ { k } , U _ { 2 k } = ( U _ { k } - U _ { k - 1 } ) ( U _ { k } + U _ { k - 1 } ) , \qquad k \geqslant 1 .
$$

Our experience with the Chebyshev polynomials of the first kind will make the task of exhibiting the complete factorization of the $U _ { \pmb { k } } ( \pmb { x } )$ over $\mathbb { Q }$ fairly easy. We begin with the observation that the factorization of $U _ { \pmb { k } } ( \pmb { x } )$ over $\mathbb { Q }$ is equivalent to that of $S _ { k } ( x ) ( = U _ { k } ( x / 2 ) )$ . Thus we restrict our attention to $\stackrel { \cdot } { S } _ { n - 1 } ( x ) , \stackrel { \cdot } { n } = 2 , 3 , \ldots .$ (The choice of ${ \pmb n } - 1$ instead of $\pmb { n } _ { \pmb { i } }$ , makes the subsequent notation simpler.） As is obvious from the expression preceding Exercise 1.5.54 $, S _ { n - 1 } ( x ) , n = 2 , 3 , \ldots .$ , is monic and has integer coefficients. The zeros of $\pmb { S _ { n - 1 } } ( \pmb { x } )$ are

$$
y _ { j } = 2 \eta _ { j } ^ { ( n ) } = e ^ { \pi i j / n } + e ^ { - \pi i j / n } , \qquad j = 1 , . . . , n - 1 ,
$$

so that

$$
S _ { n - 1 } ( x ) = ( x - y _ { 1 } ) \cdot \cdot \cdot ( x - y _ { n - 1 } ) ,
$$

and, as Schur [1,p. 425] remarks, we are dealing with $( 2 n ) \operatorname { t h }$ roots of unity. Suppose $\pmb { n } \geqslant 2 .$ Let $\pmb { h }$ be a divisor of $\mathbf { 2 n } .$ Put

$$
G _ { h } ( t ) = \prod _ { \stackrel { j = 1 } { ( j , 2 n ) = h } } ^ { n - 1 } ( t - y _ { j } ) .
$$

Keep in mind that the index $\pmb { n }$ is tacit in $G _ { h }$

We claim that $G _ { h } ( t )$ is monic, has integer coefficients and is irreducible over $\pmb { \mathbb { Q } }$ For, suppose $\pmb { h } = 1$ Put $m = 2 n$ Equation (5.16) yields

$$
x ^ { - \varphi ( m ) / 2 } \Phi _ { m } ( x ) = V _ { 1 } ( x + x ^ { - 1 } ) ,
$$

where we write $V _ { 1 }$ in place of $\pmb { q _ { m } }$ as an indication that $h = 1 .$ If $( j , 2 n ) = 1$ ， $j = 1 , . . . , n - 1$ then $e ^ { 2 \pi i j / 2 n }$ is a primitive $( 2 n ) \operatorname { t h }$ root of unity, hence a zero of $\Phi _ { m } ( x ) ,$ and so $V _ { 1 } ( y _ { j } ) = 0$ by (5.23). But $V _ { 1 }$ is of degree $\varphi ( m ) / 2$ and the number $\mathfrak { s f } j , j = 1 , . . . , n - 1 ;$ , which are relatively prime to $\pmb { m }$ is exactly $\varphi ( m ) / 2$ Hence $G _ { 1 } ( t ) = V _ { 1 } ( t ) .$ ，and since $V _ { 1 } ( t )$ is monic, has integer coefficients and is irreducible over $\pmb { \mathbb { Q } }$ the same is true of $G _ { 1 } ( t )$

Now, suppose $h > 1$ and $( j , 2 n ) = h , j = 1 ,$ ${ \pmb n } - 1$ (so that $1 < h \leqslant n - 1 \AA$ . Then $j = i h$ where

$$
\left( i , { \frac { 2 n } { h } } \right) = 1 , 1 \leqslant i \leqslant { \frac { n - 1 } { h } } ,
$$

and if (5.27) holds then $j = i h$ satisfies $( j , 2 n ) = h .$ . Thus if we put $m = 2 n / h ,$ (5.16) gives

$$
x ^ { - \varphi ( m ) / 2 } \Phi _ { m } ( x ) = V _ { h } ( x + x ^ { - 1 } )
$$

(we write $V _ { h }$ in place of $\pmb { q _ { m } } ,$ ，where $V _ { h }$ is monic, has integer coefficients, is irreducible over $\mathbb { Q }$ and of degree $\varphi ( m ) / 2 ,$ exactly the number of $j ,$ $1 \leqslant j \leqslant n - 1$ ，such that $( j , 2 n ) = h .$ ，Thus,as in the case $\pmb { h } = 1$ we obtain $G _ { h } ( t ) = V _ { h } ( t )$ is monic, has integer coefficients and is irreducible over $\mathbb { Q }$

Since for every $j , j = 1 , \ldots , n - 1$ there exists an h $, 1 \leqslant h \leqslant n - 1$ which divides $_ { 2 n }$ such that $( j , 2 n ) = h$ and every $\pmb { h }$ which divides $2 n , 1 \leqslant h \leqslant n - 1$ satisfies $( j , 2 n ) = h$ for some $j , \ j = 1 , \ \ldots , \ n - 1$ we obtain the desired factorization.

$$
S _ { n - 1 } ( t ) = \prod _ { \substack { h / 2 n } } G _ { h } ( t )
$$

# EXERCISES 5.2.26-5.2.29

5.2.26. According to Remark 2 following Theorem 5.5, if $\pmb { n } = \pmb { p }$ , an odd prime, then $C _ { n } ( { \boldsymbol { x } } ) = { \boldsymbol { x } } F _ { 1 } ( { \boldsymbol { x } } ) .$ .Show that

$$
{ \frac { C _ { p } ( x ) } { x } } = F _ { 1 } ( x ) = ( - 1 ) ^ { ( p - 1 ) / 2 } \sum _ { j = 0 } ^ { ( p - 1 ) / 2 } ( - 1 ) ^ { j } C _ { 2 j } ( x ) .
$$

5.2.27. If $\pmb { p }$ is an odd prime and $\pmb { n } = 2 ^ { k } \pmb { p }$ then $C _ { n } ( x ) = C _ { 2 ^ { k } } ( x ) F _ { 1 } ( x )$ .When $k = 1$ , so that $\pmb { n } = 2 \pmb { p }$

$$
C _ { 2 p } ( x ) = C _ { 2 } ( x ) \sum _ { j = 0 } ^ { ( p - 1 ) / 2 } ( - 1 ) ^ { ( p - 1 ) / 2 - j } C _ { 4 j } ( x ) .
$$

5.2.28. If $\pmb { p }$ is an odd prime and $S _ { p - 1 } ( x ) = G _ { 1 } ( x ) G _ { 2 } ( x ) ,$ show that

$$
G _ { 2 } ^ { 2 } ( x ) = \frac { C _ { p } ( x ) - 2 } { x - 2 } , ~ \mathrm { a n d }
$$

$$
G _ { 1 } ( x ) = ( - 1 ) ^ { ( p - 1 ) / 2 } G _ { 2 } ( - x ) .
$$

Hint. (i) Both sides have exactly the same zeros.

(ii) The zeros of ${ \pmb G _ { 1 } }$ are the negatives of the zeros of $\pmb { G } _ { 2 }$

5.2.29. If $\pmb { p }$ is an odd prime and $S _ { p - 1 } ( x ) = G _ { 1 } ( x ) G _ { 2 } ( x )$ then

$$
{ \cal G } _ { 1 } ( x ) = S _ { ( p - 1 ) / 2 } ( x ) - S _ { ( p - 3 ) / 2 } ( x ) , \qquad { \cal G } _ { 2 } ( x ) = S _ { ( p - 1 ) / 2 } ( x ) + S _ { ( p - 3 ) / 2 } ( x ) .
$$

Hint. $G _ { 2 } ( x ) = 1 + C _ { 1 } ( x ) + \cdots + C _ { ( p - 1 ) / 2 } ( x ) = S _ { ( p - 1 ) / 2 } ( x ) + S _ { ( p - 3 ) / 2 } ( x ) ;$ The first equality is a consequence of Exercise 5.2.28(i) and the second follows from Exercise 1.2.13b.

With hindsight we now see that the explicit complete factorization of $\pmb { S } _ { p - 1 } ( \pmb { x } )$ is easy. For,

$$
S _ { p - 1 } ( x ) = ( S _ { ( p - 1 ) / 2 } ( x ) - S _ { ( p - 3 ) / 2 } ( x ) ) ( S _ { ( p - 1 ) / 2 } ( x ) + S _ { ( p - 3 ) / 2 } ( x ) )
$$

and the zeros of the factors are exactly the zeros of ${ \pmb G } _ { 1 }$ and $\pmb { G } _ { 2 }$ , respectively.

# 5.3. Some Number Theoretic Properties of the Chebyshev Polynomials

The paper of Schur [1] which motivated the preceding section contains a wealth of material about number theoretic properties of the Chebyshev polynomials (see also Bang [1] and Rankin [1]). We are going to conclude by presenting only a few of the most elementary results to be found there, chosen because they make minimal demands on previous knowledge of number theory beyond material presented in Section 5.2. In this section we will adopt Schur's notation and put

$$
\mathcal { U } _ { n } ( x ) \equiv U _ { n - 1 } ( x ) , \qquad n = 0 , 1 , 2 , \ldots .
$$

Thus $\mathcal { U } _ { 0 } ( x ) = 0 , \mathcal { U } _ { 1 } ( x ) = 1 , \mathcal { U } _ { 2 } ( x ) = 2 x ,$ .... Keep in mind that now

$$
\mathcal { U } _ { n } ( \cos \theta ) = \frac { \sin n \theta } { \sin \theta } , \qquad n = 0 , 1 , 2 , . . . ,
$$

and $\begin{array} { r } { \mathcal { U } _ { n } ( - x ) = - \mathcal { U } _ { n } ( x ) . } \end{array}$

# 1. Pell's Equation. The Diophantine equation

$$
\ x ^ { 2 } - D y ^ { 2 } = 1
$$

is called Pells equation. Given an integer $\pmb { D }$ we seek integers $\pmb { x }$ and $\boldsymbol { y }$ which satisfy (5.30). We restrict our attention to $\boldsymbol { x } , \boldsymbol { y } , D$ positive. Indeed, we shall also assume that $\pmb { D }$ is not a square, for if $D = a ^ { 2 }$ then $x ^ { 2 } = ( a y ) ^ { 2 } + 1$ is impossible. Any $( x , y )$ satisfying (5.30) is calld a solution of (5.30).

It is a fact (cf. Hua [1]) that, under our assumption, there always exists a solution to (5.30), and hence a solution for which $\pmb { x }$ is least, say $( x _ { 1 } , y _ { 1 } )$ .Note that $\mathbf { \delta x _ { 1 } } > 1 .$ Consider the identity (Exercise 1.2.15(i))

$$
T _ { n } ^ { 2 } ( x ) - ( x ^ { 2 } - 1 ) \mathcal { U } _ { n } ^ { 2 } ( x ) = 1 .
$$

Then

$$
\begin{array} { l } { 1 = T _ { n } ^ { 2 } ( x _ { 1 } ) - ( x _ { 1 } ^ { 2 } - 1 ) \mathcal { U } _ { n } ^ { 2 } ( x _ { 1 } ) } \\ { \quad \ = \ T _ { n } ^ { 2 } ( x _ { 1 } ) - \frac { x _ { 1 } ^ { 2 } - 1 } { y _ { 1 } ^ { 2 } } ( y _ { 1 } ^ { 2 } \mathcal { U } _ { n } ^ { 2 } ( x _ { 1 } ) . } \end{array}
$$

Since

$$
\frac { x _ { 1 } ^ { 2 } - 1 } { y _ { 1 } ^ { 2 } } = D ,
$$

by definition, we conclude that for each $\pmb { n } \in \mathbb { N }$

$$
( T _ { n } ( \mathbf { x _ { 1 } } ) , y _ { 1 } \mathbf { \mathcal { U } } _ { n } ( \mathbf { x _ { 1 } } ) )
$$

is a solution of(5.30). Thus Pell's equation has infinitely many solutions. It is not difficult to show that al positive solutions of(5.30),for a nonsquare $\pmb { D }$ ,are given by (5.31) (cf. Hua [1]).

2. Fermat's Theorem for the Chebyshev Polynomials. We show that an analog of (5.8) (Fermat's Theorem) holds for the Chebyshev polynomials. Namely, if $\boldsymbol { x } \in \mathbb { N }$ and $\pmb { p }$ is an odd prime

$$
T _ { p } ( x ) \equiv T _ { 1 } ( x ) ( { \bf m o d } p ) ,
$$

If we put $2 m + 1 = p$ in Exercise 1.2.1, we obtain

$$
T _ { p } ( x ) = \sum _ { j = 0 } ^ { m } \binom { p } { 2 j } x ^ { p - 2 j } ( x ^ { 2 } - 1 ) ^ { j } .
$$

Since $\pmb { p } \bigg / \binom { p } { j } , j = 1 , . . . , m$

$$
T _ { p } ( x ) \equiv x ^ { p } ( { \bf m o d } p ) ,
$$

and (5.32) follows from (5.8).

3. $( \mathcal { U } _ { n } ( x ) , \mathcal { U } _ { m } ( x ) ) = \mathcal { U } _ { ( m , n ) } ( x )$ 。We wish to establish the equality

$$
( \mathcal { U } _ { n } ( x ) , \mathcal { U } _ { m } ( x ) ) = \mathcal { U } _ { ( m , n ) } ( x )
$$

for $\boldsymbol x \in \mathbb { N }$ amd $n > m > 1$ For example, $\begin{array} { r } { \mathcal { U } _ { m } ( 1 ) = m , ~ \mathcal { U } _ { n } ( 1 ) = n , } \end{array}$ and $\mathcal { U } _ { ( m , n ) } ( 1 ) = ( m , n ) .$ ，so (5.33) holds for ${ \boldsymbol x } = 1$ .The proof of the general case requires some simple identites.

Since $\mathcal { U } _ { k } ( \cos \theta ) = ( \sin k \theta ) / \sin \theta$ it is easy to see that

$$
\begin{array} { r } { \mathcal { U } _ { j k } ( x ) = \mathcal { U } _ { j } ( T _ { k } ( x ) ) \mathcal { U } _ { k } ( x ) , } \end{array}
$$

and if $k > j > 1$

$$
\mathscr { U } _ { k - j } ( x ) = \mathscr { U } _ { k } ( x ) \mathscr { U } _ { j + 1 } ( x ) - \mathscr { U } _ { k + 1 } ( x ) \mathscr { U } _ { j } ( x ) ,
$$

a paraphrase of an easily established trigonometric identity.

Let $\pmb { \mathcal { U } } _ { \mathbf { k } }$ denote ${ \pmb \mathcal { U } } _ { { \pmb { k } } } ( { \pmb x } )$ for a given ${ \boldsymbol { x } } \in  { \mathbb { N } }$ Suppose $( n , m ) = d , \ n = n _ { 1 } d ,$ $m = m _ { 1 } d ,$ then in view of (5.34),

$$
\mathcal { U } _ { n } = \mathcal { U } _ { n _ { 1 } d } = \mathcal { U } _ { n _ { 1 } } ( T _ { d } ) ( \mathcal { U } _ { d } )
$$

yields ${ \pmb q } _ { \pmb d } / \sigma _ { \pmb u } ^ { \prime }$ ,and similarly, ${ \pmb u } _ { { \pmb d } } / { \pmb u } _ { m }$ . Thus $\mathcal { U } _ { d } / D$ ，where $\pmb { { \cal D } } = ( \mathcal { U } _ { n } , \mathcal { U } _ { m } )$ .Now it suffices to show that $\pmb { D } / \pmb { \mathcal { U } _ { d } }$ to establish (5.33).

A simple consequence of the Euclidean algorithm applied to $\pmb { n }$ and $\pmb { m }$ is $d = s n + t m , s , t \in \mathbb { Z } , s t \neq 0$ (cf. Hua [1]), and with no loss of generality we may assume that

$$
d = a n - b m , \qquad a , b \in \mathbb { N } .
$$

But (5.35) with $k = a n$ ， $j = b m$ yields

$$
\mathcal { U } _ { d } = \mathcal { U } _ { a n - b m } = \mathcal { U } _ { a n } \mathcal { U } _ { b m + 1 } - \mathcal { U } _ { a n + 1 } \mathcal { U } _ { b m } ,
$$

and in view of (5.34) we have

$$
\mathcal { U } _ { a n } = \mathcal { U } _ { a } ( T _ { n } ) \mathcal { U } _ { n } , \qquad \mathcal { U } _ { b m } = \mathcal { U } _ { b } ( T _ { m } ) ( \mathcal { U } _ { m } ) .
$$

Equation (5.37) implies that $\pmb { D } / \pmb { \mathcal { U } } _ { \pmb { a n } }$ and $\pmb { D } / \mathcal { U } _ { \pmb { b m } }$ ,and hence we conclude from (5.36) that $\pmb { D } / \pmb { \mathcal { U } } _ { d }$ , the required result.

Remark 1. We have also proved (5.33) for the polynomials $\mathcal { U } _ { n } , \mathcal { U } _ { m }$

Remark 2. A result of a similar flavor for the Fibonacci numbers, due to Lucas, is given in Knuth [1].

# REFERENCES

# Achieser, N. I.

1. Theory of Approximation, Ungar, New York,1956.

Adler, R. $\mathbf { L } _ { \mathbf { \nabla } }$ and T. J. Rivlin

1. Ergodic and mixing properties of Chebyshev polynomials,Proc.Amer. Math. Soc.,15 (1964), 794-796.

Anderssen, R. S. and G. H. Golub

1. Richardson's non-stationary matrix iterative procedure, Rep. STAN-CS-72-304, Computer Science Department, Stanford University, 1972.

# Askey, R.

1. Jacobi polynomial expansions with positive coefficients and imbeddings of projective spaces, Bull. Amer. Math. Soc.,74 (1968),301-304.   
2. Mean convergence oforthogonal series and Lagrange interpolation, Acta Math. Acad. Sci. Hungar.,23 (1972),71-85.   
3. A sine inequality,Problem 73-21, SIAM Rev.,15 (1973),788.

Askey, R., and G. Gasper, L. A. Harris

1. An inequality for Tchebycheff polynomials and extensions, J. Approximation Theory, 14 (1975), 1-11.

Askey, $\mathbf { R _ { \Rightarrow } }$ and J. Steinig

1. Some positive trigonometric sums, Trans. Amer. Math. Soc., 187 (1974), 295-307.

Bak, $\mathbf { J } _ { \mathbf { \hat { \Pi } } }$ and D. J. Newman

1. Complex Analysis,Springer-Verlag,New York,1982.

Bang, T.

1. Congruence properties of the Tchebycheff Polynomials, Math. Scand.,2 (1954), 327- 333.

Berman, D. L.

1. Solution of an extremal problem in the theory of interpolation (Russian), Dokl. Akad. Nauk SSSR,87 (1952),167-170.

# Bernstein, S. N.

1. Sur la meilleure approximation de $| { \pmb x } |$ par des polynomes de degrés donnes, Acta Math.,37 (1913), 1-57.   
2.Lecons sur les Proprietés Extrémales et la Meilleure Approximation des Fonctions Analytiquesd'une VariableReelle,Gauthier-Villars,Paris,1926.   
3. On a theorem of V.A. Markov (Russian), Trudy Leningrad Indust. Inst., No.5, Phys.- math. Sci.Section, No.1(1938), 8-13. (Also in Vol.II of The Collected Works of S. N. Bernstein,Akad.Nauk SSSR,Moscow,1954).   
4. Sur la limitation des valeurs d'une polynome $P ( x )$ de degré n sur tout un segment par ses valeurs en $( n + 1 )$ points du segment, Izv. Akad. Nauk SSSR,7(1031), 1025-1050.

# Bertram, E. A.

1.Polynomials which commute with a Tchebycheff polynomial, Amer. Math.Monthly, 78 (1971), 650-653.

Block, H. D., and H. P. Thielman

1.Commutative polynomials, Quart.J. Math. Oxford Ser. (2),2 (1951),241-24.

Boas, R. P., Jr.

1.Inequalities for the derivatives of polynomials,Math. Mag., 42 (1969),165-174.

Bojanov, B. D.

1.An extension of the Markov inequality,J.Approximation Theory,35 (1982),181-190. 2.Proof of a conjecture of Erdos about the longest polynomial, Proc.A.M.S.,84 (1982), 99-103. Also Proc. A.M.S., 89 (1983), 188.

# de Boor, C., and A. Pinkus

1.Proof of the conjectures of Bernstein and Erdos concerning the optimal nodes for polynomial interpolation,J. Approximation Theory,24 (1978),289-303.

de Boor, C., and J. Rice

1. Extremal polynomials with application to Richardson iteration for indefinite linear systems, SIAM J. Sci. Stat. Comput.,3 (1982), 47-57.

# de Bruijn, N. G.,

1. Inequalities concerning polynomials in the complex domain, Nedere. Akad. Wetensch. Indag.Math.,IX (1947), 591-598.

# Brutman, L.

1. On the Lebesgue function for polynomial interpolation, SIAM J. of Numer. Anal., 15 (1978), 694-704.

Carlson, B. C., and J. Todd

1. Zolotarev's first problem-the best approximation by polynomials of degree ≤n - 2 to $\pmb { x } ^ { n } - n \sigma \pmb { x } ^ { n - 1 }$ in [-1,1], Aequationes Math.,26 (1983), 1-33.

Cavaretta, A. S., Jr.

1. An elementary proof of Kolmogorov's theorem, Amer. Math. Monthly,81 (1974), 480- 486.

Cline, A. K.

1. Lipschitz conditions on uniform approximation operators, J. Approximation Theory, 8 (1973), 160-172.

van der Corput, J. G., and G. Schaake

1. I. Ungleichungen fur Polynome und trigonometrische Polynome, Compositio Math.2 (1935), 321-361. Correction ibid., 3 (1936), 128.

# De Vore, R. A.

1. A property of Chebyshev polynomials, J. Approximation Theory,12 (1974), 418-419.

Duffin, R. J. and A. C. Schaeffer

1. A refinement of an inequality of the brothers Markoff, Trans. Amer. Math. Soc. 50 (1941), 517-528.

Ehlich, H., and K. Zeller

1. Schwankung von Polynomen zwischen Gitterpunkten, Math. Z., 86 (1964), 41-44. 2. Auswertung der Normen von Interpolationsoperatoren, Math. Ann.,164 (1966),105- 112. 3.Cebysev-Polynome in mehreren Veränderlichen, Math. Z., 93 (1966),142-143.

# Erdos, P.

1.Problems and results on the theory of interpolation,I, Acta. Math. Acad.Sci. Hungar., 9 (1958), 381-388.

2. Some remarks on polynomials, Bull. Amer. Math. Soc.,53 (1947),1169-1176.

3.An extremum-problem concerning trigonometric polynomials, Acta Sci. Math. Szeged, 9 (1939), 113-115.

Erdos, P., and G. Grinwald

1. Note on an elementary problem of interpolation,Bull Amer. Math. Soc.,44 (1938), 515-518.

Faber, G.

1. Uber die interpolatorische Darstellung stetiger Funktionen, Jber. Deutsch. Math.- Verein.,23 (1914), 192-210.

# Fejer, L.

1. Uber Interpolation, Gott. Nachr. (1916), 66-91.

2. Die Abschätzung eines Polynoms in einem Intervalle, wenn Schranken fur seine Werte und ersten Ableitungswerte in einzelnen Punkten des Intervalles gegeben sind, und ihre Anwendung auf die Konvergenzfrage Hermitescher Interpolationsreihen, Math. Z., 32 (1930), 426-457.

3.Bestimmung derjenigen Abszissen eines Intervalles,fur welche die Quadratsumme der Grundfunktionen der Lagrangeschen Interpolation im Intervalle ein moglichst kleines Maximum besitzt, Ann. Scuola, Norm. Sup. Pisa,1 (1932), 263-276.

4.Mechanische Quadraturen mit positiven Cotesschen Zahlen, Math.Z.,37(1933),287- 309.

# Feldheim, E.

1. Sur l'orthogonalite des fonctions fondamentales et sur la forte convergence en moyenne des polynomes d'interpolation de Lagrange dans le cas des abscisses de Tchebychef, Bull. Soc.Math.France, 65 (1937),1-40.

Fischer, B., and R. Freund

1. On the constrained Chebyshev approximation problem on ellipses, J. Approximation Theory, to appear.

Fox, L., and I. B. Parker

1. Chebyshev Polynomials in Numerical Analysis,Oxford University Press,London,1968.

# Freud, G.

1.Eine Ungleichung fur Tschebysheffsche Approximationspolynome,Acta Sci.Math. (Szeged),19 (1958), 162-164.   
2.Orthogonal Polynomials,Akadémiai Kiadó,Budapest,1971.

# Freund, R.

1. On some approximation problems for complex polynomials, Constr. Approx.,4(1988), 111-121.

Freund, R., and S. Ruscheweyh

1. On a class of Chebyshev approximation problems which arise in connection with a conjugate gradient type method, Numer. Math., 48 (1986), 522-542.

# Friedman, S. L.

1. Chebyshev constant and Chebyshev points, Trans. Amer. Math. Soc.,186 (1973),129- 139.

von Golitschek, $\mathbf { M _ { \eta } }$ and G. G. Lorentz

1. Bernstein inequalities in $L _ { p }$ ， $0 \leqslant p \leqslant + \infty$ ,Rocky Mountain Journal,19 (1989),145- 156.

Golub, G. $\mathbf { H } _ { \mathbf { \eta } }$ and C. F. Van Loan

1. Matrix Computations, Johns Hopkins University Press, Baltimore,1983.

Halmos, P. R.

1. Measure Theory,Van Nostrand,New York,1950.

Haussmann, W., and K. Zeller

1. Approximate Zolotarev polynomials, Comp. & Maths. with Appls.,12B (1986), 1133- 1140.

Hille, E.

1. Topics in classical analysis,Lectures on Modern Mathematics,Vol.II,T.L.Saaty,Ed. Wiley,New York,1965.

# Hsiao, H. J.

1. On factorization of Tchebyschef's Polynomials of the frst kind, Bull. Inst.Math. Acad. Sinica,12 (1954), 89-94.

Hua, L. K.

1. Introduction to Number Theory, Springer,Berlin,1982.

# Jacobsthal, E.

1. Uber vertauschbare Polynome, Math. Z., 63 (1955), 243-276.

John, F.

1. Lectures on Advanced Numerical Analysis,Gordon and Breach,New York,1967.

Johnson, L. W., and R. D. Riess

1. Convergence of polynomials interpolating at the zeros of $T _ { n } ( x ) ,$ Math. Z., 116 (1970), 355-358.

Julia, G.

1. Mémoire sur la permutabilité des fractions rationnelles,Ann.Sci. Ecole Norm. Sup, 39 (1922), 131-215.

Karlin, S., and W. J. Studden

1.Tchebycheff Systems:With Applications in Analysis and Statistics,Wiley,New York, 1966.

Kemperman, J. H. B.

1. Markov type inequalities for the derivatives of a polynomial, Aspects of Mathematics and its Applications,Ed.J.A.Barroso,Elsevier,1986,pp.465-476.

Kilgore, T. A.

1. A characterization of the Lagrange interpolating projection with minimal Tchebycheff norm, J. Approximation Theory,24 (1978),273-288.

# Kimberling, C.

1. Generalized cyclotomic polynomials,Fibonacci-cyclotomic polynomials,and Lucascyclotomic polynomials, The Fibonacci Quarterly,18 (1980),108-126.

# Knopp, K.

1. Theory and Application of Infinite Series,Hafner,New York,1949.

Knuth, D. E.

1. The Art of Computer Programming,Vol.1,Fundamental Algorithms,Addison-Wesley, Reading,Mass.,1968.

Korsak, A., and C. Schubert

1. A determinant expression of Tchebyshev polynomials, Canad. Math. Bull,3 (1960), 243-246.

# Kristiansen, G. K.

1. Some inequalities for algebraic and trigonometric polynomials,J. London Math. Soc. (2),20 (1979),300-314.

Kroo, A., and E. B. Saff

1.On polynomials of minimal $L _ { q }$ deviation, $0 < q < 1$ ,J.London Math. Soc. (2),37 (1988), 182-192.

# Lanczos, C.

1．Applied Analysis,Prentice Hall,Englewood Cliffs,N.J.,1956.

de La Vallee Poussin, C. J.

1. Lecons sur PApproximation des Fonctions dune Variable Reele,Gauthier-Villrs,Paris, 1952.

Lax, P. D.

1. Proof of a conjecture of P.Erdos on the derivative of a polynomial, Bull. Am. Math. Soc.,50 (1944), 509-513.

# Lepson, B.

1. Upper bounds for Dirichlet kernels and Tchebycheff polynomials of the second kind, J. Math. Anal. Appl., 48 (1974),139-149.

Malik, M. A.

1. On the derivative of a polynomial, J.London Math. Soc.(2),1 (1969), 57-60.

# Marchuk, G. I.

1.Methods of Numerical Mathematics,2nd ed.,Springer,New York,1982.

Markov, V. A. (W. Markof)

1.Uber Polynome,die in einem gegeben Intervalle möglichst wenig von Null abweichen, Math. Ann., 77 (1916),213-258.

# Matorin, A. P.

1. On inequalities between the maxima of the absolute values of a function and its derivatives on a half-line,Amer.Math. Soc.Transl., Series 2,8 (1958),13-17.

# Mohr, E.

1. Elementarer Beweis einer Ungleichung von W. A. Markoff, Tensor (N.S.),14 (1963), 71-85.

# Mysovskikh, I. P.

1. Quadrature formulae of the highest trigonometric degree of accuracy， U.S.S.R. Comput.Maths.Math.Phys.,25 (1985),180-184.

# Natanson, I. P.

1.Constructive Function Theory,Vols.I,I,II,Ungar,New York: I,964; II,196;II, 1965.

Newman D. J., and H. S. Shapiro

1. Some theorems on Cebysev approximations, Duke Math. J.,30 (1963), 673-682.

Opfer, G., and G. Schober

1.Richardson's iteration for nonsymmetric matrices,Linear Algebra Appl.,58 (1984), 343-361.

Ortiz, E. L. and T. J. Rivlin

1.Another look at the Chebyshev polynomials, Amer. Math. Monthly,90 (1983), 3-10.

# Paszkowski, S.

1. The theory of uniform approximation: I. Non-asymptotic theoretical problems, Rozprawy Matematyczne, XXVI,1962,Panstwowe Wydawnictwo Naukowe, Warsaw.

# Pierre, $\mathbf { R _ { \eta } }$ and Q. I. Rahman

1. On polynomials with curved majorants, Studies in Pure Mathematics: To the Memory of Paul Turan,Ed.P.Erdos,Birkhäuser,Basel,1983,543-549.

Pollard, $\mathbf { H } _ { \mathfrak { s } }$ and H. G. Diamond

1. The Theoryof Algebraic Numbers, Mathematical Asociation ofAmerica, Washington, 1975.

# Rahman, Q. I.

1. On a problem of Turan about polynomials with curved majorants, Trans. Amer. Math. Soc., 163 (1972), 447-455.

2. Addendum to: On a problem of Turan about polynomials with curved majorants, Trans. Amer. Math. Soc.,168 (1972), 517-518.

Rahman, Q. I, and G. Schmeisser

1. Les Inegalités de Markof et de Bernstein, Les Presses de I'Université de Montreal, Montreal, 1983.

Rainville, E. D.

1. Special Functions,Macmillan,New York,1960.

# Rankin, R. A

1. Chebyshev polynomials and the modulary group of level p,Math. Scand.,2 (1954), 315-326.

# Reimer, M.

1. Bounds for the Horner sums, SIAM J. Numer. Anal.,5 (1968), 461-469.

# Riesz, M.

1.Eine trigonometrische Interpolationsformel und einige Ungleichungen fur Polynome, Jber.Deutsch.Math.-Verein.,23 (1914), 354-368.

Ritt, J. F.

1. Permutable rational functions, Trans. Amer. Math. Soc.,25 (1923),399-448.

# Rivlin, T. J.

1. An Introduction to the Approximation of Functions,Dover,New York,1981. 2. The strong uniqueness constant in complex approximation, Lecture Notes in Mathematics,1105, Springer, Berlin,1984,145-149.

Rivlin, T. J.,and H. S.Shapiro

1. A unified approach to certain problems of approximation and minimization,J. Soc. Indust. Appl. Math.,9 (1961), 670-699.

Rivlin, T. J., and M. W. Wilson

1. An optimal property of Chebyshev expansions, J. Approximation Theory,2 (1969), 312-317.

Rogosinski, W. W.

1.Some elementary inequalities for polynomials, Math. Gaz., 39 (1955), 7-12.

# Rudin, W.

1. Some theorems on Fourier coeffcients,Proc.Amer. Math. Soc.,10 (1959), 855-859.

# Schur, I.

1.Arithmetisches üiberdie Tschebyscheffschen Polynome,Gesammelte Abhandlungen,II, Springer,Berlin,1973,422-453. 2.Zur Irreduzibilitat der Kreisteilungsgleichung,Math.Zeit.,29 (1928),463.

# Shapiro, H. S.

1.Extremal Problems for Polynomials and Power Series,Master's thesis,MIT,1951. 2.Topics in Approximation Theory,Lecture Notes in Mathematics,187,Springer,New York, 1971.

# Szego, G.

1. Orthogonal Polynomials,American Mathematical Society,Fourth Ed.,Providence,RI, 1975.

2.Uber einen Satz des Herrn Serge Bernstein, Schriften der Konigsberger Gelehrten Gesellschaft,Naturw.Klasse,5(1928), 59-70. Reprinted in: Gabor Szego:Collected Papers,Vol 2,Birkhäuser,Boston,1982,207-219 (including an interesting added survey of subsequent developments).

3.Bemerkungen zu einem Satz von J.H.Grace über die Wurzeln algebraischen Gleichungen, Math. Zeitschr.,13 (1922),28-55. (or: Gabor Szego: Collected Papers, Vol.1,Ed.R.Askey,Birkhäuser,Boston,1982,505-534.)

4. Inequalities for the zeros of Legendre polynomials and related functions, Trans. Amer. Math. Soc., 39 (1936),1-17. Reprinted in: Gabor Szego: Collected Papers,Vol.2, Birkhäuser, Boston, 1982, 593-609.

# Tchakaloff, V.

1. Formules de cubatures mécaniques a coefficients non négatifs, Bull Sci. Math. 2,81 (1957), 123-134.

# Tchebychef, P. L.

1. Oeuvres,2 vols., Chelsea, New York,1962.

# Titchmarsh, E. C.

1.The Theory of Functions,2nd ed., Oxford University Press,London, 1939.

# REFERENCES

# Turan, P.

1. On an inequality of Cebysev,Ann. Univ.Sci. Budapest,Eotvos Sect.Math.,11(1968), 15-16.

Varga, R. S., and A. J. Carpenter

1. On the Bernstein conjecture in Approximation theory, Constr. Approx.,1(1985), 333- 348.

# Voronovskaja, E. V.

1.The Functional Method and its Applications,Translations of Mathematical Monographs,Vol. 28,American Mathematical Society,Providence,R.I.,1970.

# van der Waerden, B. L.

1. Modern Algebra, Volume I,Ungar,New York,1953.

# Zygmund, A.

1. Trigonometric Series,Vols.I and II, Cambridge University Press,London,1959.   
2.A remark on conjugate series,Proc.London Math.Society,(2),34 (1932),392-40C

# GLOSSARY OF SYMBOLS

$B _ { n }$ Unit ball in ${ \mathcal { P } } _ { \pmb { n } }$ 107   
$c _ { n }$ Convex subset of ${ \mathcal { P } } _ { n }$ 107   
$C _ { n } ( { \pmb x } )$ $2 T _ { n } ( x / 2 )$ 60   
$\pmb { { \cal E } }$ Array of nodes consisting of equally spaced points of I. 26   
$E ( g ; B )$ Subset of $\pmb { B }$ on which $| g | = \| g \|$ 72   
$E _ { k } ( f )$ Error of best approximation by polynomials of degree   
at most $\pmb { k }$ 12   
$\eta _ { j } , \eta _ { j } ^ { ( n ) }$ Extrema of the Chebyshev polynomial of degree n 7   
${ \pmb F } _ { \pmb n }$ Fibonacci number 61   
2\* Best strong uniqueness constant. 80   
hj(x) Fundamental polynomials of the first kind for Hermite   
interpolation 28   
j(x) Fundamental polynomials of the second kind for   
Hermite interpolation 28   
1 The interval [-1,1]. 2   
$l _ { j , n } ( x )$ Fundamental polynomials for interpolation 11   
$L _ { k } ( f , X ; x )$ Interpolating polynomial of degree $\pmb { k }$ to $f$ at the points   
of the $( k - 1 ) { \mathsf { s t } }$ row of $\pmb { X }$ ,evaluated at $\pmb { x }$ 12   
$L _ { ☉ }$ Lucas number 62   
$\lambda _ { k } ( X ; x )$ Lebesgue function of polynomial interpolation theory 13   
$\pmb { \Lambda } _ { \pmb { k } } ( \pmb { X } )$ Lebesgue constant of polynomial interpolation theory 13   
${ \pmb \omega } ( { \pmb x } )$ Polynomial with zeros at nodes 14   
$\mathcal { P } _ { \pmb { \mathscr { n } } }$ The set of polynomials of degree at most n 1   
$\varphi _ { j } , \varphi _ { j } ^ { ( n ) }$ Extrema of cos n0 6   
$\mathbb { R } ^ { n }$ Real $\pmb { n }$ -space 68   
${ \pmb S } _ { \pmb { n } } ( { \pmb x } )$ $U _ { \pmb { n } } ( \pmb { x } / 2 )$ 60   
s The convex hull of S 69   
Partial sum of the coefficients of $\pmb { T _ { n } } ( \pmb { x } )$ 9   
$\mathcal { S } _ { \star } ( z )$ The Shapiro polynomial of degree $\pmb { k } .$ 162   
$\pmb { \sigma }$ The domain or base of a signature 74   
$\pmb { \Sigma }$ Signature 74   
$\Sigma ^ { \prime }$ Sum with the frst term halved 40   
$\Sigma ^ { \prime \prime }$ Trapezoidal sum 38   
$_ T$ Array of nodes consisting of the zeros of the   
Chebyshev polynomial 14   
$t _ { j } ^ { ( n ) } , t _ { j }$ Coefficient of the Chebyshev polynomial of degree n 4   
$\pmb { T _ { n } } ( \pmb { x } )$ Chebyshev polynomial of degree n 1   
$\widetilde { T } _ { n } ( x )$ Chebyshev polynomial of degree n normalized so that   
its leading coeffcient is 1 6   
$\mathcal { T } _ { \pmb { n } }$ The set of trigonometric polynomials of degree at   
most n 15   
$\theta _ { j } , \theta _ { j } ^ { ( n ) }$ The zeros of cos nθ 6   
$\pmb { U }$ Array of nodes consisting of the extrema of the   
Chebyshev polynomials 24   
$U _ { \pmb { n } } ( \pmb { x } )$ Chebyshev polynomial of the second kind 7   
$\textstyle { \mathcal { U } } _ { n } ( x )$ Notation for $U _ { n - 1 } ( x )$ 231   
$\xi _ { j } ,$ The zeros of the Chebyshev polynomial of degree n 6   
$\| \cdot \|$ The uniform norm 10

# INDEX

Achieser, N. I., 95   
Adler, R.L., 205   
Algebraic:   
integer,221   
number, 221   
Anderssen,R.S.,151,153   
Askey,R.,53,60,139,161,190   
Bak, J.,42   
Bang,T.,231   
Berman,D.L.,138   
Bernstein, S.N.,22,23,123,179,180   
inequality,119,141,142,146,147   
Bertram,E.A.,193   
Best approximation, 74   
characterization of,74-76   
existence of, 77   
on finite set,85,91-93   
strong uniqueness of,80   
uniqueness of,78   
Block, H. D., 196   
Boas,R.P.,Jr.,123,130   
Bojanov,B.D.,149,151   
Brutman,L., 23

Caratheodory's theorem, 69,74   
Carlson, B. C., 95   
Carpenter, A.J.,180   
Cavaretta, A. S.,Jr.,140   
Chebyshev,P.L.,5 coefficients,evaluating,180 condition,78,84 differential equation,87 expansion, 164 optimal property,188 form,155 iteration, 151 polynomial, 4 best strong uniqueness constant,81

coefficients, 4,37 discriminant of,217,219 generating function,41 orthogonality, 34 renormalized, 60 of second kind,7 stylized,213 Christoffel-Darboux formula, 40 Cline, A. K., 83 Convex hull, 69 Convex set, 68 Critical point, 72

de Boor,C.,23,27,153   
de Bruijn, N. G.,142,143   
de La Vallee Poussin, C.J., 169   
means of, 169   
De Vore,R., 109   
Diamond,H.G.,221   
Dini-Lipschitz test,168   
Divided difference,24   
Duffin,R.J.,38,123,136   
Duffin and Schaeffer theorem,136

Economization, 156   
Ehlich,H.,15,26,77,140   
Enestrom-Kakeya theorem,159   
Erdos,P.,22,23,58,63-65,144,149-151   
Ergodic transformation,201   
Extremal signature,74 primitive,75-77 weights for, 75   
Extreme point,107

Faber, G., 14   
Fejer,L.,31,33,52,56   
means, 169   
Fekete points,220   
Feldheim,E.,53,56   
Fermat's theorem,221,232   
Fibonacci numbers,61-63,233   
Binet's formula,61,62   
Fischer,B.,154   
Fox,L.,157   
Freud,G.,84,149   
Freund, R., 154   
Friedman, S., 90   
Gasper, G., 60   
Gauss-Chebyshev quadrature formula, 45   
Gauss-Lucas theorem,132,141   
Gauss quadrature formula,45,101   
Gauss'theorem,222   
Generating function of Chebyshev poly  
nomial, 41   
Golub,G.H.,151,153   
Grunwald,G., 58   
Haar theorem,78   
Halmos,P., 201   
Harris,L.A., 60   
Haussmann,W.,95   
Hermite interpolation,29,31,33   
Hille,E.,90,220   
Hsiao,H.J., 227   
Hua,L.K.,231-233   
Jackson's theorem,167   
Jacobsthal,E.,196   
Jia, R.-Q., 27   
John,F., 152   
Johnson, L. W.,168   
Julia,G., 197   
Karlin, S., 78   
Kemperman,J.H. B., 65   
Kilgore,T.,23   
Kimberling,C., 227   
Knopp,K., 21   
Knuth,D.E.,61,233   
Kolmogorov criterion,76   
Korsak, A., 58   
Kristiansen, G.K.,151   
Kr06, A., 120   
Lanczos,C., 115,156   
Lax, P. D., 144   
Least squares,42   
Lebesgue constant,13,19,22,23,26,27,   
138,167   
Lebesgue function,13   
Lepson, B., 139   
Linear equations, solution of,151

Linear functional, 97 canonical representation of,99-107 extremal for, 98   
interpolation formula for, 98   
norm of, 98 null space of, 98 on $\pmb { \mathscr { s } } _ { \pmb { \mathscr { n } } }$ ,102 positive,100 strictly positive,100   
Lorentz, G.G.,120   
Lucas numbers,62,63,233

Malik, M. A., 144   
Mapping,measure preserving,201   
strongly mixing,201   
Marchuk,G.I.,151   
Markov,A.A.,123   
theorem of,123,141,149   
Markov,V. A.,123   
theorem of,123,148   
Matorin,A.P.,140   
Modulus of continuity,167   
Mohr,E., 123   
Mysovskikh,I.P.,101

Newman,D.J.,20,42,80 Numerical integration,43 for Chebyshev coefficients,185 formula of Lobatto-Markov,54 highest degree of precision,185

Opfer, G., 154   
Orthogonality of Chebyshev polynomials,   
34   
Ortiz,E. L.,216   
Overdetermined linear system,92

Parker, I. B., 157   
Paszkowski, S.,95   
Pel's equation, 231   
Pierre,R., 148   
Pinkus, A., 23   
Poisson kernel, 42   
Pollard,H.,221   
Polynomial, 1 Chebyshev: generalized,90,96 of second kind,7 cyclotomic,224 extrapolation,140 fundamental,11,28,41,46,47 Gegenbauer, 35 growth of,108 interpolating, 11

irreducible, 221   
Jacobi, 35   
Lagrange interpolating,11   
Legendre, 56   
longest, 149   
minimal, 221   
Newton interpolating,25   
permutable,192   
primitive,222   
reducible,221   
Shapiro, 162   
similar, 194   
size of coefficients, 110   
size of derivative of,118   
stable evaluation of,158   
ultraspherical, 35   
Zolotarev, 94   
'olynomial chain,194   
Rahman, Q.I.,145-148   
Rainville,E.D.,190   
Rankin, R. A., 231   
Remez inequality,149   
Reversal of $\pmb { T _ { n } }$ ,10   
Rice, J., 153   
Richardson,iteration,151,153   
Riess, R.D.,168   
Riesz, M., 26,57   
Ritt,J.F., 197   
Rivlin,T.J.,12,14,90,167,189,205,216   
Rogosinski,W.W.,39   
Rouche's theorem,130   
Rudin, W., 162   
Ruscheweyh, S., 154   
Saff,E.B.,94,120   
Schaake,G.,119,146,147   
Schaeffer,A.C.,38,123,136   
Schmeisser,G.,145,148   
Schober, G., 154

Schubert, C., 58   
Schur,1.,210,220,225,227-229,231   
Semi-group property,192   
Separating hyperplane theorem,71   
Shapiro,H. S.,80,162 polynomial,162   
Signature, 74 base of, 74 extremal, 74   
Skeleton theorem,75   
Steinig, J., 161   
Strong uniqueness,80   
Strongly mixing mapping,201   
Studden, W. J., 78   
Szego,G.,35,45,95,119,143,144,159 188

Tau method,113   
Tchakaloff,V.,100   
Thielman, H.P.,196   
Three-term recurrence formula,40   
Titchmarsh,E.C.,131   
Todd, J., 95   
Transfinite diameter, 90   
Trapezoidal rule,101   
Turan,P.,89,145,146   
van der Corput, J.G.,119,146,147   
Vandermonde determinant, 219   
Van Loan, C.F.,151   
Varga,R. S.,180   
von Golitschek,M.,120   
Voronovskaja,E.V.,95,123,130   
Weierstrass approximation theorem,33   
“White”curves, 208   
Wilson, M. W.,189   
Zeller,K.,15,26,77,95,140   
Zygmund,A.,120,165,171,206