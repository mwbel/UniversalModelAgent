# 306 Taylor’s theorem

We start from the identity,

$$
\begin{array} { r } { f ( a + \delta ) = f ( a ) + f ^ { \prime } ( a ) ( \delta ) + \frac { 1 } { 2 ! } f ^ { \prime \prime } ( a ) ( \delta , \delta ) \qquad } \\ { + \dots + \displaystyle \frac { 1 } { n ! } f ^ { ( n ) } ( a ) ( \delta , \delta , \dots , \delta ) + R _ { n } , } \end{array}
$$

where the ‘remainder’ $R _ { n }$ is given by

$$
R _ { n } = \frac { 1 } { n ! } \int _ { 0 } ^ { 1 } f ^ { ( n + 1 ) } ( a + \xi \delta ) ( \delta , \delta , \ldots , \delta ) ( 1 - \xi ) ^ { n } d \xi .
$$

This is proved by induction, with the key step being

$$
R _ { n - 1 } = \frac { 1 } { n ! } f ^ { ( n ) } ( a ) ( \delta , \delta , \dots , \delta ) + R _ { n } ,
$$

which is verified by integration by parts. With Taylor’s theorem written in the form (306a), the result is quite versatile and applies if $f : X \subset \mathbb { R } ^ { M } \to \mathbb { R } ^ { N }$ , where $a + \xi \delta \in O \subset X$ , for all $\xi \in [ 0 , 1 ]$ . Assuming that $\| f ^ { ( n + 1 ) } ( x ) \|$ exists and is bounded for $x \in O$ , then

$$
\| R _ { n } \| = O ( \| \delta \| ^ { n + 1 } ) .
$$

We consider a slight variation of the theorem, in which $\delta$ is replaced by the sum of a finite number of vectors, $\delta _ { i }$ , $i = 1 , 2 , \dots , m$ . We assume that $f$ is analytic in a neighbourhood of $a$ and that each of the $\delta _ { i }$ is small. The formal result we present can be interpreted as a finite series, together with remainder, with the details dependent on the relative magnitudes of the $\delta _ { i }$ . Let $I$ denote a sequence of integers from the set $\{ 1 , 2 , \ldots , m \}$ and $\mathcal { L } _ { m }$ the set of all such sequences. Two sequences $I$ and $I ^ { \prime }$ will be regarded as identical if the members of $I ^ { \prime }$ are a permutation of the members of $I$ . The ‘symmetry’ of $I$ is the order of the group of permutations of the elements of $\{ 1 , 2 , \ldots , \# I \}$ , which maps the ordered members of $I$ to themselves. That is, if $I$ contains $k _ { i }$ occurrences of $i$ , for each $i = 1 , 2 , \dots , m$ , then

$$
\sigma ( I ) = k _ { 1 } ! k _ { 2 } ! \cdot \cdot \cdot k _ { m } ! .
$$

For $m = 2$ , the first few $I \in \mathcal { I } _ { m }$ , together with the corresponding symmetries, are given in Table 306(I).

For $I = ( i _ { 1 } , i _ { 2 } , \ldots , i _ { k } ) \in { \mathcal { T } } _ { m }$ , we denote by $\delta _ { I }$ the quantity

$$
( \delta _ { i _ { 1 } } , \delta _ { i _ { 2 } } , \ldots , \delta _ { i _ { m } } ) \in ( \mathbb { R } ^ { N } ) ^ { m } .
$$

These will be used as operands for multilinear operators, such as $f ^ { ( m ) } ( a )$ , and, in the case $I = ( )$ , we interpret $f ( a ) ( )$ as being simply $f ( a )$ . We are now in a position to state the form of the Taylor expansion (306a), when $\delta$ is replaced by $\textstyle \sum _ { i = 1 } ^ { \cdot { m } } \delta _ { i }$ .

Theorem 306A

$$
f \biggl ( a + \sum _ { i = 1 } ^ { m } \delta _ { i } \biggr ) = \sum _ { I \in \mathcal { T } _ { m } } \frac { 1 } { \sigma ( I ) } f ^ { ( \# I ) } ( a ) \delta _ { I } .
$$

Proof. Continue to write $k _ { i }$ for the number of occurrences of $i$ in $I$ , so that $\sigma ( I )$ is given by (306b). The coefficient of $f ^ { ( \# I ) } ( a ) \delta _ { I }$ is equal to the coefficient of $\textstyle \prod _ { i = 1 } ^ { m } x ^ { k _ { i } }$ in $\textstyle \exp \left( \sum _ { i = 1 } ^ { m } x _ { i } \right)$ . This equals the coefficient of $\textstyle \prod _ { i = 1 } ^ { m } x ^ { k _ { i } }$ in

$$
\begin{array} { r } { \left( 1 + x _ { 1 } + \frac { 1 } { 2 ! } x _ { 1 } ^ { 2 } + \cdot \cdot \cdot \right) \left( 1 + x _ { 2 } + \frac { 1 } { 2 ! } x _ { 2 } ^ { 2 } + \cdot \cdot \cdot \right) \cdot \cdot \left( 1 + x _ { m } + \frac { 1 } { 2 ! } x _ { m } ^ { 2 } + \cdot \cdot \cdot \right) } \end{array}
$$

and is equal to $1 / \sigma ( I )$ .

We illustrate this result by applying (306A) to the case $m = 2$ , using Table 306(I):

$$
\begin{array} { r l } & { f ( a + \delta _ { 1 } + \delta _ { 2 } ) = f ( a ) + f ^ { \prime } ( a ) \delta _ { 1 } + f ^ { \prime } ( a ) \delta _ { 2 } + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } ) } \\ & { \qquad + f ^ { \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 2 } ) + \frac { 1 } { 2 } f ^ { \prime \prime } ( a ) ( \delta _ { 2 } , \delta _ { 2 } ) + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } , \delta _ { 1 } ) } \\ & { \qquad + \frac { 1 } { 2 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 1 } , \delta _ { 2 } ) + \frac { 1 } { 2 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 1 } , \delta _ { 2 } , \delta _ { 2 } ) + \frac { 1 } { 6 } f ^ { \prime \prime \prime } ( a ) ( \delta _ { 2 } , \delta _ { 2 } , \delta _ { 2 } ) + \cdots \ . } \end{array}
$$

