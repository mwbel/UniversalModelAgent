# 545 Fourth order, four-stage ARK methods

We write specific coefficients of the method as shown in the tableau

$$
\left[ \begin{array} { c c c c c c c } { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { a _ { 2 1 } } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { u _ { 1 2 } } } & { { u _ { 1 3 } } } \\ { { a _ { 3 1 } } } & { { a _ { 3 2 } } } & { { 0 } } & { { 0 } } & { { 1 } } & { { u _ { 2 2 } } } & { { u _ { 2 3 } } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { 0 } } & { { 0 } } & { { 1 } } & { { b _ { 0 } } } & { { 0 } } \\ { { b _ { 1 } } } & { { b _ { 2 } } } & { { b _ { 3 } } } & { { 0 } } & { { 0 } } & { { 1 } } & { { b _ { 0 } } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { \beta _ { 1 } } } & { { \beta _ { 2 } } } & { { \beta _ { 3 } } } & { { \beta _ { 4 } } } & { { \beta _ { 0 } } } & { { 0 } } & { { 0 } } \end{array} \right] .
$$

As usual, $c$ will denote the abscissa vector. We also write $b ^ { \intercal } = \left[ b _ { 1 } \quad b _ { 2 } \quad b _ { 3 } \quad 0 \right]$ and $\beta ^ { 1 } = [ \beta _ { 1 } , \quad \beta _ { 2 } \quad \beta _ { 3 } \quad \beta _ { 4 } ]$ .

As in the example method discussed in Subsection 543, the input approximations will be of the form $y ( x _ { n - 1 } ) + O ( h ^ { 5 } )$ , $h y ^ { \prime } ( x _ { n - 1 } ) + O ( h ^ { 5 } )$ and $h ^ { 2 } y ^ { \prime \prime } ( x _ { n - 1 } ) + O ( h ^ { 3 } )$ , The crucial assumptions we will make are that each of the stages is computed with order at least 2, and that the three output values are not affected by order 3 perturbations in the third input approximation. For stage order 2 it is necessary and sufficient that the matrix $U$ should have the form

$$
U = [ { \bf 1 } c - A { \bf 1 } \frac { 1 } { 2 } c ^ { 2 } - A c ] .
$$

Since $u _ { 4 2 } = b _ { 0 }$ , this will mean that $b ^ { \mathsf { I } } \mathbf { 1 } + b _ { 0 } = 1$ . The conditions for order 4 on the first output component yield the equations

