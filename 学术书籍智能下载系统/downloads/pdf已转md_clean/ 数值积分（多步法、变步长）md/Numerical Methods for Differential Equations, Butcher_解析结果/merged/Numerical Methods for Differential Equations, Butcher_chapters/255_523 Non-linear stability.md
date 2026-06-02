# 523 Non-linear stability

We will consider an example of an A-stable linear multistep method based on the function

$$
( 1 - z ) w ^ { 2 } + ( - { \textstyle \frac { 1 } { 2 } } + { \textstyle \frac { 1 } { 4 } } z ) w + ( - { \textstyle \frac { 1 } { 2 } } - { \textstyle \frac { 3 } { 4 } } z ) .
$$

As a linear multistep method this is

$$
[ \begin{array} { c c c c }  { 1  { \begin{array} { c c c c } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { - \frac { 1 } { 4 } } } & { { \frac { 3 } { 4 } } } \\ { { 1  { \begin{array} { c c c c } { { \frac { 1 } { 2 } } } & { { \frac { 1 } { 2 } } } & { { - \frac { 1 } { 4 } } } & { { \frac { 3 } { 4 } } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } \end{array} }  } } , } \end{array} ] } , \end{array}
$$

where the input to step $n$ consists of the vectors $y _ { n - 1 } , y _ { n - 2 } , h f ( y _ { n - 1 } ) , h f ( y _ { n - 2 } )$ , respectively.

To understand the behaviour of this type of method with a dissipative problem, Dahlquist (1976) analysed the corresponding one-leg method. However, with the general linear formulation, the analysis can be carried out directly. We first carry out a transformation of the input and output variables to the form

$$
\left[ \begin{array} { c c } { { A } } & { { U T ^ { - 1 } } } \\ { { T B } } & { { T V T ^ { - 1 } } } \end{array} \right] ,
$$

where