# Exercises 30

30.1 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = | \mathbf { t } |$ , where $| \mathbf { t } | = ( V , E )$ , with

$$
V = \{ a , b , c , d , e , f , g \} \mathrm { ~ a n d ~ } E = \{ ( a , b ) , ( b , c ) , ( b , d ) , ( a , e ) , ( e , f ) , ( e , g ) \} .
$$

30.2 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = [ [ \tau ] ^ { 2 } \tau ^ { 3 } ]$ .

30.3 Find $r ( t ) , \sigma ( t ) , \gamma ( t ) , \alpha ( t )$ and $\beta ( t )$ for the tree $t = \tau \tau \cdot ( \tau \tau \cdot \tau ) \tau$ .

30.4 Define $f : \mathbb { R } ^ { 3 } \longrightarrow \mathbb { R } ^ { 3 }$ by

$$
f ( y ^ { 1 } , y ^ { 2 } , y ^ { 3 } ) = \left[ \begin{array} { c } { { y ^ { 1 } + y ^ { 2 } y ^ { 3 } } } \\ { { ( y ^ { 1 } ) ^ { 2 } + 2 y ^ { 1 } y ^ { 2 } } } \\ { { 1 + ( y ^ { 2 } + y ^ { 3 } ) ^ { 2 } } } \end{array} \right] .
$$

Find formulae for $f _ { j } ^ { i }$ , $f _ { j k } ^ { i }$ and $f _ { j k l } ^ { \imath }$ , for $i , j , k , l = 1 , 2 , 3$ .

30.5 Expand $f ( a + \delta _ { 1 } \xi + \delta _ { 2 } \xi ^ { 2 } + \delta _ { 3 } \xi ^ { 3 } )$ up to terms in $\xi ^ { 3 }$ using Theorem 306A.
