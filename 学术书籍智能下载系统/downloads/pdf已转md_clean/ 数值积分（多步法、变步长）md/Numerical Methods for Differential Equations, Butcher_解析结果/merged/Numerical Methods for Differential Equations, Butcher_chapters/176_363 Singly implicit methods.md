# 363 Singly implicit methods

We consider methods for which the stage order $q$ and the order are related by $p = q = s$ . To make the methods cheaply implementable, we also assume that

$$
\sigma ( A ) = \{ \lambda \} .
$$

The detailed study of methods for which $A$ has a one-point spectrum and for which $q \geq p - 1$ began with Burrage (1978). The special case $q = p$ was further developed in Butcher (1979), and this led to the implementation of STRIDE described in Burrage, Butcher and Chipman (1980).

Given $q = p$ and (363a), there will be a constraint on the abscissae of the method. To explore this, write down the $C ( s )$ conditions

$$
\sum _ { j = 1 } ^ { s } a _ { i j } c _ { j } ^ { k - 1 } = \frac { 1 } { k } c _ { i } ^ { k } , \qquad i , k = 1 , 2 , \ldots , s ,
$$

or, more compactly,

$$
A c ^ { k - 1 } = \frac { 1 } { k } c ^ { k } , \qquad k = 1 , 2 , \ldots , s ,
$$

where $c ^ { k }$ denotes the component-by-component power.

We can now evaluate $A ^ { k - 1 } \mathbf { 1 }$ by induction. In fact,

$$
A ^ { k } \mathbf { 1 } = { \frac { 1 } { k ! } } c ^ { k } , \qquad k = 1 , 2 , \ldots , s ,
$$

because the case $k = 1$ is just (363b), also with $k = 1$ ; and the case $k > 1$ follows from (363c) with $k$ replaced by $k - 1$ and from (363b).

Because of (363a) and the Cayley–Hamilton theorem, we have

$$
( A - \lambda I ) ^ { s } = 0 .
$$

Laguerre polynomials $L _ { s }$ for degrees $s = 1 , 2 , \ldots , 8$   