$$
T = \left[ { \begin{array} { r r r r r } { { \frac { 2 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 3 } } } & { { \frac { 1 } { 2 } } } \\ { { \frac { 1 } { 3 } } } & { { - \frac { 1 } { 3 } } } & { { \frac { 7 } { 6 } } } & { { - \frac { 1 } { 2 } } } \\ { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \end{array} } \right] .
$$

The resulting method is found to be

$$
[ { \begin{array} { r r r r r } { 1 } & { { | \ 1 } & { { \ } - { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { { \frac { 3 } { 2 } } } & { 1 } & { - { \frac { 1 } { 2 } } } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 0 } \end{array} } ] } \ .
$$

Because the first two output values in the transformed formulation do not depend in any way on the final two input values, these values, and the final two output values, can be deleted from the formulation. Thus, we have the reduced method

$$
[ { \frac { 1 } { 1 } } | { \begin{array} { r r } { 1 } & { - { \frac { 1 } { 2 } } } \\ { 1 } & { 0 } \\ { { \frac { 3 } { 2 } } } \end{array} } ] .
$$

From the coefficients in the first two rows of $T$ , we identify the inputs in (523a) with specific combinations of the input values in the original formulation:

$$
\begin{array} { r } { y _ { 1 } ^ { [ n - 1 ] } = \frac { 2 } { 3 } y _ { n - 1 } + \frac { 1 } { 3 } y _ { n - 2 } + \frac { 1 } { 3 } h f ( y _ { n - 1 } ) + \frac { 1 } { 2 } h f ( y _ { n - 2 } ) , } \\ { y _ { 2 } ^ { [ n - 1 ] } = \frac { 1 } { 3 } y _ { n - 1 } - \frac { 1 } { 3 } y _ { n - 2 } + \frac { 7 } { 6 } h f ( y _ { n - 1 } ) - \frac { 1 } { 2 } h f ( y _ { n - 2 } ) . } \end{array}
$$

Stable behaviour of this method with a dissipative problem hinges on the verifiable identity

$$
\begin{array} { r l r } {  { \| y _ { 1 } ^ { n } \| ^ { 2 } + \frac { 1 } { 3 } \| y _ { 2 } ^ { [ n ] } \| ^ { 2 } = \| y _ { 1 } ^ { n - 1 ] } \| ^ { 2 } + \frac { 1 } { 3 } \| y _ { 2 } ^ { [ n - 1 ] } \| ^ { 2 } } } \\ & { } & { + 2 \langle h f ( Y ) , Y \rangle - \frac { 1 } { 4 } \| y _ { 2 } ^ { [ n - 1 ] } - h f ( Y ) \| ^ { 2 } . } \end{array}
$$

This means that if $2 \langle h f ( Y ) , Y \rangle ~ \leq ~ 0$ , then $\| y ^ { [ n ] } \| _ { G } ~ \leq ~ \| y ^ { [ n - 1 ] } \| _ { G }$ , where $G = \mathrm { d i a g } ( 1 , { \textstyle { \frac { 1 } { 3 } } } )$ .

Given an arbitrary general linear method, we ask when a similar analysis can be performed. It is natural to restrict ourselves to methods without unnecessary inputs, outputs or stages; such irreducible methods are discussed in Butcher (1987a).

As a first step we consider how to generalize the use of the $G$ norm. Let $G$ denote an $r \times r$ positive semi-definite matrix. For $u , v \in \mathbb { R } ^ { r N }$ made up from subvectors $u _ { 1 } , u _ { 2 } , \ldots , u _ { r } \in \mathbb { R } ^ { N }$ , $v _ { 1 } , v _ { 2 } , \ldots , v _ { r } \in \mathbb { R } ^ { N }$ , respectively, define $\langle \cdot , \cdot \rangle _ { G }$ and the corresponding semi-norm $\| \cdot \| _ { G }$ as

$$
\begin{array} { c } { { \displaystyle { \langle u , v \rangle _ { G } = \sum _ { i , j = 1 } ^ { r } g _ { i j } \langle u _ { i } , v _ { j } \rangle } , } } \\ { { \| u \| _ { G } ^ { 2 } = \langle u , u \rangle _ { G } . } } \end{array}
$$

We will also need to consider vectors $U \oplus u \in \mathbb { R } ^ { ( s + r ) N }$ , made up from subvectors $U _ { 1 } , U _ { 2 } , \dots , U _ { s } , u _ { 1 } , u _ { 2 } , \dots , u _ { r } \in \mathbb { R } ^ { N }$ . Given a positive semi-definite $( s + t ) \times ( s + r )$ matrix $M$ , we will define $\| U \oplus u \| _ { M }$ in a similar way. Given a diagonal $s \times s$ matrix $D$ , with diagonal elements $d _ { i } ~ \geq ~ 0$ , we will also write $\langle U , V \rangle _ { D }$ as $\textstyle \sum _ { i = 1 } ^ { s } d _ { i } \langle U _ { i } , V _ { i } \rangle$ . Using this terminology we have the following result:

Theorem 523A Let $Y$ denote the vector of stage values, $F$ the vector of stage derivatives and $y ^ { [ n - 1 ] }$ and $y ^ { \lfloor n \rfloor }$ the input and output respectively from a single step of a general linear method $( A , U , B , V )$ . Assume that $M$ is $a$ positive semi-definite $( s + r ) \times ( s + r )$ matrix, where

$$
M = \left[ \begin{array} { c c } { { D A + A ^ { \top } D - B ^ { \top } G B } } & { { D U - B ^ { \top } G V } } \\ { { U ^ { \top } D - V ^ { \top } G B } } & { { G - V ^ { \top } G V } } \end{array} \right] ,
$$

with $G$ a positive semi-definite $r \times r$ matrix and $D$ a positive semi-definite diagonal $s \times s$ matrix. Then

$$
\| y ^ { [ n ] } \| _ { G } ^ { 2 } = \| y ^ { [ n - 1 ] } \| _ { G } ^ { 2 } + 2 \langle h F , Y \rangle _ { D } - \| h F \oplus y ^ { [ n - 1 ] } \| _ { M } ^ { 2 } .
$$

Proof. The result is equivalent to the identity

$$
M = \left[ 0 \quad 0 \right] - \left[ B ^ { \intercal } \right] G \left[ B \quad V \right] + \left[ D \right] \left[ A \quad U \right] + \left[ A ^ { \intercal } \right] \left[ D \quad 0 \right] .
$$

We are now in a position to extend the algebraic stability concept to the general linear case.

Theorem 523B If $M$ given by (523b) is positive semi-definite, then

$$
\| y ^ { [ n ] } \| _ { G } ^ { 2 } \leq \| y ^ { [ n - 1 ] } \| _ { G } ^ { 2 } .
$$

524 Reducible linear multistep methods and $G$ -stability

We consider the possibility of analysing the possible non-linear stability of linear multistep methods without using one-leg methods. First note that a linear $k$ -step method, written as a general linear method with $r = 2 k$ inputs, is reducible to a method with only $k$ inputs. For the standard $k$ -step method written in the form (400b), we interpret $h f ( x _ { n - i } , y _ { n - i } )$ , $i = 1 , 2 , \ldots , k$ , as having already been evaluated from the corresponding $y _ { n - i }$ . Define the input vector $y ^ { [ n - 1 ] }$ by

$$
y _ { i } ^ { [ n - 1 ] } = \sum _ { j = i } ^ { k } { \bigl ( } \alpha _ { j } y _ { n - j + i - 1 } + \beta _ { j } h f ( x _ { n - j + i } , y _ { n - j + i - 1 } ) { \bigr ) } , \quad i = 1 , 2 , \ldots , k ,
$$

so that the single stage $Y = y _ { n }$ satisfies

$$
Y = h \beta _ { 0 } f ( x _ { n } , Y ) + y _ { 1 } ^ { [ n - 1 ] }
$$

and the output vector can be found from

$$
y _ { i } ^ { [ n ] } = \alpha _ { i } y _ { 1 } ^ { [ n - 1 ] } + y _ { i + 1 } ^ { [ n ] } + ( \beta _ { 0 } \alpha _ { i } + \beta _ { i } ) h f ( x _ { n } , Y ) ,
$$

where the term y [n]i+1 is omitted when $i ~ = ~ k$ . The reduced method has the defining matrices

$$
\left[ \begin{array} { c c } { A } & { U } \\ { B } & { V } \end{array} \right] = \left[ \begin{array} { c } { \beta _ { 0 } } \\ { \beta _ { 0 } \alpha _ { 1 } + \beta _ { 1 } } \\ { \beta _ { 0 } \alpha _ { 2 } + \beta _ { 2 } } \\ { \beta _ { 0 } \alpha _ { 3 } + \beta _ { 3 } } \\ { \vdots } \\ { \beta _ { 0 } \alpha _ { k - 1 } + \beta _ { k - 1 } } \\ { \beta _ { 0 } \alpha _ { k } + \beta _ { k } } \end{array} \right] \left[ \begin{array} { c c c c c c } { 1 } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \alpha _ { 1 } } & { 1 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \alpha _ { 2 } } & { 0 } & { 1 } & { \cdots } & { 0 } & { 0 } \\ { \alpha _ { 3 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \\ { \vdots } & { \vdots } & { \vdots } & & { \vdots } & { \vdots } \\ { \alpha _ { k - 1 } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 1 } \\ { \alpha _ { k } } & { 0 } & { 0 } & { \cdots } & { 0 } & { 0 } \end{array} \right] ,
$$

and was shown in Butcher and Hill (2006) to be algebraically stable if it is A-stable.
