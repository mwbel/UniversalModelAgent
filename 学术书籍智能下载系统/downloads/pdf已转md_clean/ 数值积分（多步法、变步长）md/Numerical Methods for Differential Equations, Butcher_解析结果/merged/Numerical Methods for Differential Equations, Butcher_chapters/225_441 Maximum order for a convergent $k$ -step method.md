# 441 Maximum order for a convergent $k$ -step method

As a starting point for the proof we present of the Dahlquist first barrier, use Theorem 410B. Modify this by substituting $z$ in (410d) with the function

$$
\frac { 2 z } { 1 - z }
$$

and then multiplying throughout by $( 1 + z ) ^ { k }$ . We then have

$$
( 1 + z ) ^ { k } \alpha \Bigl ( \frac { 1 - z } { 1 + z } \Bigr ) - \log \Big ( \frac { 1 + z } { 1 - z } \Bigr ) ( 1 + z ) ^ { k } \beta \Bigl ( \frac { 1 - z } { 1 + z } \Bigr ) = O ( z ^ { p + 1 } ) ,
$$

or, what is equivalent,

$$
{ \frac { ( 1 + z ) ^ { k } \alpha \left( { \frac { 1 - z } { 1 + z } } \right) } { z } } { \frac { z } { \log \left( { \frac { 1 + z } { 1 - z } } \right) } } - ( 1 + z ) ^ { k } \beta \Bigl ( { \frac { 1 - z } { 1 + z } } \Bigr ) = O ( z ^ { p } ) .
$$

For the rest of this subsection, including assumptions within lemmas and theorems, we write

$$
\begin{array} { r l } & { a ( z ) = a _ { 0 } + a _ { 1 } z + a _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + a _ { k } z ^ { k } = ( 1 + z ) ^ { k } \alpha \big ( \frac { 1 - z } { 1 + z } \big ) , } \\ & { } \\ & { b ( z ) = b _ { 0 } + b _ { 1 } z + b _ { 2 } z ^ { 2 } + \cdot \cdot \cdot + b _ { k } z ^ { k } \ = ( 1 + z ) ^ { k } \beta \big ( \frac { 1 - z } { 1 + z } \big ) . } \end{array}
$$

By consistency, $a _ { 0 } = 0$ so that (441a) can be written in the form

$$
\begin{array} { c } { { ( a _ { 1 } + a _ { 2 } z + \cdots + a _ { k } z ^ { k - 1 } ) ( c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdots ) } } \\ { { { } } } \\ { { - ( b _ { 0 } + b _ { 1 } z + b _ { 2 } z ^ { 2 } + \cdots + b _ { k } z ^ { k } ) = O ( z ^ { p } ) , } } \end{array}
$$

where

$$
{ \frac { z } { \log \left( { \frac { 1 + z } { 1 - z } } \right) } } = c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdot \cdot \cdot .
$$

The way we use this result, when we consider the possibility that $p > k$ , is to note that this implies that the coefficients of zk+1, , $z ^ { p - 1 }$ in

$$
( a _ { 1 } + a _ { 2 } z + \cdot \cdot \cdot + a _ { k } z ^ { k - 1 } ) ( c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdot \cdot \cdot )
$$

are zero.

We will go about this is by establishing some results on the signs of the coefficients $a _ { 1 }$ , $a _ { 2 }$ , . . . , $a _ { k }$ , $c _ { 2 }$ , $c _ { 4 }$ , . . . .

Lemma 441A If the method under consideration is stable then $a _ { 1 } > 0$ and $a _ { i } \geq 0$ , for $i = 2 , 3 , \ldots , k$ .

Proof. Write the polynomial $a$ in the form

$$
a ( z ) = ( 1 + z ) ^ { k } - \alpha _ { 1 } ( 1 + z ) ^ { k - 1 } ( 1 - z ) - \alpha _ { 2 } ( 1 + z ) ^ { k - 2 } ( 1 - z ) ^ { 2 } - \cdot \cdot \cdot - \alpha _ { k } ( 1 - z ) ^ { k } .
$$

We calculate the value of $a _ { 1 }$ , the coefficient of $z$ , to be

$$
k - ( k - 2 ) \alpha _ { 1 } - ( k - 4 ) \alpha _ { 2 } - \cdot \cdot \cdot - ( - k ) \alpha _ { k } = k \alpha ( 1 ) - 2 \alpha ^ { \prime } ( 1 ) = - 2 \alpha ^ { \prime } ( 1 ) ,
$$

because $\alpha ( 1 ) = 0$ . The polynomial $\rho$ , which we recall is defined by

$$
\rho ( z ) = z ^ { k } - \alpha _ { 1 } z ^ { k - 1 } - \alpha _ { 2 } z ^ { k - 2 } - \cdot \cdot \cdot - \alpha _ { k } ,
$$

has no real zeros greater than 1, and hence, because $\rho ( 1 ) = 0$ and because $\begin{array} { r } { \operatorname* { l i m } _ { z - > \infty } \rho ( z ) = \infty } \end{array}$ , it is necessary that $\rho ^ { \prime } ( 1 ) > 0$ . Calculate this to be