$$
\begin{array} { r } { b ^ { \top } c = \frac { 1 } { 2 } , } \\ { b ^ { \top } c ^ { 2 } = \frac { 1 } { 3 } , } \\ { b ^ { \top } c ^ { 3 } = \frac { 1 } { 4 } , } \\ { b ^ { \top } A c ^ { 2 } = \frac { 1 } { 1 2 } , } \\ { b ^ { \top } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \end{array}
$$

where (545e) is included to ensure that an $O ( h ^ { 3 } )$ error in the third input vector does not detract from the order 4 behaviour. Combining (545b) and (545e), we find

$$
\begin{array} { r } { b ^ { \intercal } A c = \frac { 1 } { 6 } . } \end{array}
$$

Either (545e) or the equivalent condition (545f), together with the related condition on $\beta ^ { 1 }$ given in (545i) below, will be referred to as ‘annihilation conditions’. The vector $\beta ^ { \intercal }$ , together with $\beta _ { 0 }$ , defines the third output approximation, which is required to give the result $h ^ { 2 } y ^ { \prime \prime } ( x _ { n } ) + O ( h ^ { 3 } )$ . Hence,

$$
\begin{array} { r } { \beta ^ { \mathsf { T } } \mathbf { 1 } + \beta _ { 0 } = 0 , } \\ { \beta ^ { \mathsf { T } } c = 1 . } \end{array}
$$

We now turn to the conditions for RK stability. If the stability matrix

$$
M ( z ) = V + z B U + z ^ { 2 } B A U + z ^ { 3 } B A ^ { 2 } U + z ^ { 4 } B A ^ { 3 } U
$$

is of $M ( z )$ e only a single non-zero eige and for order 4 must equal $\begin{array} { r } { 1 + z + \frac { 1 } { 2 } z ^ { 2 } + \frac { 1 } { 6 } z ^ { 3 } + \frac { 1 } { 2 4 } z ^ { 4 } } \end{array}$ st. tracerefore impose the conditions that the traces of $B U$ , $B A U$ , $B A ^ { 2 } U$ and $B A ^ { 3 } U$ values $^ { 1 }$ , $\textstyle { \frac { 1 } { 2 } }$ , $\textstyle { \frac { 1 } { 6 } }$ , $\textstyle { \frac { 1 } { 2 4 } }$ , respectively. These can be written in the form

$$
\begin{array} { r } { \beta ^ { \top } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 . } \\ { \beta ^ { \top } A ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { \beta ^ { \top } A ^ { 2 } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = 0 , } \\ { b ^ { \top } A ^ { 2 } c + \beta ^ { \top } A ^ { 3 } ( \frac { 1 } { 2 } c ^ { 2 } - A c ) = \frac { 1 } { 2 4 } . } \end{array}
$$

Because $A ^ { 4 } = 0$ , (545l) simplifies to

$$
b ^ { \mathsf { T } } A ^ { 2 } c = { \frac { 1 } { 2 4 ( 1 + { \frac { 1 } { 2 } } \beta _ { 4 } c _ { 1 } ) } } .
$$

We now show that $\beta ^ { \sf I }$ satisfies the equation

$$
\beta _ { 4 } e _ { 4 } ^ { \mathsf { T } } = \beta ^ { \mathsf { T } } ( I + \beta _ { 4 } A ) .
$$

This follows by observing that $\beta _ { 4 } e _ { 4 } ^ { \mathsf { I } } - \beta ^ { \mathsf { I } } ( I + \beta _ { 4 } A )$ multiplied respectively by $e _ { 4 }$ , ${ \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c$ , $A ( \scriptstyle { \frac { 1 } { 2 } } c ^ { 2 } - A c )$ and $A ^ { 2 } ( { \textstyle { \frac { 1 } { 2 } } } c ^ { 2 } - A c )$ are each zero if and only if each of (545j), (545k) and (545l) holds.

Multiply each side of (545n) by $( I + \beta _ { 4 } A ) ^ { - 1 } c$ and use (545h) to show that

$$
1 = \beta _ { 4 } - \frac { 1 } { 2 } \beta _ { 4 } ^ { 2 } + \frac { 1 } { 6 } \beta _ { 4 } ^ { 3 } - \frac { \beta _ { 4 } ^ { 4 } } { 2 4 ( 1 + \frac { 1 } { 2 } \beta _ { 4 } c _ { 1 } ) } ,
$$

from which it follows that

$$
c _ { 1 } = \frac { - 2 ( 1 - \beta _ { 4 } + \frac { 1 } { 2 } \beta _ { 4 } ^ { 2 } - \frac { 1 } { 6 } \beta _ { 4 } ^ { 3 } + \frac { 1 } { 2 4 } \beta _ { 4 } ^ { 4 } ) } { \beta _ { 4 } ( 1 - \beta _ { 4 } + \frac { 1 } { 2 } \beta _ { 4 } ^ { 2 } - \frac { 1 } { 6 } \beta _ { 4 } ^ { 3 } ) } .
$$

To construct a four-stage fourth order ARK method in detail, carry out the following steps:

1. Choose the value of $\beta _ { 4 }$ .   
2. Evaluate $c _ { 1 }$ from (545o).   
3. Choose values of $c _ { 2 }$ and $c _ { 3 }$ .   
4. Evaluate $b _ { 0 }$ , $b _ { 1 }$ , $b _ { 2 }$ , $b _ { 3 }$ to satisfy (545a), (545b), (545c), (545g).   
5. Evaluate $a _ { 2 1 }$ , $a _ { 3 1 }$ , $a _ { 3 2 }$ to satisfy (545f), (545d), (545m).   
6. Evaluate the remaining elements of $\beta ^ { \mathsf { T } }$ from (545n).   
7. Evaluate the elements of $U$ and $V$ .

In contrast to the method given in (505a), the following method has the same $c = [ 1 \quad { \scriptstyle { \frac { 1 } { 2 } } } \quad { \scriptstyle { \frac { 1 } { 2 } } } \quad 1 ] ^ { \intercal }$ but different $b ^ { \top }$ :

<table><tr><td>0 0 1 0 16 1 16</td><td>0 0 1 0</td><td>0 1 0 1 0 1</td><td>1 7 16 7 16</td><td>1-21-165 16</td></tr><tr><td>1</td><td>1</td><td>1 0 1 0</td><td>1 1 1 1</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td></td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0 0</td><td>0</td></tr><tr><td></td><td>4</td><td>4 2</td><td>0 -1</td><td>0</td></tr></table>

A further example with $\begin{array} { r } { c = [ \frac { 1 1 } { 2 4 } \frac { 1 3 } { 2 4 } 1 1 1 ] ^ { ! } } \end{array}$ is given by the matrix

<table><tr><td rowspan=1 colspan=1>0      0      0     0</td><td rowspan=1 colspan=1>11         121124        1152</td></tr><tr><td rowspan=1 colspan=1>104     0      0     0297</td><td rowspan=1 colspan=1>1    455        1432376      10368</td></tr><tr><td rowspan=1 colspan=1>1820    44      0     04653    47</td><td rowspan=1 colspan=1>1523       47314653       2538</td></tr><tr><td rowspan=1 colspan=1>48     48     47    0143    143    286</td><td rowspan=1 colspan=1>1     47         0286</td></tr><tr><td rowspan=1 colspan=1>48     48     47    0143    143    286</td><td rowspan=1 colspan=1>1     47         0286</td></tr><tr><td rowspan=1 colspan=1>0      0      0     1</td><td rowspan=1 colspan=1>0     0          0</td></tr><tr><td rowspan=1 colspan=1>354    162    423    3143    143    286</td><td rowspan=1 colspan=1>51         00286</td></tr></table>

These methods were introduced in Butcher (1997, 1998). Although it does not seem possible to find similar methods with $s = p$ stages where $p > 4$ , we will see in the next subsection that something very similar can be achieved.