<table><tr><td>S L(S）</td></tr><tr><td>1 1 -</td></tr><tr><td>2 1 1 + s</td></tr><tr><td>北 3 3 1 1 + 1-6 2-35-3 5</td></tr><tr><td>4 1 + 4</td></tr><tr><td>124524 5 1 1 + 1 m5 120 S</td></tr><tr><td>6 6 1 1 十 1 1 6 20 720</td></tr><tr><td>中 10336° 583524 7 s² 7 5 7 6 1 57 7 1 十 m 4 40 十 720 5040 1</td></tr><tr><td>2 8 14g2 五 1 8 + + 7 × 7 1 1 s 7 + 15 180 630</td></tr></table>

Post-multiply by $\mathbf { 1 }$ and expand using the binomial theorem, and we find

$$
\sum _ { i = 0 } ^ { s } \binom { s } { i } ( - \lambda ) ^ { s - i } A ^ { i } \mathbf { 1 } = \boldsymbol { 0 } .
$$

Using (363c), we find that

$$
\sum _ { i = 0 } ^ { s } \binom { s } { i } ( - \lambda ) ^ { s - i } \frac { 1 } { i ! } c ^ { i } = 0 .
$$

This must hold for each component separately so that, for $i = 1 , 2 , \dots , s$ , $c _ { i } / \lambda$ is a zero of

$$
\sum _ { i = 0 } ^ { s } { \binom { s } { i } } ( - 1 ) ^ { i } \frac { ( - \xi ) ^ { i } } { i ! } .
$$

However, this is just the Laguerre polynomial of degree $s$ , usually denoted by $L _ { s } ( \xi )$ , and it is known that all its zeros are real and positive. For convenience, expressions for these polynomials, up to degree 8, are listed in Table 363(I) and approximations to the zeros are listed in Table 363(II). We saw in Subsection 361 that for $\lambda = \xi ^ { - 1 }$ for the case of three doubly underlined zeros of orders 2 and 3, L-stability is achieved. Double underlining to show similar choices for other orders is continued in the table and these are the only possibilities that exist (Wanner, Hairer and Nørsett, 1978). This means that there are no L-stable methods $^ -$ and in fact there is not even an A-stable method $-$ with $s = p = 7$ or with $s = p > 8$ . Even though fully L-stable methods are confined to the eight cases indicated in this table, there are other choices of $\lambda = \xi ^ { - 1 }$ that give stability which is acceptable for many problems. In each of the values of $\xi$ for which there is a single underline, the method is $\mathrm { A } ( \alpha )$ -stable with $\alpha \geq 1 . 5 5 \approx 8 9 ^ { \circ }$ .

Zeros of Laguerre polynomials for degrees $s = 1 , 2 , \ldots , 8$   

<table><tr><td>S</td><td>$1,...,Ss</td><td></td><td></td><td></td></tr><tr><td>1</td><td>1.0000000000</td><td></td><td></td><td></td></tr><tr><td>2</td><td>0.5857864376</td><td>3.4142135624</td><td></td><td></td></tr><tr><td>3</td><td>0.4157745568</td><td>2.2942803603</td><td>6.2899450829</td><td></td></tr><tr><td>4</td><td>0.3225476896</td><td>1.7457611012</td><td>4.5366202969</td><td>9.3950709123</td></tr><tr><td>5</td><td>0.2635603197</td><td>1.4134030591</td><td>3.5964257710</td><td>7.0858100059</td></tr><tr><td>6</td><td>12.6408008443</td><td></td><td></td><td></td></tr><tr><td></td><td>0.2228466042</td><td>1.1889321017</td><td>2.9927363261</td><td>5.7751435691</td></tr><tr><td></td><td>9.8374674184</td><td>15.9828739806</td><td></td><td></td></tr><tr><td>7</td><td>0.1930436766</td><td>1.0266648953</td><td>2.5678767450</td><td>4.9003530845</td></tr><tr><td></td><td>8.1821534446</td><td>12.7341802918</td><td>19.3957278623</td><td></td></tr><tr><td>8</td><td>0.1702796323</td><td>0.9037017768</td><td>2.2510866299</td><td>4.2667001703</td></tr><tr><td></td><td>7.0459054024</td><td>10.7585160102</td><td>15.7406786413</td><td>22.8631317369</td></tr></table>

The key to the efficient implementation of singly implicit methods is the similarity transformation matrix that transforms the coefficient matrix to lower triangular form. Let $T$ denote the matrix with $( i , j )$ element

$$
t _ { i j } = L _ { j - 1 } ( \xi _ { i } ) , \qquad i , j = 1 , 2 , \ldots , s .
$$

The principal properties of $T$ and its relationship to $A$ are as follows:

Theorem 363A The $( i , j )$ element of $T ^ { - 1 }$ is equal to

$$
\frac { \xi _ { j } } { s ^ { 2 } L _ { s - 1 } ( \xi _ { j } ) ^ { 2 } } L _ { i - 1 } ( \xi _ { j } ) .
$$

Let $\widetilde { A }$ denote $T ^ { - 1 } A T$ ; then

$$
\widetilde { A } = \lambda \left[ \begin{array} { c c c c c c } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { - 1 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { - 1 } & { 1 } \end{array} \right] .
$$

Proof. To prove (363d), use the Christoffel–Darboux formula for Laguerre polynomials in the form

$$
\sum _ { k = 0 } ^ { s - 1 } L _ { k } ( x ) L _ { k } ( y ) = \frac s { x - y } \big ( L _ { s } ( y ) L _ { s - 1 } ( x ) - L _ { s } ( x ) L _ { s - 1 } ( y ) \big ) .
$$

For $i \neq j$ , substitute $x = \xi _ { i } , y = \xi _ { j }$ to find that rows $i$ and $j$ of $T$ are orthogonal. To evaluate the inner product of row $i$ with itself, substitute $y = \xi _ { i }$ and take the limit as $x \to \xi _ { i }$ . It is found that

$$
\sum _ { k = 0 } ^ { s - 1 } L _ { k } ( \xi _ { k } ) ^ { 2 } = - s L _ { s } ^ { \prime } ( \xi _ { i } ) L _ { s - 1 } ( \xi _ { i } ) = \frac { s ^ { 2 } L _ { s - 1 } ( \xi _ { i } ) ^ { 2 } } { \xi _ { i } } .
$$

The value of $T T ^ { \rvert }$ as a diagonal matrix with $( i , i )$ element given by (363f) is equivalent to (363d).

The formula for $\widetilde { A }$ is verified by evaluating

$$
\begin{array} { r l } { \displaystyle \sum _ { j = 1 } ^ { s } a _ { i j } L _ { k - 1 } ( \xi _ { j } ) = \sum _ { j = 1 } ^ { s } a _ { i j } L _ { k - 1 } ( c _ { j } / \lambda ) } \\ { = \displaystyle \int _ { 0 } ^ { \lambda \xi _ { i } } L _ { k - 1 } ( c _ { j } / \lambda ) d t } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } L _ { k - 1 } ( t ) d l } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } ( L _ { k - 1 } ^ { \prime } ( t ) - L _ { k } ^ { \prime } ( t ) ) d l } \\ { = \lambda \displaystyle \int _ { 0 } ^ { \xi _ { i } } ( L _ { k - 1 } ^ { \prime } ( t ) - L _ { k } ^ { \prime } ( t ) ) d t } \\ { = \lambda ( L _ { k - 1 } ( \xi _ { i } ) - L _ { k } ( \xi _ { i } ) ) d t , } \end{array}
$$