$$
\rho ^ { \prime } ( 1 ) = k - ( k - 1 ) \alpha _ { 1 } - ( k - 2 ) \alpha _ { 2 } - \cdot \cdot \cdot - \alpha _ { k - 1 } = a _ { 1 } .
$$

This completes the proof that $a _ { 1 } > 0$ .

Write $\zeta$ for a possible zero of $a$ so that, because of the relationship between this polynomial and $\alpha$ , it follows that

$$
\frac { 1 - \zeta } { 1 + \zeta }
$$

is a zero of $\alpha$ , unless it happens that $\zeta = - 1$ , in which case there is a drop in the degree of $\alpha$ . In either case, we must have $\mathrm { R e } ( \zeta ) \leq 0$ . Because all zeros of $a$ are real, or occur in conjugate pairs, the polynomial $a$ can be decomposed into factors of the form $z - \xi$ or of the form $z ^ { 2 } - 2 \xi z + ( \xi ^ { 2 } + \eta ^ { 2 } )$ , where the real number $\xi$ cannot be positive. This means that all factors have only terms with coefficients of the same sign, and accordingly this also holds for $a$ itself. These coefficients must in fact be non-negative because $a _ { 1 } > 0$ . 

Lemma 441B The coefficients $c _ { 2 }$ , $c _ { 4 }$ , . . . are all negative.

Proof. Using the series for $\log { \big ( } ( 1 + z ) / ( 1 - z ) { \big ) } / z$ , we see that $c _ { 0 }$ , $c _ { 2 }$ , $c _ { 4 }$ , . . . satisfy

$$
\bigl ( 2 + { \frac { 2 } { 3 } } z ^ { 2 } + { \frac { 2 } { 5 } } z ^ { 4 } + \cdots \bigr ) ( c _ { 0 } + c _ { 2 } z ^ { 2 } + c _ { 4 } z ^ { 4 } + \cdots ) = 1 .
$$

It follows that $c _ { 0 } = \textstyle { \frac { 1 } { 2 } }$ , $c _ { 2 } = - \textstyle { \frac { 1 } { 6 } }$ . We prove $c _ { 2 n } < 0$ by induction for $n = 2$ , $n = 3$ , . . . . If $c _ { 2 i } < 0$ for $i = 1 , 2 , \dots , n - 1$ then we multiply (441c) by $2 n + 1 - ( 2 n - 1 ) z ^ { 2 }$ . We find

$$
\sum _ { i = 0 } ^ { \infty } d _ { 2 i } z ^ { 2 i } \cdot \sum _ { i = 0 } ^ { \infty } c _ { 2 i } z ^ { 2 i } = 2 n + 1 - ( 2 n - 1 ) z ^ { 2 } ,
$$

where, for $i = 1 , 2 , \ldots , n$ ,

$$
d _ { 2 i } = \frac { 2 ( 2 n + 1 ) } { 2 i + 1 } - \frac { 2 ( 2 n - 1 ) } { 2 i - 1 } = - \frac { 8 ( n - i ) } { ( 2 i + 1 ) ( 2 i - 1 ) } ,
$$

so that $d _ { 2 i } < 0$ , for $i = 1 , 2 , \dots , n - 1$ , and $d _ { 2 n } = 0$ . Equate the coefficients of $z ^ { 2 n }$ in (441d) and we find that

$$
c _ { 2 n } = - { \frac { c _ { 2 } d _ { 2 n - 2 } + c _ { 4 } d _ { 2 n - 4 } + \cdot \cdot \cdot + c _ { 2 n - 2 } d _ { 2 } } { d _ { 0 } } } < 0 .
$$

We are now in a position to prove the Dahlquist barrier result.

Theorem 441C Let $\lfloor \alpha , \beta \rfloor$ denote a stable linear multistep method with order $p$ . Then

$$
p \leq \left\{ \begin{array} { l l } { k + 1 , } & { k o d d , } \\ { k + 2 , } & { k e v e n . } \end{array} \right.
$$

Proof. Consider first the case $k$ odd and evaluate the coefficient of $z ^ { k + 1 }$ in (441b). This equals

$$
a _ { k } c _ { 2 } + a _ { k - 2 } c _ { 4 } + \cdot \cdot \cdot + a _ { 1 } c _ { k + 1 }
$$

and, because no term is positive, the total can be zero only if each term is zero.   
However, this would mean that $a _ { 1 } = 0$ , which is inconsistent with stability.

In the case $k$ even, we evaluate the coefficient of $z ^ { k + 2 }$ in (441b). This is

$$
a _ { k - 1 } c _ { 4 } + a _ { k - 3 } c _ { 6 } + \cdot \cdot \cdot + a _ { 1 } c _ { k + 2 } .
$$

Again, every term is non-positive and because the total is zero, it again follows that $a _ { 1 } = 0$ which contradicts the assumption of stability. 

There is some interest in the methods with maximal order $2 k + 2$ , for $k$ even. For these methods, $\alpha$ has all its zeros on the unit circle. This evidently gives the methods a symmetry that suggests it might be advantageous to use them for problems whose behaviour is dominated by linear terms with purely imaginary eigenvalues. Against this possible advantage is the observation that the stability regions necessarily have empty interiors.
