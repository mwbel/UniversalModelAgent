3. (a) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 0 , 0 , 0 ) ^ { t } } \end{array}$ . (b) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 0 , 1 , 3 ) ^ { t } } \end{array}$ . (c) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 0 , 0 , \frac { 1 } { 2 } ) ^ { t } } \end{array}$ . (d) We have $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } \mathbf { x } ^ { ( k ) } = ( 1 , - 1 , 1 ) ^ { t } } \end{array}$ .

4. The $l _ { \infty }$ norms are as follows:

(a) 25 (b) 16 (c) 4 (d) 12

5. (a) We have $| | \mathbf { x } - \hat { \mathbf { x } } | | _ { \infty } = 8 . 5 7 \times 1 0 ^ { - 4 }$ and $| | A \hat { \mathbf { x } } - \mathbf { b } | | _ { \infty } = 2 . 0 6 \times 1 0 ^ { - 4 }$ .

(b) We have $| | \mathbf { x } - \hat { \mathbf { x } } | | _ { \infty } = 0 . 9 0$ and $| | A { \hat { \mathbf { x } } } - \mathbf { b } | | _ { \infty } = 0 . 2 7$ .   
(c) We have $| | \mathbf { x } - \hat { \mathbf { x } } | | _ { \infty } = 0 . 5$ and $| | A \hat { \mathbf { x } } - \mathbf { b } | | _ { \infty } = 0 . 3$ .   
(d) We have $| | \mathbf { x } - { \hat { \mathbf { x } } } | | _ { \infty } = 6 . 5 5 \times 1 0 ^ { - 2 }$ , and $| | A { \hat { \mathbf { x } } } - \mathbf { b } | | _ { \infty } = 0 . 3 2$ .

6. The $l _ { \infty }$ norms are as follows:

(a) 16 (b) 25 (c) 4 \*(d) 12 $^ { * } 7$ . Let $A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] }$ and $B = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] }$ . Then $\| A B \| _ { \otimes } = 2$ , but $\left\| A \right\| _ { \bigotimes } \cdot \left\| B \right\| _ { \bigotimes } = 1$

8. Showing properties (i) – (iv) of Definition 7.8 is similar to the proof in Exercise 2a. To show property (v),

$$
\begin{array} { r l } & { \| A B \| _ { \mathbb { D } } = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 1 } ^ { n } \left| \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j } \right| \leq \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } \sum _ { k = 1 } ^ { n } | a _ { i k } | | b _ { k j } | } \\ & { \qquad = \displaystyle \sum _ { i = 1 } ^ { n } \left\{ \sum _ { k = 1 } ^ { n } \left| a _ { i k } \right| \sum _ { j = 1 } ^ { n } | b _ { k j } | \right\} \leq \displaystyle \sum _ { i = 1 } ^ { n } \left( \sum _ { k = 1 } ^ { n } | a _ { i k } | \right) \left( \displaystyle \sum _ { k = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | b _ { k j } | \right) } \\ & { \qquad = \displaystyle \left( \sum _ { i = 1 } ^ { n } \sum _ { k = 1 } ^ { n } | a _ { i k } | \right) \| B \| _ { \mathbb { D } } = \| A \| _ { \mathbb { D } } \| B \| _ { \mathbb { D } } . } \end{array}
$$

The norms of the matrices in Exercise 4 are (4a) 26, (4b) 26, (4c) 10, and (4d) 28.

9. (a) Showing properties ( $i )$ - $( i v )$ of Definition 7.8 is straight-forward. Property (v) is shown as

follows:

$$
\begin{array} { r l r } { \| A B \| _ { F } ^ { 2 } = } & { \left( \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 1 } ^ { n } \left| \displaystyle \sum _ { k = 1 } ^ { n } a _ { i k } b _ { k j } \right| ^ { 2 } \right) } \\ & { \leq } & { \left( \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { j = 1 } ^ { n } \left( \displaystyle \sum _ { k = 1 } ^ { n } \left| a _ { i k } \right| ^ { 2 } \displaystyle \sum _ { k = 1 } ^ { n } | b _ { k j } | ^ { 2 } \right) \right) \quad \mathrm { ~ b y ~ T h e o r e m ~ 7 . 3 ~ } } \\ & { = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } \left[ | a _ { i k } | ^ { 2 } \left( \displaystyle \sum _ { j = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } | b _ { k j } | ^ { 2 } \right) \right] } \\ & { = \displaystyle \sum _ { i = 1 } ^ { n } \displaystyle \sum _ { k = 1 } ^ { n } | a _ { i k } | ^ { 2 } \| B \| _ { F } ^ { 2 } = \| B \| _ { F } ^ { 2 } \displaystyle \sum _ { i = 1 } ^ { n } | a _ { i k } | ^ { 2 } = \| B \| _ { F } ^ { 2 } \| A \| _ { F } ^ { 2 } = \| A \| _ { F } ^ { 2 } \| B \| _ { F } ^ { 2 } . } \end{array}
$$

(b) We have

(4a) $\begin{array} { l } { \| A \| _ { F } = \sqrt { 3 2 6 } } \\ { \| A \| _ { F } = \sqrt { 3 2 6 } } \\ { \| A \| _ { F } = 4 } \\ { \| A \| _ { F } = \sqrt { 1 4 8 } . } \end{array}$   
(4b)   
(4c)   
(4d)

(c) We have

$$
\begin{array} { r l } & { \| A \| _ { 2 } ^ { 2 } = \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right) ^ { 2 } \leq \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | | x _ { j } | \right) ^ { 2 } } \\ & { \qquad \leq \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left[ \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right] ^ { 2 } = \displaystyle \operatorname* { m a x } _ { \| { \bf x } \| _ { 2 } = 1 } \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) } \\ & { \qquad = \displaystyle \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } = \| A \| _ { F } ^ { 2 } } \end{array}
$$

Let $j$ be fixed and define

$$
x _ { k } = { \left\{ \begin{array} { l l } { 0 , } & { { \mathrm { i f ~ } } k \neq j } \\ { 1 , } & { { \mathrm { i f ~ } } k = j . } \end{array} \right. }
$$

Then $A \mathbf { x } = ( a _ { 1 j } , a _ { 2 j } , \dotsc , a _ { n j } ) ^ { t }$ , so

$$
\| A \| _ { 2 } ^ { 2 } \geq \| A \mathbf { x } \| _ { 2 } ^ { 2 } \geq \sum _ { i = 1 } ^ { n } | a _ { i j } | ^ { 2 } .
$$

Thus

$$
\| A \| _ { F } ^ { 2 } = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } = \sum _ { j = 1 } ^ { n } \sum _ { i = 1 } ^ { n } | a _ { i j } | ^ { 2 } \leq \sum _ { j = 1 } ^ { n } \| A \| _ { 2 } ^ { 2 } = n \| A \| _ { 2 } ^ { 2 } .
$$

Hence, $\| A \| _ { 2 } \leq \| A \| _ { F } \leq { \sqrt { n } } \| A \| _ { 2 }$ .

10. We have

$$
\| A \mathbf { x } \| _ { 2 } ^ { 2 } = \sum _ { i = 1 } ^ { n } \left| \sum _ { j = 1 } ^ { n } a _ { i j } x _ { j } \right| ^ { 2 } \leq \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | | x _ { j } | \right) ^ { 2 } .
$$

Using the Cauchy–Buniakowsky–Schwarz inequality gives

$$
\| A \mathbf { x } \| _ { 2 } ^ { 2 } \leq \sum _ { i = 1 } ^ { n } \left( \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \left( \sum _ { j = 1 } ^ { n } | x _ { j } | ^ { 2 } \right) ^ { \frac { 1 } { 2 } } \right) ^ { 2 } = \sum _ { i = 1 } ^ { n } \left( \sum _ { j = 1 } ^ { n } | a _ { i j } | ^ { 2 } \right) \| \mathbf { x } \| _ { 2 } ^ { 2 } = \| A \| _ { F } ^ { 2 } \| \mathbf { x } \| _ { 2 } ^ { 2 } .
$$

Thus, $\| A \mathbf { x } \| _ { 2 } \leq \| A \| _ { F } \| \mathbf { x } \| _ { 2 }$ .

$^ { * } 1 1$ . That $\| \mathbf { x } \| \geq 0$ follows easily. That $\| \mathbf { x } \| = 0$ if and only if $\mathbf x = \mathbf 0$ follows from the definition of positive definite. In addition,

$$
\| { \boldsymbol { \alpha } } \mathbf { x } \| = \left[ \left( \alpha \mathbf { x } ^ { t } \right) { \boldsymbol { S } } ( { \boldsymbol { \alpha } } \mathbf { x } ) \right] ^ { \frac { 1 } { 2 } } = \left[ \alpha ^ { 2 } \mathbf { x } ^ { t } { \boldsymbol { S } } \mathbf { x } \right] ^ { \frac { 1 } { 2 } } = | { \boldsymbol { \alpha } } | \left( \mathbf { x } ^ { t } { \boldsymbol { S } } \mathbf { x } \right) ^ { \frac { 1 } { 2 } } = | { \boldsymbol { \alpha } } | \| \mathbf { x } \| .
$$

From Cholesky’s factorization, let $S = L L ^ { t }$ . Then

$$
\begin{array} { r l } & { \mathbf { x } ^ { t } S \mathbf { y } = \mathbf { x } ^ { t } L L ^ { t } \mathbf { y } = \left( L ^ { t } \mathbf { x } \right) ^ { t } \left( L ^ { t } \mathbf { y } \right) } \\ & { \qquad \leq \left[ \left( L ^ { t } \mathbf { x } \right) ^ { t } \left( L ^ { t } \mathbf { x } \right) \right] ^ { 1 / 2 } \left[ \left( L ^ { t } \mathbf { y } \right) ^ { t } \left( L ^ { t } \mathbf { y } \right) \right] ^ { 1 / 2 } } \\ & { \qquad = \left( \mathbf { x } ^ { t } L L ^ { t } \mathbf { x } \right) ^ { 1 / 2 } \left( \mathbf { y } ^ { t } L L ^ { t } \mathbf { y } \right) ^ { 1 / 2 } = \left( \mathbf { x } ^ { t } S \mathbf { x } \right) ^ { 1 / 2 } \left( \mathbf { y } ^ { t } S \mathbf { y } \right) ^ { 1 / 2 } . } \end{array}
$$

Thus

$$
\begin{array} { r l } & { \| \mathbf { x } + \mathbf { y } \| ^ { 2 } = \left[ \left( \mathbf { x } + \mathbf { y } \right) ^ { t } S \left( \mathbf { x } + \mathbf { y } \right) \right] = \left[ \mathbf { x } ^ { t } S \mathbf { x } + \mathbf { y } ^ { t } S \mathbf { x } + \mathbf { x } ^ { t } S \mathbf { y } + \mathbf { y } ^ { t } S \mathbf { y } \right] } \\ & { \qquad \leq \mathbf { x } ^ { t } S \mathbf { x } + 2 \left( \mathbf { x } ^ { t } S \mathbf { x } \right) ^ { 1 / 2 } \left( \mathbf { y } ^ { t } S \mathbf { y } \right) ^ { 1 / 2 } + \left( \mathbf { y } ^ { t } S \mathbf { y } \right) ^ { 1 / 2 } } \\ & { \qquad = \mathbf { x } ^ { t } S \mathbf { x } + 2 \| \mathbf { x } \| \| \mathbf { y } \| + \mathbf { y } ^ { t } S \mathbf { y } = \left( \| \mathbf { x } \| + \| \mathbf { y } \| \right) ^ { 2 } . } \end{array}
$$

This demonstrates properties $( i ) \mathrm { ~ - ~ } ( i v )$ of Definition 7.1.

12. Since $\| \mathbf { x } \| ^ { \prime } = 0$ implies $\| S \mathbf { x } \| = 0$ , we have $S x = \mathbf { 0 }$ . Since $S$ is nonsingular, $\mathbf x = \mathbf 0$ . Also,

$$
\| \mathbf { x } + \mathbf { y } \| ^ { \prime } = \| S ( \mathbf { x } + \mathbf { y } ) \| = \| S \mathbf { x } + S \mathbf { y } \| \leq \| S \mathbf { x } \| + \| S \mathbf { y } \| = \| \mathbf { x } \| ^ { \prime } + \| \mathbf { y } \| ^ { \prime }
$$

and

$$
\| \alpha \mathbf { x } \| ^ { \prime } = \| S ( \alpha \mathbf { x } ) \| = | \alpha | \ \| S \mathbf { x } \| = | \alpha | \ \| \mathbf { x } \| ^ { \prime } .
$$

$^ *$ 13. It is not difficult to show that $( i )$ holds. If $\| A \| = 0$ , then $\| A \mathbf { x } \| = 0$ for all vectors $\mathbf { x }$ with $\| \mathbf { x } \| = 1$ . Using $\mathbf { x } = ( 1 , 0 , \ldots , 0 ) ^ { t }$ , $\mathbf { x } = ( 0 , 1 , 0 , \ldots , 0 ) ^ { t } , . . .$ , and $\mathbf { x } = ( 0 , \ldots , 0 , 1 ) ^ { t }$ successively implies that each column of $A$ is zero. Thus, $\| A \| = 0$ if and only if $A = 0$ . Moreover,

$$
\begin{array} { r l r } & { } & { \| \alpha A \| = \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } \| ( \alpha A { \bf x } ) \| = | \alpha | \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } \| A { \bf x } \| = | \alpha | \cdot \| A \| , } \\ & { } & { \| A + B \| = \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } \| ( A + B ) { \bf x } \| \le \underset { \| { \bf x } \| = 1 } { \operatorname* { m a x } } ( \| A { \bf x } \| + \| B { \bf x } \| ) , ~ } \end{array}
$$

so

$$
| | A + B | | \leq \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } | | A \mathbf { x } | | + \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } | | B \mathbf { x } | | = \| A \| + \| B \|
$$

and

$$
\| A B \| = \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| ( A B ) \mathbf { x } \| = \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| A ( B \mathbf { x } ) \| .
$$

Thus

$$
| | A B | | \leq \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| A \| \ \| B \mathbf { x } \| = \| A \| \operatorname* { m a x } _ { \| \mathbf { x } \| = 1 } \| B \mathbf { x } \| = \| A \| \ \| B \| .
$$

14. (a) We have

$$
\begin{array} { l } { \displaystyle \sum _ { i = 1 } ^ { \frac { n } { 2 } } \left( \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } - \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } \right) ^ { 2 } = \sum _ { i = 1 } ^ { n } \frac { x _ { i } ^ { 2 } } { \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } } - 2 \sum _ { i = 1 } ^ { n } \frac { x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \\ { + \displaystyle \sum _ { i = 1 } ^ { n } \frac { y _ { i } ^ { 2 } } { \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } } } \\ { = 1 - 2 \sum _ { i = 1 } ^ { n } \frac { x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } + 1 . } \end{array}
$$

Thus

$$
{ \frac { \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } = 1 - { \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \left( { \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } - { \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \right) ^ { 2 } .
$$

(b) Since

$$
{ \frac { 1 } { 2 } } \sum _ { i = 1 } ^ { n } \left( { \frac { x _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } - { \frac { y _ { i } } { \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } } \right) ^ { 2 } \geq 0 ,
$$

we have

$$
\frac { \sum _ { i = 1 } ^ { n } x _ { i } y _ { i } } { \left( \sum _ { j = 1 } ^ { n } x _ { j } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { j = 1 } ^ { n } y _ { j } ^ { 2 } \right) ^ { 1 / 2 } } \leq 1
$$

and

$$
\sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \left( \sum _ { i = 1 } ^ { n } x _ { i } ^ { 2 } \right) ^ { 1 / 2 } \left( \sum _ { i = 1 } ^ { n } y _ { i } ^ { 2 } \right) ^ { 1 / 2 } .
$$

15. Define $\mathbf { z } = ( z _ { 1 } , z _ { 2 } , \ldots , z _ { n } ) ^ { t }$ by $z _ { i } ~ = ~ x _ { i }$ when $y _ { i } \geq 0$ and $z _ { i } = - x _ { i }$ when $y _ { i } < 0$ . Since the Cauchy-Buniakowsky-Schwarz Inequality holds for $\mathbf { z }$ and $\mathbf { y }$ we have

$$
\sum _ { i = 1 } ^ { n } x _ { i } y _ { i } \leq \sum _ { i = 1 } ^ { n } | x _ { i } y _ { i } | = \sum _ { i = 1 } ^ { n } z _ { i } y _ { i } \leq \sum _ { i = 1 } ^ { n } \{ z _ { i } ^ { 2 } \} ^ { 1 / 2 } \sum _ { i = 1 } ^ { n } \{ y _ { i } ^ { 2 } \} ^ { 1 / 2 } = \sum _ { i = 1 } ^ { n } \{ x _ { i } ^ { 2 } \} ^ { 1 / 2 } \sum _ { i = 1 } ^ { n } \{ y _ { i } ^ { 2 } \} ^ { 1 / 2 } .
$$

# Exercise Set 7.2, page 449

1. (a) The eigenvalue $\lambda _ { 1 } = 3$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = 1$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , 1 ) ^ { t }$ . (b) alue has $\textstyle \lambda _ { 1 } = { \frac { 1 + { \sqrt { 5 } } } { 2 } }$ has ctor $\mathbf { x } = \left( 1 , ( 1 + \sqrt { 5 } ) / 2 \right) ^ { t }$ , and the eigenvalue λ2 = 1− √5 $\mathbf { x } = { \left( 1 , { \left( 1 - { \sqrt { 5 } } \right) } / 2 \right) } ^ { t }$ (c) The eigenvalue $\lambda _ { 1 } = \textstyle { \frac { 1 } { 2 } }$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = - \frac { 1 } { 2 }$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , - 1 ) ^ { t }$ . $^ { * } ( \mathrm { d } )$ The eigenvalue $\lambda _ { 1 } = 1$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 , 0 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = \lambda _ { 3 } =$ 3 has the eigenvectors $\mathbf { x } _ { 2 } = ( 1 , 1 , 0 ) ^ { t }$ and $\mathbf { x } _ { 3 } = ( 0 , 0 , 1 ) ^ { t }$ . (e) The eigenvalue $\lambda _ { 1 } = 7$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , 4 , 4 ) ^ { t }$ , the eigenvalue $\lambda _ { 2 } = - 1$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , 0 , 0 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = 3$ has the eigenvector $\mathbf { x } _ { 3 } = ( 1 , 2 , 0 ) ^ { t }$ . (f) The eigenvalue $\lambda _ { 1 } = \lambda _ { 2 } = 1$ has the eigenvectors $\mathbf { x } _ { 1 } = ( - 1 , 0 , 1 ) ^ { t }$ and $\mathbf { x } _ { 2 } = ( - 1 , 1 , 0 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = 5$ has the eigenvector $\mathbf { x } = ( 1 , 2 , 1 ) ^ { t }$ .

2. (a) The eigenvalue $\lambda _ { 1 } = 0$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = - 1$ has the eigenvector $\mathbf { x } _ { 2 } = ( 1 , - 2 ) ^ { t }$ . (b) The eigenvalue $\lambda _ { 1 } ~ = ~ - 1 / 3$ has the eigenvector $\mathbf { x } _ { 1 } ~ = ~ ( - 3 / 2 , 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = - 1 / 2$ has the eigenvector $\mathbf { x } _ { 2 } = ( - 2 , 1 ) ^ { t }$ . (c) The eigenvalue $\lambda _ { 1 } = - 1$ has the eigenvector $\mathbf { x } _ { 1 } = ( 1 , - 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 2 } = 4$ has the eigenvector $\mathbf { x } _ { 2 } = ( 4 , 1 ) ^ { t }$ . (d) The eigenvalue $\lambda _ { 1 } = 3$ has the eigenvector $\mathbf { x } _ { 1 } = ( - 1 , 1 , 2 ) ^ { t }$ , the eigenvalue $\lambda _ { 2 } = 4$ has the eigenvector $\mathbf { x } _ { 2 } = ( 0 , 1 , 2 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = - 2$ has the eigenvector $\mathbf { x } = ( - 3 , 8 , 1 ) ^ { t }$ . (e) The eigenvalue $\lambda _ { 1 } = \lambda _ { 2 } = 1 / 2$ has the eigenvector $\mathbf { x } _ { 1 } = ( 0 , 5 , 1 2 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = - 1 / 3$ has the eigenvector $\mathbf { x } _ { 3 } = ( 0 , 0 , 1 ) ^ { t }$ . (f) The eigenvalue $\lambda _ { 1 } = 2 + 2 i$ has the eigenvector $\mathbf { x } _ { 1 } = ( 0 , - 2 i , 1 ) ^ { t }$ , the eigenvalue $\lambda _ { 2 } =$ $2 - 2 i$ has the eigenvector $\mathbf { x } _ { 2 } = ( 0 , 2 i , 1 ) ^ { t }$ , and the eigenvalue $\lambda _ { 3 } = 2$ has the eigenvector $\mathbf { x } _ { 3 } = ( 1 , 0 , 0 ) ^ { t }$ .

3. (a) The eigenvalue $\lambda _ { 1 } = 2 + \sqrt { 2 } i$ has the eigenvector $( { \sqrt { 2 } } i , - 1 ) ^ { t }$ and the eigenvalue $\lambda _ { 2 } =$ $2 - \sqrt { 2 } i$ has the eigenvector $( \sqrt { 2 } i , 1 ) ^ { t }$ . \*(b) The eigenvalue $\begin{array} { r } { \lambda _ { 1 } = \frac { 1 } { 2 } ( 3 + \sqrt { 7 } i ) } \end{array}$ has the eigenvector $( 1 - { \sqrt { 7 } } i , 2 ) ^ { t }$ and the eigenvalue $\begin{array} { r } { \lambda _ { 2 } = \frac { 1 } { 2 } ( 3 - \sqrt { 7 } i } \end{array}$ has the eigenvector $( 1 + { \sqrt { 7 } } i , 2 ) ^ { t }$ .

4. (a) The eigenvalue $\lambda _ { 1 } = 1 + { \sqrt { 3 } } i$ has the eigenvector $( 2 \sqrt { 3 } i , - \sqrt { 3 } i , - 3 ) ^ { t }$ and the eigenvalue $\lambda _ { 2 } = 1 - \sqrt { 3 } i$ has the eigenvector $( 2 { \sqrt { 3 } } i , - { \sqrt { 3 } } i , 3 ) ^ { t }$ . (b) The eigenvalue $\lambda _ { 1 } = 1 { + } \sqrt { 2 } i$ has the eigenvector $( 3 , 1 - \sqrt { 2 } i , - 1 - 2 \sqrt { 2 } i ) ^ { t }$ and the eigenvalue $\lambda _ { 2 } = 1 - \sqrt { 2 } i$ has the eigenvector $( 3 , 1 + { \sqrt { 2 } } i , - 1 + 2 { \sqrt { 2 } } i ) ^ { t }$ .

5. The spectral radii for the matrices in Exercise $^ { 1 }$ are;

(a) 3 $( \mathrm { b ) ~ { \frac { 1 + { \sqrt { 5 } } } { 2 } } ~ \quad ( c ) ~ { \frac { 1 } { 2 } } ~ \quad ~ \ast ( \mathrm { d } ) ~ { 3 } }$ (e) 7 (f) 5

6. The spectral radii for the matrices in Exercise 2 are:

(a) 1 (b) $\frac { 1 } { 2 }$ (c) 4 (d) 4 (e) $\frac { 1 } { 2 }$ (f ) 2 √2

$^ { * } 7$ . Only the matrix in $1 ( \mathrm { c } )$ is convergent.

8. Only the matrices in $2 ( \mathrm { b } )$ and $2 ( \mathrm { e } )$ are convergent.

9. The $l _ { 2 }$ norms for the matrices in Exercise 1 are:

(a) 3 (b) 1.618034 (c) 0.5 (d) 3 (e) 8.224257 (f) 5.203527

10. The $l _ { 2 }$ norms for the matrices in Exercise 1 are:

(a) 3.162278 (b) 1.458020 (c) 5.036796 (d) 5.601152 (e) 2.896954 (f) 4.701562

11. Since

$$
A _ { 1 } ^ { k } = [ \frac { 1 } { 2 ^ { k } - 1 } \quad 2 ^ { - k } ] , \quad \mathrm { ~ w e ~ h a v e ~ } \quad \operatorname* { l i m } _ { k  \infty } A _ { 1 } ^ { k } = [ \frac { 1 } { 2 } \quad 0 ] .
$$

Also,

$$
A _ { 2 } ^ { k } = [ { \frac { 2 ^ { - k } } { 2 ^ { k - 1 } } } \quad \quad 0 \atop { 2 ^ { - k } } ] , \quad { \mathrm { ~ s o ~ } } \quad \operatorname* { l i m } _ { k  \infty } A _ { 2 } ^ { k } = [ { \begin{array} { l l } { 0 } & { 0 } \\ { 0 } & { 0 } \end{array} } ] .
$$

$^ { * } 1 2$ . Suppose the $\lambda$ is an eigenvalue of $A$ with corresponding eigenvector $\mathbf { x }$ . Then $A \mathbf { x } \ = \ \lambda \mathbf { x }$ , $A ^ { 2 } \mathbf { x } = A ( \lambda \mathbf { x } ) = \lambda A \mathbf { x } = \lambda ^ { 2 } \mathbf { x }$ , and in general, $A ^ { m } { \bf x } = \lambda ^ { m } { \bf x }$ , for any positive integer $m$ . As a consequence,

$$
\mathbf { 0 } = A ^ { m } \mathbf { x } = \lambda ^ { m } \mathbf { x } \quad { \mathrm { w h i c h ~ i m p l i e s ~ t h a t ~ } } \lambda ^ { m } = 0 .
$$

Hence $\lambda = 0$ .

13. Let $A$ be an $n \times n$ matrix. Expanding across the first row gives the characteristic polynomial

$$
p ( \lambda ) = \operatorname * { d e t } ( A - \lambda I ) = ( a _ { 1 1 } - \lambda ) M _ { 1 1 } + \sum _ { j = 2 } ^ { n } ( - 1 ) ^ { j + 1 } a _ { 1 j } M _ { 1 j } .
$$

The determinants $M _ { 1 j }$ are of the form

$$
M _ { 1 j } = \operatorname* { d e t } \left[ \begin{array} { c c c c c c c c } { a _ { 2 1 } } & { a _ { 2 2 } - \lambda } & { \cdots } & { a _ { 2 , j - 1 } } & { a _ { 2 , j + 1 } } & { \cdots } & { a _ { 2 n } } \\ { a _ { 3 1 } } & { a _ { 3 2 } } & { \cdots } & { a _ { 3 , j - 1 } } & { a _ { 3 , j + 1 } } & { \cdots } & { a _ { 3 n } } \\ { \vdots } & { \vdots } & & & { \vdots } & & & { \vdots } \\ { a _ { j - 1 , 1 } } & { a _ { j - 1 , 2 } } & { \cdots } & { a _ { j - 1 , j - 1 } - \lambda } & { a _ { j - 1 , j + 1 } } & { \cdots } & { a _ { j - 1 , n } } \\ { a _ { j , 1 } } & { a _ { j , 2 } } & { \cdots } & { a _ { j , j - 1 } } & { a _ { j , j + 1 } } & { \cdots } & { a _ { j , n } } \\ { a _ { j + 1 , 1 } } & { a _ { j + 1 , 2 } } & { \cdots } & { a _ { j + 1 , j - 1 } } & { a _ { j + 1 , j + 1 } - \lambda } & { \cdots } & { a _ { j + 1 , n } } \\ { \vdots } & { \vdots } & & & { \vdots } & { \vdots } & & { \vdots } \\ { a _ { n 1 } } & { a _ { n 2 } } & { \cdots } & { a _ { n , j - 1 } } & { a _ { n , j + 1 } } & { \cdots } & { a _ { n n } - \lambda } \\ { a _ { n 1 } } & & & & & & {  } \end{array} \right] ,
$$

for $j = 2 , \dots , n$ . Note that each $M _ { 1 j }$ has $n - 2$ entries of the form $a _ { i i } - \lambda$ . Thus,

$$
p ( \lambda ) = \operatorname* { d e t } ( A - \lambda I ) = ( a _ { 1 1 } - \lambda ) M _ { 1 1 } + \{ { \mathrm { t e r m s ~ o f ~ d e g r e e ~ } } n - 2 { \mathrm { ~ o r ~ l e s s } } \} .
$$

Since

$$
M _ { 1 1 } = \operatorname* { d e t } { \left[ \begin{array} { l l l l l l } { a _ { 2 2 } - \lambda } & { a _ { 2 3 } } & { \cdots } & { \cdots } & { a _ { 2 n } } \\ { a _ { 3 2 } } & { a _ { 3 3 } - \lambda } & { \ddots } & & { \vdots } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { \vdots } & & { \ddots } & { \ddots } & { a _ { n - 1 , n } } \\ { a _ { n 2 } } & { \ldots } & { \ldots } & { a _ { n , n - 1 } } & { a _ { n n } - \lambda } \end{array} \right] }
$$

is of the same form as $\operatorname* { d e t } ( A - \lambda I )$ , the same argument can be repeatedly applied to determine

$$
p ( \lambda ) = ( a _ { 1 1 } - \lambda ) { \left( a _ { 2 2 } - \lambda \right) } \cdot \cdot { \left( a _ { n n } - \lambda \right) } + \{ { \mathrm { t e r m s ~ o f ~ d e g r e e ~ } } n - 2 { \mathrm { ~ o r ~ l e s s ~ i n ~ } } \lambda \} .
$$

Thus, $p ( \lambda )$ is a polynomial of degree $n$

$^ *$ 14. (a) $P ( \lambda ) = ( \lambda _ { 1 } - \lambda ) \ldots ( \lambda _ { n } - \lambda ) = \operatorname* { d e t } ( A - \lambda I ) , { \mathrm { ~ s o ~ } } P ( 0 ) = \lambda _ { 1 } \cdots \lambda _ { n } = \operatorname* { d e t } A .$ (b) A singular if and only if $\operatorname* { d e t } A = 0$ , which is equivalent to at least one of $\lambda _ { i }$ being $0$ .

15. (a) $\operatorname* { d e t } ( A - \lambda I ) = \operatorname* { d e t } ( ( A - \lambda I ) ^ { t } ) = \operatorname* { d e t } ( A ^ { t } - \lambda I )$ (b) If $A \mathbf { x } = \lambda \mathbf { x }$ , then $A ^ { 2 } \mathbf { x } = \lambda A \mathbf { x } = \lambda ^ { 2 } \mathbf { x }$ , and by induction, $A ^ { k } \mathbf { x } = \lambda ^ { k } \mathbf { x }$ . (c) If $A \mathbf { x } = \lambda \mathbf { x }$ and $A ^ { - 1 }$ exists, then $\mathbf { x } = \lambda A ^ { - 1 } \mathbf { x }$ . By Exercise 14 (b), $\lambda \neq 0$ , so $\textstyle { \frac { 1 } { \lambda } } \mathbf { x } = A ^ { - 1 } \mathbf { x }$ . (d) Since $\begin{array} { r } { A ^ { - 1 } \mathbf { x } = \frac { 1 } { \lambda } \mathbf { x } } \end{array}$ , we have $\begin{array} { r } { ( A ^ { - 1 } ) ^ { 2 } \mathbf { x } = \frac { 1 } { \lambda } A ^ { - 1 } \mathbf { x } = \frac { 1 } { \lambda ^ { 2 } } \mathbf { x } } \end{array}$ . Mathematical induction gives

$$
( A ^ { - 1 } ) ^ { k } \mathbf { x } = { \frac { 1 } { \lambda ^ { k } } } \mathbf { x } .
$$

(e) If $A \mathbf { x } = \lambda \mathbf { x }$ , then

$$
q ( A ) \mathbf { x } = q _ { 0 } \mathbf { x } + q _ { 1 } A \mathbf { x } + \ldots + q _ { k } A ^ { k } \mathbf { x } = q _ { 0 } \mathbf { x } + q _ { 1 } \lambda \mathbf { x } + \ldots + q _ { k } \lambda ^ { k } \mathbf { x } = q ( \lambda ) \mathbf { x } .
$$

(f) Let $A - \alpha I$ be nonsingular. Since $A \mathbf { x } = \lambda \mathbf { x }$ ,

$$
( A - \alpha I ) \mathbf { x } = A \mathbf { x } - \alpha I \mathbf { x } = \lambda \mathbf { x } - \alpha \mathbf { x } = ( \lambda - \alpha ) \mathbf { x } .
$$

Thus,

$$
{ \frac { 1 } { \lambda - \alpha } } \mathbf { x } = ( A - \alpha I ) ^ { - 1 } \mathbf { x } .
$$

16. Since $A ^ { t } A = A ^ { 2 }$ and $A \mathbf { x } = \lambda \mathbf { x }$ , we have $A ^ { 2 } \mathbf { x } = \lambda ^ { 2 } \mathbf { x }$ . Thus

$$
\rho \left( A ^ { t } A \right) = \rho \left( A ^ { 2 } \right) = \left[ \rho ( A ) \right] ^ { 2 } \quad { \mathrm { a n d } } \quad \| A \| _ { 2 } = \left[ \rho \left( A ^ { t } A \right) \right] ^ { \frac { 1 } { 2 } } = \rho ( A ) .
$$

17. (a) We have the real eigenvalue $\lambda = 1$ with the eigenvector $\mathbf { x } = ( 6 , 3 , 1 ) ^ { t }$ . (b) Choose any multiple of the vector $( 6 , 3 , 1 ) ^ { t }$ .

18. For

$$
A = { \left[ \begin{array} { l l } { 1 } & { 1 } \\ { 0 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } B = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 1 } & { 1 } \end{array} \right] } ,
$$

we have $\rho ( A ) = \rho ( B ) = 1$ and $\rho ( A + B ) = 3$ .

19. Let $A \mathbf { x } = \lambda \mathbf { x }$ . Then $\left| \lambda \right| \ \left\| \mathbf { x } \right\| = \left\| A \mathbf { x } \right\| \leq \left\| A \right\| \ \left\| \mathbf { x } \right\|$ , which implies $| \lambda | \leq \| A \|$ . Also, $( 1 / \lambda ) \mathbf { x } =$ $A ^ { - 1 } \mathbf { x }$ so $1 / | \lambda | \leq \| A ^ { - 1 } \|$ and $\| A ^ { - 1 } \| ^ { - 1 } \leq | \lambda |$ .

# Exercise Set 7.3, page 459

1. Two iterations of Jacobi’s method gives the following results.

\*(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 4 2 8 5 7 1 , - 0 . 3 5 7 1 4 2 9 , 0 . 4 2 8 5 7 1 4 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 7 , 0 . 9 1 , 0 . 7 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 6 5 , 1 . 6 5 , - 0 . 4 , - 2 . 4 7 5 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 3 2 5 , - 1 . 6 , 1 . 6 , 1 . 6 7 5 , 2 . 4 2 5 ) ^ { t }$

2. Two iterations of Jacobi’s method gives the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 2 5 0 0 0 0 0 , - 1 . 3 3 3 3 3 3 3 , 0 . 2 0 0 0 0 0 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 0 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 , - 1 . 3 3 3 3 3 3 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 2 0 8 3 3 3 , - 0 . 0 4 1 6 6 6 6 7 , - 0 . 2 1 6 6 6 6 7 , 0 . 4 1 6 6 6$ 667) $t$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 6 8 7 5 , 1 . 1 2 5 , 0 . 6 8 7 5 , 1 . 3 7 5 , 0 . 5 6 2 5 , 1 . 3 7 5 ) ^ { t }$

3. Two iterations of the Gauss-Seidel method give the following results.

\*(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 1 1 1 1 1 1 , - 0 . 2 2 2 2 2 2 2 , 0 . 6 1 9 0 4 7 6 ) ^ { i }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 7 9 , 0 . 9 4 9 5 , 0 . 7 8 9 9 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 , 2 . 6 4 , - 0 . 3 3 6 8 7 5 , - 2 . 2 6 7 3 7 5 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 1 8 9 0 6 3 , - 1 . 5 2 1 3 5 4 , 1 . 8 6 2 3 9 6 , 1 . 8 8 2 5 2 6 , 2 . 2 5 5 6 4 5 ) ^ { t }$

4. Two iterations of the Gauss-Seidel method give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 2 5 0 0 0 0 0 0 0 0 , - 0 . 9 1 6 6 6 6 6 6 6 7 , 0 . 0 6 6 6 6 6 6 6 6 6 6 6 6 ) ^ { \mathrm { {  u } } }$ t (b) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 6 6 6 6 6 6 6 6 6 7 , 1 . 3 3 3 3 3 3 3 3 4 , - 0 . 8 8 8 8 8 8 8 8 9 4 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 6 2 5 , 0 , - 0 . 2 2 5 , 0 . 6 1 6 6 6 6 7 ) ^ { t }$ (d) $\mathbf { x } ^ { ( z ) } = ( 0 . 6 8 7 5 , 1 . 5 4 6 8 7 5 , 0 . 7 9 2 9 6 8 8 , 1 . 7 1 8 7 5 , 0 . 7 2 2 6 5 6 3 , 1 . 8 7 8 9 0 6 ) ^ { t }$

5. Jacobi’s Algorithm gives the following results.

\*(a) ${ \bf x } ^ { ( 9 ) } = ( 0 . 0 3 5 1 0 0 7 9 , - 0 . 2 3 6 6 3 7 5 1 , 0 . 6 5 8 1 2 7 3 2 )$ t (b) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 9 9 5 7 2 5 0 , 0 . 9 5 7 7 7 5 0 , 0 . 7 9 1 4 5 0 0 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 1 ) } = ( - 0 . 7 9 7 1 0 5 8 1 , 2 . 7 9 5 1 7 0 6 7 , - 0 . 2 5 9 3 9 5 7 8 , - 2 . 2 5 1 7 9 2 9 9$ )t (d) $\mathbf { x } ^ { ( 1 2 ) } = ( 0 . 7 8 7 0 8 8 3 , - 1 . 0 0 3 0 3 6 , 1 . 8 6 6 0 4 8 , 1 . 9 1 2 4 4 9 , 1 . 9 8 5 7 0 7 ) ^ { t }$

6. Jacobi’s Algorithm gives the following results.

(a) $\mathbf { x } ^ { ( 1 0 ) } = ( 1 . 4 4 7 6 4 2 3 8 4 , - 0 . 8 3 5 5 6 4 7 8 8 2 , - 0 . 0 4 5 0 2 2 6 6 1 8 ) ^ { t }$   
(b) $\mathbf { x } ^ { ( 2 1 ) } = ( - 1 . 4 5 4 8 5 7 9 5 , 1 . 4 5 4 8 5 7 9 5 , - 0 . 7 2 7 0 4 3 9 6 ) ^ { t }$   
(c) $\mathbf { x } ^ { ( 1 2 ) } = ( - 0 . 7 5 2 0 5 5 9 9 , 0 . 0 4 0 2 7 0 2 8 , - 0 . 2 8 0 2 5 9 5 7 , 0 . 6 9 0 0 8 5 3 6 ) ^ { t }$   
(d) $\mathbf { x } ^ { ( 9 ) } = ( 0 . 3 5 7 0 5 5 6 6 , 1 . 4 2 8 5 2 8 8 3 , 0 . 3 5 7 0 5 5 6 6 , 1 . 5 7 1 4 1 1 1 3 , 0 . 2 8 5 5 2 2 4 6 , 1 . 5 7 1 4 1 1 1 1 3 , 0 . 2 7 8 7 5 0 9 , 0 . 1 7 7 1 4 1 1 1 1 3 )$ 3)t

7. The Gauss-Seidel Algorithm gives the following results.

\*(a) $\mathbf { x } ^ { ( 6 ) } = ( 0 . 0 3 5 3 5 1 0 7 , - 0 . 2 3 6 7 8 8 6 , 0 . 6 5 7 7 5 9 0 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 4 ) } = ( 0 . 9 9 5 7 4 7 5 , 0 . 9 5 7 8 7 3 8 , 0 . 7 9 1 5 7 4 8 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 7 9 6 9 1 4 7 6 , 2 . 7 9 4 6 1 8 2 7 , - 0 . 2 5 9 1 8 0 8 1 , - 2 . 2 5 1 8 3 6 1 6 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 7 ) } = ( 0 . 7 8 6 6 8 2 5 , - 1 . 0 0 2 7 1 9 , 1 . 8 6 6 2 8 3 , 1 . 9 1 2 5 6 2 , 1 . 9 8 9 7 9 0 ) ^ { t }$

8. The Gauss-Seidel Algorithm gives the following results.

(a) $\mathbf { x } ^ { ( 6 ) } = ( 1 . 4 4 7 8 1 6 3 5 0 , - 0 . 8 3 5 8 1 7 3 0 3 7 , - 0 . 0 4 4 7 9 9 6 1 8 6 ) ^ { i }$ $t$   
(b) $\mathbf { x } ^ { ( 8 ) } = ( - 1 . 4 5 4 8 0 4 2 0 , 1 . 4 5 4 4 1 3 1 6 , - 0 . 7 2 7 2 0 6 5 8 ) ^ { t }$   
(c) $\mathbf { \boldsymbol { x } } ^ { ( 8 ) } = ( - 0 . 7 5 3 1 7 6 3 , 0 . 0 4 1 0 1 0 4 9 , - 0 . 2 8 0 7 0 4 7 , 0 . 6 9 1 6 3 0 5 ) ^ { \circ }$ t   
(d) x(6) = (0.35713196, 1.42856598, 0.35714149, 1.57140350, 0.28570175, 1.57142544)t

9. (a)

$$
T _ { j } = \left[ \begin{array} { c c c } { { 0 } } & { { \frac { 1 } { 2 } } } & { { - \frac { 1 } { 2 } } } \\ { { - 1 } } & { { 0 } } & { { - 1 } } \\ { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { 0 } } \end{array} \right] \quad \mathrm { a n d } \quad \operatorname* { d e t } ( \lambda I - T _ { j } ) = \lambda ^ { 3 } + \frac { 5 } { 4 } x .
$$

Thus, the eigenvalues of $T _ { j }$ are $0$ and $\pm \frac { \sqrt { 5 } } { 2 } i$ , so $\rho ( T _ { j } ) = \frac { \sqrt { 5 } } { 2 } > 1$ .

(b) x(25) = (−20.827873, 2.0000000, −22.827873)t

(c)

$$
T _ { g } = \left[ \begin{array} { c c c } { { 0 } } & { { { \frac { 1 } { 2 } } } } & { { - { \frac { 1 } { 2 } } } } \\ { { 0 } } & { { { - \frac { 1 } { 2 } } } } & { { - { \frac { 1 } { 2 } } } } \\ { { 0 } } & { { 0 } } & { { - { \frac { 1 } { 2 } } } } \end{array} \right] \quad \mathrm { a n d } \quad \operatorname* { d e t } ( \lambda I - T _ { g } ) = \lambda \left( \lambda + \frac 1 2 \right) ^ { 2 } .
$$

Thus, the eigenvalues of $T _ { g }$ are 0, $- \frac 1 2$ , and $- \frac 1 2$ ; and $\rho ( T _ { g } ) = \frac { 1 } { 2 }$

(d) $\mathbf { x } ^ { ( 2 3 ) } = ( 1 . 0 0 0 0 0 2 3 , 1 . 9 9 9 9 9 7 5 , - 1 . 0 0 0 0 0 0 1 ) ^ { t }$ is within $1 0 ^ { - 5 }$ in the ${ \mathit { l } } _ { \infty }$ norm.

10. (a) $T _ { j } = \left[ { \begin{array} { c c c } { 0 } & { - 2 } & { 2 } \\ { - 1 } & { 0 } & { - 1 } \\ { - 2 } & { - 2 } & { 0 } \end{array} } \right]$ and $\operatorname* { d e t } ( \lambda I - T _ { j } ) = \lambda ^ { 3 }$ , so $\rho ( T _ { j } ) = 0$ . (b) $\mathbf { x } ^ { ( 4 ) } = ( 1 . 0 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 , - 1 . 0 0 0 0 0 0 0 0 ) ^ { t }$ is within $1 0 ^ { - 5 }$ in the $l _ { \infty }$ norm. (c) $T _ { g } = { \frac { \left[ 0 \mathrm { ~ ~ - 2 ~ ~ ~ } 2 \right] } { \left[ 0 \mathrm { ~ ~ ~ } 2 \right] } } \mathrm { ~ ~ a n d ~ } \operatorname* { d e t } ( \lambda I - T _ { g } ) = \lambda ( \lambda - 2 ) ^ { 2 } , \mathrm { ~ s ~ }$ o $\rho ( T _ { g } ) = 2$ .

$$
\mathbf { x } ^ { ( 2 5 ) } = \left( 1 . 3 0 \times 1 0 ^ { 9 } , - 1 . 3 2 5 \times 1 0 ^ { 9 } , 3 . 3 5 5 \times 1 0 ^ { 7 } \right) ^ { t }
$$

11. (a) $A$ is not strictly diagonally dominant.

(b)

$$
T _ { g } = \left[ { 0 \atop 0 } \ { 0 \atop 0 } \ { 0 . 7 5 } \right] \quad { \mathrm { a n d } } \quad \rho ( T _ { g } ) = 0 . 6 2 5 .
$$

Since $T _ { g }$ is convergent, the Gauss-Seidel method will converge.

(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , $\mathbf { x } ^ { ( 1 3 ) } = ( 0 . 8 9 7 5 1 3 1 0 , - 0 . 8 0 1 8 6 5 1 8 , 0 . 7 0 1 5 5 4 3 1 ) ^ { t }$

(d) $\rho ( T _ { g } ) = 1 . 3 7 5$ . Since $T _ { g }$ is not convergent, the Gauss-Seidel method will not converge

12. (a) $A$ is not strictly diagonally dominant.

(b) We have

$$
T _ { j } = \left[ \begin{array} { c c c } { { 0 } } & { { 0 } } & { { 1 } } \\ { { 0 . 5 } } & { { 0 } } & { { 0 . 2 5 } } \\ { { - 1 } } & { { 0 . 5 } } & { { 0 } } \end{array} \right] \quad \mathrm { a n d } \quad \rho ( T _ { j } ) = 0 . 9 7 2 1 0 5 2 1 .
$$

Since $T _ { j }$ is convergent, the Jacobi method will converge.

(c) With $\mathbf { x } ^ { ( 0 ) } = ( 0 , 0 , 0 ) ^ { t }$ , $\mathbf { x } ^ { ( 1 8 7 ) } = ( 0 . 9 0 2 2 2 6 5 5 , - 0 . 7 9 5 9 5 2 4 2 , 0 . 6 9 2 8 1 3 1 6 ) ^ { t }$

(d) $\rho ( T _ { j } ) = 1 . 3 9 3 3 1 7 7 9 3 7 1$ . Since $T _ { j }$ is not convergent, the Jacobi method will not converge.

13. (a) Subtract ${ \bf x } = T { \bf x } + { \bf c }$ from $\mathbf { x } ^ { ( k ) } = T \mathbf { x } ^ { ( k - 1 ) } + \mathbf { c }$ to obtain $\mathbf { x } ^ { ( k ) } - \mathbf { x } = T ( \mathbf { x } ^ { ( k - 1 ) } - \mathbf { x } )$ . Thus,

$$
\| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| \leq \| T \| \| \mathbf { x } ^ { ( k - 1 ) } - \mathbf { x } \| .
$$

Inductively, we have

$$
\| \mathbf { x } ^ { ( k ) } - \mathbf { x } \| \leq \| T \| ^ { k } \| \mathbf { x } ^ { ( 0 ) } - \mathbf { x } \| .
$$

The remainder of the proof is similar to the proof of Corollary 2.5.

(b) The last column has no entry when $| | T | | _ { \infty } = 1$ .

<table><tr><td></td><td>=x(2）- x|∞</td><td>|T|o</td><td>|T12 T|²x(0）- x| |/x(1）-x(|∞ 1-|IT|</td></tr><tr><td>1 (a)</td><td>0.22932</td><td>0.857143</td><td>0.48335</td></tr><tr><td>1 (b)</td><td>0.051579</td><td>0.3 0.089621</td><td>2.9388 0.11571</td></tr><tr><td>1 (c)</td><td>1.1453</td><td>0.9</td><td>2.2642 20.25</td></tr><tr><td>1 (d)</td><td>0.27511</td><td>1</td><td>0.75342</td></tr><tr><td>1(e)</td><td>0.59743</td><td>1</td><td>1.9897</td></tr><tr><td>1 (f)</td><td>0.875</td><td>0.75</td><td>1.125</td></tr></table>

\*14. The matrix $T _ { j } = \left( t _ { i k } \right)$ has entries given by

Since $A$ is strictly diagonally dominant, $\| T _ { j } \| _ { \infty } = \underset { 1 \leq i \leq n } { \operatorname* { m a x } } \sum _ { \stackrel { k = 1 } { k \neq i } } ^ { n } \left| \frac { a _ { i k } } { a _ { i i } } \right| < 1$ .

<table><tr><td></td><td>Jacobi 33 iterations</td><td>Gauss-Seidel 8 iterations</td><td></td><td>Jacobi 33 iterations</td><td>Gauss-Seidel 8 iterations</td></tr><tr><td>X1</td><td>1.53873501</td><td>1.53873270</td><td>X41</td><td>0.02185033</td><td>0.02184781</td></tr><tr><td>x2</td><td>0.73142167</td><td>0.73141966</td><td>X42</td><td>0.02133203</td><td>0.02132965</td></tr><tr><td>x3</td><td>0.10797136</td><td>0.10796931</td><td>X43</td><td>0.02083782</td><td>0.02083545</td></tr><tr><td>X4</td><td>0.17328530</td><td>0.17328340</td><td>X44</td><td>0.02036585</td><td>0.02036360</td></tr><tr><td>X5</td><td>0.04055865</td><td>0.04055595</td><td>X45</td><td>0.01991483</td><td>0.01991261</td></tr><tr><td>X6</td><td>0.08525019</td><td>0.08524787</td><td>X46</td><td>0.01948325</td><td>0.01948113</td></tr><tr><td>X7</td><td>0.16645040</td><td>0.16644711</td><td>X47</td><td>0.01907002</td><td>0.01906793</td></tr><tr><td>x8</td><td>0.12198156</td><td>0.12197878</td><td>X48</td><td>0.01867387</td><td>0.01867187</td></tr><tr><td>x9</td><td>0.10125265</td><td>0.10124911</td><td>X49</td><td>0.01829386</td><td>0.01829190</td></tr><tr><td>X10</td><td>0.09045966</td><td>0.09045662</td><td>x50</td><td>0.71792896</td><td>0.01792707</td></tr><tr><td>X11</td><td>0.07203172</td><td>0.07202785</td><td>X51</td><td>0.01757833</td><td>0.01757648</td></tr><tr><td>X12</td><td>0.07026597</td><td>0.07026266</td><td>X52</td><td>0.01724113</td><td>0.01723933</td></tr><tr><td>X13</td><td>0.06875835</td><td>0.06875421</td><td>X53</td><td>0.01691660</td><td>0.01691487</td></tr><tr><td>X14</td><td>0.06324659</td><td>0.06324307</td><td>X54</td><td>0.01660406</td><td>0.01660237</td></tr><tr><td>X15</td><td>0.05971510</td><td>0.05971083</td><td>X55</td><td>0.01630279</td><td>0.01630127</td></tr><tr><td>X16</td><td>0.05571199</td><td>0.05570834</td><td>X56</td><td>0.01601230</td><td>0.01601082</td></tr><tr><td>X17</td><td>0.05187851</td><td>0.05187416</td><td>X57</td><td>0.01573198</td><td>0.01573087</td></tr><tr><td>X18</td><td>0.04924911</td><td>0.04924537</td><td>X58</td><td>0.01546129</td><td>0.01546020</td></tr><tr><td>X19</td><td>0.04678213</td><td>0.04677776</td><td>X59</td><td>0.01519990</td><td>0.01519909</td></tr><tr><td>X20</td><td>0.04448679</td><td>0.04448303</td><td>X60</td><td>0.01494704</td><td>0.01494626</td></tr><tr><td>X21</td><td>0.04246924</td><td>0.04246493</td><td>X61</td><td>0.01470181</td><td>0.01470085</td></tr><tr><td>X22</td><td>0.04053818</td><td>0.04053444</td><td>X62</td><td>0.01446510</td><td>0.01446417</td></tr><tr><td>X23</td><td>0.03877273</td><td>0.03876852</td><td>X63</td><td>0.01423556</td><td>0.01423437</td></tr><tr><td>X24</td><td>0.03718190</td><td>0.03717822</td><td>X64</td><td>0.01401350</td><td>0.01401233</td></tr><tr><td>X25</td><td>0.03570858</td><td>0.03570451</td><td>X65</td><td>0.01380328</td><td>0.01380234</td></tr><tr><td>X26</td><td>0.03435107</td><td>0.03434748</td><td>X66</td><td>0.01359448</td><td>0.01359356</td></tr><tr><td>X27</td><td>0.03309542</td><td>0.03309152</td><td>X67</td><td>0.01338495</td><td>0.01338434</td></tr><tr><td>X28</td><td>0.03192212</td><td>0.03191866</td><td>X68</td><td>0.01318840</td><td>0.01318780</td></tr><tr><td>X29</td><td>0.03083007</td><td>0.03082637</td><td>X69</td><td>0.01297174</td><td>0.01297109</td></tr><tr><td>X30</td><td>0.02980997</td><td>0.02980666</td><td>X70</td><td>0.01278663</td><td>0.01278598</td></tr><tr><td>X31</td><td>0.02885510</td><td>0.02885160</td><td>X71</td><td>0.01270328</td><td>0.01270263</td></tr><tr><td>x32</td><td>0.02795937</td><td>0.02795621</td><td>72</td><td>0.01252719</td><td>0.01252656</td></tr><tr><td>X33</td><td>0.02711787</td><td>0.02711458</td><td>X73</td><td>0.01237700</td><td>0.01237656</td></tr><tr><td>x34</td><td>0.02632478</td><td>0.02632179</td><td>X74</td><td>0.01221009</td><td>0.01220965</td></tr><tr><td>X35</td><td>0.02557705</td><td>0.02557397</td><td>75</td><td>0.01129043</td><td>0.01129009</td></tr><tr><td>X36</td><td>0.02487017</td><td>0.02486733</td><td>X76</td><td>0.01114138</td><td>0.01114104</td></tr><tr><td>X37</td><td>0.02420147</td><td>0.02419858</td><td>77</td><td>0.01217337</td><td>0.01217312</td></tr><tr><td>x38</td><td>0.02356750</td><td>0.02356482</td><td>X78</td><td>0.01201771</td><td>0.01201746</td></tr><tr><td>X39</td><td>0.02296603</td><td>0.02296333</td><td>X79</td><td>0.01542910</td><td>0.01542896</td></tr><tr><td>X40</td><td>0.02239424</td><td>0.02239171</td><td>X80</td><td>0.01523810</td><td>0.01523796</td></tr></table>

16. (a) We have $P _ { 0 } = 1$ , so the equation $P _ { 1 } = { \textstyle \frac { 1 } { 2 } } P _ { 0 } + { \textstyle \frac { 1 } { 2 } } P _ { 2 }$ gives $\begin{array} { r } { P _ { 1 } - \frac { 1 } { 2 } P _ { 2 } = \frac { 1 } { 2 } } \end{array}$ . Since $P _ { i } =$ $\textstyle { \frac { 1 } { 2 } } P _ { i - 1 } + { \frac { 1 } { 2 } } P _ { i + 1 }$ , we have $\begin{array} { r } { - \frac { 1 } { 2 } P _ { i - 1 } + P _ { i } - \frac { 1 } { 2 } \mathbf { \bar { \mathit { P } } } _ { i + 1 } = \bar { \mathbf { \mathit { 0 } } } } \end{array}$ , for $i = 2 , \ldots , n - 2$ 2 . Finally, since $P _ { n } = 0$ 2 and $P _ { n - 1 } = { \textstyle { \frac { 1 } { 2 } } } P _ { n - 2 } + { \textstyle { \frac { 1 } { 2 } } } P _ { n }$ 2, we have $- { \textstyle \frac { 1 } { 2 } } P _ { n - 2 } + P _ { n - 1 } = 0$ . This gives the linear system.

(b) The solution vector is $( 0 . 8 9 9 9 6 4 3 1 , 0 . 7 9 9 9 3 5 4 4 , 0 . 6 9 9 9 1 5 4 9 , 0 . 5 9 9 9 0 5 5 2 , 0 . 4 9 9 9 0 5 5 2$ , 0.39991454, 0.29993086, 0.19995223, 0.09997611)t, using 86 iterations with a tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in $l _ { \infty }$ with the Gauss-Seidel method.

The solution vector $\mathrm { 1 S \ ( 0 . 9 6 \dot { 2 } S \times 9 / ( 4 , 0 . 9 2 5 9 9 5 ) 2 7 , 0 . 8 8 9 2 \dot { 2 } ) 0 4 2 , 0 . 8 5 2 8 9 8 9 } / , \ 0 . 8 1 6 \times 5 4 2 7 0 9 2$ , $) , \langle | { \mathrm { S } } { \mathrm { 1 } } 3 5 0 0 \rangle / 2 , \{ \mathrm { 0 } . { \cdot } { \mathrm { ( 4 6 2 8 3 4 0 , 0 ) } } { \mathrm { , ~ 0 } } { \mathrm { . ~ ( 1 . 8 4 / 9 8 , 0 . 6 / 8 0 5 9 / 9 , 0 . 6 2 4 9 / 4 2 1 , 0 . 6 1 2 0 4 2 0 0 , 0 . 5 8 1 1 0 9 5 ) } }$ , $9 . 9 5 0 9 4 1 8 0 1 , 0 . 5 3 2 5 0 9 0 9 4 0 1 1 , 0 . 4 9 2 1 0 9 9 9 1 0 0 , 0 . 4 0 9 3 ( 2 9 9 4 9 , 0 . 4 3 0 0 \ ( \mathrm { ~ 1 ~ } 0 . 9 ) , 0 . 4 1 0 0 \ ( 9 4 4 , 0 . 3 8 5 0 2 ( 0 . 1 0 ) )$ , 0.36156768, 0.33850391, 0.31643400, 0.29535198, 0.27524791, 0.25610805, 0.23791514, 0.22064859, 0.20428475, 0.18879715, 0.17415669, 0.16033195, 0.14728936, 0.13499341, 0.12340690, 0.11249111, 0.10220596, 0.09251023, 0.08336165, 0.07471709, 0.06653267, 0.05876386, 0.05136562, 0.04429243, 0.03749843, 0.03093747, 0.02456315, 0.01832893, 0.01218814, 0.00609407)t, using 231 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in ${ \mathit { l } } _ { \infty }$ with the Gauss-Seidel method.

The solution vector is $( 0 . 9 6 3 0 5 8 5 4 , 0 . 9 2 6 2 7 4 9 4 , 0 . 8 8 9 7 2 6 1 3 , 0 . 8 5 3 4 8 7 0 6 , 0 . 8 1 7 6 3 0 ^ { \circ } 2 6 0 9 8 8 9 8 8 0 ^ { \circ } )$ , 0.78222543, 0.74733909, 0.71303418, $\mathrm { 0 . 6 \mathord { \left/ { \vphantom { 0 . 6 \mathrm { 0 . 6 9 3 6 9 8 3 } } } \right. \kern - delimiterspace } 0 . 6 \mathrm { 0 . 6 4 6 4 0 1 0 1 , 0 . 6 1 4 1 / \mathrm { 8 4 1 } } , 0 . \mathrm { . 0 8 2 / 4 8 1 6 } }$ , $0 . 3 9 3 2 1 3 1 ( 8 , 0 . 3 2 2 4 2 0 0 1 2 , 0 . 4 9 3 9 0 1 2 8 ( , 0 . 4 0 5 ) ( 1 9 9 3 0 ) , 0 . 4 3 8 ( 0 8 3 2 , 0 . 4 1 2 ( 9 1 0 1 , 0 . 3 8 ( 8 0 8 0 8 )$ , $0 . 3 0 0 3 8 1 1 9 0 , 0 . 3 4 0 8 1 1 4 , 0 . 3 1 8 8 8 1 0 4 2 , 0 . 2 9 9 ( \mathrm { \it ~ ( 9 4 0 8 ) . 0 2 ~ ( 1 ~ 0 . 0 6 8 ) . 0 2 0 8 ( \mathrm { \it ~ 1 3 3 3 8 , 0 . 2 4 0 0 2 0 1 4 } ) }$ , 0.22346997, 0.20724328, 0.19191807, 0.17747025, 0.16387393, 0.15110162, 0.13912457, 0.12791297, 0.11743622, 0.10766312, 0.09856216, 0.09010163, 0.08224988, 0.07497547, 0.06824731, 0.06203481, 0.05630801, 0.05103770, 0.04619548, 0.04175387, 0.03768638, 0.03396754, 0.03057293, 0.02747926, 0.02466435, 0.02210715, 0.01978772, 0.01768725, $0 . 0 1 5 7 8 8 0 6 , 0 . 0 1 4 0 7 3 5 0 , 0 . 0 1 2 5 2 8 0 3 , 0 . 0 1 1 1 3 7 1 0 , 0 . 0 0 9 8 8 ^ { \prime } 1 8 , 0 . 0 0 8 7 6 5 6 8 , 0 . 0 0 7 7 6 0 9 9 2 , 0 . 0 0 9 8 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 8 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime } 2 8 0 ^ { \prime }$ $0 . 0 0 6 8 6 2 1 0 , 0 . 0 0 6 0 5 9 2 6 , 0 . 0 0 5 3 4 3 2 1 , 0 . 0 0 4 7 0 5 5 2 , 0 . 0 0 4 1 3 8 4 4 , 0 . 0 0 3 6 3 4 9 0 , 0 . 0 0 3 1 8 8 4 2 ,$ $0 . 1 0 0 2 d ( 9 3 \bot \mathrm { Z } , \mathrm  0 . 1 0 0 2 4 4 3 6 3 , 0 . 0 0 2 1 . 3 9 0 9 , 0 . 0 0 1 8 0 3 6 0 8 , 0 . 0 0 1 6 0 2 3 0 2 , 0 . 0 0 1 4 1 3 1 , 0 . 0 0 1 2 2 8 3 1 , 0 . 0 0 0 2 6 2 2 6 3 6 0 8 , 0 . 0 0 0 2 2 6 1 2 8 0 2 , 0 . 0 0 0 2 2 6 2 8 2 8 2 8 0 2 8 , 0 . 0 0 0 2 2 2 6 2 8 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0 2 8 0$ , $9 . 0 0 1 1 0 6 6 3 5 0 , 0 . 0 0 0 9 2 4 4 / \ , 0 . 0 0 0 8 0 0 4 / \ , 0 . 0 0 0 0 6 9 2 2 1 , 0 . 0 0 0 0 3 9 7 8 1 , 0 . 0 0 0 0 3 1 3 6 0 0 , 0 . 0 0 0 0 4 4 4 0 9$ , $0 . 0 0 0 3 8 \mathrm { { L } 9 7 } , 0 . 0 0 0 0 3 3 2 8 0 6 6 , 0 . 0 0 0 0 0 2 8 \mathrm { { L } 3 2 } , 0 . 0 0 0 0 2 4 0 8 2 , 0 . 0 0 0 0 2 0 5 7 5 , 0 . 0 0 0 1 7 5 3 9 , 0 . 0 0 0 1 4 9 0 9 .$ 0.00012629, 0.00010648, 0.00008920, 0.00007405, 0.00006067, 0.00004871, 0.00003787, $0 . 0 0 0 0 2 7 8 6 , 0 . 0 0 0 0 1 8 3 9 , 0 . 0 0 0 0 0 9 1 9 ) ^ { u }$ , using 233 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in $l _ { \infty }$ norm with the Gauss-Seidel method.

(c) The equations are $P _ { i } = \alpha P _ { i - 1 } + ( 1 - \alpha ) P _ { i + 1 }$ , for $i = 1 , 2 , \ldots , n - 1$ , and the linear system becomes

$$
{ \left[ \begin{array} { l l l l l } { 1 } & { \alpha - 1 } & { 0 } & { \cdots } & { 0 } \\ { - \alpha } & { 1 } & { \alpha - 1 } & { \ddots } & { \vdots } \\ { 0 } & { - \alpha } & { \ddots } & { \ddots } & { 0 } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & { \alpha - 1 } \\ { 0 } & { \cdots } & { 0 } & { - \alpha } & { 1 } \end{array} \right] } \quad { \left[ \begin{array} { l } { P _ { 1 } } \\ { P _ { 2 } } \\ { \vdots } \\ { \vdots } \\ { P _ { n - 1 } } \end{array} \right] } = { \left[ \begin{array} { l } { \alpha } \\ { 0 } \\ { \vdots } \\ { \vdots } \\ { 0 } \end{array} \right] }
$$

(d) The solution vector is (0.49947985, 0.24922901, 0.12411164, 0.06155895, 0.03028662, 0.01465286, 0.00683728, 0.00293009, 0.00097670)t, using 35 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in ${ \mathit { l } } _ { \infty }$ norm with the Gauss-Seidel method. The solution vector is $( 4 . 9 9 9 5 3 2 8 \times 1 0 ^ { - 1 } , 2 . 4 9 9 3 9 6 7 \times 1 0 ^ { - 1 } , 1 . 2 4 9 4$ $1 . 2 4 9 4 2 1 5 \times 1 0 ^ { - 1 }$ , $6 . 2 4 5 1 1 7 2 \times 1 0 ^ { - 2 } .$ $, 3 . 1 2 1 1 7 1 9 \times 1 0 ^ { - 2 } , 1 . 5 5 9 6 4 4 8 \times 1 0 ^ { - 2 } , 7 . 7 9 1 9 7 5 7 \times 1 0 ^ { - 3 } , 3 . 8 9 1 9 1 9 3 \times 1 0 ^ { - 3 } , 2 . 7 9 1 4 9 5 7 \times 1 0 ^ { - 2 }$

$1 . 9 4 3 3 5 5 6 \times 1 0 ^ { - 3 } , 9 . 7 0 0 3 6 7 3 \times 1 0 ^ { - 4 } , 4 . 8 3 9 9 8 7 6 \times 1 0 ^ { - 4 } , 2 . 4 1 3 7 4 1 5 \times 1 0 ^ { - 4 } , 1 . 2 0 3 0 8 3 2 \times 1 0 ^ { - 4 } ,$ $5 . 9 9 2 7 3 2 1 \times 1 0 ^ { - 5 } , 2 . 9 8 2 9 2 6 0 \times 1 0 ^ { - 5 } , 1 . 4 8 3 5 8 0 3 \times 1 0 ^ { - 5 } , 7 . 3 7 2 1 1 4 0 \times 1 0 ^ { - 6 } , 3 . 6 5 9 7 0 3 7 \times 1 0 ^ { - 6 } . 9 9 9 6 0 0 0 0 0 0 0 0 0 0 0 ,$ $1 . 8 1 4 8 1 6 7 \times 1 0 ^ { - 6 }$ $\mathrm { , 8 . 9 8 9 0 2 2 9 \times 1 0 ^ { - 7 } , 4 . 4 4 6 7 7 5 2 \times 1 0 ^ { - 7 } , }$ $7 7 5 2 \times 1 0 ^ { - 7 } , 2 . 1 9 6 8 0 4 8 \times 1 0 ^ { - 7 } , 1 . 0 8 3 7 0 9 3 \times 1 0 ^ { - \cdot }$ 7, $3 7 9 1 6 5 \times 1 0 ^ { - \circ } , 2 . 6 2 5 0 1 7 7 \times 1 0 ^ { - \circ } , 1 . 2 8 8 7 2 3 3 2 \times 1 0 ^ { - \circ } , 6 . 3 1 5 6 9 5 3 \times 1 0 ^ { - \circ } , 3 . 0 8 9 4 8 2 9 \times 1 0 ^ { - \circ } ,$ 1.5084 $2 7 7 \times 1 0 ^ { - 9 } , 7 . 3 5 0 3 8 7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 }$ $7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 } , 1 . 7 3 4 7 0 3 5 \times 1 0 ^ { - 1 0 } ,$ $\mathrm { 3 2 } \times 1 0 ^ { - 1 0 } , \mathrm { 1 . 7 3 4 7 0 3 5 } \times 1 0 ^ { - 1 0 } , \mathrm { 8 . 4 0 0 6 1 0 5 } \times 1 0 ^ { - 1 1 } ,$ $4 . 0 5 9 3 4 7 0 { \times } 1 0 ^ { - 1 1 }$ $4 7 0 \times 1 0 ^ { - 1 1 } , 1 . 9 5 7 2 4 1 8 \times 1 0 ^ { - 1 1 } , 9 . 4 1 5 8 7 9 8 \times 1 0 ^ { - 1 1 }$ $1 1 8 \times 1 0 ^ { - 1 1 } , 9 . 4 1 5 8 7 9 8 \times 1 0 ^ { - 1 2 } , 4 . 5 1 9 5 1 9 7 \times 1 0 ^ { - 1 2 }$ $9 8 \times 1 0 ^ { - 1 2 } , 4 . 5 1 9 5 1 9 7 \times 1 0 ^ { - 1 2 } , 2 . 1 6 4 3 4 6 5 \times 1 0 ^ { - 1 2 }$ , $1 . 0 3 4 0 7 7 0 \times 1 0 ^ { - 1 2 } , 4 . 9 2 8 9 7 5 7 \times 1 0 ^ { - 1 3 } , 2 . 3 4 3 7 6 7$ $7 { \times } 1 0 ^ { - 1 3 } , 2 . 3 4 3 7 6 7 7 { \times } 1 0 ^ { - 1 3 } , 1 . 1 1 1 6 6 4 4 { \times } 1 0 ^ { - 1 3 } ,$ 5.2577488 10−14, $2 . 4 7 7 6 5 0 9 \times 1 0 ^ { - 1 4 } , 1 . 1 6 0 8 1 9 0 \times 1 0 ^ { - 1 4 } , 5 . 3 7 6 7 4 5 8 \times 1 0 ^ { - 1 5 } , 2 . 4 2 4 9 9 7 7 \times 1 0 ^ { - 1 5 } , 1 . 0 1 9 2 4 8 9 \times 1 0 ^ { - 1 5 } .$ $3 . 3 9 7 4 9 6 5 \times 1 0 ^ { - 1 6 } ) ^ { t }$ , using 40 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in $l _ { \infty }$ norm with the Gauss-Seidel method. The solution $\mathrm { \ v e c t o r ~ i s ~ ( 4 . 9 9 9 5 3 2 8 \times 1 0 ^ { - 1 } , 2 . 4 9 9 3 9 6 7 \times 1 0 ^ { - 1 } , 1 . 2 4 9 4 2 1 5 \times 1 0 ^ { - 1 } , }$ $6 . 2 4 5 1 1 7 2 \times 1 0 ^ { - 2 } , 3 . 1 2 1 1 7 1 9 \times 1 0 ^ { - 2 } , 1 . 5 5 9 6 4 4 8 \times 1 0 ^ { - 2 } , 7 . 7 9 1 9 7 5 7 \times 1 0 ^ { - 3 } , 3 . 8 9 1 9 1 9 3 9 8 8 8 7 8 8 7 8 7 8 7 8 7 8 8 7 8$ 3, $1 . 9 4 3 3 5 5 6 \times 1 0 ^ { - 3 }$ $, 9 . 7 0 0 3 6 7 3 \times 1 0 ^ { - 4 } , 4 . 8 3 9 9 8 7 6 \times 1 0 ^ { - 4 } , 2 . 4 1 3 7 4 1 5 \times 1 0 ^ { - 4 } , 1 . 2 0 3 0 8 3 2 \times 1 0 ^ { - 4 }$ , $5 . 9 9 2 7 3 2 1 \times 1 0 ^ { - 5 }$ $\times 1 0 ~ ^ { \circ } , 2 . 9 8 \angle 9 2 0 0 \times 1 0 ~ ^ { \circ } , 1 . 4 8 . 3 0 8 0 3 \times 1 0 ~ ^ { \circ } , ( . 3 ( \bar { \cal Z } 1 1 4 0 \times 1 0 ~ ^ { \circ } , 3 . 0 3 9 ( 0 3 i \times 1 0 ~ ^ { \circ }$ , $1 . 8 1 4 8 1 6 7 \times 1 0 ^ { - 6 }$ , $8 . 9 8 9 0 2 2 9 \times 1 0 ^ { - 7 } , 4 . 4 4 6 7 7 5 2 \times 1 0 ^ { - 7 } , 2 . 1 9 6 8 0 4 8 \times$ $7 7 5 2 \times 1 0 ^ { - 7 } , 2 . 1 9 6 8 0 4 8 \times 1 0 ^ { - 7 } , 1 . 0 8 3 7 0 9 3 \times 1 0 ^ { - 1 }$ 7, $5 . 3 3 7 9 1 6 5 \times 1 0 ^ { - 8 }$ , $2 . 6 2 5 0 1 7 7 \times 1 0 ^ { - 8 } , 1 . 2 8 8 7 2 3 2 \times 1 0 ^ { - 8 } , 6 . 3 1 5 6 9 5 3 \times$ $7 2 3 2 \times 1 0 ^ { - 8 } , 6 . 3 1 5 6 9 5 3 \times 1 0 ^ { - 9 } , 3 . 0 8 9 4 8 2 9 \times 1 0 ^ { - 9 }$ 9, $\in \Omega \odot 4 . 9 7 7 \ddots 1 \Omega - 9 ^ { ' } 7 \phantom { ' } \supset \Omega \odot 9 . 9 7 \phantom { ' } \rho \sim \cdot 1 \ : \Omega - 1 0 ^ { - 1 } \phantom { ' } 0 \succeq \succeq 7 . 4 \succeq \sigma \odot 9 . \hdots 1 \Omega - 1 0 ^ { - 1 } 1 \phantom { ' } 1 \quad \tau \circ 4 . 7 \ 0 \Omega \succeq \zeta \hdots 1 \Omega - 1 0 ^ { - 1 } \phantom { ' } 0 \phantom { ' } \odot 4 . 0 0 \sigma + \Omega \in \Omega \times \hdots 1 \Omega - 1 1$ $1 . 5 0 8 4 2 7 7 \times 1 0 ^ { - 9 }$ $7 7 \times 1 0 ^ { - 9 } , 7 . 3 5 0 3 8 7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 }$ $7 6 \times 1 0 ^ { - 1 0 } , 3 . 5 7 4 5 2 3 2 \times 1 0 ^ { - 1 0 } , 1 . 7 3 4 7 0 3 5 \times 1 0 ^ { - 1 0 } ,$ $\mathrm { 5 2 } \times 1 0 ^ { - 1 0 } , \mathrm { 1 . 7 3 4 7 0 3 5 } \times \mathrm { 1 0 ^ { - 1 0 } , 8 . 4 0 0 6 1 0 6 } \times \mathrm { 1 0 ^ { - 1 1 } } .$ $4 . 0 5 9 3 4 7 2 \times 1 0 ^ { - 1 1 } , 1 . 9 5 7 2 4 2 1 \times 1 0 ^ { - 1 1 } , 9 . 4 1 5 8 8 4 8 \times 1 0 ^ { - 1 2 } , 4 . 5 1 9 5 2 7 5 \times 1 0 ^ { - 1 2 } , 2 . 1 9 5 2 6 2 1 \times 1 0 ^ { - 1 2 } , 2 . 2 7 6 2 6 2 1 \times 1 0 ^ { - 1 2 } , 2 . 2 7 6 2 2 6 2 1$ $, 4 . 5 1 9 5 2 7 5 \times 1 0 ^ { - 1 2 } , 2 . 1 6 4 3 5 8 1 \times 1 0 ^ { - 1 2 }$ , $0 3 4 0 9 4 0 \times 1 0 ^ { - 1 2 } , 4 . 9 2 9 2 1 6 7 \times 1 0 ^ { - 1 9 } , 2 . 3 4 4 1 0 2 5 \times 1 0 ^ { - 1 9 } , 1 . 1 1 2 1 1 8 9 \times 1 0 ^ { - 1 9 } , 5 . 2 6 3 7 8 7 7 \times 1 0 ^ { - 1 9 } , 9 . 9 9 9 8 8 8 8 , 1 . 2 7 6 7 8 7 8$ 2.4855 $1 1 6 \times 1 0 ^ { - 1 4 } , 1 . 1 7 0 8 5 3 2 \times 1 0 ^ { - 1 4 } , 5 . 5 0 2 4 7 8 9 \times 1 0 ^ { - 1 }$ $2 \times 1 0 ^ { - 1 4 } , 5 . 5 0 2 4 7 8 9 \times 1 0 ^ { - 1 5 } , 2 . 5 7 9 7 9 1 5 \times 1 0 ^ { - 1 5 } ,$ $\mathrm { 8 9 \times 1 0 ^ { - 1 5 } , 2 . 5 7 9 7 9 1 5 \times 1 0 ^ { - 1 5 } , 1 . 2 0 6 6 5 4 9 \times 1 0 ^ { - 1 5 } }$ , $5 . 6 3 0 6 2 4 1 \times 1 0 ^ { - 1 6 } , 2 . 6 2 1 2 5 0 5 \times 1 0 ^ { - 1 6 } , 1 . 2 1 7 4 2 8$ $\mathrm { \dot { 0 } 5 } \times 1 0 ^ { - 1 6 } , 1 . 2 1 7 4 2 8 1 \times 1 0 ^ { - 1 6 } , 5 . 6 4 1 1 2 4 9 \times 1 0 ^ { - 1 7 }$ $\mathbf { 8 1 } \times 1 0 ^ { - 1 6 } , 5 . 6 4 1 1 2 4 9 \times 1 0 ^ { - 1 7 } , 2 . 6 0 7 8 4 1 5 \times 1 0 ^ { - 1 7 }$ , $1 . 2 0 2 8 0 6 3 \times 1 0 ^ { - 1 4 } , 5 . 5 3 4 9 7 4 3 \times 1 0 ^ { - 1 8 } , 2 . 5 4 1 2 5 2 2 \times 1 0 ^ { - 1 8 } , 1 . 1 6 4 1 2 4 3 \times 1 0 ^ { - 1 8 } , 5 . 5 3 4 2 5 6 0 , 0 . 1 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 2 . 2 2 6 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 2 . 2 2 6 2 2 6 2 \times 1 0 ^ { - 1 8 } , 0 . 1 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 0 . 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 0 . 2 2 6 2 2 \times 1 0 ^ { - 1 8 } , 0 . 2 2 6 2 8$ $( 2 2 \times 1 0 ^ { - 1 8 } , 1 . 1 6 4 1 2 4 3 \times 1 0 ^ { - 1 8 } , 5 . 3 2 0 8 1 2 0 \times 1 0 ^ { - 1 9 }$ , $2 . 4 2 6 5 6 0 9 \times 1 0 ^ { - 1 9 } , 1 . 1 0 4 1 9 8 8 \times 1 0 ^ { - 1 9 } , 5 . 0 1 3 6 5 4 8 \times 1 0 ^ { - 2 0 } , 2 . 2 7 1 5 4 3 6 \times 1 0 ^ { - 2 0 } , 1 . 0 2 6 9 6 5 5 \times 1 0 ^ { - 2 0 } ,$ $4 . 6 3 3 0 5 5 2 { \times } 1 0 ^ { - 2 1 } , 2 . 0 8 5 7 6 2 3 { \times } 1 0 ^ { - 2 1 } , 9 . 3 7 0 3 7 1$ $\}$ $1 5 \times 1 0 ^ { - 2 2 } , 4 . 2 0 0 9 9 7 8 \times 1 0 ^ { - 2 2 } , 1 . 8 7 9 5 8 0 0 \times 1 0 ^ { - 2 2 }$ , 8.3924 $9 3 3 \times 1 0 ^ { - 2 3 } , 3 . 7 3 9 8 3 2 0 \times 1 0 ^ { - 2 3 } , 1 . 6 6 3 2 3 3 5 \times 1 0 ^ { - 2 }$ $3 2 0 \times 1 0 ^ { - 2 3 } , 1 . 6 6 3 2 3 3 5 \times 1 0 ^ { - 2 3 } , 7 . 3 8 2 5 0 0 9 \times 1 0 ^ { - 2 4 }$ $3 5 \times 1 0 ^ { - 2 3 } , 7 . 3 8 2 5 0 0 9 \times 1 0 ^ { - 2 4 } , 3 . 2 7 0 4 8 4 0 \times 1 0 ^ { - 2 4 }$ , $1 . 4 4 6 0 6 5 2 { \times } 1 0 ^ { - 2 4 } , 6 . 3 8 1 7 5 3 7 { \times } 1 0 ^ { - 2 5 } , 2 . 8 1 1 1 0 8$ $A A \in \cap \theta C 5 < 9 < 1 0 - 2 4 < 6 . 9 8 1 7 5 < 2 7 < 1 0 - 2 5 < 2 8 1 1 1 0 8 1 < 1 0 ^ { - 2 5 } 1 9 3 5 0 7 7 2 0 < 1 0 ^ { - 2 5 } < 4 9 . 4 2 0 6 A < 1 0 ^ { - 2 6 }$ $7 \times 1 0 ^ { - 2 5 } , 2 . 8 1 1 1 0 8 1 \times 1 0 ^ { - 2 5 } , 1 . 2 3 5 9 7 3 9 \times 1 0 ^ { - 2 5 } ,$ $5 . 4 2 4 3 0 6 4 \times 1 0 ^ { - 2 6 }$ $2 . 3 7 6 2 4 4 3 \times 1 0 ^ { - 2 6 } , 1 . 0 3 9 1 0 3 1 \times 1 0 ^ { - 2 6 } , 4 . 5 3 5 8 1 7 9 \times 1 0 ^ { - 2 \prime } , 1 . 9 7 6 4 7 1 4 \times 1 0 ^ { - 2 \prime } , 8 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 2 \prime } , 9 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 2 \prime } , 9 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 2 \prime } , 1 . 9 7 6 2 4 1 8 \times 1 0 ^ { - 3 \prime } .$ $8 . 5 9 7 4 9 5 6 \times 1 0 ^ { - 2 8 }$ , $3 . 7 3 3 4 3 2 6 \times 1 0 ^ { - 2 8 } , 1 . 6 1 8 4 8 2 3 \times 1 0 ^ { - 2 8 } , 7 . 0 0 4 5 3 1 9 \times 1 0 ^ { - 2 9 } , 3 . 0 2 6 4 2 5 5 \times 1 0 ^ { - 2 9 } , 1 . 0 2 6 8 4 8 2 5 2 6 \times 1 0 ^ { - 2 9 } , 2 . 0 2 6 8 4 8 2 5 8 8 8 1 9 \times 1 0 ^ { - 2 9 } , 2 . 0 2 6 8 4 8 2 5 8 8 1 9 \times 1 0 ^ { - 2 9 } , 3 . 0 2 8 4 8 2 4 9 6 2 5 8 8 1 9 \times 1 0 ^ { - 2 9 } , 2 . 0 2 8 4 8 2 4 9 6 2 5 8 1 9 \times 1 0 ^ { - 2 9 } , 3 . 0 2 8 4 8 2 4 8 2 8 8 8 1 9 8 2 8 8 1$ $1 . 3 0 5 4 7 5 3 \times 1 0 ^ { - 2 9 }$ , $5 . 6 2 2 1 5 7 7 \times 1 0 ^ { - 3 0 }$ $5 7 7 \times 1 0 ^ { - 3 0 } , 2 . 4 1 7 3 5 7 3 \times 1 0 ^ { - 3 0 } , 1 . 0 3 7 7 4 1 4 \times 1 0 ^ { - 3 6 }$ $5 7 3 \times 1 0 ^ { - 3 0 } , 1 . 0 3 7 7 4 1 4 \times 1 0 ^ { - 3 0 } , 4 . 4 4 7 8 7 2 6 \times 1 0 ^ { - 3 1 }$ $\cdot 1 4 \times 1 0 ^ { - 3 0 } , 4 . 4 4 7 8 7 2 6 \times 1 0 ^ { - 3 1 } , 1 . 9 0 3 3 7 5 1 \times 1 0 ^ { - 3 1 }$ , 8. $. 1 3 1 2 4 5 3 \times 1 0 ^ { - 3 2 } , 3 . 4 6 6 0 5 1 3 \times 1 0 ^ { - 3 2 } , 1 . 4 7 1 2 6 6 5 \times 1 0 ^ { - 3 2 } , 6 . 1 7 0 7 3 2 5 \times 1 0 ^ { - 3 3 } , 2 . 4 7 9 0 8 1 2 \times 1 0 ^ { - 3 3 } , 2 . 7 9 0 7 2 6 8 1 2 \times 1 0 ^ { - 3 3 }$ $8 . 2 6 3 6 0 3 9 \times 1 0 ^ { - 3 4 } ) ^ { t }$ , using 40 iterations with tolerance $1 . 0 0 \times 1 0 ^ { - 5 }$ in $l _ { \infty }$ norm with the Gauss-Seidel method.

17. (a) Since $A$ is a positive definite, $a _ { i i } > 0$ for $1 \leq i \leq n$ and $A$ is symmetric. Thus, $A$ can be written as $A = D - L - L ^ { t }$ , where $D$ is diagonal with $d _ { i i } > 0$ and $L$ is lower triangular. The diagonal of the lower triangular matrix $D - L$ has the positive entries $d _ { 1 1 } = a _ { 1 1 }$ , $d _ { 2 2 } = a _ { 2 2 } , \cdots$ , $d _ { n n } = a _ { n n }$ , so $( D - L ) ^ { - 1 }$ exists.

(b) Since $A$ is symmetric,

$$
P ^ { t } = \left( A - T _ { g } ^ { t } A T _ { g } \right) ^ { t } = A ^ { t } - T _ { g } ^ { t } A ^ { t } T _ { g } = A - T _ { g } ^ { t } A T _ { g } = P .
$$

Thus, $P$ is symmetric.

(c) $T _ { g } = ( D - L ) ^ { - 1 } L ^ { t }$ , so

$$
( D - L ) T _ { g } = L ^ { t } = D - L - D + L + L ^ { t } = ( D - L ) - ( D - L - L ^ { t } ) = ( D - L ) - A .
$$

Since $( D - L ) ^ { - 1 }$ exists, we have $T _ { g } = I - ( D - L ) ^ { - 1 } A$ .

(d) Since $Q = ( D - L ) ^ { - 1 } A$ , we have $T _ { g } = I - Q$ . Note that $Q ^ { - 1 }$ exists. By the definition of $P$ we have

$$
\begin{array} { r l } & { P = A - T _ { g } ^ { t } A T _ { g } = A - \left[ I - \left( D - L \right) ^ { - 1 } A \right] ^ { t } A \left[ I - \left( D - L \right) ^ { - 1 } A \right] } \\ & { \quad = A - \left[ I - Q \right] ^ { t } A [ I - Q ] = A - \left( I - Q ^ { t } \right) A ( I - Q ) } \\ & { \quad = A - \left( A - Q ^ { t } A \right) \left( I - Q \right) = A - \left( A - Q ^ { t } A - A Q + Q ^ { t } A Q \right) } \\ & { \quad = Q ^ { t } A + A Q - Q ^ { t } A Q = Q ^ { t } \left[ A + \left( Q ^ { t } \right) ^ { - 1 } A Q - A Q \right] } \\ & { \quad = Q ^ { t } \left[ A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A \right] Q . } \end{array}
$$

(e) Since

$$
\boldsymbol { A } \boldsymbol { Q } ^ { - 1 } = \boldsymbol { A } \left[ \boldsymbol { A } ^ { - 1 } ( \boldsymbol { D } - \boldsymbol { L } ) \right] = \boldsymbol { D } - \boldsymbol { L } \quad \mathrm { a n d } \quad \left( \boldsymbol { Q } ^ { t } \right) ^ { - 1 } \boldsymbol { A } = \boldsymbol { D } - \boldsymbol { L } ^ { t } ,
$$

we have

$$
A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A = D - L + D - L ^ { t } - \left( D - L - L ^ { t } \right) = D .
$$

Thus,

$$
P = Q ^ { t } \left[ A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A \right] Q = Q ^ { t } D Q .
$$

So for $\mathbf { x } \in \mathbb { R } ^ { n }$ , we have ${ \bf x } ^ { t } P { \bf x } = { \bf x } ^ { t } Q ^ { t } D Q { \bf x } = ( Q { \bf x } ) ^ { t } D ( Q { \bf x } )$ .

Since $D$ is a positive diagonal matrix, $( Q { \bf x } ) ^ { t } D ( Q { \bf x } ) \ge 0$ unless $Q \mathbf { x } = \mathbf { 0 }$ . However, $Q$ is nonsingular, so $Q \mathbf { x } = \mathbf { 0 }$ if and only if $\mathbf x = \mathbf 0$ . Thus, $P$ is positive definite.

(f) Let $\lambda$ be an eigenvalue of $T _ { g }$ with the eigenvector $\mathbf { x } \neq \mathbf { 0 }$ . Since $\mathbf { x } ^ { t } P \mathbf { x } > 0$ ,

$$
\mathbf { x } ^ { t } \left[ A - T _ { g } ^ { t } A T _ { g } \right] \mathbf { x } > 0
$$

and

$$
\mathbf { x } ^ { t } A \mathbf { x } - \mathbf { x } ^ { t } T _ { g } ^ { t } A T _ { g } \mathbf { x } > 0 .
$$

Since $T _ { g } \mathbf { x } = \lambda \mathbf { x }$ , we have $\mathbf { x } ^ { t } T _ { g } ^ { t } = \lambda \mathbf { x } ^ { t }$ so

$$
\left( 1 - \lambda ^ { 2 } \right) \mathbf { x } ^ { t } A x = \mathbf { x } ^ { t } A \mathbf { x } - \lambda ^ { 2 } \mathbf { x } ^ { t } A x > 0 .
$$

Since $A$ is positive definite, $1 - \lambda ^ { 2 } > 0$ , and $\lambda ^ { 2 } < 1$ . Thus $| \lambda | < 1$

(g) For any eigenvalue $\lambda$ of $T _ { g }$ , we have $| \lambda | < 1$ . This implies $\rho ( T _ { g } ) < 1$ and $T _ { g }$ is convergent.

# Exercise Set 7.4, page 467

1. Two iterations of the SOR method with $\omega = 1 . 1$ give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 0 5 4 1 0 0 7 9 , - 0 . 2 1 1 5 4 3 5 , 0 . 6 4 7 7 1 5 9 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 8 7 6 7 9 0 , 0 . 9 7 8 4 9 3 5 , 0 . 7 8 9 9 3 2 8 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 7 1 8 8 5 , 2 . 8 1 8 8 2 2 , - 0 . 2 8 0 9 7 2 6 , - 2 . 2 3 5 4 2 2 ) ^ { i }$ t

$$
\mathbf { x } ^ { ( 2 ) } = ( 1 . 0 7 9 6 7 5 , - 1 . 2 6 0 6 5 4 , 2 . 0 4 2 4 8 9 , 1 . 9 9 5 3 7 3 , 2 . 0 4 9 5 3 6 ) ^ { t }
$$

2. Two iterations of the SOR method with $\omega = 1 . 1$ give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 5 1 2 7 7 5 0 0 0 , - 0 . 8 2 9 8 4 9 1 6 6 7 , - 0 . 0 8 4 3 3 7 3 6 6 7 ) ^ { t }$   
(b) $\mathfrak { c } ^ { ( 2 ) } = ( - 1 . 5 8 5 2 3 7 5 0 , 1 . 3 7 8 8 5 6 8 8 , - 0 . 7 0 3 9 2 1 2 8 \mathrm { . }$ 12)t   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 6 6 0 4 9 0 2 , 0 . 0 3 7 0 0 7 4 9 , - 0 . 2 4 9 3 5 1 3 , 0 . 6 5 6 1 1 3 9 ) ^ { t }$   
(d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 3 7 8 1 2 5 0 0 0 0 , 1 . 4 4 5 4 6 8 7 5 0 , 0 . 3 5 9 6 9 1 4 0 6 2 , 1 . 4 5 8 5 3 1 2 5 0 , 0 . 3 0 7 1 9 2 1 8 7 6 0 0 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 . 0 , 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 .$ 5, 1.572124727)t

3. Two iterations of the SOR method with $\omega = 1 . 3$ give the following results.

\*(a) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 1 0 4 0 1 0 3 , - 0 . 1 3 3 1 8 1 4 , 0 . 6 7 7 4 9 9 7 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 5 7 0 7 3 , 0 . 9 9 0 3 8 7 5 , 0 . 7 2 0 6 5 6 9 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 2 3 6 9 5 , 3 . 2 2 8 7 5 2 , - 0 . 1 5 2 3 8 8 8 , - 2 . 0 4 1 2 6 6 ) ^ { t }$ (d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 7 0 6 4 2 5 8 , - 0 . 4 1 0 3 8 7 6 , 2 . 4 1 7 0 6 3 , 2 . 2 5 1 9 5 5 , 1 . 0 6 1 5 0 7 ) ^ { t }$

4. Two iterations of the SOR method with $\omega = 1 . 3$ give the following results.

(a) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 4 5 5 7 8 3 3 3 4 , - 0 . 7 7 2 1 4 9 4 4 4 2 , - 0 . 0 8 0 5 3 9 6 2 2 8 ) ^ { t }$   
(b) $\mathbf { x } ^ { ( 2 ) } = ( - 1 . 4 2 0 7 3 7 5 0 , 1 . 5 9 5 7 5 8 1 2 5 , - 0 . 8 5 9 7 9 2 7 8 1 2 ) ^ { t }$   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 7 2 6 8 8 9 3 , 0 . 1 2 5 1 4 8 3 , - 0 . 2 9 2 3 3 7 1 , 0 . 7 0 3 7 0 1 8 ) ^ { t }$   
(d) $\mathbf { x } ^ { \left. \varepsilon \right. } = ( 0 . 5 2 8 1 2 5 0 0 0 0 , 1 . 4 8 0 7 8 1 2 5 0 , 0 . 3 2 2 8 1 6 4 0 6 , 1 . 3 5 9 7 1 8 7 5 0 , 0 . 4 2 8 8 1 7 1 8 7 5 , 1 . 5 0 5 9 4 9 9 6 1 ) ^ { \varepsilon }$

5. The SOR Algorithm with $\omega = 1 . 2$ gives the following results.

\*(a) $\mathbf { x } ^ { ( 1 1 ) } = ( 0 . 0 3 5 4 4 3 5 6 , - 0 . 2 3 7 1 8 3 3 3 , 0 . 6 5 7 8 8 3 1 7 ) ^ { t }$ (b) $\mathbf { x } ^ { ( 7 ) } = ( 0 . 9 9 5 8 3 4 1 , 0 . 9 5 7 9 0 4 1 , 0 . 7 9 1 5 7 5 6 ) ^ { t }$ (c) $\mathbf { x } ^ { ( 8 ) } = ( - 0 . 7 9 7 6 0 0 9 , 2 . 7 9 5 2 8 8 , - 0 . 2 5 8 8 2 9 3 , - 2 . 2 5 1 7 6 8 ) ^ { t }$ (d) $\mathfrak { c } ^ { ( \mathrm { 1 0 } ) } = ( 0 . 7 8 6 6 3 1 0 , - 1 . 0 0 2 8 0 7 , 1 . 8 6 6 5 3 0 , 1 . 9 1 2 6$ 45, 1.989792) $t$

6. The SOR Algorithm with $\omega = 1 . 2$ gives the following results.

(a) $\mathbf { x } ^ { ( 8 ) } = ( 1 . 4 4 7 5 0 3 8 1 4 , - 0 . 8 3 5 9 2 9 7 6 2 4 , - 0 . 0 4 4 5 5 1 6 5 3 2 ) ^ { t }$   
(b) $\mathbf { x } ^ { ( 6 ) } = ( - 1 . 4 5 4 5 8 2 8 5 0 , 1 . 4 5 4 4 9 8 8 6 3 , - 0 . 7 2 7 3 3 0 2 7 1 4 ) ^ { t }$   
(c) $\mathbf { x } ^ { ( 0 ) } = ( - 0 . 7 5 3 0 8 9 7 1 , 0 . 0 4 1 1 7 2 8 1 , - 0 . 2 8 0 7 4 8 1 7 , 0 . 6 9 1 6 3 5 0 6 ) ^ { u }$   
(d) $\mathbf { x } ^ { ( 7 ) } = ( 0 . 3 5 7 1 2 8 4 9 4 5 , 1 . 4 2 8 5 8 2 2 4 0 , 0 . 3 5 7 1 4 8 9 7 3 1 , 1 . 5 7 1 4 4 0 1 1 6 , 0 . 2 8 5 7 5 , 0 . 1 , 0 . 1 , 0 . 1 , 0 . 1 )$ 000650, 1.571445036)t

7. The tridiagonal matrices are in parts (b) and (c). \*(9b): For $\omega = 1 . 0 1 2 8 2 3$ we have $\mathbf { x } ^ { ( 4 ) } = ( 0 . 9 9 5 7 8 4 6 , 0 . 9 5 7 8 9 3 5 , 0 . 7 9 1 5 7 8 8 ) ^ { t }$ . (9c): For $\omega = 1 . 1 5 3 4 9 9$ we have $\mathbf { x } ^ { ( 7 ) } = ( - 0 . 7 9 7 7 6 5 1 , 2 . 7 9 5 3 4 3 , - 0 . 2 5 8 8 0 2 1 , - 2 . 2 5 1 7 6 0 ) ^ { t }$ .

8. The tridiagonal matrix is in part (d). (10d): For $\omega = 1 . 0 3 3 3 7 0 4 5 3$ we have

x(5) = (0.3571407017, 1.428570817, 0.357142771, 1.571421010, 0.2857118407, 1.571428256)t.

9. Let $\lambda _ { 1 } , . . . , \lambda _ { n }$ be the eigenvalues of $T _ { \omega }$ . Then

$$
\begin{array} { l } { \displaystyle \prod _ { i = 1 } ^ { n } \lambda _ { i } = \operatorname* { d e t } T _ { \omega } = \operatorname* { d e t } \bigg ( ( D - \omega L ) ^ { - 1 } [ ( 1 - \omega ) D + \omega U ] \bigg ) } \\ { = \operatorname* { d e t } ( D - \omega L ) ^ { - 1 } \operatorname* { d e t } ( ( 1 - \omega ) D + \omega U ) = \operatorname* { d e t } \big ( D ^ { - 1 } \big ) \operatorname* { d e t } ( ( 1 - \omega ) D ) } \\ { = \bigg ( \displaystyle \frac { 1 } { \big ( a _ { 1 1 } a _ { 2 2 } \ldots a _ { n n } \big ) } \bigg ) \bigg ( ( 1 - \omega ) ^ { n } a _ { 1 1 } a _ { 2 2 } \ldots a _ { n n } \bigg ) \bigg ) = ( 1 - \omega ) ^ { n } . } \end{array}
$$

Thus

$$
\rho ( T _ { \omega } ) = \underset { 1 \leq i \leq n } { \operatorname* { m a x } } | \lambda _ { i } | \geq | \omega - 1 | ,
$$

and $| \omega - 1 | < 1$ if and only if $0 < \omega < 2$ .

10. (a) The system was reordered so that the diagonal of the matrix had nonzero entries.

(b) (i) The solution vector using 30 iterations is

$( 0 . 0 0 3 6 \dot { 2 } , - 6 \dot { 3 } 3 9 . 7 4 4 6 \dot { 3 } 8 , - 3 6 6 0 . 2 5 \dot { 3 } 2 7 \dot { 2 } , - 8 9 6 5 . 7 5 5 8 0 8 , 6 \dot { 3 } \dot { 3 } 9 . 7 4 4 6 \dot { 3 } 8 , 1 0 0 0 0$ , − 7320.508959, 6339.746729)t.

(ii) The solution vector using 57 iterations is

(−0.002651, − 6339.744637, −3660.255362, −8965.752851, 6339.748259, 10000, − 7320.506544, 6339.748258)t.

(iii) Method does not converge using $\omega = 1 . 2 5$ . However, using $\omega = 1 . 1$ and using 132 iterations gives the solution vector

(0.0045175, − 6339.744528, −3660.253009, $-$ 8965.756179, 6339.743756, 10000, $- 7 3 2 0 . 5 0 9 5 4 7 , 6 3 3 9 . 7 4 7 5 4 4 ) ^ { \iota }$ .

11. The results that follow include approximations from the Jacobi and Gauss-Seidel methods for comparison.   

<table><tr><td></td><td>Jacobi 33</td><td>Gauss-Seidel 8 iterations</td><td>SOR (ω = 1.2) 13</td><td></td><td>Jacobi</td><td>Gauss-Seidel</td><td>SOR (ω = 1.2)</td></tr><tr><td></td><td>iterations</td><td></td><td>iterations</td><td></td><td>iterations</td><td>iterations</td><td>iterations</td></tr><tr><td>X1</td><td>1.53873501</td><td>1.53873270</td><td>1.53873549</td><td>X41</td><td>0.02185033</td><td>0.02184781</td><td>0.02184855</td></tr><tr><td>x2</td><td>0.73142167</td><td>0.73141966</td><td>0.73142226</td><td>X42</td><td>0.02133203</td><td>0.02132965</td><td>0.02133038</td></tr><tr><td>x3</td><td>0.10797136</td><td>0.10796931</td><td>0.10797063</td><td>X43</td><td>0.02083782</td><td>0.02083545</td><td>0.02083615</td></tr><tr><td>X4</td><td>0.17328530</td><td>0.17328340</td><td>0.17328480</td><td>X44</td><td>0.02036585</td><td>0.02036360</td><td>0.02036429</td></tr><tr><td>X5</td><td>0.04055865</td><td>0.04055595</td><td>0.04055737</td><td>X45</td><td>0.01991483</td><td>0.01991261</td><td>0.01991324</td></tr><tr><td>X6</td><td>0.08525019</td><td>0.08524787</td><td>0.08524925</td><td>X46</td><td>0.01948325</td><td>0.01948113</td><td>0.01948175</td></tr><tr><td>X7</td><td>0.16645040</td><td>0.16644711 0.12197878</td><td>0.16644868 0.12198026</td><td>X47</td><td>0.01907002</td><td>0.01906793</td><td>0.01906846</td></tr><tr><td>x8</td><td>0.12198156</td><td></td><td></td><td>X48</td><td>0.01867387</td><td>0.01867187</td><td>0.01867239</td></tr><tr><td>x9</td><td>0.10125265</td><td>0.10124911</td><td>0.10125043</td><td>X49</td><td>0.01829386</td><td>0.01829190</td><td>0.01829233</td></tr><tr><td>X10</td><td>0.09045966</td><td>0.09045662</td><td>0.09045793 0.07202912</td><td>X50</td><td>0.71792896</td><td>0.01792707</td><td>0.01792749</td></tr><tr><td>X11</td><td>0.07203172</td><td>0.07202785</td><td>0.07026392</td><td>X51</td><td>0.01757833</td><td>0.01757648</td><td>0.01757683</td></tr><tr><td>X12</td><td>0.07026597</td><td>0.07026266</td><td>0.06875546</td><td>X52</td><td>0.01724113</td><td>0.01723933</td><td>0.01723968</td></tr><tr><td>X13</td><td>0.06875835</td><td>0.06875421 0.06324307</td><td>0.06324429</td><td>X53</td><td>0.01691660</td><td>0.01691487</td><td>0.01691517</td></tr><tr><td>X14</td><td>0.06324659</td><td>0.05971083</td><td>0.05971200</td><td>X54</td><td>0.01660406</td><td>0.01660237</td><td>0.01660267</td></tr><tr><td>X15</td><td>0.05971510</td><td>0.05570834</td><td>0.05570949</td><td>X55</td><td>0.01630279</td><td>0.01630127</td><td>0.01630146</td></tr><tr><td>X16</td><td>0.05571199 0.05187851</td><td>0.05187416</td><td>0.05187529</td><td>X56</td><td>0.01601230 0.01573198</td><td>0.01601082</td><td>0.01601101</td></tr><tr><td>X17</td><td>0.04924911</td><td>0.04924537</td><td>0.04924648</td><td>X57</td><td></td><td>0.01573087</td><td>0.01573077</td></tr><tr><td>X18</td><td>0.04678213</td><td>0.04677776</td><td>0.04677885</td><td>X58</td><td>0.01546129</td><td>0.01546020</td><td>0.01546010</td></tr><tr><td>X19</td><td>0.04448679</td><td>0.04448303</td><td>0.04448409</td><td>X59</td><td>0.01519990</td><td>0.01519909</td><td>0.01519878</td></tr><tr><td>x20</td><td>0.04246924</td><td>0.04246493</td><td>0.04246597</td><td>X60</td><td>0.01494704</td><td>0.01494626</td><td>0.01494595</td></tr><tr><td>X21</td><td>0.04053818</td><td>0.04053444</td><td>0.04053546</td><td>X61</td><td>0.01470181</td><td>0.01470085</td><td>0.01470077</td></tr><tr><td>X22</td><td></td><td>0.03876852</td><td>0.03876952</td><td>X62</td><td>0.01446510</td><td>0.01446417</td><td>0.01446409</td></tr><tr><td>X23</td><td>0.03877273 0.03718190</td><td>0.03717822</td><td>0.03717920</td><td>X63</td><td>0.01423556</td><td>0.01423437</td><td>0.01423461</td></tr><tr><td>X24</td><td></td><td>0.03570451</td><td>0.03570548</td><td>X64</td><td>0.01401350</td><td>0.01401233</td><td>0.01401256</td></tr><tr><td>X25</td><td>0.03570858 0.03435107</td><td>0.03434748</td><td>0.03434844</td><td>X65</td><td>0.01380328</td><td>0.01380234</td><td>0.01380242</td></tr><tr><td>X26</td><td>0.03309542</td><td>0.03309152</td><td>0.03309246</td><td>X66</td><td>0.01359448</td><td>0.01359356</td><td>0.01359363</td></tr><tr><td>X27</td><td>0.03192212</td><td>0.03191866</td><td>0.03191958</td><td>X67</td><td>0.01338495</td><td>0.01338434</td><td>0.01338418</td></tr><tr><td>X28</td><td></td><td>0.03082637</td><td>0.03082727</td><td>X68</td><td>0.01318840</td><td>0.01318780</td><td>0.01318765</td></tr><tr><td>X29</td><td>0.03083007 0.02980997</td><td>0.02980666</td><td>0.02980755</td><td>X69</td><td>0.01297174</td><td>0.01297109 0.01278598</td><td>0.01297107</td></tr><tr><td>X30</td><td>0.02885510</td><td>0.02885160</td><td>0.02885248</td><td>x70</td><td>0.01278663</td><td>0.01270263</td><td>0.01278597</td></tr><tr><td>X31</td><td>0.02795937</td><td>0.02795621</td><td>0.02795707</td><td>X71</td><td>0.01270328</td><td></td><td>0.01270271</td></tr><tr><td>X32</td><td>0.02711787</td><td>0.02711458</td><td>0.02711543</td><td>X72</td><td>0.01252719</td><td>0.01252656</td><td>0.01252663</td></tr><tr><td>X33</td><td></td><td></td><td></td><td>X73</td><td>0.01237700</td><td>0.01237656</td><td>0.01237654</td></tr><tr><td>X34</td><td>0.02632478</td><td>0.02632179</td><td>0.02632262</td><td>X74</td><td>0.01221009</td><td>0.01220965</td><td>0.01220963</td></tr><tr><td>X35</td><td>0.02557705</td><td>0.02557397</td><td>0.02557479</td><td>X75</td><td>0.01129043</td><td>0.01129009</td><td>0.01129008</td></tr><tr><td>X36</td><td>0.02487017</td><td>0.02486733</td><td>0.02486814</td><td>X76</td><td>0.01114138</td><td>0.01114104</td><td>0.01114102</td></tr><tr><td>X37</td><td>0.02420147</td><td>0.02419858</td><td>0.02419938</td><td>X77</td><td>0.01217337</td><td>0.01217312</td><td>0.01217313</td></tr><tr><td>x38</td><td>0.02356750</td><td>0.02356482</td><td>0.02356560</td><td>X78</td><td>0.01201771</td><td>0.01201746</td><td>0.01201746</td></tr><tr><td>X39</td><td>0.02296603</td><td>0.02296333</td><td>0.02296410</td><td>x79</td><td>0.01542910</td><td>0.01542896</td><td>0.01542896</td></tr><tr><td>X40</td><td>0.02239424</td><td>0.02239171</td><td>0.02239247</td><td>x80</td><td>0.01523810</td><td>0.01523796</td><td>0.01523796</td></tr></table>

12. For $0 < \omega < 2$ , let $T _ { \omega } = ( D - \omega L ) ^ { - 1 } \left[ ( 1 - \omega ) D + \omega L ^ { t } \right] .$ . Let $P = A - T _ { \omega } ^ { t } A T _ { \omega }$ and note that $P$ is symmetric.

As in Exercise 17 of Section 7.3, we derive a new representation for $T _ { \omega }$ :

$$
( D - \omega L ) T _ { \omega } = ( 1 - \omega ) D + \omega L ^ { t } = ( D - \omega L ) - \omega A , \mathrm { s o } T _ { \omega } = I - \omega ( D - \omega L ) ^ { - 1 } A .
$$

Let

$$
\begin{array} { r } { Q = \omega ( D - \omega L ) ^ { - 1 } A \quad \mathrm { a n d } \quad Q ^ { t } = \omega A \left[ ( D - \omega L ) ^ { - 1 } \right] ^ { t } . } \end{array}
$$

We again have

$$
P = Q ^ { t } \left[ A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A \right] Q .
$$

But

$$
A Q ^ { - 1 } = \frac { 1 } { \omega } ( D - \omega L ) \quad \mathrm { a n d } \quad \left( Q ^ { t } \right) ^ { - 1 } A = \frac { 1 } { \omega } \left( D - \omega L ^ { t } \right)
$$

so

$$
\begin{array} { c } { \displaystyle { A Q ^ { - 1 } + \left( Q ^ { t } \right) ^ { - 1 } A - A = \frac 1 \omega \left[ D - \omega L + D - \omega L ^ { t } \right] - A } } \\ { \displaystyle { = \frac 2 \omega D - D + D - L - L ^ { t } - A } } \\ { \displaystyle { = \left( \frac 2 \omega - 1 \right) D . } } \end{array}
$$

Thus $P = \left( { \frac { 2 } { \omega } } - 1 \right) Q ^ { t } D Q$ . Since $0 < \omega < 2$ , we have $\frac { \ d ^ { 2 } } { \ d \omega } - 1 > 0$ and $P$ is positive definite.

The proof follows Exercise 17 with $T _ { g }$ replaced by $T _ { \omega }$ . Hence, $T _ { \omega }$ is convergent.

# Exercise Set 7.5, page 482

1. The $l _ { \infty }$ condition numbers are:

(a) 50 (b) 241.37 (c) 600,002 (d) 339,866

2. The $l _ { \infty }$ condition numbers are:

(a) 12.24012756 (b) 12.24012756 (c) 12 \*(d) 198.17

3. We have

<table><tr><td></td><td>=x-xα</td><td>K(A)/b- Ax∞/A</td></tr><tr><td>(a)</td><td>8.571429 × 10-4</td><td>1.238095 × 10-2</td></tr><tr><td>(b)</td><td>0.1</td><td>3.832060</td></tr><tr><td>(c）</td><td>0.04</td><td>0.8</td></tr><tr><td>(d）</td><td>20</td><td>1.152440 × 105</td></tr></table>

4. We have

<table><tr><td></td><td>x-x|α</td><td>K(A)|b- Ax|∞/A∞</td></tr><tr><td>(a)</td><td>20</td><td>65.03241</td></tr><tr><td>(b)</td><td>0.02</td><td>720.5764</td></tr><tr><td>（c）</td><td>0.1</td><td>3.727412 × 10-1</td></tr><tr><td>*（d)</td><td>6.551700 × 10-2</td><td>9.059201</td></tr></table>

5. Gaussian elimination and iterative refinement give the following results.

(a) (i) $( - 1 0 . 0 , 1 . 0 1 ) ^ { t }$ , (ii) $( 1 0 . 0 , 1 . 0 0 ) ^ { t }$   
(b) (i) $( 1 2 . 0 , 0 . 4 9 9 , - 1 . 9 8 ) ^ { t }$ , (ii) $( 1 . 0 0 , 0 . 5 0 0 , - 1 . 0 0 ) ^ { t }$   
(c) (i) $( 0 . 1 8 5 , 0 . 0 1 0 3 , - 0 . 0 2 0 0 , - 1 . 1 2 ) ^ { t }$ , (ii) $( 0 . 1 7 7 , 0 . 0 1 2 7 , - 0 . 0 2 0 7 , - 1 . 1 8 ) ^ { \tau }$   
(d) (i) $( 0 . 7 9 9 , - 3 . 1 2 , 0 . 1 5 1 , 4 . 5 6 ) ^ { t }$ , (ii) $( 0 . 7 5 8 , - 3 . 0 0 , 0 . 1 5 9 , 4 . 3 0 ) ^ { t }$

6. Gaussian elimination and iterative refinement give the following results.

$$
\begin{array} { r l } & { ( 1 2 . 0 0 , 0 . 9 9 9 0 ) ^ { t } , ( 1 0 . 0 0 , 1 . 0 0 0 ) ^ { t } } \\ & { ( 1 . 2 0 0 , 0 . 5 0 0 2 , - 1 . 3 8 0 ) ^ { t } , ( 1 . 0 0 0 , 0 . 5 0 0 0 , - 0 . 9 9 9 8 ) ^ { t } } \\ & { ( 0 . 1 7 5 6 , 0 . 0 1 3 0 5 , - 0 . 0 2 0 7 5 , - 1 . 1 9 2 ) ^ { t } , ( 0 . 1 7 6 8 , 0 . 0 1 2 6 9 , - 0 . 0 2 0 6 5 , - 1 . 1 8 2 ) ^ { t } } \\ & { ( 0 . 7 9 6 3 , - 3 . 1 5 2 , 0 . 1 7 0 5 , 4 . 6 1 5 ) ^ { t } , ( 0 . 7 8 8 9 , - 3 . 1 2 8 , 0 . 1 6 7 8 , 4 . 5 6 1 ) ^ { t } } \end{array}
$$

7. The matrix is ill-conditioned since $K _ { \infty } = 6 0 0 0 2$ . We have $\tilde { \mathbf { x } } = ( - 1 . 0 0 0 0 , 2 . 0 0 0 0 ) ^ { t }$ .

8. The matrix $A$ is ill-conditioned since $K _ { \infty } ( A ) = 6 0 0 , 0 0 2$ and $\hat { \mathbf { x } } = ( 1 . 8 1 8 1 9 2 , 0 . 5 9 0 9 0 9 1 ) ^ { \iota }$

$^ { * } 9$ . For any vector $\mathbf { x }$ , we have

$$
\left\| \mathbf { x } \right\| = \left\| A ^ { - 1 } A \mathbf { x } \right\| \leq \left\| A ^ { - 1 } \right\| \left\| A \mathbf { x } \right\| , \ \mathrm { s o } \ \left\| A \mathbf { x } \right\| \geq { \frac { \left\| \mathbf { x } \right\| } { \left\| A ^ { - 1 } \right\| } } .
$$

Let $\mathbf { x } \neq \mathbf { 0 }$ be such that $\| \mathbf { x } \| = 1$ and $B \mathbf { x } = \mathbf { 0 }$ . Then

$$
\left\| ( A - B ) \mathbf { x } \right\| = \left\| A \mathbf { x } \right\| \geq { \frac { \left\| \mathbf { x } \right\| } { \left\| A ^ { - 1 } \right\| } } { \mathrm { a n d } } { \frac { \left\| ( A - B ) \mathbf { x } \right\| } { \left\| A \right\| } } \geq { \frac { 1 } { \left\| A ^ { - 1 } \right\| \left\| A \right\| } } = { \frac { 1 } { K ( A ) } } .
$$

Since $\| \mathbf { x } \| = 1$ ,

$$
\left\| ( A - B ) \mathbf { x } \right\| \leq \left\| A - B \right\| \left\| \mathbf { x } \right\| = \left\| A - B \right\| { \mathrm { ~ a n d ~ } } { \frac { \| A - B \| } { \left\| A \right\| } } \geq { \frac { 1 } { K ( A ) } } .
$$

10. The approximate condition numbers are as follows:

$^ { * } ( \mathrm { a } )$ With $B = { \left[ \begin{array} { l l } { 1 } & { 2 } \\ { 1 } & { 2 } \end{array} \right] }$ , we have $K _ { \infty } ( A ) \geq 3 0 \small { , } 0 0 0$ (b) With $B = \left[ \begin{array} { l l } { 4 . 0 } & { 1 . 6 } \\ { 7 . 0 } & { 2 . 8 } \end{array} \right]$ , we have $K _ { \infty } ( A ) \geq { \frac { 9 7 } { 3 } }$ .

11. (a) $K _ { \infty } \left( H ^ { ( 4 ) } \right) = 2 8 , 3 7 5$ (b) $K _ { \infty } \left( H ^ { ( 5 ) } \right) = 9 4 3 , 6 5 6$ (c) actual solution $\mathbf { x } = ( - 1 2 4 , 1 5 6 0 , - 3 9 6 0 , 2 6 6 0 ) ^ { t }$ ; approximate solution $\tilde { \mathbf { x } } = ( - 1 2 4 . 2 , ~ 1 5 6 3 . 8 , - 3 9 7 1 . 8 , 2 6 6 8 . 8 ) ^ { t }$ ; $\| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } = 1 1 . 8$ ; and $\frac { \| \mathbf { x } - \tilde { \mathbf { x } } \| _ { \infty } } { \| \mathbf { x } \| _ { \infty } } = 0 . 0 2 9 8 0$ $\frac { K _ { \infty } ( A ) } { 1 - K _ { \infty } ( A ) \left( \frac { \| \delta A \| _ { \infty } } { \| A \| _ { \infty } } \right) } \left[ \frac { \| \delta b \| _ { \infty } } { \| b \| _ { \infty } } + \frac { \| \delta A \| _ { \infty } } { \| A \| _ { \infty } } \right] = \frac { 2 8 3 7 5 } { 1 - 2 8 3 7 5 \left( \frac { 6 . 6 \times 1 0 ^ { - 6 } } { 2 . 0 8 3 } \right) } \left[ 0 + \frac { 6 . { \overline { { 6 } } } \times 1 0 ^ { - 6 } } { 2 . 0 8 { \overline { { 3 } } } } \right]$

12. For the $3 \times 3$ Hilbert matrix $H$ , we have

$$
\hat { H } ^ { - 1 } = \left[ \begin{array} { c c c } { 8 . 9 6 8 } & { - 3 5 . 7 7 } & { 2 9 . 7 7 } \\ { - 3 5 . 7 7 } & { 1 9 0 . 6 } & { - 1 7 8 . 6 } \\ { 2 9 . 7 7 } & { - 1 7 8 . 6 } & { 1 7 8 . 6 } \end{array} \right] , \qquad \hat { H } = \left[ \begin{array} { c c c } { 0 . 9 7 9 9 } & { 0 . 4 8 7 0 } & { 0 . 3 2 3 8 } \\ { 0 . 4 8 6 0 } & { 0 . 3 2 4 6 } & { 0 . 2 4 3 4 } \\ { 0 . 3 2 3 2 } & { 0 . 2 4 3 3 } & { 0 . 1 9 4 9 } \end{array} \right] ,
$$

and $\| H - \hat { H } \| _ { \infty } = 0 . 0 4 2 6 0$ .

# Exercise Set 7.6, page 492

1. (a) (0.18, 0.13)t (b) (0.19, 0.10)t (c) Gaussian elimination gives the best answer since $\mathbf { v } ^ { ( 2 ) } = ( 0 , 0 ) ^ { t }$ in the conjugate gradient method. (d) $( 0 . 1 3 , 0 . 2 1 ) ^ { t }$ . There is no improvement, although $\mathbf { v } ^ { ( 2 ) } \neq \mathbf { 0 }$ .

2. (a) (1.0, 1.0)t (b) (1.0, 1.0)t (c) Both answers are the same. However, more operations are required in the conjugate gradient method. (d) $( 1 . 1 , 1 . 0 ) ^ { t }$ . The answer is not as good due to rounding error.

3. (a) $( 1 . 0 0 , - 1 . 0 0 , 1 . 0 0 ) ^ { t }$ (b) (0.827, 0.0453, −0.0357)t (c) Partial pivoting and scaled partial pivoting also give $( 1 . 0 0 , - 1 . 0 0 , 1 . 0 0 ) ^ { t }$ . (d) $( 0 . 7 7 6 , 0 . 2 3 8 , - 0 . 1 8 5 ) ^ { t } .$

The residual from (3b) is $( - 0 . 0 0 0 4 , - 0 . 0 0 3 8 , 0 . 0 0 3 7 ) ^ { t }$ , and the residual from part (3d) is (0.0022, −0.0038,0.0024)t. There does not appear to be much improvement, if any. Rounding error is more prevalent because of the increase in the number of matrix multiplications.

4. (a) $( 0 . 9 9 9 9 9 9 9 9 9 9 7 , - 1 , 1 ) ^ { t }$ (b) $( 0 . 9 9 9 9 9 9 9 1 9 5 9 , - 1 . 0 0 0 0 6 6 4 1 9 , 0 . 9 9 9 9 9 9 6 6 9 3 ) ^ { u }$ ; The residual is $\left( 0 . 1 1 2 3 6 \times 1 0 ^ { - 5 } , 0 . 6 2 4 2 \times 1 0 ^ { - 6 } , 0 . 4 3 8 7 \times 1 0 ^ { - 6 } \right) ^ { \tau }$ (c) Partial pivoting gives the same answer as in part (a). (d) (1.000000364, −0.999999391, 1.000000888)t.

The residual is $\left( - 0 . 1 0 0 0 1 \times 1 0 ^ { - 5 } , - 0 . 6 3 0 8 7 \times 1 0 ^ { - 6 } , - 0 . 4 6 9 1 \times 1 0 ^ { - 6 } \right) ^ { t } .$ .

There does not seem to be an improvement in this preconditioning method.

5. Two steps of the Conjugate Gradient method with $C = C ^ { - 1 } = I$ give the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 5 3 5 9 3 3 4 5 6 , - 0 . 1 6 9 7 9 3 2 1 1 7 , 0 . 5 9 0 1 1 7 2 0 9 1 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 2 2 1$ .   
\*(b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 9 9 3 1 2 9 5 1 0 , 0 . 9 6 4 2 7 3 4 4 5 6 , 0 . 7 7 8 4 2 6 6 5 7 5 ) ^ { t } \hat { \varepsilon }$ nd $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 1 4 4$ .   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 7 2 9 0 9 5 4 1 1 4 , 2 . 5 1 5 7 8 2 4 5 2 , - 0 . 6 7 8 8 9 0 4 0 5 8 , - 2 . 3 3 1 9 4 3 9 8 2 ) ^ { t } :$ and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 2 . 2$ .   
(d) $\mathbf { x } ^ { ( 2 ) } = \left( - 0 . 7 0 7 1 1 0 8 9 0 1 , - 0 . 0 9 5 4 7 4 8 8 8 1 , - 0 . 3 4 4 1 0 7 4 0 9 3 , 0 . 5 2 5 6 0 9 1 4 9 7 \right)$ t and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } =$ 0.39.   
(e) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 3 3 5 9 6 8 3 8 1 , 0 . 9 3 6 7 5 8 8 9 3 5 , 1 . 3 3 9 9 2 0 9 4 9 , 1 . 7 4 3 0 8 3 0 0 4 , 1 . 7 4 3 0 8 3 0 0 4 ) ^ { t } \mathfrak { s o l t a r s o f f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f } \quad \mathrm { a n d f }$ nd $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } =$ 1.3.   
(f) $\mathbf { x } ^ { ( 2 ) } = ( 1 . 0 2 2 3 7 5 6 7 1 , 1 . 6 8 6 4 5 1 8 9 3 , 1 . 0 2 2 3 7 5 6 7 1 , 2 . 0 6 0 9 1 9 5 6 8 , 0 . 8 3 1 0 9 9 1 8 )$ 7764, 2.060919568)t and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 1 . 1 3$ .

6. Two steps of the Conjugate Gradient method with $C ^ { - 1 } = D ^ { - 1 / 2 }$ give the following:

(a) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 0 1 2 8 1 3 2 9 3 , - 0 . 2 0 9 5 5 0 7 3 5 2 , 0 . 0 7 0 1 2 1 7 8 9 1 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 1 4 5$   
\*(b) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 9 9 9 3 1 2 9 5 1 0 , 0 . 9 6 4 2 7 3 4 4 5 5 , 0 . 7 7 8 4 2 6 6 5 7 7 ) ^ { t } { \mathrm { a n d } } \left\| \mathbf { r } ^ { ( 2 ) } \right\| _ { \infty }$ $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 0 . 1 4 4$   
(c) $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 3 3 6 5 8 0 2 6 2 5 , 2 . 1 2 9 6 9 3 1 8 9 , - 0 . 7 6 0 0 3 9 5 5 8 0 , 2 . 7 0 3 1 9 6 8 1 4 ) ^ { t } \sin ^ { 2 } { \delta }$ nd $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 2 . 3 5$   
(d) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 5 9 2 7 7 2 1 5 6 4 , - 0 . 3 7 9 1 9 6 8 2 3 3 , - 0 . 0 2 6 4 9 9 4 3 8 2 7 , 0 . 0 1 9 7 7 2 7 2 8 3 ) ^ { \circ }$ t and $\left\| \mathbf { r } ^ { ( 2 ) } \right\| _ { \infty } =$ 0.146   
(e) $\mathbf { x } ^ { ( 2 ) } = ( 0 . 4 4 1 4 2 4 8 5 7 6 , 0 . 8 0 8 9 2 7 6 5 0 0 , 1 . 4 6 3 7 6 0 2 0 0 , 1 . 7 3 0 5 3 7 7 2 1 , 1 . 8 9 5 8 0 8 6 0 0 ) ^ { t } { \mathrm { a n d } }$ $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } =$ 1.06   
(f) x(2) = (1.022375670, 1.686451892, 1.022375670, 2.060919568, 0.8310997753, 2.060919568)t and $\| \mathbf { r } ^ { ( 2 ) } \| _ { \infty } = 1 . 1 3$

7. The Conjugate Gradient method with $C = C ^ { - 1 } = I$ gives the following:

(a) $\mathfrak { c } ^ { ( 3 ) } = ( 0 . 0 6 1 8 5 5 6 7 0 1 3 , - 0 . 1 9 5 8 7 6 2 8 8 7 , 0 . 6 1 8 5 5$ 67010)t and $\| \mathbf { r } ^ { ( 3 ) } \| _ { \infty } = 0 . 4 \times 1 0 ^ { - 9 }$ .   
\*(b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 9 5 7 8 9 4 7 3 8 , 0 . 9 5 7 8 9 4 7 3 6 9 , 0 . 7 9 1 5 7 8 9 4 7 4 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 3 ) } \| _ { \infty } = 0 . 1 \times 1 0 ^ { - 9 }$ .   
(c) $\mathbf { x } ^ { ( 4 ) } = ( - 0 . 7 9 7 6 4 7 0 5 7 9 , 2 . 7 9 5 2 9 4 1 2 0 , - 0 . 2 5 8 8 2 3 5 3 0 5 , - 2 . 2 5 1 7 6 4 7 0 6 ) ^ { t } \mathrm { a }$ nd $\| \mathbf { r } ^ { ( 4 ) } \| _ { \infty } = 0 . 3 9 \times$ $1 0 ^ { - 7 }$ .   
(d) $\mathbf { x } ^ { ( 4 ) } \ = \ ( - 0 . 7 5 3 4 2 4 6 5 7 5 , 0 . 0 4 1 0 9 5 8 9 0 3 9 , - 0 . 2 8 0 8 2 1 9 1 7 9 , 0 . 6 9 1 7 8 0 8 2 1 9 ) ^ { t }$ and $\| \mathbf { r } ^ { ( 4 ) } \| _ { \infty } =$ 0.11  10−9.   
(e) $\mathbf { x } ^ { ( 5 ) } = ( 0 . 4 5 1 6 1 2 9 0 3 2 , 0 . 7 0 9 6 7 7 4 1 9 7 , 1 . 6 7 7 4 1 9 3 5 5 , 1 . 7 4 1 9 3 5 4 8 3 , 1 . 8 0 6 4 5 1 6 1 3 ) ^ { t } \mathrm { a n d } \mathbf { x } ^ { ( 5 ) }$ nd $\| \mathbf { r } ^ { ( 5 ) } \| _ { \infty } =$ $0 . 2 \times 1 0 ^ { - 9 }$ .

(f) $\mathbf { x } ^ { ( 4 ) } = ( 1 . 0 0 0 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 0 0 , 1 . 0 0 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 0 0 , 0 . 9 9 9 9 9 9 9$ 9997, 2.000000000)t and $\| \mathbf { r } ^ { ( 4 ) } \| _ { \infty } = 0 . 4 4 \times 1 0 ^ { - 9 }$ .

8. The Conjugate Gradient method with $C ^ { - 1 } = D ^ { - 1 / 2 }$ gives the following:

(a) x(3) = (0.06185567019, −0.1958762885, 0.6185567006)t and $\left\| \mathbf { r } ^ { ( 3 ) } \right\| _ { \infty } = 0 . 1 2 \times 1 0 ^ { - 8 }$   
\*(b) $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 9 5 7 8 9 4 7 3 9 , 0 . 9 5 7 8 9 4 7 3 6 8 , 0 . 7 9 1 5 7 8 9 4 7 5 ) ^ { t }$ and $\left\| \mathbf { r } ^ { ( 3 ) } \right\| _ { \infty } = 0 . 1 9 \times 1 0 ^ { - 8 }$   
(c) x(4) = (−0.7976470596, 2.795294118, −0.2588235287, −2.251764706)t and $\left\| \mathbf { r } ^ { ( 4 ) } \right\| _ { \infty } = 0 . 7 \times$ $1 0 ^ { - 8 }$   
(d) $\mathbf { x } ^ { ( 4 ) } = ( 0 . 6 1 6 4 3 8 3 5 6 0 , - 0 . 3 9 7 2 6 0 2 7 4 2 , 0 . 0 4 7 9 4 5 2 0 5 5 0 , - 0 . 0 2 0 5 4 7 9 4 5 2 5 ) ^ { t }$ and $\left\| \mathbf { r } ^ { ( 4 ) } \right\| _ { \infty } =$ 0.76 × 10−9   
(e) x(5) = (0.4516129026, 0.7096774190, 1.677419356, 1.741935484, 1.806451615)t and $\left\| \mathbf { r } ^ { ( 5 ) } \right\| _ { \infty } =$ $0 . 6 1 \times 1 0 ^ { - 1 0 }$   
(f) $\mathfrak { c } ^ { ( 4 ) } = ( 0 . 9 9 9 9 9 9 9 9 9 2 , 1 . 9 9 9 9 9 9 9 9 9 9 , 0 . 9 9 9 9 9 9 9 9 9 9 \mathfrak { c }$ 92, 2.000000000, 0.9999999989, 2.000000000)t and $\left\| \mathbf { r } ^ { ( 4 ) } \right\| _ { \infty } = 0 . 1 1 \times 1 0 ^ { - 9 }$

9. Approximations to within $1 0 ^ { - 5 }$ in the $l _ { i n f t y }$ are shown in the tables.

<table><tr><td>(a)</td><td>Jacobi 49 iterations</td><td>Gauss-Seidel 28 iterations</td><td>SOR (ω = 1.3) 13 iterations</td><td>Conjugate Gradient 9 iterations</td></tr><tr><td>x1</td><td>0.93406183</td><td>0.93406917</td><td>0.93407584</td><td>0.93407713</td></tr><tr><td>x2</td><td>0.97473885</td><td>0.97475285</td><td>0.97476180</td><td>0.97476363</td></tr><tr><td>x3</td><td>1.10688692</td><td>1.10690302</td><td>1.10691093</td><td>1.10691243</td></tr><tr><td>X4</td><td>1.42346150</td><td>1.42347226</td><td>1.42347591</td><td>1.42347699</td></tr><tr><td>X5</td><td>0.85931331</td><td>0.85932730</td><td>0.85933633</td><td>0.85933790</td></tr><tr><td>X6</td><td>0.80688119</td><td>0.80690725</td><td>0.80691961</td><td>0.80692197</td></tr><tr><td>X7</td><td>0.85367746</td><td>0.85370564</td><td>0.85371536</td><td>0.85372011</td></tr><tr><td>x8</td><td>1.10688692</td><td>1.10690579</td><td>1.10691075</td><td>1.10691250</td></tr><tr><td>xg</td><td>0.87672774</td><td>0.87674384</td><td>0.87675177</td><td>0.87675250</td></tr><tr><td>X10</td><td>0.80424512</td><td>0.80427330</td><td>0.80428301</td><td>0.80428524</td></tr><tr><td>X11</td><td>0.80688119</td><td>0.80691173</td><td>0.80691989</td><td>0.80692252</td></tr><tr><td>X12</td><td>0.97473885</td><td>0.97475850</td><td>0.97476265</td><td>0.97476392</td></tr><tr><td>X13</td><td>0.93003466</td><td>0.93004542</td><td>0.93004899</td><td>0.93004987</td></tr><tr><td>X14</td><td>0.87672774</td><td>0.87674661</td><td>0.87675155</td><td>0.87675298</td></tr><tr><td>X15</td><td>0.85931331</td><td>0.85933296</td><td>0.85933709</td><td>0.85933979</td></tr><tr><td>X16</td><td>0.93406183</td><td>0.93407462</td><td>0.93407672</td><td>0.93407768</td></tr><tr><td>(b)</td><td>Jacobi 60 iterations</td><td>Gauss-Seidel 35 iterations</td><td>SOR (ω = 1.2) 23 iterations</td><td>Conjugate Gradient 11 iterations</td></tr><tr><td>x1</td><td>0.39668038</td><td>0.39668651</td><td>0.39668915</td><td>0.39669775</td></tr><tr><td>x2</td><td>0.07175540</td><td>0.07176830</td><td>0.07177348</td><td>0.07178516</td></tr><tr><td>x3</td><td>-0.23080396</td><td>-0.23078609</td><td>-0.23077981</td><td>-0.23076923</td></tr><tr><td>X4</td><td>0.24549277</td><td>0.24550989</td><td>0.24551535</td><td>0.24552253</td></tr><tr><td>x5</td><td>0.83405412</td><td>0.83406516</td><td>0.83406823</td><td>0.83407148</td></tr><tr><td>X6</td><td>0.51497606</td><td>0.51498897</td><td>0.51499414</td><td>0.51500583</td></tr><tr><td>X7</td><td>0.12116003</td><td>0.12118683</td><td>0.12119625</td><td>0.12121212</td></tr><tr><td>x8</td><td>-0.24044414</td><td>-0.24040991</td><td>-0.24039898</td><td>-0.24038462</td></tr><tr><td>x9</td><td>0.37873579</td><td>0.37876891</td><td>0.37877812</td><td>0.37878788</td></tr><tr><td>X10</td><td>1.09073364</td><td>1.09075392</td><td>1.09075899</td><td>1.09076341</td></tr><tr><td>X11</td><td>0.54207872</td><td>0.54209658</td><td>0.54210286</td><td>0.54211344</td></tr><tr><td>X12</td><td>0.13838259</td><td>0.13841682</td><td>0.13842774</td><td>0.13844211</td></tr><tr><td>X13</td><td>-0.23083868</td><td>-0.23079452</td><td>-0.23078224</td><td>-0.23076923</td></tr><tr><td></td><td>0.41919067</td><td>0.41923122</td><td>0.41924136</td><td></td></tr><tr><td>X14</td><td>1.15015953</td><td></td><td>1.15019025</td><td>0.41925019</td></tr><tr><td>X15</td><td></td><td>1.15018477</td><td></td><td>1.15019425</td></tr><tr><td>X16</td><td>0.51497606 0.12116003</td><td>0.51499318</td><td>0.51499864</td><td>0.51500583</td></tr><tr><td>X17</td><td>-0.24044414</td><td>0.12119315</td><td>0.12120236</td><td>0.12121212</td></tr><tr><td>X18</td><td></td><td>-0.24040359</td><td>-0.24039345</td><td>-0.24038462</td></tr><tr><td>X19</td><td>0.37873579</td><td>0.37877365</td><td>0.37878188</td><td>0.37878788</td></tr><tr><td>X20</td><td>1.09073364</td><td>1.09075629</td><td>1.09076069</td><td>1.09076341</td></tr><tr><td>X21</td><td>0.39668038</td><td>0.39669142</td><td>0.39669449</td><td>0.39669775</td></tr><tr><td>X22</td><td>0.07175540</td><td>0.07177567</td><td>0.07178074</td><td>0.07178516</td></tr><tr><td>X23</td><td>-0.23080396</td><td>-0.23077872</td><td>-0.23077323 0.24551982</td><td>-0.23076923</td></tr><tr><td>X24</td><td>0.24549277</td><td>0.24551542</td><td></td><td>0.24552253</td></tr><tr><td>X25</td><td>0.83405412</td><td>0.83406793</td><td>0.83407025</td><td>0.83407148</td></tr><tr><td>(c）</td><td>Jacobi 15</td><td>Gauss-Seidel 9</td><td>SOR (ω = 1.1) 8</td><td>Conjugate Gradient 8</td></tr><tr><td></td><td>iterations</td><td>iterations</td><td>iterations</td><td>iterations</td></tr><tr><td>X1</td><td>-3.07611424</td><td>-3.07611739</td><td>-3.07611796</td><td>-3.07611794</td></tr><tr><td>X2</td><td>-1.65223176</td><td>-1.65223563</td><td>-1.65223579</td><td>-1.65223582</td></tr><tr><td>X3</td><td>-0.53282391</td><td>-0.53282528</td><td>-0.53282531</td><td>-0.53282528</td></tr><tr><td>X4</td><td>-0.04471548</td><td>-0.04471608</td><td>-0.04471609</td><td>-0.04471604</td></tr><tr><td>x5</td><td>0.17509673</td><td>0.17509661</td><td>0.17509661</td><td>0.17509661</td></tr><tr><td>X6</td><td>0.29568226</td><td>0.29568223</td><td>0.29568223</td><td>0.29568218</td></tr><tr><td>X7</td><td>0.37309012</td><td>0.37309011</td><td>0.37309011</td><td>0.37309011</td></tr><tr><td>X8</td><td>0.42757934</td><td>0.42757934</td><td>0.42757934</td><td>0.42757927</td></tr><tr><td>xg</td><td>0.46817927</td><td>0.46817927</td><td>0.46817927</td><td>0.46817927</td></tr><tr><td>X10</td><td>0.49964748</td><td>0.49964748</td><td>0.49964748</td><td>0.49964748</td></tr><tr><td>X11</td><td>0.52477026</td><td>0.52477026</td><td>0.52477026</td><td>0.52477027</td></tr><tr><td>X12</td><td>0.54529835</td><td>0.54529835</td><td>0.54529835</td><td>0.54529836</td></tr><tr><td>X13</td><td>0.56239007</td><td>0.56239007</td><td>0.56239007</td><td>0.56239009</td></tr><tr><td>X14</td><td>0.57684345</td><td>0.57684345</td><td>0.57684345</td><td>0.57684347</td></tr><tr><td>X15</td><td>0.58922662</td><td>0.58922662</td><td>0.58922662</td><td>0.58922664</td></tr><tr><td>X16</td><td>0.59995522</td><td>0.59995522</td><td>0.59995522</td><td>0.59995523</td></tr><tr><td>X17</td><td>0.60934045 0.61761997</td><td>0.60934045</td><td>0.60934045</td><td>0.60934045</td></tr><tr><td>X18</td><td></td><td>0.61761997</td><td>0.61761997</td><td>0.61761998</td></tr><tr><td>X19</td><td>0.62497846</td><td>0.62497846</td><td>0.62497846</td><td>0.62497847</td></tr><tr><td>X20</td><td>0.63156161 0.63748588</td><td>0.63156161</td><td>0.63156161</td><td>0.63156161</td></tr><tr><td>X21</td><td></td><td>0.63748588</td><td>0.63748588</td><td>0.63748588</td></tr><tr><td>X22</td><td>0.64284553</td><td>0.64284553</td><td>0.64284553</td><td>0.64284553</td></tr><tr><td>X23</td><td>0.64771764</td><td>0.64771764</td><td>0.64771764</td><td>0.64771764</td></tr><tr><td>X24</td><td>0.65216585</td><td>0.65216585</td><td>0.65216585</td><td>0.65216585</td></tr><tr><td>X25</td><td>0.65624320</td><td>0.65624320</td><td>0.65624320</td><td>0.65624320</td></tr><tr><td>X26</td><td>0.65999423</td><td>0.65999423</td><td>0.65999423</td><td>0.65999422</td></tr><tr><td>X27</td><td>0.66345660</td><td>0.66345660</td><td>0.66345660</td><td>0.66345660</td></tr><tr><td>X28</td><td>0.66666242</td><td>0.66666242</td><td>0.66666242</td><td>0.66666242</td></tr><tr><td>X29</td><td>0.66963919</td><td>0.66963919</td><td>0.66963919</td><td>0.66963919</td></tr><tr><td>x30</td><td>0.67241061</td><td>0.67241061</td><td>0.67241061</td><td>0.67241060</td></tr><tr><td>x31</td><td>0.67499722</td><td>0.67499722</td><td>0.67499722</td><td>0.67499721</td></tr><tr><td>X32</td><td>0.67741692</td><td>0.67741692</td><td>0.67741691</td><td>0.67741691</td></tr><tr><td>X33</td><td>0.67968535</td><td>0.67968535</td><td>0.67968535</td><td>0.67968535</td></tr><tr><td>X34</td><td>0.68181628</td><td>0.68181628</td><td>0.68181628</td><td>0.68181628</td></tr><tr><td>X35</td><td>0.68382184</td><td>0.68382184</td><td>0.68382184</td><td>0.68382184</td></tr><tr><td>X36</td><td>0.68571278</td><td>0.68571278</td><td>0.68571278</td><td>0.68571278</td></tr><tr><td>X37</td><td>0.68749864</td><td>0.68749864</td><td>0.68749864</td><td>0.68749864</td></tr><tr><td>x38</td><td>0.68918652</td><td>0.68918652</td><td>0.68918652</td><td>0.68918652</td></tr><tr><td>X39</td><td>0.69067718</td><td>0.69067718</td><td>0.69067718</td><td>0.69067717</td></tr><tr><td>X40</td><td>0.68363346</td><td>0.68363346</td><td>0.68363346</td><td>0.68363349</td></tr></table>

10. $n = 1 0$ : The solution vector is (0.90909091, 0.81818182, 0.72727273, 0.63636364, 0.54545455, 0.45454545, 0.36363636, 0.27272727, 0.18181818, 0.09090909)t, using 10 iterations with $\left\| \mathbf { r } ^ { ( 1 0 ) } \right\| _ { \infty } = 0$ .

$n = 5 0$ : The solution vector is

(0.98039216, 0.96078432, 0.94117648, 0.92156863, 0.90196079, 0.88235295, 0.86274511, 0.84313727, 0.82352943, 0.80392158, 0.78431374, 0.76470590, 0.74509806, 0.72549021, 0.70588237, 0.68627453, $0 . 6 6 6 6 6 6 6 6 8 8 , \ 0 . 6 4 7 0 5 8 8 4 , \ 0 . 6 5 2 7 4 5 1 0 1 0 , \ 0 . 6 0 7 8 4 3 1 5 , \ 0 . 5 8 8 2 3 5 3 3 1 , \ 0 . 5 6 8 6 2 7 4 7 , \ 0 . 5 4 9 0 1 9 6 2 , \ 0 . 5 2 9 9 2$ 41178, 0.50980394, 0.49019609, 0.47058825, 0.45098041, 0.43137256, 0.41176472, 0.39215688, 0.37254903, 0.35294119, 0.33333335, 0.31372550, 0.29411766, 0.27450981, 0.25490197, 0.23529413, 0.21568628, 0.19607844, 0.17647060, 0.15686275, 0.13725491, 0.11764706, 0.09803922, 0.07843138, 0.05882353, 0.03921569, 0.01960784)t, using 50 iterations with a tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in $l _ { \infty }$ and $\| \mathbf { r } ^ { ( 5 0 ) } \| _ { \infty } = 0$ .

$n = 1 0 0$ : The solution vector is

(0.99009901, 0.98019803, 0.97029704, 0.96039606, 0.95049507, 0.94059409, 0.93069310, 0.92079212,   
0.91089113, 0.90099014, 0.89108916, 0.88118817, 0.87128718, 0.86138620, 0.85148521, 0.84158422,   
0.83168323, 0.82178225, 0.81188126, 0.80198027, 0.79207928, 0.78217830, 0.77227731, 0.76237632,   
0.75247533, 0.74257434, 0.73267335, 0.72277237, 0.71287138, 0.70297039, 0.69306940, 0.68316841,   
0.67326742, 0.66336643, 0.65346544, 0.64356445, 0.63366347, 0.62376248, 0.61386149, 0.60396050,   
0.59405951, 0.58415852, 0.57425753, 0.56435654, 0.55445555, 0.54455456, 0.53465357, 0.52475258,   
0.51485159, 0.50495059, 0.49504960, 0.48514861, 0.47524762, 0.46534663, 0.45544564, 0.44554465,   
0.43564366, 0.42574267, 0.41584168, 0.40594068, 0.39603969, 0.38613870, 0.37623771, 0.36633672,   
0.3 $) 6 4 3 5 7 ( 3 , 0 . 3 4 6 5 3 4 / ( 4 , 0 . 3 3 6 6 3 3 / ( 4 , 0 . 3 3 2 6 / 3 2 7 ( 3 ) , 0 . 3 1 6 8 3 1 / ( 6 , 0 . 3 3 0 6 9 3 3 0 / ( , 0 . 2 9 ( 0 2 9 / 8 ) , 0 . 2 8 ( 1 . 2 8 ( 9 ) 9 ) )$   
0.2 $/ ( 2 2 2 / ( 9 , 0 . 2 2 6 / 3 2 6 8 0 , 0 . 2 5 ) / 4 2 5 8 8 1 , 0 . 2 4 / 3 2 4 8 2 , 0 . 2 3 / 6 2 3 8 3 , 0 . 2 2 / ( 7 2 2 8 3 , 0 . 2 1 / 8 2 1 8 4 , 0 . 2 0 / 9 2 0 8 3 ) ,$   
0.1 $)  \mathrm { S G I . S N S 6 , ~ 0 . 1 . N S K . I . N S S 6 , ~ 0 . 1 \cdot ( N Z 2 1 ^ { \prime } ( 8 ^ { \prime } , 0 . 1 6 8 3 4 1 6 8 8 , 0 . 1 5 3 8 4 1 5 8 5 9 , 0 . 1 4 8 5 1 . 4 8 5 ) . 1 4 8 5 9 , 0 . 1 . 3 3 8 6 1 3 9 0 , 0 . 1 . 2 8 ( 1 . 2 9 1 1 , 0 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 7 3 9 1 , 0 . 1 . 1 . 0 5 ) }$   
0.11881192, 0.10891092, 0.09900993, 0.08910894, 0.07920794, 0.06930695, 0.05940596, 0.04950497,   
0.03960397, 0.02970298, 0.01980199, 0.00990099)t,

using 100 iterations with a tolerance $1 . 0 0 \times 1 0 ^ { - 3 }$ in ${ \mathit { l } } _ { \infty }$ and $\left\| \mathbf { r } ^ { ( 1 0 0 ) } \right\| _ { \infty } = 0$

11. The Conjugate Gradient method gives the results in the following tables.

(a)

<table><tr><td>Solution</td><td>Residual</td></tr><tr><td>2.55613420</td><td>0.00668246</td></tr><tr><td>4.09171393</td><td>-0.00533953</td></tr><tr><td>4.60840390</td><td>-0.01739814</td></tr><tr><td>3.64309950</td><td>-0.03171624</td></tr><tr><td>5.13950533</td><td>0.01308093</td></tr><tr><td>7.19697808</td><td>-0.02081095</td></tr><tr><td>7.68140405</td><td>-0.04593118</td></tr><tr><td>5.93227784</td><td>0.01692180</td></tr><tr><td>5.81798997</td><td>0.04414047</td></tr><tr><td>5.85447806</td><td>0.03319707</td></tr><tr><td>5.94202521</td><td>-0.00099947</td></tr><tr><td>4.42152959</td><td>-0.00072826</td></tr><tr><td></td><td></td></tr><tr><td>3.32211695</td><td>0.02363822</td></tr><tr><td>4.49411604</td><td>0.00982052</td></tr><tr><td></td><td></td></tr><tr><td></td><td></td></tr><tr><td>4.80968966</td><td>0.00846967</td></tr><tr><td></td><td></td></tr><tr><td>3.81108707</td><td>-0.01312902</td></tr></table>

This converges in 6 iterations with tolerance $5 . 0 0 \times 1 0 ^ { - 2 }$ in the ${ \mathit { l } } _ { \infty }$ norm and $\| \mathbf { r } ^ { ( 6 ) } \| _ { \infty } =$ 0.046.

(b)

<table><tr><td>Solution</td><td>Residual</td></tr><tr><td>2.55613420</td><td>0.00668246</td></tr><tr><td>4.09171393</td><td>-0.00533953</td></tr><tr><td>4.60840390</td><td>-0.01739814</td></tr><tr><td>3.64309950</td><td>-0.03171624</td></tr><tr><td>5.13950533</td><td>0.01308093</td></tr><tr><td>7.19697808</td><td>-0.02081095</td></tr><tr><td>7.68140405</td><td>-0.04593118</td></tr><tr><td>5.93227784</td><td>0.01692180</td></tr><tr><td>5.81798996</td><td>0.04414047</td></tr><tr><td>5.85447805</td><td>0.03319706</td></tr><tr><td>5.94202521</td><td>-0.00099947</td></tr><tr><td>4.42152959</td><td>-0.00072826</td></tr><tr><td>3.32211694</td><td>0.02363822</td></tr><tr><td></td><td></td></tr><tr><td>4.49411603</td><td>0.00982052</td></tr><tr><td>4.80968966</td><td>0.00846967</td></tr><tr><td></td><td></td></tr><tr><td>3.81108707</td><td>-0.01312902</td></tr></table>

This converges in 6 iterations with tolerance $5 . 0 0 \times 1 0 ^ { - 2 }$ in the ${ \mathit { l } } _ { \infty }$ norm and $\| \mathbf { r } ^ { ( 6 ) } \| _ { \infty } =$ 0.046.

(c) All tolerances lead to the same convergence specifications.

$^ { \ast } 1 2$ . With $\langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } \mathbf { y }$ , we have

$$
\langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } \mathbf { y } = \mathbf { y } ^ { t } \mathbf { x } = \langle \mathbf { y } , \mathbf { x } \rangle ;
$$

$$
\langle c \mathbf { x } , \mathbf { y } \rangle = ( c \mathbf { x } ) ^ { t } \mathbf { y } = c \mathbf { x } ^ { t } \mathbf { y } = c \langle \mathbf { x } , \mathbf { y } \rangle = \mathbf { x } ^ { t } c \mathbf { y } = \langle \mathbf { x } , c \mathbf { y } \rangle ;
$$

$$
\langle \mathbf { x } + \mathbf { z } , \mathbf { y } \rangle = ( \mathbf { x } + \mathbf { z } ) ^ { t } \mathbf { y } = \left( \mathbf { x } ^ { t } + \mathbf { z } ^ { t } \right) \mathbf { y } = \mathbf { x } ^ { t } \mathbf { y } + \mathbf { z } ^ { t } \mathbf { y } = \langle \mathbf { x } , \mathbf { y } \rangle + \langle \mathbf { z } , \mathbf { y } \rangle ;
$$

$$
\langle \mathbf { x } , \mathbf { x } \rangle = \mathbf { x } ^ { t } \mathbf { x } = \| \mathbf { x } \| _ { 2 } ^ { 2 } \geq 0 .
$$

We show (v) as follows:

If $\langle \mathbf { x } , \mathbf { x } \rangle = \| \mathbf { x } \| _ { 2 } ^ { 2 } = 0$ , then $\mathbf x = \mathbf 0$ by the properties of norms. If $\mathbf x = \mathbf 0$ , then $0 = \mathbf { x } ^ { t } \mathbf { x } = \langle \mathbf { x } , \mathbf { x } \rangle$ .

13. (a) Let $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ be a set of nonzero $A$ -orthogonal vectors for the symmetric positive definite matrix $A$ . Then $\langle \mathbf { v } ^ { ( i ) } , A \mathbf { v } ^ { ( j ) } \rangle = 0$ , if $i \neq j$ . Suppose

$$
c _ { 1 } \mathbf { v } ^ { ( 1 ) } + c _ { 2 } \mathbf { v } ^ { ( 2 ) } + \cdot \cdot \cdot + c _ { n } \mathbf { v } ^ { ( n ) } = \mathbf { 0 } ,
$$

where not all $c _ { i }$ are zero. Suppose $k$ is the smallest integer for which $c _ { k } \neq 0$ . Then

$$
c _ { k } \mathbf { v } ^ { ( k ) } + c _ { k + 1 } \mathbf { v } ^ { ( k + 1 ) } + \cdot \cdot \cdot + c _ { n } \mathbf { v } ^ { ( n ) } = \mathbf { 0 } .
$$

We solve for $\mathbf { v } ^ { ( k ) }$ to obtain

$$
\mathbf { v } ^ { ( k ) } = - { \frac { c _ { k + 1 } } { c _ { k } } } \mathbf { v } ^ { ( k + 1 ) } - \cdot \cdot \cdot - { \frac { c _ { n } } { c _ { k } } } \mathbf { v } ^ { ( n ) } .
$$

Multiplying by $A$ gives

$$
A \mathbf { v } ^ { ( k ) } = - { \frac { c _ { k + 1 } } { c _ { k } } } A \mathbf { v } ^ { ( k + 1 ) } - \cdot \cdot \cdot - { \frac { c _ { n } } { c _ { k } } } A \mathbf { v } ^ { ( n ) } ,
$$

so

$$
\begin{array} { r c l } { ( { \mathbf v } ^ { ( k ) } ) ^ { t } A { \mathbf v } ^ { ( k ) } } & { = } & { - \frac { c _ { k + 1 } } { c _ { k } } ( { \mathbf v } ^ { ( k ) } ) ^ { t } A { \mathbf v } ^ { ( k + 1 ) } - \cdot \cdot \cdot - \frac { c _ { n } } { c _ { k } } ( { \mathbf v } ^ { ( k ) t } ) A { \mathbf v } ^ { ( n ) } } \\ & { = } & { - \frac { c _ { k + 1 } } { c _ { k } } \langle { \mathbf v } ^ { ( k ) } , A { \mathbf v } ^ { ( k + 1 ) } \rangle - \cdot \cdot \cdot - \frac { c _ { n } } { c _ { k } } \langle { \mathbf v } ^ { ( k ) } , A { \mathbf v } ^ { ( n ) } \rangle } \\ & { = } & { - \frac { c _ { k + 1 } } { c _ { k } } \cdot 0 - \cdot \cdot \cdot - \frac { c _ { n } } { c _ { k } } \cdot 0 = 0 . } \end{array}
$$

Since $A$ is positive definite, $\mathbf { v } ^ { ( k ) } = \mathbf { 0 }$ , which is a contradiction. Thus, all the $c _ { i }$ must be zero, and $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ is linearly independent.

(b) Let $\{ \mathbf { v } ^ { ( 1 ) } , \ldots , \mathbf { v } ^ { ( n ) } \}$ be a set of nonzero $A$ -orthogonal vectors for the symmetric positive definite matrix $A$ , and let $\mathbf { z }$ be orthogonal to $\mathbf { v } ^ { ( i ) }$ , for each $i = 1 , \ldots , n$ . From part (a), the set $\{ \mathbf { v } ^ { ( 1 ) } , \ldots \mathbf { v } ^ { ( n ) } \}$ is linearly independent, so there is a collection of constants $\beta _ { 1 } , \ldots , \beta _ { n }$ with

$$
\mathbf { z } = \sum _ { i = 1 } ^ { n } \beta _ { i } \mathbf { v } ^ { ( i ) } .
$$

Hence,

$$
\langle \mathbf { z } , \mathbf { z } \rangle = \mathbf { z } ^ { t } \mathbf { z } = \sum _ { i = 1 } ^ { n } \beta _ { i } \mathbf { z } ^ { t } \mathbf { v } ^ { ( i ) } = \sum _ { i = 1 } ^ { n } \beta _ { i } \cdot 0 = 0 ,
$$

and Theorem 7.30, part (e), implies that $\mathbf { z } = \mathbf { 0 }$ .

\*14. To prove Theorem 7.33 by mathematical induction:

(a) First note that we have

$$
\mathbf { x } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } + t _ { 1 } \mathbf { v } ^ { ( 1 ) } = \mathbf { x } ^ { ( 0 ) } + \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } \mathbf { v } ^ { ( 1 ) } .
$$

Thus

$$
A \mathbf { x } ^ { ( 1 ) } = A \mathbf { x } ^ { ( 0 ) } + \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } A \mathbf { v } ^ { ( 1 ) }
$$

and

$$
{ \bf b } - A { \bf x } ^ { ( 1 ) } = { \bf b } - A { \bf x } ^ { ( 0 ) } - \frac { \left. { \bf v } ^ { ( 1 ) } , { \bf r } ^ { ( 0 ) } \right. } { \left. { \bf v } ^ { ( 1 ) } , A { \bf v } ^ { ( 1 ) } \right. } A { \bf v } ^ { ( 1 ) } .
$$

Hence,

$$
\mathbf { r } ^ { ( 1 ) } = \mathbf { r } ^ { ( 0 ) } - \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } A \mathbf { v } ^ { ( 1 ) } .
$$

Taking the inner product with $\mathbf { v } ^ { ( 1 ) }$ gives

$$
\begin{array} { r l } & { \left. \mathbf { r } ^ { ( 1 ) } , \mathbf { v } ^ { ( 1 ) } \right. = \left. \mathbf { r } ^ { ( 0 ) } , \mathbf { v } ^ { ( 1 ) } \right. - \frac { \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. } { \left. \mathbf { v } ^ { ( 1 ) } , A \mathbf { v } ^ { ( 1 ) } \right. } \left. A \mathbf { v } ^ { ( 1 ) } , \mathbf { v } ^ { ( 1 ) } \right. } \\ & { \qquad = \left. \mathbf { r } ^ { ( 0 ) } , \mathbf { v } ^ { ( 1 ) } \right. - \left. \mathbf { v } ^ { ( 1 ) } , \mathbf { r } ^ { ( 0 ) } \right. = 0 . } \end{array}
$$

This establishes the base step.

(b) For the inductive hypothesis we assume that $\left. \mathbf { r } ^ { ( k ) } , \mathbf { v } ^ { ( j ) } \right. = 0$ , for all $k \ \leq \ l$ and $j ~ =$ $1 , 2 , \ldots , k$ . We must then show

$$
\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( j ) } \right. = 0 , \quad \mathrm { f o r } \quad j = 1 , 2 , \ldots , l + 1 .
$$

We do this in two parts.

First, for $j = 1 , 2 , \dots , l$ , we will show that $\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( j ) } \right. = 0$ . We have

$$
\begin{array} { r l } & { \mathbf { x } ^ { ( l + 1 ) } = \mathbf { x } ^ { ( l ) } + t _ { l + 1 } \mathbf { v } ^ { ( l + 1 ) } } \\ & { \quad \quad = \mathbf { x } ^ { ( l ) } + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } \mathbf { v } ^ { ( l + 1 ) } , } \end{array}
$$

so

$$
A \mathbf { x } ^ { ( l + 1 ) } = A \mathbf { x } ^ { ( l ) } + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } A \mathbf { v } ^ { ( l + 1 ) } .
$$

Subtracting $\mathbf { b }$ from both sides gives

$$
- \mathbf { r } ^ { ( l + 1 ) } = - \mathbf { r } ^ { ( l ) } + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } A \mathbf { v } ^ { ( l + 1 ) } .
$$

Taking the inner product of both sides of (2) with $\mathbf { v } ^ { ( i ) }$ gives

$$
- \left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right. = - \left. \mathbf { r } ^ { ( l ) } , \mathbf { v } ^ { ( i ) } \right. + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } \left. A \mathbf { v } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right. .
$$

The first term on the right-hand side of (3) is $0$ by the inductive hypothesis, and the factor $\left. A \mathbf { v } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right.$ is $0$ because of $A$ -orthogonality. Thus, $\left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( i ) } \right. = 0$ , for $1 , 2 , \ldots , l$ .

(c) For the second part we take the inner product of both sides of (2) with $\mathbf { v } ^ { ( l + 1 ) }$ to obtain

$$
- \left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. = - \left. \mathbf { r } ^ { ( l ) } , \mathbf { v } ^ { ( l + 1 ) } \right. + \frac { \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. } { \left. \mathbf { v } ^ { ( l + 1 ) } , A \mathbf { v } ^ { ( l + 1 ) } \right. } \left. A \mathbf { v } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. .
$$

Thus,

$$
- \left. \mathbf { r } ^ { ( l + 1 ) } , \mathbf { v } ^ { ( l + 1 ) } \right. = - \left. \mathbf { r } ^ { ( l ) } , \mathbf { v } ^ { ( l + 1 ) } \right. + \left. \mathbf { v } ^ { ( l + 1 ) } , \mathbf { r } ^ { ( l ) } \right. = 0 .
$$

This completes the proof by induction.

15. If $A$ is a positive definite matrix whose eigenvalues are $0 < \lambda _ { 1 } \leq \cdot \cdot \cdot \leq \lambda _ { n }$ , then $| | { \cal { A } } | | _ { 2 } = \lambda _ { n }$ and $| | A ^ { - 1 } | | _ { 2 } = 1 / \lambda _ { 1 }$ , so $K _ { 2 } ( A ) = \lambda _ { n } / \lambda _ { 1 }$ .

For the matrix $A$ in Example 3 we have

$$
K _ { 2 } ( A ) = { \frac { \lambda _ { 5 } } { \lambda _ { 1 } } } = { \frac { 7 0 0 . 0 3 1 } { 0 . 0 5 7 0 7 3 7 } } = 1 2 2 6 5 . 2 ,
$$

and the matrix $A H$ has

$$
K _ { 2 } ( A H ) = { \frac { \lambda _ { 5 } } { \lambda _ { 1 } } } = { \frac { 1 . 8 8 0 5 2 } { 0 . 1 5 6 3 7 0 } } = 1 2 . 0 2 6 1 .
$$

Maple gives ConditionNumber $\mathbf { \sigma } \cdot ( A , 2 ) = 1 2 2 6 5 . 1 5 9 1 4$ and ConditionNumber $\cdot ( A H , 2 ) = 1 2 . 0 2 5 9 8 1 2 4$

# Approximation Theory

# Exercise Set 8.1, page 506

$^ { * } 1$ . The linear least-squares polynomial is $1 . 7 0 7 8 4 x + 0 . 8 9 9 6 8$ .   
$^ { * 2 }$ . The least-squares polynomial of degree two is $P _ { 2 } ( x ) = 0 . 4 0 6 6 6 6 7 + 1 . 1 5 4 8 4 8 x + 0 . 0 3 4 8 4 8 4 8 x ^ { . }$ 2, with $E = 1 . 7 0 3 5$ .   
3. The least-squares polynomials with their errors are, respectively, $0 . 6 \dot { 2 } 0 8 9 5 0 + 1 . 2 1 9 6 \dot { 2 } 1 x$ , with $E = 2 . 7 1 9 \times 1 0 ^ { - 5 }$ ; $0 . 5 9 6 5 8 0 7 + 1 . 2 5 3 2 9 3 x - 0 . 0 1 0 8 5 3 4 3 x ^ { 2 }$ , with $E = 1 . 8 0 1 \times 1 0 ^ { - 5 }$ ; and 0.629019 $3 + 1 . 1 8 5 0 1 0 x + 0 . 0 3 5 3 3 2 5 2 x ^ { 2 } - 0 . 0 1 0 0 4 7 2 3 x ^ { 3 }$ , with $E = 1 . 7 4 1 \times 1 0 ^ { - 5 }$ .   
4. The least-squares polynomials with their errors are, respectively, $P _ { 1 } ( x ) = 0 . 9 2 9 5 1 4 0 + 0 . 5 2 8 1 0 2 1 x$ , with $2 . 4 5 7 \times 1 0 ^ { - 2 }$ ; $P _ { 2 } ( x ) = 1 . 0 1 1 3 4 1 - 0 . 3 2 5 6 9 8 8 x + 1 . 1 4 7 3 3 0 x ^ { 2 }$ , with $9 . 4 5 3 \times 1 0 ^ { - 4 }$ ; $P _ { 3 } ( x ) = 1 . 0 0 0 4 4 0 - 0 . 0 0 1 5 4 0 9 8 6 x - 0 . 0 1 1 5 0 5 6 7 5 x ^ { 2 } + 1 . 0 2 1 0 2 3 x ^ { 3 }$ with $1 . 1 1 2 \times 1 0 ^ { - 4 }$ .   
5. (a) The linear least-squares polynomial is $7 2 . 0 8 4 5 x - 1 9 4 . 1 3 8$ , with error 329. (b) The least-squares polynomial of degree two is $6 . 6 1 8 2 1 x ^ { 2 } - 1 . 1 4 3 5 2 x + 1 . 2 3 5 5 6$ , with error $1 . 4 4 \times 1 0 ^ { - 3 }$ . (c) The least-squares polynomial of degree three is $- 0 . 0 1 3 6 7 4 2 x ^ { 3 } + 6 . 8 4 5 5 7 x ^ { 2 } - 2 . 3 7 9 1 9 x +$ 3.42904, with error $5 . 2 7 \times 1 0 ^ { - 4 }$ . (d) The least-squares approximation of the form $b e ^ { a x }$ is $2 4 . 2 5 8 8 e ^ { 0 . 3 7 2 3 8 2 x }$ , with error 418. (e) The least-squares approximation of the form $b x ^ { a }$ is $6 . 2 3 9 0 3 x ^ { 2 . 0 1 9 5 4 }$ , with error 0.00703.   
6. (a) The linear least-squares polynomial is $P _ { 1 } ( x ) = 1 . 6 6 5 5 4 0 x - 0 . 5 1 2 4 5 6 8$ , with error 0.33559. (b) The least-squares polynomial of degree two is $P _ { 2 } ( x ) = 1 . 1 2 9 4 2 4 x ^ { 2 } - 0 . 3 1 1 4 0 3 5 x + 0 . 0 8 5 1 4 3 9 3$ with error $2 . 4 1 9 9 \times 1 0 ^ { - 3 }$ . (c) The least-squares polynomial of degree three is $P _ { 3 } ( x ) = 0 . 2 6 6 2 0 8 1 x ^ { 3 } + 0 . 4 0 2 9 3 2 2 x ^ { 2 } +$ $0 . 2 4 8 3 8 5 7 x - 0 . 0 1 8 4 0 1 4 0$ , with error $5 . 0 7 4 7 \times 1 0 ^ { - 6 }$ . (d) The least-squares approximation of the form $b e ^ { a x }$ is $f ( x ) = 0 . 0 4 5 7 0 7 4 8 e ^ { 2 . 7 0 7 2 9 5 x }$ , with error 1.0750. (e) The least-squares approximation of the form $b x ^ { a }$ is $f ( x ) = 0 . 9 5 0 1 5 6 5 x ^ { 1 . 8 / 2 0 0 9 }$ , with error 0.054477.

. (a) $k = 0 . 8 9 9 6 , \ E ( k ) = 0 . 2 9 5$ (b) $k = 0 . 9 0 5 2$ , $E ( k ) = 0 . 1 2 8$ Part (b) fits the total experimental data best.

$^ { * } 8$ . $P _ { 1 } ( x ) = 0 . 2 2 3 3 5 x - 0 . 8 0 2 8 3$ . For minimal $A$ , 406; for minimal $D$ , 272. The prediction for an $A$ is certainly unreasonable.

9. The least squares line for the point average is 0.101 (ACT score) + 0.487.

10. The percent occurrence is $- 0 . 0 0 2 2 5 5 0 x$ (average weight) $+ 1 3 . 1 4 6$ .

11. The linear least-squares polynomial gives $y \approx 0 . 1 7 9 5 2 x + 8 . 2 0 8 4$ .

12. The linear least-squares polynomial is $1 . 6 0 0 3 9 3 x + 2 5 . 9 2 1 7 5$

13. (a) $\ln R = \ln 1 . 3 0 4 + 0 . 5 7 5 6 \ln W$ (b) $E = 2 5 . 2 5$ (c) $\begin{array} { r l } & { \ln R = \ln 1 . 0 5 1 + 0 . 7 0 0 6 \ln W + 0 . 0 6 6 9 5 ( \ln W ) ^ { 2 } } \\ & { E = \sum _ { i = 1 } ^ { 3 7 } \Big ( R _ { i } - b W _ { i } ^ { a } e ^ { c ( \ln W _ { i } ) ^ { 2 } } \Big ) ^ { 2 } = 2 0 . 3 0 } \end{array}$ (d)

\*14. For each i = 1, . . . , n + 1 and j = 1, . . . , n + 1, aij = aji = Pmk=1 xi+jk , so $A = \left( a _ { i j } \right)$ is symmetric. Suppose $A$ is singular and $\mathbf c \neq \mathbf 0$ satisfies $\mathbf { c } ^ { t } A \mathbf { c } = \mathbf { 0 }$ . Then

$$
0 = \sum _ { i = 1 } ^ { n + 1 } \sum _ { j = 1 } ^ { n + 1 } a _ { i j } c _ { i } c _ { j } = \sum _ { i = 1 } ^ { n + 1 } \sum _ { j = 1 } ^ { n + 1 } \left( \sum _ { k = 1 } ^ { m } x _ { k } ^ { i + j - 2 } \right) c _ { i } c _ { j } = \sum _ { k = 1 } ^ { m } \left[ \sum _ { i = 1 } ^ { n + 1 } \sum _ { j = 1 } ^ { n + 1 } c _ { i } c _ { j } x _ { k } ^ { i + j - 2 } \right] ,
$$

so

$$
\sum _ { k = 1 } ^ { m } \left( \sum _ { i = 1 } ^ { n + 1 } c _ { i } x _ { k } ^ { i - 1 } \right) ^ { 2 } = 0 .
$$

Define $P ( x ) = c _ { 1 } + c _ { 2 } x + . . . + c _ { n + 1 } x ^ { n }$ . Then $\begin{array} { r } { \sum _ { k = 1 } ^ { m } \left[ P ( x _ { k } ) \right] ^ { 2 } = 0 } \end{array}$ and $P ( x )$ has roots $x _ { 1 } , \ldots , x _ { m }$ Since the roots are distinct and $m > n$ , $P ( x )$ must be the zero polynomial. Thus, $c _ { 1 } = c _ { 2 } =$ $\ldots = c _ { n + 1 } = 0$ , and $A$ must be nonsingular.

# Exercise Set 8.2, page 518

1. The linear least-squares approximations are:

(a) $P _ { 1 } ( x ) = 1 . 8 3 3 3 3 3 + 4 x$ $^ *$ (b) $P _ { 1 } ( x ) = - 1 . 6 0 0 0 0 3 + 3 . 6 0 0 0 0 3 x$ (c) $P _ { 1 } ( x ) = 1 . 1 4 0 9 8 1 - 0 . 2 9 5 8 3 7 5 x$ (d) $P _ { 1 } ( x ) = 0 . 1 9 4 5 2 6 7 + 3 . 0 0 0 0 0 1 x$ (e) $P _ { 1 } ( x ) = 0 . 6 1 0 9 2 4 5 + 0 . 0 9 1 6 7 1 0 5 x$ (f) $P _ { 1 } ( x ) = - 1 . 8 6 1 4 5 5 + 1 . 6 6 6 6 6 7 x$

2. The linear least-squares approximations on $[ - 1 , 1 ]$ are:

(a) $P _ { 1 } ( x ) = 3 . 3 3 3 3 3 3 - 2 x$ (b) $P _ { 1 } ( x ) = 0 . 6 0 0 0 0 2 5 x$ (c) $P _ { 1 } ( x ) = 0 . 5 4 9 3 0 6 3 - 0 . 2 9 5 8 3 7 5 x$ (d) $P _ { 1 } ( x ) = 1 . 1 7 5 2 0 1 + 1 . 1 0 3 6 3 9 x$ (e) $P _ { 1 } ( x ) = 0 . 4 2 0 7 3 5 5 + 0 . 4 3 5 3 9 7 5 x$ (f) $P _ { 1 } ( x ) = 0 . 6 4 7 9 1 8 4 + 0 . 5 2 8 1 2 2 6 x$

3. The least squares approximations of degree two are:

(a) $P _ { 2 } ( x ) = 2 + 3 x + x ^ { 2 } \equiv f ( x )$ \*(b) $P _ { 2 } ( x ) = 0 . 4 0 0 0 1 6 3 - 2 . 4 0 0 0 5 4 x + 3 . 0 0 0 0 2 8 x ^ { 2 }$ (c) $P _ { 2 } ( x ) = 1 . 7 2 3 5 5 1 - 0 . 9 3 1 3 6 8 2 x + 0 . 1 5 8 8 8 2 7 x ^ { 2 }$ 2 (d) $P _ { 2 } ( x ) = 1 . 1 6 7 1 7 9 + 0 . 0 8 2 0 4 4 4 2 x + 1 . 4 5 8 9 7 9 x$ 2 (e) $P _ { 2 } ( x ) = 0 . 4 8 8 0 0 5 8 + 0 . 8 2 9 1 8 3 0 x - 0 . 7 3 7 5 1 1 9 x ^ { 2 }$ (f) $P _ { 2 } ( x ) = - 0 . 9 0 8 9 5 2 3 + 0 . 6 2 7 5 7 2 3 x + 0 . 2 5 9 7 7 3 6 x ^ { 2 }$ 2

4. The least squares approximation of degree two on $[ - 1 , 1 ]$ are:

(a) $P _ { 2 } ( x ) = 3 - 2 x + 1 . 0 0 0 0 9 x ^ { 2 }$ (b) $P _ { 2 } ( x ) = 0 . 6 0 0 0 0 2 5 x$ (c) $^ { D } _ { 2 } ( x ) = 0 . 4 9 6 3 4 5 4 - 0 . 2 9 5 8 3 7 5 x + 0 . 1 5 8 8 8 2 7 x ^ { 2 }$ 2 (d) $^ { D } _ { 2 } ( x ) = 0 . 9 9 6 2 9 1 8 + 1 . 1 0 3 6 3 9 x + 0 . 5 3 6 7 2 8 2 x ^ { 2 }$ (e) $P _ { 2 } ( x ) = 0 . 4 9 8 2 7 9 8 + 0 . 4 3 5 3 9 7 5 x - 0 . 2 3 2 6 3 3 0 x ^ { 2 }$ 2 (f) $P _ { 2 } ( x ) = 0 . 6 9 4 7 8 9 8 + 0 . 5 2 8 1 2 2 6 x - 0 . 1 4 0 6 1 4 1 x ^ { \mathrm { i } }$ 2

5. The errors $E$ for the least squares approximations in Exercise 3 are:

(a) $0 . 3 4 2 7 \times 1 0 ^ { - 9 }$ \*(b) 0.0457142(c) 0.000358354(d) 0.0106445(e) 0.0000134621(f) 0.0000967795

6. The errors for the approximations in Exercise 4 are:

(a) 0   
(b) 0.0457206   
(c) 0.00035851   
(d) 0.0014082   
(e) 0.00575753   
(f) 0.00011949

7. The Gram-Schmidt process produces the following collections of polynomials:

$$
\begin{array} { l l l l } { { \phi _ { 0 } ( x ) = 1 , \phi _ { 1 } ( x ) = x - 0 . 5 , } } & { { \phi _ { 2 } ( x ) = x ^ { 2 } - x + \frac { 1 } { 6 } , } } & { { \mathrm { a n d } } } & { { \phi _ { 3 } ( x ) = x ^ { 3 } - 1 . 5 x ^ { 2 } + 0 . 6 x - 0 . 0 5 , } } \\ { { \phi _ { 0 } ( x ) = 1 , \phi _ { 1 } ( x ) = x - 1 , } } & { { \phi _ { 2 } ( x ) = x ^ { 2 } - 2 x + \frac { 2 } { 3 } , } } & { { \mathrm { a n d } } } & { { \phi _ { 3 } ( x ) = x ^ { 3 } - 3 x ^ { 2 } + \frac { 1 2 } { 5 } x - \frac { 2 } { 5 } x + \frac { 1 } { 6 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 2 } , } } \\ { { \phi _ { 0 } ( x ) = 1 , \phi _ { 1 } ( x ) = x - 2 , } } & { { \phi _ { 2 } ( x ) = x ^ { 2 } - 4 x + \frac { 1 1 } { 3 } , } } & { { \mathrm { a n d } } } & { { \phi _ { 3 } ( x ) = x ^ { 3 } - 6 x ^ { 2 } + 1 1 . 4 x - 6 . 8 5 . } } \end{array}
$$

8. The Gram-Schmidt process produces the following collections of polynomials.

(a) $3 . 8 3 3 3 3 3 \phi _ { 0 } ( x ) + 4 . 0 0 0 0 0 0 \phi _ { 1 } ( x )$ (b) $2 \phi _ { 0 } ( x ) + 3 . 6 \phi _ { 1 } ( x )$ (c) $0 . 5 4 9 3 0 6 1 \phi _ { 0 } ( x ) - 0 . 2 9 5 8 3 6 9 \phi _ { 1 } ( x )$ (d) $3 . 1 9 4 5 2 8 \phi _ { 0 } ( x ) + 3 \phi _ { 1 } ( x )$ (e) $0 . 6 5 6 7 6 0 0 \phi _ { 0 } ( x ) + 0 . 0 9 1 6 7 1 0 5 \phi _ { 1 } ( x )$ (f) $1 . 4 7 1 8 7 8 \phi _ { 0 } ( x ) + 1 . 6 6 6 6 6 7 \phi _ { 1 } ( x )$

9. The least-squares polynomials of degree three are:

(a) $P _ { 3 } ( x ) = 3 . 8 3 3 3 3 4 \phi _ { 0 } ( x ) + 4 . 0 0 0 0 0 0 \phi _ { 1 } ( x ) + 0 . 9 9 9 9 9 8 \phi _ { 2 } ( x )$ \*(b) $P _ { 3 } ( x ) = 2 \phi _ { 0 } ( x ) + 3 . 6 \phi _ { 1 } ( x ) + 3 \phi _ { 2 } ( x ) + \phi _ { 3 } ( x )$ (c) $P _ { 3 } ( x ) = 0 . 5 4 9 3 0 6 1 \phi _ { 0 } ( x ) - 0 . 2 9 5 8 3 6 9 \phi _ { 1 } ( x ) + 0 . 1 5 8 8 7 8 5 \phi _ { 2 } ( x ) - 0 . 0 8 5 2 4 4 7 0 \phi _ { 3 } ( x )$ (d) $P _ { 3 } ( x ) = 3 . 1 9 4 5 2 8 \phi _ { 0 } ( x ) + 3 \phi _ { 1 } ( x ) + 1 . 4 5 8 9 6 0 \phi _ { 2 } ( x ) + 0 . 4 7 8 7 9 5 9 \phi _ { 3 } ( x )$ (e) $P _ { 3 } ( x ) = 0 . 6 5 6 7 6 0 0 \phi _ { 0 } ( x ) + 0 . 0 9 1 6 7 1 0 5 \phi _ { 1 } ( x ) - 0 . 7 3 7 5 1 1 8 \phi _ { 2 } ( x ) - 0 . 1 8 7 6 9 5 2 \phi _ { 3 } ( x )$ ) (f) $P _ { 3 } ( x ) = 1 . 4 7 1 8 7 8 \phi _ { 0 } ( x ) + 1 . 6 6 6 6 7 \phi _ { 1 } ( x ) + 0 . 2 5 9 7 7 0 5 \phi _ { 2 } ( x ) - 0 . 0 4 5 5 9 6 1 1 \phi _ { 3 } ( x )$

10. The least-squares polynomials of degree two are:

(a) $P _ { 2 } ( x ) = 3 . 8 3 3 3 3 3 \phi _ { 0 } ( x ) + 4 \phi _ { 1 } ( x ) + 0 . 9 9 9 9 9 9 8 \phi _ { 2 } ( x )$ (b) $P _ { 2 } ( x ) = 2 \phi _ { 0 } ( x ) + 3 . 6 \phi _ { 1 } ( x ) + 3 \phi _ { 2 } ( x )$ (c) $P _ { 2 } ( x ) = 0 . 5 4 9 3 0 6 1 \phi _ { 0 } ( x ) - 0 . 2 9 5 8 3 6 9 \phi _ { 1 } ( x ) + 0 . 1 5 8 8 7 8 5 \phi _ { 2 } ( x )$ (d) $P _ { 2 } ( x ) = 3 . 1 9 4 5 2 8 \phi _ { 0 } ( x ) + 3 \phi _ { 1 } ( x ) + 1 . 4 5 8 9 6 0 \phi _ { 2 } ( x )$ (e) $P _ { 2 } ( x ) = 0 . 6 5 6 7 6 0 0 \phi _ { 0 } ( x ) + 0 . 0 9 1 6 7 1 0 5 \phi _ { 1 } ( x ) - 0 . 7 3 7 5 1 2 1 8 \phi _ { 2 } ( x )$ ) (f) $P _ { 2 } ( x ) = 1 . 4 7 1 8 7 8 \phi _ { 0 } ( x ) + 1 . 6 6 6 6 6 7 \phi _ { 1 } ( x ) + 0 . 2 5 9 7 7 0 5 \phi _ { 2 } ( x )$

11. The Laguerre polynomials are $L _ { 1 } ( x ) = x - 1$ , $L _ { 2 } ( x ) = x ^ { 2 } - 4 x + 2$ and $L _ { 3 } ( x ) = x ^ { 3 } - 9 x ^ { 2 } + 1 8 x - 6$ .

12. The least-squares polynomials of degrees one, two, and three are:

(a) $2 L _ { 0 } ( x ) + 4 L _ { 1 } ( x ) + L _ { 2 } ( x )$ (b) $\begin{array} { r } { \frac { 1 } { 2 } L _ { 0 } ( x ) - \frac { 1 } { 4 } L _ { 1 } ( x ) + \frac { 1 } { 1 6 } L _ { 2 } ( x ) - \frac { 1 } { 9 6 } L _ { 3 } ( x ) } \end{array}$ (c) $6 L _ { 0 } ( x ) + 1 8 L _ { 1 } ( x ) + 9 L _ { 2 } ( x ) + L _ { 3 } ( x )$ (d) $\textstyle { \frac { 1 } { 3 } } L _ { 0 } ( x ) - { \frac { 2 } { 9 } } L _ { 1 } ( x ) + { \frac { 2 } { 2 7 } } L _ { 2 } ( x ) - { \frac { 4 } { 2 4 3 } } L _ { 3 } ( x )$

\*13. Let $i = 0 , 1 , \ldots , n$ $\{ \phi _ { 0 } ( x ) , \phi _ { 1 } ( x ) , \ldots , \phi _ { n } ( x ) \}$ , let $\begin{array} { r } { \phi _ { i } ( x ) \ : = \ : \sum _ { k = 0 } ^ { n } b _ { k i } x ^ { k } } \end{array}$ be a linearly independent set of polynomials in . Let $\begin{array} { r } { Q ( x ) \ = \ \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } \ \in \ \prod _ { n } } \end{array}$ n. We want to find $\prod _ { n }$ . For each constants $c _ { 0 } , \ldots , c _ { n }$ so that

$$
Q ( x ) = \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ( x ) .
$$

This equation becomes

$$
\sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { i = 0 } ^ { n } c _ { i } \left( \sum _ { k = 0 } ^ { n } b _ { k i } x ^ { k } \right) 
$$

so we have both

$$
\sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { k = 0 } ^ { n } \left( \sum _ { i = 0 } ^ { n } c _ { i } b _ { k i } \right) x ^ { k } , \quad { \mathrm { a n d } } \quad \sum _ { k = 0 } ^ { n } a _ { k } x ^ { k } = \sum _ { k = 0 } ^ { n } \left( \sum _ { i = 0 } ^ { n } b _ { k i } c _ { i } \right) x ^ { k } .
$$

But $\{ 1 , x , \ldots , x ^ { n } \}$ is linearly independent, so, for each $k = 0 , \ldots , n$ , we have

$$
\sum _ { i = 0 } ^ { n } b _ { k i } c _ { i } = a _ { k } ,
$$

which expands to the linear system

$$
{ \left[ \begin{array} { l l l l } { b _ { 0 1 } } & { b _ { 0 2 } } & { \cdots } & { b _ { 0 n } } \\ { b _ { 1 1 } } & { b _ { 1 2 } } & { \cdots } & { b _ { 1 n } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { b _ { n 1 } } & { b _ { n 2 } } & { \cdots } & { b _ { n n } } \\ { } & { } & { } & { } \end{array} \right] } \quad { \left[ \begin{array} { l } { c _ { 0 } } \\ { c _ { 1 } } \\ { \vdots } \\ { c _ { n } } \end{array} \right] } = { \left[ \begin{array} { l } { a _ { 0 } } \\ { a _ { 1 } } \\ { \vdots } \\ { a _ { n } } \end{array} \right] } .
$$

This linear system must have a unique solution $\{ c _ { 0 } , c _ { 1 } , \ldots , c _ { n } \}$ , or else there is a nontrivial set of constants $\{ c _ { 0 } ^ { \prime } , c _ { 1 } ^ { \prime } , \ldots , c _ { n } ^ { \prime } \}$ , for which

$$
{ \begin{array} { r l } { \left[ b _ { 0 1 } \quad \cdot \cdot \cdot \right]} & { b _ { 0 n } } \\ { \vdots } & { \vdots } \\ { b _ { n 1 } \quad \cdot \cdot \cdot } & { b _ { n n } } \end{array}  } &  { \Bigg [ } { \begin{array} { l } { c _ { 0 } ^ { \prime } } \\ { \vdots } \\ { c _ { n } ^ { \prime } } \end{array} } { \Bigg ] } = { \Bigg [ } { \begin{array} { l } { 0 } \\ { \vdots } \\ { 0 } \end{array} } { \Bigg ] } ~ .
$$

Thus

$$
c _ { 0 } ^ { \prime } \phi _ { 0 } ( x ) + c _ { 1 } ^ { \prime } \phi _ { 1 } ( x ) + \ldots + c _ { n } ^ { \prime } \phi _ { n } ( x ) = \sum _ { k = 0 } ^ { n } 0 x ^ { k } = 0 ,
$$

which contradicts the linear independence of the set $\{ \phi _ { 0 } , . . . , \phi _ { n } \}$ . Thus, there is a unique set of constants $\{ c _ { 0 } , \ldots , c _ { n } \}$ , for which

$$
Q ( x ) = c _ { 0 } \phi _ { 0 } ( x ) + c _ { 1 } \phi _ { 1 } ( x ) + . . . + c _ { n } \phi _ { n } ( x ) .
$$

$^ { * } 1 4$ . If $\textstyle \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ( x ) = 0$ , for all $a \leq x \leq b$ , then

$$
\int _ { a } ^ { b } \left( \sum _ { i = 0 } ^ { n } c _ { i } \phi _ { i } ( x ) \right) \phi _ { j } ( x ) w ( x ) d x = 0 , \quad { \mathrm { f o r ~ e a c h ~ } } j = 0 , 1 , \dots , n .
$$

Thus, $c _ { j } = 0$ , for each $j = 0 , 1 , \dotsc , n$ .

15. The normal equations are

$$
\sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = \int _ { a } ^ { b } x ^ { j } f ( x ) d x , \quad { \mathrm { f o r ~ e a c h } } \ j = 0 , 1 , \dots , n .
$$

Let

$$
b _ { j k } = \int _ { a } ^ { b } x ^ { j + k } d x , \quad { \mathrm { f o r ~ e a c h } } \ j = 0 , \dots , n , \quad { \mathrm { a n d } } \quad k = 0 , \dots , n ,
$$

and let $B = \left( b _ { j k } \right)$ . Further, let

$$
\mathbf { a } = ( a _ { 0 } , \ldots , a _ { n } ) ^ { t } \quad { \mathrm { a n d } } \quad \mathbf { g } = \left( \int _ { a } ^ { b } f ( x ) d x , \ldots , \int _ { a } ^ { b } x ^ { n } f ( x ) d x \right) ^ { t } .
$$

Then the normal equations produce the linear system $B \mathbf { a } = \mathbf { g }$ .

To show that the normal equations have a unique solution, it suffices to show that if $f \equiv 0$ then $\mathbf { a } = \mathbf { 0 }$ . If $f \equiv 0$ , then

$$
\sum _ { k = 0 } ^ { n } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = 0 , \quad \mathrm { f o r } j = 0 , \dots , n , \quad \mathrm { a n d } \quad \sum _ { k = 0 } ^ { n } a _ { j } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = 0 , \quad \mathrm { f o r } j = 0 , \dots , n
$$

and summing over $j$ gives

$$
\sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } a _ { j } a _ { k } \int _ { a } ^ { b } x ^ { j + k } d x = 0 .
$$

Thus

$$
\int _ { a } ^ { b } \sum _ { j = 0 } ^ { n } \sum _ { k = 0 } ^ { n } a _ { j } x ^ { j } a _ { k } x ^ { k } d x = 0 \quad { \mathrm { a n d } } \quad \int _ { a } ^ { b } { \biggl ( } \sum _ { j = 0 } ^ { n } a _ { j } x ^ { j } { \biggr ) } ^ { 2 } d x = 0 .
$$

Define $P ( x ) = a _ { 0 } + a _ { 1 } x + \cdot \cdot \cdot + a _ { n } x ^ { n }$ . Then $\begin{array} { r } { \int _ { a } ^ { b } \left[ P ( x ) \right] ^ { 2 } d x = 0 } \end{array}$ and $P ( x ) \equiv 0$ . This implies that $a _ { 0 } = a _ { 1 } = \cdot \cdot \cdot = a _ { n } = 0$ , so $\mathbf { a } = \mathbf { 0 }$ . Hence, the matrix $B$ is nonsingular, and the normal equations have a unique solution.

# Exercise Set 8.3, page 527

1. The interpolating polynomials of degree two are:

\*(a) $^ { D } _ { 2 } ( x ) = 2 . 3 7 7 4 4 3 + 1 . 5 9 0 5 3 4 ( x - 0 . 8 6 6 0 2 5 4 ) +$ $3 4 ( x - 0 . 8 6 6 0 2 5 4 ) + 0 . 5 3 2 0 4 1 8 ( x - 0 . 8 6 6 0 2 5 4 ) ;$ x (b) $P _ { 2 } ( x ) = 0 . 7 6 1 7 6 0 0 + 0 . 8 7 9 6 0 4 7 ( x - 0 . 8 6 6 0 2 5 4 )$ (c) $P _ { 2 } ( x ) = 1 . 0 5 2 9 2 6 + 0 . 4 1 5 4 3 7 0 ( x - 0 . 8 6 6 0 2 5 4 ) - 0 . 1 3 8 4 2 6 2 x ( x - 0 . 8 6 6 0 2 5 4 )$ (d) $P _ { 2 } ( x ) = 0 . 5 6 2 5 + 0 . 6 4 9 5 1 9 ( x - 0 . 8 6 6 0 2 5 4 ) + 0 . 7 5 x ( x - 0 . 8 6 6 0 2 5 4 )$

2. The interpolating polynomials of degree three are:

(a) $P _ { 3 } ( x ) = 2 . 5 1 9 0 4 4 + 1 . 9 4 5 3 7 7 ( x - 0 . 9 2 3 8 7 9 5 ) + 0 . 7 0 4 7 4 2 0 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 )$ $+ 0 . 1 7 5 1 7 5 7 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ( x + 0 . 3 8 2 6 8 3 4 )$

(b) $P _ { 3 } ( x ) = 0 . 7 9 7 9 4 5 9 + 0 . 7 8 4 4 3 8 0 ( x - 0 . 9 2 3 8 7 9 5 ) - 0 . 1 4 6 4 3 9 4 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 )$ $- 0 . 1 5 8 5 0 4 9 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ( x + 0 . 3 8 2 6 8 3 4 )$ (c) $P _ { 3 } ( x ) = 1 . 0 7 2 9 1 1 + 0 . 3 7 8 2 0 6 7 ( x - 0 . 9 2 3 8 7 9 5 ) - 0 . 0 9 7 9 9 2 1 3 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 )$ $+ 0 . 0 4 9 0 9 0 7 3 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ( x + 0 . 3 8 2 6 8 3 4 )$ (d) $P _ { 3 } ( x ) = 0 . 7 2 8 5 5 3 3 + 1 . 3 0 6 5 6 3 ( x - 0 . 9 2 3 8 7 9 5 ) + 0 . 9 9 9 9 9 9 9 ( x - 0 . 9 2 3 8 7 9 5 ) ( x - 0 . 3 8 2 6 8 3 4 ) ^ { 2 }$ )

3. Bounds for the maximum errors of polynomials in Exercise 1 are:

\*(a) 0.1132617 (b) 0.04166667 (c) 0.08333333 (d) 1.000000

4. Bounds for the maximum errors of polynomials in Exercise 3 are:

(a) 0.01415772 (b) 0.004382661 (c) 0.03125000 (d) 0.1250000

5. The zeros of $\ddot { T } _ { 3 }$ produce the following interpolating polynomials of degree two.

(a) $^ { D } _ { 2 } ( x ) = 0 . 3 4 8 9 1 5 3 - 0 . 1 7 4 4 5 7 6 ( x - 2 . 8 6 6 0 2 5 ) -$ $\cdot - 2 . 8 6 6 0 2 5 ) + 0 . 1 5 3 8 4 6 2 ( x - 2 . 8 6 6 0 2 5 ) ( x - 2 )$ (b) $P _ { 2 } ( x ) = 0 . 1 5 4 7 3 7 5 - 0 . 2 4 6 1 1 5 2 ( x - 1 . 8 6 6 0 2 5 ) + 0 . 1 9 5 7 2 7 3 ( x - 1 . 8 6 6 0 2 5 ) ( x - 1 )$ (c) $P _ { 2 } ( x ) = 0 . 6 1 6 6 2 0 0 - 0 . 2 3 7 0 8 6 9 ( x - 0 . 9 3 3 0 1 2 7 ) - 0 . 7 4 2 7 7 3 2 ( x - 0 . 9 3 3 0 1 2 7 ) ( x - 0 . 9 3 3 0 1 2 7 ) .$ 0.5) (d) $P _ { 2 } ( x ) = 3 . 0 1 7 7 1 2 5 + 1 . 8 8 3 8 0 0 ( x - 2 . 8 6 6 0 2 5 ) + 0 . 2 5 8 4 6 2 5 ( x - 2 . 8 6 6 0 2 5 ) ( x - 2 )$

6. The polynomial

$$
P ( x ) = { \frac { 1 } { 3 8 4 0 } } + { \frac { 3 7 9 } { 3 8 4 } } x + { \frac { 6 3 7 } { 6 4 0 } } x ^ { 2 } + { \frac { 5 3 } { 9 6 } } x ^ { 3 } + { \frac { 4 3 } { 2 4 0 } } x ^ { 4 }
$$

approximates $x e ^ { x }$ , with error at most 0.00718.

7. The cubic polynomial ${ \frac { 3 8 3 } { 3 8 4 } } x - { \frac { 5 } { 3 2 } } x ^ { 3 }$ approximates $\sin x$ with error at most $7 . 1 9 \times 1 0 ^ { - 4 }$ .

$^ { * } 8$ . If $i > j$ , then

$$
{ \frac { 1 } { 2 } } ( T _ { i + j } ( x ) + T _ { i - j } ( x ) ) = { \frac { 1 } { 2 } } \left( \cos ( i + j ) \theta + \cos ( i - j ) \theta \right) = \cos i \theta \cos j \theta = T _ { i } ( x ) T _ { j } ( x ) .
$$

$^ { * } 9$ . The change of variable $x = \cos \theta$ produces

$$
\int _ { - 1 } ^ { 1 } { \frac { T _ { n } ^ { 2 } ( x ) } { \sqrt { 1 - x ^ { 2 } } } } \ d x = \int _ { - 1 } ^ { 1 } { \frac { [ \cos ( n \operatorname { a r c c o s } x ) ] ^ { 2 } } { \sqrt { 1 - x ^ { 2 } } } } \ d x = \int _ { 0 } ^ { \pi } ( \cos ( n \theta ) ) ^ { 2 } \ d x = { \frac { \pi } { 2 } } .
$$

10. The zeros of $T _ { n } ( x )$ are ${ \overline { { x } } } _ { n } = \cos \left( { \frac { 2 k - 1 } { 2 n } } \pi \right)$ for $k = 1 , 2 , \ldots , n$

The cosine function is strictly decreasing from $0$ to $\pi$ , with values decreasing from $\cos 0 = 1$ to $\cos \pi = - 1$ . So

$$
- 1 = \cos ( \pi ) < \cos \left( { \frac { 2 n - 1 } { 2 n } } \pi \right) = { \overline { { x } } } _ { n } < { \overline { { x } } } _ { n - 1 } < \cdot \cdot \cdot < { \overline { { x } } } _ { 1 } = \cos \left( { \frac { \pi } { 2 n } } \right) < \cos ( 1 ) = 1
$$

Hence the zeros are distinct and lie in $( - 1 , 1 )$

11. The zeros of $T _ { n } ^ { \prime } ( x )$ are ${ \overline { { x ^ { \prime } } } } _ { n } = \cos \left( { \frac { k \pi } { n } } \right)$ for $k = 1 , 2 , \ldots , n - 1$

The cosine function is strictly decreasing from $0$ to $\pi$ , with values decreasing from $\cos 0 = 1$ to $\cos \pi = - 1$ . So

$$
- 1 = \cos ( \pi ) < \cos \left( { \frac { ( n - 1 ) \pi } { n } } \right) = { \overline { { x ^ { \prime } } } } _ { n - 1 } < { \overline { { x ^ { \prime } } } } _ { n - 2 } < \cdot \cdot \cdot < { \overline { { x ^ { \prime } } } } _ { 1 } = \cos \left( { \frac { \pi } { n } } \right) < \cos ( 1 ) = 1
$$

Hence the zeros are distinct and lie in $( - 1 , 1 )$

# Exercise Set 8.4, page 537

$^ { * } 1$ . The Pad´e approximations of degree two for $f ( x ) = e ^ { 2 x }$ are:

$$
\begin{array} { l l l } { n } & { = } & { 2 , m = 0 : r _ { 2 , 0 } ( x ) = 1 + 2 x + 2 x ^ { 2 } } \\ { n } & { = } & { 1 , m = 1 : r _ { 1 , 1 } ( x ) = ( 1 + x ) / ( 1 - x ) } \\ { n } & { = } & { 0 , m = 2 : r _ { 0 , 2 } ( x ) = ( 1 - 2 x + 2 x ^ { 2 } ) ^ { - 1 } } \end{array}
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r2,0(xi)</td><td>r1,1(xi)</td><td>r0,2(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.4918</td><td>1.4800</td><td>1.5000</td><td>1.4706</td></tr><tr><td>2</td><td>0.4</td><td>2.2255</td><td>2.1200</td><td>2.3333</td><td>1.9231</td></tr><tr><td>3</td><td>0.6</td><td>3.3201</td><td>2.9200</td><td>4.0000</td><td>1.9231</td></tr><tr><td>4</td><td>0.8</td><td>4.9530</td><td>3.8800</td><td>9.0000</td><td>1.4706</td></tr><tr><td>5</td><td>1.0</td><td>7.3891</td><td>5.0000</td><td>undefined</td><td>1.0000</td></tr></table>

2. The Pad´e approximations of degree three for $f ( x ) = x \ln ( x + 1 )$ are:

$$
\begin{array} { l } { m = 0 , n = 3 ; ~ x ^ { 2 } - \displaystyle \frac { 1 } { 2 } x ^ { 3 } } \\ { m = 1 , n = 2 ; ~ \displaystyle \frac { x ^ { 2 } } { 1 + \frac { 1 } { 2 } x } } \end{array}
$$

$m = 1$ , $n = 2$ ; $m = 2$ , $n = 1$ ; and $m = 3$ , $n = 0$ : $\frac { x ^ { 2 } } { 1 + { \frac { 1 } { 2 } } x }$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r3.0(xi)</td><td>r2,1(xi)</td></tr><tr><td>1</td><td>0.2</td><td>0.03646431</td><td>0.03600000</td><td>0.03636364</td></tr><tr><td>2</td><td>0.4</td><td>0.13458889</td><td>0.12800000</td><td>0.13333333</td></tr><tr><td>3</td><td>0.6</td><td>0.28200218</td><td>0.25200000</td><td>0.27692308</td></tr><tr><td>4</td><td>0.8</td><td>0.47022933</td><td>0.38400000</td><td>0.45714286</td></tr><tr><td>5</td><td>1.0</td><td>0.69314718</td><td>0.50000000</td><td>0.66666666</td></tr></table>

3. The Pad´e approximation of degree five for $f ( x ) = e ^ { x }$ with $n = 2$ and $m = 3$ is:

$$
r _ { 2 , 3 } ( x ) = ( 1 + \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } ) / ( 1 - \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } - \frac { 1 } { 6 0 } x ^ { 3 } )
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r2.3(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.22140276</td><td>1.22140277</td></tr><tr><td>2</td><td>0.4</td><td>1.49182470</td><td>1.49182561</td></tr><tr><td>3</td><td>0.6</td><td>1.82211880</td><td>1.82213210</td></tr><tr><td>4</td><td>0.8</td><td>2.22554093</td><td>2.22563652</td></tr><tr><td>5</td><td>1.0</td><td>2.71828183</td><td>2.71875000</td></tr></table>

4. The Pad´e approximations of degree five for $f ( x ) = e ^ { x }$ with $n = 3$ and $m = 2$ is:

$$
r _ { 3 , 2 } ( x ) = \left( 1 + \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } + \frac { 1 } { 6 0 } x ^ { 3 } \right) / \left( 1 - \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } \right)
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r3.2(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.22140276</td><td>1.22140275</td></tr><tr><td>2</td><td>0.4</td><td>1.49182470</td><td>1.49182390</td></tr><tr><td>3</td><td>0.6</td><td>1.82211880</td><td>1.82210797</td></tr><tr><td>4</td><td>0.8</td><td>2.22554093</td><td>2.22546816</td></tr><tr><td>5</td><td>1.0</td><td>2.71828183</td><td>2.71794872</td></tr></table>

5. The Pad´e approximations of degree six for $f ( x ) = \sin { x }$ with $m = n = 3$ is:

$$
r _ { 3 , 3 } ( x ) = ( x - \frac { 7 } { 6 0 } x ^ { 3 } ) / ( 1 + \frac { 1 } { 2 0 } x ^ { 2 } )
$$

<table><tr><td>i</td><td>xi</td><td>f(xi)</td><td>Maclaurin polynomial of degree 6</td><td>r3,3(xi)</td></tr><tr><td>0</td><td>0.0</td><td>0.00000000</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.1</td><td>0.09983342</td><td>0.09966675</td><td>0.09938640</td></tr><tr><td>2</td><td>0.2</td><td>0.19866933</td><td>0.19733600</td><td>0.19709571</td></tr><tr><td>3</td><td>0.3</td><td>0.29552021</td><td>0.29102025</td><td>0.29246305</td></tr><tr><td>4</td><td>0.4</td><td>0.38941834</td><td>0.37875200</td><td>0.38483660</td></tr><tr><td>5</td><td>0.5</td><td>0.47942554</td><td>0.45859375</td><td>0.47357724</td></tr></table>

6. The Pad´e approximations of degree six for $f ( x ) = \sin { x }$ are as follows.

(a) Wit $\mathrm { ~ h ~ } n = 2 \mathrm { ~ a n d ~ } m = 4 : \mathrm { ~ } r _ { 2 , 4 } ( x ) = x / \left( 1 + \frac { 1 } { 6 } x ^ { 2 } + \frac { 7 } { 3 6 0 } x ^ { 4 } \right)$ (b) With $n = 4$ $4 { \mathrm { ~ a n d ~ } } m = 2 ! \ r _ { 4 , 2 } ( x ) = \left( x - { \frac { 7 } { 6 0 } } x ^ { 3 } \right) / \left( 1 + { \frac { 1 } { 2 0 } } x ^ { 2 } \right)$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>r2.4（xi)</td><td>T4,2(xi)</td></tr><tr><td>0</td><td>0.0</td><td>0.00000000</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.1</td><td>0.09983342</td><td>0.09983342</td><td>0.09938640</td></tr><tr><td>2</td><td>0.2</td><td>0.19866933</td><td>0.19866936</td><td>0.19709571</td></tr><tr><td>3</td><td>0.3</td><td>0.29552021</td><td>0.29552065</td><td>0.29246305</td></tr><tr><td>4</td><td>0.4</td><td>0.38941834</td><td>0.38942158</td><td>0.38483660</td></tr><tr><td>5</td><td>0.5</td><td>0.47942554</td><td>0.47944065</td><td>0.47357724</td></tr></table>

7. The Pad´e approximations of degree five are:

(a) $r _ { 0 , 5 } ( x ) = ( 1 + x + \frac { 1 } { 2 } x ^ { 2 } + \frac { 1 } { 6 } x ^ { 3 } + \frac { 1 } { 2 4 } x ^ { 4 } + \frac { 1 } { 1 2 0 } x ^ { 5 } ) ^ { - 1 }$ (b) $r _ { 1 , 4 } ( x ) = ( 1 - \frac { 1 } { 5 } x ) / ( 1 + \frac { 4 } { 5 } x + \frac { 3 } { 1 0 } x ^ { 2 } + \frac { 1 } { 1 5 } x ^ { 3 } + \frac { 1 } { 1 2 0 } x ^ { 4 } )$ (c) $r _ { 3 , 2 } ( x ) = ( 1 - \frac { 3 } { 5 } x + \frac { 3 } { 2 0 } x ^ { 2 } - \frac { 1 } { 6 0 } x ^ { 3 } ) / ( 1 + \frac { 2 } { 5 } x + \frac { 1 } { 2 0 } x ^ { 2 } )$ (d) $r _ { 4 , 1 } ( x ) = ( 1 - \frac { 4 } { 5 } x + \frac { 3 } { 1 0 } x ^ { 2 } - \frac { 1 } { 1 5 } x ^ { 3 } + \frac { 1 } { 1 2 0 } x ^ { 4 } ) / ( 1 + \frac { 1 } { 5 } x )$

<table><tr><td>i</td><td>xi</td><td>f(xi)</td><td>r0.5(xi)</td><td>r1,4(xi)</td><td>r2,3(xi)</td><td>T4,1(xi)</td></tr><tr><td>1</td><td>0.2</td><td>0.81873075</td><td>0.81873081</td><td>0.81873074</td><td>0.81873075</td><td>0.81873077</td></tr><tr><td>2</td><td>0.4</td><td>0.67032005</td><td>0.67032276</td><td>0.67031942</td><td>0.67031963</td><td>0.67032099</td></tr><tr><td>3</td><td>0.6</td><td>0.54881164</td><td>0.54883296</td><td>0.54880635</td><td>0.54880763</td><td>0.54882143</td></tr><tr><td>4</td><td>0.8</td><td>0.44932896</td><td>0.44941181</td><td>0.44930678</td><td>0.44930966</td><td>0.44937931</td></tr><tr><td>5</td><td>1.0</td><td>0.36787944</td><td>0.36809816</td><td>0.36781609</td><td>0.36781609</td><td>0.36805556</td></tr></table>

8. The continued fraction forms of the rational functions are shown.

$$
\begin{array} { c } { { * ( \mathrm { a } ) ~ 1 + \frac { 4 } { x - \frac { 5 } { 4 } + \frac { 2 1 } { x + \frac { 1 } { 4 } } } } } \\ { { ( \mathrm { b } ) ~ \frac { 2 } { x - \frac { 1 } { 4 } + \displaystyle \frac { \frac { 2 3 } { 8 } } { x - \frac { 6 3 } { 9 2 } - \frac { \frac { 4 0 6 } { 5 2 9 } } { x + \frac { 3 3 } { 2 3 } } } } } } \end{array}
$$

9. For $f ( x ) = e ^ { x }$ we have the following approximations.

$r _ { T _ { 2 , 0 } } ( x ) = ( 1 . 2 6 6 0 6 6 T _ { 0 } ( x ) - 1 . 1 3 0 3 1 8 T _ { 1 } ( x ) + 0 . 2 7 1 4 9 5 3 T _ { 2 } ( x ) ) / T _ { 0 } ( x )$ $r _ { T _ { 1 , 1 } } ( x ) = ( 0 . 9 9 4 5 7 0 5 T _ { 0 } ( x ) - 0 . 4 5 6 9 0 4 6 T _ { 1 } ( x ) ) / ( T _ { 0 } ( x ) + 0 . 4 8 0 3 8 7 4 5 T _ { 1 } ( x )$ x)) $r _ { T _ { 0 , 2 } } ( x ) = 0 . 7 9 4 0 2 2 0 T _ { 0 } ( x ) / ( T _ { 0 } ( x ) + 0 . 8 7 7 8 5 7 5 T _ { 1 } ( x ) + 0 . 1 7 7 4 2 6 6 T _ { 2 } ( x ) )$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>TT2.0(xi)</td><td>rT1,1(xi)</td><td>TT0，2(xi)</td></tr><tr><td>1</td><td>0.25</td><td>0.77880078</td><td>0.74592811</td><td>0.78595377</td><td>0.74610974</td></tr><tr><td>2</td><td>0.50</td><td>0.60653066</td><td>0.56515935</td><td>0.61774075</td><td>0.58807059</td></tr><tr><td>3</td><td>1.00</td><td>0.36787944</td><td>0.40724330</td><td>0.36319269</td><td>0.38633199</td></tr></table>

10. For $f ( x ) = \cos x$ we have the following approximations.

$m = 3$ , $n = 0$ and $m = 2 , n = 1$ :

$$
\frac { \cup . \ i \cup \cup \cup \bigcirc \cup . 0 1 0 ( . 4 ) } { T _ { 0 } ( x ) + 0 . 3 0 0 3 2 3 8 T _ { 2 } ( x ) }
$$

$m = 1$ , $n = 2$ and $m = 0 , n = 3$ :

$$
\frac { 0 . 7 6 5 1 9 7 5 T _ { 0 } ( x ) - 0 . 2 2 9 8 0 7 0 T _ { 2 } ( x ) } { T _ { 0 } ( x ) }
$$

This gives

<table><tr><td>C</td><td>f(x)</td><td>rT0,3(x） and rT1,2(x)</td><td>TT2,1（x） and rT3,0(x)</td></tr><tr><td>0.78539816</td><td>0.70710678</td><td>0.68276861</td><td>0.71149148</td></tr><tr><td>1.04719755</td><td>0.50000000</td><td>0.53792021</td><td>0.49098135</td></tr></table>

11. For $f ( x ) = \sin { x }$ we have the following approximations.

$$
r _ { T _ { 2 , 2 } } ( x ) = \frac { 0 . 9 1 7 4 7 T _ { 1 } ( x ) } { T _ { 0 } ( x ) + 0 . 0 8 8 9 1 4 T _ { 2 } ( x ) }
$$

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>TT2,2(xi)</td></tr><tr><td>0</td><td>0.00</td><td>0.00000000</td><td>0.00000000</td></tr><tr><td>1</td><td>0.10</td><td>0.09983342</td><td>0.09093843</td></tr><tr><td>2</td><td>0.20</td><td>0.19866933</td><td>0.18028797</td></tr><tr><td>3</td><td>0.30</td><td>0.29552021</td><td>0.26808992</td></tr><tr><td>4</td><td>0.40</td><td>0.38941834</td><td>0.35438412</td></tr></table>

12. For $f ( x ) = e ^ { x }$ we have the following degree five approximations. When $m = 5 , n = 0$ :

When $m = 4 , n = 1$ :

When $m = 3 , n = 2$ :

When $m = 2 , n = 3$ :

When $m = 1 , n = 4$ :

$m = 0 , n = 5$ :

<table><tr><td>i</td><td>Xi</td><td>f(xi)</td><td>TTo,5(xi)</td><td>rT1,4(xi)</td><td>TT2,3(xi)</td><td>TT3,2(xi)</td><td>TT4,1(xi)</td><td>TT5,0(xi)</td></tr><tr><td>1</td><td>0.2</td><td>1.22140276</td><td>1.22137251</td><td>1.22142042</td><td>1.22140929</td><td>1.22141264</td><td>1.29573091</td><td>1.22142198</td></tr><tr><td>2</td><td>0.4</td><td>1.49182470</td><td>1.49190745</td><td>1.49184755</td><td>1.49184841</td><td>1.49183231</td><td>1.54914242</td><td>1.49179061</td></tr><tr><td>3</td><td>0.6</td><td>1.82211880</td><td>1.82224269</td><td>1.82211712</td><td>1.82213166</td><td>1.82211572</td><td>1.84678705</td><td>1.82208177</td></tr><tr><td>4</td><td>0.8</td><td>2.22554093</td><td>2.22539680</td><td>2.22551178</td><td>2.22550877</td><td>2.22553290</td><td>2.19970546</td><td>2.22557527</td></tr><tr><td>5</td><td>1.0</td><td>2.71828183</td><td>2.71856417</td><td>2.71831087</td><td>2.71832589</td><td>2.71828966</td><td>2.62151591</td><td>2.71823332</td></tr></table>

13. (a) $e ^ { x } = e ^ { M \ln \sqrt { 1 0 } + s } = e ^ { M \ln \sqrt { 1 0 } } e ^ { s } = e ^ { \ln 1 0 \frac { M } { 2 } } e ^ { s } = 1 0 ^ { \frac { M } { 2 } } e ^ { s }$ (b) $e ^ { s } \approx \left( 1 + { \frac { 1 } { 2 } } s + { \frac { 1 } { 1 0 } } s ^ { 2 } + { \frac { 1 } { 1 2 0 } } s ^ { 3 } \right) / \left( 1 - { \frac { 1 } { 2 } } s + { \frac { 1 } { 1 0 } } s ^ { 2 } - { \frac { 1 } { 1 2 0 } } s ^ { 3 } \right)$ , with $| \mathrm { e r r o r } | \le 3 . 7 5 \times 1 0 ^ { - 7 }$ . (c) S $\mathrm { * } ~ M = \mathrm { r o u n d } ( 0 . 8 6 8 5 8 8 9 6 3 8 x ) , ~ s = x - M / ( 0 . 8 6 8 5 8 8 9 6 3 8 )$ , and $\hat { f } = \left( 1 + \frac { 1 } { 2 } s + \frac { 1 } { 1 0 } s ^ { 2 } + \frac { 1 } { 1 2 0 } s ^ { 3 } \right) / \left( 1 - \frac { 1 } { 2 } s + \frac { 1 } { 1 0 } s ^ { 2 } - \frac { 1 } { 1 2 0 } s ^ { 3 } \right) .$ Then $f = ( 3 . 1 6 2 2 7 7 6 6 ) ^ { M } \hat { f }$ .

$^ { * } 1 4$ . (a) Since

$$
\sin | x | = \sin ( M \pi + s ) = \sin M \pi \cos s + \cos M \pi \sin s = ( - 1 ) ^ { M } \sin s ,
$$

we have

$$
\sin x = { \mathrm { ~ s i g n ~ } } x \sin | x | = \operatorname { s i g n } { \big ( } x { \big ) } ( - 1 ) ^ { M } \sin s .
$$

(b) We have

$$
\sin x \approx \left( s - { \frac { 3 1 } { 2 9 4 } } s ^ { 3 } \right) \left/ \left( 1 + { \frac { 3 } { 4 9 } } s ^ { 2 } + { \frac { 1 1 } { 5 8 8 0 } } s ^ { 3 } \right) , \right.
$$

with $| \mathrm { e r r o r } | \le 2 . 8 4 \times 1 0 ^ { - 4 }$ .

(c) Set $M = \operatorname { R o u n d } ( | x | / \pi )$ , $s = | x | - M \pi$ , and $f _ { 1 } = \left( s - \frac { 3 1 } { 2 9 4 } s ^ { 3 } \right) \bigg / \left( 1 + \frac { 3 } { 4 9 } s ^ { 2 } + \frac { 1 1 } { 5 8 8 0 } s ^ { 4 } \right) .$ Then $f = ( - 1 ) ^ { M } f _ { 1 } \cdot x / | x |$ is the approximation.

(d) Set $y = x + { \frac { \pi } { 2 } }$ , and repeat part (c) with $y$ in place of $x$

# Exercise Set 8.5, page 546

$$
S _ { 2 } ( x ) = \frac { \pi ^ { 2 } } { 3 } - 4 \cos x + \cos 2 x
$$

2. $S _ { 3 } ( x ) = 2 \sin x - \sin 2 x$

3. $\begin{array} { r l r } { S _ { 3 } ( x ) } & { = } & { 3 . 6 7 6 0 7 8 - 3 . 6 7 6 0 7 8 \cos x + 1 . 4 7 0 4 3 1 \cos 2 x - 0 . 7 3 5 2 1 5 6 \cos 3 x + 3 . 6 7 6 0 7 8 \sin 3 x } \end{array}$ x − $2 . 9 4 0 8 6 2 \sin { 2 x }$

4. The general trigonometric least-squares polynomial is

$$
\begin{array} { l } { { \displaystyle S _ { n } ( x ) = \frac { e ^ { \pi } - e ^ { - \pi } } { 2 \pi } + \frac { ( - 1 ) ^ { n } e ^ { \pi } + ( - 1 ) ^ { n + 1 } e ^ { - \pi } } { \pi ( n ^ { 2 } + 1 ) } \cos n x } } \\ { { \displaystyle \qquad + \frac { 1 } { \pi } \sum _ { k = 1 } ^ { n - 1 } \left[ \frac { ( - 1 ) ^ { k } e ^ { \pi } + ( - 1 ) ^ { k + 1 } e ^ { - \pi } } { k ^ { 2 } + 1 } \right] ( \cos k x - k \sin k x ) . } } \end{array}
$$

$$
S _ { n } ( x ) = { \frac { 1 } { 2 } } + { \frac { 1 } { \pi } } \sum _ { k = 1 } ^ { n - 1 } { \frac { 1 - ( - 1 ) ^ { k } } { k } } \sin k x 
$$

6. The general trigonometric least-squares polynomial is

$$
S _ { n } ( x ) = \sum _ { k = 1 } ^ { n - 1 } { \frac { 2 } { k \pi } } \left( 1 - ( - 1 ) ^ { k } \right) \sin k x .
$$

7. The trigonometric least-squares polynomials are:

\*(a) $S _ { 2 } ( x ) = \cos { 2 x }$   
(b) $S _ { 2 } ( x ) = 0$   
(c) $S _ { 3 } ( x ) = 1 . 5 6 6 4 5 3 + 0 . 5 8 8 6 8 1 5 \cos x - 0 . 2 7 0 0 6 4 2 \cos 2 x + 0 . 2 1 7 5 6 7 9 \cos 3 x + 0 . 8 3 4 1 6 4 0 \sin x - 0 . 0 0 0 0 0 1 1 \sin 2 x \cos 3 x$ $0 . 3 0 9 7 8 6 6 \sin { 2 x }$   
(d) $S _ { 3 } ( x ) = - 2 . 0 4 6 3 2 6 + 3 . 8 8 3 8 7 2 \cos x - 2 . 3 2 0 4 8 2 \cos 2 x + 0 . 7 3 1 0 8 1 8 \cos 3 x$

8. \*(a) $E ( S _ { 2 } ) = 0$ (b) $E ( S _ { 2 } ) = 4$ (c) $E ( S _ { 3 } ) = 0 . 8 2 5 9 8 1 4$ (d) $E ( S _ { 3 } ) = 1 . 9 3 6 6 6 8$

9. The trigonometric least-squares polynomial is

$S _ { 3 } ( x ) = - 0 . 4 9 6 8 9 2 9 + 0 . 2 3 9 1 9 6 5 \cos x + 1 . 5 1 5 3 9 3 \cos 2 x + 0 . 2 3 9 1 9 6 5 \cos 3 x - 1 . 1 5 0 6 4 9 \sin x ,$

with error $E ( S _ { 3 } ) = 7 . 2 7 1 1 9 7$ .

\*10. The trigonometric least-squares polynomial is

with error 107.913.

The approximation in Exercise 10 is better because, in this case,

$$
\sum _ { j = 0 } ^ { 1 0 } \left( f ( \xi _ { j } ) - S _ { 3 } ( \xi _ { j } ) \right) ^ { 2 } = 3 9 7 . 3 6 7 8 ,
$$

whereas the approximation in Exercise 9 has

$$
\sum _ { j = 0 } ^ { 1 0 } ( f ( \xi _ { j } ) - S _ { 3 } ( \xi _ { j } ) ) ^ { 2 } = 5 6 9 . 3 5 8 9 .
$$

11. The trigonometric least-squares polynomials and their errors are

(a)

with $E ( S _ { 3 } ) = 2 1 0 . 9 0 4 5 3$ .

(b)

with $E ( S _ { 4 } ) = 1 6 9 . 4 9 4 3$ .

12. (a) The trigonometric least-squares polynomial is

(b) $\int _ { 0 } ^ { 1 } S _ { 4 } ( x ) d x = 0 . 2 7 7 2 1 4 8 6$ (c) $\int _ { 0 } ^ { 1 } x ^ { 2 } \sin x d x = 0 . 2 2 3 2 4 4 3$

13. Let $f ( - x ) = - f ( x )$ . The integral $\textstyle \int _ { - a } ^ { 0 } f ( x ) d x$ under the change of variable $t = - x$ transforms to

$$
- \int _ { a } ^ { 0 } f ( - t ) \ d t = \int _ { 0 } ^ { a } f ( - t ) \ d t = - \int _ { 0 } ^ { a } f ( t ) \ d t = - \int _ { 0 } ^ { a } f ( x ) \ d x .
$$

Thus,

$$
\int _ { - a } ^ { a } f ( x ) \ d x = \int _ { - a } ^ { 0 } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = - \int _ { 0 } ^ { a } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = 0 .
$$

14. Let $f ( - x ) = f ( x )$ . The integral $\textstyle \int _ { - a } ^ { 0 } f ( x ) d x$ under the change of variable $t = - x$ transforms to

$$
- \int _ { a } ^ { 0 } f ( - t ) \ d t = \int _ { 0 } ^ { a } f ( - t ) \ d t = \int _ { 0 } ^ { a } f ( t ) \ d t = \int _ { 0 } ^ { a } f ( x ) \ d x .
$$

Thus

$$
\int _ { - a } ^ { a } f ( x ) \ d x = \int _ { - a } ^ { 0 } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = \int _ { 0 } ^ { a } f ( x ) \ d x + \int _ { 0 } ^ { a } f ( x ) \ d x = 2 \int _ { 0 } ^ { a } f ( x ) \ d x .
$$

$^ \mathrm { * _ { 1 5 } }$ . The following integrations establish the orthogonality.

$$
\begin{array} { r l } & { \displaystyle \int _ { - \infty } ^ { \infty } \{ \theta _ { 0 } ( x ) ^ { 2 } \log ( x ) \} ^ { 2 } d x = \frac { 1 } { 2 } \int _ { - \infty } ^ { \infty } d x = \pi , } \\ & { \displaystyle \int _ { - \infty } ^ { \infty } ( \psi _ { 0 } ( x ) ^ { 2 } ) d x = \int _ { - \infty } ^ { \infty } ( \cos k x ) ^ { 2 } d x = \int _ { - \infty } ^ { x } [ \frac { 1 } { 2 } + \frac { 1 } { 2 } \cos 2 k x ] d x = x + [ \frac { 1 } { 4 k } \sin 2 k x ] _ { - \infty } ^ { \infty } = x , } \\ & { \displaystyle \int _ { - \infty } ^ { x } [ \theta _ { 0 } ( x ) ( x ) ^ { 2 } + d x = \int _ { - \infty } ^ { x } ( \sin k x ) ^ { 2 } d x = \int _ { - \infty } ^ { x } [ \frac { 1 } { 2 } - \frac { 1 } { 2 } \cos 2 k x ] d x = \pi - [ \frac { 1 } { 4 k } \sin ^ { 2 } 2 k x ] _ { - \infty } ^ { \infty } = x ^ { \infty } } \\ & { \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \frac { 1 } { 2 } \int _ { - \infty } ^ { x } \cos k x \mathrm { d } x = [ \frac { 1 } { 2 k } \sin k x ] _ { - \infty } ^ { \infty } = 0 , } \\ & { \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \frac { 1 } { 2 } \int _ { - \infty } ^ { x } \sin k x \mathrm { d } x = [ \frac { - 1 } { 2 k } \cos k x ] _ { - \infty } ^ { \infty } = - \frac { 1 } { 2 k } \frac { 1 } { \cos k x } \cos ( - k x ) \mathrm { d } - 0 , } \\ & { \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \int _ { - \infty } ^ { x } \cos k x \cos j x d x = \int _ { - \infty } ^ { x } [ \cos k x ] _ { - \infty } ^ { \infty } = x - j k x \mathrm { d } j x = 0 , } \\ &  \displaystyle \int _ { - \infty } ^ { x } \psi _ { 0 } ( x ) \partial _ { 0 } ( x ) d x = \int _ { - \infty } ^ { x } \cos k x \cos j x \end{array}
$$

and

$$
\int _ { - \pi } ^ { \pi } \phi _ { k } ( x ) \phi _ { n + j } ( x ) d x = \int _ { - \pi } ^ { \pi } \cos k x \sin j x d x = { \frac { 1 } { 2 } } \int _ { - \pi } ^ { \pi } [ \sin ( k + j ) x - \sin ( k - j ) x ] d x = 0 .
$$

16. The Fourier Series for $f ( x ) = \left| x \right|$ is

$$
S ( x ) = { \frac { \pi } { 2 } } + { \frac { 2 } { \pi } } \sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } } \cos k x .
$$

Assuming $f ( 0 ) = S ( 0 )$ gives

$$
0 = S ( 0 ) = \frac { \pi } { 2 } + \frac { 2 } { \pi } \sum _ { k = 1 } ^ { \infty } \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } ,
$$

but

$$
\sum _ { k = 1 } ^ { \infty } { \frac { ( - 1 ) ^ { k } - 1 } { k ^ { 2 } } } = - { \frac { 2 } { 1 ^ { 2 } } } + { \frac { 0 } { 2 ^ { 2 } } } - { \frac { 2 } { 3 ^ { 2 } } } + { \frac { 0 } { 4 ^ { 2 } } } + \cdots = - \sum _ { k = 0 } ^ { \infty } { \frac { 2 } { ( 2 k + 1 ) ^ { 2 } } } .
$$

Thus

$$
0 = \frac { \pi } { 2 } - \frac { 2 } { \pi } \sum _ { k = 0 } ^ { \infty } \frac { 2 } { ( 2 k + 1 ) ^ { 2 } } ,
$$

from which

$$
\sum _ { k = 0 } ^ { \infty } { \frac { 1 } { ( 2 k + 1 ) ^ { 2 } } } = { \frac { \pi ^ { 2 } } { 8 } }
$$

follows.

17. The steps are nearly identical to those for determining the constants $b _ { k }$ except for the additional constant term $a _ { 0 }$ in the cosine series. In this case

$$
\frac { \partial E } { \partial a _ { 0 } } = 2 \sum _ { j = 0 } ^ { 2 m - 1 } [ y _ { j } - S _ { n } ( x _ { j } ) ] ( - 1 / 2 ) = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } - \sum _ { j = 0 } ^ { 2 m - 1 } \left( \frac { a _ { 0 } } { 2 } + a _ { n } \cos n x _ { j } + \sum _ { k = 1 } ^ { n - 1 } ( a _ { k } \cos k x _ { j } + b _ { k } \sin k x _ { k } ) \right) ,
$$

The orthogonality implies that only the constant term remains in the second sum. So

$$
0 = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } - { \frac { a _ { 0 } } { 2 } } ( 2 m ) \quad { \mathrm { w h i c h ~ i m p l i e s ~ t h a t } } \quad a _ { 0 } = { \frac { 1 } { m } } \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } .
$$

# Exercise Set 8.6, page 557

1. The trigonometric interpolating polynomials are:

\*(a) $S _ { 2 } ( x ) = - 1 2 . 3 3 7 0 1 + 4 . 9 3 4 8 0 2 \cos x - 2 . 4 6 7 4 0 1 \cos 2 x + 4 . 9 3 4 8 0 2 \sin x$ (b) $S _ { 2 } ( x ) = - 6 . 1 6 8 5 0 3 + 9 . 8 6 9 6 0 4 \cos x - 3 . 7 0 1 1 0 2 \cos 2 x + 4 . 9 3 4 8 0 2 \sin x$ (c) $S _ { 2 } ( x ) = 1 . 5 7 0 7 9 6 - 1 . 5 7 0 7 9 6 \cos x$   
(d) $S _ { 2 } ( x ) = - 0 . 5 - 0 . 5 \cos 2 x + \sin x$

2. Parts (a) and (b) give the same answer: The trigonometric interpolating polynomial is

$\mathfrak { I } _ { 4 } ( x ) = \mathrm { ~ - ~ } 4 . 6 2 6 3 7 7 + 6 . 6 7 9 5 1 8 \cos x - 3 . 7 0 1 1 0$ $. 6 7 9 5 1 8 \cos x - 3 . 7 0 1 1 0 2 \cos 2 x + 3 . 1 9 0 0 8 6 \cos ^ { \circ } { \cos ^ { \circ } }$ $0 1 1 0 2 \cos 2 x + 3 . 1 9 0 0 8 6 \cos 3 x - 1 . 5 4 2 1 2 6 \cos 4 ;$ x + 5. $9 5 6 6 8 3 3 \sin x - 2 . 4 6 7 4 0 1 \sin 2 x + 1 . 0 2 2 0 3 1 \sin 3 x$ .

3. The Fast Fourier Transform Algorithm gives the following trigonometric interpolating polynomials.

(a) $S _ { 4 } ( x ) = - 1 1 . 1 0 3 3 1 + 2 . 4 6 7 4 0 1 \cos x - 2 . 4 6 7 4 0 1 \cos 2 x + 2 . 4 6 7 4 0 1 \cos 3 x - 1 . 2 3 3 7 0 1 \cos 4 x + 2 . 1 4 6 7 2 \cos 3 x$ 5.9568 $\mathtt { 3 \sin { x } - 2 . 4 6 7 4 0 1 \sin { 2 x } + 1 . 0 2 2 0 3 0 \sin { 3 x } }$

(b) $S _ { 4 } ( x ) = 1 . 5 7 0 7 9 6 - 1 . 3 4 0 7 5 9 \cos x - 0 . 2 3 0 0 3 7 8 \cos 3 x$ (c) $S _ { 4 } ( x ) = - 0 . 1 2 6 4 2 6 4 + 0 . 2 6 0 2 7 2 4 \cos x - 0 . 3 0 1 1 1 4 0 \cos 2 x + 1 . 1 2 1 3 7 2 \cos 3 x + 0 . 0 4 5 8 9 6 4 8 \cos 2 x$ 4x− 0.1022190 $\sin x + 0 . 2 7 5 4 0 6 2 \sin 2 x - 2 . 0 5 2 9 5 5 \sin 3 x$

(d) $S _ { 4 } ( x ) = - 0 . 1 5 2 6 8 1 9 + 0 . 0 4 7 5 4 2 7 8 \cos x + 0 . 6 8 6 2 1 1 4 \cos 2 x - 1 . 2 1 6 9 1 3 \cos 3 x + 1 . 1 7 6 1 4 3 \cos 4 x - 0 . 0 0 0 0 1 1 1 \sin 6 x$ 0.817938 $\sin x + 0 . 1 8 0 2 4 5 0 \sin 2 x + 0 . 2 7 5 3 4 0 2 \sin 3 x$

$^ { * } 4$ . (a) The trigonometric interpolating polynomial is

$S _ { 4 } ( x ) = 0 . 1 7 3 5 5 0 0 - 0 . 0 2 4 7 5 4 9 8 \cos ( 2 x - 1 ) \pi - 0 . 0 6 9 7 5 7 0 \cos 2 ( 2 x - 1 ) \pi$ $+ 0 . 0 8 4 6 8 3 1 7 \cos 3 ( 2 x - 1 ) \pi - 0 . 0 4 3 8 6 4 7 9 \cos 4 ( 2 x - 1 ) \pi$ + 0.2268260 sin(2x − 1)π $- 0 . 1 0 2 1 6 4 0 \sin 2 ( 2 x - 1 ) \pi + 0 . 0 4 2 8 4 6 4 8 \sin 3 ( 2 x - 1 ) \pi$ .

(b) 0.1735500   
(c) 0.2232443

5. The trigonometric polynomials give the following integral approximations.

<table><tr><td>Approximation</td><td>Actual</td></tr><tr><td>(a) -69.76415</td><td>-62.01255</td></tr><tr><td>(b) 9.869602</td><td>9.869604</td></tr><tr><td>（c） -0.7943605</td><td>-0.2739383</td></tr><tr><td>(d) -0.9593287</td><td>-0.9557781</td></tr></table>

6. The $b _ { k }$ terms are all zero. The $a _ { k }$ terms are

$a _ { 0 } = - 4 . 0 1 2 8 7 5 8 6$ , $a _ { 1 } = 3 . 8 0 2 7 6 9 0 3$ , $a _ { 2 } = - 2 . 2 3 5 1 9 8 7 0$ , $a _ { 3 } = 0 . 6 3 8 1 0 4 0 3$ , $a _ { 4 } = - 0 . 3 1 5 5 0 8 2 1$ , $a _ { 5 } = 0 . 1 9 4 0 8 1 4 5$ , $a _ { 6 } = - 0 . 1 3 4 6 4 4 9 1$ , $a _ { 7 } = 0 . 1 0 1 0 0 5 9 3$ , $a _ { 8 } = - 0 . 0 8 0 1 5 7 0 8$ , $a _ { 9 } = 0 . 0 6 6 4 3 5 9 8$ , $a _ { 1 0 } = - 0 . 0 5 7 0 4 3 5 3$ , $a _ { 1 1 } = 0 . 0 5 0 4 6 6 7 5$ , $a _ { 1 2 } = - 0 . 0 4 5 8 3 4 3 1$ , $a _ { 1 3 } = 0 . 0 4 2 6 2 3 1 8$ , $a _ { 1 4 } = - 0 . 0 4 0 5 1 3 9 5$ , $a _ { 1 5 } = 0 . 0 3 9 3 1 5 8 4$ , and $a _ { 1 6 } = - 0 . 0 3 8 9 2 7 1 3$ .

7. The $b _ { j }$ terms are all zero. The $a _ { j }$ terms are as follows:

$^ { * } 8$ . Since $( \cos x ) ^ { 2 } = { \frac { 1 } { 2 } } + { \frac { 1 } { 2 } } \cos 2 x$

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos m x _ { j } ) ^ { 2 } = \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } 1 + \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } \cos 2 m x _ { j } = m + \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } \cos 2 m x _ { j } .
$$

However,

$$
\cos 2 m x _ { j } = \cos 2 m \left( - \pi + { \frac { j } { m } } \pi \right) = \cos ( 2 j \pi - 2 m \pi ) = \cos ( 2 j - 2 m ) \pi = ( - 1 ) ^ { 2 j - 2 m } = 1 .
$$

Thus

$$
\sum _ { j = 0 } ^ { 2 m - 1 } ( \cos m x _ { j } ) ^ { 2 } = m + \frac { 1 } { 2 } \sum _ { j = 0 } ^ { 2 m - 1 } 1 = m + m = 2 m .
$$

\*9. From Eq. (8.28),

$$
c _ { k } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } e ^ { \frac { \pi i j k } { m } } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } ( \zeta ) ^ { j k } = \sum _ { j = 0 } ^ { 2 m - 1 } y _ { j } \left( \zeta ^ { k } \right) ^ { j } .
$$

Thus

$$
\begin{array} { r } { c _ { k } = \left( 1 , \zeta ^ { k } , \zeta ^ { 2 k } , \dots , \zeta ^ { \left( 2 m - 1 \right) k } \right) ^ { t } \left[ \begin{array} { c } { y _ { 0 } } \\ { y _ { 1 } } \\ { \vdots } \\ { y _ { 2 m - 1 } } \end{array} \right] , } \end{array}
$$

and the result follows.

10. We have $\mathbf { c } = A \mathbf { d }$ , $\mathbf { d } = B \mathbf { e }$ , $\mathbf { e } = C \mathbf { f }$ , and $\mathbf { f } = D \mathbf { y }$ , where

$$
\begin{array} { r } { A = \left[ \begin{array} { c c c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] , \quad B = \left[ \begin{array} { c c c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - i } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { - i } & { - i } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] , } \end{array}
$$

$$
C = \left[ \begin{array} { c c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - i } & { - i } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { \frac { - i + 1 } { \sqrt { 2 } } } & { \frac { - i + 1 } { \sqrt { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \frac { - i - 1 } { \sqrt { 2 } } } & { \frac { - i - 1 } { \sqrt { 2 } } } \\ { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { - 1 } \end{array} \right] ,
$$

and

$$
D = \left[ \begin{array} { c c c c c c c c } { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { i } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { i } & { 0 } \\ { 0 } & { \frac { i - 1 } { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \frac { i - 1 } { \sqrt { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \frac { - ( i + 1 ) } { \sqrt { 2 } } } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { \frac { ( i + 1 ) } { \sqrt { 2 } } } \end{array} \right] .
$$

Note that $\mathbf { c } = A B C D \mathbf { y }$ , which would give Eq. (8.28) if expanded.

# Approximating Eigenvalues

# Exercise Set 9.1, page 568

1. \*(a) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = 2 , \mathbf { v } ^ { ( 1 ) } = ( 1 , 0 , 0 ) ^ { t }$ ; $\lambda _ { 2 } = 1 , \mathbf { v } ^ { ( 2 ) } =$ $( 0 , 2 , 1 ) ^ { t }$ ; and $\lambda _ { 3 } = - 1 , \mathbf { v } ^ { ( 3 ) } = ( - 1 , 1 , 1 ) ^ { t }$ . The set is linearly independent. (b) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = 2 , \mathbf { v } ^ { ( 1 ) } = ( 0 , 1 , 0 ) ^ { t }$ ; $\lambda _ { 2 } = 3 , { \bf v } ^ { ( 2 ) } =$ $( 1 , 0 , 1 ) ^ { t }$ ; and $\lambda _ { 3 } = 1 , \mathbf { v } ^ { ( 3 ) } = ( 1 , 0 , - 1 ) ^ { t }$ . The set is linearly independent. (c) The eigenvalues and associated eigenvectors are $\lambda _ { \underline { { { 1 } } } } = 1 , { \bf v } ^ { ( 1 ) } = ( 0 , - 1 , 1 ) ^ { t } ; \lambda _ { 2 } = 1 +$ $\sqrt { 2 } , \mathbf { v } ^ { ( 2 ) } = ( \sqrt { 2 } , 1 , 1 ) ^ { t }$ ; and $\lambda _ { 3 } = 1 - \sqrt { 2 } , \mathbf { v } ^ { ( 3 ) } = ( - \sqrt { 2 } , 1 , 1 ) ^ { t } .$ . The set is linearly independent. (d) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = \lambda _ { 2 } = 2$ with $\mathbf { v } ^ { ( 1 ) } = ( 1 , 0 , 0 ) ^ { t }$ and $\lambda _ { 3 } = 3$ with $\mathbf { v } ^ { ( 3 ) } = ( 0 , 1 , 1 ) ^ { t }$ . There are not three linearly independent eigenvectors.   
2. (a) Eigenvalue $\lambda _ { 1 } ~ = ~ 1$ has multiplicity 3 and eigenvectors $\mathbf { v } ^ { ( 1 ) } = ( - 1 , 1 , 0 ) ^ { t }$ and ${ \bf v } ^ { ( 2 ) } =$ $( 1 , 0 , 1 ) ^ { t }$ . There are not three linearly independent eigenvectors. (b) Eigenvalue $\lambda _ { 1 } ~ = ~ 3$ has multiplicity 2 and eigenvectors $\mathbf { v } ^ { ( 1 ) } = ( - 1 , 1 , 0 ) ^ { t }$ and ${ \bf v } ^ { ( 2 ) } =$ $( - 1 , 0 , 1 ) ^ { t }$ . Eigenvalue $\lambda _ { 2 } = 0$ has eigenvector $\mathbf { v } ^ { ( 3 ) } = ( 1 , 1 , 1 ) ^ { t }$ . There are three linearly independent eigenvectors. (c) Eigenvalue $\lambda _ { 1 } = 4$ has eigenvector $\mathbf { v } ^ { ( 1 ) } = ( 1 , 1 , 1 ) ^ { t }$ . Eigenvalue $\lambda _ { 2 } = 1$ has multiplicity 2 and eigenvectors $\mathbf { v } ^ { ( 2 ) } = ( - 1 , 1 , 0 ) ^ { t }$ and $\mathbf { v } ^ { ( 3 ) } = ( - 1 , 0 , 1 ) ^ { t }$ . There are three linearly independent eigenvectors. (d) Eigenvalue $\lambda _ { 1 } ~ = ~ 2$ has multiplicity 2 and eigenvectors $\mathbf { v } ^ { ( 1 ) } \ = \ ( 1 , 0 , 0 ) ^ { t }$ and ${ \bf v } ^ { ( 2 ) } =$ $( 0 , - 1 , 1 ) ^ { t }$ . Eigenvalue $\lambda _ { 2 } = 3$ has eigenvector $\mathbf { v } ^ { ( 3 ) } = ( 1 , 1 , 0 ) ^ { t }$ . There are three linearly independent eigenvectors.

3. The eigenvalues are within the Gerˇsgorin circles that are shown.

(a) The three eigenvalues are within $\{ \lambda | | \left| \lambda \right| \leq 2 \} \cup \{ \lambda | | \left| \lambda - 2 \right| \leq 2 \}$ so $\rho ( A ) \leq 4$ .

![](images/415498a97e541154ddd14dfc43d29df2c69db064ad3e92eb960de4b75e491f13.jpg)

(b) The three eigenvalues are within $\{ \lambda | \ | \lambda - 4 | \le 2 \}$ so $\rho ( A ) \leq 6$ .

![](images/907031ba5cffdcdc4b7883def90c31e9d2e9c20dca03c3149205f596e6acbf4e.jpg)

(c) The three real eigenvalues satisfy $0 \leq \lambda \leq 6$ so $\rho ( A ) \leq 6$ .

![](images/4ffebbe294c13765f19e65b4dcaeade775bc19663ac74ef7e81152475f28cd49.jpg)

(d) The three real eigenvalues satisfy $1 . 2 5 \le \lambda \le 8 . 2 5$ so $1 . 2 5 \le \rho ( A ) \le 8 . 2 5$ .

![](images/af7bccc30961bb6ae1bbd1d10dadf4b06f8c6b6357a3da4d17769fa7afdea554.jpg)

4. The eigenvalues are within the Gerˇsgorin circles that are shown.

(a) The four real eigenvalues satisfy $- 8 \leq \lambda \leq 1$ , so $\rho ( A ) \leq 8$ .

![](images/0d401b2afa4916b2feed4fb937c30fcebf6644711317ec4f6324368f82d78bc9.jpg)

\*(b) The real eigenvalues satisfy $- 2 \leq \lambda \leq 6$ , so $\rho ( A ) \leq 6$ .

![](images/a52aaf2d0d16b06eca369418f7f46901196a7b0057f13f7f3130a3f09fa460fd.jpg)

(c) The four real eigenvalues satisfy $- 2 \leq \lambda \leq 6$ , so $\rho ( A ) \leq 6$ .

![](images/8c86f9040b68cb6a2203b1d5045b4ba04914a262a5dfaf0b0a1faea0f6160af7.jpg)

(d) The real eigenvalues satisfy either $1 \leq \lambda \leq 5$ or $6 \leq \lambda \leq 1 2$ , so $1 \leq \rho ( A ) \leq 1 2$

![](images/a44e99803ea9627d1ca8aa03aaa855641f45b12be0de117eb561e70a6bc8c5c0.jpg)

5. All the matrices except (d) have 3 linearly independent eigenvectors. The matrix in part (d) has only 2 linearly independent eigenvectors. One choice for $P$ is each case is

\*(a)

$$
\left[ { \begin{array} { r r r } { - 1 } & { 0 } & { 1 } \\ { 1 } & { 2 } & { 0 } \\ { 1 } & { 1 } & { 0 } \end{array} } \right] ,
$$

$$
\left[ { \begin{array} { r r r } { 0 } & { - 1 } & { 1 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } \end{array} } \right] ,
$$

(c)

$$
\left[ { \begin{array} { r r r } { 0 } & { { \sqrt { 2 } } } & { - { \sqrt { 2 } } } \\ { - 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { 1 } \end{array} } \right] ,
$$

6. (a) This matrix is not factorable because it does not have 3 linearly independent eigenvectors. (b)

$$
P = \left[ { \begin{array} { c c c } { 1 } & { 1 } & { 1 } \\ { 1 } & { 0 } & { - 1 } \\ { 1 } & { - 1 } & { 0 } \end{array} } \right] , \quad P ^ { - 1 } = { \frac { 1 } { 3 } } \left[ { \begin{array} { c c c } { 1 } & { 1 } & { 1 } \\ { 1 } & { 1 } & { - 2 } \\ { 1 } & { - 2 } & { 1 } \end{array} } \right] , \quad { \mathrm { a n d } } \quad D = P = \left[ { \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 3 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} } \right] .
$$

(c)

$$
P = \left[ \begin{array} { c c c } { 1 } & { 1 } & { 1 } \\ { 0 } & { - 1 } & { 1 } \\ { - 1 } & { 0 } & { 1 } \end{array} \right] , \quad P ^ { - 1 } = \frac { 1 } { 3 } \left[ \begin{array} { c c c } { 1 } & { 1 } & { - 2 } \\ { 1 } & { - 2 } & { 1 } \\ { 1 } & { 1 } & { 1 } \end{array} \right] , \quad \mathrm { a n d } \quad D = P = \left[ \begin{array} { c c c } { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 4 } \end{array} \right] .
$$

(d)

$$
P = \left[ { \begin{array} { c c c } { 1 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 1 } \\ { 0 } & { - 1 } & { 0 } \end{array} } \right] , \quad P ^ { - 1 } = \left[ { \begin{array} { c c c } { 1 } & { - 1 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 1 } \end{array} } \right] , \quad \mathrm { a n d } \quad D = P = \left[ { \begin{array} { c c c } { 2 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} } \right] .
$$

7. The vectors are linearly dependent because $- 2 v _ { 1 } + 7 v _ { 2 } - 3 v _ { 3 } = 0$ .

$^ { * } 8$ . The vectors are linearly independent if and only if the matrix formed by having these vectors as columns (or rows) is nonsingular, which is true if and only if the determinant of this matrix is nonzero. Since

$$
\operatorname* { d e t } { \left[ \begin{array} { l l l } { 0 } & { 0 } & { - 2 } \\ { 1 } & { 2 } & { ~ 0 } \\ { 1 } & { 1 } & { ~ 1 } \end{array} \right] } = 2 ,
$$

the vectors are linearly independent.

9. If $c _ { 1 } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + c _ { k } \mathbf { v } _ { k } = \mathbf { 0 }$ , then for any $j$ , with $1 \le j \le k$ , we have $c _ { 1 } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + c _ { k } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { k } = \mathbf { 0 }$ . But orthogonality gives $c _ { i } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { i } = 0$ , for $i \neq j$ , so $c _ { j } \mathbf { v } _ { j } ^ { t } \mathbf { v } _ { j } = 0$ and since $\mathbf { v } _ { j } ^ { t } \mathbf { v } _ { j } \neq 0$ , we must have $c _ { j } = 0$ .

$^ { * } 1 0$ . There must be a largest subset $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j } \right\}$ , with $j ~ \leq ~ k$ that is linearly independent because the set with the nonzero vector $\{ { \bf x } _ { 1 } \}$ is linearly independent. Suppose that we have this largest linearly independent set and that $j < k$ . Then $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j } , \mathbf { x } _ { j + 1 } \right\}$ is linearly dependent and there is a set of constants $\{ c _ { 1 } , c _ { 2 } , \ldots , c _ { j } \}$ , not all zero, with

$$
\mathbf { x } _ { j + 1 } = c _ { 1 } \mathbf { x } _ { 1 } + c _ { 2 } \mathbf { x } _ { 2 } + \cdot \cdot \cdot + c _ { j } \mathbf { x } _ { j } .
$$

Because these are all eigenvectors, $A { \bf x } _ { i } = \lambda _ { i } { \bf x } _ { i }$ for each $i = 1 , 2 , \ldots j + 1$ , so

$$
A \mathbf { x } _ { j + 1 } = \lambda _ { j + 1 } \mathbf { x } _ { j + 1 } = c _ { 1 } \lambda _ { 1 } \mathbf { x } _ { 1 } + c _ { 2 } \lambda _ { 2 } \mathbf { x } _ { 2 } + \cdot \cdot \cdot + c _ { j } \lambda _ { j } \mathbf { x } _ { j } .
$$

But we also have

$$
\lambda _ { j + 1 } \mathbf { x } _ { j + 1 } = c _ { 1 } \lambda _ { j + 1 } \mathbf { x } _ { 1 } + c _ { 2 } \lambda _ { j + 1 } \mathbf { x } _ { 2 } + \cdot \cdot \cdot + c _ { j } \lambda _ { j + 1 } \mathbf { x } _ { j } ,
$$

and subtracting these equations gives

$$
\mathbf { \Gamma } _ { + 1 } ) \mathbf { x } _ { 1 } + c _ { 2 } ( \lambda _ { 2 } - \lambda _ { j + 1 } ) \mathbf { x } _ { 2 } + \cdots c _ { j } ( \lambda _ { j } - \lambda _ { j + 1 } ) \mathbf { x } _ { j }
$$

But the set $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j } \right\}$ was assumed to be linearly independent, so we must have

$$
0 = c _ { 1 } ( \lambda _ { 1 } - \lambda _ { j + 1 } ) = c _ { 2 } ( \lambda _ { 2 } - \lambda _ { j + 1 } ) = \cdots = c _ { j } ( \lambda _ { j } - \lambda _ { j + 1 } ) .
$$

Since eigenvalues are all distinct, this implies that $0 = c _ { 1 } = c _ { 2 } = \cdot \cdot \cdot = c _ { j }$ . This contradicts the original statement that $\mathbf { x } _ { j + 1 }$ could be written as a combination of the vectors $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { j }$ . The only assumption that was made was that $j < k$ , and this statement must be false. As a consequence, the entire set $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k } \right\}$ must be linearly independent.

11. Since $\{ { \bf v } _ { i } \} _ { i = 1 } ^ { n }$ is linearly independent in $\mathbb { R } ^ { n }$ , there exist numbers $c _ { 1 } , \ldots , c _ { n }$ with

$$
\mathbf { x } = c _ { 1 } \mathbf { v } _ { 1 } + \cdots + c _ { n } \mathbf { v } _ { n } .
$$

Hence, for any $k$ , with $1 \leq k \leq n$ ,

$$
\mathbf { v } _ { k } ^ { t } \mathbf { x } = c _ { 1 } \mathbf { v } _ { k } ^ { t } \mathbf { v } _ { 1 } + \cdot \cdot \cdot + c _ { n } \mathbf { v } _ { k } ^ { t } \mathbf { v } _ { n } = c _ { k } \mathbf { v } _ { k } ^ { t } \mathbf { v } _ { k } = c _ { k } .
$$

$^ { \ast } 1 2$ . Not necessarily. Consider the vectors $\mathbf { x } _ { 1 } = ( 1 , 0 ) ^ { t }$ , $\mathbf { x } _ { 2 } = ( 0 , 1 ) ^ { t }$ , and $\mathbf { x } _ { 3 } = ( 1 , 1 ) ^ { t }$ .

13. (a) (i) $\begin{array} { r } { | \mathbf { 0 } = c _ { 1 } ( 1 , 1 ) ^ { t } + c _ { 2 } ( - 2 , 1 ) ^ { t } \operatorname { i m p l i e s } \operatorname { t h a t } \left[ \begin{array} { l l } { 1 } & { - 2 } \\ { 1 } & { 1 } \end{array} \right] \left[ \begin{array} { l } { c _ { 1 } } \\ { c _ { 2 } } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 0 } \end{array} \right] . \operatorname { B u t } \operatorname* { d e t } \left[ \begin{array} { l l } { 1 } & { - 2 } \\ { 1 } & { 1 } \end{array} \right] = \left[ \begin{array} { l } { 0 } \\ { 1 } & { - 2 } \end{array} \right] . } \end{array}$ $3 \neq 0$ so by Theorem 6.7 we have $c _ { 1 } = c _ { 2 } = 0$ . (ii) $\{ ( 1 , 1 ) ^ { t } , ( - 3 / 2 , 3 / 2 ) ^ { t } \}$ . (iii) $\{ ( { \sqrt { 2 } } / 2 , { \sqrt { 2 } } / 2 ) ^ { t } , ( - { \sqrt { 2 } } / 2 , { \sqrt { 2 } } / 2 ) ^ { t } \} .$ .

(b) (i) The determinant of this matrix is $- 2 \neq 0$ , so $\{ ( 1 , 1 , 0 ) ^ { t } , ( 1 , 0 , 1 ) ^ { t } , ( 0 , 1 , 1 ) ^ { t } \}$ is a linearly independent set. (ii) (iii) $\begin{array} { r l } & { \{ ( 1 , 1 , 0 ) ^ { t } , ( 1 / 2 , - 1 / 2 , 1 ) ^ { t } , ( - 2 / 3 , 2 / 3 , 2 / 3 ) ^ { t } \} } \\ & { \{ ( \sqrt { 2 } / 2 , \sqrt { 2 } / 2 , 0 ) ^ { t } , ( \sqrt { 6 } / 6 , - \sqrt { 6 } / 6 , \sqrt { 6 } / 3 ) ^ { t } , ( - \sqrt { 3 } / 3 , \sqrt { 3 } / 3 , \sqrt { 3 } / 3 ) ^ { t } \} } \end{array}$

(c) (i) If $\mathbf { 0 } = c _ { 1 } ( 1 , 1 , 1 , 1 ) ^ { t } + c _ { 2 } ( 0 , 2 , 2 , 2 ) ^ { t } + c _ { 3 } ( 1 , 0 , 0 , 1 ) ^ { \textnormal { \scriptsize } }$ t, then we have $( E _ { 1 } ) : c _ { 1 } + c _ { 3 } = 0 , \quad ( E _ { 2 } ) : c _ { 1 } + 2 c _ { 2 } = 0 , \quad ( E _ { 3 } ) : c _ { 1 } + 2 c _ { 2 } = 0 , \quad ( E _ { 4 } ) : c _ { 1 } + 2 c _ { 2 } + c _ { 3 } = 0 .$ Subtracting ( $E _ { 3 }$ ) from ( $E _ { 4 }$ ) implies that $c _ { 3 } = 0$ . Hence, from ( $E _ { 1 }$ ) we have $c _ { 1 } = 0$ , and from ( $E _ { 2 }$ ) we have $c _ { 2 } = 0$ . The vectors are linearly independent. (ii) $\{ ( 1 , 1 , 1 , 1 ) ^ { t } , ( - 3 / 2 , 1 / 2 , 1 / 2 , 1 / 2 ) ^ { t } , ( 0 , - 1 / 3 , - 1$ 1/3, 2/3)t} (iii) $\{ ( 1 / 2 , 1 / 2 , 1 / 2 , 1 / 2 ) ^ { t } , ( - \sqrt { 3 } / 2 , \sqrt { 3 } / 6 , \sqrt { 3 } / 6 , \sqrt { 3 } / 6 ) ^ { t } , ( 0 , - \sqrt { 6 } / 6 , - \sqrt { 6 } / 6 , \sqrt { 6 } / 3 ) ^ { t } \}$

(d) (i) If $A$ is the matrix whose columns are the vectors $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \mathbf { v } _ { 3 } , \mathbf { v } _ { 4 } , \mathbf { v } _ { 5 }$ , then $\operatorname* { d e t } A = 6 0 \neq 0$ , so the vectors are linearly independent. (iii) (ii) $\begin{array} { r l } & { ( 2 , 2 , 3 , 2 , 3 ) ^ { t } , ( 2 , - 1 , 0 , - 1 , 0 ) ^ { t } , ( 0 , 0 , 1 , 0 , - 1 ) ^ { t } , ( 1 , 2 , - 1 , 0 , - 1 ) ^ { t } , ( - 2 / 7 , 3 / 7 , 2 / 7 , - 1 , 2 / 7 ) ^ { t } \} } \\ & { \{ ( \sqrt { 3 0 } / 1 5 , \sqrt { 3 0 } / 1 5 , \sqrt { 3 0 } / 1 0 , \sqrt { 3 0 } / 1 5 , \sqrt { 3 0 } / 1 0 ) ^ { t } , ( \sqrt { 6 } / 3 , - \sqrt { 6 } / 6 , 0 , - \sqrt { 6 } / 6 , 0 ) ^ { t } , } \\ & { \sqrt { 2 } / 2 , 0 , - \sqrt { 2 } / 2 ) ^ { t } , ( \sqrt { 7 } / 7 , 2 \sqrt { 7 } / 7 , - \sqrt { 7 } / 7 , 0 , - \sqrt { 7 } / 7 ) ^ { t } , } \\ & { 7 0 / 3 5 , 3 \sqrt { 7 0 } / 7 0 , \sqrt { 7 0 } / 3 5 , - \sqrt { 7 0 } / 1 0 , \sqrt { 7 0 } / 3 5 ) ^ { t } \} } \end{array}$

14. To show linear independence we will show that the matrix whose columns are the given vectors has a nonzero determinant. In case there are fewer vectors than the dimension of the space we can add a vector or vectors to complete the matrix. If the larger set is linearly independent, the original set will also be linearly independent.

(a) (i) The matrix has determinant 7. (ii) The set $\left\{ ( 2 , - 1 ) ^ { t } , { \frac { 1 } { 5 } } ( 1 , 2 ) ^ { t } \right\}$ is orthogonal. (iii) The set $\left\{ { \frac { \sqrt { 5 } } { 5 } } ( 2 , - 1 ) ^ { t } , { \frac { \sqrt { 5 } } { 5 } } ( 1 , 2 ) ^ { t } \right\}$ is orthonormal.

(b) (i) The matrix has determinant $- 2$ . (iii) The set (ii) The set $\begin{array} { r l } & { \left\{ ( 2 , - 1 , 1 ) ^ { t } , \frac { 1 } { 2 } ( 0 , 1 , 1 ) ^ { t } , \frac { 2 } { 3 } ( 1 , 1 , - 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o g o n a l } . } \\ & { \left\{ \frac { \sqrt { 6 } } { 6 } ( 2 , 1 - , 1 ) ^ { t } , \frac { \sqrt { 2 } } { 2 } ( 0 , 1 , 1 ) ^ { t } , \frac { \sqrt { 3 } } { 3 } ( 1 , 1 , - 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o n o r m a l } . } \end{array}$ (c) (i) The matrix with the vector $( 0 , 0 , 0 , 1 ) ^ { t }$ added in the last column has determinant 1. (iii) The set (ii) The set $\begin{array} { r l } & { \left\{ ( 1 , 1 , 1 , 1 ) ^ { t } , \frac { 1 } { 4 } ( - 3 , 1 , 1 , 1 ) ^ { t } , \frac { 1 } { 3 } ( 0 , - 2 , 1 , 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o g o n a l } . } \\ & { \left\{ \frac { 1 } { 2 } ( 1 , 1 , 1 , 1 ) ^ { t } , \frac { \sqrt { 3 } } { 6 } ( 3 , - 1 , - 1 , - 1 ) ^ { t } , \frac { \sqrt { 6 } } { 6 } ( 0 , - 2 , 1 , 1 ) ^ { t } \right\} \mathrm { i s ~ o r t h o n o r m a l } . } \end{array}$ (d) (i) The matrix with the vector $( 0 , 0 , 1 , 0 , 0 ) ^ { t }$ added in the last column has determinant 12. (ii) The set $\left\{ ( 2 , 2 , 0 , 2 , 1 ) ^ { t } , \frac { 3 } { 1 3 } ( - 5 , 8 , 0 , - 5 , 4 ) ^ { t } , \frac { 1 } { 1 0 } ( - 5 , 2 , 0 , 5 , - 4 ) ^ { t } , \frac { 4 } { 7 } ( - 1 , - 1 , 0 , 1 , 2 ) ^ { t } \right\} ^ { - 1 } ,$ is orthogonal. (iii) The set $\left\{ \frac { \sqrt { 1 3 } } { 1 3 } ( 2 , 2 , 0 , 2 , 1 ) ^ { t } , \frac { 1 3 \sqrt { 1 3 0 } } { 1 6 9 0 } ( 5 , - 8 , 0 , 5 , - 4 ) ^ { t } , \frac { \sqrt { 7 0 } } { 7 0 } ( 5 , - 2 , 0 , - 5 , 4 ) ^ { t } , - \frac { \sqrt { 7 } } { 7 } ( 1 , 1 , 0 , - 1 , - 2 ) ^ { t } \right\}$

is orthonormal.

$^ \ast 1 5$ . If $A$ is a strictly diagonally dominant matrix, then in each row, the sum of the magnitudes of the off-diagonal entries in the row are less than the magnitude of the diagonal entry in that row. By Gerˇsgorin Circle Theorem this implies that for each row the magnitude of the center of the Gerˇsgorin circle for that row exceeds the radius so the circle does not contain the origin. Hence 0 cannot be in any Gerˇsgorin circle and consequently cannot be an eigenvalue of $A$ . This implies that $A$ in nonsingular.

$^ *$ 16. Let $( X ) _ { k } = \left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { k } \right\}$ and define the set $( V ) _ { k } = \left\{ \mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots , \mathbf { v } _ { k } \right\}$ in the Gram-Schmidt manner as

$$
\mathbf { v } _ { 1 } = \mathbf { x } _ { 1 } , \quad { \mathrm { a n d } } \quad \mathbf { v } _ { k } = \mathbf { x } _ { k } - \sum _ { i = 1 } ^ { k - 1 } \left( { \frac { \mathbf { v } _ { i } ^ { t } \mathbf { x } _ { k } } { \mathbf { v } _ { i } ^ { t } \mathbf { v } _ { i } } } \right) \mathbf { v } _ { i } .
$$

for each $k > 1$ . We will use Mathematical Induction to show that $( V ) _ { k }$ is orthogonal for every integer $k$ .

First note that since

$$
\mathbf { v } _ { 1 } = \mathbf { x } _ { 1 } , \quad { \mathrm { a n d } } \quad \mathbf { v } _ { 2 } = \mathbf { x } _ { 2 } - \left( { \frac { \mathbf { v } _ { 1 } ^ { t } \mathbf { x } _ { 2 } } { \mathbf { v } _ { 1 } ^ { t } \mathbf { v } _ { 1 } } } \right) \mathbf { v } _ { 1 } ,
$$

we have

$$
\mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { v } _ { 2 } = \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { x } _ { 2 } - \left( { \frac { \mathbf { v } _ { 1 } ^ { t } \mathbf { x } _ { 2 } } { \mathbf { v } _ { 1 } ^ { t } \mathbf { v } _ { 1 } } } \right) \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { v } _ { 1 } = \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { x } _ { 2 } - \mathbf { v } _ { 1 } ^ { t } \cdot \mathbf { x } _ { 2 } = 0 ,
$$

so $( V ) _ { 2 }$ is an orthogonal set.

Now assume that $( V ) _ { j }$ is orthogonal for some positive integer $j$ , and consider $( V ) _ { j + 1 }$ . Since $( V ) _ { j }$ is orthogonal the set $( V ) _ { j + 1 }$ will be orthogonal if and only if $\mathbf { v } _ { s } ^ { t } \cdot \mathbf { v } _ { j + 1 } = 0$ for each $s = 1 , 2 , \dots j$ .

For each $s = 1 , 2 , . . . j$ we have

$$
\begin{array} { l } { { \displaystyle { \bf v } _ { s } ^ { t } \cdot { \bf v } _ { j + 1 } ^ { t } = { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } - \sum _ { i = 1 } ^ { j } \left( \frac { { \bf v } _ { i } ^ { t } { \bf x } _ { j + 1 } } { { \bf v } _ { i } ^ { t } { \bf v } _ { i } } \right) ( { \bf v } _ { s } ^ { t } \cdot { \bf v } _ { i } ) } \ ~ } \\ { { \displaystyle ~ = { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } - \left( \frac { { \bf v } _ { s } ^ { t } { \bf x } _ { j + 1 } } { { \bf v } _ { s } ^ { t } { \bf v } _ { s } } \right) ( { \bf v } _ { s } ^ { t } \cdot { \bf v } _ { s } ) = { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } - { \bf v } _ { s } ^ { t } \cdot { \bf x } _ { j + 1 } ^ { t } = 0 } . } \end{array}
$$

So $( V ) _ { j }$ being orthogonal implies that $( V ) _ { j + 1 }$ is also orthogonal. Mathematical Induction implies that $( V ) _ { j }$ is true for all positive integers $j$ .

17. (a) Let $\mu$ be an eigenvalue of $A$ . Since $A$ is symmetric, $\mu$ is real and Theorem 9.13 gives $0 \leq \mu \leq 4$ . The eigenvalues of $A - 4 I$ are of the form $\mu - 4$ . Thus,

$$
\rho ( A - 4 I ) = \operatorname* { m a x } \lvert \mu - 4 \rvert = \operatorname* { m a x } ( 4 - \mu ) = 4 - \operatorname* { m i n } \mu = 4 - \lambda = \lvert \lambda - 4 \rvert .
$$

(b) The eigenvalues of $A - 4 I$ are $- 3 . 6 1 8 0 3 4$ , $- 2 . 6 1 8 0 3 4$ , −1.381966, and $- 0 . 3 8 1 9 6 6$ , so $\rho ( A - 4 I ) = 3 . 6 1 8 0 3 4$ and $\lambda = 0 . 3 8 1 9 6 6$ . An eigenvector is $( 0 . 6 1 8 0 3 4 , 1 , 1 , 0 . 6 1 8 0 3 4 ) ^ { t }$ .

(c) As in part (a), $0 \le \mu \le 6$ , so $\lvert \lambda - 6 \rvert = \rho ( B - 6 I )$ .

(d) The eigenvalues of $B - 6 I$ are $- 5 . 2 3 6 0 6 7 3$ , $^ { - 4 }$ , $- 2$ , and $- 0 . 7 6 3 9 3 2 0 2$ , so $\rho ( B - 6 I ) =$ 5.2360673 and $\lambda = 0 . 7 6 3 9 3 2 7$ . An eigenvector is $( 0 . 6 1 8 0 3 3 9 5 , 1 , 1 , 0 . 6 1 8 0 3 9 5 ) ^ { \iota }$ t.

# Exercise Set 9.2, page 573

1. In each instance we will compare the characteristic polynomial of $A$ ( $C ( A )$ ) to that of $B$ . They must agree if the matrices are to be similar.

$$
\begin{array} { r l } & { p ( A ) = x ^ { 2 } - 4 x + 3 \neq x ^ { 2 } - 2 x - 3 = p ( B ) . } \\ & { p ( A ) = x ^ { 2 } - 5 x + 6 \neq x ^ { 2 } - 6 x + 6 = p ( B ) . } \\ & { p ( A ) = x ^ { 3 } - 4 x ^ { 2 } + 5 x - 2 \neq x ^ { 3 } - 4 x ^ { 2 } + 5 x - 6 = p ( B ) . } \\ & { p ( A ) = x ^ { 3 } - 5 x ^ { 2 } + 1 2 x - 1 1 \neq x ^ { 3 } - 4 x ^ { 2 } + 4 x + 1 1 = p ( B ) . } \end{array}
$$

2. For a pair of matrices to be similar the determinants and characteristic polynomials must be the same.

(a) $\operatorname* { d e t } ( A ) = 3 \neq 2 = \operatorname* { d e t } ( B )$

(b) $\operatorname* { d e t } ( A ) = - 4 = \operatorname* { d e t } ( B )$ , but $p ( A ) = \lambda ^ { 2 } + \lambda - 4 \neq \lambda ^ { 2 } - \lambda - 4 = p ( B )$ . (c) (d) $\begin{array} { l } { \operatorname* { d e t } ( A ) = 1 \neq - 8 = \operatorname* { d e t } ( B ) } \\ { \operatorname* { d e t } ( A ) = - 2 4 \neq 0 = \operatorname* { d e t } ( B ) } \end{array}$

3. In each case we have $A ^ { 3 } = ( P D P ^ { ( - 1 ) } ) ( P D P ^ { ( - 1 ) } ) ( P D P ^ { ( - 1 ) } ) = P D ^ { 3 } P ^ { ( - 1 ) } .$

$$
\begin{array} { r l } { ( 8 ) \left[ \begin{array} { c c } { \frac { 2 6 } { 6 } } & { - \frac { 1 4 } { 1 5 } } \\ { - \frac { 2 1 } { 5 } } & { \frac { 1 } { 5 } } \end{array} \right] } & { } \\ { ( 6 ) \left[ \begin{array} { c c } { 1 } & { 9 } \\ { 0 } & { - 8 } \end{array} \right] } & { } \\ { ( \mathrm { c } ) \left[ \begin{array} { c c } { \frac { 8 } { 9 } } & { - \frac { 8 } { 8 } } \\ { \frac { 4 } { 5 } } & { - \frac { 3 } { 5 } } & { \frac { 2 } { 5 } } \\ { - \frac { 2 } { 5 } } & { \frac { 4 } { 5 } } & { - \frac { 6 } { 5 } } \end{array} \right] } & { } \\ { ( \mathrm { d } ) \left[ \begin{array} { c c } { 8 } & { 0 } \\ { 0 } & { 8 } \end{array} \right] } & { } \\ { ( \mathrm { d } ) \left[ \begin{array} { c c } { 0 } & { 8 } \\ { 0 } & { 0 } \end{array} \right] } & { } \end{array}
$$

4. (a) The technique is described in part (b). The result is

$$
\left[ { \begin{array} { c c } { 1 0 } & { - 6 } \\ { - 9 } & { 7 } \end{array} } \right] .
$$

\*(b) It would be easy to simply use $A ^ { 3 }$ from Exercise 3(b) and multiply by $A$ . However, we don’t explicitly have $A$ . Alternatively,

$$
A ^ { 4 } = P D ^ { 4 } P ^ { - 1 } = \left[ \begin{array} { c c } { { - 1 } } & { { 2 } } \\ { { 1 } } & { { 0 } } \end{array} \right] \left[ \begin{array} { c c } { { 1 6 } } & { { 0 } } \\ { { 0 } } & { { 1 } } \end{array} \right] \left[ \begin{array} { c c } { { 0 } } & { { 1 } } \\ { { { \frac { 1 } { 2 } } } } & { { { \frac { 1 } { 2 } } } } \end{array} \right] = \left[ \begin{array} { c c } { { 1 } } & { { - 1 5 } } \\ { { 0 } } & { { 1 6 } } \end{array} \right] .
$$

(c) The technique is described in part (b). The result is

$$
A ^ { 4 } = \frac 1 5 \left[ \begin{array} { l l l } { 7 } & { - 4 } & { 1 } \\ { 4 } & { - 3 } & { 2 } \\ { 2 } & { - 4 } & { 6 } \end{array} \right] .
$$

(d) The technique is described in part (b). The result is

$$
A ^ { 4 } = \left[ { \begin{array} { c c c } { 1 6 } & { 0 } & { 0 } \\ { 0 } & { 1 6 } & { 0 } \\ { 0 } & { 0 } & { 1 6 } \end{array} } \right] .
$$

5. They are all diagonalizable with $P$ and $D$ as follows.

$$
{ \begin{array} { r } { P = { \left[ \begin{array} { l l } { - 1 } & { { \frac { 1 } { 4 } } } \\ { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l } { 5 } & { 0 } \\ { 0 } & { 0 } \end{array} \right] } } \\ { P = { \left[ \begin{array} { l l } { 1 } & { - 1 } \\ { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { 3 } \end{array} \right] } } \end{array} }
$$

$$
{ \begin{array} { r l } & { P = { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 0 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 3 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } } \\ & { P = { \left[ \begin{array} { l l l } { { \sqrt { 2 } } } & { - { \sqrt { 2 } } } & { 0 } \\ { 1 } & { 1 } & { - 1 } \\ { 1 } & { 1 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 1 + { \sqrt { 2 } } } & { 0 } & { 0 } \\ { 0 } & { 1 - { \sqrt { 2 } } } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] } } \end{array} }
$$

$$
P = \left[ \begin{array} { c c } { { - 1 } } & { { 1 } } \\ { { 1 } } & { { 1 } } \end{array} \right] \mathrm { ~ a n d ~ } D = \left[ \begin{array} { c c } { { 1 } } & { { 0 } } \\ { { 0 } } & { { 3 } } \end{array} \right]
$$

$$
P = { \left[ \begin{array} { l l l } { 1 } & { - 1 } & { - 1 } \\ { 1 } & { 0 } & { 1 } \\ { 1 } & { 1 } & { 0 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 4 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 1 } \end{array} \right] }
$$

$$
P = { \left[ \begin{array} { l l l } { 0 } & { 1 } & { 1 } \\ { - 1 } & { 0 } & { 1 } \\ { 1 } & { 0 } & { 0 } \end{array} \right] } { \mathrm { ~ a n d ~ } } D = { \left[ \begin{array} { l l l } { 2 } & { 0 } & { 0 } \\ { 0 } & { 2 } & { 0 } \\ { 0 } & { 0 } & { 3 } \end{array} \right] }
$$

7. Only the matrices in parts (a) and (c) are positive definite.

$$
Q = \left[ { \begin{array} { r r } { - { \frac { \sqrt { 2 } } { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \\ { { \frac { \sqrt { 2 } } { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \end{array} } \right] { \mathrm { ~ a n d ~ } } D = \left[ { \begin{array} { c c } { 1 } & { 0 } \\ { 0 } & { 3 } \end{array} } \right]
$$

$$
* ( { \bf c } ) ~ Q = \left[ \begin{array} { r r r } { { \frac { \sqrt { 2 } } { 2 } } } & { { 0 } } & { { \frac { \sqrt { 2 } } { 2 } } } \\ { { 0 } } & { { 1 } } & { { 0 } } \\ { { - \frac { \sqrt { 2 } } { 2 } } } & { { 0 } } & { { \frac { \sqrt { 2 } } { 2 } } } \end{array} \right] \mathrm { ~ a n d ~ } D = \left[ \begin{array} { r r r } { { 1 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 2 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 3 } } \end{array} \right]
$$

8. The matrix will be positive definite if and only if the all the principle leading submatrices have a positive determinant. Let $A _ { n }$ denote the $n \times n$ principle leading submatrix of $A$ .

(a) $\operatorname* { d e t } ( A _ { 1 } ) = 4 \quad \operatorname* { d e t } ( A _ { 2 } ) = 1 2 , \quad \mathrm { a n d } \quad \operatorname* { d e t } ( A ) = 4 4$ , so $A$ is positive definite. A factorization $D = Q ^ { t } A Q$ has

$$
Q = \left[ \begin{array} { c c c } { 0 } & { \frac { \sqrt { 2 } } { 2 } } & { - \frac { \sqrt { 2 } } { 2 } } \\ { \frac { \sqrt { 5 } } { 4 } } & { \frac { \sqrt { 1 0 } } { 5 } } & { \frac { \sqrt { 1 0 } } { 5 } } \\ { - \frac { \sqrt { 5 } } { 2 } } & { \frac { \sqrt { 1 0 } } { 1 0 } } & { \frac { \sqrt { 1 0 } } { 1 0 } } \end{array} \right] \quad \mathrm { a n d } \quad D = \left[ \begin{array} { c c c } { 4 } & { 0 } & { 0 } \\ { 0 } & { 4 + \sqrt { 5 } } & { 0 } \\ { 0 } & { 0 } & { 4 - \sqrt { 5 } } \end{array} \right]
$$

(b) $\operatorname* { d e t } ( A ) = 0$ so $A$ is not positive definite.

(c) $\operatorname* { d e t } ( A ) = - 5$ so $A$ is not positive definite.

(d) $\operatorname * { l e t } ( A _ { 1 } ) = 8 \quad \operatorname * { d e t } ( A _ { 2 } ) = 4 8 , \quad \operatorname * { d e t } ( A _ { 3 } ) = 3 5 2 .$ , and $\operatorname* { d e t } ( A ) = 2 7 3 6$ , so $A$ is positive definite. A factorization $D = Q ^ { t } A Q$ has, approximately,

$$
\left[ { \begin{array} { r r r r } { - 0 . 6 0 0 5 } & { - 0 . 6 0 0 5 } & { - 0 . 4 4 9 6 } & { - 0 . 2 7 7 0 } \\ { - 0 . 7 0 7 1 } & { 0 . 7 0 7 1 } & { 0 } & { 0 } \\ { 0 . 2 8 4 4 } & { 0 . 2 8 4 4 } & { - 0 . 8 9 0 6 } & { 0 . 2 1 2 2 } \\ { - 0 . 2 4 1 9 } & { - 0 . 2 4 1 9 } & { 0 . 0 6 8 8 } & { 0 . 9 3 7 1 } \end{array} } \right] \quad { \mathrm { a n d } } \quad D = \left[ { \begin{array} { r r r r } { 1 3 . 9 5 8 7 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 4 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 6 . 4 8 4 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 7 . 5 5 7 2 } \end{array} } \right]
$$

9. In each case the matrix fails to have 3 linearly independent eigenvectors.

(a) $\operatorname* { d e t } ( A ) = 1 2$ , so $A$ is nonsingular.   
(b) $\operatorname* { d e t } ( A ) = - 1$ , so $A$ is nonsingular.   
\*(c) $\operatorname* { d e t } ( A ) = 1 2$ , so $A$ is nonsingular.   
(d) $\operatorname* { d e t } ( A ) = 1$ , so $A$ is nonsingular.

10. $^ *$ (a) The matrix is clearly singular because it has a row (and a column) all of whose entries are $0$ . However, the eigenvalues of $A$ , which are $\lambda _ { 1 } = 0$ , $\lambda _ { 2 } = 1$ , and $\lambda _ { 3 } = 3$ are distinct so the corresponding eigenvectors, $\mathbf { x } _ { 1 } = ( 0 , 0 , 1 ) ^ { t }$ , $\mathbf { x } _ { 1 } = ( 1 , 1 , 0 ) ^ { t }$ , and $\mathbf { x } _ { 3 } = ( 1 , - 1 , ) ^ { t }$ , can be used to form the columns of the matrix $P$ with $A = P D P ^ { - 1 }$ . The matrix $D$ is the diagonal matrix with diagonal entries in the order $0$ , $^ { 1 }$ , and 3.

(b) The eigenvalues of $A$ are $\lambda _ { 1 } ~ = ~ 0$ , $\lambda _ { 2 } ~ = ~ 3$ , and $\lambda _ { 3 } ~ = ~ 3$ , so $A$ is singular. However, there are three linearly independent eigenvectors of $A$ . The eigenvector $\mathbf { x } _ { 1 } = ( 1 , 1 , 1 ) ^ { t }$ , corresponding to $\lambda _ { 1 } = 0$ , and the eigenvectors $\mathbf { x } _ { 2 } ~ = ~ ( 1 , 0 , - 1 ) ^ { t }$ and $\mathbf { x } _ { 3 } ~ = ~ ( 1 , - 1 , 0 ) ^ { t }$ , corresponding to $\lambda _ { 2 } = \lambda _ { 3 } = 3$ . These eigenvectors can be used to form the columns of the matrix $P$ with $A = P D P ^ { - 1 }$ . The matrix $D$ is the diagonal matrix with diagonal entries in the order 0, 3, and 3.

11. (a) The eigenvalues and associated eigenvectors are $\lambda _ { 1 } = 5 . 3 0 7 8 5 7 5 6 3$ , (0.59020967, 0.51643129, 0.62044441)t; $\lambda _ { 2 } = - 0 . 4 2 1 3 1 1 2 9 9 3$ , $( 0 . 7 7 2 6 4 2 3 4 , - 0 . 1 3 8 7 6 2 7 8 , - 0 . 6 1 9 4 9 0 6 9 ) ^ { u }$ ; $\lambda _ { 3 } = - 0 . 1 3 6 5 4 6 2 6 4 7$ , $( 0 . 2 3 3 8 2 9 7 8 , - 0 . 8 4 5 0 1 1 0 2 , 0 . 4 8 0 9 1 5 8 1 ) ^ { \iota } .$ . (b) $A$ is not positive definite because $\lambda _ { 2 } < 0$ and $\lambda _ { 3 } < 0$ .

12. Since $B$ is nonsingular, $B ^ { - 1 }$ exists and

$$
A B = I \cdot ( A B ) = ( B ^ { - 1 } B ) ( A B ) = B ^ { - 1 } ( B A ) B .
$$

So $A B$ is similar to $B A$ .

13. Because $A$ is similar to $B$ and $B$ is similar to $C$ there exist invertible matrices $S$ and $T$ with $A = S ^ { - 1 } B S$ and $B = T ^ { - 1 } C T$ Hence $A$ is similar to $C$ because

$$
A = S ^ { - 1 } B S = S ^ { - 1 } ( T ^ { - 1 } C T ) S = ( S ^ { - 1 } T ^ { - 1 } ) C ( T S ) = ( T S ) ^ { - 1 } C ( T S ) .
$$

14. Suppose that $A = P B P ^ { - 1 }$ .

(a) We have

$$
{ \begin{array} { r l } & { \operatorname* { d e t } ( A ) = \operatorname* { d e t } ( P B P ^ { - 1 } ) = \operatorname* { d e t } ( P ) \operatorname* { d e t } ( B ) \operatorname* { d e t } ( P ^ { - 1 } ) } \\ & { \qquad = \operatorname* { d e t } ( P ) \operatorname* { d e t } ( P ^ { - 1 } ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( P P ^ { - 1 } ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( I ) \operatorname* { d e t } ( B ) = \operatorname* { d e t } ( B ) . } \end{array} }
$$

(b) We have

$$
\begin{array} { l } { p ( A ) = \operatorname* { d e t } ( A - \lambda I ) = \operatorname* { d e t } ( P B P ^ { - 1 } - \lambda P \cdot I \cdot P ^ { - 1 } ) } \\ { \quad = \operatorname* { d e t } ( P ) \operatorname* { d e t } ( B - \lambda I ) \operatorname* { d e t } ( P ^ { - 1 } ) = \operatorname* { d e t } ( B - \lambda I ) = p ( B ) . } \end{array}
$$

(c) The characteristic polynomials of $A$ and $B$ agree, so $A$ and $B$ have the same eigenvalues. The matrix $A$ is singular if and only if $0$ is an eigenvalue of $A$ , which is true if and only if $0$ is an eigenvalue of $B$ . So $A$ is nonsingular if and ony if $B$ is nonsingular.

(d) We have

$$
A ^ { - 1 } = ( P B P ^ { - 1 } ) ^ { - 1 } = ( P ^ { - 1 } ) ^ { - 1 } B ^ { - 1 } P ^ { - 1 } = P B ^ { - 1 } P ^ { - 1 } .
$$

So $A ^ { - 1 }$ is similar to $B ^ { - 1 }$ .

(e) We have

$$
A ^ { t } = ( P B P ^ { - 1 } ) ^ { t } = ( P ^ { - 1 } ) ^ { t } B ^ { t } P ^ { t } = ( P ^ { t } ) ^ { - 1 } B ^ { t } P ^ { t } .
$$

Since $P$ is invertible if and only if $P ^ { t }$ is invertible, $A ^ { t }$ is similar to $B ^ { t }$ .

15. The matrix $A$ has an eigenvalue of multiplicity $1$ at $\lambda _ { 1 } = 3$ with eigenvector $\mathbf { s } _ { 1 } = ( 0 , 1 , 1 ) ^ { t }$ , and an eigenvalue of multiplicity 2 at $\lambda _ { 2 } = 2$ with linearly independent eigenvectors ${ \bf s } _ { 2 } = ( 1 , 1 , 0 ) ^ { t }$ and $\mathbf { s } _ { 3 } = ( - 2 , 0 , 1 ) ^ { t }$ . Let

$$
S _ { 1 } = \{ \mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \mathbf { s } _ { 3 } \} , \quad S _ { 2 } = \{ \mathbf { s } _ { 2 } , \mathbf { s } _ { 1 } , \mathbf { s } _ { 3 } \} , \quad \mathrm { a n d } \quad S _ { 3 } = \{ \mathbf { s } _ { 2 } , \mathbf { s } _ { 3 } , \mathbf { s } _ { 1 } \} .
$$

Then

$$
A = S _ { 1 } ^ { - 1 } D _ { 1 } S _ { 1 } = S _ { 2 } ^ { - 1 } D _ { 2 } S _ { 2 } = S _ { 3 } ^ { - 1 } D _ { 3 } S _ { 3 } ,
$$

so $A$ is similar to $D _ { 1 }$ , $D _ { 2 }$ , and $D _ { 3 }$ .

\*16. (i) Let the columns of $Q$ be denoted by the vectors ${ \bf q } _ { 1 } , { \bf q } _ { 2 } , \ldots , { \bf q } _ { n }$ , which are also the rows of $Q ^ { t }$ . Because $Q$ is orthogonal, $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { j }$ is zero when $i \neq j$ and $^ { 1 }$ when $i = j$ . But the $_ { i j }$ - entry of $Q ^ { t } Q$ is $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { j }$ for each $i$ and $j$ so $Q ^ { t } Q = I$ . Hence $Q ^ { t } = Q ^ { - 1 }$ .

(ii) From part (i) we have $Q ^ { t } Q = I$ , so

$$
( Q \mathbf { x } ) ^ { t } ( Q \mathbf { y } ) = ( \mathbf { x } ^ { t } Q ^ { t } ) ( Q \mathbf { y } ) = \mathbf { x } ^ { t } ( Q ^ { t } Q ) \mathbf { y } = \mathbf { x } ^ { t } ( I ) \mathbf { y } = \mathbf { x } ^ { t } \mathbf { y } .
$$

(iii) This follows from part (ii) with $\mathbf { x }$ replacing $\mathbf { y }$ , since then

$$
| | Q \mathbf { x } | | _ { 2 } ^ { 2 } = ( Q \mathbf { x } ) ^ { t } ( Q \mathbf { x } ) = \mathbf { x } ^ { t } \mathbf { x } = | | \mathbf { x } | | _ { 2 } ^ { 2 } .
$$

17. The matrix $A$ has an eigenvalue of multiplicity $^ { 1 }$ at $\lambda _ { 1 } = 3$ , and an eigenvalue of multiplicity 2 at $\lambda _ { 2 } = 2$ . However, $\lambda _ { 2 } = 2$ has only one linearly independent unit eigenvector, so by Theorem 9.13, $A$ is not similar to a diagonal matrix.

$^ { * } 1 8$ . Let the columns of $Q$ be denoted by the vectors ${ \bf q } _ { 1 } , { \bf q } _ { 2 } , \ldots , { \bf q } _ { n }$ , which are also the rows of $Q ^ { t } = Q ^ { - 1 }$ . Then $Q ^ { t } Q = I$ is equivalent to having $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { j } = 0$ when $i \neq j$ and $( { \bf q } _ { i } ) ^ { t } \cdot { \bf q } _ { i } = 1$ , for each $i = 1 , 2 , \ldots , n$ and $j = 1 , 2 , \dots , n$ . But this is precisely what is required for the columns of $Q$ to form an orthonormal set. Hence $Q$ is an orthogonal matrix.

19. The proof of Theorem 9.13 follows by considering the form the diagonal matrix must assume. The matrix $A$ is similar to a diagonal matrix $D$ if and only if an invertible matrix $S$ exists with $D = S ^ { - 1 } A S$ , which is equivalent to $A S = S D$ , with $S$ invertible. Suppose that we have $A S = S D$ with the columns of $S$ denoted $\mathbf { s } _ { 1 } , \mathbf { s } _ { 2 } , \ldots , \mathbf { s } _ { n }$ and the diagonal elements of $D$ denoted $d _ { 1 } , d _ { 2 } , \ldots , d _ { n }$ . Then $A \mathbf { s } _ { i } = d _ { i } \mathbf { s } _ { i }$ for each $i = 1 , 2 , \ldots , n$ . Hence each $d _ { i }$ is an eigenvalue of $A$ with corresponding eigenvector ${ \bf s } _ { i }$ . The matrix $S$ is invertible, and consequently $A$ is similar to $D$ , if and only if there are $n$ linearly independent eigenvectors that can be placed in the columns of $S$ .

# Exercise Set 9.3, page 590

1. The approximate eigenvalues and approximate eigenvectors are:

\*(a) $\mu ^ { ( 3 ) } = 3 . 6 6 6 6 6 7$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 7 7 2 7 2 7 , 0 . 9 3 1 8 1 8 2 , 1 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 2 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 1 , 0 . 5 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 5 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 2 5 7 8 9 4 7 , 1 , - 0 . 2 8 4 2 1 0 5 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 5 . 0 3 8 4 6 2$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 0 . 2 2 1 3 7 4 1 , 0 . 3 8 9 3 1 3 0 , 0 . 4 0 4 5 8 0 2 ) ^ { t }$

2. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 3 ) } = 6 . 0 5 0 8 4 7 5$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 0 . 5 7 1 4 2 8 5 7 , 0 . 7 7 5 9 1 0 3 6 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 5 . 5 2 6 3 1 5 8$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 1 7 1 1 7 1 1 7 , 0 . 4 5 9 4 5 9 4 6 , 1 , 0 . 9 4 5 9 4 6 0 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 7 . 5 3 1 0 7 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 6 8 8 6 7 2 2 , - 0 . 6 7 0 6 6 7 7 , - 0 . 9 2 1 9 8 0 5 , 1 ) ^ { i }$ t (d) $\mu ^ { ( 3 ) } = 4 . 1 0 6 0 6 1$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 1 2 5 4 6 1 3 , 0 . 0 8 4 8 7 0 8 5 , 0 . 0 0 9 2 2 5 0 9 , 1 ) ^ { t }$

3. The approximate eigenvalues and approximate eigenvectors are:

\*(a) $\mu ^ { ( 3 ) } = 1 . 0 2 7 7 3 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 1 8 8 9 0 8 2 , 1 , - 0 . 7 8 3 3 6 2 2 ) ^ { i }$ t (b) $\mu ^ { ( 3 ) } = - 0 . 4 1 6 6 6 6 7$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , - 0 . 7 5 , - 0 . 6 6 6 6 6 7 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 1 7 . 6 4 4 9 3$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 8 0 5 7 9 4 , - 0 . 0 9 0 7 9 1 3 2 , 1 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 1 . 3 7 8 6 8 4$ $\mathrm { 4 , ~ \ \mathbf { x } ^ { ( 3 ) } = ( - 0 . 3 6 9 0 2 7 7 , - 0 . 2 5 2 2 8 8 0 , 0 . 2 0 7 7 4 3 8 , 1 ) ^ { t } }$

4. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 3 ) } = 5 . 9 1 8 2 3 2 9$ , $\mathbf { x } ^ { ( 3 ) } = ( 1 , 0 . 5 5 2 6 3 3 6 4 , 0 . 8 1 2 9 6 5 6 1 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 2 . 6 4 5 8 4 3 6$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 6 0 8 4 6 0 4 0 , 1 , - 0 . 3 2 6 7 7 4 8 8 8 , 0 . 0 3 7 3 8 3 1 8 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 3 . 9 9 6 0 7 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 9 9 9 1 4 2 9 , 0 . 9 9 3 2 0 1 4 , 1 , 0 . 9 9 3 9 8 2 5 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 4 . 1 0 5 2 9 3$ $^ { 1 9 3 , } \quad \mathbf { x } ^ { ( 3 ) } = ( 0 . 0 6 2 8 1 4 1 9 , 0 . 0 8 7 0 4 0 8 9 , 0 . 0 1 8 2 5 2 1 3 , 1 ) ^ { t }$

5. The approximate eigenvalues and approximate eigenvectors are:

\*(a) $\mu ^ { ( 3 ) } = 3 . 9 5 9 5 3 8$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 8 1 6 1 2 4 , 0 . 5 5 4 5 6 0 6 , 0 . 5 9 5 1 3 8 3 ) ^ { i }$ t (b) $\mu ^ { ( 3 ) } = 2 . 0 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 6 6 6 6 6 6 7 , - 0 . 6 6 6 6 6 6 7 , - 0 . 3 3 3 3 3 3 ) ^ { t }$ (c) $\mu ^ { ( 3 ) } = 7 . 1 8 9 5 6 7$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 9 9 5 3 0 8 , 0 . 7 3 6 7 4 7 2 , 0 . 3 1 2 6 7 6 2 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 6 . 0 3 7 0 3 7$ $\mathbf { x } ^ { ( 3 ) } = ( 0 . 5 0 7 3 7 1 4 , 0 . 4 8 7 8 5 7 1 , - 0 . 6 6 3 4 8 5 7 , - 0 . 2 5 3 6 8 5 7 ) ^ { t }$

6. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 3 ) } = 3 . 8 4 8 4 1 6 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 2 9 8 4 1 3 1 9 , - 0 . 4 6 8 9 3 5 0 1 , 0 . 8 3 1 2 9 3 9 ) ^ { t }$ (b) $\mu ^ { ( 3 ) } = 4 . 6 9 0 5 6 6 0$ , $\mathbf { x } ^ { ( 3 ) } = ( - 0 . 9 5 5 5 7 2 6 6 , - 0 . 2 9 1 2 2 2 1 4 , 0 . 0 4 5 5 0 3 4 6 ) ^ { i }$ t (c) $\mu ^ { ( 3 ) } = 5 . 1 4 2 5 6 2$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 8 3 7 3 0 5 1 , 0 . 3 7 0 1 7 7 0 , 0 . 1 9 3 9 0 2 2 , 0 . 3 5 2 5 4 9 5 ) ^ { t }$ (d) ${ \bf \tau } ^ { ( 3 ) } = 8 . 5 9 3 1 4 2 , \quad { \bf x } ^ { ( 3 ) } = ( - 0 . 4 1 3 4 7 6 2 , 0 . 4 0 2 6 6 6 4 , 0 . 5 5 3 5 5 3 6 , - 0 . 6 0 0 3 9 6 2 ) ^ { t }$

7. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 9 ) } = 3 . 9 9 9 9 0 8 , \quad \mathbf { x } ^ { ( 9 ) } = ( 0 . 9 9 9 9 9 4 3 , 0 . 9 9 9 9 8 2 8 , 1 ) ^ { t }$ (b) $\mu ^ { ( 1 3 ) } = 2 . 4 1 4 2 1 4$ , $\mathbf { x } ^ { ( 1 3 ) } = ( 1 , 0 . 7 0 7 1 4 2 9 , 0 . 7 0 7 0 7 0 7 ) ^ { t }$ (c) $\mu ^ { ( 9 ) } = 5 . 1 2 4 7 4 9$ , $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 2 4 2 4 4 7 6 , 1 , - 0 . 3 1 9 9 7 3 3 ) ^ { t }$ (d) $\mu ^ { ( 2 4 ) } = 5 . 2 3 5 8 6 1$ , $\mathbf { x } ^ { ( 2 4 ) } = ( 1 , 0 . 6 1 7 8 3 6 1 , 0 . 1 1 8 1 6 6 7 , 0 . 4 9 9 9 2 2 0 ) ^ { t }$

8. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 1 2 ) } = 5 . 9 1 9 3 4 7 6$ , $\mathbf { x } ^ { ( 1 2 ) } = ( 1 , 0 . 5 5 4 7 8 8 4 5 , 0 . 8 0 9 9 5 8 1 6 ) ^ { t }$ (b) $\mu ^ { ( 1 4 ) } = 5 . 6 6 5 8 9 7 2$ , $\mathbf { x } ^ { ( 1 4 ) } = ( 0 . 0 5 5 2 0 4 4 4 , 0 . 2 5 7 4 9 7 2 8 , 1 , 0 . 8 8 8 6 1 7 2 6$ )t (c) $\mathbf { \boldsymbol { \tau } } ^ { \prime } ) = 8 . 9 9 9 6 6 7 , \quad \mathbf { \boldsymbol { x } } ^ { ( 1 7 ) } = ( 0 . 9 9 9 9 0 8 5 , - 0 . 9 9 9 9 0 7 8 , - 0 . 9 9 9 9 9 9 3 , 1 ) ^ { t }$ (d) The method did not converge in 25 iterations. However, $\lambda _ { 1 } \approx \mu ^ { ( 3 6 3 ) } = 4 . 1 0 5 3 0 9$ , $\mathrm { t h e n } \mathbf { x } ^ { ( 3 6 3 ) } = ( 0 . 0 6 2 8 6 2 9 9 , 0 . 0 8 7 0 2 7 5 4 , 0 . 0 1 8 2 4 6 8 0 , 1 ) ^ { t }$ and $\lambda _ { 2 } \approx \mu ^ { ( 1 5 ) } = - 4 . 0 2 4 3 0 8$

9. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 9 ) } = 1 . 0 0 0 0 1 5 2 3$ with $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 1 9 9 9 9 3 9 1 , 1 , - 0 . 7 9 9 9 9 0 8 7 ) ^ { t }$   
(b) $\mu ^ { ( 1 2 ) } = - 0 . 4 1 4 2 1 3 5 6$ with $\mathbf { x } ^ { ( 1 2 ) } = ( 1 , - 0 . 7 0 7 0 9 1 8 4 , - 0 . 7 0 7 1 2 1 7 2 0 ^ { t }$   
(c) The method did not converge in 25 iterations. However, convergence occurred with $\mu ^ { ( 4 2 ) } = 1 . 6 3 6 6 3 6 4 2$ with $\mathbf { x } ^ { ( 4 2 ) } = ( - 0 . 5 7 0 6 8 1 5 1 , 0 . 3 6 3 3 6 5 8 , 1 ) ^ { t }$   
(d) $\mu ^ { ( 9 ) } = 1 . 3 8 1 9 5 9 2 9$ with $\mathbf { x } ^ { ( 9 ) } = ( - 0 . 3 8 1 9 4 0 0 3 , - 0 . 2 3 6 1 0 0 6 8 , 0 . 2 3 6 0 1 9 0 9 , 1 ) ^ { t }$

10. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 7 ) } = 5 . 9 1 9 6 6 8 8$ , $\mathbf { x } ^ { ( 7 ) } = ( 1 , 0 . 5 5 4 8 4 7 7 6 , 0 . 8 0 9 9 7 3 3 0 ) ^ { t }$ (b) $\mu ^ { ( 6 ) } = 2 . 6 4 5 9 3 1 2$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 6 0 7 5 6 1 9 1 , 1 , - 0 . 3 2 5 0 6 9 3 0 , 0 . 0 3 8 3 6 9 2 6 ) ^ { t }$ (c) $\mu ^ { ( 6 ) } = 3 . 9 9 9 9 9 7$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 9 9 9 9 9 3 9 , 0 . 9 9 9 9 9 9 9 , 0 . 9 9 9 9 9 4 0 , 1 ) ^ { t }$ (d) $\mu ^ { ( 3 ) } = 4 . 1 0 5 2 9 3$ , $\mathbf { x } ^ { ( 3 ) } = ( 0 . 0 6 2 8 1 4 1 9 , 0 . 0 8 7 0 4 0 8 9 , 0 . 0 1 8 2 5 2 1 3 , 1 ) ^ { t }$

11. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 8 ) } = 4 . 0 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 8 ) } = ( 0 . 5 7 7 3 5 4 7 , 0 . 5 7 7 3 2 8 2 , 0 . 5 7 7 3 6 7 9 ) ^ { t }$ (b) $\mu ^ { ( 1 3 ) } = 2 . 4 1 4 2 1 4$ , $\mathbf { x } ^ { ( 1 3 ) } = ( - 0 . 7 0 7 1 0 6 8 , - 0 . 5 0 0 0 2 5 5 , - 0 . 4 9 9 9 7 4 5 ) ^ { t }$ (c) $\mu ^ { ( 1 6 ) } = 7 . 2 2 3 6 6 3$ , $\mathbf { x } ^ { ( 1 6 ) } = ( 0 . 6 2 4 7 8 4 5 , 0 . 7 2 0 4 2 7 1 , 0 . 3 0 1 0 4 6 6 ) ^ { t }$ (d) $\mu ^ { ( 2 0 ) } = 7 . 0 8 6 1 3 0$ $8 6 1 3 0 , \quad \mathbf { x } ^ { ( 2 0 ) } = ( 0 . 3 3 2 5 9 9 9 , 0 . 2 6 7 1 8 6 2 , - 0 . 7 5 9 0 1 0 8 , - 0 . 4 9 1 8 2 4 6 ) ^ { t }$

12. The approximate eigenvalues and approximate eigenvectors are:

(a) The method did not converge in 25 iterations. Dominant eigenvalues are $\sqrt { 1 5 }$ and $- { \sqrt { 1 5 } }$ . (b) $\mu ^ { ( 1 6 ) } = 4 . 8 3 4 7 7 8 0$ , $\mathbf { x } ^ { ( 1 6 ) } = ( - 0 . 9 2 9 0 4 8 7 0 , - 0 . 3 6 7 7 8 3 6 1 , 0 . 0 4 0 0 4 6 6 2 ) ^ { t }$ (c) $\mu ^ { ( 2 1 ) } = 5 . 2 3 6 0 6 8$ , $\mathbf { x } ^ { ( 2 1 ) } = ( 0 . 7 7 9 5 5 3 9 , 0 . 4 8 1 5 9 9 6 , 0 . 0 9 2 1 4 2 1 4 , 0 . 3 8 9 7 0 1 6 )$ )t (d) $\mu ^ { ( 1 6 ) } = 9 . 0 0 0 0 0 0 0 , \quad \mathbf { x } ^ { ( 1 6 ) } = ( - 0 . 4 9 9 9 5 9 2 , 0 . 4 9 9 9 5 8 4 , 0 . 5 0 0 0 4 0 8 , - 0 . 5 0 0 0 4 1 6 ) ^ { \mathrm { t } }$

13. The approximate eigenvalues and approximate eigenvectors are:

(a) $\lambda _ { 2 } { \approx } \mu ^ { ( 1 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 1 ) } = ( - 2 . 9 9 9 9 0 8 , 2 . 9 9 9 9 0 8 , 0 ) ^ { t }$ (b) $\lambda _ { 2 } { \approx } \mu ^ { ( 1 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 1 ) } = ( 0 , - 1 . 4 1 4 2 1 4 , 1 . 4 1 4 2 1 4 ) ^ { t }$ (c) $\lambda _ { 2 } { \approx } \mu ^ { ( 6 ) } = 1 . 6 3 6 7 3 4$ , $\mathbf { x } ^ { ( 6 ) } = ( 1 . 7 8 3 2 1 8 , - 1 . 1 3 5 3 5 0 , - 3 . 1 2 4 7 3 3 ) ^ { t }$ t

$$
\lambda _ { 2 } \approx \mu ^ { ( 1 0 ) } = 3 . 6 1 8 1 7 7 , \quad \mathbf { x } ^ { ( 1 0 ) } = ( 0 . 7 2 3 6 3 9 0 , - 1 . 1 7 0 5 7 3 , 1 . 1 7 0 6 7 5 , - 0 . 2 7 6 3 3 7 4 ) ^ { t }
$$

14. The approximate eigenvalues and approximate eigenvectors are:

(a) The method did not converge in 25 iterations. The remaining eigenvalues are complex numbers.   
(b) $\mu ^ { ( 9 ) } = 2 . 6 4 5 9 0 9 5 , \quad \mathbf { x } ^ { ( 9 ) } = ( - 1 . 6 9 3 0 9 5 3 , - 2 . 7 8 6 7 3 8 3 , 0 . 9 0 5 8 2 5 3 3 , - 0 . 1 0 6 9 2 8 4 2 ) ^ { t }$   
(c) $\lambda _ { 2 } \approx \mu ^ { ( 2 1 ) } = 5 . 0 0 0 0 5 1 , \quad \mathbf { x } ^ { ( 2 1 ) } = ( 1 . 9 9 9 3 3 8 , - 1 . 9 9 9 6 0 3 , 1 . 9 9 9 6 0 3 , - 2 . 0 0 0 1 9 8 ) ^ { t }$   
(d) $\mathbf { x } ^ { ( 1 5 ) } = ( - 8 . 1 5 1 9 6 5 , 2 . 1 0 0 6 9 9 , 0 . 7 5 1 9 0 8 0 , - 0 . 3 5 5 4 9 4 1 ) ^ { t }$ .

15. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 8 ) } = 4 . 0 0 0 0 0 1 , \quad \mathbf { x } ^ { ( 8 ) } = ( 0 . 9 9 9 9 7 7 3 , 0 . 9 9 9 9 3 1 3 4 , 1 ) ^ { t }$ (b) The method fails because of division by zero. (c) $\mu ^ { ( 7 ) } = 5 . 1 2 4 8 9 0$ , $\mathbf { x } ^ { ( 7 ) } = ( - 0 . 2 4 2 5 9 3 8 , 1 , - 0 . 3 1 9 6 3 5 1 ) ^ { t }$ (d) $\mu ^ { ( 1 5 ) } = 5 . 2 3 6 1 1 2 , \quad \mathbf { x } ^ { ( 1 5 ) } = ( 1 , 0 . 6 1 2 5 3 6 9 , 0 . 1 2 1 7 2 1 6 , 0 . 4 9 7 8 3 1 8 ) ^ { t }$

16. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 9 ) } = 5 . 9 1 9 7 1 4 1 0$ , $\mathbf { x } ^ { ( 9 ) } = ( 1 , 0 . 5 5 4 7 8 8 4 5 , 0 . 8 0 9 9 5 8 1 6 ) ^ { t }$ (b) $\mathbf { \xi } = 5 . 6 6 5 8 1 2 1 1 , \quad \mathbf { x } ^ { ( 1 1 ) } = ( 0 . 0 5 5 2 0 4 4 , 0 . 2 5 7 4 9 9 2 8 , 1 , 0 . 8 8 8 6 1 7 2 8 )$ t (c) $\mu ^ { ( 1 0 ) } = 8 . 9 9 9 8 9 0$ , $\mathbf { x } ^ { ( 1 0 ) } = ( 0 . 9 9 4 4 1 3 7 , - 0 . 9 9 4 2 1 4 8 , - 0 . 9 9 9 7 9 9 1 , 1$ )t (d) $\mu ^ { ( 1 1 ) } = 4 . 1 0 5 3 1 7 , \quad \mathbf { x } ^ { ( 1 1 ) } = ( 0 . 1 1 7 1 6 5 4 0 , 0 . 0 7 2 8 5 3 9 9 5 , 0 . 0 1 3 1 6 6 5 5 , 1 ) ^ { t }$

17. The approximate eigenvalues and approximate eigenvectors are:

(a) $\mu ^ { ( 2 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 2 ) } = ( 0 . 1 5 4 2 3 7 3 , - 0 . 7 7 1 5 8 2 8 , 0 . 6 1 7 1 4 7 4 ) ^ { t }$ (b) $\mu ^ { ( 1 3 ) } = 1 . 0 0 0 0 0 0$ , $\mathbf { x } ^ { ( 1 3 ) } = ( 0 . 0 0 0 0 7 4 3 2 , - 0 . 7 0 7 0 7 2 3 , 0 . 7 0 7 1 4 1 3 ) ^ { t }$ (c) $\mu ^ { ( 1 4 ) } = 4 . 9 6 1 6 9 9$ , $\mathbf { x } ^ { ( 1 4 ) } = ( - 0 . 4 8 1 4 4 7 2 , 0 . 0 5 1 8 0 4 7 3 , 0 . 8 7 4 9 4 2 8 ) ^ { t }$ (d) $\mu ^ { ( 1 7 ) } = 4 . 4 2 8 0 0 7 $ , $\mathbf { x } ^ { ( 1 7 ) } = ( 0 . 7 1 9 4 2 3 0 , 0 . 4 2 3 1 9 0 8 , 0 . 1 1 5 3 5 8 9 , 0 . 5 3 8 5 4 6 6 ) ^ { t }$

18. The Power method was applied to the matrices in Exercise 1 using $\mathbf { x } ^ { ( 0 ) }$ as given with $T O L =$ $1 0 ^ { - 4 }$ . The following table summarizes the results. (Note: The results are very sensitive to roundoff error.)

<table><tr><td></td><td>入1</td><td>Number of iterations</td><td>入2</td><td>Eigenvector</td></tr><tr><td>(1a)</td><td>3.999908</td><td>2</td><td>1.000037</td><td>(-0.1999411,1, -0.799911)t</td></tr><tr><td>(16)</td><td>2.414213562</td><td>15</td><td>1.000003</td><td>(0.00004881, -0.9999485,1)t</td></tr><tr><td>(1c)</td><td>5.12488541</td><td>5</td><td>1.636636</td><td>(-0.5706569,0.3633325,1)t</td></tr><tr><td>(1d</td><td>5.23606796</td><td>13</td><td>3.617997</td><td>(-0.6180177,1, -0.9999990,0.2360394)t</td></tr></table>

19. (a) We have $| \lambda | \le 6$ for all eigenvalues $\lambda$ . (b) The approximate eigenvalue is $\mu ^ { ( 1 3 3 ) } = 0 . 6 9 7 6 6 8 5 4$ , with the approximate eigenvector $\mathbf { x } ^ { ( 1 3 3 ) } = ( 1 , 0 . 7 1 6 6 7 2 7 , 0 . 2 5 6 8 0 9 9 , 0 . 0 4 6 0 1 2 1 7 ) ^ { i }$ . (c) The characteristic polynomial is

$$
P ( \lambda ) = \lambda ^ { 4 } - \frac { 1 } { 4 } \lambda - \frac { 1 } { 1 6 } ,
$$

and the eigenvalues are

λ1 = 0.6976684972, λ2 = 0.2301775942+0.56965884i, $\begin{array} { r } { , \quad \lambda _ { 3 } = - 0 . 2 3 0 1 7 7 5 9 4 2 - 0 . 5 6 9 6 5 8 8 4 i } \end{array}$ ,

and

$$
\lambda _ { 4 } = - 0 . 2 3 7 3 1 3 3 0 8 .
$$

(d) The beetle population should approach zero since $A$ is convergent.

$^ *$ 20. Since

$$
\mathbf { x } ^ { t } = \frac { 1 } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } ( a _ { i 1 } , a _ { i 2 } , \ldots , a _ { i n } ) ,
$$

the $i$ th row of $B$ is

$$
\left( a _ { i 1 } , a _ { i 2 } , \dots , a _ { i n } \right) - \frac { \lambda _ { 1 } } { \lambda _ { 1 } v _ { i } ^ { ( 1 ) } } \left( v _ { i } ^ { ( 1 ) } a _ { i 1 } , v _ { i } ^ { ( 1 ) } a _ { i 2 } , \dots , v _ { i } ^ { ( 1 ) } a _ { i n } \right) = \mathbf { 0 } .
$$

21. Using the Inverse Power method with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 1 ) ^ { t }$ and $q = 0$ gives the following results:

(a) $\mu ^ { ( 4 9 ) } = 1 . 0 2 0 1 9 2 6$ , so $\rho ( A ^ { - 1 } ) \approx 1 / \mu ^ { ( 4 9 ) } = 0 . 9 8 0 2 0 7 1$ (b) $\mu ^ { ( 3 0 ) } = 1 . 0 4 0 4 5 6 8$ , so $\rho ( A ^ { - 1 } ) \approx 1 / \mu ^ { ( 3 0 ) } = 0 . 9 6 1 1 1 6 3$ (c) $\mu ^ { ( 2 2 ) } = 1 . 0 6 0 6 9 7 4$ , so $\rho ( A ^ { - 1 } ) \approx 1 / \mu ^ { ( 2 2 ) } = 0 . 9 4 2 7 7 6 0$ The method appears to be stable for all $\alpha$ in $[ \frac { 1 } { 4 } , \frac { 3 } { 4 } ]$ .

22. (a) $\rho \left( A ^ { - 1 } \right) = 0 . 9 8 0 1 4 8 5$ (b) $\rho \left( A ^ { - 1 } \right) = 0 . 9 6 1 0 6 9 9$ (c) $\rho \left( A ^ { - 1 } \right) = 0 . 9 4 2 7 1 9 8$ The method appears to be stable for $\alpha > 0$ .

23. Forming $A ^ { - 1 } B$ and using the Power method with $\mathbf { x } ^ { ( 0 ) } = ( 1 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 1 ) ^ { t }$ gives the following results:

(a) The spectral radius is approximately $\mu ^ { ( 4 6 ) } = 0 . 9 8 0 0 0 2 1$ .   
(b) The spectral radius is approximately $\mu ^ { ( 2 5 ) } = 0 . 9 6 0 3 5 4 3$ .   
(c) The spectral radius is approximately $\mu ^ { ( 1 8 ) } = 0 . 9 4 1 0 7 5 4$ .

24. (a) $\lambda _ { 1 } = - 6$ , $\lambda _ { 2 } = - 5$ , $\lambda _ { 3 } = - 2$ , the system is stable. (b) $\lambda _ { 1 } = - 2$ , $\lambda _ { 2 } = - 1 . 1 0 6 7 7 1 1$ , $\lambda _ { 3 } = - 3 . 9 4 6 6 4 + 0 . 8 2 9 7 0 i$ , $\lambda _ { 4 } = - 3 . 9 4 6 6 4 - 0 . 8 2 9 7 0 i$ , the system is stable.

# Exercise Set 9.4, page 600

1. Householder’s method produces the following tridiagonal matrices.

12.00000 10.77033 0.0   
\*(a) 10.77033 3.862069 5.344828 0.0 5.344828 7.137931 2.0000000 1.414214 0.0   
(b) 1.414214 1.000000 0.0 0.0 0.0 3.0 1.0000000 1.414214 0.0   
(c) 1.414214 1.000000 0.0 0.0 0.0 1.000000 4.750000 2.263846 0.0   
(d) 2.263846 4.475610 1.219512 0.0 1.219512 5.024390

2. Householder’s method produces the following tridiagonal matrices.

3. Householder’s method produces the following tridiagonal matrices.

2.0000000 2.8284271 1.4142136 (a) 2.8284271 1.0000000 2.0000000 0.0000000 2.0000000 3.0000000

−1.0000000 3.0655513 0.0000000   
(b) 3.6055513 0.23076923 3.1538462 0.0000000 0.15384615 2.2307692 5.0000000 4.9497475 1.4320780 1.5649769 1.4142136 2.0000000 2.4855515 1.8226448   
(c) 0.0000000 5.4313902 1.4237288 2.6486542 0.0000000 0.0000000 1.5939865 5.4237288 4.0000000 1.7320508 0.0000000 0.0000000 1.7320508 2.3333333 0.23570226 0.40824829   
(d) 0.0000000 0.47140452 4.6666667 0.57735027 0.0000000 0.0000000 0.0000000 5.0000000

# Exercise Set 9.5, page 611

1. Two iterations of the QR Algorithm without shifting produce the following matrices.

3.142857 0.559397 0.0   
(a) A(3) 0.559397 2.248447 0.187848 0.0 0.187848 0.608696 4.549020 1.206958 0.0   
(b) A(3) 1.206958 3.519688 0.000725 0.0 0.000725 −0.068708 4.592920 0.472934 0.0   
(c) A(3) 0.472934 3.108760 0.232083 0.0 0.232083 1.298319 3.071429 0.855352 0.0 0.0   
(d) A(3) = 0.855352 3.314192 1.161046 0.0 0.0 1.1610446 3.331770 0.268898 0.0 0.0 0.268898 0.282609  3.607843 0.612882 0.0 0.0   
(e) A(3) 0.612882 1.395227 1.111027 0.0 0.0 1.111027 3.133919 0.346353 0.0 0.0 0.346353 0.869151 1.013260 0.279065 0.0 0.0   
(f) A(3) 0.279065 0.696255 0.107448 0.0 0.0 0.107448 0.843061 0.310832 0.0 0.0 0.310832 0.317424

2. Two iterations of the QR Algorithm without shifting produce the following matrices.

$$
{ \begin{array} { r l } { A ^ { ( 3 ) } = { \Biggl [ \begin{array} { l l l } { 2 . 6 3 3 3 3 3 3 3 } & { - 1 . 1 6 8 5 6 9 8 8 } & { 0 } \\ { - 1 . 1 6 8 5 6 9 8 8 } & { 0 . 9 3 7 8 6 2 7 6 } & { - 2 . 5 7 5 9 4 4 9 8 { \Biggr ] } } \\ { 0 } & { - 2 . 5 7 5 9 4 4 9 8 } & { 0 . 4 2 8 8 0 3 9 1 } \end{array} } } \\ { A ^ { ( 3 ) } = { \Biggl [ \begin{array} { l l l } { 4 . 6 0 1 3 0 7 1 9 } & { 1 . 3 8 5 4 5 1 3 4 } & { 0 } \\ { 1 . 3 8 5 4 5 1 3 4 } & { 4 . 1 6 5 3 2 3 1 3 } & { 0 . 2 4 2 8 0 0 1 1 } \\ { 0 } & { 0 . 2 4 2 8 0 0 1 1 } & { 1 . 2 3 3 3 6 9 6 8 { \Biggr ] } } \end{array} } } \end{array} }
$$

<table><tr><td rowspan="7">A(3）</td><td>6.28571429</td><td>1.16057692</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1.16057692</td><td>5.26984127</td><td>1.49897084</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1.49897084</td><td>4.80808081</td><td>1.50776756</td><td>0</td></tr><tr><td>0</td><td>0</td><td>1.50776756</td><td>3.07260525</td><td>0.23213209</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0.23213209</td><td>0.56375839</td></tr><tr><td>5.58655992</td><td>-0.60565234</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-0.60565234</td><td>3.92585374</td><td>0.02385124</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0.02385124</td><td>3.03035281</td><td>-1.22483017</td><td>0</td></tr><tr><td>0</td><td>0</td><td>-1.22483017</td><td>2.29033145</td><td>0.73675527</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0.73675527</td><td>1.66690207</td></tr></table>

3. The matrices in Exercise 1 have the following eigenvalues, accurate to within $1 0 ^ { - 5 }$ .

\*(a) 3.414214, 2.000000, 0.58578644  
(b) −0.06870782, 5.346462, 2.722246  
(c) 1.267949, 4.732051, 3.000000  
(d) 4.745281, 3.177283, 1.822717, 0.2547188  
(e) 3.438803, 0.8275517, −1.488068, −3.778287  
(f) 0.9948440, 1.189091, 0.5238224, 0.1922421

4. The matrices have the following eigenvalues, accurate to within $1 0 ^ { - 5 }$ .

(a) 3.9115033, 2.1294613, −2.0409646 (b) 1.2087122, 5.7912878, 3.0000000 (c) $\mathrm { 5 . 0 0 0 0 0 0 0 0 , 2 . 0 0 0 0 0 0 0 0 , 4 . 0 0 0 0 0 0 0 0 , 7 . 4 6 4 1 0 1 6 , 0 . 5 3 5 8 9 8 4 }$ (d) 4.0274350, 2.0707128, 3.7275564, 5.7839956, 0.8903002

5. The matrices in Exercise 1 have the following eigenvectors, accurate to within $1 0 ^ { - 5 }$ .

(a) $( - 0 . 7 0 7 1 0 6 7 , 1 , - 0 . 7 0 7 1 0 6 7 ) ^ { t }$ , $( 1 , 0 , - 1 ) ^ { t }$ , $( 0 . 7 0 7 1 0 6 8 , 1 , 0 . 7 0 7 1 0 6 8 ) ^ { t }$   
(b) $( 0 . 1 7 4 1 2 9 9 , - 0 . 5 3 4 3 5 3 9 , 1 ) ^ { t }$ , $( 0 . 4 2 6 1 7 3 5 , 1 , 0 . 4 6 0 1 4 4 3 ) ^ { t }$ , $( 1 , - 0 . 2 7 7 7 5 4 4 , - 0 . 3 2 2 5 4 9 1 ) ^ { \iota }$   
(c) $( 0 . 2 6 7 9 4 9 2 , 0 . 7 3 2 0 5 0 8 , 1 ) ^ { t }$ , $( 1 , - 0 . 7 3 2 0 5 0 8 , 0 . 2 6 7 9 4 9 2 ) ^ { t }$ , $( 1 , 1 , - 1 ) ^ { t }$   
(d) $( - 0 . 0 8 0 2 9 4 4 7 , - 0 . 3 0 0 7 2 5 4 , 0 . 7 4 5 2 8 1 2 , 1 ) ^ { u }$ , $( 0 . 4 5 9 2 8 8 0 , 1 , - 0 . 7 1 7 9 9 4 9 , 0 . 8 7 2 7 1 1 8 ) ^ { \iota }$ , ( $0 . 8 7 2 7 1 1 8 , 0 . 7 1 7 9 9 4 9 , 1 , - 0 . 4 5 9 2 8 8 0 ) ^ { t } \ ($ $( 1 , - 0 . 7 4 5 2 8 1 2 , - 0 . 3 0 0 7 2 5 4 , 0 . 0 8 0 2 9 4 4 7 ) ^ { v }$   
(e) $( - 0 . 0 1 2 8 9 8 6 1 , - 0 . 0 7 0 1 5 2 9 9 , 0 . 4 3 8 8 0 2 6 , 1 ) ^ { \tau }$ , $( - 0 . 1 0 1 8 0 6 0 , - 0 . 2 8 7 8 6 1 8 , 1 , - 0 . 4 6 0 3 1 0 2 ) ^ { u }$ , $( 1 , 0 . 5 1 1 9 3 2 2 , 0 . 2 2 5 9 9 3 2 , - 0 . 0 5 0 3 5 4 2 3 ) ^ { v }$ $( - 0 . 5 6 2 3 3 9 1 , 1 , 0 . 2 1 5 9 4 7 4 , - 0 . 0 3 1 8 5 8 7 1 ) ^ { \tau }$   
(f) $( - 0 . 1 5 2 0 1 5 0 , - 0 . 3 0 0 8 9 5 0 , - 0 . 0 5 1 5 5 9 5 6 , 1 ) ^ { u }$ , $( 0 . 3 6 2 7 9 6 6 , 1 , 0 . 7 4 5 9 8 0 7 , 0 . 3 9 4 5 0 8 1 ) ^ { u }$ , $( 1 , 0 . 0 9 5 2 8 9 6 2 , - 0 . 6 9 0 7 9 2 1 , 0 . 1 4 5 0 7 0 3 ) ^ { t } , ( 0 . 8 0 2 9 4 0 3 , - 0 . 9 8 8 4 4 4 8 , 1 , - 0 . 1 2 3 7 9 9 5 ) ^ { t }$

6. (a) The inverse power method using $\mathbf { x } ^ { ( 0 ) } \ = \ ( 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

$\lambda _ { 1 } = 3 . 9 1 1 5 0 3 3 1$ , $\mathbf { x } ^ { ( 9 ) } = ( 0 . 3 4 1 3 2 5 4 6 , - 0 . 5 1 8 1 9 8 9 1 , 1 ) ^ { t }$ $\lambda _ { 2 } = 2 . 1 2 9 4 6 1 2 8$ , $\mathbf { x } ^ { ( 5 ) } = ( 1 , - 0 . 1 7 8 1 9 4 1 4 , - 0 . 2 1 6 8 3 2 1 9 ) ^ { t }$ $\lambda _ { 3 } = - 2 . 0 4 0 9 6 4 5 9$ , $\mathbf { x } ^ { ( 6 ) } = ( 0 . 2 7 0 5 3 4 1 1 , 1 , 0 . 2 1 2 9 2 9 4 0 ) ^ { t }$ (b) The inverse power method using $\mathbf { x } ^ { ( 0 ) } \ = \ ( 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

(c) The inverse power method using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

(d) The inverse power method using $\mathbf { x } ^ { ( 0 ) } = ( 1 , 1 , 1 , 1 ) ^ { t }$ gives the following eigenvalues and eigenvectors.

$\lambda _ { 1 } = 4 . 0 2 7 4 3 4 9 6$ , $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 5 0 0 9 0 0 8 , - 0 . 4 8 7 1 5 8 6 , - 0 . 1 3 5 3 4 3 3 4 , 1 , 0 . 9 7 3 2 9 7 6 2 ) ^ { t }$ $\lambda _ { 2 } = 2 . 0 7 0 7 1 2 8$ , $\mathfrak { c } ^ { ( z ) } = ( - 0 . 0 1 1 1 5 3 0 0 , - 0 . 0 3 2 6 7 0 3 5 , 0 . 3 4 1 0 6 3 2 7 , - 0 . 9 2 9 2 8 7 2 0 , 1 )$ )t $\lambda _ { 3 } = 3 . 7 2 7 5 5 6 4 2$ , $\mathbf { x } ^ { ( 2 ) } = ( 0 . 7 8 5 8 8 9 4 6 , 1 , 0 . 0 6 7 2 2 9 4 4 , 0 . 0 4 1 5 6 9 7 5 , 0 . 0 5 7 1 3 6 1 1 ) ^ { t }$ $\lambda _ { 4 } = 5 . 7 8 3 9 9 5 5 7$ , x $\mathbf { \dot { \hat { \rho } } ^ { ( 2 ) } } = ( 1 , - 0 . 7 8 3 9 9 5 5 7 , - 0 . 0 3 3 2 3 4 1 6 , 0 . 0 0 5 4 8 2 3$ 8, 0.00196925)t $\lambda _ { 5 } = 0 . 8 9 0 3 0 0 2 5$ , $\mathbf { x } ^ { ( 2 ) } = ( - 0 . 0 1 4 4 5 6 3 2 , - 0 . 0 5 9 4 1 1 1 2 , 1 , 0 . 2 4 4 5 4 5$ 382, 0.11591404)t \*7. (a) First note that for any vector $\mathbf { x } = ( x _ { 1 } , x _ { 2 } ) ^ { t }$ we have

and that

$$
\begin{array} { r l } & { v _ { 1 } \cos \theta - x _ { 2 } \sin \theta ) ^ { 2 } + ( x _ { 1 } \sin \theta + x _ { 2 } \cos \theta ) ^ { 2 } = x _ { 1 } ^ { 2 } ( ( \cos \theta ) ^ { 2 } + ( \sin \theta ) ^ { 2 } ) + x _ { 2 } ^ { 2 } ( ( - \sin \theta ) ^ { 2 } + ( \cos \theta ) ^ { 2 } ) } \\ & { \qquad = x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } . } \end{array}
$$

So the $l _ { 2 }$ norms are the same.

Now let ${ \bf z } = ( z _ { 1 } , z _ { 2 } ) ^ { t }$ represent the vector that has the same magnitude as $\mathbf { x }$ but has been rotated by the angle $\theta$ . Let $\phi$ be the angle from the $x$ -axis to the point $( x _ { 1 } , x _ { 2 } )$ and let $r = \sqrt { x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } } = | | \mathbf { x } | | _ { 2 }$ . Then

$$
x _ { 1 } = r \cos \phi \quad { \mathrm { a n d } } \quad x _ { 2 } = r \sin \phi .
$$

In a similar manner,

$$
\begin{array} { r } { z _ { 1 } = r \cos ( \phi + \theta ) = r \cos \phi \cos \theta - r \sin \phi \sin \theta = x _ { 1 } \cos \theta - x _ { 2 } \sin \theta } \\ { z _ { 2 } = r \sin ( \phi + \theta ) = r \cos \phi \sin \theta + r \sin \phi \cos \theta = x _ { 1 } \sin \theta + x _ { 2 } \cos \theta } \end{array}
$$

So the unique vector $\mathbf { z }$ that has the same $l _ { 2 }$ norm as $\mathbf { x }$ and is rotated by an angle of $\theta$ is given by multiplying $\mathbf { x }$ by the rotation matrix.

(b) Consider the the vector $\mathbf { x } = ( 1 , 1 ) ^ { t }$ , which has ${ \mathit { l } } _ { \infty }$ norm 1. If $\theta = \pi / 4$ , then

$$
\left[ { \begin{array} { r r } { \cos \theta } & { - \sin \theta } \\ { \sin \theta } & { \cos \theta } \end{array} } \right] \left[ { \begin{array} { r } { 1 } \\ { 1 } \end{array} } \right] = \left[ { \begin{array} { r r } { { \frac { \sqrt { 2 } } { 2 } } } & { - { \frac { \sqrt { 2 } } { 2 } } } \\ { { \frac { \sqrt { 2 } } { 2 } } } & { { \frac { \sqrt { 2 } } { 2 } } } \end{array} } \right] \left[ { \begin{array} { r } { 1 } \\ { 1 } \end{array} } \right] = \left[ { \begin{array} { r } { 0 } \\ { \sqrt { 2 } } \end{array} } \right] ,
$$

which has ${ \mathit { l } } _ { \infty }$ norm $\sqrt { 2 }$ .

$^ { * } 8$ . Let $P = ( p _ { i j } )$ be a rotation matrix with nonzero entries $p _ { j j } = p _ { i i } = \cos \theta$ , $p _ { i j } = - p _ { j i } = \sin { \theta }$ , and $p _ { k k } = 1$ , if $k \neq i$ and $k \neq j$ . For any $n \times n$ matrix $A$ ,

$$
( A P ) _ { r s } = \sum _ { k = 1 } ^ { n } a _ { r k } p _ { k s } .
$$

If $s \neq i , j$ , then $p _ { k s } = 0$ unless $k = s$ . Thus, $( A P ) _ { r s } = a _ { r s }$ . If $s = j$ , then

$$
( A P ) _ { r j } = a _ { r j } p _ { j j } + a _ { r i } p _ { i j } = a _ { r j } \cos \theta + a _ { r i } \sin \theta .
$$

If $s = i$ , then

$$
( A P ) _ { r i } = a _ { r j } p _ { j i } + a _ { r i } p _ { i i } = - a _ { r j } \sin \theta + a _ { r i } \cos { \theta }
$$

Similarly, $\textstyle ( P A ) _ { r s } = \sum _ { k = 1 } ^ { n } p _ { r k } a _ { k s }$ . If $r \neq i , j$ , then $p _ { r k } = 0$ unless $r = k$ . Thus, $( P A ) _ { r s } = a _ { r s }$ If $r = i$ , then

$$
P A ) _ { i s } = p _ { i j } a _ { j s } + p _ { i i } a _ { i s } = a _ { j s } \sin \theta + a _ { i s } \cos \theta .
$$

If $r = j$ , then

$$
( P A ) _ { j s } = p _ { j j } a _ { j s } + p _ { j i } a _ { i s } = a _ { j s } \cos \theta - a _ { i s } \sin \theta .
$$

9. Let is upper triangular and is upper Hessenberg. Then n Sinc $C = R Q$ , where n upper $R$ iangular matrix, $Q$ f . Thus $\begin{array} { r } { c _ { i j } = \sum _ { k = 1 } ^ { n } r _ { i k } q _ { k j } } \end{array}$ uif $R$ enberg m. Hence, $q _ { k j } = 0$ $k > j + 1$ $r _ { i k } = 0$ . Thus,  means $k < i$ $\begin{array} { r } { c _ { i j } = \sum _ { k = i } ^ { j + 1 } r _ { i k } q _ { k j } } \end{array}$ $\begin{array} { r } { c _ { i j } = \sum _ { k = i } ^ { n } r _ { i k } q _ { k j } } \end{array}$ =i . The sum will be zeror Hessenberg matrix. $i > j + 1$ $c _ { i j } = 0$ $i \geq j + 2$ $C$

10. (a) We have

$$
\begin{array} { c c } { { { \cal P } _ { 2 } ^ { e } { \cal P } _ { 3 } ^ { e } = } } & { { { \bf \pi } ^ { \nu } \cdot { \bf \Lambda } ^ { 0 } } } & { { { \bf 0 } } } \\ { { { \cal P } _ { 2 } ^ { e } { \cal P } _ { 3 } ^ { e } = } } & { { { \bf \pi } ^ { \nu } \cdot { \bf \Lambda } ^ { 0 } } } & { { { \bf 0 } } } & { { \cdots \ { \bf 0 } ^ { \nu } } } \\ { { { \bf 0 } } } & { { { \bf 0 } } } & { { { \bf 1 } } } & { { { \bf 0 } } } & { { \cdots \ { \bf 0 } ^ { \nu } } } \\ { { \vdots \ \quad \quad \vdots \quad } } & { { \vdots \ \ddots \ } } & { { \ddots \ \ddots } } & { { \vdots \ } } \\ { { \vdots \quad \quad \vdots \quad } } & { { \ddots \quad } } & { { \ddots \quad \ddots } } & { { { \bf \Lambda } _ { 0 } } } \\ { { { \bf 0 } } } & { { { \bf 0 } } } & { { \cdots \ } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf 0 } } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { e } { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { \cdots \ { \bf \Lambda } ^ { 0 } } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 1 } } } & { { \ddots \quad \ddots } } \\ { { \vdots \quad \quad } } & { { \vdots \quad \vdots \quad } } & { { \ddots \quad \ddots } } & { { \vdots \ } } \\ { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } & { { { \bf \Lambda } ^ { 0 } } } \end{array}
$$

(b) Let $Q _ { k } \ = \ P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k } ^ { t }$ be an upper triangular matrix except for the entries $( Q _ { k } ) _ { 2 , 1 }$ , matrix $( Q _ { k } ) _ { 3 , 2 }$ , . . . , $( P _ { k + 1 } ) ^ { t }$ $( Q _ { k } ) _ { k , k - 1 }$ −can only change columns , which may be nonzero. Since multiplying $k$ and $k + 1$ in forming $Q _ { k + 1 } = P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k } ^ { t } P _ { k + 1 } ^ { t }$ $Q _ { k }$ by the rotation , we only need to consider the entries $( Q _ { k + 1 } ) _ { i , k }$ and $( Q _ { k + 1 } ) _ { i , k + 1 }$ , for $i = k { + } 2 , \ldots , n$ . First, we have

$$
( Q _ { k + 1 } ) _ { i , k } = \sum _ { j = 1 } ^ { n } ( Q _ { k } ) _ { i , j } \left( P _ { k + 1 } ^ { t } \right) _ { j , k } = ( Q _ { k } ) _ { i , k } c _ { k + 1 } + ( Q _ { k } ) _ { i , k - 1 } s _ { k + 1 } .
$$

However, $( Q _ { k } ) _ { i , k } = 0$ for $i > k$ and $( Q _ { k } ) _ { i , k + 1 } = 0$ , for $i > k + 1$ . Thus, $( Q _ { k + 1 } ) _ { i , k } = 0$ , for $i \geq k + 2$ . Further,

$$
( Q _ { k + 1 } ) _ { i , k + 1 } = - ( Q _ { k } ) _ { i , k } s _ { k + 1 } + ( Q _ { k } ) _ { i , k + 1 } c _ { k + 1 } = 0 ,
$$

for $i \geq k + 2$ . Thus, $Q _ { k + 1 } = P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdot \cdot \cdot P _ { k + 1 } ^ { t }$ is upper triangular except for the entries in positions $( 2 , 1 )$ , $( 3 , 2 )$ , $\cdot \cdot \cdot$ , $( k , k - 1 ) , ( k + 1 , k )$ , which may be nonzero.

(c) From parts (a) and (b) and mathematical induction, it follows that the matrix $P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdots P _ { n } ^ { t }$ is upper triangular except that the entries in positions $( 2 , 1 )$ , $( 3 , 2 )$ , $\cdot \cdot \cdot$ , $( n , n - 1 )$ may be nonzero. Thus, the entries in positions $( i , j )$ , for $i \geq j + 2$ are zero, which means that $P _ { 2 } ^ { t } P _ { 3 } ^ { t } \cdots P _ { n } ^ { t }$ is an upper Hessenberg matrix.

Note: There is no material deleted here. Exercise 11 is placed on a separate page so that the alignment of the steps in the algorithm are easier to see.