where we have used known properties of Laguerre polynomials. The value of this sum is equivalent to (363e). 

For convenience we sometimes write

$$
J = \left[ \begin{array} { l l l l l l } { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { \cdots } & { 1 } & { 0 } \end{array} \right] ,
$$

so that (363e) can be written

$$
{ \widetilde { A } } = \lambda ( I - J ) .
$$

We now consider the possible A-stability or L-stability of singly implicit methods. This hinges on the behaviour of the rational functions

$$
R ( z ) = { \frac { N ( z ) } { ( 1 - \lambda z ) ^ { s } } } ,
$$

where the degree of the polynomial $N ( z )$ is no more than $s$ , and where

$$
N ( z ) = \exp ( z ) ( 1 - \lambda z ) ^ { s } + O ( z ^ { s + 1 } ) .
$$

We can obtain a formula for $N ( z )$ as follows:

$$
N ( z ) = \sum _ { i = 0 } ^ { s - i } ( - \lambda ) ^ { i } L _ { s } ^ { ( s - i ) } \left( \frac { 1 } { \lambda } \right) z ^ { i } ,
$$

where $L _ { n } ^ { ( m ) }$ denotes the $m$ -fold derivative of $L _ { n }$ , rather than a generalized Laguerre polynomial. To verify the L-stability of particular choices of $s$ and $\lambda$ , we note that all poles of $N ( z ) / ( 1 - \lambda z ) ^ { s }$ are in the right half-plane. Hence, it is necessary only to test that $| D ( z ) | ^ { 2 } - | ( 1 - \lambda z ) ^ { s } | ^ { 2 } \ge 0$ , whenever $z$ is on the imaginary axis. Write $z = i y$ and we find the ‘E-polynomial’ defined in this case as

$$
E ( y ) = ( 1 + \lambda ^ { 2 } y ^ { 2 } ) ^ { s } - N ( i y ) N ( - i y ) ,
$$

with $E ( y ) \ge 0$ for all real $y$ as the condition for A-stability. Although Astability for $s = p$ is confined to the cases indicated in Table 363(II), it will be seen in the next subsection that higher values of $s$ can lead to additional possibilities.

We conclude this subsection by constructing the two-stage L-stable singly implicit method of order 2. From the formulae for the first few Laguerre polynomials,

$$
L _ { 0 } ( x ) = 1 , \quad L _ { 1 } ( x ) = 1 - x , \quad L _ { 2 } ( x ) = 1 - 2 x + \frac { 1 } { 2 } x ^ { 2 } ,
$$

we find the values of $\xi _ { 1 }$ and $\xi _ { 2 }$ , and evaluate the matrices $T$ and $T ^ { - 1 }$ . We have

$$
\xi _ { 1 } = 2 - \sqrt { 2 } , \qquad \xi _ { 2 } = 2 + \sqrt { 2 }
$$

and

$$
\begin{array} { r } { \mathrm { ~  ~ { ~ \sigma ~ } ~ } ^ { \prime } = \left[ \begin{array} { l l } { L _ { 0 } ( \xi _ { 1 } ) } & { L _ { 1 } ( \xi _ { 1 } ) } \\ { L _ { 0 } ( \xi _ { 2 } ) } & { L _ { 1 } ( \xi _ { 2 } ) } \end{array} \right] = \left[ \begin{array} { l l } { 1 } & { - 1 + \sqrt { 2 } } \\ { 1 } & { - 1 - \sqrt { 2 } } \end{array} \right] , \quad T ^ { - 1 } = \left[ \begin{array} { l l } { \frac { 1 } { 2 } + \frac { \sqrt { 2 } } { 4 } } & { \frac { 1 } { 2 } - \frac { \sqrt { 2 } } { 4 } } \\ { \frac { \sqrt { 2 } } { 4 } } & { - \frac { \sqrt { 2 } } { 4 } } \end{array} \right] . } \end{array}
$$

For L-stability, choose $\begin{array} { r } { \lambda = \xi _ { 2 } ^ { - 1 } = 1 - \frac { 1 } { 2 } \sqrt { 2 } } \end{array}$ , and we evaluate $A = \lambda T ( I - J ) T ^ { - 1 }$ to give the tableau

$$
{ \frac { 3 - 2 { \sqrt { 2 } } } { 1 } } { \frac { \frac { 5 } { 4 } - { \frac { 3 } { 4 } } { \sqrt { 2 } } } { \frac { 1 } { 4 } + { \frac { 1 } { 4 } } { \sqrt { 2 } } } } { \frac { \frac { 7 } { 4 } - { \frac { 5 } { 4 } } { \sqrt { 2 } } } { \frac { 1 } { 4 } - { \frac { 1 } { 4 } } { \sqrt { 2 } } } }  .
$$

In the implementation of this, or any other, singly implicit method, the actual entries in this tableau are not explicitly used. To emphasize this point, we look in detail at a single Newton iteration for this method. Let $M = I - h \lambda f ^ { \prime } ( y _ { n - 1 } )$ . Here the Jacobian matrix $f ^ { \prime }$ is supposed to have been evaluated at the start of the current step. In practice, a Jacobian evaluated at an earlier time value might give satisfactory performance, but we do not dwell on this point here. If the method were to be implemented with no special use made of its singly implicit structure, then we would need, instead of the $N \times N$ matrix $M$ , a $2 N \times 2 N$ matrix $\widetilde { M }$ given by

$$
\widetilde { \cal M } = \left[ \begin{array} { c c } { { I - h a _ { 1 1 } f ^ { \prime } ( y _ { n - 1 } ) } } & { { - h a _ { 1 2 } f ^ { \prime } ( y _ { n - 1 } ) } } \\ { { - h a _ { 2 1 } f ^ { \prime } ( y _ { n - 1 } ) } } & { { I - h a _ { 2 2 } f ^ { \prime } ( y _ { n - 1 } ) } } \end{array} \right] .
$$

In this ‘fully implicit’ situation, a single iteration would start with the input approximation $y _ { n - 1 }$ and existing approximations to the stage values and stage derivatives $Y _ { 1 }$ , $Y _ { 2 }$ , $h F _ { 1 }$ and $h F _ { 2 }$ . It will be assumed that these are consistent with the requirements that

$$
Y _ { 1 } = y _ { n - 1 } + a _ { 1 1 } h F _ { 1 } + a _ { 1 2 } h F _ { 2 } , \quad Y _ { 2 } = y _ { n - 1 } + a _ { 2 1 } h F _ { 1 } + a _ { 2 2 } h F _ { 2 } ,
$$

and the iteration process will always leave these conditions intact.
